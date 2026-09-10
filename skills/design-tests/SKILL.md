---
name: design-tests
description: Design or improve tests and test strategy for specified behavior, invariants or regressions. Use when choosing test boundaries, adding meaningful coverage or evaluating an existing suite; merely running established tests does not require this workflow.
---

# Design Tests

Build the smallest set of checks that can distinguish the required behavior
from the failures that matter, and tell a maintainer where a failure belongs.

## Derive the units from behavior

Read the requirement and trace the affected component's inputs, decisions,
state and outputs. Locate the invariants and contracts with their owners.
Group behavior that must be understood together into a logical unit; a function,
class or directory is not automatically that unit. Use existing test boundaries
when they can show the distinction. Where a missing requirement changes the
expected answer, resolve it before encoding an oracle.

Choose the narrowest sufficient view. Use isolation where it lets a case drive
the real decision; add integration when ordering, contention, persistence or
protocol behavior only exists between participants. Name those participants and
the additional fact the integration proves. Neither universal mocking nor a
blanket ban on component or end-to-end tests answers this decision.

## Build discriminating cases

1. Derive expected results independently from the requirement, a worked example
   or known behavior. Check important contracts at the point they matter so a
   mismatch is named there rather than appearing as a distant downstream error.
   For state invariants, arrange a meaningful precondition and check the relevant
   transition as well as its result.
2. Make doubles capable of representing both sides of the distinction. Model
   failure, emptiness and unavailable data separately when the behavior does.
   Control time, ordering or contention deliberately rather than relying on
   sleeps or a permissive default that makes every branch succeed.
3. For a regression, obtain a focused reproduction that fails for the reported
   reason on the unfixed implementation and passes after the correction. If
   the old structure cannot run the new guard, show another direct reproduction
   and explain that limit. A guard green before the fix is not its evidence.
4. When developing test-first, use small feedback cycles: failing behavior,
   minimal implementation, then improvements that keep the oracle intact.
   Avoid a speculative farm of tests for an implementation that does not exist.
   Existing agreed contracts do not need fresh human approval for each test.

## Keep the suite understandable

Keep a logical unit's cases together and name them for current behavior.
Each independently arranged case should be independently runnable. Parameterize
only a shared arrange/act/assert flow whose rows are declarative input and
expected output; split cases when rows choose different control flow. Shared
setup belongs at its narrowest common owner and must not supply expected
business truth. Explain non-obvious expectations and link their maintained
specification where one exists, not temporary work identifiers.

For an existing suite, ask what failure each check can detect and whether its
double can expose it. Remove implementation-coupled or redundant checks only
after identifying the surviving evidence or deliberately excluded requirement.
Do not delete another active change's oracle to make a cleanup look smaller.

Run the affected cases and relevant combined checks. Deliver the tests, their
coverage rationale and observed results; for a strategy-only request, deliver
the proposed units, risks and checks without altering the implementation.

Adapted source methods are credited in [NOTICE.md](NOTICE.md).
