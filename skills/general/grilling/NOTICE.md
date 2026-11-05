# Source and local adaptation

Based on Matt Pocock's [Grilling skill](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling)
at commit `3cca18b368ae95cdbdebbff572ccafa662551015`. The MIT license is preserved
in [LICENSE.txt](LICENSE.txt).

Reviewed on 2026-11-04 against the retained local upstream checkout at
`07121a191388677ffbc2ea60ec55fb468b0c2da6`. The retained upstream Grilling instruction file and
interface metadata match the public baseline byte for byte:

| Upstream file | SHA-256 |
|---|---|
| `SKILL.md` | `10ff989e7498b23b5acb49d5048f11dcd906757d2f79c5cdf8a00001381296f2` |
| `agents/openai.yaml` | `1411d7df7d99b7e621a1ff8283c8133cc2464be63d064e52d8ce169c6800ee9b` |

The local variant adds `policy.allow_implicit_invocation: false` to the native
metadata. The local opening now explains why prerequisite-aware rounds are useful,
and factual lookups distinguish direct tool use from substantial delegated research.
The human decision owner and question template remain intact. The 2026-11-05
quality review distinguishes human interviews from agent councils in discovery,
bounds the decision tree to the requested outcome and adds a fictional two-round
example showing a prerequisite-dependent question. Invocation control remains
in native metadata, not description labels.

`skills/general/grilling/` in Agent Profile owns this complete local variant.
Installed directories are deployment copies. The former catalog-only entry and
separate policy overlay are retired; future changes belong in this directory.
