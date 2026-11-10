#!/usr/bin/env python3
"""Measure whether target skills load within the first tool calls of fresh `claude -p` runs.

Usage: trigger_window.py EVALS PROJECT OUT --targets a,b [--inject SKILL_DIR]
                         [--window 4] [--runs 2] [--model ID]

EVALS is a JSON list of {"query", "should_trigger"}. Each query runs RUNS times
in PROJECT; a run is a hit when any target skill is loaded (Skill tool, a Read of
its file or a shell command naming it) within the first WINDOW tool calls. OUT receives per-query hits and
the observed tool sequence, so misses show what the agent did instead.

Run it in a small fixture repository, not an empty folder: agents explore files
before loading skills, so a first-tool-only check cannot discriminate. Always
measure a baseline configuration with the same queries. Edits are disabled and
each run is stopped after WINDOW tool calls. --inject installs a skill as a
project skill for the run; placement changes trigger rates, so make the final
measurement with a temporary user-level copy. Hide competing skills through the
fixture's .claude/settings.json `skillOverrides`. These are real, billed model
runs; pass --model with the model the user's sessions actually use.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def run_query(query, args, targets):
    # Nested claude -p refuses to start while CLAUDECODE is set.
    env = {key: value for key, value in os.environ.items() if key != "CLAUDECODE"}
    cmd = ["claude", "-p", query, "--output-format", "stream-json", "--verbose",
           "--max-turns", str(args.window + 1),
           "--disallowedTools", "Edit", "Write", "NotebookEdit", "Agent", "Workflow"]
    if args.model:
        cmd += ["--model", args.model]
    tools = []
    try:
        process = subprocess.Popen(cmd, cwd=args.project, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL, text=True, env=env)
        for line in process.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") != "assistant":
                continue
            for item in event["message"].get("content", []):
                if item.get("type") == "tool_use":
                    data = item.get("input", {})
                    detail = data.get("skill") or data.get("file_path") or data.get("command") or ""
                    tools.append((item["name"], str(detail)[:80]))
            if len(tools) >= args.window:
                break
        process.kill()
        process.wait(timeout=10)
    except (OSError, subprocess.SubprocessError) as error:
        tools.append(("ERROR", str(error)[:80]))
    hit = any(loads_target(name, detail, targets) for name, detail in tools)
    return hit, tools


def loads_target(name, detail, targets):
    """A skill counts as loaded through the Skill tool, or a Read or shell read of its
    directory (agents often cat explicit-only skills they cannot invoke by name).
    A bare word is not enough: `ls design` in a fixture with a design/ folder
    must not count as loading a skill named `design`."""
    for t in targets:
        word = rf"(?<![\w-]){re.escape(t)}(?![\w-])"
        if name == "Skill" and (detail == t or detail.endswith(":" + t)):
            return True
        if name in ("Read", "Bash") and re.search(rf"skills/(?:{word}|\{{[^}}]*{word})|{word}/SKILL\.md", detail):
            return True
    return False


def inject(skill_dir, project):
    source = Path(skill_dir)
    name = re.search(r"^name:\s*([\w-]+)", (source / "SKILL.md").read_text(), re.M).group(1)
    target = Path(project, ".claude", "skills", name)
    if target.exists():
        raise SystemExit(f"refusing to overwrite existing project skill: {target}")
    shutil.copytree(source, target)
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evals")
    parser.add_argument("project")
    parser.add_argument("out")
    parser.add_argument("--targets", required=True, help="comma-separated skill names that count as a hit")
    parser.add_argument("--inject", help="skill directory to install as a project skill for this run")
    parser.add_argument("--window", type=int, default=4)
    parser.add_argument("--runs", type=int, default=2)
    parser.add_argument("--model")
    args = parser.parse_args()
    targets = args.targets.split(",")

    queries = json.loads(Path(args.evals).read_text())
    injected = inject(args.inject, args.project) if args.inject else None
    try:
        jobs = [(index, entry["query"]) for index, entry in enumerate(queries) for _ in range(args.runs)]
        with ThreadPoolExecutor(8) as pool:
            outcomes = list(pool.map(lambda job: run_query(job[1], args, targets), jobs))
    finally:
        if injected:
            shutil.rmtree(injected)

    results = [{**entry, "hits": 0, "runs": 0, "tools": []} for entry in queries]
    for (index, _), (hit, tools) in zip(jobs, outcomes):
        results[index]["hits"] += hit
        results[index]["runs"] += 1
        results[index]["tools"].append(tools)
    Path(args.out).write_text(json.dumps(results, indent=1))

    for label, wanted in (("should trigger", True), ("near-misses", False)):
        group = [r for r in results if r["should_trigger"] is wanted]
        print(f"{label}: {sum(r['hits'] for r in group)} / {sum(r['runs'] for r in group)} runs loaded a target")


if __name__ == "__main__":
    main()
