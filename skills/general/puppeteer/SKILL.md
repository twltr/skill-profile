---
name: puppeteer
description: Decide and coordinate native agent delegation for independent, verifiable work. Use when a task may benefit from a subagent, parallel work, or an independent review; small dependent tasks can stay with the main agent.
---

# Puppeteer

Own the requirements, decisions, shared contracts, integration, and final verification in the main agent. Choose among doing the work directly, assigning one bounded task, and running independent tasks in parallel. Delegate only when separation, specialist judgment, a large isolated read, or an independent check justifies the extra setup, model work, and integration. A deterministic lookup rarely does.

## Cut work at a stable boundary

For repository work, prefer a coherent user-visible capability or other independently testable outcome. Let one owner handle its necessary code and tests. Do not split UI, API, and data by layer while their contract is unsettled. A vertical slice is a design aid, not a rule that every slice gets an agent; use the existing `vertical-slices` skill when the code boundary itself needs judgment.

Before parallel work, identify prerequisites and shared resources in a short dependency list. Serialise a shared migration, contract decision, lockfile, generated output, Git index, database, or port unless ownership is isolated. Worktrees separate files, not contradictory semantics. One writer owns each shared resource.

## Give each agent a complete small contract

Provide the observable outcome, relevant requirements and invariants, exact inputs and accessible paths, starting revision and relevant local changes, allowed reads and writes, shared dependencies, acceptance evidence, output shape, and stop conditions. Include any user restriction that exists only in the main conversation. Use a fresh context when the client supports it; do not hand over the whole chat for convenience. In Codex, use `fork_turns="none"` by default and only one or two recent turns when a standalone brief truly cannot carry the needed information.

Use native read-only tools or sandboxing for research. A prompt saying "read-only" does not make a shell or connector harmless. Select a task-appropriate model and reasoning level. Narrow research may use a small model; difficult implementation or consequential review may need a stronger one. Do not force one cheap model on every task. Child agents must not delegate further; enforce this natively where available and otherwise mark it as an instruction, not a hard limit.

Require the result, changed artifacts or exact references, the checked starting state, tests actually run, unresolved risks, and the next action. No raw logs or work diary. A returned report is submitted for review, not verified. Inspect decisive evidence and changes without repeating all exploration. Resolve disagreement against the contract and reproducible behavior. After integration, run the checks affected by the combined state.

If a dependency, permission, requirement, or base changes, pause the affected assignment and rescope it. Do not let a subagent invent a wider task or start an identical replacement job while the first job's state is unknown.

Read [examples](references/examples.md) when the division is unclear. Read [evidence and limits](references/evidence.md) only when explaining or revising these delegation rules. `minmax-tokens` owns information economy and need not be loaded merely because delegation is considered.
