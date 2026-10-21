---
name: technical-writing
description: "Write or revise repository READMEs, system explanations and architecture documentation. Make the system understandable through purposeful Markdown, grouped topics and diagrams of relationships and behavior. Source comments belong to Golden Comments. Automatic selection disabled; use only by explicit user request or through Good Writing."
---

# Technical Writing

Use this method only when explicitly requested by the user or selected by Good
Writing. An ordinary matching request goes through that router.

Explain the system so a new developer can understand its construction, reasons
and constraints without reconstructing them from scattered implementation.
This method owns repository documentation and READMEs. Source comments and local headers
have their own owner in Golden Comments.

Establish the intended reader, question, repository
conventions and actual implementation before choosing the documentation shape.
Preserve a working book structure outside the requested change.

Accept the reader, purpose, source material and constraints from Good Writing
when supplied. Direct invocation works without that router. Do not invoke Good
Writing from here. **Always apply `unslop`**, including during direct use. Load
it once through the host's skill catalog and returned path or read interface
unless already loaded. If unavailable, name the missing dependency and leave
the language review open; continue independent preparation without claiming
the full method was applied.

## Make a mental map before writing paragraphs

Show what the system does, its parts and their relationships before expanding
the detail. Think like a mind map: cluster related concepts, expose the hierarchy
and connect dependencies. This is a reading model, not a requirement to draw a
radial diagram. Prefer visible structure to a long linear explanation.

Use the full useful range of supported Markdown: headings, grouped lists,
numbered procedures, emphasis, inline code, language-tagged code examples,
links, images and comparable tables. Unslop owns their shared usage rules.
Choose each form for its information: lists for parts, steps for order, tables
for common attributes, diagrams for relationships. Use highlighting, callouts
and collapsible detail only where the renderer supports them. Essential
conditions stay visible. Verify the rendered result, not just its source.

Aim for little prose and much usable information. Keep the reasons, conditions,
invariants and uncertainties needed to understand the system. A few clear
sentences can carry meaning a diagram cannot. Avoid repeating visible content
as a paragraph and then summarizing it again.

Link details only where a different depth helps. Keep common facts at one owner:
six timers with the same fields belong in one shared table, not six repeated
tables or six new pages. Prose around it explains a relationship or consequence.

A bundle of MCP servers may need an overview of included servers and their
release status, product details for each server, and version sheets for support
status, pinned dependencies and delivery conditions. Use these levels when the
questions justify them; they are an example, not a required page hierarchy.

## A book that works forward and as a reference

A multi-part system can use a stable book under docs/ when its explanations
need separate chapters. Follow the repository's established organization.
Its map, often docs/00-README.md, routes every maintained chapter and provides
useful reader paths, such as operator, developer and agent. Go from the whole
picture to detail: orientation, prerequisites and vocabulary, relationships,
then the individual capabilities and mechanisms.

Where used, numbering expresses that didactic order. It is not a requirement to read every
previous chapter for each task. Support both the person learning the system
from the beginning and the person looking up one concrete question.
A small repository can be fully explained by a short README; do not invent an
empty book or ignore an explicit project exception.

Give each chapter a short purpose header: what question it answers and for whom.
Use the Diátaxis distinction between tutorial, how-to, explanation and reference.
Do not mix four different reading jobs into a chapter just because they mention
the same tool. Keep the existing source of truth for each fact.

## Keep the structure shallow; cluster substantial subjects

Group the closest related concepts under their common subject, as in
hierarchical clustering. Prefer a shallow documentation structure. A core
subject with independently useful parts can earn a folder; an isolated option
or minor behavior cannot. Each document owns a capability, mechanism or contract
with a clear reader question. Keep inseparable explanations together.

For example, Agents and Flows may be central subjects in a multi-agent runtime:

```text
docs/
  README.md
  architecture.md
  agents/
    README.md
    coordinator.md
    reviewer.md
  flows/
    README.md
    intake/
      README.md
      flow.html
      flow.svg
    review/
      README.md
      flow.html
      flow.svg
```

The Agents README explains collaboration and links to each role's purpose,
inputs, responsibilities, boundaries and behavior. A role usually needs one
file; a subfolder is useful only when it owns more material.

The Flows README gives a shared overview of when and how each flow is triggered,
its eligibility conditions, action and observable result. Keep shared timer
fields here once. Each substantial flow gets a linked explanation with its
diagram and short account of branches, failures and outcomes. Colocate editable
diagram source and the embedded export; use a flow folder when those assets
justify it. Simple flows can remain together in the overview. This is an
example of useful grouping, not a mandatory tree for every repository.

Use roughly ten top-level documentation slots as a review signal, not a hard
limit. A coherent folder counts as one slot: six files and four folders are ten.
More slots need an explanation of their independent subjects. Do not hide an
unexamined collection of fragments behind ever-deeper folders to satisfy a count.

## Build the chapter around its reader's question

Build chapters from these elements:

| Element | What it must explain when relevant |
|---|---|
| **Overview** | The chapter's subject, purpose and reader. |
| **How-built** | Which parts provide the capability and how they relate; use tables and diagrams where clearer. |
| **Why-this-construction** | The reason for the arrangement and the material alternative that was rejected. |
| **Rules** | MUST/MUST-NOT constraints, their enforcing mechanism and the consequence of violation. |
| **Patterns applied** | Meaningful applied patterns and their canonical primary-source references. |
| **Failure modes** | What can go wrong, how it appears and what must not be assumed. |
| **References** | The authoritative places to verify or deepen the explanation. |

