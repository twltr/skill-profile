---
name: vertical-slices
description: Organize repository code into vertical capabilities with clear public boundaries and Shared Machinery. Use whenever building, extending, changing or assessing a repository, feature or module, including implementation inside existing codebases.
---

# Vertical Slices

Keep the context needed to change a system local and understandable. Apply
vertical structure throughout repository development: creating a repository,
adding a feature or module, extending an existing capability and maintaining
existing code. Start from the affected slice and respect its existing ownership.
A small change uses these boundaries without requiring a whole-system redesign.

## A small ownership example

In an illustrative cancellation feature, `ordering/` owns order state and
cancellation orchestration, `inventory/` owns reservations, and `payments/` owns
payment and refund outcomes. Each capability contains the API, state, logic and
UI it actually needs. Ordering uses the other capabilities' public contracts;
it does not update their storage directly.

A reservation-expiry change belongs in inventory with its invariant and tests.
Ordering changes only if the public outcomes it handles change. Shared transaction
mechanics may be reusable; reservation policy remains with inventory. Derive the
real boundaries from the system, not from this example's nouns or file count.

## Minimum Surface as the design measure

Build the full intended capability with the smallest coherent system that can
honestly own it. **Min-Max Engineering** means maximum useful behavior for the
state, code, modules, dependencies, configuration and operational moving parts
needed to deliver it. Same capability with less system is an architectural gain.
Smallest means least error, state and search surface, not fewest lines: a shared
choke point may add code while giving a wrong behavior one enforceable address.

**Surface is context.** Ask before and after a design or implementation: what can
be reduced, what now has one owner, and what becomes easier to change without
losing capability, robustness or safety? Explicitness comes from honest names,
boundaries, errors and structure, not an ever-growing inventory of special cases.

Before adding machinery, consider deleting obsolete surfaces, consolidating
owners, reusing an existing boundary, table-driving repeated behavior or using
an established pattern. Compatibility layers, broad abstractions, fallback paths
and parallel workflows must justify the states and maintenance they introduce.
A green suite does not excuse unnecessary parallel machinery.

No arbitrary file-count or line-count targets. Useful comments, module briefings
and explanations preserve the model, reasons and invariants; they are not code
volume to shave away. Consolidate repetition without losing those explanations.

## Establish the model before cutting files

Read the affected code, current vocabulary, requirements and architecture.
Trace a representative behavior from its entrypoint through decisions, state
and outputs. Distinguish the actual model from the requested change.

If **Domain Modeling** is available, use it when concepts, lifecycles or names need
clarification; pass the affected scenarios and receive the settled model. If it
called this skill to map an already-settled model, use that model without calling
back. Without it, resolve the relevant meanings through the checks below.

Clarify terms with real counterexamples: can two concepts change independently,
have different lifetimes or mean different things across contexts? Keep the
resolved vocabulary at its existing canonical owner. A substantial system needs
a context map, each context's responsibility and lexicon, and an explanation of
terms whose meaning changes across boundaries. Extend the existing explanation;
do not impose a second glossary or another methodology's folder names.

Give each responsibility and maintained truth one canonical owner. Multiple
inputs are legitimate; independent writers or competing implementations of the
same responsibility create drift. Establish the existing owner before adding
another implementation. Similar code alone does not mean identical responsibility.

Make declarations express the real concepts. **One name, one job:** a cap is not
also a fetch page size; a floor is not also a server default; a timeout is not
also an embedding budget. Separate meanings need honest names even when their
values currently agree. Comments cannot excuse a false declaration.

**Withhold, never fabricate:** represent unavailable or undetermined separately
from absent, empty, false or expired in the contract and its types, then give
consumers an explicit handling decision. A fallback may provide a less useful
answer, but must keep the contract's promises, including timeout nesting, budget
pairing and invariants when a dependency or configuration is missing.

## Vertical co-location and safe localization

Start from the business capability. Technical roles live **inside** the owning
module, rather than forming global controllers/services/repositories layers.

For example, a pricing change should be understandable at its capability owner
rather than requiring reconstruction across five global technical-layer folders.

For each capability, identify its inputs, state, decisions, invariants, outputs
and expected changes. Keep parts that must be understood together together.
Split where responsibility, technology, failure behavior or a genuine contract
creates an independently understandable boundary. A broad product area can be a
namespace; independent capabilities inside it still need their own owners.

Do not create tiny packages or numbered file chunks to hit a size target. A
large coherent file is a signal to examine its responsibilities, not permission
to scatter one state machine. Judge the blast radius and implicit knowledge a
future change needs. Optimize for safe localization and manageable context.

## Public boundaries and dependency direction

Give each module one intentional public surface. Cross-module callers use it,
never deep internals. Describe the inputs, results, error vocabulary, ordering
and state guarantees callers need. Hide useful complexity behind that surface;
an interface that only adds forwarding layers has not earned its place.

