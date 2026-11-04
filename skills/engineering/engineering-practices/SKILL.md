---
name: engineering-practices
description: Choose and review software languages, architectures, protocols, frameworks and dependencies using current primary sources, established engineering knowledge and the needs of maintainers. Apply during development at the scale of the actual decision, from a small feature to a new system.
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

## Scale the investigation

Start with the requested outcome, actual repository, current stack and existing
decisions. For a known local fix, inspect the affected contract and use established
practice. For a new service or a material technology decision, compare a small set
of credible alternatives. For an architecture review, begin with the large choices
and deepen only where evidence shows a meaningful problem.

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
