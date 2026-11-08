---
name: golden-comments
description: "Preserve design intent, system context, named mechanisms and decision reasons beside source code. Apply while creating or changing source files and important modules, and when reviewing them, even if comments were not requested. Repository-wide architecture and operating guides belong to Engineering Documentation."
---

# Golden Comments

Make source code carry the understanding needed to continue its design after the
conversation is gone. The next maintainer should be able to read the implementation
alongside the reasons for its construction: what it serves in the larger system,
why it has this shape and what a seemingly harmless change would break.

Apply this method to each new or substantively changed source file during ordinary
implementation. Important modules, public boundaries and policy owners need a
local explanation; do not wait for a separate documentation request or a detected
high-risk bug. A self-explanatory leaf needs no ceremonial header. Judge coverage
by what a future reader must reconstruct, never by a comment count or percentage.
A comment-only assignment still does not authorize code redesign.

## Example: preserve the reason for a status model

Fictional brief: several runtime consumers disagree about which waiting tasks
still reserve an exclusive write slot. The accepted design gives the vocabulary
and its question-specific sets one owner. The source briefing can say:

```python
"""Own task lifecycle vocabulary shared by the scheduler, store and client events.

TaskStatus uses StrEnum to retain the existing wire strings. Named sets answer
different questions: LIVE identifies unfinished work; SLOT_HOLDING reserves the
exclusive write slot. They overlap intentionally. A task waiting for approval
has stopped executing but must keep that slot until its operation resumes.

A type alias alone would name the strings while leaving set membership scattered
across consumers. Keep that policy here so a new status cannot silently mean
different things to admission and recovery. Session status is a separate model.

See docs/runtime.md#task-lifecycle for the lifecycle overview and public contract.
"""
```

The module explains the design, its alternative and the consequence of collapsing
two concepts. The docs own the wider lifecycle and route here for membership
reasons. Verify every claim against the real code; this illustrative docstring
does not implement a state machine or establish slot enforcement by itself.
Farther down, a comment on the exceptional membership explains that case next to
the set. Do not repeat the whole briefing beside every use.

## Find the explanation's local owner

Read the relevant mechanism and its canonical requirements before writing about
it. Identify what a new maintainer cannot safely infer: the architectural model,
dependency direction, invariant, assumption, ordering or failure mode. Explain
that at the narrowest place that owns the reason.

Recover accepted decisions from the current conversation, design review or agent
handoff while that evidence is available. Translate the settled rationale into
durable source explanation in the same change; do not paste the conversation or
its participants into code. Preserve the constraint and any meaningful condition
for revisiting the decision. Unsettled alternatives remain open at the task's
decision owner; they must not become an invented account of why the code is right.

Name an applied pattern or mechanism when it helps a reader recognize the design,
and explain its concrete role here. For example, a Command dispatcher maps a typed
envelope to its handler; the local briefing explains why execution stays out of
the transport. The owning architecture chapter can carry the pattern's primary
source and repository-wide locations. A local link connects those explanations.
Use plain descriptive names for local mechanisms; do not invent a famous origin.

If an explanation contradicts the code, determine whether the code is wrong,
the explanation stale or the requirement changed. Do not make a comment justify
a known defect. Surface an unresolved behavior decision rather than inventing
a reason the implementation happens to look this way.

## Brief the important entrypoints

A package doc, important script header or migration header is a compact local
architecture briefing. Cover what the entrypoint actually needs:

- **Direction / Context:** what this unit does and which way the work flows.
- **Bigger Picture / Dependencies:** how it serves the system and what it relies on.
- **Local Construction:** the mechanism and the relationships inside it.
- **Why This Construction:** why this arrangement is appropriate, including the
  reason behind the immediate design choice.
- **Canonical Semantics:** what the names, states and outcomes mean here.
- **Design Rules / Assumptions:** what must remain true for the mechanism to work.
- **Forbidden Responsibilities:** what this unit must not start owning.

Explain the relationship to the larger system even when the local code is simple:
who calls this unit, what decision it owns and why that boundary matters. A reader
should not need the original chat to discover that a short helper is the only
writer of a lifecycle transition. Name the actual entrypoints and relevant siblings
when they provide a useful route; avoid an inventory of every file.

