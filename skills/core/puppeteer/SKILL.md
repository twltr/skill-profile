---
name: puppeteer
description: Decide whether to hand work to native subagents, then cut it into independent assignments, brief each agent, choose its model for the phase and check what comes back. Use when work could be investigated, implemented or reviewed in parallel, needs an independent reviewer, or needs a delegate model chosen, even if the user only says "use agents", "parallelize this" or "get a second opinion". Review criteria belong to Engineering Review; this skill only arranges the reviewer. Not the Puppeteer browser-automation library.
metadata:
  skill-type: core
---

# Puppeteer

**Core skill.** On the agent's surface and usable in any context.

Delegation fails in four predictable ways. The lead's context fills with raw
exploration until it can no longer steer. A confident summary is accepted as a
verified result. Two agents write the same migration, lockfile or contract and
contradict each other. And a task lands on a model that is wrong for its phase:
an expensive model on settled typing, or a weak one on an unresolved design.

This skill prevents each failure with one move. Scouts return **evidence, not
narratives**, so the lead's context holds conclusions with their sources. Every
return is **a claim to check**, not a result. Work is cut at **stable boundaries
with one writer per shared resource**. The model is chosen **per phase and
capability**, not per habit. The lead keeps requirements, cross-cutting
decisions, integration and the final acceptance; delegating a part never
delegates responsibility for the whole. Coordinating acceptance does not mean
personally certifying every part: delegate the specialist judgments the lead
cannot competently make.

## A scout and a useful return

