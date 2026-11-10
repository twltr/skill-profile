---
name: gsap
description: Build, explain or debug GSAP animations, including tweens, timelines, scroll effects, plugins and React/Vue/Svelte integration. Use for GSAP work or JavaScript animation-library selection; respect an already chosen alternative.
metadata:
  skill-type: leaf
  skill-tree: design
---

# GSAP

**Leaf skill** in Design; reached through its domain or by name.

Select the reference matching the animation task and continue that task. Establish
whether the work is explanation, implementation or diagnosis, which framework and
GSAP version the project uses, and the intended animation and lifecycle behavior.
Keep an explicitly chosen alternative library; ordinary CSS transitions do not
require adopting GSAP.

## A small routing example

**Request:** Add a scroll-linked sequence to a panel in an existing React page.
Read the React lifecycle reference and ScrollTrigger reference; include timeline
guidance if elements must appear in sequence. Check the installed GSAP version
before using version-sensitive details.

**Verify:** Inspect the real page at its relevant viewport sizes, then mount,
unmount and revisit it to check cleanup. Confirm the content remains available
with reduced motion. Do not load plugin, utility or other framework guides unless
the implementation needs them.

## Choose the relevant references

Read only the documents needed for the current question. Combine independent
facets when needed, such as React lifecycle and a scroll-driven timeline. Core
concepts are a prerequisite only when the task needs them, not a compulsory read
before every utility lookup.

| Question or task | Reference |
|---|---|
| Library choice, tween API, easing, transforms, responsive or reduced-motion behavior | [gsap-core](references/gsap-core.md) |
| Sequencing, position parameters or playback | [gsap-timeline](references/gsap-timeline.md) |
| Scroll-linked animation, pinning, scrub or ScrollTrigger lifecycle | [gsap-scrolltrigger](references/gsap-scrolltrigger.md) |
| React/Next.js integration, useGSAP, scope or cleanup | [gsap-react](references/gsap-react.md) |
| Vue/Nuxt, Svelte/SvelteKit or other framework lifecycle | [gsap-frameworks](references/gsap-frameworks.md) |
| Plugin registration, Flip, Draggable, text/SVG plugins or custom easing | [gsap-plugins](references/gsap-plugins.md) |
| Jank, layout/paint cost or animation performance | [gsap-performance](references/gsap-performance.md) |
| gsap.utils, mapping, clamping, snapping, collections or value helpers | [gsap-utils](references/gsap-utils.md) |

Resolve paths relative to this directory. The references retain their original
headings and related-skill names: those names refer to the files in this table,
not additional installed workflows. Follow a related reference only when it
answers a remaining question; do not traverse the whole collection or restart
this router. If a resource is missing, report the missing topic and consult its
official GSAP documentation when needed rather than inventing the contents.

## What is newer than the references

The references are GreenSock's own text and stop at GSAP 3.14. Checked on
2026-11-10, the current release is 3.15.1:

- **3.15** added `easeReverse`, a separate ease for when the playhead moves
  backwards (`true` reuses the forward ease; also valid in timeline `defaults`).
  It deprecates `yoyoEase`, which still works; write `easeReverse` in new code.
- **`@gsap/react`** is stable at 2.1.2; a 4.0 beta exists. Use the beta only if
  the project already does, and then read its release notes.
- **Licensing:** since 3.13 (April 2025) GSAP and every plugin, including the
  former Club plugins such as SplitText and MorphSVG, are free from the public
  `gsap` package, also commercially. The library's license is Webflow's
  standard "no charge" GSAP license, not MIT — the MIT license in this folder
  covers only the skill text. Its one notable restriction concerns no-code
  visual animation builders that compete with Webflow; if the project is such a
  tool, say so rather than assume the license allows it.

Check the installed version (`npm ls gsap`) before using anything from 3.13 on.

## Apply and verify

Return an explanation for an explanation request. For an authorized code change,
apply the selected API and framework guidance within the existing animation owner.
Check the affected animation, lifecycle cleanup and relevant responsive or
reduced-motion behavior in the actual available runtime. Report what ran and
any unverified visual or performance outcome. Consult current official GSAP docs
for version-sensitive APIs instead of treating a bundled example as timeless.
