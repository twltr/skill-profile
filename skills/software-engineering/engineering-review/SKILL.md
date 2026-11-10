---
name: engineering-review
description: Independently review software changes and their documentation against requirements, behavior, architecture and rendered UI. Resolve material questions with the implementer, record evidence-backed findings and recheck corrections on the current revision.
metadata:
  skill-type: parent
  skill-tree: software-engineering
---

# Engineering Review

**Parent skill** in Software Engineering; applies its lenses together where they are relevant.

Review a concrete change against its intended result and actual evidence. Two
things make a review worth having. It is **independent**: the reviewer did not
author the work being accepted, so implementers' own checks are evidence, not
approval. And its findings are **true**: each one was checked before it was
reported, because a false finding costs the implementer a round trip and teaches
them to skim the next review.

## A worked review exchange

Fictional change: a cancellation screen and the refund status behind it.

```text
Finding 1 [P1, confirmed]: refunds/status.py:58 maps a provider timeout to
REFUNDED. The requirement separates pending from confirmed, and nothing confirms
the refund. A customer whose request timed out sees "refunded" and may never be
paid. Reproduced with the timeout fixture. Smallest fix: map the timeout to
PENDING and leave confirmation to reconciliation.

Finding 2 [P3, confirmed]: at 360 px the select's chevron touches its right edge
in the form's open state (screenshot attached). Other controls use the shared inset.

Question 1: refunds/client.py:30 retries on every exception, including 4xx
responses. Is a 409 from the provider ever retryable? Recommended answer: no;
retry only timeouts and 5xx.

Dropped before reporting: refund_status() can return None, but its only caller
treats None as pending (refunds/views.py:41).

Implementer: Timeout now maps to PENDING, with a behavioral test. 409 is not
retryable, so the client retries only timeouts and 5xx. The chevron uses the
shared inset. Revised build at <revision>.

Reviewer: Rechecked on <revision>. The new test fails on the old mapping and
passes on the new one; narrow and wide form states render correctly; the retry
change adds no new path. All three resolved. Not covered: live provider
behavior, which no stated check reaches.
```

The question tests a real uncertainty without declaring an unproven bug; the
dropped candidate did not survive checking, so it cost the implementer nothing.
Severity and confidence are stated separately, and the recheck names what it did
not cover.

## Establish an independent reviewer

Establish who authored each affected part, including material design and
composition decisions, not only who holds which job title. The main agent can
review a subagent's implementation when it has the capability and evidence
access; if the main agent implemented the change, another agent reviews it. An
agent who fixes a disputed part becomes an author of that part, so its
correction needs an independent check too.

If **Puppeteer** is available, use its model routing to arrange suitable
independent reviewers, scope their access and coordinate responses; reuse an
existing assignment that meets these requirements. A separate context on the
same model can be independent. If no independent reviewer is available, perform
honest author verification and report independent review as open; do not
simulate a second opinion or call self-checks approval.

Give reviewers the requirements, accepted decisions, baseline and current
revision, the relevant diff, the author's verification and runnable or rendered
access. State the change's intent, but do not prime reviewers with the
implementer's conclusion that it works. Review the current state, not an earlier
screenshot or a summary of what was supposed to change.

## Select the actual change

Split a mixed review by the expertise its questions need: behavior and
contracts, visual presentation and interaction, and factual agreement between a
figure and the system it explains; a strong code reviewer does not thereby
establish visual quality. Use one capable reviewer when that suffices, or bounded
specialists without duplicating the whole review for each. The lead keeps
integration and evidence coverage and does not manufacture a missing verdict.

Establish whether the target is uncommitted work, a commit, a branch or an
explicitly broader assessment. For a branch, resolve the intended target and its
verified upstream, then diff from the merge base to HEAD; comparing two branch
tips attributes the target branch's work to the proposal. Do not guess an
unavailable reference. For local work, include staged, unstaged and relevant new
files, and preserve unrelated changes. If the same revision was already reviewed
and nothing changed, say so rather than reviewing it again; scale the depth of a
trivial or generated change to its risk.

Read the complete scoped diff and enough callers, contracts and tests to
establish the affected behavior. Finding one defect does not finish the review.
Distinguish a regression introduced here from an existing issue; a broader
assessment may address existing problems, but label them as such.

## Review the result and its explanation

Substantial work is reviewed in two phases: first the implementation, then,
separately, the documentation updated to match the accepted result. Accepting
phase 1 is not permission to merge before phase 2. Review source comments with
the code and durable README and documentation in phase 2; if the latter exposes a
behavior defect, reopen the implementation review.

Trace the changed behavior through the affected boundaries: correctness,
regressions, contract compatibility, data ownership and verification. Give
failure paths their own pass — errors swallowed or logged and ignored, broad
catches that hide unrelated failures, defaults and fallbacks that make an outage
look like a valid result. A passing test does not excuse a false model, a
duplicated owner, a missing requirement or misleading documentation.

Apply these criteria where relevant, from the methods the domain loaded for the
reviewer role:

- **Technology choices:** justified language, pattern, protocol, framework and
  dependency choices, with current evidence where the choice is consequential.
- **Domain language:** meanings and names tested against actual scenarios and
  lifecycles.
- **Ownership and placement:** coherent ownership, public boundaries and
  file and module placement.
- **Reason comments:** reasons, models and invariants explained beside the code,
  and still true of it.
