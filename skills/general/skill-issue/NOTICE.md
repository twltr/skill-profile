# Sources and adaptation

Skill Issue is a maintained local authoring method. The 2026-11-04 revision
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
