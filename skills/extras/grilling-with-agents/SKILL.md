---
name: grilling-with-agents
description: Develop a plan through domain scouting and iterative questioning between specialist agents and the lead agent. Resolve design decisions, expose consequential uncertainty and return a reasoned decision report or planning handoff for a repository, feature or conceptual task.
metadata:
  skill-type: leaf
---

# Grilling with Agents

**Shared leaf skill** outside every tree, usable from any domain; a person starts it by name, and a routing skill may only suggest it.

Questions follow a **design tree**: every decision branches into the decisions
that hang off it. Work in **rounds**. The frontier is the in-scope decisions whose
prerequisites are settled; ask the whole frontier together, number each question,
give a recommended answer, and settle it before opening the branches that depend
on it — asking earlier would decide against facts the next answer may change. If
**Puppeteer** is available, use it for delegation mechanics; without it, keep this
method's scoped briefs, dependency-aware questions and evidence checks, and never
pretend a method was loaded.
The lead agent is the interviewee and decision owner within the user's brief;
specialist agents challenge that lead. The user receives decisions, reasons and
remaining limitations, never interview questions from this method. Keeping the
questioning inside the agent team lets it work through alternatives without
turning every engineering trade-off into homework for the user.

Unlike an interview with a person, every decision here belongs to the lead agent
within the user's brief, and the next round waits for the lead's answers, not the
user's; the result is the report-only outcome below. Keep facts separate from
decisions. When the user wants to be interviewed, that is a separate method they
start themselves; do not start it as a fallback or run it alongside this council.

## A worked feature example

Fictional request: add cancellation of unfulfilled orders to an existing shop.
The brief says inventory must be released and payment handling must be explicit.

The lead identifies ordering, inventory and payment as investigation areas, then
assigns bounded scouts before reading every implementation itself. These are
questions about existing owners, not three implementation tickets split by layer.

```text
Lead -> Payment scout
Investigate payment outcomes when an unfulfilled order is cancelled.
Inputs: the verified payment entrypoint, relevant tests and the current contract.
Read-only. Challenge my design with dependency-aware questions, one round at a time;
I am the interviewee, and this council never asks the user questions.
Return source-backed facts, unresolved decisions, your recommendation and
the consequences for other capabilities. Ask me, not the user.

Scout -> Lead
The current provider can return an indeterminate result after a timeout.
Should that count as refunded?
Recommendation: no; retain an explicit pending outcome and reconcile it.

Lead -> Scout
Agreed. A timeout is not evidence of a refund. Keep cancellation and the
payment outcome distinct. Check which existing owner can reconcile it.

Scout -> Lead
The existing payment reconciler can own this. However, retried cancellation
requests could start another refund unless they share a stable operation key.

Lead -> Scouts
Use the same cancellation operation identity for retries. Ordering owns the
cancellation lifecycle; payment owns the refund outcome. Recheck the inventory
and UI contracts against these decisions, including a pending refund.
```

The lead resolves ownership, retry behavior and honest status from the brief and
evidence. It also gives the scouts a bounded release decision to challenge:

```text
Lead -> Scouts
Plan whole-order cancellation for this release. Partial cancellation introduces
allocation and partial-refund rules beyond the requested outcome. Check for an
existing contract or requirement that would make that scope insufficient.

Report / active plan
Decision: whole-order cancellation; partial cancellation is outside this release.
Reason: it satisfies the supplied outcome without inventing allocation rules.
Reopen if: an existing contract or an explicit requirement needs partial cancellation.
Evidence: the scouts' verified contract locations and their remaining limitations.
```

The lead records that choice as its scoped decision, not a preference supplied by
the user. If a decisive contract cannot be inspected, the dependent scope remains
unresolved in the report. Neither a question to the user nor a guessed contract
is used to close the gap.

## 1. Establish scope and authority

Read the user's objective, existing decisions, constraints and intended output.
Distinguish a whole repository, a bounded feature and conceptual work. Establish
what is already authorized: investigation, plans, local repository creation,
implementation and remote publication are different effects. Reuse authorization
already present; the council does not create additional permission.

