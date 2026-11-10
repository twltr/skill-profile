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
Design second. Re-measure after the plugin is uninstalled, with the sets in
[trigger-evals/](trigger-evals/) and Skill Issue's `scripts/trigger_window.py`.
