---
name: good-writing
description: "Write or revise correspondence, commercial copy, shared notes, articles, reports and repository documentation. The automatic router for Customer Writing, Commercial Writing, Workspace Writing and Technical Writing. Ordinary replies and quick wording fixes use Unslop directly. Automatic selection enabled; explicit use also supported."
---

# Good Writing

Infer the reader, purpose, language, tone, facts and destination. Ask only about
a gap that changes the meaning or permitted action. Preserve the brief and
protected content when editing; pass them to the selected specialist once.

**Apply `unslop` to every writing task**, including explicit specialist choices.
Load it once through the host's skill catalog and returned path or read interface.
It owns clear language, meaningful formatting and protection against lost detail.

| Intended result | Method |
|---|---|
| Customer or business-partner correspondence | `customer-writing` |
| Offer, sales copy, pitch or commercial decision | `commercial-writing` |
| Shared working notes in OpenAI ChatGPT Pages and Spaces | `workspace-writing` |
| Repository README, system or architecture documentation | `technical-writing` |
| Ordinary reply, quick wording fix or other prose | `unslop` and the reader's brief; no further route required |

An explicit choice wins. Route by the text's job, not its source: a product pitch
based on code is commercial writing. For mixed tasks, select the needed methods
here and apply each only to its relevant part.

Good Writing is the sole automatic router for the four specialists. They disable
implicit invocation and remain usable by explicit user choice or as resources
loaded by this router. Resolve the selected name through the host's installed-skill
lookup and read its complete `SKILL.md` before applying it. In a filesystem runtime,
use the configured skill roots; in a flat installation the file is the sibling
`../<skill-name>/SKILL.md`. Absence from the automatic catalog alone does not mean
uninstalled. Pass the existing brief, apply the method, then return the finished
text to this task. Specialists never route back here or select another specialist.

Use `writing-fragments` only when explicitly requested; it stays outside
automatic routing.

Make the structure easy to see with the destination's supported formatting.
Across all routes, load `editorial-svg-diagrams` when a visual explains relationships
or behavior better. Pass the verified model, audience and output needs; it owns
diagram sources, design, export and visual checks. A short reply needs no diagram.

Check meaning, conditions, uncertainty, links and requested depth against the
source. After specialist work and artifact assembly, apply Unslop's final
wording check to the complete reader-facing result, including titles and headings.
Text added by a renderer or another agent needs the same check. Reading Unslop
at the start does not complete this step. Revise failures before returning the
finished text; keep the language rules with Unslop rather than duplicating them
in each specialist. Artifact skills own native editing and render checks; a
draft does not authorize saving, sending, publishing or reorganization.

If a required skill cannot be read, name it and leave that method's completion
open while continuing independent preparation. Never claim it was applied.
A missing optional diagram may remain a list, table or prose; an explicitly
required diagram or write needs access or an agreed alternative. Do not install
dependencies or invent tool calls.
