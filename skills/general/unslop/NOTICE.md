# Sources and licenses

This is a maintained adaptation, revised on 2026-10-09. It combines selected
writing guidance rather than concatenating the upstream skills. The exact
reviewed revisions and source hashes are in [sources.json](sources.json).

| Source | Reviewed revision | Material used | Preserved license |
|---|---|---|---|
| [Lauren Tan, Pstack Unslop](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/unslop/SKILL.md) | `ccb5507cec1546dc88135c1139c811e6c59115ba` | Plain words, concrete mechanisms, active voice, removal of filler and protection against over-compression. | [MIT, Copyright 2026 Lauren Tan](LICENSE) |
| [Siqi Chen, Humanizer 3.1.0](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md) | `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8` | Meaning-preserving revision, reader context, structural repetition and respect for the writer's supplied voice. | [MIT, Copyright 2025 Siqi Chen](licenses/Humanizer-MIT.txt) |
| [Leonardo Flores, Writing Clearly and Concisely](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/writing-clearly-and-concisely/SKILL.md) | `3027f20f3181758385a1bb8c022d4041dfb4de84` | Concrete language, paragraph focus, parallel comparisons and keeping related words together. | [MIT, Copyright 2026 Leonardo Flores](licenses/Writing-clearly-and-concisely-MIT.txt) |

The original local Unslop import used Cursor commit
`70b2dc8b4b85c8d5648624ca40d692c421fff32f`, Git blob
`229a090708710c36caa0017f8d33e90880dc6846`. Its SKILL.md SHA-256 was
`195411d320b5b328f9f642baf59757ed19aaf0931c0838740e0aca273d538dc1`.
The newly reviewed Cursor revision has the same skill bytes. The current
adaptation changes those bytes; the source hashes identify upstream inputs,
not the installed result.

Writing Clearly and Concisely summarizes William Strunk Jr.'s 1918
*The Elements of Style*. Its composition reference was consulted for those
principles; no book passages are reproduced. Humanizer attributes its pattern
research to Wikipedia's Signs of AI writing. This adaptation takes selected
editorial principles and independently phrases them; it does not reproduce
Wikipedia material or Humanizer's examples.

The adaptation adds German usage, meaningful Markdown formatting, topic grouping,
preserved uncertainty, requested depth and a lightweight path for ordinary replies.
These additions include Tobi's 2026-10-09 direction to make relationships visually
legible without losing necessary meaning. It does not carry
forward blanket punctuation bans, invented personal reactions, mandatory
multi-pass output, automatic subagent delegation or a percentage-reduction
quota. The old numbered rule list is retired; no references to its rule IDs
were found in the affected source or local standalone skills.

Invocation uses the documented `agents/openai.yaml` policy. The upstream
`disable-model-invocation` frontmatter and the conflicting “Must always apply”
claim are replaced by a precise prose trigger and implicit invocation enabled.
Good Writing and its four specialists require this method, including during
direct use. That instruction is not a technical guarantee that every runtime
loads it; installation, discovery and actual use require separate evidence.