Gain enough orientation to assign useful investigations without preloading the
whole codebase. Use real native subagents and their actual capacity. If agents
are unavailable, report that this method cannot run as specified; do not simulate
independent reviewers inside one answer.

## 2. Assign independent investigation areas

Use Puppeteer, when available, for briefs, native tools, boundaries, context economy
and result verification. Assign coherent domains, capabilities or decision questions rather
than mandatory personas or one agent per folder. Scale to the work and available
slots; use waves where parallel capacity is limited.

Reuse the caller's selected decision dimensions. A new application calls for a
broad initial assessment; a feature calls for its affected concerns. Assign a
coherent topic or independent subquestion, not automatically one agent per listed
concept. A difficult topic may benefit from several independent investigations.
Supply shared requirements and cross-topic dependencies, then challenge whether
the combined decisions still hold together. For example, data recovery and
security findings may constrain each other; neither scout owns that combined
trade-off alone. These are investigation boundaries, not implementation layers.

For engineering, use **Vertical Slices** when available for responsibility,
interfaces, dependencies, invariants and Shared Machinery. Perform active domain modeling: distinguish
overloaded terms, test definitions with counterexamples, compare them with actual
behavior, and keep settled language at its existing owner. If **Domain Modeling**
is available, use it for those decisions; do not claim an uninstalled skill
was invoked or create a competing glossary by default.

If **Engineering Practices** is available, use it for unresolved language, framework,
protocol, architecture and dependency choices, with current primary evidence. If
it is the caller or an active ancestor, challenge its supplied alternatives and return the decision;
do not invoke it recursively or start a new research council inside the council.

Repository and module names should express settled concepts and avoid collisions.
Check an existing naming convention before inventing one. A name for a local
engineering repository may be chosen from a clear brief; a public brand or an
ambiguous product identity may depend on a human preference. Record an unsettled
identity as unresolved; do not invent the preference or turn it into an interview.

When an interface has a consequential trade-off, ask independent agents for
different designs under the same constraints. Compare caller knowledge, ownership,
failure behavior, testability and likely change. Do not require alternatives for
obvious decisions or import another skill's vocabulary over the project's own.

## 3. Run the question-and-answer loop

Each scout returns a compact batch:

```text
Area and inspected revision:
Facts and exact supporting locations:
Question whose prerequisites are settled:
Recommended answer and reason:
Alternative worth considering:
Affected owners and dependent decisions:
Uncertainty or missing evidence:
```

The lead checks decisive evidence, deduplicates questions and answers those that
can be decided from the task, established practice and verified facts. Identify
a chosen trade-off as a decision, not a fact learned from the user. Keep reasons,
rejected alternatives and unresolved conditions with the active design or plan.

Return the decision and reasoning to affected agents. Ask them to challenge it
against their evidence, revise their understanding and expose newly unblocked
questions. Agents need not agree for social reasons. Resolve disagreement with
facts, counterexamples or a discriminating check; retain material dissent when
the evidence is insufficient. Revisit an earlier choice when new evidence defeats it.

Investigate factual gaps directly or through an appropriate scout. A deterministic
lookup does not need another agent. A blocked fact delays only decisions that
depend on it. Do not mistake absence of evidence for absence of a problem.

## 4. Resolve within the team; report unresolved prerequisites

Use one rule for every entry: this method asks the user no questions. It applies
when the user invokes it directly and when another authorized workflow uses it.
There is no question-budget option or separate technical mode. A caller must not
relay council questions to the user or start a human interview to work around
this boundary.

Decide from the supplied requirements and verified evidence. Choose defensible
trade-offs within the brief, label assumptions and return the reasoning to the
affected agents for challenge. Do not seek approval of routine choices merely
because alternatives exist.

