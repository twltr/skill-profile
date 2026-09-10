---
name: min-max
description: Human-invoked Min-Max/refactoring work to reduce system complexity while preserving agreed capability and behavior. Never start automatically from a code smell, routine completion or a project reference.
disable-model-invocation: true
---

# Min-Max

Improve the chosen system so the same intended capability needs less state,
error surface, duplication, search and operational machinery. This is deliberate
structural work, not a line-count contest.

**Start only on an explicit human request for this work.** A skill reference in
project instructions, another skill or a review finding is not that request.
An analysis-only assignment ends with findings and a proposal; it does not
silently become a refactoring. Once the human has authorized the improvement,
complete the ordinary steps within that scope without asking again for each edit.

## Define the Min-Max gain

Establish the requested scope, intended capability, constraints and observable
behavior that must survive. Inspect the actual working tree and preserve unrelated
changes. Identify what the user wants improved rather than inventing a whole-repo
cleanup from a small request.

Ask of the existing construction and the proposed result:

- What capability does it own, and which future changes must remain possible?
- Which state, dependency, duplicate owner, fallback or operational part can disappear?
- What would make a mistake have one address and a change need less scattered context?
- Can deletion, consolidation, reuse or an established pattern achieve the gain
  before a new abstraction is introduced?

A shared mechanism can add lines while reducing the whole system. Deleting
necessary comments, tests or explanations to improve a count is not a Min-Max gain.
Record the concrete improvement so the final state can be compared against it.

## Classify before deleting

Distinguish canonical implementation, adapters, live migrations, generated
artifacts, compatibility paths, mocks, dead code, duplicate helpers, shadow state
and documentation/configuration drift. Cleanup here is architecture work:
removing an obsolete surface is usually more valuable than shaving its internals.

For a deletion or migration candidate, establish its path, current owner, reason
for existing, replacement, verification and whether it can disappear now or only
after a consumer migrates. Verify every dead-code claim against the whole relevant
tree: entrypoints, bootstrap, scripts, registries and dynamic loading as well as
static callers. An unused-code report or another agent's finding is a lead to
check personally, not proof of safe deletion.

Two implementations of the same responsibility need one canonical target and a
migration/removal decision. A named temporary coexistence can be legitimate;
"we left both just in case" is a second permanent truth.

## Preserve an independent behavioral oracle

Run the relevant existing checks before changing their oracle and record baseline
failures separately. Where the behavior is not represented, obtain the smallest
useful characterization from the known contract or observed inputs and outcomes.
Do not invent expected behavior for an unresolved requirement.

Keep the checks that unfinished migration steps depend on. An unchanged behavioral
suite is strong evidence that an extraction preserved its contract. Moving a test
or adapting its structural setup is different from changing its expected result.
If an expectation must change, expose the behavior decision; never weaken it to
make the refactoring pass.

## Move the responsibility whole

Choose the canonical target and identify every consumer, stored shape, config
entry and public contract the move affects. If the old model is false, correct
its declarations and consumers rather than hiding it behind filters or new aliases.

Cut changes into attributable, verifiable steps with a recovery point appropriate
to the risk. Use mechanical, language-aware moves across the tree and check them
with the compiler and relevant tests. Coordinate shared owners before consumer
edits. The steps must be recoverable; there is no universal rule requiring one
consumer per commit or a particular worktree or migration framework.

For Shared Machinery, identify the generic execution being extracted and the
concrete contracts that stay declared at each capability. Compare moved
contracts directly. Keep capability logic out of the machinery and verify that
net complexity goes down for each adopting module. A rejected mechanism needs a
reason, not another copy of the same behavior. Shared components instead own
common capability behavior; their consumers keep only their own data and wiring.

Retire old implementations, configuration, retired-only fixtures and stale
references when their consumers have moved. Check real loading and operational
paths, not merely one text search. A temporary bridge needs an agreed owner,
removal condition and short route to deletion. Do not turn a completed migration
into a permanent compatibility layer.

## Verify the gain and finish

Run the behavior and interaction checks affected by the change. Review the full
diff for accidental semantics, duplicate owners and unrelated edits. For each
removed behavioral check, identify surviving evidence or the deliberately retired
requirement. Check the actual contracts and loading paths after removal.

Compare the complete resulting system with the stated Min-Max gain, including
its consumers and operating parts. A smaller helper beside unchanged parallel
logic has not completed the consolidation. Keep Golden Comments and system
explanations current where the construction changed.

Update the owning workboard and outcome record, remove completed temporary plans
and artifacts, and finish cleanup in the same work. Preserve evidence still needed
by open work. Report what became simpler, what behavior was preserved, the checks
and their limits, and any remaining authorized migration step. Passing local tests
does not establish that a live deployment or migration happened.
