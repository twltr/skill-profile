---
name: engineering-review
description: Independently review software changes and their documentation against requirements, behavior, architecture and rendered UI. Resolve material questions with the implementer, record evidence-backed findings and recheck corrections on the current revision.
---

# Engineering Review

Review a concrete change against its intended result and actual evidence. The
reviewer must not be the author of the work being accepted. Implementers run
their own checks, but those checks are not independent review approval.

## A worked review exchange

Fictional change: a new cancellation screen and its payment status.

```text
Reviewer: At the narrow viewport, the select's chevron touches its right edge.
Observed on the provided build, in the cancellation form's open state.
Please correct the owning spacing rule and recheck the same state.

Reviewer question: Why does a timed-out refund appear as "refunded"?
The requirement distinguishes pending from confirmed. Is there provider evidence
that makes this outcome definitive, or does this state need to stay pending?

Implementer: There is no confirmation; the mapping was incorrect. I changed the
timeout outcome to pending and added the relevant behavioral check. The chevron
now uses the same inset as the other controls. Here is the revised build/evidence.

Reviewer: Rechecked the changed mapping and rendered narrow/wide form states on
the updated revision. Both findings are resolved; unrelated states remain covered
by the stated checks, not by assumption.
```

The question tests a real uncertainty without declaring an unproven bug. A
confirmed defect is a finding with evidence. Both belong in the review record;
neither needs a theatrical debate or an arbitrary numerical score.

## Establish an independent reviewer

Identify the authors of the affected change. The main agent can review subagent
implementation when it has the relevant capability and evidence access. Otherwise
delegate that judgment to a suitable independent reviewer. If the main agent
implemented the change, another agent must review it. Review authorship per
affected work, including material design/composition decisions, not merely by job title. An
agent who fixes a disputed part becomes an author of that part; obtain an independent
check of that correction rather than approving it itself.

If **Puppeteer** is available, use its phase/capability model routing to arrange
appropriate independent reviewers, scope access and coordinate responses. Use
real native agents; reuse an existing assignment that meets these requirements.
A separate context on the same model can be independent.
If no independent
reviewer is available, perform honest author verification and report independent
review as open; do not simulate a second opinion or call self-checks approval.

Provide the requirements, accepted decisions, baseline/current revision, relevant
diff, author verification and runnable or rendered access. Do not prime reviewers
with the implementer's conclusion. Review the actual current state, not merely
an earlier screenshot or a summary of what was supposed to change.

## Select the actual change

Split a mixed review by the questions that need different expertise: behavioral
correctness and contracts, visual presentation and interaction, and factual
agreement between a figure and the system it explains. A strong code reviewer
does not automatically establish visual quality. Give visual work to a capable
independent reviewer with the actual renders, including when the main agent is
not suited to judge them. The lead retains integration and evidence coverage;
it resolves factual discrepancies with evidence and does not manufacture a missing
specialist verdict. Use one capable reviewer when that suffices, or bounded
specialists when the work benefits; do not duplicate the complete review for each.

Establish whether the target is uncommitted work, a commit, a branch or an explicitly
broader assessment. For a branch review, resolve the intended target and its verified
upstream state, then inspect the diff from the merge base with HEAD. Comparing two
branch tips directly can attribute target-branch work to the proposal. Do not guess
an unavailable reference. Include staged, unstaged and relevant new files when the
requested target is local work; preserve unrelated changes.

Read the complete scoped diff and enough callers, contracts and tests to establish
the affected behavior. Finding one defect does not finish the remaining review.
Distinguish a regression introduced here from an existing issue. Broader architecture
or requirement assessments may legitimately address existing problems, but label
that scope instead of presenting them as newly introduced regressions.

## Review the result and its explanation

Establish the review phase. Road to Glory first requests implementation review,
then a separate review of documentation updated to match that accepted result.
A Phase 1 acceptance is not permission to merge before Phase 2. Review source
comments with code; review the durable README and documentation in Phase 2. If
the latter exposes a behavior defect, reopen the affected implementation review.

Trace the changed behavior through the affected boundaries. Check correctness,
regressions, failure states, contract compatibility, data ownership and verification.
Inspect the README and affected durable documentation in its review phase;
the complete change must leave source and explanation in agreement. A passing test does not excuse a false model,
duplicated owner, missing requirement or misleading documentation.

Use these supporting methods when available and relevant:

- **Engineering Practices:** assess justified language, pattern, protocol, framework
  and dependency choices, with current evidence where the choice is consequential.
- **Domain Modeling:** test meanings and names against actual scenarios and lifecycles.
- **Vertical Slices:** check coherent ownership, public boundaries and file/module placement.
- **MinMax Codebase:** assess system complexity, redundant owners and preserved behavior
  in review mode; do not turn a finding into an unrelated refactoring assignment.
