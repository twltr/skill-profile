---
name: minmax-tokens
description: Reduce unnecessary context and tool output during file, search, Git, test, log, and web work while preserving requirements and verification. Use for tool-driven tasks; skip self-contained conversation.
---

# MinMax Tokens

Use the smallest sufficient evidence, not the smallest possible answer. Keep active requirements, contrary evidence, safety constraints, unresolved failures, and final checks intact. If a filtered result cannot establish the answer, expand the scope.

## A bounded read

For a known checkout test failure in a large saved log, search the case identifier
and failure blocks before reading the relevant error and surrounding context.
Return the failure, exact location, actual process exit status and unresolved
questions. Preserve access to the original log and expand when the excerpt cannot
explain the problem. A model summary after pasting the entire log cannot undo
the context cost. Independent reasoning across another subsystem may justify a scout.

## Get only the useful result

Before a tool call, know the question it must answer and the expected size of its result. Use known IDs, paths, symbols, fields, ranges, and structured queries directly. Search narrowly, then widen deliberately if coverage is insufficient. Read a small file or a complete function when its context matters; do not add a count or planning step before an already bounded read.

Filter, project, deduplicate, or compare large data in the source tool or local process before its output enters model context. A language-model summary after a raw dump does not undo the dump. Preserve the original data or a defined snapshot for targeted recovery. Do not save a full dump merely to read it back. Set per-call output limits where available, disclose truncation, and retrieve omitted evidence when needed.

Reuse a finding while its inputs remain valid. Refresh affected parts after your edits, other edits, new files, changed dependencies, or changed configuration. A negative search only covers its queried scope. A passed test is no longer current after a relevant change. Record a compact state only when it will prevent substantial rereading, without creating a work diary.

## Match the check to the claim

For Git, locate affected files and hunks before reading a large diff. Account for staged, unstaged, untracked, and pre-existing changes. A diff statistic locates work; it does not review behavior.

Run the tests needed by the project's rules and the change's risk. Compact their display without shrinking the required test scope. Preserve the process exit status, distinct failure causes, IDs, stderr, and nearby context. A failure can occur in the middle of output. Do not use blind head/tail truncation, mask exit codes with a pipeline, or rerun a side-effecting command only to recover its log.

For web research, use precise questions and authoritative sources. Keep version or date, the relevant passage, and uncertainty. Reuse a located source unless new evidence or a contradiction calls for another query.

When delegation is useful and `puppeteer` is available, use it for task division and authority. Substantial independent investigations can keep irrelevant source out of the main context; there is no general limit here on useful agent count. Do not summon a subagent merely to count or filter data that a deterministic tool can handle. Without Puppeteer, define bounded questions, ownership and evidence directly. Puppeteer owns phase- and capability-based model selection; native client configuration owns executable bindings and defaults. Do not maintain a competing model list here or infer total savings from a cheaper individual call.
