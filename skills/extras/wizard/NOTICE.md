# Source and local adaptation

Based on Matt Pocock's [Wizard skill](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/wizard)
at commit `3cca18b368ae95cdbdebbff572ccafa662551015`. The MIT license from the
upstream repository root is preserved in [LICENSE](LICENSE).

Imported on 2026-11-10 from a locally installed Codex copy, at the owner's
request to add Wizard to the extras. The installed files match the upstream
files at that commit byte for byte:

| Upstream file | SHA-256 |
|---|---|
| `skills/engineering/wizard/SKILL.md` | `bdf31d48211ea559878f95a4f344aeabf8d85897488ba564382bab0b000daac1` |
| `skills/engineering/wizard/template.sh` | `33cbe9dfb1d0e9185b60248a52aabed14bc64785a00cac695e302e739dd6c153` |
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

## Later upstream changes not included

Upstream `main` at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` changes
`template.sh` in two later commits:
`868c4cf20cb7e08bc805c388ff1f305dbedd261a` and
`49dd158d1076134a641b33efb035946536778336` (PR #1237). In the library they
single-quote values written to `.env` and decode them on re-runs, create a new
`.env` with mode 0600, write through a symlinked `.env` instead of replacing it,
make a prompt fail at end of input instead of continuing with an empty value,
edit visible input with Readline and drop the unused `RED` variable, which
`shellcheck` reports as SC2034 in this snapshot. Below the marker they wrap the
example stages in a `run_wizard` function so an edit during a run cannot break
it. `SKILL.md` and `agents/openai.yaml` are unchanged upstream. Adopting these
fixes is a vendored snapshot refresh: review them, then replace `template.sh`
as a whole.

`skills/extras/wizard/` in the Skill Profile owns this local variant. Installed
directories are deployment copies.
