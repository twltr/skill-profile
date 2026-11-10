---
name: puppeteer
description: Decide and coordinate native agent delegation for independent, verifiable work. Use when a task may benefit from a subagent, parallel work, or an independent review; small dependent tasks can stay with the main agent.
---

# Puppeteer

Keep large investigations out of the main agent's context until they produce
useful evidence. Keep requirements, cross-domain decisions, integration and
evidence coverage with the main agent. Delegate specialist judgments the lead
cannot competently establish; coordinating acceptance does not mean personally
certifying every part. For substantial work, normally delegate coherent
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

## Match the phase and the capability

Apply this routing by default when assigning work; it needs no special user switch.
Match uncertainty, consequence and modality, not only the phase's name:

- **Planning and unresolved design:** a suitable strong main model can retain the
  work or use similarly capable scouts. A narrow factual lookup still belongs to
  deterministic tools or a sufficient bounded researcher.
- **Settled nonvisual implementation:** prefer a sufficient efficient worker when
  requirements, contracts and acceptance are clear. A plan file alone does not
  establish that clarity. Escalate unresolved or high-consequence implementation,
  or a demonstrated capability gap, before accumulating repeated failed attempts.
- **Independent review:** prefer a strong reviewer suited to the actual change.
  Review strength does not expand scope: inspect the change and relevant consumers;
  recheck affected behavior after corrections, widening only for new evidence.
- **Visual planning, creation and review:** assess visual judgment and access to
  rendered results separately from coding ability. A good refactoring worker may
  need a different author for a diagram or interface, and another independent
  reviewer for its visual quality.

When selecting or reassessing delegate models, read the shared
[model routing reference](references/model-routing.md). It owns current preferences,
verified identifiers, host limitations and the usage feedback rule. Native client
configuration owns executable bindings and defaults; do not change the main model,
settings, account or provider merely to follow this table. Check the actual spawn
schema and role restrictions: a preset can lock a model or effort. Use an available
role that supports the required choice instead of assuming a label such as
"reviewer" makes its fixed model suitable.

For example, a code-focused lead refactors a settings flow and needs a diagram.
It settles the behavior and hands the verified model, existing visual direction
and embedding constraints to a visually capable author using the relevant design
skill. After integration, a separate capable reviewer receives the brief, exact
revision and rendered narrow/wide or light/dark states, without the author's
approval. The lead verifies behavior and reconciles the specialist's findings;
the author corrects defects and the reviewer checks the changed renders. Authoring
includes material composition decisions, not only typing the SVG or CSS.

Independent agents may use the same model in separate contexts. Provider diversity
is not required. A small suitable task can stay direct, but that does not waive
required independent review. If a capable author, independent reviewer or rendered
access is missing, state that particular gap and continue unaffected work. Source
validity, a model name or author self-critique cannot stand in for visual acceptance.

## Cut work at a stable boundary

For research and design, a boundary can be an engineering concern rather than a
code capability. Select questions relevant to the change; a new application needs
an initial view across the concerns, while a small feature may touch only a few.
Assign one coherent topic to an agent, or split a broad topic into independent
subquestions or competing analyses. Several agents may investigate one topic when
that produces distinct evidence; the topic list is not a required agent count.

For example, a design investigation might separate data lifecycle and recovery
requirements from protection needs and trust boundaries, sharing the same workload
and constraints. The lead then resolves interactions such as retention versus
deletion requirements. These are example topics, not a required design or team.
Keep common assumptions, dependencies and decisions visible to all affected agents;
return material decisions for challenge before integrating their recommendations.
If **State of the Art** is available, it owns evidence research; if **Grilling with
Agents** is available and selected, it owns iterative challenge. Reuse an active
caller's topic scope and return results to it without restarting either method.

For repository work, prefer a coherent user-visible capability or other independently testable outcome. Let one owner handle its necessary code and tests. Do not split UI, API, and data by layer while their contract is unsettled. A vertical slice is a design aid, not a rule that every slice gets an agent; use `vertical-slices` when available and the code boundary itself needs judgment. Without it, establish ownership and contracts directly.

Before parallel work, identify prerequisites and shared resources in a short dependency list. Serialise a shared migration, contract decision, lockfile, generated output, Git index, database, or port unless ownership is isolated. Worktrees separate files, not contradictory semantics. One writer owns each shared resource.

## Give each agent a complete small contract

Provide the observable outcome, relevant requirements and invariants, exact inputs and accessible paths, starting revision and relevant local changes, allowed reads and writes, shared dependencies, acceptance evidence, output shape, and stop conditions. Include any user restriction that exists only in the main conversation. Use a fresh context when the client supports it; do not hand over the whole chat for convenience. Resolve the actual tool schema: in a host exposing only `fork_turns="none"` or `"all"`, a standalone brief uses `"none"`; do not invent a partial-history value.

Use native read-only tools or sandboxing for research. A prompt saying "read-only"
does not make a shell or connector harmless. Select the model and effort through
the phase/capability routing above and verify the effective selection where the
host exposes it; a requested model is not proof of the model that ran. Child agents
must not delegate further; enforce this natively where available and otherwise
mark it as an instruction, not a hard limit.

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
