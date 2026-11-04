---
name: technical-writing
description: "Write technical manuals, product guides, procedures and reference material from verified specifications and source documents. Organize learning, tasks, explanations and lookup for the reader. Repository READMEs, agent instructions and documentation maintained with code belong to Engineering Documentation."
---

# Technical Writing

Help the reader understand a technical subject or complete a task without
guessing prerequisites, sequence or meaning. A manual may describe a device,
service, protocol or product without access to its implementation. Establish
what the sources support; do not invent internals to make the story complete.

Use figures as the primary explanation for relationships and behavior when they
make the answer visible. Remove the paragraphs they replace. Keep exact procedures,
parameters and consequential qualifications as text. Concision removes repetition,
not conditions or useful detail.

## A small worked example

Fictional source: a device stores its calibration only after the operator chooses
Save. Disconnecting earlier discards the pending calibration.

The source contains a paragraph about every screen. The reader needs a procedure:

```text
Before you start: keep the device connected until the save confirmation appears.
1. Open Calibration and complete the measurement.
2. Choose Save.
3. Wait for “Calibration saved” before disconnecting.
If confirmation is missing, the new calibration is not established as saved.
```

A state figure can explain **pending → saved** and the **discarded** branch more
clearly than the longer screen narrative. The action labels and success condition
remain textual so a reader can perform and verify the task. These labels and
guarantees are fictional; use the actual product's labels and contract.

## 1. Establish scope and evidence

Identify the reader, intended outcome, product/version/platform, source owner and
publishing destination. Reuse a supplied brief and source-selection handoff. If
missing, use Writing Fragments when available to select the relevant claims,
source locators, qualifiers and gaps; otherwise do that bounded preparation
directly. A direct request needs no return to Good Writing.

Choose this method when the document's authoritative inputs are specifications,
verified product behavior or supplied technical material. If the requested result
is maintained with a software repository—its README, agent instructions,
architecture or SDK contracts—use Engineering Documentation when available.
A vendor API manual can belong here; an SDK's code-owned reference belongs there.
Missing repository access is a blocked source check, not permission to pretend
its implementation was inspected. Do not re-enter an already active caller.

Verify current product/version claims with their actual owner. Mark unsupported
or planned behavior explicitly. For a consequential unresolved engineering fact,
use State of the Art if available and return its scoped evidence here; do not
turn every writing task into broad research or silently redesign the product.

## 2. Organize by the reader's job

| Job | Useful structure |
|---|---|
| Learn through a first successful experience | A tutorial with a supported starting point, small steps and visible results. |
| Complete a known task | A how-to with prerequisites, ordered actions, expected outcomes and relevant recovery. |
| Understand a model or reason | An explanation built around the concept, relationships, causes and limits. |
| Look up an exact fact | A reference with consistent names, units, defaults, constraints, errors and version scope. |

Use these Diátaxis distinctions to separate different jobs, not as four compulsory
folders. Preserve a working manual's structure. A substantial manual can use
numbered chapters and shallow topic folders, with a map and direct task/reference
links. Keep one small guide together; do not produce empty chapters to look complete.
Use one term per concept and one owner for shared prerequisites or definitions.

## 3. Make procedures and references exact

State required access, equipment, environment and initial state before the action
that depends on them. Use actual labels and literal examples. Separate a performed
action from evidence of its result. Include only relevant failure/recovery paths;
do not promise recovery the product does not support.

For API or configuration reference, distinguish required from optional values,
units, accepted ranges, defaults, compatibility and errors. A concise table may
be clearer than a page per field. Keep examples minimal but sufficient; label
illustrative examples and placeholders, and never fill gaps with invented APIs.

Do not require repository chapters, AGENTS.md, build instructions or deployment
steps when the reader's task has none. Conversely, a software command is not
verified merely because it resembles a familiar tool's syntax.

## 4. Let figures replace the explanation they carry

For a model, process, state change or relationship, consider the visual form before
drafting paragraphs. Use Editorial SVG Diagrams when available with the verified
model, reader's question and destination. Let it own drawing, editable source,
exports and visual checks. Use a state diagram for state changes, a sequence for
interactions, or another form that makes the point visible. Exact lookup may need
a table instead. Do not put explanatory paragraphs inside graphic boxes.

Remove prose that merely walks through the finished figure. Retain necessary
preconditions, reasons, exceptions and consequences. Supply short identification
and a complete concise textual equivalent of essential information, adjacent or
directly linked. Use a structured list or table where appropriate, not a duplicate
essay. Keep literal commands, identifiers and source citations searchable outside
the image; do not rely on SVG metadata alone.

If Editorial SVG is unavailable, use a faithful available representation and
report the missing method; a required figure remains open. Preserve verified
meaning and supported output formats when revising an existing figure.

## 5. Verify the finished manual

Use Unslop when available on the assembled text, including headings, captions and
text equivalents. Remove filler and repeated explanations without deleting facts,
conditions or uncertainty. Without it, perform that clarity check directly.
There is no fixed pass count or word-reduction target.

Walk through a representative reader task against the stated version and actual
sources. Execute safe examples when tools and access permit; record what was
inspected, executed or still unverified. A documentation request does not authorize
external effects such as sending, deploying or operating dangerous equipment.
Inspect the intended rendering, diagram legibility, links, navigation and text
alternatives. Where a material contract remains unclear, state the exact source gap.

Revise the canonical explanation in place. Keep publication history, temporary
progress and open work with their existing record owner rather than appending
dated commentary to the manual. Return to the calling workflow without starting
another router, council or implementation task.

Read [NOTICE.md](NOTICE.md) only when maintaining this method or checking its lineage.
