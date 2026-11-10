---
name: vertical-slices
description: Use whenever adding, changing, debugging, refactoring or reviewing behavior in a repository, feature or module. Locate capability and coordination owners, expose the chosen patterns' participants and relationships, and keep coherent code and its explanation together. Apply within ordinary implementation, not only architecture tasks.
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# Vertical Slices

**Leaf skill** in Software Engineering; reached through its domain or by name.

Keep the context needed to change a system local and understandable. Apply
vertical structure throughout repository development: creating a repository,
adding a feature or module, extending an existing capability and maintaining
existing code. Start from the affected slice and respect its existing ownership.
A small change uses these boundaries without requiring a whole-system redesign.

The structure and its named roles leave a durable route for the next change.
Future maintainers should discover where to extend a pattern and which other
mechanisms constrain it without reconstructing the original conversation. Identify
the affected capability, coordinating owner and participants before editing; keep
their local explanations current while changing them. A tidy tree alone does not
preserve the intent behind its boundaries.

## Example: make composition and its participants visible

Fictional brief: a monitoring capability runs website and provider checks. Each
provider has its own request mapping, evidence rules and fixtures. A flat list of
`firebase.py`, `vercel.py` and `search_console.py` does not explain how a run works.
Make the coordinating responsibility and cohesive participants discoverable:

```text
monitoring/
  __init__.py                 # public entry and capability briefing
  pipeline/
    run.py                    # stage order, admission and failure propagation
    contracts.py              # Stage input/result, including unavailable evidence
  stages/
    website/                  # website probe and its evidence interpretation
    firebase/                 # provider mapping and local check policy
    vercel/
    search_console/
```

Here `run.py` composes the stages through the Stage contract; stage implementations
do not import or start each other. Its declaration makes ordering and permitted
parallel work visible. Each provider folder owns the meaningful parts it needs,
with tests beside it or under the matching test convention. `pipeline/` is the
shared coordination owner, not a dumping ground for provider-specific rules.

These names are illustrative. An existing `base/`, `core/` or composition module
can serve the same job if its responsibility is explicit. A single small probe
may remain one file; do not pre-create empty providers or one-file wrappers for
symmetry. The improvement is a readable architectural relationship, not depth.

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

When a settled model is supplied, map it as given. Otherwise resolve the relevant
meanings through the checks below. When concepts, lifecycles or names stay
ambiguous, report that to the lead with the affected scenarios instead of settling
them here.

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

Make the architecture visible at each useful scale. Repository boundaries expose
independent systems and their contracts; capability folders group cohesive behavior;
submodules and files expose the roles of the chosen construction. A collection of
well-named leaf files is incomplete if the reader cannot find what connects them.
Show the composition owner and how control/data passes between participants in
code, using the relevant native mechanism: a pipeline declaration, handler registry,
transition table, subscription wiring or explicit constructor composition.

Use folders when a responsibility has several parts that belong together. A state
machine might own `states/` plus a transition policy and coordinator; an extensible
integration may own adapter packages plus a factory or registry. Keep the policy
and its assembly discoverable instead of scattering state transitions or hiding
ordering in import side effects. A small machine can keep its states in one table.
Folders express the model; they do not substitute for it or mandate a class per state.

Separate the owner of runtime sequencing from application composition when those
are different responsibilities. Creating dependencies at startup does not by itself
explain which stage runs next or how a failed stage affects the remaining run.
Do not call every coordinator a Composition Root, or every status enum a State
pattern. Name a mechanism only after checking its defining roles in the code.

Give each module one intentional public surface. Cross-module callers use it,
never deep internals. Describe the inputs, results, error vocabulary, ordering
and state guarantees callers need. Hide useful complexity behind that surface;
an interface that only adds forwarding layers has not earned its place.

Respect existing public boundaries even on a small change. When module boundaries
and dependency drift are consequential, use suitable enforcement such as native
module-private visibility, import constraints or dependency checks. Reuse existing
mechanisms before adding another. Derive a needed machine-readable dependency map from
actual imports or declarations; do not maintain a second architectural truth
manually. New cross-module edges must be deliberate, reviewable changes; an
existing-edge baseline can support a ratchet during a migration. A single-script
tool with no such boundaries does not need a map or new gate merely to follow
this method.

Keep operational scripts and contract checks with the system they protect.
Temporary authoring aids and convention checks must be removable without breaking
builds, tests or operation. A one-off inspection does not earn a permanent gate;
use existing commands and actual requirements rather than adding administration
to complete an ordinary change.

During implementation, give each affected important module a local briefing and
its decision reasons, written from the actual model, accepted decisions and code.
Preserve purpose, system context, construction, reasons, public boundary and change
constraints at their source owners. Keep the briefing at the existing package
documentation or entrypoint and link wider architecture instead of duplicating
it. A self-explanatory leaf needs no separate briefing. A design proposal identifies the explanation's
owner; placing it in source requires authorized implementation.

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

Consequential language, architecture, framework, provider, security, persistence,
protocol or runtime choices are decisions of their own, not a by-product of the
layout. Consult current primary sources and established literature for them;
when such a choice needs dedicated current-practice research, report it to the
lead. Keep the accepted choice and rationale at the repository's canonical
design owner.
Do not invent citations or rename a system after a methodology. Bounded contexts,
ports, events and invariants matter through the boundaries they express.

If **Puppeteer** is available, use it for substantial exploration of independent
capabilities or competing boundaries before loading the whole system into the
main context. Scouts return current owners, contracts, evidence and disagreements;
the main agent reconciles the architecture. When this method answers scoped
structural questions, return the answers to whoever loaded it; do not start a
council of its own. A known local change needs no parallel architecture study.

## Check and deliver the design

Walk a normal domain change, a boundary failure and a likely extension through
the design. Show where code, tests, invariants and explanation live, how callers
reach the public surface and what new dependency edges appear. Compare actual
state, error surface and context needed against useful alternatives.

Try the extension without chat history: can a maintainer find the coordinator,
participant contract and the correct folder for a new stage, state or adapter?
Can they see which ordering, failure and ownership rules the extension must retain?
Verify these against executable wiring, not a tree diagram alone. A flat module
or a nested layout may pass; neither a file-count limit nor a required depth does.

If a change still scatters across unrelated files, duplicates policy or requires
knowledge hidden in another module, revise the ownership. Deliver the vocabulary,
capability and dependency relationships, interface decisions, any needed briefings,
reasons and remaining questions at the existing design owner, scaled to the change.
Do not launch a refactoring
from a design-only request. If implementation is separately authorized, use
mechanical, compiler/test-checked moves where structure changes across the tree.

Supplementary upstream methods are credited in [NOTICE.md](NOTICE.md).
