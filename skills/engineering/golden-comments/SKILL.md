---
name: golden-comments
description: "Explain models, reasons, invariants and failure consequences in code comments and local briefings. Use when writing or changing source code that needs those explanations, or reviewing its comments; system books and READMEs use the Engineering Documentation route in Good Writing."
---

# Golden Comments

Make source code explain the model a future maintainer needs to change it safely.
Golden Comments carry **why, how and why this construction**. Code already says
what the statements do; repeating their syntax adds no understanding.

Use this method when writing or changing source commentary, including
within ordinary implementation. A comment-only assignment does not authorize a
code redesign. This skill owns source commentary, not a system documentation book.
For system books and READMEs, use Good Writing's Engineering Documentation route when
those skills are available; otherwise document the limit and keep the explanation
inside the explicitly requested scope.

## A reason-bearing comment

**Weak:** `Update the registry.`

**Better, if this matches the real mechanism:**

> This upsert must run before the registry write, or the id check races.

The second comment names the required ordering and the failure it prevents. Read
the mechanism before writing it; if the implementation does not enforce that
ordering, report the discrepancy instead of making the comment sound reassuring.

## Find the explanation's local owner

Read the relevant mechanism and its canonical requirements before writing about
it. Identify what a new maintainer cannot safely infer: the architectural model,
dependency direction, invariant, assumption, ordering or failure mode. Explain
that at the narrowest place that owns the reason.

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

Read the result with its mechanism: does it explain why, how and why this how;
are the ownership, ordering and failure claims true; and could someone safely
modify the unit using it? Verify referenced paths and recheck a claim whose
pointer was stale. Return the revised source commentary and any unresolved model
question to the calling task. Use the work's relevant verification; a prose-only
change does not need a new test farm.
