# Skill Profile

A curated collection of agent skills for Claude Code, Codex, Kimi Code and
Gemini CLI, composed as **trees** rather than a flat list. Each skill is a
complete package — instructions, metadata, references, scripts, assets,
licenses and provenance — that works on its own, and the collection defines how
the skills route to each other so an agent loads only what a task needs.

- Find a skill, its type and its provenance in [SKILLS.md](SKILLS.md).
- Read [AGENTS.md](AGENTS.md) before changing anything in this repository.
- The authoring method for new skills, including the full rules summarized
  below, is [Skill Issue](skills/core/skill-issue/SKILL.md) and its
  [architecture reference](skills/core/skill-issue/references/skill-architecture.md).

## The architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="figures/skill-architecture.dark.svg">
  <img src="figures/skill-architecture.svg" width="840" alt="The agent starts in the middle with six core skills and three domain trees; edges point only down or along the Road to Glory flow.">
</picture>

Picture a room. The agent stands in the middle. Around it are **core skills** it
can use anywhere, and **trees**, one per domain. A request enters a tree at its
root, which decides where in the tree the work belongs; the agent then moves
down that tree and nowhere else.

### Why trees

- **Routing saves context.** Only the roots and the core skills compete for
  selection. A coding request loads the Software Engineering root and the
  branch it needs, not every skill whose description mentions code.
- **Flows define order and roles.** Multi-step work — especially with several
  agents — needs one place that says what happens in which order and who does
  it. The orchestrating agent follows the flow; delegates take single branches.
- **Leaves stay reusable.** A method that loads nothing and assumes no caller
  can serve any router, any flow, or a user who calls it by name.

The alternative this replaced was a mesh: in November 2026 the 30 skills formed 39
mutually referencing pairs, the three most important engineering methods were loaded in
none of 20 realistic coding requests in a trigger test, and a small task could
pull in half the collection.

### Five types

| Type | What it is | Selected | Loads | In this profile |
|---|---|---|---|---|
| **Core** | Standalone method on the agent's surface, useful in any context | Implicitly | Nothing | Unslop, Editorial SVG Diagrams, MinMax Tokens, Puppeteer, Skill Issue, Workspace Management |
| **Domain** | Root of a tree; establishes the context and routes | Implicitly | Its children | Good Writing, Software Engineering, Design |
| **Parent** | Inner node that applies its children together | Through its parent | Its children | Engineering Review over its lenses; Design Review over critique and accessibility |
| **Flow** | Runs steps left to right, with roles, inside a tree | Through its domain | Its step skills | Road to Glory |
| **Leaf** | Self-contained method, always invoked manually | Through a routing skill or by a person | Nothing | Golden Comments, Customer Writing, Grilling, Grilling with Agents, … |

Domain, parent and flow skills are **routing skills**: nodes that have
children. Every skill has exactly one type, and the type fixes how it is
selected: core and domain are implicit; parent, flow and leaf are explicit-only.

**Selection decides the type.** What lies on the agent's surface — what it may
select by itself — is a core skill or a domain root. Everything else is invoked
manually: by a routing skill above it, or by a person. There is no
manual core skill. Grilling, the interview you start with "grill me", is a leaf
whose root is you: you call it, it loads nothing, and it works on its own.

A domain routes in one of two ways. Good Writing **selects** the one
specialist that owns the result. Software Engineering selects by **role** —
implementer, orchestrator, reviewer, documenter — and loads that role's
**pack**, the methods that always apply together in that role.

### Why there is no core flow

A flow that stands on the surface and starts by itself sounds useful, but it
cannot exist, for three reasons that follow from each other:

1. **It could only use core skills.** A flow in `core/` that called skills from a
   tree would make core depend on that domain, and core must stand alone.
2. **Core skills cannot be put in order.** They fire by themselves whenever they
   apply. A flow that arranged them in steps could not hold its sequence; they
   would fire across it.
3. **A sequence needs steps that wait.** Steps that are only called when the
   flow reaches them are not core but leaves or parents, and a node that orders
   such children is the root of a tree — a domain.

