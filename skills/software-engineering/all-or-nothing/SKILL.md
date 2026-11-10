---
name: all-or-nothing
description: Carry an agreed replacement or model correction through its affected declarations, consumers, data and documentation, retiring the old implementation. Use when an authorized change supersedes an existing model, responsibility, contract or code path.
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# All or Nothing

**Leaf skill** in Software Engineering; reached through its domain or by name.

Make a settled change true throughout the system it affects. A new implementation
beside the old one, or a new label hiding the old model, has not completed the
change. The outcome is one coherent target with its consumers moved and its
superseded surfaces retired.

Use this method within the authorized change. Establish the intended target from
the assignment and current requirements; do not invent a replacement decision.
An inspection or review produces findings, not permission to implement them.
Complete means the affected contract, not an unsolicited sweep of the repository.

## A complete replacement in miniature

Illustrative approved change: batch delivery is retired and streaming is the only
supported mode. Removing the batch button is not the transition. Move the real
consumers and supported configuration, remove the retired option and behavior,
update their tests and documentation, and verify the streaming path. A stale batch
setting must produce the intended explicit error instead of silently selecting
a removed behavior. Preserve historical records without leaving them active.

## Establish the change boundary

Read the current owners and trace the affected behavior from entrypoint to state
and consumers. Identify what the new decision replaces, what must remain true,
and which declarations, stored shapes, configuration, APIs, UI, managed files,
tests and maintained explanations depend on it. Follow real dependencies rather
than restricting the change to the first file or expanding it to unrelated code.

Choose the canonical target before creating a competing owner. Multiple inputs
can feed it; independently maintained implementations of the same responsibility
cannot silently remain. If the intended behavior or external effect is unsettled,
state the decision and affected scope instead of choosing a convenient shim.

## Model Truth Over Diff Size

Correct the declarations themselves: types, schemas, registries, persisted data,
lookups and names must stop stating the false premise. Filters, aliases and
selectability guards do not repair a model that still declares the wrong thing.

For example, if a connection is an integration rather than a user, renaming its
display label and filtering it out of a user list is insufficient. Its identity,
stored shape and consumers must express integration semantics; the former user
path must stop owning it. Derive the actual migration from the real contract.

Apply the declaration test: **could a new reader still derive the false premise
from any affected type, field, registry or lookup?** If yes, the correction is
incomplete. A larger diff or more callers is not a reason to silently preserve
the false model. Make a material scope, migration or behavior decision visible;
comments cannot explain away dishonest declarations.

## Move consumers and retire the previous owner

Preserve the relevant existing behavioral oracle and record baseline failures.
Move consumers, data and configuration in attributable, verifiable steps with a
recovery point appropriate to the risk. Coherent completion does not require
one giant commit. Intermediate states must be understood and recoverable.

Retire the old code path, names, flags, fixtures, configuration and misleading
explanations when the target owns their job. Check entrypoints, bootstrap,
registries, dynamic imports and operational callers before declaring code dead.
A search result or another agent's report is a lead to verify, not proof that
a runtime path is unreachable. Historical records and required archives can
retain past names; they must not remain active implementation or instructions.

Temporary coexistence needs an agreed purpose, an explicit owner and a removal
condition. Surface any required approval before creating a compatibility bridge
or changing external state. Do not keep a fallback merely because finishing the
consumer migration is inconvenient, and do not remove a live data path blindly.

## Prove the transition and finish

Verify the target through the boundaries that can expose the relevant failure.
Check that the new behavior is used, its consumers agree on the model and the
retired path no longer owns active work. A string search can find stale names;
it cannot prove the new API is callable or the data migration actually ran.
Distinguish local source verification from a deployed or migrated system.

Keep nearby explanations and maintained contracts current in the same change.
Review the combined diff for old assumptions, duplicate owners and unrelated
edits. Preserve evidence still needed by open work. When an active plan or
workflow owns closure, return transition evidence and remaining retirement
items to that owner; leave its plan and working artifacts until its review and
closeout gates pass. For direct work without an enclosing workflow, finish cleanup
within the authorized scope after the required verification and review. Retain the
necessary evidence, retire completed temporary artifacts and update the owning record.

Deliver the corrected model or replacement, the retired surfaces, actual evidence
and remaining limits. If an external migration or decision is still outstanding,
name that boundary explicitly; do not report the whole transition as complete.

If **Puppeteer** is available for a broad transition, use it to investigate or
change independent consumers after the shared target contract is settled. For
substantial work, keep sequencing, verification and cleanup in the active plan.
The complete result needs independent review; report that need to the lead.
Return the result to whoever loaded this method rather than starting the same
workflow again; without an enclosing workflow, keep the same ownership and
evidence boundaries in the task's existing workflow.
