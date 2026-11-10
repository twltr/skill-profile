# Sources and evidence

Design is a repository-owned domain skill created on 2026-11-10. It replaces the
separate implicit triggers of Frontend Design, Motion Design, SVG Design and
GSAP, which became explicit-only, and routes to the leaves adapted from
Anthropic's design plugin (provenance in each child's `NOTICE.md`).

## Trigger evidence

Measured on 2026-11-10 with `claude -p` (model `claude-opus-5-5`, Claude Code
2.1.311) in a small web fixture repository; a hit is the skill loading within the
first four tool calls. The domain was installed as a temporary user-level skill;
its leaves were hidden through project `skillOverrides`. The Design plugin's
skills could not be hidden that way and still competed in the target runs.

| Configuration | Design requests | Near-misses |
|---|---|---|
| Before: four design leaves and the plugin's seven skills implicit | 12 / 20 | 0 / 20 |
| Domain, first description | 14 / 20 | 2 / 20 |
| Domain, final description | 15 / 20 | 0 / 20 |
| Domain, final description, fresh held-out set | 7 / 12 | 1 / 6 |

Misses cluster where design meets implementation in a repository ("clean up the
design tokens", "gsap timeline animation"): Software Engineering loads instead,
which the description now pairs explicitly. A German UX-copy request missed in
every run. The held-out false positive loaded Editorial SVG Diagrams first and
Design second. ## Re-measurement without the Design plugin (2026-11-10)

Same model, harness and fixture, with the plugin uninstalled and the domain
installed at user level as in daily use; two runs per query.

| Set | Design requests | Near-misses |
|---|---|---|
| [train.json](trigger-evals/train.json) | 20 / 20 | 0 / 20 |
| [holdout.json](trigger-evals/holdout.json), unseen | 12 / 12 | 0 / 6 |

The first pass seemed to show two near-miss hits ("set up eslint and
prettier", a slide deck). Their tool sequences showed no Design load: the
harness had counted `ls design` in the fixture's `design/` folder. After the
hit rule was fixed, all stored runs were re-scored with these results. The
description now also excludes presentations and the Prettier formatter; it
scored the same before and after that wording change. The German UX-copy
request that missed before now loads the domain in both runs.

Rerun both sets with Skill Issue's `scripts/trigger_window.py` after changing
the description.
