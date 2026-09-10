---
name: road-to-glory
description: Plan and maintain larger, understood or interruptible Engineering work with a ROADMAP, active .tmp plans and a CHANGELOG. Use when work needs coordinated packages or resumable state; keep shipped outcomes and human verification distinct.
---

# Road to Glory

Make what is actually left to do visible, executable and safe to resume. This
method keeps the roadmap and active execution plans aligned. Project-specific instructions or
an explicitly chosen external workflow may override these defaults; otherwise
use ROADMAP.md, CHANGELOG.md and .tmp/ deliberately rather than inventing a tracker.

Read [Engineering Mindset](../engineering-mindset/SKILL.md) if it is not already
in context. Establish whether the request is to plan, resume or execute. A
planning-only request creates the plan; it does not launch implementation or
publish to an external tracker. Unresolved direction belongs to clarification,
not to a ticket that pretends the decision has been made.

## Start with current reality

Read the assignment, settled decisions, existing board, active plans and relevant
code or artifacts. Re-scout resumed work; counts, paths, dependencies and previous
conclusions may be stale. Define the outcome, why it matters, no-go constraints,
affected owners and the evidence that will establish completion.

Before adding a roadmap item, scout lightly: is the need real, which capability
owns it, which dependencies are likely and what obvious risks exist? A future
item needs useful scouting, not a detailed implementation plan that will age
before anyone works on it. Start detailed planning when the item becomes active,
with a fresh examination of the actual system.

## Give each kind of state its own home

**ROADMAP.md is a workboard, not documentation.** State that at its top. Keep rows
compact: item, plan link where active, and a one-to-three-line description.
No architecture essays, completed-work diary or status narrative on the board.
An active item links its actual plan one-to-one. Unstarted items retain their
lightweight need and scouting until a detailed plan is useful.

**.tmp/ owns active temporary plans and working aids.** Keep it git-ignored for
ordinary local work. Use meaningful filenames so the linked plan can be found.
If a workflow must resume on another machine, use its established accessible
plan owner instead of claiming a local ignored file is shared. State that
specific exception; it is not a reason to abandon the ordinary local convention.

**CHANGELOG.md owns shipped outcomes.** When work finishes, remove the roadmap
row and record one compact, coherent entry describing what changed and why it
matters. Do not accumulate the raw sequence of internal deliberation.

**VERIFICATION.md owns genuinely human judgment**, when the repository needs it.
A finished implementation does not remain an unfinished roadmap item merely
because a person must look at it. Keep at most one board pointer to the verification
record. Each entry states what was implemented, what is new, the expected behavior
and the one question the person must answer.

A visual judgment or an owner decision can need a person. An assertion the agent
can run is not a human-verification item, and a server whose behavior has no test
is not fixed by asking the user to check it manually.

## Cut a plan that can be executed

Use this plan skeleton, scaling its detail to the work:

| Part | Required content |
|---|---|
| **Outcome** | The resulting capability or state and its observable completion. |
| **Why This Block Exists** | The need this work addresses and why it belongs together. |
| **No-Go Constraints** | Behaviors, data boundaries and unrelated work that must be protected. |
| **Target Files/Modules** | Verified owners and paths needed to start, without duplicating their content. |
| **Done Gate** | The checks and evidence that prove the outcome. |

For a larger plan, cut verifiable capability slices. A feature package carries the
technical layers its behavior needs; do not make separate tickets for each global
layer. Give each package its inputs, meaningful boundary, acceptance evidence and
actual blockers. Link shared requirements rather than copying entire conversations.

Sequence structural prerequisites when consumers really depend on them. Do not
invent dependencies that merely express preferred order. A broad migration must
state which intermediate states are valid and how the combined result is checked;
do not introduce compatibility code just to manufacture independent green slices.

An unblocked package must be startable from the plan and its verified references.
A missing requirement stays visible with the next check or owner decision; it
must not become an assumed acceptance criterion. Publishing technical tickets or
sending messages needs authorization for that external effect.

## Maintain the plan while work happens

The active plan is live control state, not an end-of-run retrospective. Reconcile
it when an item changes state, evidence arrives, a commit lands, a worker returns
or a blocker is disproved. Check it before assigning more work or reporting status.
Keep deferred and owner-led work visible; stale totals and omitted follow-up hide
what remains just as effectively as a false completed label.

Read the plan yourself before implementing it or delegating a well-specified
piece. Delegation is not the default and never substitutes for understanding the
boundaries and decisions needed to steer the work. Verify a returned finding
against the actual source before turning it into another plan item.

## Close the work in the same slice

When implementation is complete, update the board, retain the necessary outcome
and evidence with their owners, add the CHANGELOG entry and delete the completed
.tmp plan. Remove orphaned plans and temporary helpers whose job has ended.
Do not remove an artifact still needed by another active item; move its useful
content to the proper owner before deleting its temporary carrier.

For example, a completed capability leaves ROADMAP.md, appears once in
CHANGELOG.md and loses its active .tmp plan. If only a visual judgment remains,
that question goes to VERIFICATION.md instead of keeping the implementation row
open. The roadmap then continues to answer what is actually unbuilt.

Return the canonical plan or updated work state, its location, the next executable
step and any real blocker. Keep task state in these owning files, not durable
assistant memory. The planning artifacts serve the work; small changes that can
be completed directly do not need the whole apparatus.

Supplementary specification and work-package techniques are credited in
[NOTICE.md](NOTICE.md).