- **Test evidence:** whether the evidence distinguishes the relevant failures.
- **Documentation:** README, agent instructions and durable docs against their
  distinct owners; usable entrypoints, concise explanation and accurate primary
  visuals, with **Editorial SVG Diagrams** for explanatory figures.
- **Complete replacement:** whether an agreed replacement reached its consumers,
  or a purported completion leaves the retired owner active.

Add this skill's own lenses when the change calls for them:

- **MinMax Codebase:** system complexity, redundant owners and preserved
  behavior, in review mode; a finding does not become a refactoring assignment.
- **Improve Codebase Architecture:** for an explicitly broader assessment,
  language and architecture choices down to interfaces, names, modules and
  files, reported as prioritized, evidence-backed findings.

Read each lens or loaded method once for its contribution. Without one, apply
the criteria above directly and disclose the limit. Do not start a chain of new
workflows or ask a caller to invoke itself again.

## Inspect rendered UI and graphics

For UI work, require the affected screen at the relevant viewport sizes, themes
and interaction states; for diagrams, icons and other visuals, their real
embedding size and surfaces as well as their semantic accuracy. Builds, source
inspection and component tests do not prove visual quality, and a screenshot
establishes only the state it shows. Judging visual direction, motion,
iconography or accessibility is design review: hand that part back to the agent,
which runs it from the middle, and do not invent a new aesthetic here.

Check spacing and padding, optical and icon alignment, text clearance around
chevrons, typography, contrast, clipping, overflow, responsive behavior and the
states the change touches, including focus, error and disabled. Verify
interaction and keyboard behavior when they are affected.

Obtain a read-only visual reviewer who did not author the design or
implementation, chosen through Puppeteer's model routing when available rather
than by coding strength, and give it rendered images; markup or an accessibility
tree is not visual evidence. Missing visual capability, reviewer or rendered
access is a specific blocked check: report it rather than accept the UI unseen or
hand the routine visual work to the user.

## Verify each candidate before reporting

Treat every suspected issue as a hypothesis and try to refute it:

1. **Confirm it happens.** Re-read the location and enough of its callers,
   tests and configuration to show the behavior occurs, not merely that a diff
   hunk read alone suggests it could.
2. **Rule out the usual false positives.** The issue predates this change; the
   surprising code is correct and its reason is documented nearby; a configured
   linter, type checker or test already catches it; the code deliberately
   suppresses it with a stated reason; or it is a style preference no rule asks
   for.
3. **Quote the rule.** A guideline finding cites the exact sentence and confirms
   that it covers this file; repository instruction files apply to their own
   directory and below.
4. **Classify by evidence:**

| Evidence | Record as |
|---|---|
| Reproduced, or traced end to end through the code | Finding, confirmed |
| Strong reading of the code, not executed | Finding, with the check that would confirm it |
| Depends on intent, an unknown input or an unsettled requirement | Question to the implementer |
| Refuted | Dropped; mention it only if the implementer would otherwise wonder |

Confidence and severity are independent: a certain typo is P3, and a plausible
data-loss path is a P0 question until it is settled. When candidates come from
delegated reviewers, check each decisive claim against the code before adopting
it; for a release-blocking candidate, an independent agent can re-check that one
claim with only the claim, the requirement and code access.

## Ask when the reason is materially unclear

For a material question, state the observed choice, the requirement or evidence
in tension with it and what answer would resolve the concern. Ask only questions
whose prerequisites are settled, number them and give your recommended answer to
each, in a short exchange with the implementer; the implementer answers here,
not the human user, so do not start a full interview.

Evaluate the reply against evidence and consequences: accept a supported reason,
request a correction or record an unresolved disagreement. An obvious defect
needs no question round. Do not force unanimity by repeating arguments, or
escalate technical choices the agents can settle themselves.

## Record findings and verify corrections

Order findings by impact with a compact label:

| Label | Meaning |
|---|---|
| P0 | Blocks release: data loss, security exposure, broken build or core path |
| P1 | Urgent defect on a path users or operators will hit |
| P2 | Ordinary defect or unmet agreed requirement |
| P3 | Worthwhile minor correction |

A finding states its location, observed behavior, impact, evidence class and
the smallest useful correction or missing decision. Intentional behavior and
personal preference are not defects; unmet agreed UI or documentation
requirements are. Do not pad a review with speculative defects, rewrites of
taste or inventories of unaffected code. When nothing actionable is established,
say so and report the verification limits.

For remote work, post code findings on the relevant PR lines when supported, and
cross-cutting or UI findings in the review body:

- One comment per distinct issue; an issue that recurs names its other locations
  instead of repeating itself.
- Offer a ready-to-apply suggestion only when applying it fully fixes the issue;
  otherwise describe the fix.
- Link code at the reviewed revision's full commit hash, so the link still shows
  the reviewed lines after later pushes.
- After a remote write, confirm the provider's result; a local draft is not a
  posted comment.

Record questions, answers, decisions, corrections and recheck results, linked
to the revision and evidence, even when agents also talk directly. Keep the issue
informed of material blockers or changed scope; the active plan keeps unresolved
conditions without copying the transcript.

Close with a clear outcome tied to the reviewed revision: changes required,
blocked on specified evidence, or reviewed with stated checks and limits. After
corrections, recheck the affected behavior and any newly exposed risk; an earlier
approval does not cover new edits. Resolve a discussion only once its
disposition and evidence are recorded.

Return the outcome to whoever owns the work. That owner handles cleanup,
changelog, issue closure and merge sequencing; this skill neither deletes plans
nor merges because the review passed.
