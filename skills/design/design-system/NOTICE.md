# Source and adaptation

Adapted from the `design-system` skill of Anthropic's **design** plugin, version 1.2.0, in
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/design-system),
licensed under Apache-2.0 ([LICENSE-Anthropic.txt](LICENSE-Anthropic.txt)). Imported
on 2026-11-10 from the installed plugin copy; source `SKILL.md` SHA-256
`fb31bd0144c43955106f01927126ae9fd2d4148be44c8d5887b3391f40c31445`.

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

Specific to Design System: the audit no longer reports a "Score: [X/100]" or
"8/10" completeness without criteria; it reports counts and evidence. The worked
example separates hardcoded values that duplicate a token (mechanical fix) from
values that match none (a design decision). Added: reading the actual token and
component source first, a search pattern for hardcoded values, the Design
Tokens Community Group format 2025.10 (stable since 2025-10-28) as the
interchange format, migration paths for breaking renames, and publishing to a
knowledge base only on request. The three templates were trimmed. The
description gained "tokens" and "instead of duplicating one".
