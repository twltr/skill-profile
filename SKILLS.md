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
| [`technical-writing`](skills/engineering/technical-writing/SKILL.md) | Explain repositories with purposeful Markdown, shallow topic groups and diagrams of relationships and behavior; callable through Good Writing or directly. |
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
| [`good-writing`](skills/general/good-writing/SKILL.md) | Adapted from the user-supplied 2026-09-23 export. Short common entry selecting the relevant writing specialist. |
| [`commercial-writing`](skills/general/commercial-writing/SKILL.md) | Adapted from the same export. Evidence-grounded offers, sales arguments and commercial decisions. |
| [`customer-writing`](skills/general/customer-writing/SKILL.md) | Repository-owned method for external correspondence with customers and business partners. |
| [`workspace-writing`](skills/general/workspace-writing/SKILL.md) | Repository-owned method for shared working knowledge in OpenAI ChatGPT Pages and Spaces, organized by related topics and maintained in place. |
| [`writing-fragments`](skills/general/writing-fragments/SKILL.md) | Same export, adapting [Matt Pocock's Writing Fragments](https://github.com/mattpocock/skills/blob/main/skills/in-progress/writing-fragments/SKILL.md). Included MIT license and attribution preserved; implicit invocation disabled. |
| [`unslop`](skills/general/unslop/SKILL.md) | Maintained adaptation of Pstack Unslop, Humanizer and Writing Clearly and Concisely. [Provenance](skills/general/unslop/NOTICE.md), pinned hashes and all three MIT licenses are preserved. Shared language rules for German and English; implicit invocation enabled. |
| [`editorial-svg-diagrams`](skills/general/editorial-svg-diagrams/SKILL.md) | Reviewed adaptation of the user-supplied 2026-10-23 `skill.zip`, with the three accepted test figures. Owns visual-first transparent SVGs, explicit theme variants, exports and visual review. [Provenance and review changes](skills/general/editorial-svg-diagrams/NOTICE.md); [current import hashes](skills/general/editorial-svg-diagrams/source-manifest-20261023.json). Implicit invocation enabled. |

### Writing sources and composition

Good Writing, Commercial Director and Writing Fragments originated in the
user-supplied `writing-skills.zip` export, imported on 2026-09-23. Archive
SHA-256: `71bb4a17c423b91a779c1a7d060f23844d16508d3d98674be2e607cf19b74965`.
The [export manifest](skills/general/writing-skills-export.json) identifies the
original 15 files, not the current adapted trees. Writing Fragments keeps its
original method, MIT license and attribution; its description and UI label now
state the existing explicit-only invocation policy.

The 2026-10-09 revision replaces Good Writing's mandatory pipeline and reserved
director registry with a short router and four independent specialists.
`technical-writing` replaces Synopsis; `commercial-writing` replaces Writing
Commercial Director. Customer Writing and Workspace Writing own the former
business and Spaces references. The former names and references are retired
from the maintained source; historical export records keep their original names.

Good Writing is the sole automatic router for the four writing specialists.
Commercial, Customer, Workspace and Technical Writing disable implicit
invocation; they are loaded by the router or explicitly selected by the user.
Good Writing and every specialist require Unslop even when used directly, and
can call Editorial SVG Diagrams. Unslop and Editorial SVG Diagrams remain automatic.
Their descriptions and UI labels state the configured invocation mode; Writing
Fragments remains explicit-only. These labels document policy, not proof of an
actual model invocation. Golden Comments points documentation work to the
Technical Writing route in Good Writing.
Workspace Writing emphasizes hierarchical topic grouping. Technical Writing
keeps a shallow structure with substantial topic folders, favors visual
explanations, and updates legacy diagrams within an authorized revision.
Its documentation depth and shared fact ownership remain intact. The commercial
method retains evidence and decision rules. Duplicated language rules and
percentage-cut targets are retired. Unslop's
[notice](skills/general/unslop/NOTICE.md) owns the exact upstream revisions,
adaptation decisions and licenses. Humanizer and Writing Clearly and Concisely
are source material, not additional installed entry points.

The 2026-10-26 writing revision makes Unslop's prohibition on slogan-like
parallel phrasing explicit for paired and longer constructions, including
headings. Good Writing invokes its final wording check after the finished
artifact is assembled. Language rules remain owned by Unslop; routing and
invocation metadata are unchanged.

On 2026-10-21, `editorial-svg-diagrams` replaced the external `diagram-design`
snapshot. The previous skill and its native overlay are retired; writing routes
now use the included replacement. Its source SVGs stay editable, while PNG and
PDF are verified exports. The imported archive and replaced local trees are
preserved outside active skill roots for recovery.

The writing skills preserve supported Cloud-normalized metadata and supplied icons.
Their product list excludes `api`, which causes Codex CLI 0.159.0 and the Desktop
loader 0.162.0-alpha.2 to discard the whole metadata file and lose its invocation
policy. Verify both export parity and
native metadata loading after distribution. ChatGPT adds `api` back on export;
that host-generated product-list difference is the sole allowed exception to
local/Cloud equality. It does not change the matched invocation policies or method
content and must not be copied back into the Codex deployment.
The Pages plugin likewise remains host-managed. Each target host must expose
its own skill catalog and actual tools. A missing dependency is reported; no
skill is described as applied before its instructions have been read.

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
The reviewed local revision is `07121a1`, which already restricts Research and
Prototype to explicit requests or an explicitly started Wayfinder workflow in
their instructions. Native Codex overlays in
[client-config/skill-invocation](client-config/skill-invocation) enforce the same
scope with `allow_implicit_invocation: false` and visible labels. Merge each
overlay into its matching external skill; do not vendor or rewrite the method.

## Intentionally outside this repository

- `svg-design` and the remaining Matt Pocock workflows are omitted by choice.
- Codex system skills and skills supplied by plugins remain host-managed.
- `hatch-pet` remains a Codex-local specialist skill.
- `inkscape-mcp` is a plain MCP reference without valid skill metadata and is
  not treated as a distributable skill.
