# Sources and evidence

Software Engineering is a repository-owned context router created on 2026-11-10.
It replaces separate implicit triggers of Engineering Practices, Golden Comments
and Vertical Slices, which became explicit-only and are loaded by role.

## Trigger evidence

Measured on 2026-11-10 with `claude -p` (model `claude-opus-5-5`, Claude Code
2.1.311) in a small fixture Git repository. A run counts as a hit when the
target skill is loaded within the first four tool calls; edits were disabled.
In the target configuration the three specialists were hidden from the model
through project `skillOverrides`.

| Configuration | Engineering requests | Near-misses |
|---|---|---|
| Before: the three specialists implicit at user level, no router | 0 / 20 | 0 / 20 |
| Before-description of Engineering Practices as project skill | 5 / 20 | 0 / 20 |
| Router, first description, user level | 14 / 20 | 0 / 20 |
| Router, final description, user level | 19 / 20 | 0 / 20 |
| Router, final description, user level, unseen held-out set | 12 / 16 | 0 / 8 |

A first-tool-only measurement in an empty folder scored 1 / 30 for both the
router and the old description and was discarded as non-discriminating. The
remaining systematic gap is PR review ("look at PR #482"), where the first call
is often `gh pr view`. The query sets are in [trigger-evals/](trigger-evals/) and the harness is
Skill Issue's `scripts/trigger_window.py`; rerun both sets after changing this
description and compare against these numbers.