Write coherent local prose rather than a stack of labels with no explanation.
Keep a longer briefing when moving it elsewhere would separate a critical
invariant from the mechanism. A module's domain and public-contract explanation
keeps its canonical owner; link it instead of copying a documentation chapter.

These are selection questions, not seven mandatory headings for every file. A
short module docstring can establish purpose, dependency and one critical boundary:

```python
"""Apply accepted turn results through the event store's transaction boundary.

Review decides acceptance; this module persists it with the cursor update.
Both writes must commit together so recovery cannot skip an unapplied result.
"""
```

This is a fictional example; verify the dependency and atomicity claim against
the actual implementation. Put such a briefing at the file's natural entrypoint
when it saves a reader from reconstructing the module's job. Keep it short and
specific; obvious files need no ceremonial header. Detailed local reasons remain
beside the mechanism. Use Domain Modeling for precise concepts and Vertical Slices
for actual ownership and dependencies when those skills are available; a comment
does not create a new contract or authorize restructuring the code.

## Explain where the voltage is

Explain ordinary design decisions as well as dangerous boundaries: why a factory
centralizes construction, why an observer is unsubscribed at this lifetime boundary,
why a pipeline owns ordering, or why a state handler must return control to its
coordinator. These explanations help future changes preserve a coherent design;
security and concurrency are not the only reasons to leave a useful comment.

Critical-boundary comments are required where a small change can create a
second truth, a race or data loss. Inspect optimistic concurrency, idempotency,
event append/load boundaries, projection cursors, transactions, retry/claim/lease
logic, deletion gates, authentication and secrets, reconciliation and cross-system
calls. The list identifies risks to look for, not comments to add mechanically.

"Save record" does not explain the risk. When a severity cue helps, begin with
`Important:` or `Critical:` and name the consequence. Never label source comments
`Golden comment`, `Hotspot comment`, `agent note` or another authoring category.
Those are names for this method, not the language of the product's source.

Semantic nil/default branches, retry loops, cursor saves, silent skips,
external/internal ID conversions and migration bridges deserve a closer look.
If documentation says "must" while the code permits the opposite, a reassuring
comment is not a repair. Explain the real invariant or address the construction
within the authorized scope.

## Keep the explanation durable

Keep detailed local construction and decision reasons beside their implementation.
Repository docs own overall architecture, applied-pattern/source navigation,
cross-module contracts and operating procedures. Link between them instead of
copying the same explanation. A brief orientation in both places is useful; two
independently maintained accounts of the same rule are not. Use Engineering
Documentation directly when available for an affected repository explanation;
pass the verified change and its source anchors without restarting Good Writing.
If unavailable, preserve this division of ownership and report a material gap.

Write concise, complete, grammatical sentences in the repository's language.
Source prose serves the next developer. It does not discuss the coding agent,
model, prompt, generation process, delegation or internal workflow that produced
it. An agent that is an actual domain or runtime concept can of course be named.

Use section banners only at real phase boundaries, where they clarify direction
or an invariant. For migration code, distinguish the target owner, temporary
bridge and retiring implementation; state the temporary part's removal condition.

Temporary work coordinates such as roadmap IDs, waves, ticket shorthand or
meeting labels do not belong in source, test names, fixtures or maintained
reference prose. For example, D3, CC16 or R20 are not durable explanations of a
requirement. State the actual behavior and reference its canonical descriptive
chapter or contract where useful. History may point to source; source does not
need to point back to an expired planning coordinate.

## Revise and verify in place

When behavior changes, update its nearby explanation in the same work. Consolidate
adjacent corrections into one coherent comment instead of accumulating defensive
paragraphs after each edit. Preserve useful reasons and assumptions while removing
repetition; commentary is not a line-count reduction target.

Read each affected important file as a maintainer with no chat history: can they
explain its system role, construction, reasons and change constraints, then follow
a precise pointer for wider context? Check whether accepted rationale was left
only in a plan or final reply. Verify the ownership, ordering and failure claims
against the mechanism. Verify referenced paths and recheck a claim whose
pointer was stale. Return the revised source commentary and any unresolved model
question to the calling task. Use the work's relevant verification; a prose-only
change does not need a new test farm.