If a missing fact, conflicting requirement, genuine preference or authorization
prevents a defensible decision, record the exact prerequisite, affected outcome,
evidence already checked and what would resolve it. Continue independent work and
leave the dependent part blocked. For example: "Deployment target unresolved;
the brief supplies neither the environment nor access to its configuration.
Hosting-specific design remains blocked pending verified environment details."
This is a status statement, not a disguised question or an approval request.

No-question behavior does not invent facts, user preferences, access or consent.
Mandatory host approval requirements still govern external actions; the council
cannot supply approval or bypass them. A user who wants to be interviewed can start
that separately. This method finishes with the useful result it can
support and its explicit limitations.

## 5. Converge and hand off

Stop when material requirements have owners, boundaries and checks; the active
decision frontier is empty or explicitly blocked; and new challenges no longer
reveal a substantive contradiction. Repeating the same arguments without new
evidence is a reason to change the investigation, not to run endless rounds.
Consensus or a numerical score is not proof of correctness or a perfect design.

Summarize decisions the lead made, why they were made, relevant evidence, rejected
alternatives, previously supplied user decisions, remaining assumptions and what
would reopen an important choice. Direct invocation returns that report to the
user without questions or a confirmation gate. It does not automatically start
Road to Glory or create planning artifacts before the requested planning scope
calls for them.

When a workflow called the council, return the same result to that owner. If a
Road to Glory plan already owns the work, integrate decisions, reasons, evidence,
rejected alternatives and unresolved prerequisites there, including when the
immediate caller was Engineering Practices or State of the Art. Do not leave the
rationale only in chat or create a parallel council log.

For engineering work that includes roadmap planning, if **Road to Glory** is
available, hand off with:

- The repository purpose, name and source location, or the bounded feature owner.
- Domain language, capability boundaries and public interfaces.
- Invariants, meaningful alternatives and chosen trade-offs.
- A whole-scope roadmap with coarse later items where uncertainty remains.
- One plan for each roadmap item. Active plans contain decisions, dependencies
  and evidence; future plans may contain only the outcome, settled decisions and
  remaining questions. Do not invent detail to fill out a future plan.
- Verification needs, including rendered UI and independent review where applicable.
- Remote issue/PR expectations when a remote exists; local work needs no ticket store.

For other requests limited to a decision report, return it to the caller or user
without creating repositories, plans or tickets. When planning is in scope but
Road to Glory is unavailable, preserve the decisions and next work at the task's
existing planning owner.

Create a missing local repository when repository creation is part of the authorized
task and its destination is settled. Otherwise provide the concrete proposal and
name the unresolved destination. Planning alone does not authorize product
implementation or remote publication. Road to Glory owns planning artifacts and
lifecycle; this skill does not start another council when it returns to that caller.

## Another example: a new repository

Fictional brief: build a small reservation service for shared equipment.
Domain investigation distinguishes Equipment, Reservation and Checkout: reserving
an item and physically collecting it are different events with different lifetimes.
An architecture scout challenges who prevents overlapping reservations; an operations
scout checks the requested deployment constraints. The lead chooses one owner for
availability, a public reservation operation and a clearly named repository. The
roadmap covers reservation, collection/return and notifications without inventing
detailed future schemas. The first active plan proves that overlapping requests
cannot both reserve the same equipment. If the brief supplies no rental-policy
rule needed for pricing, record that exact gap and leave pricing-dependent work
blocked; return the supported reservation design and its reasons without questions.

## Another example: conceptual work

Fictional brief: plan an internal onboarding guide. Agents inspect the existing
audience, process and source material. They ask the lead whether a step applies
to all staff or only a specialist role, challenge duplicated ownership and test
the proposed sequence against a new starter's first week. The lead resolves clear
structure decisions from the brief and reports any unresolved audience priority
as a limitation without asking the user. Return an outline, decisions, reasons
and source gaps at the document's owner; do not create an engineering repository,
roadmap or issue tracker for a writing task.


Source influences are recorded in [NOTICE.md](NOTICE.md).

Direct entry is explicit. A declared step in an authorized planning workflow may
resolve and read this method deliberately when the host permits composition;
merely encountering a complex task does not bypass native invocation controls.
