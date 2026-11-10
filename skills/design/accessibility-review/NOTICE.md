# Source and adaptation

Adapted from the `accessibility-review` skill of Anthropic's **design** plugin, version 1.2.0, in
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/accessibility-review),
licensed under Apache-2.0 ([LICENSE-Anthropic.txt](LICENSE-Anthropic.txt)). Imported
on 2026-11-10 from the installed plugin copy; source `SKILL.md` SHA-256
`ef42982af0d51238dda2ab16d08626712891bdd41864876c32d1e7b13fb3124f`.

Changes: the pointer to the plugin's `CONNECTORS.md` is replaced by an inline
explanation of the `~~category` placeholders; `metadata` declares the skill as a
leaf of the Design tree, with a matching first body line; `agents/openai.yaml`
and icons were added.

## 2026-11-10 refinement against Skill Issue

Shared with the other four leaves from the same plugin: the slash-command
scaffolding (`# /name`, a Usage block with `$ARGUMENTS` and `@$1`) became a
titled method, because a skill loaded by a router or read from disk receives no
argument substitution; the user-facing "Tips" addressed to a human reader
became instructions for the agent or were cut; emoji status markers, where used, became
words; the `~~category` note now follows the opening and explains every
category the skill uses. Each leaf opens with the problem it solves and a short
fictional worked example. Boundaries to neighboring design work are stated
without naming other skills. `argument-hint`, `metadata` and the invocation
policy are unchanged.

Specific to Accessibility Review: the plugin listed "2.5.5 Touch target >= 44x44"
as an AA criterion; in WCAG 2.1 it is Level AAA, so smaller targets are now a
usability finding unless WCAG 2.2 applies, where 2.5.8 (24 × 24 CSS px, AA)
does. The criteria table now gives each level and adds frequently failed A/AA
criteria (1.3.5, 1.4.1, 1.4.4, 1.4.10, 1.4.12, 1.4.13, 2.1.2, 2.2.2, 2.4.4,
2.5.3, 3.3.3, 4.1.3), the large-text threshold, and the WCAG 2.2 additions and
removal of 4.1.1. The "~30%" automated-coverage figure was replaced by "only
part", since sources differ. The audit now separates what a mockup can and
cannot verify, reports which test steps ran, uses one findings table instead of
four, and shares its severity scale with the design critique. WCAG 2.1 AA stays
the default standard, consistent with the skill's name and its parent. The
description now mentions criterion citations, zoom and reflow, and WCAG 2.2.

## 2026-11-10: WCAG 2.2 AA default

On the owner's decision the audit now defaults to WCAG 2.2 AA, the current W3C
Recommendation: the 2.2 AA and A additions are part of the criteria table, and
a project that still requires 2.1 AA drops them explicitly. Design Review
changed with it.
