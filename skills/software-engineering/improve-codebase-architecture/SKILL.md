---
name: improve-codebase-architecture
description: Assess an existing system from language and architecture choices down to interfaces, domain names, modules and files. Research alternatives, prioritize evidence-backed improvements and turn accepted recommendations into a coordinated plan.
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# Improve Codebase Architecture

**Leaf skill** in Software Engineering; reached through its domain or by name.

Reassess an existing system deliberately, from broad choices to local structure.
Produce a grounded recommendation and executable planning handoff. An assessment
does not by itself authorize a rewrite, language migration or product implementation.

## A worked assessment

Fictional request: reassess a growing operations backend made from several scripts.

```text
Broad question: Does the current language/runtime fit its lifespan, workload,
maintenance team and operating environment?
Evidence: actual deployment constraints, recurring defects, ownership, supported
SDKs and the costs of both staying and migrating.

Next: compare system shape and communication; then domain meanings and lifecycle
owners; then public interfaces; finally module names and file organization.

Recommendation: first consolidate the duplicated scheduling policy at one owner.
Do not propose a language rewrite just because the scripts are untidy. A rewrite
needs evidence that the target improves the problem enough to pay its migration cost.

Handoff: one verifiable roadmap outcome, its accepted decisions, actual blockers,
checks and cleanup. Add an issue only when a remote tracker is part of the workflow.
```

The conclusion can be a full language change when the evidence supports it. It
can equally be a smaller correction or retaining the current system. Do not
predetermine the answer from the review's name.

## 1. Establish the assessment boundary

Read the user's concerns, intended capabilities, relevant history, existing decisions
and actual operating constraints. Inspect the dirty working tree and preserve
unrelated work. Identify whether the scope is a whole system, one repository or
a bounded capability. Include maintenance by people and agents, not just runtime
performance. Start with observed friction and the parts that are changing.

## 2. Investigate from broad to fine

Three lenses recur: current research with language, framework, dependency,
architecture and protocol comparisons; names, relationships and lifecycle
distinctions; and ownership, boundaries, interfaces, file/module placement and
Shared Machinery. Apply only the lens needed at each level; the three are not
three competing owners of the same decision.

Examine in this order, adjusting to the task:

1. Purpose, constraints, language/runtime and long-term human maintenance.
2. System shape, deployment, data ownership, consistency and communication.
3. Domain meanings, identities, lifecycles and names.
4. Capability/public-interface boundaries, error contracts and dependencies.
5. Shared mechanisms, module construction, files and local explanation.

If **Puppeteer** is available, delegate independent investigations before loading
all source into the main context. Give each scout an evidence question and return
shape, not a license to refactor. Settle shared assumptions before detailed designs.
When competing consequential options need challenge, ask the lead for a
challenge between agents. Its questions stay between agents; return decisions,
reasons and unresolved prerequisites without asking the user or relaying council
questions. A human interview is a separate step the user chooses, not a mode of
this council. Preserve unresolved prerequisites instead of guessing or
letting discussion loop indefinitely.

When a consequential interface admits genuinely different designs, compare a few
under the same requirements: caller knowledge, ownership, failure behavior, change
locality and testability. Scale the agents and variants to the available runtime.
Do not force a fixed number of providers or rename the project to an imported vocabulary.

Without a supporting skill, perform the necessary bounded analysis directly and
identify material limitations. Do not claim absent tools or independent agents.

## 3. Turn evidence into prioritized recommendations

For each material candidate, show:

- Observed behavior or friction, with exact source/operating evidence.
- The proposed change and the improvement it would make possible.
- A credible alternative, including keeping the current construction.
- Costs: migration, compatibility, dependencies, operations and learning.
- Behavior and evidence that must survive; remaining uncertainty.
- Priority and dependency on other decisions or work.

Use diagrams when they clarify ownership or behavior; a report does not require
HTML, a CDN or opening a foreground browser. Temporary research belongs in `.tmp/`.
Compare the whole system's complexity: the state, error surface, duplication,
search and operational machinery its capability needs. Preserve the behavioral
oracle; this does not start a refactoring. Evaluate whether the important
models, reasons and invariants are understandable beside their mechanisms.

## 4. Hand off accepted work

Recommend a course with reasons. The user's request and existing authority decide
whether it is accepted for implementation; a council score does not. Pass agreed
outcomes, decisions, reasons, rejected alternatives, sources, dependencies and
verification to the planning owner. If a plan is already active, update it
instead of restarting the workflow. Keep later work coarse until its
prerequisites settle. Local work uses roadmap and plans; remote work adds
meaningful issues, PRs and traceable review. Do not create one ticket per
opinion or file.

If implementation was authorized, continue in the active plan. Carry an agreed
replacement through all its affected consumers. Preserve needed tests and
temporary migration evidence until the replacement proves the same intended
capability; retire old owners in the authorized lifecycle. Do not introduce permanent coexistence merely to avoid
finishing the migration.

Return the assessment, recommendation, actual planning artifacts and open gates.
This skill does not apply itself during ordinary development; its native metadata
keeps direct selection explicit. A targeted request for architecture reassessment
is the intentional entry, not a consequence of encountering an unfamiliar codebase.

Source influences are recorded in [NOTICE.md](NOTICE.md).
