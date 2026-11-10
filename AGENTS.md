# Maintaining the Skill Profile

This repository is the canonical source for Tobi's curated agent skills. Read
README.md, SKILLS.md and the complete skill being changed before editing it.
Create or revise skills with Skill Issue (`skills/core/skill-issue/`), including
its architecture reference for types, edges and dependency declarations.

Ownership is explicit:

- Each skill directory owns its complete package: instructions, metadata,
  references, scripts, assets, licenses and notices.
- skills/core/ owns the core skills: implicit, first-level, cross-domain.
  skills/writing/, skills/software-engineering/ and skills/design/ own one tree
  each, where only the domain's routing skill is implicit. skills/extras/ owns
  shared leaves: explicit-only skills several domains can use, outside every
  tree, which routing skills may suggest but never load. A skill's folder must match its
  type and invocation policy.
- SKILLS.md owns the inventory, each skill's type, provenance and catalog-only
  references. README.md owns the architecture explanation and its rationale.
- figures/ owns the editable maps of the collection.
- Installation and client configuration belong to the consuming profile or
  installer, not to this repository. Source edits do not install anything.

Keep the collection a tree. Declare every skill's type in `metadata`
(`skill-type`, `skill-tree`, `skill-requires`), in the first body line and at the
start of its short description. Routing skills name their children; children never
name their callers; no edge crosses into another tree. Run
`python3 -B skills/core/skill-issue/scripts/check_tree.py skills` after changing
types or references: it must report no ERROR, and explain any new rule finding.
`skill_graph.py` shows the underlying edges. Measure a domain's
trigger behavior before making its children explicit-only.

Write skill instructions, metadata descriptions and authored examples in English.
Keep personal data out of this repository: no local paths, hostnames, account
names, customer details or private machine setup. Those belong in the private
agent profile. Preserve original licenses and provenance records. Every skill
package carries a license file: an adapted skill keeps its upstream license and
names its changes in `NOTICE.md`; original work carries the repository's MIT
`LICENSE`. Do not license a package whose origin is unrecorded.

Before replacing, changing or removing a skill package, archive its complete
previous bytes inside this repository and commit the recovery point before the
exchange. Use a uniquely named ZIP plus manifest under archive/; never overwrite
an archive entry, and keep executable instruction filenames inside archives
rather than as loose nested SKILL.md files that loaders could discover. Git
history alone does not satisfy this rule.

Each skill keeps editable SVG icon originals in `assets/` and transparent PNG
exports referenced by `agents/openai.yaml`: `icon-small.png` at 128 px and
`icon.png` at 256 px. Some skill renderers treat custom SVGs as monochrome
masks, so both slots need PNGs. After editing an SVG, regenerate its PNG, for
example `inkscape assets/icon.svg --export-filename=assets/icon.png --export-width=256 --export-background-opacity=0`,
and check small renders on light and dark surfaces. The writing family shares one
pencil; other marks use restrained colors with a fine neutral edge.

Review upstream changes before refreshing a vendored snapshot. Do not create a
docs book or build system; README.md and SKILLS.md are the documentation. Keep
one-off inspection in .tmp/, review the complete diff and run `git diff --check`
before committing.