Choose the language's native enforcement and a suitable architecture check:
module-private visibility, import constraints or a dependency rule appropriate
to the repository. Keep a machine-readable dependency map derived from actual
imports or declarations. New cross-module edges must be deliberate, reviewable
changes; an existing-edge baseline can support a ratchet during a migration.
Do not maintain a second architectural truth manually.

Keep operational scripts and contract checks with the system they protect.
Temporary authoring aids and convention checks must be removable without breaking
builds, tests or operation. A one-off inspection does not earn a permanent gate;
use existing commands and actual requirements rather than adding administration
to complete an ordinary change.

Each module carries a compact briefing at its package documentation or existing
entrypoint: purpose, what it owns, public API, allowed and forbidden dependencies,
and references to its contracts. Update it with the change it explains. A design
proposal includes the proposed briefing; placing it in implementation is part of
an authorized implementation, not an automatic consequence of a design review.

## Invariants live with their mechanism

Document and enforce a rule at its owner, usually the capability or command
boundary. A state machine that exists only in prose leaves every writer free to
violate it. State what MUST hold, where and how it is enforced, and what breaks
if it is violated. Only genuinely system-wide rules belong at architecture level.

For example: an aggregate holds at most one record per key, and an arriving
record with that key replaces the existing one before and after every supported
manipulation. Or an occupied slot rejects immediately while another slot type
queues at its target inbox. Those rules cannot be understood away from the
component that owns the data or contention behavior.

Keep local invariants in their capability explanation, beside the enforcing
mechanism. Derive any whole-system index from those owners; do not maintain a
central duplicate register. Tests point to the behavior's specification; a
chapter need not maintain a second inventory of the tests.

## Shared Machinery and shared capability components

Evaluate these as different responsibilities:

- **Shared Machinery** executes capability-neutral mechanics, such as a persistence
  skeleton, handler factory or store/hydration mechanism. It contains **zero
  capability-specific logic**. The module declares its concrete queries,
  envelopes, contracts and error vocabulary. The machinery executes that contract;
  it never generates or silently changes it.
- **Shared capability components** own genuinely common behavior. This includes a
  UI interaction used by multiple consumers: the shared component owns the
  interaction, while each consumer supplies its own data and wiring. The same
  behavior in two components is still two places for one truth to diverge.

For each adoption, compare the consumer before and after. Net complexity must go
down per module; otherwise keep the unsuitable mechanism out and record the
reason at the design owner. Rejecting a mechanism never licenses duplication of
the same responsibility. Equally, code resemblance is not a reason to merge
independent business policies. This is a semantic ownership decision, not an
automatic extraction rule at the second similar snippet.

Keep interfaces intention-revealing. If the capability honestly is plain CRUD,
binding an appropriate generic mechanism directly is clearer than wrappers with
no responsibility. Moving onto Shared Machinery preserves the concrete contracts
and observable behavior, reviewable as near-verbatim moves. A behavior change
must be identified as its own decision.

## Patterns serve the architecture

Use established patterns when they reduce places to look, centralize enforcement
or make evolution safer: a state machine, registry, factory, adapter, repository,
event log, outbox or process manager can each earn a place. A pattern that adds a
layer without reducing the search or error surface is decoration.

If **Engineering Practices** is available, use it for consequential language,
architecture, framework, provider, security, persistence, protocol or runtime
choices. If **State of the Art** is available and current evidence is needed,
use its research method through that decision owner. Without those methods,
consult current primary sources and established literature directly. Keep the
accepted choice and rationale at the repository's canonical design owner.
Do not invent citations or rename a system after a methodology. Bounded contexts,
ports, events and invariants matter through the boundaries they express.

If **Puppeteer** is available, use it for substantial exploration of independent
capabilities or competing boundaries before loading the whole system into the
main context. Scouts return current owners, contracts, evidence and disagreements;
the main agent reconciles the architecture. If **Grilling with Agents** is already
the caller, answer its scoped structural questions instead of starting another
council. A known local change needs no parallel architecture study.

## Check and deliver the design

Walk a normal domain change, a boundary failure and a likely extension through
the design. Show where code, tests, invariants and explanation live, how callers
reach the public surface and what new dependency edges appear. Compare actual
state, error surface and context needed against useful alternatives.

If a change still scatters across unrelated files, duplicates policy or requires
knowledge hidden in another module, revise the ownership. Deliver the vocabulary,
capability and dependency map, interface decisions, proposed briefings, reasons
and remaining questions at the existing design owner. Do not launch a refactoring
from a design-only request. If implementation is separately authorized, use
mechanical, compiler/test-checked moves where structure changes across the tree.

Supplementary upstream methods are credited in [NOTICE.md](NOTICE.md).