- **Golden Comments:** check the explanation of reasons, models and invariants beside code.
- **Marshmallow Tests:** assess whether evidence distinguishes the relevant failures.
- **Good Writing**, its **Engineering Documentation** route and **Editorial SVG Diagrams**:
  assess README, agent instructions and durable docs against their distinct owners;
  check usable entrypoints, concise explanation and accurate primary visuals.
- **All or Nothing:** check whether an agreed replacement reached affected consumers
  and whether a purported completion still leaves the retired owner active.

Read a supporting method once for its specific contribution. Without it, apply
the bounded review criteria directly and disclose a material limit. Do not start
a chain of new workflows or ask a caller to invoke itself again.

## Inspect rendered UI and graphics in detail

For UI work, require the actual affected screen and relevant viewport sizes,
themes and interaction states. For diagrams, icons and other visual artifacts,
inspect their real embedding size and intended surfaces as well as semantic
accuracy. Use Editorial SVG Diagrams or SVG Design when available for the relevant
craft criteria. Builds, source inspection and component tests do
not prove visual quality. Use **Frontend Design** when available to assess the
established visual direction; use **Motion Design** when available for relevant
transitions and reduced-motion behavior. Do not invent a new aesthetic during review.

Check spacing and padding, optical/icon alignment, text clearance around chevrons,
typography, readable contrast, clipping, overflow, responsive behavior and the
states relevant to the change, including focus, error and disabled states. Verify
interaction and keyboard behavior when they are affected. A screenshot establishes
only the state it shows; inspect the real interaction where needed.

Obtain an independent read-only visual reviewer who did not author the affected
design or implementation. Use Puppeteer's current model-routing reference when
available rather than selecting by the parent's coding strength or a fixed role
name. The main agent performs the checks it can establish and integrates the
specialist's evidence; it does not need to duplicate or claim that visual judgment.
Additional perspectives may help substantial visual work; do not claim provider
diversity or access that the host does not expose. An image-capable model must
actually receive rendered evidence; an accessibility tree or markup is insufficient.

Return the screen/state, observed issue, consequence and reproduction or visual
evidence. Send justified fixes to the implementer and recheck the affected states
on the corrected build. Missing visual capability, an independent reviewer or
rendered access is a specific blocked check, not a reason
to ask the user to do all the routine visual work or to accept the UI unseen.

## Ask when the reason is materially unclear

Separate a reproducible defect from an uncertain rationale. For a material question,
state the observed choice, the requirement or evidence in tension with it and what
answer would resolve the concern. If **Grilling** is available, use its question and
recommended-answer pattern for a short exchange with the implementer; the implementer
is the respondent here, not the human user. Do not start a full human interview.

Evaluate the reply against evidence and consequences. Accept a supported reason,
request a correction or preserve an unresolved disagreement. Do not require a
question round for an obvious defect. Do not force unanimity by repeating the same
arguments or escalate technical choices the agents can settle themselves.

## Record findings and verify corrections

For remote work, publish actionable code findings on the relevant PR lines when
supported. Use PR review/comments for cross-cutting and UI findings. Record open
questions, meaningful answers, decisions, corrections and recheck results even
when agents also communicate directly. Link the actual revision and evidence.
Keep the issue informed of material blockers or changed scope; the active plan
retains relevant unresolved conditions without duplicating the entire transcript.

A finding states location, observed behavior, impact, evidence and the smallest
useful correction or missing decision. Do not pad a review with speculative defects,
preference-only rewrites or inventories of unaffected code. After remote writes,
confirm the provider's result; a local draft is not a posted comment.

Order actionable findings by impact. A compact priority label can distinguish a
release blocker (P0), urgent defect (P1), ordinary defect (P2) and worthwhile minor
correction (P3). Demonstrate the affected scenario and cite the smallest relevant
location in the change. Intentional behavior or personal style preference is not
itself a defect; unmet agreed UI or documentation requirements still are findings.
When no actionable issue is established, say so and report verification limits;
do not invent a finding to make the review look substantial.

Use a clear outcome: changes required, blocked on specified evidence, or reviewed
with stated checks and limits. Tie it to the reviewed revision. After changes,
recheck affected behavior and any newly exposed risk; previous approval does not
automatically cover new edits. Resolve a discussion only after its disposition
and required evidence are recorded.

Return the outcome to **Road to Glory** when available or to the existing work owner.
Road to Glory owns final cleanup, changelog, issue closure and merge sequencing.
This skill neither deletes plans nor merges merely because the review passed.
