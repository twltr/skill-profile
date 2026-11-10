# Source and adaptation

Adapted from the `ux-copy` skill of Anthropic's **design** plugin, version 1.2.0, in
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/ux-copy),
licensed under Apache-2.0 ([LICENSE-Anthropic.txt](LICENSE-Anthropic.txt)). Imported
on 2026-11-10 from the installed plugin copy; source `SKILL.md` SHA-256
`d46a00a62ec637e9ca9d5f7823ea3e0a4ec26dffc53bb5035f59b48ebfcdcde7`.

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

Specific to UX Copy: the description and a new section cover copy in any
language — writing natively instead of translating, reply language versus
interface language, formal or informal address, infinitive button labels,
capitalization, typography and text expansion — after a German UX-copy request
was missed in every trigger run. The redundant error example ("Payment declined.
Your card was declined …") was rewritten, the voice guidance reconciled
("empathetic" errors versus "errors don't apologize"), the patterns condensed
into one table with examples, and the output scaled: alternatives only when the
choice is open, plus a current/proposed table for reviews. The description was
reworded within the length limit.
