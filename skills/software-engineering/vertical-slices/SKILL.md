---
name: vertical-slices
description: Use whenever adding, changing, debugging, refactoring or reviewing behavior in a repository, feature or module. Locate capability and coordination owners, expose the chosen patterns' participants and relationships, and keep coherent code and its explanation together. Apply within ordinary implementation, not only architecture tasks.
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# Vertical Slices

**Leaf skill** in Software Engineering; reached through its domain or by name.

Keep the context needed to change a system local and understandable. A change
should be readable at the capability it affects, not reconstructed across global
`controllers/`, `services/` and `repositories/` folders. Apply this throughout
repository work — creating a repository, adding a feature, extending a
capability, maintaining existing code — starting from the affected slice and
respecting its existing ownership. A small change uses these boundaries; it does
not require a whole-system redesign.

Structure and named roles leave a route for the next change. A maintainer should
find where to extend a pattern, and which other mechanisms constrain it, without
the original conversation. A tidy tree alone does not preserve the intent behind
its boundaries, so identify the capability, its coordinating owner and its
participants before editing, and keep their explanations current while changing
them.

## Example: one change, one address

Fictional request: "Discount codes may now be used once per customer." The
repository is layered by technical role:

```text
src/
  controllers/checkout.py        # parses the code from the request
  services/pricing.py            # applies the discount
  services/orders.py             # re-checks expiry before placing the order
  validators/discounts.py        # checks expiry
  repositories/discounts.py
```

Expiry already has two owners, `validators/discounts.py` and `services/orders.py`,
and a usage limit would need a third decision about where it belongs. Arranged
by capability, the same behavior has one address:

```text
src/
  pricing/
    __init__.py          # public surface: quote(cart, code) -> Quote
    discounts.py         # code rules: expiry, usage limit, stacking
    store.py             # discount persistence; imported only inside pricing
    test_discounts.py
  checkout/
    api.py               # parses the request and calls pricing.quote
```

The gain is the single owner of discount rules, not the folder move: the limit
becomes one rule and one store query, and checkout cannot bypass it because it
only sees `pricing.quote`. In an ordinary feature task, that restructuring is
not yours to start. Add the rule beside the existing expiry check that actually
decides, and report the duplicate owner with its consequence; the move needs its
own authorization.

## Minimum surface as the design measure

Build the full intended capability with the smallest coherent system that can
honestly own it. **Min-Max Engineering** means maximum useful behavior for the
state, code, modules, dependencies, configuration and operational moving parts
needed to deliver it. The same capability with less system is an architectural
gain. Smallest means least error, state and search surface, not fewest lines: a
shared choke point may add code while giving a wrong behavior one address.

Ask before and after a design or implementation: what can be removed, what now
has one owner, and what became easier to change without losing capability,
robustness or safety? Before adding machinery, consider deleting obsolete
surfaces, consolidating owners, reusing an existing boundary, table-driving
repeated behavior or using an established pattern. Compatibility layers, broad
abstractions, fallback paths and parallel workflows must justify the states and
maintenance they add; a green suite does not excuse them.

There are no file-count or line-count targets. Comments, module briefings and
explanations preserve the model and its reasons; they are not volume to shave.

## Establish the model before cutting files

Read the affected code, vocabulary, requirements and architecture, and trace a
representative behavior from its entrypoint through decisions, state and
outputs. Distinguish the actual model from the requested change. When a settled
model is supplied, map it as given. When concepts, lifecycles or names stay
ambiguous, report that to the lead with the affected scenarios instead of
settling them here.

Test terms with real counterexamples: can two concepts change independently,
live for different times or mean different things in different contexts? Keep
the resolved vocabulary at its existing canonical owner; extend that explanation
rather than adding a second glossary or another methodology's folder names. A
substantial system needs a context map, each context's responsibility and
lexicon, and the terms whose meaning changes across boundaries.

