# Sources and adaptation

Skill Issue is a maintained local authoring method.

## Anthropic Skill Creator (2026-11-10 revision)

The 2026-11-10 revision rebases the method on Anthropic's `skill-creator`, as
installed through the claude.ai account skill sync on 2026-11-10 (`SKILL.md`
SHA-256 `1d51c0b077c24489baa7fdb6c7072ff0c94479dab7110dad2fc6039a47a4bed4`).
Licensed under Apache-2.0; the license is retained as
[LICENSE-Anthropic.txt](LICENSE-Anthropic.txt).

Adapted, partly close to the original wording: the create–test–review–improve
loop, progressive disclosure, the principle of lack of surprise, the anatomy and
domain-organization trees, the 500-line guidance, how skill triggering works and
the advice to write slightly pushy descriptions, the writing-style passage on
explaining the why instead of capitalized MUSTs, the four improvement principles,
the `evals/` case layout read by `claude plugin eval`, and the trigger-eval query
guidance with its good and bad examples.

Deliberately not adopted: the browser eval viewer, benchmark aggregation scripts,
grader/analyzer/comparator agent files, `.skill` packaging and the host-specific
Claude.ai and Cowork sections. Results are reviewed with the user in the
conversation; the upstream tooling is referenced as an optional route when it is
installed. Added locally: named principles "One owner per fact" and "Trees, not
meshes", router guidance for sibling skills, composition rules,
`scripts/skill_graph.py`, multi-host invocation metadata and the review format.

## 2026-11-04 revision

The 2026-11-04 revision
combines its existing ownership, authorization and workflow rules with early
worked examples, explicit placement criteria for supporting files, and a separate
installation reference.

## OpenAI source

Reviewed the public `openai/skills` repository at commit
`49f948faa9258a0c61caceaf225e179651397431` on 2026-11-04:

- [Skill Creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md), blob `72bc0b97e7a6476254a9d5c424c9971748402ec3`.
- [Native metadata reference](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/references/openai_yaml.md), blob `da5629f8de500ec6f81291d239a2d9c68d1d9044`.
- [Skill Installer](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-installer/SKILL.md), blob `8ca23bf833379d2272a0a67e0026c2709b8823f1`.

Adapted principles include concrete usage examples, specificity appropriate to
risk, progressive loading of optional material, distinctions between scripts,
references and assets, and iteration after real use. The retained OpenAI license
is [LICENSE-OpenAI.txt](LICENSE-OpenAI.txt).

This revision is a selective rewrite, not a copied creator or installer. Short
normal-path examples stay in the main skill. Installation is conditional guidance;
no upstream scripts are bundled or assumed available. Native invocation policy
remains separate from descriptions. Existing supported metadata and authoring
rules are reconciled rather than replaced by an upstream template.

## Existing attribution

The repository inventory records prior influence from Matt Pocock's
`writing-for-agents` and OpenAI Skill Creator. The existing
[LICENSE.txt](LICENSE.txt) and OpenAI license remain unchanged. This revision does
not claim a newly verified Matt Pocock source snapshot.

## 2026-11-10 quality pass

The `agents/openai.yaml` example in `references/installation.md` now starts its
short description with the skill's type, as `SKILL.md` requires; the example
skill is explicit-only, so it is a leaf.
