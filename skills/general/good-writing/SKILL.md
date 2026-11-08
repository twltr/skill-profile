---
name: good-writing
description: "Write or revise correspondence, commercial copy, shared notes, articles, reports, technical manuals and repository documentation. Select the writing method for the reader and purpose. Ordinary replies and quick wording fixes use Unslop directly."
---

# Good Writing

Match preparation to the writing job. An ordinary conversational reply or local
wording fix uses Unslop directly with the brief and supplied text; fact-finding remains with the
actual task. Check the finished wording and preserved meaning without starting
a source-scouting or specialist workflow merely because the result contains prose.
For example, correcting a typo in a supplied sentence needs no fragment handoff.

For a document, correspondence or other writing artifact, infer the reader,
purpose, language, tone, facts and destination. Select useful evidence through
Writing Fragments, then route to the method that
owns the intended result. A rewrite that changes claims or purpose, or combines
sources, needs this preparation even when the final text is short. Preserve the
brief and protected content; pass them and the source handoff to the specialist
once. An explicit specialist choice wins. Ask the user only about a gap that
changes the meaning or permitted action.

An engineering change can include writing even when the user only asks to implement
a feature. Source commentary is handled in that implementation by Golden Comments,
when available. Engineering Practices or another active engineering workflow may
load Engineering Documentation directly for affected architecture, pattern sources,
contracts or operating instructions, using its existing evidence. It need not come
through this router first. This preserves a short route without making each writing
specialist an independent automatic entrypoint.

## Prepare the material first

If `writing-fragments` is available, deliberately load it from the host's
installed-skill lookup and read its complete method; its native policy is
explicit-only. This preparation applies to the routed writing work above,
scaled to the material. A source-heavy report may need bounded scouting and a
fuller handoff. If the brief is the only source, draft from the brief and state
any consequential evidence gap;
do not invent research or citations. The handoff preserves source locators,
qualifiers, uncertainty and any figure suggestion for the selected writer.
Writing Fragments returns to this workflow; it does not select a writer or call
Good Writing again.

If that supporting skill cannot be read, perform the bounded source selection
locally: retain purpose-relevant claims with their locators, context, qualifiers,
counterevidence and material gaps, then choose a useful prose or figure handoff.
State that Writing Fragments itself was unavailable; do not skip preparation or
invent sources. Reuse a current handoff already supplied by the task instead of
scouting the same material again.

**Example:** The user wants a customer told that a migration is ready but asks
for a maintenance window before scheduling. Route the message to Customer Writing;
its draft asks for the window and says the date will be confirmed before scheduling.
Run the finished draft through Unslop. Keep it a draft unless sending was requested.
This illustrates a route and result; use the supplied facts in real messages.

**Apply `unslop` to every writing task**, including explicit specialist choices,
when the skill is available. Load it once through the host's skill catalog and
returned path or read interface. It owns clear language, meaningful formatting
and protection against lost detail. If unavailable, preserve those requirements
in your own final check and report that Unslop was not applied.

| Intended result | Method |
|---|---|
| Customer or business-partner correspondence | `customer-writing` |
| Offer, sales copy, pitch or commercial decision | `commercial-writing` |
| Shared working notes in OpenAI ChatGPT Pages and Spaces | `workspace-writing` |
| Repository README, agent instructions, architecture or SDK docs maintained with code | `engineering-documentation` |
| Technical manual, product guide or reference maintained from specifications or other non-repository sources | `technical-writing` |
| Ordinary reply, quick wording fix or other prose | `unslop` and the reader's brief; no further route required |

Choose between the two technical routes by the document's owner and task. An SDK's
code-owned documentation uses Engineering Documentation even for external readers;
a vendor API manual based on published specifications uses Technical Writing.
Missing code access remains an unresolved verification, not a reason to pretend
repository documentation was checked through the other route.

For repository docs, keep durable product and system knowledge in its canonical
documentation owner. Put temporary progress, task status, agent diaries and
"since the last update" notes in the active plan, roadmap item, issue, PR or
changelog that owns that work. If a status note reveals a lasting behavior or
constraint, rewrite that fact in the appropriate documentation instead of
copying the transient update into the README.

An explicit choice wins. Route by the text's job, not its source: a product pitch
based on code is commercial writing. For mixed tasks, select the needed methods
here and apply each only to its relevant part.

Good Writing is the default automatic router for writing work across the five
specialists. They disable implicit invocation and remain usable by explicit user
choice, this router, or a scoped deliberate call from another authorized workflow.
Technical Writing is directly callable for manuals; Engineering Documentation is
directly callable for code-owned docs. Automatic selection and deliberate workflow
composition are different routes. Resolve the selected name through the host's installed-skill
lookup and read its complete `SKILL.md` before applying it. In a filesystem runtime,
use the configured skill roots; in a flat installation the file is the sibling
`../<skill-name>/SKILL.md`. Absence from the automatic catalog alone does not mean
uninstalled. Pass the existing brief, apply the method, then return the finished
text to this task. Specialists never route back here. A directly invoked method
that discovers a scope mismatch may hand off once to the correct sibling; the
receiving method completes the task without routing again. A specialist selected
by this router returns a scope mismatch to the active caller instead of choosing
another writer.

Writing Fragments is a deliberate preparation dependency before the specialist
route, not another automatic router. Its explicit-only policy remains in native
metadata; this workflow deliberately loads it when writing is routed through Good
Writing.

Make the structure easy to see with the destination's supported formatting.
Across all routes, use `editorial-svg-diagrams` when available and a visual
explains relationships or behavior better. Pass the verified model, audience and
output needs; it owns diagram sources, design, export and visual checks. A short
reply needs no diagram. If it is unavailable, use a clear list, table or prose and
report the limit if a diagram was requested.

Check meaning, conditions, uncertainty, links and requested depth against the
source. After specialist work and artifact assembly, apply Unslop's final
wording check to the complete reader-facing result, including titles and headings,
when available. If it cannot be read, run its preservation and clarity checks yourself.
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
