---
name: engineering-practices
description: Make and review engineering decisions about architecture, data, reliability, security and technology choices from requirements, current evidence and maintenance needs. Apply during development at the scale of the actual decision, from a small feature to a new system.
---

# Engineering Practices

Make engineering choices from the problem, evidence and human maintenance needs.
Apply these criteria throughout development; a small change usually reuses the
system's sound choices and needs no new research exercise. A new repository,
capability or consequential replacement needs an explicit comparison.

## A worked choice

Fictional brief: a long-lived operations service has transactional workflows,
several maintainers and an existing supported JVM build/deployment environment.
It needs a browser UI later, but its current scope is a backend service.

```text
Decision: use the team's supported Java stack for the service and begin with
a modular monolith. Keep an explicit public HTTP contract for its consumers.

Why: existing operational knowledge and tooling reduce maintenance cost;
the current workload does not justify independently deployed services.
A future browser UI does not determine the backend language.

Alternatives: a small standalone service in another language could be justified
by deployment constraints; a JavaScript backend needs a positive reason beyond
generator convenience. Neither alternative currently beats the stated fit.

Before pinning versions: verify the language/runtime support line, framework
compatibility and required SDK support in their current official documentation.
```

This is a conditional example, not a default recommendation of Java. Change the
workload, team or operating constraints and the conclusion may change. State the
actual choice, rejected alternative, evidence and what would justify revisiting it.

## A compact set of practices

1. **Choose for the whole lifetime.** Compare workload fit, correctness needs,
   deployment, debugging, readability, team familiarity, handover and support cost.
   A language that is easy for an agent to generate is not thereby the best owner
   of a long-lived system.
2. **Use supported, compatible foundations.** Verify current standards, SDK guidance,
   release/support policy and ecosystem compatibility when making or revisiting a
   consequential choice. Latest, stable, supported and compatible are different claims.
3. **Make quality trade-offs explicit.** Identify the few requirements that actually
   constrain the design: consistency, availability, latency, scale, portability,
   operability or cost. Compare plausible options against those requirements rather
   than adopting a familiar architecture label.
4. **Make every dependency earn its place.** Compare the capability gained with
   transitive/runtime/build weight, maintenance, licensing, security exposure and
   replacement cost. Reuse the standard library or a small local mechanism when it
   honestly suffices; do not hand-roll complex security, protocol or format logic
   merely to reduce package count.
5. **Choose communication for its semantics.** Decide what needs a synchronous
   answer, durable asynchronous processing, ordering, delivery guarantees or streaming.
   Select REST/HTTP, RPC, events or an in-process call for those needs and consumers.
   A network boundary and a new broker both introduce work that must be justified.
6. **Put guarantees in enforceable contracts.** Use the language's types and native
   mechanisms to make invalid inputs and states explicit. Define error, cancellation,
   time, ownership and resource-lifetime behavior at the relevant boundary; follow
   the actual ecosystem's idioms instead of translating another language's style.
7. **Design for failure and operation.** Work out partial failure, timeouts, retries,
   idempotency, contention and recovery where they apply. Make failures diagnosable
   through suitable logs, metrics or traces, without collecting data for its own sake.
8. **Measure performance claims.** Establish the workload and bottleneck before
   optimizing. Benchmark representative behavior, include relevant resource costs
   and keep a before/after comparison; a microbenchmark is not proof of user benefit.
9. **Validate risky assumptions cheaply.** Use a bounded experiment, compatibility
   check or small prototype when reading alone cannot distinguish options. State
   what it establishes and discard temporary scaffolding when its job is complete.
10. **Revisit choices with evidence.** At a relevant refactor or changing constraint,
    check whether an old dependency, pattern or language choice still earns its cost.
    Include migration and operating costs; dissatisfaction alone is not a rewrite case.

