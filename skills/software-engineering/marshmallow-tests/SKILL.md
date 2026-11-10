---
name: marshmallow-tests
description: Design tests around coherent units, invariants and precise failure addresses. Use when choosing test boundaries, adding cases or regression guards, or improving a suite; merely running existing checks does not need this method.
---

# Marshmallow Tests

Prove invariants, contracts and final-state behavior with the smallest suite that
can honestly do so. A suite is not worth its count. Its structure must let a
maintainer understand the protected behavior and locate the failure without
reconstructing a hundred scattered checks.

Derive the units, vocabulary and evidence from the actual system.
Use focused diagnosis and test-first feedback where they help establish the
behavior; neither replaces understanding the unit and its invariants.

## One invariant with discriminating evidence

Illustrative test contract, not executable project code:

```text
Given an unpaid invoice for 100 and a payment event P for 30,
when P is delivered twice,
then the ledger records one P and the remaining balance is 70.

Two ledger entries identify duplicate storage.
A balance of 40 identifies duplicate application.
```

These checks describe one meaningful payment flow. A concurrent-delivery or
restart case earns a wider test only if the isolated flow cannot expose that
failure. Derive the real unit, numbers and outcomes from the system's contract.

## Cut top-down, starting with the system

First understand the affected system: components, interactions, critical paths,
external interfaces and data flow. Only then ask what must be separated inside
a component so its behavior can be understood and tested coherently. A small
component may need no subdivision. Separation made without the picture above it
is a guess.

Find the logical parts, which parts belong together and where invariants and
contracts cluster. The unit is often a **capsule** that receives, decides, changes
state and emits, but derive the capsule from the actual system. An actor may be
the unit in a work-dispatch runtime; authorization, capture and refund in a payment
system; scene state, pass ordering and resource lifetime in a renderer; a stage
in an ingest pipeline. Do not import another system's unit names blindly.

To derive a unit, start with a behavior and ask upward: who does it, in what
role, why does it happen, which larger lifecycle contains it and what else can
happen in that lifecycle? That coherent cycle is the unit; the starting behavior
is one case within it. A function, class, message kind or folder is not
necessarily an independently meaningful test unit.

## Two questions determine the necessary test levels

1. **If this fails, is it enough?** Does the failure identify the logical unit and
   tell me which invariant or decision broke inside it? When it does, adding
   another address for the same fact does not improve the evidence.
2. **Is the isolated view enough?** Can this view expose the ordering, contention,
   persistence, protocol or hand-off behavior that matters, or does that fact
   exist only when participants interact?

The second question earns the next level: unit, between units, component,
component-to-component, business case through an application or between
applications. Name the participants and the additional fact a higher level proves.
A wider test is useful when the narrower view structurally cannot show the behavior,
not merely because more levels look thorough.

Use isolation and controlled doubles when they let cases drive the real decisions.
Do not impose universal mocking or ban entire categories of component or end-to-end
tests. For a replaceable external counterpart, weigh whether its stable contract
is enough and simulate inbound messages where appropriate. Binding a cross-application
suite to a volatile neighbor needs a clear benefit; a stated decision not to add
that tier can be sound.

## One logical address, meaningful cases inside

Keep the cases for a logical unit together in one file, or a coherent named
package when several independently understandable units justify it. No numbered
chunks or per-function files to satisfy a line limit. The file is the coarse
address; the case name and failure message give the fine address within it.
Do not create a new file for every small distinction.

The test runner collects independent cases. Never build a parent test that calls
child tests, or hide distinct flows behind an if/switch dispatcher to reduce
function count. That creates a second test language, misleading fixtures and a
shared hotspot for unrelated cases.

Parameter rows are data. Use one matrix only when every row runs the same
arrange/act/assert body with different inputs and expected values. If rows select
different setup, calls or assertions, use separate named cases in the same unit.
A semantic parameter ID does not excuse branching on that ID.

A case is a whole meaningful flow, with checks where decisions matter. For
example: the named entry exists, lookup returns the expected record, the work
item is created and the recipient holds it. Each failing condition must explain
what was expected and where. One fat test that cannot locate its failure is no
better than many microscopic checks without context.

