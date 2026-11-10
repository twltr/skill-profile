# Source and adaptation

Adapted from the `design-handoff` skill of Anthropic's **design** plugin, version 1.2.0, in
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/design-handoff),
licensed under Apache-2.0 ([LICENSE-Anthropic.txt](LICENSE-Anthropic.txt)). Imported
on 2026-11-10 from the installed plugin copy; source `SKILL.md` SHA-256
`38f1efc807928030654218443ad07f6a37ac82de6b4d627a03113a3568d787b7`.

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

Specific to Design Handoff: behavior the design leaves open is now proposed and
marked for the designer instead of "specify everything" by guessing; the
template uses the project's breakpoints instead of fixed 768/1024 px values and
adds reduced-motion, failure and open-question rows. The "What to include" lists
became one coverage table. The worked excerpt shows states and an edge case with
reasons. Boundaries: the spec records decisions already made; choosing motion,
copy or a new component, and documenting reusable components, are separate
design work. The description gained content limits, accessibility and its
purpose.