So every attempt at a core flow turns into a domain: a process that should start
by itself is a domain whose routing runs a flow, or orders its children itself.
The repository shows the same rule: `core/` holds no routing skill at all, and
every flow lives inside a domain folder, below the one skill there that fires by
itself.

### How an agent moves

1. **Start in the middle.** Only core skills and domain roots are implicit;
   from the middle the agent may enter one tree or several.
2. **Go down.** A routing skill names its children; a child never names its
   caller and returns its result to whoever loaded it.
3. **Never cross trees.** When work in one tree needs another tree, the need
   goes back to the middle, and the agent opens the second domain itself.
4. **Do not reconnect branches.** When two siblings need the same child, their
   common parent loads it; when every tree needs it, it is core.
5. **Read flows left to right.** A flow orders skills that remain usable
   without it; it adds the order, the hand-offs and conditions such as "only as
   the orchestrating agent".

### Four walks through the profile

**A quick fix.** "Fix the double charge when users click pay twice." The agent
enters Software Engineering, takes the implementer role and reads its pack:
Engineering Practices chooses an idempotency key, Vertical Slices keeps the
guard inside the payment capability, Golden Comments records why the key
exists. No flow, no delegation.

**Substantial work.** "Add cancellation across ordering, inventory and billing."
Software Engineering assigns the orchestrator role, which runs Road to Glory:
plan, delegate, review, document, close. Each delegate receives the implementer
pack by name in its brief through Puppeteer's `Skills:` field. The review step
loads Engineering Review, a parent that applies its lenses; the documentation
step switches the lead to the documenter role.

**Two trees, one task.** "Update the README for the new event bus, and write a
customer email announcing it." The README is documentation maintained with
code, so the agent enters Software Engineering in the documenter role; the email
goes through Good Writing to Customer Writing. Neither tree calls into the
other. Both may use the core skills Unslop and Editorial SVG Diagrams, which the
agent applies from the middle.

**A shared child.** The implementer and the reviewer both need Marshmallow
Tests. Neither role's methods load it; the Software Engineering domain lists it
in both role rows, so the branches never reconnect below the root.

### Declaring types and dependencies