Give the unit's file a compact explanation of what it covers, why those behaviors
belong together and where they are specified. Each case's expected result needs
a discoverable reason: a clear case name, assertion and referenced contract can
supply it. Add prose when the rationale is not evident there, especially for
non-obvious boundaries; do not narrate the test code or repeat an obvious assertion.

## Make the evidence discriminate

Derive expected results independently from a requirement, a worked example or
known behavior. Do not compute the expected answer by copying the implementation.
A missing requirement is a question to resolve before encoding an oracle.

Invariants are explicit targets. State them at the capability they govern and
prove them at the relevant decision point. For a data invariant, establish the
meaningful precondition and check before and after the manipulation that could
break it. For a behavioral branch, represent both outcomes with cases or a genuine
declarative matrix. A passing final-state check alone can conceal that the fixture
never exercised the claimed distinction.

Check a critical contract **inside a test of the unit's real behavior**, naming
the contract when it fails rather than letting a mismatch surface several layers
later. Avoid an isolated farm of schema-shape assertions when the behavioral case
can exercise the same seam and prove its use. A focused contract case is legitimate
when it reveals an independently relevant failure.

Test our system in its vocabulary. "I am authenticated; what does our component
do?" treats authentication as the premise rather than retesting the vendor.
Keep adapter and protocol tests identifiable beside their adapter so readers
can see which assumptions belong to one neighbor and which survive replacing it.

Inspect relevant shipped defects for missing guards. For a regression, reproduce
the failure against the unfixed behavior, then show the guard passing after the
repair. A guard green before the fix never demonstrated the defect. If a changed
structure prevents the new guard from running on the old code, show a direct
reproduction and state that limit.

Question every double: can it represent the distinction under test? An empty-list
stub, a status the system never emits or a permissive default can pin the defect
green by making two paths indistinguishable. Model missing, unavailable and empty
separately when the real contract does. Control clocks, ordering and contention
instead of relying on sleeps or accidental test order.

## Share construction without sharing expected business truth

Shared setup belongs at its narrowest common owner. When another case needs the
same neutral client, session, store, transport, clock or application harness,
reuse one helper or fixture rather than rebuilding it. Keep it beside local cases
or in explicit package support when genuinely shared across files.

A fixture executes setup; it does not own capability policy, expected business
truth or assertions. Do not centralize one-use setup speculatively. Split a large
file only when its logical units have independent purposes, failure modes or
setup, not because its line count feels uncomfortable.

## Improve an existing suite without losing its oracle

For each check, ask what failure its absence would hide. Count protected rules
rather than sampled scenarios or assertions. If several cases only compensate
for scattered enforcement, consider whether enforcement belongs at the real
boundary before cutting their evidence. A test deletion follows understanding
of the behavior; it is not a quota.

Delete redundant or implementation-coupled checks only after identifying the
surviving test that protects the requirement, or the requirement deliberately
retired with its implementation. Never delete the suite another active refactoring
needs as its oracle.

Temporary migration scaffolding and transient development states do not justify
permanent test farms. A shipped defect protecting durable behavior can still
deserve a regression guard. A grep for a string is not proof that a callable
contract works: exercise the real surface and report the expected and actual
identifiers when that is the relevant behavior. Text searches can inspect prose
or stale references as one-off authoring checks; they are not runtime evidence.

Use current semantic names, not roadmap IDs, waves or meeting labels, in files,
cases, fixtures and parameter IDs. Test provenance is the invariant and its
canonical descriptive specification. References run TEST → DOC; a documentation
chapter does not need a duplicate list of every test. History may point to tests,
while tests should remain understandable when the old work item is forgotten.

## Run the feedback loop and deliver

When developing test-first, work in small cycles: a failing behavioral case,
the smallest correct implementation, then improvements that preserve the oracle.
Do not write a speculative inventory of tests for a guessed implementation.
An already agreed requirement does not need fresh human approval for every case.

Run the affected cases and the necessary combined checks. Deliver the unit cuts,
protected behavior, actual evidence and limits. A strategy-only assignment ends
with the proposed units and checks; it does not modify production code. For a
suite edit, report which surviving evidence justified any deletion.

Supplementary TDD and diagnosis methods are credited in [NOTICE.md](NOTICE.md).
