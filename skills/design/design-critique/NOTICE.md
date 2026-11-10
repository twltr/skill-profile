# Source and adaptation

Adapted from the `design-critique` skill of Anthropic's **design** plugin, version 1.2.0, in
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/design-critique),
licensed under Apache-2.0 ([LICENSE-Anthropic.txt](LICENSE-Anthropic.txt)). Imported
on 2026-11-10 from the installed plugin copy; source `SKILL.md` SHA-256
`3a4f260eb9f60b431782bf6d90f22afb480c0c67860267a032df58a3e1bd19cd`.

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

Specific to Design Critique: severity now uses the same Critical / Major /
Minor scale as the accessibility audit, with definitions, so the two can be
merged into one list; the plugin used Critical / Moderate / Minor here and
Critical / Major / Minor there. The accessibility lens is limited to problems
noticed in passing — contrast ratios and touch-target sizes belong to the WCAG
audit — and the critique no longer implies compliance. The worked finding shows
location, observation, consequence, severity and the smallest change. The
undeclared `~~user feedback` category is now explained. The description was
reworded to name live screens and design file links.
