# Source and local adaptation

Based on Matt Pocock's [Wizard skill](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wizard)
at commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`. The MIT license from the
upstream repository root is preserved in [LICENSE](LICENSE).

Imported on 2026-11-10 at the owner's request to add Wizard to the extras.
`SKILL.md`, `agents/openai.yaml` and `LICENSE` came from a locally installed
Codex copy of commit `3cca18b368ae95cdbdebbff572ccafa662551015`. They are
unchanged at `4ae2317`. `template.sh` was taken whole from `4ae2317`, which
includes the later template fixes in `868c4cf20cb7e08bc805c388ff1f305dbedd261a`
and `49dd158d1076134a641b33efb035946536778336` (PR #1237). The upstream files at
`4ae2317`:

| Upstream file | SHA-256 |
|---|---|
| `skills/engineering/wizard/SKILL.md` | `bdf31d48211ea559878f95a4f344aeabf8d85897488ba564382bab0b000daac1` |
| `skills/engineering/wizard/template.sh` | `6566f147299bc6f1d941e64591ed04385416d543e11f96f564c7228f5018d0ed` |
| `skills/engineering/wizard/agents/openai.yaml` | `98f44d682d58e262f160dc59a8befc365e0aa65820dd0261864af26aa8e59d83` |
| `LICENSE` (repository root) | `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5` |

## Local changes

Only the repository's shared-leaf conventions required changes:

- `SKILL.md` frontmatter gains `metadata.skill-type: leaf`. A shared leaf
  declares no `skill-tree` and no `skill-requires`.
- `SKILL.md` gains one first body line declaring the shared-leaf type, worded
  as in the other extras. The rest of the instruction text, the description
  included, is unchanged.
- `agents/openai.yaml` adds `policy.allow_implicit_invocation: false`, the
  `Leaf:` prefix on the short description and the two icon slots.
- `assets/` holds a local wizard-hat icon (SVG originals, 128 and 256 px PNG
  exports) in the collection's palette. It is original work.

`template.sh` is byte-identical to upstream, including the library above the
`STAGES` marker that the method says never to hand-edit.

## Review on 2026-11-10

`bash -n` passes. The helpers `SKILL.md` names (`stage`, `say`, `step`,
`open_url`, `ask`, `ask_secret`, `write_env`, `set_secret`, `set_var`, `pause`,
`confirm`, `TOTAL_STAGES`) all exist in the template. The template's own comment
adds that stages stay inside `run_wizard`. `shellcheck` reports SC1087 on
`$e[Enter keeps current]` in `ask`. That is a false positive: `$e` is a scalar
followed by literal text. It also reports SC2329 for `confirm` and `set_var`,
which the example stage does not call.

On bash 3.2, the default `bash` on macOS, `_existing` keeps the backslash when
decoding a stored value that contains a single quote: `it's` comes back as
`it\'s`, and keeping it on a re-run writes the backslash back into `.env`.
Bash 4.4 and 5.2 decode it correctly. The 0600 mode, symlink and
end-of-input fixes behave as intended on all three.