For a cancellation feature, the lead identifies ordering, inventory and payment
as affected capabilities before reading all three implementations, then sends
one scout per capability. An illustrative brief, using every field of the
[brief template](#3-brief-each-agent):

```text
Task:       Find inventory behavior when an unfulfilled order is cancelled.
Outcome:    Source-backed behavior and the decisions cancellation still needs.
Inputs:     Reservation entrypoint at 4f2c1e9, current contract, inventory tests.
Must hold:  Reserved stock is never double-released.
Skills:     None; a read-only scout needs no method pack.
Boundary:   Read-only tools; inventory ownership only; no further agents.
Shared:     The order-state contract is owned by the lead; report, don't change.
Evidence:   Exact file:line for each behavior claim.
Stop if:    Behavior depends on an unsettled payment decision.
Return:     Findings, what was not verified, the smallest next decision.
```

The return the lead wants back is short and checkable:

```text
Finding:      Reservations expire after 15 min (inventory/reserve.ts:88);
              cancel ignores already-released stock (inventory/cancel.ts:41).
Not verified: Refund ordering; payment code was out of scope.
Next:         Lead decides whether cancel-after-expiry succeeds or is a no-op.
```

The lead opens the two cited lines, settles the public outcome and passes it to
the ordering scout. The other scouts keep working until a shared contract needs
a decision. That is the whole method in miniature: a bounded question, cited
evidence, an honest gap, and a lead that checks before it builds on the answer.

## 1. Decide whether to delegate

Delegation costs a brief, a context switch and a verification pass. It pays off
when the work is large, independent, or needs a judgment the lead cannot give
competently or impartially. For substantial work it is the normal method:
delegate coherent investigations, implementation packages and independent
reviews, in parallel where the host allows. Typical calls:

- **Stay direct:** a known one-file fix and its check; a lookup, count or filter
  that a deterministic tool answers faster than any agent. Staying direct never
  waives an independent review the work requires.
- **Delegate in parallel:** two capabilities with settled contracts, each with
  its own owner and behavior checks, plus one combined integration check.
- **Delegate, but wait:** two assignments that need the same migration or API
  decision wait for it. Different filenames do not make work independent.
- **Delegate for size:** a large diagnostic or research question goes to a
  read-only analyst so the lead keeps only the conclusions.
- **Delegate for independence:** a reviewer receives requirements and evidence
  without the author's conclusion. An implementer cannot approve its own work as
  independent review; the same model in a separate context can.

If the host has no native agent tool, do the work directly and record any review
that needed independence as open rather than reviewing your own work and calling
it independent.

## 2. Cut at a stable boundary

**For repository work**, cut by a coherent, independently testable outcome — a
user-visible capability or a module behind a settled contract — and let one owner
handle its code and tests. Do not split UI, API and data by layer while the
contract between them is unsettled; each agent would guess the others' half. If
the code boundary itself is unclear, settling it is design work for the lead,
not something to delegate around.

**For research and design**, the boundary can be a concern rather than a folder:
data lifecycle and recovery in one assignment, protection and trust boundaries in
another, both with the same workload and constraints. Several agents may take one
topic when that yields distinct evidence, such as competing analyses. Select only the concerns the change
actually touches. Keep shared assumptions, dependencies and decisions visible to
every affected agent, and bring material decisions back for challenge before
integrating them; the lead resolves the interactions, for example retention
versus deletion. These are example topics, not a required team.

Before parallel work, write a short dependency list and serialize each shared
resource — a migration, contract decision, lockfile, generated output, Git index,
database or port — unless each agent owns an isolated copy. Worktrees separate files, not contradictory semantics. One
writer owns each shared resource.

## 3. Brief each agent

Use the template from the worked example. Each field closes a specific gap:

| Field | Why it is there |
|---|---|
| Task, Outcome | The agent optimizes for what you name; an activity without an outcome never finishes |
| Inputs | Exact paths, the starting revision and relevant uncommitted changes; the agent cannot see your working state |
| Must hold | Requirements and invariants the result has to keep; without them the agent optimizes the task alone |
| Skills | Skills the agent should load for its role, so it applies them itself instead of receiving a paraphrase |
| Boundary | Allowed reads and writes, tools, and "no further agents" |
| Shared | Resources and decisions owned elsewhere, so the agent reports instead of changing them |
| Evidence | What acceptance will check, so the agent collects it on the way |
| Stop if | The conditions where continuing would mean guessing a decision |
| Return | The shape of the answer, including what was not verified; no raw logs or work diary |

An implementer returns a different shape than a scout:

```text
Return:     Changed files, starting revision checked, tests run with results,
            unresolved risks, next action.
```

Include any user restriction that exists only in the main conversation. Give a
fresh context instead of the whole chat: the agent needs the brief, not your
history; use the host's no-history fork option (see the host notes in
[model-routing.md](references/model-routing.md#host-notes)). Enforce read-only
work with native read-only tools or sandboxing; a prompt that says "read-only"
does not make a shell harmless. Without either, keep the work direct or state
the residual risk in the brief.

Child agents do not delegate further. Nested delegation hides who owns a result
and multiplies cost; enforce it natively where the host can, and otherwise state
it in the brief as an instruction rather than claiming a hard limit.

## 4. Choose the model for the phase

Apply this routing by default whenever you assign work; it needs no user switch.
It selects delegate models only: do not change the main model, settings, account
or provider to follow it. Match uncertainty, consequence and modality, not the phase's name:

- **Planning and unresolved design:** a strong main model keeps the work or uses
  similarly capable scouts. A narrow factual lookup still goes to tools or a
  sufficient bounded researcher.
- **Settled nonvisual implementation:** an efficient worker, once requirements,
  contracts and acceptance are actually clear — a plan file alone does not make
  them clear. Escalate unresolved or high-consequence implementation, or a
  demonstrated capability gap, before repeated failed attempts pile up.
- **Independent review:** a strong reviewer suited to the change. Review strength
  does not widen scope: inspect the change and its consumers, recheck what
  corrections affected, and widen only for new evidence.
- **Visual planning, authoring and review:** judge visual ability and access to
  rendered output separately from coding ability. A good refactoring worker may
  need a different author for a diagram, and another reviewer for its quality.

The current per-host preferences, model identifiers and host limitations live in
[references/model-routing.md](references/model-routing.md); read it whenever you
select or reassess a delegate model; it also owns checking the actual spawn
schema and role locks. A requested model is not proof of the model that ran;
verify the effective selection where the host shows it.

For example, a code-focused lead refactors a settings flow and needs a diagram.
It settles the behavior, then hands the verified model, visual direction and
embedding size to a visually capable author. After integration, a separate
reviewer gets the brief, the exact revision and the rendered narrow/wide or
light/dark states, without the author's approval. The author corrects defects,
including composition decisions, and the reviewer checks the changed renders.
Source validity, a model name
or the author's self-critique cannot stand in for visual acceptance; if a capable
author, reviewer or render access is missing, name that gap and continue the
unaffected work.

## 5. Dispatch and steer

Launch independent assignments together so they finish together; queue them in
waves when the host's slots are limited. If a dependency, permission, requirement
or base revision changes, pause the affected assignment and rescope it. Do not
let an agent widen its own task, and do not start an identical replacement while
the first job's state is unknown — two writers on one resource is the failure
this skill exists to prevent.

## 6. Accept and integrate

A returned report is submitted for review, not verified. Open the decisive
evidence and changes without repeating the whole exploration. Resolve
disagreements against the contract and reproducible behavior, not against the
more confident report. A blocked agent should return the exact missing contract,
evidence or access plus its useful partial work; resize or unblock the
assignment rather than restarting it blind. After integration, run the checks
the combined state affects, because each agent only verified its own part.

## When another workflow called this skill

The caller owns its scope, criteria and questioning; this skill owns only the
agent mechanics. Name the active workflows in every brief, return results to
them, and do not load or restart them. A missing caller method does not prevent
a bounded delegation whose ownership and evidence are clear.

The research behind these rules and its limits are in
[references/evidence.md](references/evidence.md); read it only when revising
the rules themselves.
