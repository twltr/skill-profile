---
name: refactor-code
description: Implement a selected structural improvement while preserving the agreed observable behavior. Use for code consolidation, responsibility moves and removal of superseded implementations, not to decide a new product behavior.
---

# Refactor Code

Apply the chosen structural change with evidence that its behavioral contract
survives and the obsolete implementation is actually retired.

## Establish the baseline

Identify the requested improvement, its affected owners and the behavior that
must remain stable. Inspect the actual working tree and existing changes.
Trace consumers through entrypoints, registries, dynamic loading and operational
paths as well as static references. An unused-code report is a lead to verify.

Run the relevant existing checks before changing their oracle. Record baseline
failures separately. Where behavior is not represented, capture the smallest
useful characterization from an independently known contract or observed input
and result. Do not invent an expected answer for an unresolved requirement.
If the requested change alters that contract, distinguish the intended behavior
change from the refactoring before proceeding.

## Move one responsibility coherently

1. Choose the canonical target owner and name what will disappear. For each
   affected consumer, establish how it will reach the same behavior afterwards.
   Include persisted shapes, configuration and public interfaces when relevant.
2. Cut the implementation into attributable steps that can be checked and
   recovered. Coordinate shared owners before consumer edits. Use mechanical
   moves and language-aware transformations where they preserve declarations
   more reliably than rewriting them. Do not prescribe a commit per consumer
   or an expand-contract migration independent of the actual risk.
3. Keep capability policy at its owner when extracting shared machinery.
   Compare the moved contracts and behavior directly. An unchanged behavioral
   test is valuable evidence; a structural test edit needs an explanation of
   why its oracle still means the same thing. Never weaken an expectation to
   make the refactoring pass.
4. Remove superseded paths, configuration, tests of retired-only behavior and
   stale references when their consumers have migrated. Verify absence through
   the actual loading paths, not just one grep. Temporary coexistence is an
   explicit migration decision with an owner and removal condition, not a
   fallback for avoiding the completed change.

## Verify and close

Run the checks that prove the affected behavior and interactions, then inspect
the complete diff for accidental semantics or unrelated edits. For every deleted
behavioral check, identify the surviving evidence or the deliberately retired
requirement. Preserve the oracle needed by unfinished migration steps.

Update the nearby explanation, public contracts and the workflow's work record.
Remove this work's obsolete temporary artifacts as part of finishing it.
Report the structural improvement, the evidence, any baseline failures and the
remaining limits. A passing test suite does not by itself prove a live migration
or deployment occurred.
