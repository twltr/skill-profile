#!/usr/bin/env python3
"""Check a skill collection against the tree rules in references/skill-architecture.md.

Usage: check_tree.py ROOT [--strict]

ROOT is the collection's `skills/` directory, laid out as `ROOT/<group>/<skill>/`
with the groups `core`, `extras` and one folder per domain tree. Two levels:

- ERROR blocks installation: a missing or unknown `metadata.skill-type`, or a
  `skill-requires` child that does not exist or lives in another tree.
- RULE reports a break of the architecture: invocation policy or folder that
  contradicts the type, an edge into another tree, a child naming its routing
  parent, a leaf or core skill naming a tree skill.

Exit status: 1 when an ERROR exists, or a RULE exists with --strict; else 0.
Edges come from skill_graph.py and count mentions, not proven calls, so read a
RULE as a place to inspect. Needs PyYAML.
"""
import sys
from pathlib import Path

import yaml

# Installed skill folders must stay byte-identical to their source; no __pycache__ beside the scripts.
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_graph  # noqa: E402  (sibling script, shares alias and edge detection)

TYPES = {"core", "domain", "parent", "flow", "leaf"}
IMPLICIT = {"core", "domain"}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    end = text.index("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}


def implicit_policy(directory):
    # The shared invocation policy lives in agents/openai.yaml; absent means implicit.
    metadata = directory / "agents" / "openai.yaml"
    if not metadata.exists():
        return True
    data = yaml.safe_load(metadata.read_text(encoding="utf-8")) or {}
    return (data.get("policy") or {}).get("allow_implicit_invocation", True) is not False


def main(argv):
    strict = "--strict" in argv
    roots = [arg for arg in argv if not arg.startswith("--")]
    if len(roots) != 1:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    root = Path(roots[0])
    skills = {}
    for path in sorted(root.glob("*/*/SKILL.md")):
        data = (frontmatter(path).get("metadata") or {})
        skills[path.parent.name] = {
            "group": path.parent.parent.name,
            "type": data.get("skill-type"),
            "tree": data.get("skill-tree"),
            "requires": (data.get("skill-requires") or "").split(),
            "implicit": implicit_policy(path.parent),
        }
    errors, rules = [], []

    for name, s in skills.items():
        group, kind = s["group"], s["type"]
        if kind not in TYPES:
            errors.append(f"{name}: skill-type is {kind!r}, expected one of {sorted(TYPES)}")
            continue
        if s["implicit"] != (kind in IMPLICIT):
            want = "implicit" if kind in IMPLICIT else "explicit-only"
            rules.append(f"{name}: {kind} skill should be {want}, but its policy says otherwise")
        if group == "core" and kind != "core":
            rules.append(f"{name}: lives in core/ but is a {kind}")
        elif group == "extras" and (kind != "leaf" or s["tree"]):
            rules.append(f"{name}: extras hold leaves outside every tree, found {kind} in tree {s['tree']!r}")
        elif group not in ("core", "extras") and s["tree"] != group:
            rules.append(f"{name}: lives in {group}/ but declares skill-tree {s['tree']!r}")
        for child in s["requires"]:
            if child not in skills:
                errors.append(f"{name}: requires {child}, which is not in the collection")
            elif skills[child]["tree"] != s["tree"]:
                errors.append(f"{name}: requires {child} from another tree ({skills[child]['tree']!r})")

    domains = {}
    for name, s in skills.items():
        if s["type"] == "domain":
            domains.setdefault(s["tree"], []).append(name)
    for tree, names in domains.items():
        if len(names) > 1:
            rules.append(f"tree {tree!r} has several domain skills: {', '.join(names)}")

    graph = skill_graph.discover([root])
    edges = {}
    patterns = sorted(((alias, owner) for owner, d in graph.items() for alias in skill_graph.aliases_for(owner, d)),
                      key=lambda pair: -len(pair[0]))
    for name, directory in graph.items():
        edges[name] = skill_graph.references(name, directory, patterns)
    for source, targets in edges.items():
        s = skills.get(source)
        if not s or s["type"] not in TYPES:
            continue
        for target in targets:
            t = skills.get(target)
            if not t:
                continue
            if t["type"] == "core":
                continue  # core skills stand in the middle; naming one routes nothing into a tree
            if s["group"] == "extras" and t["group"] != "extras":
                rules.append(f"{source} (shared leaf) names {target}; a shared leaf loads no tree skill")
                continue
            if t["group"] == "extras":
                continue  # suggesting a shared leaf to the person routes nothing (edge rule 6)
            if s["type"] in ("core", "leaf") and s["group"] != "extras":
                rules.append(f"{source} ({s['type']}) names {target}; a {s['type']} skill loads nothing")
            elif s["tree"] and t["tree"] and s["tree"] != t["tree"]:
                rules.append(f"{source} names {target} across trees ({s['tree']} -> {t['tree']})")
            elif target in edges and source in edges[target] and t["type"] in ("domain", "parent", "flow"):
                rules.append(f"{source} names its routing parent {target}")

    for line in errors:
        print("ERROR", line)
    for line in rules:
        print("RULE ", line)
    print(f"{len(skills)} skills, {len(errors)} errors, {len(rules)} rule findings")
    return 1 if errors or (strict and rules) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