Give each responsibility and maintained truth one canonical owner. Several
inputs are fine; independent writers or competing implementations of the same
responsibility drift. Similar code alone does not mean the same responsibility.

**One name, one job.** Separate meanings need honest names even while their
values agree:

```python
# Before: one constant, two jobs
MAX_RESULTS = 100        # API response cap, also used as the upstream page size

# After: either can change without silently changing the other
RESPONSE_CAP = 100       # most results one request may return to a client
FETCH_PAGE_SIZE = 100    # rows per upstream request, bounded by the provider
```

A comment cannot excuse a false declaration.

**Withhold, never fabricate.** Represent unavailable or undetermined separately
from absent, empty, false or expired, and make consumers decide what to do with
it. A `last_backup_age() -> timedelta | None` whose `None` means both "never
backed up" and "storage unreachable" lets a dashboard show a healthy blank during
an outage; a separate `Unknown` result forces the decision. A fallback may give
a less useful answer, but it keeps the contract's promises, including timeout
nesting, budget pairing and invariants when a dependency is missing.

## Co-locate by capability

Start from the business capability; technical roles live inside the owning
module. For each capability, identify its inputs, state, decisions, invariants,
outputs and expected changes, and keep what must be understood together
together. Split where responsibility, technology, failure behavior or a genuine
contract creates an independently understandable boundary. A broad product area
can be a namespace; independent capabilities inside it still need their own
owners.

Do not create tiny packages or numbered file chunks to hit a size target. A large
coherent file is a signal to examine its responsibilities, not permission to
scatter one state machine. Judge the blast radius and the implicit knowledge a
future change needs.

## Make the composition visible

A set of well-named leaf files is incomplete if the reader cannot find what
connects them. Show the composition owner, and how control and data pass between
participants, in code: a pipeline declaration, handler registry, transition
table, subscription wiring or explicit constructor composition.

Fictional brief: a monitoring capability runs website and provider checks, each
with its own request mapping, evidence rules and fixtures. A flat list of
`firebase.py`, `vercel.py` and `search_console.py` does not explain how a run
works:

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

`run.py` composes the stages through the Stage contract, and its declaration
shows ordering and permitted parallel work; stages never import or start each
other. Each provider folder owns its parts, with tests beside it or under the
matching test convention. `pipeline/` coordinates; it is not a place for
provider-specific rules. An existing `base/` or composition module can do the
same job if its responsibility is explicit, and a single small probe may stay
one file. Do not pre-create empty providers or wrappers for symmetry.

Use folders when a responsibility has several parts that belong together: a
state machine with `states/`, a transition policy and a coordinator; an
integration with adapter packages and a registry. A small machine can keep its
states in one table. Keep ordering out of import side effects. Separate the
owner of runtime sequencing from application startup when they differ: creating
dependencies does not explain which stage runs next or what a failure does to
the rest of the run. Name a mechanism — Composition Root, State pattern — only
after checking its defining roles in the code.

## Public surface and dependency direction

Give each module one intentional public surface, and have cross-module callers
use it rather than internals. Describe the inputs, results, error vocabulary,
ordering and state guarantees callers need. An interface that only forwards has
not earned its place.

Respect existing public boundaries even on a small change. Where boundary drift
is consequential, use the language's own enforcement — module-private
visibility, import constraints or dependency checks — and reuse existing
mechanisms before adding one. Derive any machine-readable dependency map from
actual imports or declarations rather than maintaining a second truth by hand.
New cross-module edges are deliberate, reviewable changes; a baseline of
existing edges can support a ratchet during a migration. A single-script tool
needs no map or gate merely to follow this method.

Keep operational scripts and contract checks with the system they protect.
Temporary authoring aids must be removable without breaking builds, tests or
operation, and a one-off inspection does not earn a permanent gate.

Keep each affected important module's briefing current at its package
documentation or entrypoint, written from the actual model and code, and link
wider architecture instead of copying it. A design proposal names where an
explanation belongs; writing it into source needs authorized implementation.

## Invariants live with their mechanism

