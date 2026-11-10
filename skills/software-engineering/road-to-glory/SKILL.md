---
name: road-to-glory
description: Plan and maintain substantial Engineering work through roadmaps, executable plans, delegated work and verified completion. Coordinate remote issues and pull requests when available; keep small, clear tasks lightweight.
metadata:
  skill-type: flow
  skill-tree: software-engineering
---

# Road to Glory

**Flow skill** in Software Engineering. Use it as the orchestrating agent for substantial work; each phase names the role whose pack the Software Engineering domain loads.

Make what is actually left to do visible, executable and safe to resume. This
method keeps the roadmap and active execution plans aligned. Project-specific instructions or
an explicitly chosen external workflow may override these defaults; otherwise
use ROADMAP.md, versioned plans, CHANGELOG.md and .tmp/ for working artifacts. Local-only work needs no
separate ticket store; remote repositories also use their established issue tracker.

Establish whether the request is to plan, resume or execute. A
planning-only request creates the plan; it does not launch implementation. Publish
issues when the task includes the remote planning workflow. Reuse existing
authorization rather than asking again for each issue. Resolve defensible planning
choices from the brief and evidence. Report genuinely unresolved direction as an
explicit prerequisite, with dependent work blocked; do not invent a decision or
turn ordinary planning into a user interview. Mandatory host approval requirements
still govern actions outside the task's existing authority.

## Run each phase in its role

The lead holds the orchestrator role and switches role as the work moves. Each
phase names the role that runs it; when the lead switches, the Software
Engineering domain loads that role's pack. This flow names roles, not methods.

| Phase | Role | Condition |
|---|---|---|
| Plan: scout, decide, cut packages | Orchestrator | Ownership, concept and technology decisions are implementer judgments: take that role for them or give them to an implementer delegate. |
| Implement | Implementer, including every delegate | A delegate's brief carries the implementer pack in Puppeteer's `Skills:` field. |
| Review: implementation, then documentation | Reviewer, independent of the author | The lead does not approve work it authored. |
| Document | Documenter | Starts only after the implementation is accepted. |
| Close: board, changelog, cleanup, merge | Orchestrator | Starts only after both review phases succeed. |

## Scale the work before creating records

Reserve roadmap items for meaningful features, substantial changes or investigations
that need coordinated work or resumable state. A known local bug, a bounded rename,
a short verification or translating a small set of labels can usually be completed
directly. Keep their immediate steps in the harness's task list when useful; do
not manufacture a repository roadmap item, plan and issue for each small action.
Judge the actual uncertainty and affected contracts: a repository-wide public
rename or an unexplained cross-system failure may be substantial despite a short request.

For example:

| Request | Working shape |
|---|---|
| Add cancellation across ordering, inventory and billing | One meaningful roadmap outcome; scout the affected capabilities through Puppeteer, reconcile their contracts, then plan verifiable packages. |
| Rename one known private function and update its callers | Make the bounded change and run the relevant check directly; no new roadmap item or delegation. |
| Translate a small, identified set of UI labels into English | Revise and verify those labels directly; use a transient task list if needed. |
| Investigate an intermittent failure spanning multiple capabilities | Track the investigation when it needs resumable state and delegate bounded questions whose answers can be checked independently. |

The size of the repository alone does not decide the working shape. A small
repository can contain a difficult design decision; a large one can need a trivial fix.

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
compact: item, plan link, and a one-to-three-line description.
No architecture essays, completed-work diary or status narrative on the board.
Each item links its actual plan one-to-one. A future item's plan can be a small
record of its outcome, settled decisions and remaining questions; deepen it when
the item becomes active instead of inventing detail early.

**Remote issues expose the same work to collaborators.** When the repository has
a remote and an established issue tracker, create an issue for a meaningful
roadmap outcome or independently verifiable package. Link an active plan that
collaborators can actually access; a local path is not a remote plan link. Where
useful, link the issue from the roadmap. A remote alone does not prove that
a tracker is available: use the configured provider and verified access. If that
route is unavailable, retain the local plan and state the missing remote record.

Keep issue content useful without copying the whole plan:

- **Outcome and scope:** the problem, the resulting behavior and important exclusions.
- **Settled decisions:** the constraints needed to understand the assignment, with
  links to their canonical explanations.
- **Plan and current state:** the plan link and a compact externally useful status;
  the active plan owns detailed execution progress. Reconcile the issue at meaningful transitions.
