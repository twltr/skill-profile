# Source preservation

The eight references were moved from the existing GSAP skill installation without
changing their bytes, examples, source links or MIT metadata. Their source is
GreenSock's official `gsap-skills` repository at commit
`aed9cfd3277740755f6bfc1155c7aa645403b760`:
https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760/skills
The router is a local packaging adaptation; it does not claim to be an upstream
GSAP release.

`references-manifest.json` records the original entrypoint names and SHA-256 hashes.
Updates replace the matching reference from its reviewed source, refresh the hash
and check the router mapping. The references are resources, not nested SKILL.md
entrypoints. The Skill Profile is the source for every installed copy. The pre-change
installation of this router remains in the external recovery bundle recorded at
the time.

The MIT license in [LICENSE](LICENSE) covers the skill text. The GSAP library
itself is licensed separately by Webflow (see below).

## Currency check, 2026-11-10

- **Upstream skills:** `greensock/gsap-skills` HEAD is still `aed9cfd` (committed
  2026-04-21). All eight `skills/*/SKILL.md` files are byte-identical to our
  references, so no reference was refreshed.
- **Library version:** npm lists `gsap` 3.15.1 (published 2026-11-04) as current;
  3.14.0 appeared 2025-12-08 and 3.15.0 on 2026-04-13. `@gsap/react` is 2.1.2
  stable, with `4.0.0-beta.3` published 2026-11-05. The docs at
  https://gsap.com/docs/v3/ show v3.15.
- **API changes since the references:** the 3.14 MorphSVG options (`smooth`,
  `redraw`, `curveMode`) are already covered. The 3.15 release post
  (https://gsap.com/blog/3-15/, 2026-04-13) adds `easeReverse` and deprecates
  `yoyoEase`; the references do not mention either, and no reference uses
  `yoyoEase`. The router's "What is newer than the references" section records
  this instead of editing the byte-preserved files.
- **Licensing:** https://gsap.com/licensing/ shows the Standard "No Charge" GSAP
  License issued by Webflow, effective 2025-04-30: free including commercial use
  and all formerly Club-only plugins, not an open-source license, with a
  prohibited use for no-code visual animation builders competing with Webflow.
  The `gsap-plugins` reference already states that every plugin is free and that
  private-registry and auth-token instructions are outdated; the router now adds
  the license name and the restriction.