These ten are a starting set, not a permanent limit or universal ranking. Add or
revise a practice only when it supplies useful decision guidance. Structure, domain naming,
source explanations and test design retain their specialist owners below.

## Find the relevant decision dimensions

Start with required behavior and guarantees, not a technology or pattern catalogue.
For a new application, consider the full spectrum below before narrowing the work.
For an existing feature, investigate the dimensions it changes or depends on;
reuse sound established decisions elsewhere. These are lenses for discovering
questions, not a checklist that every task must complete. A dimension can require
no new mechanism or investigation; explain that briefly when the scope is substantial.

| Dimension | Questions that can change the design |
|---|---|
| State and data lifecycle | What concepts and objects exist? What does each consequential field mean, why is it needed, and which invariants govern identity, validity, ownership and change? Which information is authoritative, derived or disposable? |
| Persistence and consistency | What must be retained, for how long, and with what acceptable loss or staleness? What do concurrent changes require? Which atomicity, durability, access and evolution guarantees follow from the workload? |
| Failure modes and recovery | Which failures can occur, where can outcomes become partial or unknown, and what must remain true? What must be recovered, reconstructed or reconciled, within which tolerances, and how will that be demonstrated? |
| Communication and contracts | What must participants agree on before acting? What does acceptance or completion mean, who owns the result, and what happens with delay, cancellation, repetition, ordering or lost contact? |
| Security and trust | Which data and actions need protection, from whom, and across which trust boundaries? What confidentiality, integrity, authorization and lifecycle requirements follow? Which exposure or current security finding could change the choice? |
| Mechanisms and language fit | Which concrete responsibility or invariant needs a mechanism? Can the existing design or language-native facility express it clearly? What would an additional pattern improve, and what cost or failure behavior would it introduce? |

The same reasoning applies to deployment, performance, operability and human
maintenance in the practices above. Follow interactions between dimensions:
a recovery design may change access control, retention, consistency or cost.
Do not optimize each topic independently and assume the results compose.

Domain Modeling, when available, owns unsettled meanings, identities and lifecycle
rules. Use those results to choose representations, storage and enforceable
contracts; do not produce a full schema for a task that does not need one.
Likewise, select synchronous or asynchronous communication, a storage technology
or a language-idiomatic pattern only after its requirements are clear. A state
machine, observer or factory is an example of a candidate, not a recommended
default. Keep direct implementation and reuse among the alternatives.

Use theoretical results only within their assumptions. For example, a partition
question needs the required consistency model and acceptable service behavior;
a CAP label alone does not decide a database or the design of an entire system.

### Same failure, different requirements

Illustrative contrast: a temporary report can be regenerated from retained source
data, so restarting its calculation may meet the requirement. A valuable external
operation whose acknowledgment was lost needs its outcome established before a
repeat is considered safe. Both may follow a process crash; their preservation
and recovery needs differ. Ask what must remain true, inspect the actual contract,
then choose and verify the smallest sufficient mechanism. Neither example mandates
a database, a status enum, a retry scheme or a particular architecture.

## Scale the investigation

Start with the requested outcome, actual repository, current stack and existing
decisions. For a known local fix, inspect the affected contract and use established
practice. For a new service or a material technology decision, compare a small set
of credible alternatives. For an architecture review, begin with the large choices
and deepen only where evidence shows a meaningful problem.

For substantial work, turn the relevant dimensions into bounded decision questions
with shared requirements and explicit dependencies. If **Puppeteer** is available,
use it to assign coherent topics or independent subquestions to agents, including
multiple investigations of a difficult topic when useful. Keep cross-topic choices
with the lead; do not commission a separate full-system design from every scout.
Pass this same scope to State of the Art and any council instead of restarting
topic discovery in each method. A small settled question stays direct.

Do not default a substantial new non-browser system to JavaScript, TypeScript or
an accumulation of MJS scripts because they are convenient to generate. Establish
a positive technical and organizational case and compare suitable alternatives.
This is not a blanket ban on those languages, nor permission to rewrite an existing
system. A browser application, small tool or justified established stack may make
them appropriate. Avoid gratuitous language and module-format diversity as well.