- **Dependencies:** only work that genuinely blocks this outcome, linked by name.
- **Acceptance:** observable completion, required evidence and cleanup of the finished
  roadmap entry, active plan and temporary artifacts, plus the changelog entry.

For example, "Cancel an unfulfilled order" describes the cancellation behavior,
the reservation-release and payment outcomes, its actual blockers, its plan and
how completion is verified. It is not three tickets called "database", "API"
and "UI". Create separate packages only when they have meaningful outcomes.

For local-only repositories, ROADMAP.md and its plans are sufficient. Do not
add local issue files, a shadow tracker or a separate set of decision tickets.

**Versioned plans belong with the roadmap.** Use the repository's established
plan directory, or `plans/<descriptive-item-name>.md` when none exists. Keep one
plan per roadmap item and track it in local Git even without a remote. Do not put
the plan in an ignored temporary directory. Without Git, keep the same explicit
plan owner without pretending it is versioned.

**.tmp/ owns intermediate artifacts.** Keep disposable research, exploratory
scripts, screenshots and other working aids there, normally ignored by Git.
Do not commit raw agent transcripts or move temporary work into permanent docs.
Retain required evidence at its appropriate owner before deleting its carrier.

**CHANGELOG.md owns shipped outcomes.** When work finishes, remove the roadmap
row and record one compact, coherent entry describing what changed and why it
matters. Do not accumulate the raw sequence of internal deliberation.

**Pending evidence and blockers stay with the affected work.** Record them in the
active plan and reflect a blocking state on its roadmap item. Do not create a
separate VERIFICATION.md or a parallel acceptance board. Preserve genuinely
owner-only actions, unavailable access and explicit human preference decisions
with their exact prerequisite and next action. Distinguish implemented behavior
from evidence still missing; neither a screenshot nor a personal preference
question substitutes for a check the agent can perform.

## Cut a plan that can be executed

Use this plan skeleton, scaling its detail to the work:

| Part | Required content |
|---|---|
| **Outcome** | The resulting capability or state and its observable completion. |
| **Why This Block Exists** | The need this work addresses and why it belongs together. |
| **No-Go Constraints** | Behaviors, data boundaries and unrelated work that must be protected. |
| **Decisions and Reasons** | Chosen approach, supporting evidence, meaningful rejected alternatives and what would reopen the choice. Keep unresolved prerequisites distinct. |
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

## Delegate substantive work by default

The main agent establishes the objective, constraints and rough plan. For
substantive roadmap work, use `puppeteer`, when available, as the normal method for deeper scouting,
bounded implementation and independent review. Divide research before loading
the entire affected codebase into the main conversation. Give scouts coherent
capabilities or questions, then reconcile their evidence and dependencies into
the plan. Repository ownership and boundaries, unresolved concepts and
consequential technology decisions are implementer judgments: take the
implementer role for them, or give them to an implementer delegate, so the domain
loads that role's methods.

During deeper planning of a substantial feature or repository, convene a council:
let scouts question the main agent and challenge its decisions before
implementation. Supply the current scope and plan; receive the reconciled
decisions, reasons, evidence, rejected alternatives and remaining blockers. The
council asks the user no questions, including when a technology or
current-practice question prompted it. Keep its questions between agents; do not
relay them as a clarification round or start an interview of the user.
Record the result in the owning plan, with unsupported choices still unresolved.
A small, clear task does not need a council. If the council handed work to this
plan, continue from its settled decisions instead of recursively starting it again.

For example, scouts challenge whether cancellation should treat a payment timeout
as a confirmed refund. The lead chooses a pending outcome from the verified provider
contract. The plan records that decision, its evidence, why "confirmed" was rejected
and which owner reconciles the pending operation. The user receives the outcome
and reasoning, not the agents' question. If the provider contract is inaccessible,
that exact dependency stays blocked in the plan instead of being guessed.

Handle a small, clear item directly when briefing and integrating another agent
would cost more than completing and checking it. Existing understanding, uncertainty,
independent work and the value of a second view matter more than agent count.
Run independent assignments in parallel when supported; settle shared contracts
and serialize dependent or shared writes. Puppeteer owns the delegation mechanics;
a delegated worker is an implementer, and its brief's `Skills:` field carries
the implementer pack so the worker loads those methods itself.
Direct implementation of a small task does not waive an independent review of
work being accepted or the detailed verification required by an affected UI.

Critical work needs tighter boundaries and verification, not an automatic ban on
delegation: an independent read-only investigation or review may be valuable while
the main agent retains a sensitive mutation. Follow the actual host capabilities
and task restrictions; if agents are unavailable, state that limitation and proceed
serially where the authorized task can still be completed correctly.