Document and enforce a rule at its owner, usually the capability or command
boundary. A rule that exists only in prose leaves every writer free to break it.
State what must hold, where it is enforced and what breaks if it is violated.

For example: a subscription has at most one active plan, and changing plans ends
the old one in the same transaction. That rule belongs in
`subscriptions.change_plan`, not in the settings page, the admin tool and the
billing import separately; each of those calls the command. Only genuinely
system-wide rules belong at architecture level. Derive any whole-system index of
invariants from their owners rather than keeping a central duplicate, and let
tests point to the behavior's specification rather than a chapter listing tests.

## Shared Machinery and shared capability components

These are different responsibilities:

- **Shared Machinery** executes capability-neutral mechanics, such as a
  persistence skeleton, handler factory or hydration mechanism, with **zero
  capability-specific logic**. Each module declares its concrete queries,
  envelopes, contracts and error vocabulary; the machinery executes that contract
  and never generates or silently changes it.
- **Shared capability components** own genuinely common behavior, such as a UI
  interaction several screens use. The component owns the interaction; each
  consumer supplies its own data and wiring.

A generic repository base that each capability configures with its own queries
is machinery. Two pricing rules that look alike but answer to different business
owners are not a shared component, and merging them couples decisions that
should change independently. For each adoption, compare the consumer before and
after: net complexity must go down per module, or the mechanism stays out with
its reason recorded at the design owner. Rejecting a mechanism never licenses
duplicating the same responsibility, and resemblance alone is no reason to merge.

If a capability honestly is plain CRUD, binding a suitable generic mechanism
directly is clearer than wrappers with no responsibility. Moving onto Shared
Machinery keeps contracts and observable behavior, reviewable as near-verbatim
moves; a behavior change is its own decision.

## Patterns serve the architecture

Use established patterns when they reduce places to look, centralize enforcement
or make evolution safer: a state machine, registry, factory, adapter,
repository, event log, outbox or process manager can each earn a place. A
pattern that adds a layer without reducing the search or error surface is
decoration. Bounded contexts, ports, events and invariants matter through the
boundaries they express; do not rename a system after a methodology.

Consequential language, framework, provider, security, persistence, protocol or
runtime choices are decisions of their own, not a by-product of the layout.
Consult current primary sources for them; when one needs dedicated research,
report it to the lead. Keep the accepted choice and rationale at the
repository's design owner, and never invent citations.

If **Puppeteer** is available, use it for substantial exploration of independent
capabilities or competing boundaries before loading the whole system into the
main context; scouts return current owners, contracts, evidence and
disagreements, and the main agent reconciles them. A known local change needs no
parallel architecture study.

## Check and deliver the design

Walk three changes through the design: a normal domain change, a boundary
failure and a likely extension. For the discount example: a new stacking rule
lands in `pricing/discounts.py`; an unreachable discount store surfaces as a
`quote` error checkout must handle, not as "no discount"; a new code type adds a
rule and a test without touching checkout. Show where code, tests, invariants and
explanation live, how callers reach the public surface and which new dependency
edges appear, and compare state, error surface and needed context against
useful alternatives.

Then try the extension without chat history: can a maintainer find the
coordinator, the participant contract and the right folder for a new stage,
state or adapter, and see which ordering, failure and ownership rules it must
keep? Verify that against executable wiring, not a tree diagram. A flat module
or a nested layout may pass; neither a file limit nor a required depth does.

If a change still scatters across unrelated files, duplicates policy or depends
on knowledge hidden in another module, revise the ownership. Deliver the
vocabulary, capability and dependency relationships, interface decisions, needed
briefings, reasons and open questions at the existing design owner, scaled to
the change, and return scoped answers to whoever loaded this method. A
design-only request does not launch a refactoring; if implementation is
separately authorized, use mechanical, compiler- and test-checked moves where
structure changes across the tree.

Supplementary upstream methods are credited in [NOTICE.md](NOTICE.md).