Use a compact decision comparison when it helps:

| Criterion | Current/simple option | Credible alternative | Decision evidence |
|---|---|---|---|
| Workload and failure behavior | What it actually supports | What improves or worsens | Requirement, experiment or verified contract |
| Human maintenance | Familiarity, readability, debugging | Training and handover costs | Actual team/owner context |
| Operations and ecosystem | Deployment, compatibility, support | New moving parts | Current provider documentation |
| Total cost | Dependencies and runtime/build burden | Migration and future change | Measured or clearly qualified estimate |

Do not fill a matrix with invented numbers. Choose and explain the strongest option
when the brief and evidence suffice; do not return routine engineering decisions
to the user as a menu. A missing fact stays unverified, and a genuine authority or
preference boundary remains visible.

## Research at the actual source

For substantive or version-sensitive choices, use **State of the Art** when
available. Supply the problem, constraints, candidates and evidence needed to
choose; receive supported findings, alternatives, uncertainty and a recommendation.
It owns search strategy, source assessment and delegated research. Without it,
consult current primary specifications, SDK/release documentation and relevant
established literature directly. A forum claim about an "MCP council decision"
is not proof that a transport, SDK or version was retired.

For a security assessment or a choice that changes the attack surface, protected
data or security-relevant components, include current advisory and support information.
Assess applicability to actual versions, configuration and exposure before choosing
a mitigation or replacement. Reuse established controls for unaffected areas;
neither a familiar architecture nor a clean search establishes security.

Keep temporary research under `.tmp/research/<topic>/` or the repository's established
temporary equivalent. Keep accepted, durable decisions and their supporting
references with the existing plan/design owner, not a competing research book.

For example, a one-use formatting transformation may fit a small script and the
standard library. Full localization, complex document parsing or cryptography may
justify a maintained library despite a larger tree. Count the capability and
maintenance burden, not just files. Recheck that trade-off when requirements expand.

## Compose only the needed methods

- If **Domain Modeling** is available and meanings or names need work, use it with
  the relevant scenarios; receive settled terms, relationships and remaining ambiguity.
- If **Vertical Slices** is available, use it for repository/module/file ownership,
  public boundaries and Shared Machinery. Do not maintain a second structural ruleset.
- If **Puppeteer** is available, use it to split substantial independent research or
  compare competing designs before filling the main context with raw sources.
- If **Grilling with Agents** is available and a consequential decision benefits from
  challenge, supply the constraints and evidence; receive challenged decisions,
  reasons, rejected alternatives and explicit unresolved prerequisites. Its council
  questions stay between agents for every invocation; do not relay them to the user.
  It returns here without starting a second planning or implementation workflow.
- If **Road to Glory** is available, preserve the planning handoff: an existing plan
  receives the decisions, reasons, evidence, alternatives and unresolved prerequisites,
  including council results. If implementation needs new coordinated packages, hand
  off accepted work for planning at the authorized scope. Return to an active caller
  or ancestor instead of starting it again. Without a plan or substantial planning
  need, return the decision report; a small choice does not create a roadmap item.
- If **MinMax Codebase** or **All or Nothing** is available for an authorized structural
  correction, use the appropriate method for simplification or complete replacement.
  A design assessment itself does not authorize that correction.

Use an available skill's actual catalog/path and read it once for the relevant
subtask. Without it, perform the bounded necessary reasoning directly and identify
any material gap; never claim an unavailable method was applied. Return to the
caller with decisions, sources, reasons and verification needs. Pass active workflow
names into a handoff. Do not create a mandatory tour or re-enter a method already
active anywhere in the call chain; return its needed result to that owner.

Source influences and limits are recorded in [NOTICE.md](NOTICE.md).