Choose elements according to the text's job. A reference page is not forced through an architectural essay;
an architectural explanation must still explain its construction and reasons.

## Explain the model and the why behind the why

The reader has never seen the system. A line-by-line prose copy of the code
neither teaches the model nor remains current. Explain what provides the
capability, why the boundaries exist and what a newcomer must not assume.

An adapter example makes the required depth concrete. "There are
adapters" is not enough. Explain that the system cannot know what a given host
supports, so the binding must be replaceable, and that an established protocol
should be reused where it already provides the needed boundary rather than
inventing a bespoke adapter.

Keep invariants beside the slice that owns them. State the rule as MUST, name
the mechanism that enforces it and describe the failure consequence. Only
system-wide architectural invariants belong in the architecture chapter. Derive
an index if needed; do not maintain a second global list of every local rule.
Tests point to this specification; the chapter need not carry a parallel test list.

Explain behavior with its source, event, condition, triggered action and result.
Do not collapse a timer firing, eligibility being checked, work being dispatched
and work succeeding into one claim that the system “runs automatically”. Keep
ordering, failure conditions and unresolved release status visible. Useful
explanations are never removed merely to make the file shorter; consolidate
repetition and stale corrective prose in place.

Name meaningful applied patterns and keep their primary literature at one
reference owner. Other chapters point there.

## Prefer diagrams for relationships and behavior

Actively assess diagrams when explaining architecture, dependencies, agent
handoffs, data flows, sequences, states or branching behavior. Prefer a diagram
when the reader can follow the verified relationships faster visually; do not
wait for a separate diagram request. A simple list or exact attribute comparison
may still be clearer as Markdown. Not every page needs a graphic.

Load `editorial-svg-diagrams` through the host's catalog with the verified model, reader
and intended output. It owns visual form, editable standalone SVG source, export
and visual checks; do not copy its design manual here. Keep meaningful labels,
conditions and direction. Link large flow diagrams from the relevant explanation
instead of collecting them in a short overview. No Figma or new plugin is required.

When revising documentation, modernize legacy diagrams encountered within the
requested scope using `editorial-svg-diagrams`. Read the existing source before
converting it. Preserve verified components, relationships, direction and
conditions; disclose any necessary consolidation. Keep required repository
notation and automated consumers working. Update the embed and source links,
then retire the superseded asset once the replacement is verified. This does
not authorize a sweep of unrelated documentation or repositories.

Inspect the actual export for legible labels, unclipped content and faithful
relationships. Preserve editable source beside its output, and give embedded
figures meaningful alternative text. If the skill or exporter is unavailable,
state the limit and use available prose, lists or tables without claiming a
diagram was generated or checked. An explicitly required diagram remains open.

## README, configuration and deployment have different jobs

The README answers how to start, test and develop this component quickly, while
showing what it is and why its construction matters. For a substantial system,
use this orientation sequence where the content exists:

1. One-sentence purpose, then what it is, why it exists and its distinctive constraints.
2. A diagram or screenshot when it materially helps orientation.
3. A quickstart that can be followed in minutes with literal, verified commands.
4. What's in the box, relevant sibling repositories and the runtime landscape.
5. A short architecture abstract linking into the book.
6. Deployment notes when owned here, the documentation map, development gates and honest status.

The quickstart is operationally exact. Give the literal command and prerequisites
for each supported environment, including a component-only start if it is a real
supported workflow. Point to configuration and scripts instead of maintaining
another copy of their values. Do not assume a particular runtime or container
setup. Someone trying the system should not have to reverse-engineer its launcher.

Configuration earns a chapter when it has a non-trivial surface. It answers:
"I have something new; how do I wire it in?" Identify each config file and owner,
the minimum needed per supported environment and the recurring extension moves:
register a participant, bind a runtime, set a policy, retention or a budget.

Deployment earns a chapter when production is genuinely more than the quickstart.
It explains the complete deployment model, integration, variants and operational
cautions. A filled-in deployment record, migration log or one-off runbook is
history, not another system chapter. Keep the transferable concept in the book
and the actual operational record at its history owner.

Repository agent instructions provide onboarding: the relevant commands,
maintenance moves, access locations and pitfalls for this repository. They may
specialize process defaults. They do not duplicate the persona, general
Engineering rules or the product's architecture and domain contracts.

## Verify and finish

Check routes, fields, states and named paths against their actual owners before
writing facts. Exercise safe quickstart commands in the supported environment;
state what cannot be verified without missing access or an external effect.
Mark planned behavior as planned. The book describes the system to understand,
while open work belongs in the workboard and active plans.

After a move, check links, map completeness, purpose headers and pattern references
with the repository's appropriate checks or a focused inspection. Do not add a
permanent convention gate just to perform this one revision. A broken evidence
pointer is a reason to recheck the fact, not merely repair the URL.

Resolve discrepancies as incorrect implementation, stale documentation or a
changed target. Repair false statements in the affected work rather than adding
a corrective paragraph for later. Deliver the canonical revised explanation and
the actual verification, with unresolved questions stated plainly.
