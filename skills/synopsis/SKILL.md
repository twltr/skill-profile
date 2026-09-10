---
name: synopsis
description: Write system documentation books, architecture explanations and READMEs with clear reader paths, chapter structure and concrete examples. Use when creating or substantially revising those documents; source comments belong to Golden Comments.
---

# Synopsis

Explain the system so a new developer can understand its construction, reasons
and constraints without reconstructing them from scattered implementation.
This method owns the system book and README. Source comments and local headers
have their own owner in Golden Comments.

Establish the intended reader, question, repository
conventions and actual implementation before choosing the documentation shape.
Preserve a working book structure outside the requested change.

## A book that works forward and as a reference

A maintained multi-part system needs a stable, numbered book under docs/.
Its map, normally docs/00-README.md, routes every maintained chapter and provides
useful reader paths, such as operator, developer and agent. Go from the whole
picture to detail: orientation, prerequisites and vocabulary, relationships,
then the individual capabilities and mechanisms.

Numbering expresses that didactic order. It is not a requirement to read every
previous chapter for each task. Support both the person learning the system
from the beginning and the person looking up one concrete question.
A small repository can be fully explained by a short README; do not invent an
empty book or ignore an explicit project exception.

Give each chapter a short purpose header: what question it answers and for whom.
Use the Diátaxis distinction between tutorial, how-to, explanation and reference.
Do not mix four different reading jobs into a chapter just because they mention
the same tool. Keep the existing source of truth for each fact.

## Cut by the system's independently understandable parts

Draw the system and name its boxes. A box with its own purpose, failure modes,
configuration surface and cautions can earn a chapter. Something that cannot be
understood apart from its neighbor belongs inside that neighbor's explanation.
Ask: can a reader name what this chapter owns, and can it be understood alone?

A document owns a whole capability, module, mechanism or contract. It does not
exist for one option or one small behavior. Examples of that boundary:

- Nine pages about nine tools are usually one page about the tool surface.
- Five pages about five caches are usually one page about how the system caches.
- A pipeline whose stages genuinely need separate explanations can have a folder
  with a README for shared relationships and one chapter per stage.
- Three agent roles whose work differs can use the same arrangement: one shared
  introduction, then the role-specific explanations.

Use roughly ten top-level documentation slots as a review signal, not a hard
limit. A coherent folder counts as one slot: six files and four folders are ten.
More slots need an explanation of their independent subjects. Do not hide an
unexamined collection of fragments behind ever-deeper folders to satisfy a count.

## Build the chapter around its reader's question

Build chapters from these elements:

| Element | What it must explain when relevant |
|---|---|
| **Synopsis** | The chapter's subject, purpose and reader. |
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

Name meaningful applied patterns and keep their primary literature at one
reference owner. Other chapters point there. Diagrams, preferably Mermaid or
an equivalent maintained format, should explain relationships rather than decorate
an already clear sentence. Useful explanations are never removed merely to make
the file shorter; repetition and stale corrective prose are consolidated in place.

## README, configuration and deployment have different jobs

The README answers how to start, test and develop this component quickly, while
showing what it is and why its construction matters. For a substantial system,
use this orientation sequence where the content exists:

1. One-sentence purpose, then what it is, why it exists and its distinctive constraints.
2. An early architecture diagram or screenshot that orients the reader.
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