The [Agent Skills specification](https://agentskills.io/specification) has no
field for dependencies between skills; its `metadata` field is a free map of
strings. Each skill therefore declares its place in `metadata`:

```yaml
metadata:
  skill-type: flow
  skill-tree: software-engineering
  skill-requires: engineering-review puppeteer
```

The agent reads the same facts in the first line of the body, after it has
chosen the skill, including what to do when a required child is missing: stop
and report the skill as incomplete rather than run it partially. Descriptions
stay free of both, because they decide selection. Humans see the type in the
catalog: every short description starts with it, as in
`Leaf: Complete replacements and model corrections`.

Dependencies are best checked when installing, not while working: an
installer should refuse a routing skill whose required children are missing
and report edges that point up or across trees. Packaging a whole tree
together, for example as one plugin, is the planned distribution unit.

## Status

The type system and the two existing domains are in place:

- **Software Engineering** is live as a role-based domain. In windowed trigger
  tests with `claude -p` it loaded on 20 of 20 coding requests, 16 of 16 unseen
  ones and 12 of 12 unseen PR-review and quick-fix requests, with no false
  positives; every other engineering skill is explicit-only and loaded through
  it. The evidence is in
  [its notice](skills/software-engineering/software-engineering/NOTICE.md).
- **Good Writing** routes to explicit-only writing specialists. It loaded on 19
  of 20 writing requests and 12 of 12 unseen ones, with no false positives
  ([its notice](skills/writing/good-writing/NOTICE.md)).
- **Design** is live as a selecting domain over Frontend Design, Design System,
  Motion Design, GSAP, SVG Design, UX Copy, Design Handoff and the Design Review
  parent; five of these were adapted from Anthropic's design plugin (Apache-2.0).
  Without the plugin it loaded on 20 of 20 design requests and 12 of 12 unseen
  ones, with no false positives, against 12 of 20 for the previous implicit
  skills; the evidence is in [its notice](skills/design/design/NOTICE.md).
  Editorial SVG Diagrams is core.
- **Writing and Software Engineering** share no edges: code-owned documentation
  and source comments belong to Software Engineering.

Every skill declares its type in `metadata`, in the first line of its body and
in the prefix of its short description. No skill names its caller or a sibling
leaf, no edge crosses between trees, and shared leaves are only suggested.
`skills/core/skill-issue/scripts/check_tree.py skills` lists every remaining rule
finding; the installer refuses a collection with a missing type or required child. The [writing map](SKILLS.md#writing-family-map) and the
[engineering matrix](SKILLS.md#engineering-tree-map) show what is left;
`skills/core/skill-issue/scripts/skill_graph.py` measures it.

## Layout

The folders follow the selection rule, so a skill's place tells how it is
reached:

- **`core/`** holds skills that fire by themselves on the first level and shape
  behavior throughout a session. A core skill may serve several domains — Unslop
  is about prose and Editorial SVG Diagrams about figures, yet both apply in any
  context, so neither waits below a domain.
- **`writing/`, `software-engineering/`, `design/`** each hold one tree. Only the
  domain's routing skill fires by itself; everything else in the folder is
  reached through it or by name.
- **`extras/`** holds shared leaves: explicit-only skills that several domains
  can use, outside every tree, such as Grilling and Grilling with Agents. A
  person starts them; a routing skill may suggest one under a stated condition
  but never loads it.

The domain folders are also the planned packaging units: Writing, Software
Engineering and Design can each ship as one plugin; core and extras install as
plain skills.

```text
skills/core/                   Core skills: automatic, cross-domain
skills/writing/                Good Writing and its specialists
skills/software-engineering/   Software Engineering, its flow, parent and leaves
skills/design/                 Design, its leaves and the Design Review parent
skills/extras/                 Manually selected skills outside every tree
figures/                       Editable SVG maps of the collection, light and dark
archive/                       Complete previous package snapshots (ZIP + manifest)
```

Installation is flat: each client sees `<skill-root>/<skill-name>/SKILL.md`;
the folders above group ownership and routing, not installation paths.

## Using the skills

Copy a complete skill folder — never only `SKILL.md` — into your client's skill
root, for example `~/.claude/skills/` for Claude Code or `~/.codex/skills/` for
Codex. Install a routing skill together with the children it lists in
`skill-requires`. Explicit-only skills declare that in `agents/openai.yaml`
(`policy.allow_implicit_invocation: false`); for Claude Code, set
`disable-model-invocation: true` in the frontmatter of the installed copy.
Tools, MCP servers and accounts a skill mentions are not installed by copying it.

## License

Original work in this repository — the skills that name no other source, the
documentation and the figures — is released under the [MIT License](LICENSE):
anyone may use, copy, modify, merge, publish and redistribute it, keeping the
copyright and permission notice. Each skill package carries its own license file,
so the terms travel with every installed copy.

When you reuse a skill, say where it comes from — "adapted from the Skill
Profile's Golden Comments", "contains material from Matt Pocock's skills" — as
we do for every source below. Many skills are adapted from other people's work
and modified here. They keep
their original license beside a `NOTICE.md` that names the source and what we
changed:

| Skills | Source | License |
|---|---|---|
| Accessibility Review, Design Critique, Design Handoff, Design System, UX Copy | Anthropic design plugin 1.2.0 | Apache-2.0 |
| Frontend Design | Anthropic skills | Apache-2.0 |
| Skill Issue | Anthropic and OpenAI Skill Creator, earlier Matt Pocock influence | Apache-2.0 (see its notice) |
| Unslop | Pstack Unslop, Humanizer, Writing Clearly and Concisely | MIT |
| GSAP · Motion Design · SVG Design | GreenSock · LottieFiles · OpenData | MIT |
| Grilling, Grilling with Agents, Wizard, Writing Fragments, Domain Modeling, Improve Codebase Architecture | Matt Pocock | MIT |
| Engineering Review | Theo Browne | MIT |
| Road to Glory, Marshmallow Tests, Vertical Slices | Own work with adapted techniques from Matt Pocock | MIT (both notices) |

Editorial SVG Diagrams, Good Writing and Commercial Writing came from the
owner's own exports without a license file; the owner confirmed authorship on
2026-11-10, so they are original work under MIT. [SKILLS.md](SKILLS.md) records
the provenance of every skill.