Use Puppeteer's phase/capability routing when available: planning can retain a
suitable strong model, while implementation with settled contracts normally goes
to a sufficient efficient worker. Route visual design and graphics to an appropriate
author, even inside an otherwise routine refactor; assign a separate capable
reviewer. A plan file does not make unresolved or high-consequence work mechanical.
Record meaningful model choices and available whole-task usage/rework observations
at this plan's owner when they inform the next assignment; do not create another
model list or usage board here.

The main agent retains steering, cross-domain decisions, integration and assurance
that required acceptance evidence is complete. It delegates specialist judgments
it cannot establish itself. Verify decisive returned evidence without repeating every delegated read.
Delegation never substitutes for understanding the decisions needed to own the result.

## Maintain the plan while work happens

The active plan is live control state, not an end-of-run retrospective. Reconcile
it when an item changes state, evidence arrives, a commit lands, a worker returns
or a blocker is disproved. Check it before assigning more work or reporting status.
Keep deferred and owner-led work visible; stale totals and omitted follow-up hide
what remains just as effectively as a false completed label.

Record a blocker when it appears: the affected outcome, the exact missing access,
input or decision, what was tried, what can still proceed and what will unblock it.
Continue independent work. For remote work, post a concise issue comment for a
material blocker, intermediate result, changed decision or completed verification.
Link the evidence and next step so a person can reconstruct progress. Keep the
issue's summary current without copying every tool call or internal conversation.

Read the plan yourself before implementing it or delegating a well-specified
piece. Verify a returned finding against the actual source before turning it into
another plan item; a worker's internal step does not automatically deserve a
separate roadmap entry or remote issue.

## Verify the result and review the details

Perform every verification the agent can carry out with available tools and
access. UI work includes the rendered interface and its interactions; source,
type checks, builds and component tests alone do not establish visual correctness.
Use the actual affected screen and relevant viewport sizes, themes and states.
Inspect spacing, padding, alignment, typography, readability, contrast, clipping,
overflow and focus or error states, including hover or disabled states where relevant.
Preserve the agreed visual direction while checking these details.

For example, a select input can pass its tests while its chevron touches the right
edge. Render it at the narrow and wide layouts, inspect the icon inset and text
clearance, correct the owning style, then revisit those same states. An icon
button also needs visual centering and comfortable spacing; a screenshot of a
different control does not verify the reported defect.

For an implemented UI or graphic change, use Puppeteer, when available, to obtain
a separate capable read-only visual review by an agent who
did not author the affected work. The main agent performs its own supported
behavioral/integration checks and retains the specialist's visual findings; it
does not claim visual acceptance when that judgment exceeds its capability.
Visual judgment against the actual brief and existing design system is design
review, which the lead runs from the middle as a separate step. Give the reviewer the intended behavior, exact build or
revision, screen access or screenshots, relevant states and checks already run.
Ask for reproducible findings with location, observed defect, consequence and
evidence; do not seed the review with the implementer's approval or a target score.

The main agent reconciles findings against the requirements, sends justified
corrections to the implementation owner and obtains a fresh specialist check of
the changed states. A review of an older build
does not approve a newer one. Independent agent agreement supports judgment; it
does not replace rendered or behavioral evidence. If an independent agent or the
needed visual capability or rendered access is unavailable, identify that specific open verification instead
of claiming the review happened or sending routine agent checks to the user.

Escalate only the part that actually needs a human, such as access the agent cannot
obtain or a personal preference not determined by the brief. State the exact action
or decision needed. Keep implementation completion, checked behavior and any
outstanding human condition distinct in the active work record.

## Review in two phases

Independent acceptance runs in the reviewer role; the domain loads its pack for
whoever takes it. The main agent may review implementation by others when
qualified and able to inspect it; otherwise it assigns a suitable reviewer. If it
authored the work, another agent must review it. Author checks never count as
independent approval. If the reviewer's methods are unavailable, preserve the same
independence and evidence requirements through native tools. If no independent
reviewer is available, record the open gate rather than approving one's own work.

### Phase 1: implementation and code review

Implementers complete the feature and its behavioral verification, including
rendered UI and independent detail review where relevant. They update source
comments that explain the changed mechanism as part of the code. The reviewer
then reviews requirements, correctness, architecture, tests and those
explanations before the broad documentation refresh is commissioned, applying
the criteria for complexity, ownership and boundaries, technology choices and
reason comments where relevant. Return defects to the author and recheck the
corrected implementation. Passing this phase does not finish the PR.

