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

## Review, quick fixes and the remaining leaves (2026-11-10, second round)

Measured with the same model and harness in a fixture that holds the code the
queries name (a payment double charge, a UTC display bug, a cache TTL, a
migration, a branch `feature/cache-ttl`). The description was unchanged.

| Measurement | Should trigger | Near-misses |
|---|---|---|
| [train-review.json](trigger-evals/train-review.json): PR review and quick fixes | 9 / 10 | 0 / 6 |
| [holdout-review.json](trigger-evals/holdout-review.json), unseen | 12 / 12 | 0 / 6 |
| Implementer pack (Engineering Practices, Golden Comments, Vertical Slices) loaded within six calls on five quick fixes, three runs each | 14 / 15 | — |
| Domain Modeling, All or Nothing, Marshmallow Tests, State of the Art, Engineering Review and Road to Glory hidden: train | 20 / 20 | 0 / 20 |
| Same, holdout | 16 / 16 | 0 / 8 |
| Same, review holdout | 12 / 12 | 0 / 6 |

The PR-review gap of the first round no longer appears, and the domain catches
every request without the six remaining leaves competing, so they became
explicit-only. The one pack miss was a typo fix whose agent searched the code
before reading the pack.
