---
name: writing-fragments
description: "Scout source material and select relevant, well-supported content for a writing task, preserving citations, context and uncertainty in a concise handoff."
---

# Writing Fragments

Writing needs a useful selection of evidence before it needs polished sentences.
This skill scouts the material already in scope, keeps the claims that serve the
reader and purpose, and hands a compact, traceable brief to the writing method.
That prevents a draft from confusing a persuasive line with a supported claim,
or from carrying a whole source pile into the reader's text.

This is preparation, not a user interview, a raw-fragment diary or a draft.
Do not make the user co-author the selection or ask where to save it. Return the
handoff to the active writing task; create a separate file only when requested.
Do not call Good Writing or restart the routing chain. The caller owns what
happens after the handoff.

## A small source selection

**Fictional brief:** Write a decision brief in the active rollout plan on whether to expand
a staged service rollout beyond 20 accounts after a reliability review.

**Fictional source set:** `release-log.md#2026-05-03` says the rollout is capped
at 20 accounts. `monitoring.md#2026-05-07` reports 18 of 20 accounts completed
onboarding and says monitoring covers only this cohort. `operations-note.md#2026-05-08`
schedules a reliability review and records that no expansion decision has been made.

A useful selection might be:

- The rollout is capped at 20 accounts (`release-log.md#2026-05-03`).
- On May 7, 18 of those accounts had completed onboarding; two had not
  (`monitoring.md#2026-05-07`). This describes onboarding, not service reliability.
- The available monitoring covers only this capped cohort, so it cannot establish
  performance at larger volume (`monitoring.md#2026-05-07`).
- The May 8 note schedules a reliability review and records no expansion decision
  (`operations-note.md#2026-05-08`). Do not imply approval.

**Figure suggestion:** A small sequence—20-account cap → reliability review →
expansion decision—could clarify the decision gate in a longer report. A short
note can state it in one sentence, so no figure is needed there.

**Handoff:** The selected writer can draft the decision brief in the active plan
using the cited status and limitation, while treating the review gate as the
brief's intent. This temporary rollout status does not belong in a maintained
README. The next writer receives both what the sources support and what they
do not establish.

## Scout and select

1. **Set the purpose and source boundary.** Identify the intended reader, desired
   outcome, destination and material supplied or made available for this task.
   Inspect only authorized, relevant sources. Do not assume a linked, private or
   external source is accessible. Follow the active workflow's handling rules
   for customer, business, personnel and other sensitive material; keep the
   handoff within those boundaries and include only what the next writer needs.
2. **Read for evidence that changes the text.** Select claims, examples, wording,
   decisions or counterevidence that materially serve the purpose. For each
   candidate, record the exact source and a useful locator: file and heading or
   lines, page or section, URL and publication detail, or repository path and
   revision when relevant. Keep the surrounding conditions, date, population,
   scope and qualifications needed to interpret it.
   Prioritize relevance to the reader's task, consequences of omitting the point,
   strength of evidence, explanatory value and information not already covered.
   A vivid quotation is not automatically more useful than a precise limitation;
   remove duplication without selecting away meaningful counterevidence.
3. **Separate evidence types.** Mark whether a point is supported by a source,
   supplied only in the brief, an inference, contradicted, or still unresolved.
   Keep meaningful counterevidence and disagreement visible. Do not turn a
   plausible explanation, absence of evidence or requested outcome into a fact.
4. **Name real gaps.** If the brief and available material do not support a
   necessary claim, say which claim is unsupported and what source or decision
   would resolve it. If the user supplied no source material, prepare from the
   brief alone and identify only consequential evidence gaps. Do not invent
   sources or add research steps when the brief is sufficient.
5. **Choose prose or a figure.** Prefer prose for a point that fits plainly in a
   sentence. Suggest an explanatory visual only when relationships, sequence,
   comparisons or quantities become easier to understand as a figure. State the
   idea a figure would show and whether the destination benefits from it; do not
   draw it here. If a figure is useful, the caller can route it to Editorial SVG
   Diagrams.
6. **Return a compact handoff.** Include the purpose and likely writing method;
   the selected points with source locators and necessary qualifiers; important
   gaps or counterevidence; and a figure suggestion or a brief reason prose is
   enough. Keep enough context for the next writer to verify the selection, not a
   source-by-source diary.

Scale this work to the material. For a typo, short revision or tiny supplied
text, select locally from that text and the instruction; do not search for
unneeded sources or write a research report. For a large codebase, book,
research corpus or document set, scout only the relevant sections. If a current,
consequential research question needs fresh evidence, use the task's authorized
research method and distinguish it from supplied material.

For substantial corpora where independent scouting saves time, use Puppeteer if
available and the host permits composition. Read its complete method, then define
read-only scouts with bounded source sets and a shared return format. Keep simple,
dependent reading direct. Check returned references and claims before using them.
For a consequential customer document, repository document or other substantial
text, Grilling with Agents may challenge coverage, claims and organization with
the lead when available and useful. Resolve and read its complete method before
using it. It returns internal findings, not questions for the user; the lead
resolves the handoff. These methods are conditional aids, not a required tour.

## Handoff shape

```text
Purpose / reader / destination:
Likely writing method:
Selected material:
- [supported | brief-only | inference | disputed] Point — source locator; scope or qualifier.
Gaps / counterevidence:
Figure:
```

Use only fields that help the next writer. If there is no material beyond the
brief, say so directly. A good handoff is short enough to use and precise enough
to prevent unsupported claims.
