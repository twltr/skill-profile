---
name: plan-work
description: Plan and maintain larger, already-understood implementation work as verifiable work packages with real dependencies. Use for multi-step execution planning and resuming such work; unresolved product direction and trivial tasks are outside this workflow.
---

# Plan Work

Turn an understood outcome into work another session can pick up safely, and
keep that representation aligned with what remains to do.

## Establish the execution context

Read the current assignment, its settled decisions and relevant system state.
For resumed work, verify the existing plan against the actual code, artifacts
and tracker; do not assume its counts or labels are current. Establish the
outcome, constraints, affected owners and observable completion evidence.
Separate unresolved product or domain decisions from implementation tasks.
A plan must not turn a guess about those decisions into an approved requirement.

Find the project's authoritative workboard, issue tracker or file convention
through its instructions and existing work. Confirm the access mechanism and
permitted effects. Reuse that owner; do not install a parallel tracker, prescribe
universal local paths or copy private upstream context into technical tickets.
If no owner exists, choose an accessible, proportionate place for the draft and
state it. Publishing to a shared tracker requires authorization for that effect.

## Cut verifiable work

1. Synthesize the agreed problem, intended behavior, material decisions,
   exclusions and acceptance evidence. Link primary details instead of copying
   entire conversations. Keep an unresolved fact visible with its next check.
2. Cut by outcomes that can be demonstrated or checked. A normal feature slice
   carries the technical layers its behavior needs, rather than creating one
   ticket per layer. Size the slice for coherent understanding and recovery.
   Sequence structural prerequisites when consumers genuinely depend on them.
3. Give each package its purpose, affected boundary, constraints, required
   inputs, acceptance evidence and actual blockers. Include concrete source
   locations when they help the next actor; verify them at handoff instead of
   forbidding paths merely because they can become stale.
4. Treat a broad migration on its own terms. State which intermediate states
   are valid, how they are checked and where integration proves completion.
   Do not promise an independently green slice that cannot exist, or silently
   introduce compatibility code to force the usual shape.
5. Check that an unblocked package can start with the information provided.
   Remove dependencies that only express a preferred order. Expose decisions
   about scope, delivery or external effects before publishing; do not demand
   a new approval for ordinary details within an already authorized plan.

## Keep and finish the work

Update the canonical record when a package changes state, evidence arrives or
a blocker is disproved. Keep unfinished work, shipped results and human judgment
distinct. Detailed planning belongs with active work; the future workboard needs
enough scouting to establish a real need, not a stack of stale execution plans.

At completion, reconcile the board, retain the outcome and needed evidence with
their owners, and remove the completed plan and disposable artifacts in the
same closeout. Transfer a still-needed decision or evidence pointer before
deleting its temporary carrier. Record genuine human judgment separately;
do not send an agent-verifiable check to the user as unfinished work.

Deliver or update the actual plan, its location and the next executable work.
A planning request does not itself launch implementation or send messages.

Adapted source methods are credited in [NOTICE.md](NOTICE.md).
