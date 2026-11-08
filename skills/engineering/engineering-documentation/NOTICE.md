# Method lineage and evidence

Repository-owned method, revised on 2026-11-05. The book model comes from this
repository's Synopsis at `cddfca7:skills/synopsis/SKILL.md` and its later location
`cec7702^:skills/engineering/synopsis/SKILL.md`. Commit `cec7702` migrated it to
Technical Writing. The complete pre-split package is retained in the repository
archive; `e94a45b` identifies the last released source before this redesign.

Engineering Documentation retains ordered chapters, substantial topic folders,
construction/reason/invariant explanations and code-grounded verification. It
makes README, repository agent instructions and the docs book explicit owners,
with diagrams as primary explanations for suitable behavior and relationships.
The separate Technical Writing method owns standalone manuals; it is not a second
repository documentation owner. The shared pencil icons are preserved. The turn
figures are newly authored fictional teaching examples.

The following primary sources informed the revision. They are provenance and
scoped evidence, not a mandatory reading list for every writing task. Verify
current host behavior rather than freezing it to this research date.

The 2026-11-08 revision was compared with the user's reference repository
`twltr/agent-orchestration-backend` at `0215f3cee4bc29dc611729b79044b05422454bd9`,
especially its architecture pattern map and command/runtime/status source briefings.
The transferable method is complementary ownership: docs provide the system map,
named patterns, inspected sources and operational guidance; code preserves detailed
local intent. Its entire catalogue and convention gates are not prescribed here.
Fowler's Gateway and Seemann's Composition Root pages linked in SKILL.md were
inspected for the fictional examples. This is source-grounded method revision,
not evidence that the older skill caused the reference repository's quality.

| Source reviewed on 2026-11-05 | Contribution and limit |
|---|---|
| [GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | Supports purpose, usefulness and getting started as entrypoint jobs. The repository determines which integration/build/test/run/deploy steps apply. |
| [Diátaxis: Applying the framework](https://diataxis.fr/application/) | Distinguishes learning, task execution, explanation and reference. It does not prescribe this method's numbered filesystem layout or prove one directory tree superior. |
| [OpenAI: Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Demonstrates host-specific instruction discovery and scope. Other clients and versions need their own verification; file presence is insufficient. |
| [W3C WAI: Complex Images](https://www.w3.org/WAI/tutorials/images/complex/) | Requires identification and an equivalent account of essential information. A compact structured alternative can preserve a diagram's meaning without a second narrative. This is accessibility guidance, not evidence about model retrieval. |
| [Gloaguen et al., Evaluating AGENTS.md, arXiv:2602.11988v3](https://arxiv.org/abs/2602.11988v3), revised 2026-09-29 | Reports no general task-success improvement and increased inference cost across generated and developer-committed context files in its evaluations. It motivates selective, evaluated instructions; it does not prove all repository instructions harmful or test this skill. |
| [Khatri, Do Context Files Help Coding Agents?, REALM 2026](https://aclanthology.org/2026.realm-1.5/) | A 288-run study of two agents, 17 tasks and three repositories found no measurable correctness change within its stated equivalence bounds. Its small, task-specific setting cannot establish universal effects. |

“Agent-friendly” here means bounded entrypoints, accurate commands, searchable
identifiers and explicit owners. It is a design objective, not a benchmark result.
SVG retrieval and any claimed productivity improvement require representative
trials on the actual host. The research does not justify more always-loaded text.

These sources were summarized independently; their pages and papers were not
copied into the package. SVG construction and prose mechanics remain owned by
Editorial SVG Diagrams and Unslop.
