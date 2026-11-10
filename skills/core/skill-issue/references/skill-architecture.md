# Skill architecture: types, trees and dependencies

Read this when you create a skill, place it in a collection, add a router, or
review how skills load each other. It owns the type system and the edge rules;
`SKILL.md` keeps only the summary.

- [Why a tree](#why-a-tree)
- [The five types](#the-five-types)
- [Edge rules](#edge-rules)
- [Roles in domains and flows](#roles-in-domains-and-flows)
- [Declare type and dependencies](#declare-type-and-dependencies)
- [Place a new skill](#place-a-new-skill)

## Why a tree

Picture a room. The agent stands in the middle. Around it stand **core skills**
it can use anywhere, and several **trees**, one per domain: writing, software
engineering, design. Each tree has a root that decides where in the tree the
work belongs, inner nodes that compose or order methods, and leaves that do one
job well.

This shape exists for three reasons:

- **Routing saves context.** Only the roots compete for selection. A request
  loads one root and then only the branches it needs, instead of every skill
  whose description sounds related.
- **Flows define order and roles.** Multi-step work, especially with several
  agents, needs one place that says what happens in which order and who does it.
  The orchestrating agent follows the flow; delegates take single branches.
- **Leaves stay reusable.** A method that loads nothing and assumes no caller
  can be used by any router, by a flow, or by a user who names it directly.

A mesh, where skills call each other freely, loses all three: loads become
unpredictable, cycles make agents restart workflows, and no skill can change
without checking every other one.

## The five types

| Type | What it is | Selection | Loads |
|---|---|---|---|
| **Core** | A standalone method useful in any context | Implicit | Nothing |
| **Domain** | The root of a tree: establishes the context and routes into it | Implicit | Its children — one, several, or a role's pack |
| **Parent** | An inner node that groups children and applies them together | Explicit-only | Its children, without an order |
| **Flow** | An inner node that defines a sequence of steps and the roles that run them | Explicit-only, or loaded by its domain | Its step skills, left to right |
| **Leaf** | A self-contained method | Explicit-only | Nothing, ever |

Domain, parent and flow skills are **routing skills**: nodes that have children.

**Core versus leaf.** Both load nothing. A leaf belongs to a tree; a core skill
stands in the middle because every context can use it. A method may live as
core while no tree exists for its context yet. When you create one, ask whether
more skills of that kind will follow; if so, give it its domain early instead of
moving it later.

**Every leaf works alone.** A user can call a leaf by name, so it must not
depend on a caller's context, name a caller, or assume another method ran first.
It may state what input it needs.

**A flow orders, it does not own.** Each step skill in a flow stays usable
without the flow. The flow adds what no single step can: the order, the
hand-offs between steps, and conditions such as "use this flow only as the
orchestrating agent". Read a flow left to right; it does not reach further down
the tree than its own steps.

**Sub-domains are rare.** If a part of a domain needs its own selection, prefer
a parent skill. Introduce a nested domain only when that part is a context of
its own with several parents or flows beneath it.

## Edge rules

1. **Start in the middle.** Only core and domain skills are implicit. Every other
   skill is reached through a routing skill or by the user naming it.
2. **Edges point down.** A routing skill names its children; a child never names
   its caller. Results go back to whoever loaded the child.
3. **Never across trees.** If a skill in one tree needs work from another tree —
   a writing leaf that wants a diagram — it returns that need to the agent in
   the middle, which opens the other domain itself. A cross-tree edge means the
   trees are cut wrong, or the shared skill should be core.
4. **Branches do not reconnect.** When two siblings need the same child, the
   common parent loads it once for both. When only some siblings need it, add a
   parent for exactly those. When every tree needs it, it is core.
5. **Boundary mentions are allowed.** A description may say "logos belong to SVG
   Design" to prevent a wrong selection. That sentence routes nothing.

Example of rule 4: in an engineering domain, both the implementer and the
reviewer need the test-design leaf. Neither role's skills load it; the domain
lists it in both role rows, so it remains one edge from the common parent.

## Roles in domains and flows

A domain or flow may define **roles** instead of single targets: implementer,
reviewer, orchestrator, documenter. A role is a row that selects a **pack** —
the children that always apply in that role, plus conditional ones:

```markdown
| You are…      | Load always                            | Load when needed        |
|---------------|----------------------------------------|-------------------------|
| Implementer   | design-method, comment-method          | test-method             |
| Reviewer      | review-parent                          | its lenses              |
| Orchestrator  | delivery-flow                          | delegation-method       |
```

Packs can combine when an agent holds two roles at once. Mark combinations that
must not happen, for example "the orchestrator does not implement the work it
reviews". A delegate receives its role's pack by name in its brief, so it loads
the methods itself instead of receiving a paraphrase.

## Declare type and dependencies

The Agent Skills specification has no field for dependencies between skills;
its `metadata` field is a free map of string keys to string values, and
`compatibility` describes environment requirements such as tools or network
access. Use `metadata` for the machine-readable declaration:

```yaml
---
name: delivery-flow
description: …
metadata:
  skill-type: flow
  skill-tree: engineering
  skill-requires: review-parent delegation-method
---
```

- `skill-type` is one of `core`, `domain`, `parent`, `flow`, `leaf`.
- `skill-tree` names the domain a non-core skill belongs to.
- `skill-requires` lists, space-separated, the children without which a routing
  skill cannot do its job. Optional children appear only in the body. Leaves and
  core skills require nothing.

The agent learns the same facts after it has chosen the skill, from one line at
the top of the body:

```markdown
**Flow skill** in the engineering domain. Requires: review-parent, delegation-method.
If one is missing, stop, say this skill is incomplete without it, and do not run
a partial flow.
```

Keep both out of the `description`: the description decides selection, and a
dependency list there spends the selection budget on information that only
matters after the choice.

Humans see the type in the catalog through the short description, which starts
with it — `Leaf: Complete replacements and model corrections`, `Domain: Write
for the reader and purpose` — in `agents/openai.yaml` and
`metadata.short-description`.

**Check dependencies when installing, not while working.** The collection's
installation tooling should refuse to install a routing skill whose required
children are missing, and report edges that point up or across trees. The stop
line in the body is the fallback for hosts the tooling does not cover. To
distribute a tree as a whole, package it together, for example as one plugin.

## Place a new skill

1. **Does it load other skills?** No: it is a leaf or a core skill. Yes: it is a
   routing skill; continue with step 3.
2. **Is it useful in every context?** Yes: core. No: a leaf in the tree of its
   context. If that tree does not exist yet, decide whether to create the domain
   now or keep the skill as core until a second skill of that context appears.
3. **Does it define an order of steps or roles?** Yes: flow. Is it the entry
   point of a context? Yes: domain. Otherwise: parent.
4. **Check the edges** against the rules above with the collection's graph
   audit, then declare the type and requirements in `metadata`, the first body
   line and the short description.
