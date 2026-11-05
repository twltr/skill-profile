# Model routing by phase and capability

Read when selecting or reassessing delegate models. Puppeteer owns the work split;
this reference owns the maintained routing preference. It is guidance, not an
installed configuration, account entitlement or guarantee of output quality.

## Current preference snapshot

Reviewed **2026-11-05**. Use the current verified, supported model line that fits
the assignment and is exposed by the actual host. Do not invent a successor ID
or select a newly announced model merely because it is newer. The named GPT and
Claude routes below implement Tobi's preferences; they are not a measured ranking
of every model. In particular, Fable-over-Opus for visuals and Opus for general
Claude review are preferences, not conclusions from a comparative UI benchmark.

| Host family | Planning and unresolved design | Settled nonvisual implementation | Independent review and visual work |
|---|---|---|---|
| GPT | Retain a suitable main model; Astra scouts are appropriate for consequential reasoning. A Sol lead can keep work it can establish. | Prefer `gpt-6.1-sol` when it can satisfy the settled contract. Choose effort for the actual difficulty rather than inheriting an expensive setting accidentally. | Prefer `gpt-6-astra` for general review and for visual planning, authoring and review. Use `high` normally; `xhigh` for demanding composition, interacting states or substantial uncertainty. **Never `max` or `ultra` on this Astra route.** |
| Claude | Retain a suitable main model; use Fable for demanding unresolved work when warranted. | Prefer `claude-opus-5-5` for the settled work described here rather than automatically using Fable for every step. | Prefer `claude-opus-5-5` for general code review; prefer `claude-fable-5-1` for visual planning, authoring and review. Opus is a possible visual alternative, subject to the same rendered checks. |
| Kimi | Use a capable configured model; current public multimodal candidates include `kimi-k3.1-pro` and `kimi-k3`. | Use a sufficient configured worker. No smaller-tier cost or quality advantage is established by this snapshot. | `kimi-k3.1-pro` is a documented image-understanding candidate, not a proven best visual reviewer. Check the actual model binding and image route. |
| Gemini | Use a capable configured model; `gemini-4-argon` is a current documented reasoning candidate. | Use a sufficient configured worker. This snapshot does not establish an efficient implementation tier for the installed CLI. | `gemini-4-argon` accepts images and produces text, making it a candidate for screenshot reasoning and UI/SVG code. Validate its task fit; do not infer comparative aesthetic quality. |

The preference for Astra does not mean Sol lacks vision: current OpenAI guidance
also describes Sol for visual deliverables. Select by the requested quality bar,
observed performance and the user's route. For a compact known correction,
`high` is sufficient as the Astra starting point; a larger artifact does not
automatically justify more effort unless its decisions need it.

GPT effort labels are not portable provider settings. Use only the chosen model
and client's supported controls. For an Astra assignment, select `high` or `xhigh`
explicitly where possible and check role overrides; do not silently fall through
to an inherited `max` or an uncontrolled higher-compute mode.

## Check the actual route before assigning work

Resolve the available models, native aliases, role restrictions, effort controls
and tool access. An API model ID is not necessarily a selectable CLI alias.
Use a current authoritative host catalogue/schema; consult the model owner when
an identifier, capability or lifecycle claim is uncertain. Prefer the appropriate
route within the current authorized environment. A missing model does not authorize
switching accounts/providers, adding credentials, changing persistent settings
or installing a different client. Identify a justified available alternative and
its limits, or retain the affected quality gate as open.

Image understanding, visual design quality and image generation are distinct.
Text-output models can author SVG/CSS and reason over screenshots; a raster image
generator supplies assets through a separate supported tool. For example, Gemini's
documented `gemini-nano-banana-2.1` image-generation capability does not select the
model that should review the resulting UI. Confirm that the assigned agent actually
receives the rendered image at a useful size. An accessibility tree, DOM or source
alone cannot establish spacing, color, composition or legibility.

Native mechanisms observed locally on 2026-11-05:

- **Codex 0.159.0 / current native delegation surface:** Astra and Sol are exposed;
  explicit model and effort selection is supported. Some named roles fix their
  model/effort. Use a suitable selectable role and the actual context-fork controls.
- **Claude Code 2.1.277:** agent definitions support model and effort; image reading
  is present. Do not copy a newer per-invocation effort option blindly: current
  documentation dates that option to 2.1.292. Account/model access was not exercised.
- **Kimi Code 2.0.2:** a configured secondary-model pool can expose selection and
  effort; the installed pool/force/`primary` behavior differs from current English
  docs. Inspect its effective schema and configured pool rather than importing an
  API ID as a working alias. Image delivery depends on the selected provider route.
- **Gemini CLI 0.66.0:** after the authorized upgrade from 0.24.5, the installed
  custom-agent loader reads Markdown with YAML frontmatter. Its strict local-agent
  schema supports `model`, `temperature`, tools and execution limits, but no
  effort/thinking field. Browser `visualModel` configuration and wiring are present;
  actual screenshot analysis and account access to the listed model were not
  exercised. The separate skill loader still retains only name and description
  from frontmatter and does not enforce explicit-only invocation metadata. All 30
  shared skills were discovered; the existing disabled list was preserved.

These observations are host/version-specific, not minimum requirements or a
promise about another machine. Record requested versus effective selection when
the runtime exposes it; leave an unobservable value unverified. A supported route,
a completed delegation and a visually verified result are separate claims.

## Keep the snapshot useful

Revalidate affected entries when model lines or aliases change, the host rejects
an ID/effort, a material client update changes routing, or task results contradict
the expected capability. Inspect native availability first, then current official
model, capability and deprecation guidance. A cache alone does not settle a changed
lineup. Where comparative quality matters, use the same representative brief and
rendered states; assess requirement fidelity, visual defects, false positives and
correction cost. Do not turn provider marketing or an anecdote into a universal rank.

During authorized collection maintenance, update this single reference, its date,
sources and limits using the repository's archive-before-change and distribution
procedure. Caller skills link here instead of copying model names. No second
scheduler, telemetry store or automatic client reconfiguration is introduced.

Observe cost at the completed-assignment level: available reported tokens across
lead, workers and review; retries and correction cycles; and whether the required
quality and evidence were achieved. Keep a useful observation at the existing
plan/review owner, not in a separate usage diary. Missing totals stay unavailable;
do not invent savings or a token budget. If the route costs too much, first inspect
duplicated reading, oversized briefs and repeated review; then use a sufficient
more efficient model where quality permits. If failures drive rework, strengthen
the model or resolve the missing contract. Feed supported recurring lessons back
into this reference during maintenance; one good example is not a general result.

## Primary evidence and limits

- [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra),
  [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection)
  and [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  capabilities, task guidance and native selection; the user's effort preference
  is stricter than the full set of supported levels.
- [Claude models](https://platform.claude.com/docs/en/models/overview) and
  [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): model IDs,
  image input/text output and routing. General provider recommendations do not
  establish a visual ranking.
- [Kimi models](https://platform.kimi.ai/docs/models),
  [vision input](https://platform.kimi.ai/docs/guide/use-kimi-vision-model) and
  [Kimi Code configuration](https://www.kimi.com/code/docs/en/kimi-code-cli/configuration/config-files):
  public capabilities and pool concepts; verify installed-version differences.
- [Gemini 4 Argon](https://aistudio.google.com/docs/models/gemini-4-argon),
  [Nano Banana 2.1](https://aistudio.google.com/docs/models/gemini-nano-banana-2.1)
  and [Gemini CLI subagents](https://geminicli.com/docs/core/subagents/): reasoning,
  generation and current agent interfaces; these do not prove access in an older CLI.