### Phase 2: documentation and documentation review

Once the implementation is accepted, give its reviewed revision, behavior and
changes to bounded documentation scouts through **Puppeteer**, when available.
They inspect the affected README, repository agent instructions, setup instructions, contracts, diagrams and
explanations, returning stale or missing material with exact locations and reasons.
The main agent reconciles the findings and assigns the documentation update to
the documenter role.

The documenter makes the update with that role's methods, including **Unslop**
when available for the assembled wording. Use **Editorial SVG Diagrams**
when available to make relationships and flows visible and replace the paragraphs
the figure makes unnecessary. Keep README purpose and quick start concise, link deeper durable
knowledge and preserve essential reasons and conditions. No transient progress
notes, "since the last update" appendices or agent diaries belong there; their
owners are the plan, roadmap, issue, PR or changelog.

Have an independent reviewer check the resulting documentation against the accepted
implementation, including runnable setup instructions, resource links, diagram
accuracy and rendered legibility where relevant. A documentation author does not
approve its own work. Both phases belong to the same work item and PR. If this
phase reveals a behavior defect, return the affected part to Phase 1, then update
and recheck its documentation against the corrected result.

For example, documenting a refund as confirmed while the implementation review
has not yet settled its timeout behavior creates avoidable rework and can preserve
a false promise. First review the pending-versus-confirmed contract; then document
that accepted behavior and review the explanation. Separating the phases narrows
each review and prevents provisional implementation decisions becoming durable truth.

Only after both phases succeed does final cleanup begin. For a documentation-only
request, skip the absent implementation phase rather than inventing code work.
For a change with no affected durable documentation, the documentation audit records
that conclusion and its reason; it does not add filler just to produce a diff.

## Make remote review traceable

For remote implementation work, prefer a task branch and open or update its pull
request when there is a concrete reviewable change. Reuse an existing PR for the
same work. Follow the repository's draft/readiness conventions. Link the issue
and accessible plan, describe the problem and resulting behavior, and report the
checks actually performed with any limits.

Put actionable code findings on the relevant PR lines where supported. Record
cross-cutting or visual findings in a PR review or comment with the screen, state,
revision and useful evidence. Explain what is wrong and why it matters so the
implementer and a later human reader can act on it. Return failed work to its owner.

For each material finding, record the correction and recheck, or a reasoned
disagreement backed by evidence. Resolve a thread only after its disposition is
recorded and required verification is complete. Keep meaningful review rounds,
remaining blockers and the final verification result visible on the PR; reconcile
the linked issue at milestones. Confirm remote writes by reading back the provider's
result. A prepared comment or local report is not a published review.
Material questions and the implementer's answers belong in that record even when
agents also exchanged them directly. The reviewer role's methods own the
questioning and finding format; this workflow owns progress and closure.

## Close the work in the same slice

After independent review succeeds, update the board, retain the necessary outcome
and evidence with their owners, add the CHANGELOG entry and delete the completed
versioned plan. Remove orphaned plans and temporary helpers whose job has ended.
Do not remove an artifact still needed by another active item; move its useful
content to the proper owner before deleting its temporary carrier.

For remote work, make this cleanup part of the reviewed change before merge.
Include it in the branch/PR and have an independent reviewer check the final cleanup
diff and relevant checks before merging; do not add unreviewed behavior under cleanup.
When the change supersedes an existing owner, have the reviewer verify complete
retirement of the affected old owners. Merge or publish only within the task's
established authorization.
Preserve a useful historical plan link by pinning it to its last committed revision
before removal, or retain the necessary decision summary in the issue when the plan
was never remotely accessible. Close the issue only when its acceptance conditions
are met; an implementation merge alone does not settle an outstanding human decision.

For example, a completed capability leaves ROADMAP.md, appears once in
CHANGELOG.md and loses its active versioned plan. If required UI access is still missing,
record "implementation complete; rendered verification blocked" in the plan and
remote issue where present, and keep the affected work open until its acceptance
condition is met. Do not silently convert missing evidence into a shipped claim.

Return the canonical plan or updated work state, its location, the next executable
step and any real blocker. Keep task state in these owning files, not durable
assistant memory. The planning artifacts serve the work; small changes that can
be completed directly do not need the whole apparatus.

Supplementary specification and work-package techniques are credited in
[NOTICE.md](NOTICE.md).
