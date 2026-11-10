# Model routing by phase and capability

Read when selecting or reassessing delegate models. Puppeteer owns the work
split; this file owns the maintained routing preference. It is guidance, not an
installed configuration, account entitlement or guarantee of output quality.
Caller skills link here instead of copying model names.

## Current preference snapshot

Reviewed **2026-11-05**. The named GPT and Claude routes implement the user's
preferences, not a measured ranking of every model; in particular Fable over
Opus for visuals and Opus for general Claude review are preferences, not results
of a comparative benchmark. Use the current verified model line the actual host
exposes; do not invent a successor ID or pick a model merely because it is newer.

| Host | Planning, unresolved design | Settled nonvisual implementation | Independent review | Visual planning, authoring, review |
|---|---|---|---|---|
| GPT | Suitable main model; `gpt-6-astra` scouts for consequential reasoning; a Sol lead keeps work it can establish | `gpt-6.1-sol` when it can satisfy the settled contract | `gpt-6-astra`, effort `high` | `gpt-6-astra`, `high` or `xhigh` |
| Claude | Suitable main model; `claude-fable-5-1` when demanding | `claude-opus-5-5`, rather than Fable for every step | `claude-opus-5-5` | `claude-fable-5-1` (Opus as alternative) |
| Kimi | Configured capable model, e.g. `kimi-k3.1-pro`, `kimi-k3` | A sufficient configured worker | Configured capable model | `kimi-k3.1-pro` is an image-understanding candidate, not a proven best reviewer |
| Gemini | Configured capable model, e.g. `gemini-4-argon` | A sufficient configured worker | Configured capable model | `gemini-4-argon` accepts images; validate task fit |

**GPT effort.** Choose effort for the actual difficulty instead of inheriting an
expensive setting. On the Astra route use `high` normally and `xhigh` for
demanding composition, interacting states or substantial uncertainty; a larger
artifact alone does not justify more. **Never `max` or `ultra` on the Astra
route**: that is the user's standing rule, not a capability limit. Select the level explicitly
where possible and check role overrides so nothing silently falls through to an
inherited higher mode. Effort labels are not portable across providers.

**Astra versus Sol for visuals.** Current OpenAI guidance also describes Sol for
visual deliverables. The Astra preference reflects the requested quality bar and
observed performance, not a lack of vision in Sol.

**Smaller tiers.** This snapshot establishes no cost or quality advantage of a
smaller Kimi, Gemini or Claude tier for implementation; use the configured
worker until evidence says otherwise.

## Check the actual route before assigning work

Resolve the available models, native aliases, role restrictions, effort controls
and tool access. An API model ID is not necessarily a selectable CLI alias.
Consult the host's current catalogue or schema, and the model owner when an
identifier, capability or lifecycle claim is uncertain. A missing model does not
authorize switching accounts or providers, adding credentials, changing
persistent settings or installing another client: name a justified available
alternative and its limits, or keep the affected quality gate open.

Image understanding, visual design quality and image generation are distinct.
Text-output models can author SVG or CSS and reason over screenshots; a raster
generator such as `gemini-nano-banana-2.1` supplies assets through its own tool
and does not decide who reviews the resulting UI. Confirm that the assigned
agent actually receives the rendered image at a useful size: an accessibility
tree, DOM or source alone cannot establish spacing, color or legibility.

## Host notes

Observed locally on 2026-11-05; version-specific, not minimum requirements.

- **Codex 0.159.0:** Astra and Sol are selectable with explicit model and effort.
  Some named roles fix their model or effort. The context-fork control accepts
  only `fork_turns="none"` or `"all"`; a standalone brief uses `"none"` — do not
  invent a partial-history value.
- **Claude Code 2.1.277:** agent definitions support model and effort; image
  reading is present. Per-invocation effort is documented from 2.1.292, so do not
  rely on it on older versions. Account and model access were not exercised.
- **Kimi Code 2.0.2:** a configured secondary-model pool exposes selection and
  effort; the installed pool behavior differs from current English docs, so
  inspect the effective schema instead of importing an API ID as an alias. Image
  delivery depends on the selected provider route.
- **Gemini CLI 0.66.0:** custom agents are Markdown with YAML frontmatter and
  support `model`, `temperature`, tools and limits, but no effort or thinking
  field. Browser `visualModel` wiring exists; actual screenshot analysis was not
  exercised.

Record requested versus effective selection when the runtime exposes it and leave
an unobservable value unverified. A supported route, a completed delegation and a
visually verified result are separate claims.

## Maintaining this snapshot

Read only when updating this file. Revalidate affected entries when model lines
or aliases change, a host rejects an ID or effort, a client update changes
routing, or results contradict the expected capability. Inspect native
availability first, then current official model, capability and deprecation
guidance; a cache alone does not settle a changed lineup. Where comparative quality matters, use the same representative brief
and rendered states and assess requirement fidelity, visual defects, false
positives and correction cost; do not turn marketing or an anecdote into a rank.

Judge cost per completed assignment: reported tokens across lead, workers and
review, retries and correction cycles, and whether the required quality was
reached. Missing totals stay unavailable; do not invent savings or a token
budget. If a route costs too much, first look for duplicated reading, oversized
briefs and repeated review, then a sufficient cheaper model. If failures drive
rework, strengthen the model or fix the missing contract. Keep observations at
the existing plan or review owner and feed recurring lessons back here during
authorized maintenance, using the repository's archive-before-change and
distribution procedure.

## Primary evidence and limits

- [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra),
  [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection)
  and [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  capabilities, task guidance and native selection; the user's effort rule is
  stricter than the full set of supported levels.
- [Claude models](https://platform.claude.com/docs/en/models/overview) and
  [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): model IDs,
  image input and routing. General provider recommendations do not establish a
  visual ranking.
- [Kimi models](https://platform.kimi.ai/docs/models),
  [vision input](https://platform.kimi.ai/docs/guide/use-kimi-vision-model) and
  [Kimi Code configuration](https://www.kimi.com/code/docs/en/kimi-code-cli/configuration/config-files):
  public capabilities and pool concepts; verify installed-version differences.
- [Gemini 4 Argon](https://aistudio.google.com/docs/models/gemini-4-argon),
  [Nano Banana 2.1](https://aistudio.google.com/docs/models/gemini-nano-banana-2.1)
  and [Gemini CLI subagents](https://geminicli.com/docs/core/subagents/): reasoning,
  generation and agent interfaces; these do not prove access in an older CLI.
