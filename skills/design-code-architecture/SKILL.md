---
name: design-code-architecture
description: Clarify domain meaning or design capability boundaries and module structure when an architecture task or an authorized implementation needs that decision. Produces a reasoned model or design; it does not implement a refactoring.
---

# Design Code Architecture

Turn the requested capability or structural problem into a design that a
maintainer can understand and change locally.

Use the parts needed by the current decision. Clarifying a term yields a
resolved meaning at its existing owner; it does not require redesigning the
whole codebase. Within another workflow, return the clarified model or design
to that workflow before it continues.

## Establish the model

Read the applicable instructions, existing vocabulary and architecture sources
for the affected area, then trace representative behavior through the code.
Separate current behavior from the requested outcome. Resolve overloaded terms
with concrete counterexamples: can these concepts change independently, have
different lifetimes, or mean something different in another context? Put resolved
meaning with its existing owner; do not create a competing glossary or impose
a fixed documentation layout. Surface unresolved domain decisions before
designing a structure that depends on them.

## Derive the boundaries

1. Name the capabilities, the changes they must support and the invariants each
   controls. Group the technical parts of one capability together. Split where
   responsibility, change reasons or failure behavior can be understood apart;
   do not start from a universal folder template or a target file size.
2. Give each module an explicit public boundary. Describe what callers need to
   know: inputs, results, errors, ordering and state guarantees. Keep internal
   choices private; make significant invariants enforceable at the owner rather
   than requiring every caller to remember them. Interfaces earn their cost by
   hiding useful complexity, not by forwarding calls through more layers.
3. State dependency direction and ownership of shared data. Choose native
   enforcement where a boundary can otherwise drift; make new dependencies
   reviewable. A dependency map should be derived from actual declarations
   when possible, rather than maintained as a second implementation.
4. Separate genuinely shared capability behavior from generic execution.
   Shared execution may run a declared contract; the capability keeps its
   policy, queries and error meanings. Consolidate the same responsibility,
   but keep similar code with different reasons to change independent. Judge
   whether each affected consumer becomes simpler; reject forced generality.
5. At a consequential choice, compare the smallest useful alternatives against
   concrete change cases, failure isolation and testability. Verify relevant
   current primary sources for unfamiliar technology or patterns. Record the
   selected reason and material trade-off; a pattern name is not the evidence.

## Check and deliver

Walk a normal change, a cross-boundary failure and a likely extension through
the proposed design. Show where code, tests, invariants and explanation would
live, and which public contracts would change. If one behavior still requires
unrelated files or duplicated policy, revise the ownership before presenting it.

Deliver the design at the project's existing decision owner: vocabulary changes,
capability boundaries, dependency direction, the reasons and remaining decisions.
A small diagram or table is sufficient where it communicates those facts.
If implementation was also requested, identify the agreed design and verification
boundary before continuing; a design-only request ends with the proposal.

Adapted source methods are credited in [NOTICE.md](NOTICE.md); no other skill is
a required runtime dependency.
