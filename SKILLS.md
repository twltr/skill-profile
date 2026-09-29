# Skill Inventory

This inventory distinguishes repository-owned sources, reviewed external
snapshots and external catalog entries. A link is evidence of provenance, not a
claim that the latest upstream revision is installed locally.

## Included Engineering skills

These skills are maintained as part of this repository. Their primary source is
Tobi's former global Engineering instructions and the revision decisions in the
joined `engineering-skills` Git history. Individual `NOTICE.md` files preserve
supplementary Matt Pocock attribution where applicable.

| Skill | Purpose |
|---|---|
| [`all-or-nothing`](skills/engineering/all-or-nothing/SKILL.md) | Complete an agreed replacement and retire the superseded owner. |
| [`golden-comments`](skills/engineering/golden-comments/SKILL.md) | Explain reasons, invariants and failure consequences in source commentary. |
| [`marshmallow-tests`](skills/engineering/marshmallow-tests/SKILL.md) | Design tests around coherent units, invariants and precise failure addresses. |
| [`minmax-codebase`](skills/engineering/minmax-codebase/SKILL.md) | Human-initiated structural and architectural improvement; preserves agreed capability. |
| [`road-to-glory`](skills/engineering/road-to-glory/SKILL.md) | Maintain resumable Engineering work through roadmaps, active plans and changelogs. |
| [`synopsis`](skills/engineering/synopsis/SKILL.md) | Create system books, architecture explanations and substantial READMEs. |
| [`vertical-slices`](skills/engineering/vertical-slices/SKILL.md) | Organize repository capabilities around clear owners and public boundaries. |

## Included General skills

| Skill | Status and provenance |
|---|---|
| [`skill-issue`](skills/general/skill-issue/SKILL.md) | Repository-owned general skill. It is an independently rewritten adaptation informed by Matt Pocock's `writing-for-agents` and OpenAI's Skill Creator; both source licenses are preserved in the skill directory. |
| [`frontend-design`](skills/general/frontend-design/SKILL.md) | Reviewed snapshot of [Anthropic's `frontend-design`](https://github.com/anthropics/skills/tree/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design) at commit `2235be7c60b551f5de82ade908fd3816455afcda`. The bundled Apache-2.0 license is preserved. |
| [`motion-design`](skills/general/motion-design/SKILL.md) | Reviewed snapshot of [LottieFiles `motion-design-skill`](https://github.com/LottieFiles/motion-design-skill/tree/b6606e101601ef027f01729a7289e97c329ad0cd/skills/motion-design) at commit `b6606e101601ef027f01729a7289e97c329ad0cd`. MIT license preserved. |
| [`gsap`](skills/general/gsap/SKILL.md) | Repository-owned router around eight byte-preserved entrypoints from [GreenSock's official `gsap-skills`](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760/skills) at commit `aed9cfd3277740755f6bfc1155c7aa645403b760`. The manifest records each source hash; MIT license preserved. This is a standalone skill, not a plugin-managed installation. |
| [`workspace-management`](skills/general/workspace-management/SKILL.md) | Repository-owned workflow for provider-neutral, host-local Workspace context and AI-project bindings. |
| [`minmax-tokens`](skills/general/minmax-tokens/SKILL.md) | Repository-owned method for reducing unnecessary context and tool output without weakening verification. |
| [`puppeteer`](skills/general/puppeteer/SKILL.md) | Repository-owned delegation method for bounded tasks, shared-resource ownership and verified integration. |

## Catalog-only external skills

These skills are intentionally not copied into this repository. Pull them from
[Matt Pocock's `skills` repository](https://github.com/mattpocock/skills) when
needed. The reviewed public baseline is commit
`3cca18b368ae95cdbdebbff572ccafa662551015`.

| Skill | What it does | Upstream path |
|---|---|---|
| `grill-me` | Relentlessly interviews the user to sharpen a plan or design. | [`skills/productivity/grill-me`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grill-me) |
| `grill-with-docs` | Runs the same design interrogation while producing ADRs and a glossary. | [`skills/engineering/grill-with-docs`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs) |
| `grilling` | Stress-tests a plan, decision or idea through a decision-tree interview. | [`skills/productivity/grilling`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling) |

The local Matt checkout previously used for host distribution contains two
additional invocation-policy commits on top of that public baseline. Pulling
the upstream paths gives the public versions, not those local policy changes.

## Intentionally outside this repository

- `svg-design` and the remaining Matt Pocock workflows are omitted by choice.
- Codex system skills and skills supplied by plugins remain host-managed.
- `hatch-pet` remains a Codex-local specialist skill.
- `inkscape-mcp` is a plain MCP reference without valid skill metadata and is
  not treated as a distributable skill.
