# Sources and evidence

Good Writing is the owner's own work (MIT, see [LICENSE](LICENSE)), first
imported from his 2026-09-23 writing export and since reduced to a short router
over four specialists; [SKILLS.md](../../../SKILLS.md) records its history.

## Trigger evidence

Measured on 2026-11-10 with `claude -p` (model `claude-opus-5-5`, Claude Code
2.1.311) in a small fixture repository holding notes, offers and docs that the
queries refer to. A run is a hit when Good Writing loads within the first four
tool calls; edits were disabled. The router was installed at user level as in
daily use, with its specialists explicit-only. Two runs per query.

| Set | Writing requests | Near-misses |
|---|---|---|
| [train.json](trigger-evals/train.json) | 19 / 20 | 0 / 20 |
| [holdout.json](trigger-evals/holdout.json), unseen | 12 / 12 | 0 / 6 |

Near-misses cover wording-only fixes and ordinary replies (Unslop's job),
repository docs and code comments (software engineering), and language
questions. The single miss was a meeting-notes request that read the notes
first and loaded the router in one of two runs. Rerun both sets with Skill
Issue's `scripts/trigger_window.py` after changing the description.
