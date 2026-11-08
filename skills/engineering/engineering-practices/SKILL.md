---
name: engineering-practices
description: Use whenever implementing, debugging, refactoring or reviewing software behavior, and for architecture or design decisions. Choose mechanisms from requirements and evidence, name applied patterns and their relationships, verify relevant sources, and preserve accepted reasons in code and docs.
---

# Engineering Practices

Make engineering choices from the problem, evidence and human maintenance needs.
Apply these criteria throughout development; a small change usually reuses the
system's sound choices and needs no new research exercise. A new repository,
capability or consequential replacement needs an explicit comparison.

Carry accepted decisions into the repository before the work ends. A sound choice
left only in chat, a design council or a closing report cannot guide the next
maintainer. Keep detailed local reasons beside code and cross-system architecture,
applied-pattern references and operating guidance with their documentation owner.
Use precise links so those explanations complement each other.

The purpose is to guide future implementation after its original conversation is
lost. A named pattern connects local code to a recognizable model; its participants,
relationships and rationale tell the next maintainer how to extend that model and
when its assumptions warrant reconsideration. A working implementation alone does
not retain that decision. Do not leave the reader to infer the intended architecture
from syntax or remember an old design discussion.

For source work, apply Golden Comments at the affected code owner when available;
for structure, use Vertical Slices at the affected boundary. Do this during the
implementation, including a routine feature or bug fix, rather than waiting for
the user to request comments or architecture. When a decision affects system
understanding, patterns, contracts or operation, update its existing documentation
through Engineering Documentation. Reuse existing evidence and active methods;
a local fix needs the relevant explanation, not a new research programme.

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

## Example: leave a verifiable pattern decision

Fictional brief: provider request and response details are leaking into a report's
business logic. An accepted decision might leave this small architecture entry:

| Applied mechanism and primary source | Implementation owner | Reason and boundary |
|---|---|---|
| Gateway — [Martin Fowler](https://martinfowler.com/eaaCatalog/gateway.html) | `reporting/providers/catalog.py:CatalogGateway` | Translate the external catalog API into the report's own contract. Provider fields stay at this boundary; detailed mapping and error reasons live in its source commentary. |
| Composition Root — [Mark Seemann](https://blog.ploeh.dk/2011/07/28/CompositionRoot/) | `app.py:create_app` | Assemble the application dependencies at its entrypoint. The report receives a gateway; it does not discover a global container. |

These links support the pattern meanings, not proof that the fictional files
implement them. The gateway's local briefing explains the actual dependency,
mapping decision and rejected option of spreading SDK calls through consumers.
A tiny direct integration may not need a separate object; show what responsibility
the boundary earns. A concise entry can live in the README for a small repository.

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
| Configuration and value ownership | Which values define the program, vary with its operating context, or belong to a business operation? Who may change each value, when should changes take effect, and which validation, precedence and protection rules apply? |
| Repository and toolchain | What owns source, configuration contracts, templates, schemas, migrations and generated artifacts? Which inputs and conventions make work reproducible and discoverable for this language, project size and deployment model? |
| Delivery and operation | What is built, verified, promoted and actually running? Which configuration, state, credentials and compatibility conditions must accompany a release or recovery, and what evidence establishes the intended result? |
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

## Give values and operating changes explicit owners

Apply these questions when the task changes configuration, retained state,
execution environments or release automation. Reuse sound existing conventions
for unrelated work. A disposable tool does not need a service's operating machinery.

**Classify by meaning and lifecycle before choosing an encoding or location.**

| Kind of value | Ownership decision |
|---|---|
| A stable part of the program's meaning | Keep a genuine constant with its code, type or domain-contract owner. Do not make an invariant configurable merely because it is a literal. |
| A deployment or operating choice | Give it a cohesive configuration contract and an explicit source, independent of implementation changes when it needs to vary independently. |
| A credential or other protected value | Establish its authorized consumer, protected source and lifecycle. Configuration may reference it; ordinary tracked examples must not contain the real value. |
| Business identity, operation input, migration selection or test data | Keep it with the corresponding data, invocation, migration or fixture owner. A settings file must not become an accidental second database. |

For example, “move these orders” does not establish where their IDs belong. A
per-run order selection is an explicit input; imported identities belong to the
data record, while a migration's selection belongs to its input; a test's fixed
IDs are fixture data. A per-environment routing identifier may instead be
configuration. Decide from the actual owner
and change contract. Moving every literal into YAML would preserve the ambiguity.

**Define how configuration becomes effective.** Choose the source and placement
from the ecosystem, capability owner, project scale and operating model: a dedicated
file, environment injection, command input or managed provider can each be appropriate.
Reuse the language/framework's supported mechanism when it fits. Define the
applicable semantics: required values, defaults and constraints; precedence when
multiple sources exist; invalid-input behavior; and when changes take effect.
Validate before dependent work; expose resolved values at a clear boundary rather than scattering literals or environment lookups
through consumers. A change may require a release or restart; hot reload is not
an automatic requirement.

Keep cohesive settings and their applicable schema discoverable at their owner.
Reusable templates should expose declared inputs for project-specific assignments.
Version the non-sensitive contract, suitable defaults and placeholder examples,
and actual non-sensitive configuration where appropriate for reproducibility.
Keep real secrets and private local overrides with their approved owner.
Follow actual language/project conventions for paths and formats instead of
mandating one global config directory. Configuration provenance should be
diagnosable without printing protected values.

**Protect the whole secret lifecycle.** Distinguish a workload's identity or a
resource identifier from credential material. Use the runtime's supported identity
mechanism when it fits; an identifier alone does not establish authentication or
secrecy. Determine provisioning, access, rotation, revocation and recovery for the
actual consumer and trust boundary. Environment variables are an injection mechanism, not a confidentiality guarantee. Distinguish
build-time from runtime access and prevent unintended inclusion in source,
generated files, images, caches, logs, dumps or published artifacts. Choose controls
proportionate to exposure; a new secret-management service must earn its cost.

**Separate build inputs, release artifacts and live state.** Decide which manifests,
dependency locks, schemas, templates and generation steps must be maintained to
reproduce the intended artifact. Distinguish authored from generated content and
record its owner. A container, when used, is an execution/package boundary: identify
what is baked into it, supplied at runtime, retained elsewhere or reconstructible.
Neither the presence of a persistent volume nor an image rebuild by itself
establishes a backup. These questions also apply without containers; they do not prescribe Docker or a CI vendor.

**Design recovery around the required outcome.** Establish acceptable loss and
downtime, the actual recovery set, consistency, retention, protection and compatible
application/data versions. Select a supported backup or reconstruction mechanism
for those needs; a logical dump is one candidate, not a universal recovery plan.
Include dependent stores, configuration and access to keys only where required;
keep their distinct owners and restore order explicit. Producing backup bytes,
checking integrity, restoring data and recovering the application are different
claims. Before claiming operational recoverability, demonstrate a representative
isolated restore and the relevant application invariants against the stated target.
Repeat checks when material recovery assumptions change, not for every unrelated edit.

**Make delivery verifiable at its trust boundaries.** When releases or CI/CD are
relevant, establish artifact identity and origin, the checks it passed, environment
configuration and permission scope. Keep untrusted changes away from privileged
credentials. Promote the verified artifact when that guarantee matters; if a rebuild
is necessary, establish its traceability and verify the resulting artifact. Address
schema/data compatibility, deployment ordering and an appropriate recovery path
where the change requires them; rollback may be unsafe for irreversible state changes.
Verify the running result at its owner: a green pipeline alone does not establish
the active revision, service health or intended business effect.

Choose the smallest sufficient arrangement. A single local script may need only
explicit inputs and a documented rebuild path; an operated service with valuable
state needs stronger controls and evidence. Use State of the Art for unresolved
current capabilities, Domain Modeling for ambiguous meanings and Vertical Slices
for owner placement when available. Engineering Documentation, if available,
owns the maintained configuration/use/recovery explanation; retain actual values
and contracts at their proper sources instead of copying them into prose.

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

## Name the implemented construction and keep its evidence

Make the result answer the next implementer's practical questions: which pattern
is this, which code owns each role, why does it fit these constraints, how does it
cooperate with the surrounding patterns, and what must change if those constraints
stop holding? Put detailed local reasons in source and shared relationships in the
architecture explanation. These are coverage questions, not mandatory headings.

During ordinary implementation, identify the established patterns already present
or introduced by the change; the user need not ask for a pattern-selection exercise.
For example, provider-shape translation behind a domain-facing interface deserves
comparison with Adapter/Gateway; registering listeners with a publisher deserves
comparison with Observer or Publish–Subscribe according to the actual coupling.
Choose the term whose defining relationships fit and show those relationships.
Do not call a recognizable pattern merely a "local mechanism" to avoid naming it
or retaining its primary reference. Project-specific participants do not make the
underlying pattern a new invention. When a defining relationship cannot be checked,
mark the candidate mapping unverified instead of asserting or silently omitting it.

For an architectural or software-pattern decision, explicitly name the adopted
pattern, show its participants at real file/symbol locations and explain the
forces that make it fit. Use the recognized term when the mechanism satisfies it;
a generic claim such as "clean architecture" or "best practice" is insufficient.
If the construction is project-local, give it an honest descriptive name and mark
any resemblance as an analogy. Do not retrofit prestigious labels onto ordinary code.

This applies from repository integration to module and file design: a process
manager, pipeline, state machine, observer subscription, factory or adapter each
has concrete roles and constraints. A WebSocket is a communication mechanism, not
itself a design pattern. An enum declares states; transition policy establishes a
state machine. Event delivery does not alone establish Event Sourcing. Describe
what the actual code does, including limits and deliberate departures from a source.

Keep a compact applied-pattern map at the existing architecture owner when several
patterns need navigation. Each entry names the pattern, primary reference, actual
implementation and brief reason. Link to the owning chapter or source for detail;
do not create a second decision register. Add or revise the relevant entry with
the implementation, even when the user did not separately request documentation.
For one local decision, a short source explanation and existing docs anchor suffice.

Persist the sources that informed accepted choices in the maintained Markdown,
adjacent to the claim or in a precisely referenced source entry. Name the author
or specification, link the actual section, and state what was adopted and any
version or assumption that limits applicability. A list of prestigious homepages
or citations confined to the final chat answer does not preserve the reasoning.
Use stable references for established patterns and recheck version-sensitive claims
at the actual owner. Reuse a verified source when it still answers the question.

Distinguish a source supporting the pattern's meaning from evidence of historical
influence. A reference located during this change may explain an existing design;
it does not prove that the original author consulted it. Record actual provenance
only when supported. Keep references at the owning explanation rather than adding
the same citation to every implementation file.

For example, a protocol chapter can link the versioned
[MCP architecture specification](https://modelcontextprotocol.io/specification/2025-11-25/architecture)
for host/client/server responsibilities and identify the local client/session owner.
That is a pinned teaching reference, not a recommendation of the current version.
Record the version actually implemented and inspected in the real task. Keep local
timeout policy distinct from a protocol requirement; a specification link cannot
prove local conformance. If a source cannot be checked, record the exact gap and
avoid claiming it was researched or that its guarantee is implemented.

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
- If **Golden Comments** is available, use it while implementing each affected
  important source unit. Pass the chosen mechanism, accepted reasons and constraints;
  receive a local explanation checked against the code, not only a chat summary.
- If **Engineering Documentation** is available and the change affects system
  understanding, patterns, contracts or operation, load it directly for the affected
  explanation. Pass the existing evidence and source anchors; do not wait for an
  independent writing request or restart Good Writing. Good Writing remains the
  general writing router. Without either specialist, preserve these explanations
  at the same owners and state any material verification limit.
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

Before delivery, follow a consequential changed decision from its named pattern
and source to the implementing participants. Can a maintainer locate the local
reason, understand its relationship to surrounding mechanisms and see which
assumptions a future change must preserve or reconsider? Repair missing explanations
at their owners before handoff. A loaded skill or a pattern name in the final reply
does not establish that the repository carries this understanding.

Source influences and limits are recorded in [NOTICE.md](NOTICE.md).
