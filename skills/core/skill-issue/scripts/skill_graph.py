#!/usr/bin/env python3
"""Map cross-references between skills in one or more skill roots.

Usage: skill_graph.py ROOT [ROOT ...] [--json]

A skill is any directory holding SKILL.md at any depth below a root, except a
SKILL.md nested inside another skill (for example a vendored entrypoint under
references/), which belongs to its enclosing skill. A skill is recognized
in another skill's SKILL.md and references/*.md by its directory name, its
frontmatter `name`, the Title Case form of that name, and its `display_name`
from agents/openai.yaml. Longer aliases are matched first, so "Grilling with
Agents" is not also counted as "Grilling".

The output counts mentions, not calls: a boundary sentence ("logos belong to
SVG Design") is an edge too. Tree membership is not an edge, so the type line
("**Leaf skill** in Design") and `skill-tree:` metadata are ignored, and a
one-word skill name such as Design, GSAP or Puppeteer counts only where it is
marked as a skill — in backticks, in bold, or followed by "skill" or "domain" —
because the plain word is often ordinary prose or a library name. Unmarked
mentions of one-word skills are therefore missed; the audit can undercount them. Treat mutual pairs and high fan-out as places to
inspect. Standard library only; exits 1 if no skill is found.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path


# Lines that state where a skill sits in the tree rather than what it loads.
MEMBERSHIP = re.compile(r"^(\*\*(Core|Domain|Parent|Flow|Leaf) skill\*\*.*|\s*skill-tree:.*)$", re.MULTILINE)
ONE_WORD = re.compile(r"[A-Za-z]+")


def frontmatter_name(text):
    match = re.search(r"^name:\s*['\"]?([\w-]+)", text, re.MULTILINE)
    return match.group(1) if match else None


def discover(roots):
    skills = {}
    for root in roots:
        found = sorted(Path(root).rglob("SKILL.md"), key=lambda p: len(p.parts))
        owners = []
        for path in found:
            # Shallowest first, so an enclosing skill claims its nested files.
            if any(owner in path.parents for owner in owners):
                continue
            owners.append(path.parent)
            skills.setdefault(path.parent.name, path.parent)
    return skills


def aliases_for(name, directory):
    found = {name, " ".join(word.capitalize() for word in name.split("-"))}
    declared = frontmatter_name((directory / "SKILL.md").read_text(encoding="utf-8"))
    if declared:
        found.add(declared)
    metadata = directory / "agents" / "openai.yaml"
    if metadata.exists():
        match = re.search(r"display_name:\s*['\"]?([^'\"\n]+)", metadata.read_text(encoding="utf-8"))
        if match:
            found.add(match.group(1).strip())
    return found


def references(name, directory, patterns):
    """Count mentions of other skills in a skill's SKILL.md and references/*.md."""
    files = [directory / "SKILL.md", *sorted((directory / "references").glob("*.md"))]
    text = "\n".join(path.read_text(encoding="utf-8") for path in files)
    text = MEMBERSHIP.sub("", text)
    counts = Counter()
    for alias, owner in patterns:
        if ONE_WORD.fullmatch(alias):
            word = re.escape(alias)
            regex = re.compile(rf"`{word}`|\*\*{word}\*\*|(?<![\w-]){word}(?= (?:skill|domain)\b)")
        else:
            regex = re.compile(r"(?<![\w-])" + re.escape(alias) + r"(?![\w-])")
        hits = len(regex.findall(text))
        # Blank matched spans so a shorter alias cannot match inside a longer one.
        text = regex.sub(lambda m: " " * len(m.group(0)), text)
        if hits and owner != name:
            counts[owner] += hits
    return dict(counts.most_common())


def main(argv):
    as_json = "--json" in argv
    roots = [arg for arg in argv if arg != "--json"]
    skills = discover(roots)
    if not skills:
        print("no SKILL.md found under: " + ", ".join(roots), file=sys.stderr)
        return 1

    patterns = sorted(
        ((alias, owner) for owner, directory in skills.items() for alias in aliases_for(owner, directory)),
        key=lambda pair: -len(pair[0]),
    )
    edges = {name: references(name, directory, patterns) for name, directory in skills.items()}

    inbound = Counter(target for targets in edges.values() for target in targets)
    mutual = sorted({tuple(sorted((a, b))) for a, targets in edges.items() for b in targets if a in edges.get(b, {})})

    if as_json:
        print(json.dumps({"edges": edges, "inbound": dict(inbound.most_common()), "mutual": mutual}, indent=2))
        return 0
    width = max(len(name) for name in skills)
    for name in sorted(skills):
        targets = edges[name]
        listed = ", ".join(f"{target}({count})" for target, count in targets.items())
        print(f"{name:<{width}} -> {len(targets):2}  {listed}")
    print("\nMost referenced: " + ", ".join(f"{name}={count}" for name, count in inbound.most_common(10)))
    print(f"Mutual pairs ({len(mutual)}): " + "; ".join(f"{a} <-> {b}" for a, b in mutual))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
