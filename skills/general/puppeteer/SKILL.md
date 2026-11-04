---
name: puppeteer
description: Decide and coordinate native agent delegation for independent, verifiable work. Use when a task may benefit from a subagent, parallel work, or an independent review; small dependent tasks can stay with the main agent.
---

# Puppeteer

Keep large investigations out of the main agent's context until they produce
useful evidence. Own requirements, cross-domain decisions, integration and final
verification in the main agent. For substantial work, normally delegate coherent
investigations, implementation packages or independent reviews; run independent
assignments in parallel when supported. A small clear change or deterministic
lookup stays direct when delegation adds more work than it saves.

## A scout and a useful return

For a cancellation feature, the lead identifies ordering, inventory and payment
as affected capabilities before reading all three implementations. One illustrative
brief is:

```text
Task: Find inventory behavior when an unfulfilled order is cancelled.
Inputs: The verified reservation entrypoint, current contract and relevant tests.
Boundary: Read-only; investigate inventory ownership, not the whole repository.
Return: Source-backed behavior, invariants, missing decisions and consequences
        for the cancellation design. Identify what you did not verify.
```

The scout reports that reservations can expire before cancellation arrives and
links the actual handling of already-released stock. The lead checks that evidence,
settles the public outcome and shares it with the ordering owner. Other scouts
work independently until a shared contract needs a decision. Summaries preserve
the evidence needed to steer; they do not transfer responsibility for the result.

Useful contrasts:

- A known one-file fix and its check stay direct.
- Two capabilities with settled contracts can be implemented concurrently by
  separate owners, with their own behavior checks and a combined integration check.
- Two assignments that need the same migration or API decision wait for that
  prerequisite; different filenames do not make them independent.
- A large diagnostic investigation can use a read-only analyst; plain counting
  and filtering belong to deterministic tools.
- An independent reviewer receives requirements and evidence without the author's
  conclusion. An implementer cannot approve its own work as independent review.
- A blocked agent returns the exact missing contract, evidence or access and
  preserves useful partial work; the lead resizes or unblocks the assignment.

## Cut work at a stable boundary

For repository work, prefer a coherent user-visible capability or other independently testable outcome. Let one owner handle its necessary code and tests. Do not split UI, API, and data by layer while their contract is unsettled. A vertical slice is a design aid, not a rule that every slice gets an agent; use `vertical-slices` when available and the code boundary itself needs judgment. Without it, establish ownership and contracts directly.

Before parallel work, identify prerequisites and shared resources in a short dependency list. Serialise a shared migration, contract decision, lockfile, generated output, Git index, database, or port unless ownership is isolated. Worktrees separate files, not contradictory semantics. One writer owns each shared resource.

## Give each agent a complete small contract

Provide the observable outcome, relevant requirements and invariants, exact inputs and accessible paths, starting revision and relevant local changes, allowed reads and writes, shared dependencies, acceptance evidence, output shape, and stop conditions. Include any user restriction that exists only in the main conversation. Use a fresh context when the client supports it; do not hand over the whole chat for convenience. Resolve the actual tool schema: in a host exposing only `fork_turns="none"` or `"all"`, a standalone brief uses `"none"`; do not invent a partial-history value.

Use native read-only tools or sandboxing for research. A prompt saying "read-only" does not make a shell or connector harmless. Select a task-appropriate model and reasoning level. Narrow research may use a small model; difficult implementation or consequential review may need a stronger one. Do not force one cheap model on every task. Child agents must not delegate further; enforce this natively where available and otherwise mark it as an instruction, not a hard limit.

Require the result, changed artifacts or exact references, the checked starting state, tests actually run, unresolved risks, and the next action. No raw logs or work diary. A returned report is submitted for review, not verified. Inspect decisive evidence and changes without repeating all exploration. Resolve disagreement against the contract and reproducible behavior. After integration, run the checks affected by the combined state.

If a dependency, permission, requirement, or base changes, pause the affected assignment and rescope it. Do not let a subagent invent a wider task or start an identical replacement job while the first job's state is unknown.

Use the host's capacity honestly; queue independent assignments in waves when
slots are limited. Delegation is also useful for research and conceptual work:
the useful cut is an independent question or outcome, not necessarily a code folder.

If `minmax-tokens` is available, use it when deciding how to retrieve or return
large evidence efficiently. If `grilling-with-agents` is available for an authorized
iterative planning session, it owns the questioning protocol while this skill owns
agent mechanics. If `engineering-review` is available for acceptance, it owns review
criteria and author independence. Return to an existing caller rather than calling
it recursively. Missing methods do not prevent a bounded native delegation when
its ownership and evidence are clear.

Read [evidence and limits](references/evidence.md) only when explaining or revising
these delegation rules.
