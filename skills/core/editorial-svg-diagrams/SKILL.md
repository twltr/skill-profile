---
name: editorial-svg-diagrams
description: >-
  Create explanatory diagrams for documentation, architecture, workflows and learning material as editable transparent SVGs with theme variants and PNG/PDF exports. Use whenever a concept, system, process or relationship would be clearer as a figure, in a README, article, slide or web page, even if the user only says "draw how this works". Use SVG Design for logos, icons, brand assets and decorative website graphics.
metadata:
  skill-type: core
---

# Editorial SVG Diagrams — explanation first

**Core skill.** On the agent's surface and usable in any context.

**A diagram is a visual sentence, not a document in miniature.** The common
failure is a figure that tries to be the article: titles, cards, paragraphs and
a fixed page background, with the one relationship that mattered buried among
them. Here the visual structure carries the idea and supporting prose lives
*outside* the figure. More labels, bigger cards, longer descriptions or a giant
canvas are not higher fidelity. When the user shows a reference figure, match
its density, not its surrounding page.

## A finished explanation example

The accepted [cache hit/miss figure](assets/accepted/cache-hit-miss.svg) makes
one distinction visible: a hit returns from the cache, while a miss adds a
database round trip. It aligns Client, Cache and Database, then separates the
two paths so the added work is immediately clear. Read the figure for the
relationship; keep implementation caveats in the surrounding explanation.

## Choose the output mode before drawing

The destination decides who owns the background and the theme, so it decides
what the file must contain.

- **In a chat with native UI/diagram primitives:** prefer native host layout elements and inline SVG when they create the clearest illustration. Host-managed text, backgrounds, padding and semantic colors can follow the host theme. Use plain text outside the illustration for explanation. Do not force the user into a downloadable PNG just to show a diagram in chat. Respect the host's supported component system; do not emit unsupported tags.
- **For a repository, paper, documentation, download, reuse, or user-requested SVG:** create a *real standalone* transparent `.svg`. Treat the output as the small reusable visual portion, not the whole surrounding article. Also supply a PNG preview when useful and an explicitly colored `.dark.svg` for dark surfaces when helpful.
- **For HTML pages with native design tokens:** inline the SVG and inherit `currentColor`/CSS variables or use native UI layouts; if embedding with `<img>`, document theme limitations. A standalone SVG with `@media (prefers-color-scheme: dark)` can follow the browser/OS preference; it does **not necessarily** follow a site's manual theme override. For dependable manual themes use two SVG assets with a theme-controlled source switch.
- **For print/Office/PDF:** export the light SVG as a vector PDF if supported, or a sized PNG fallback. Transparency is still the default in the SVG file; choose a page background in the document, not inside the illustration.

[references/embedding-and-formats.md](references/embedding-and-formats.md) has
the per-destination details and export recipes.

## Decide who composes and who reviews

Geometry and legibility can only be judged by looking at a render, so before
substantial visual composition or review, assess the model's visual judgment
and render access. If **Puppeteer** is available, use its current phase/model
routing for a better-suited author or independent reviewer; pass the verified
meaning, takeaway, embedding size and relevant theme renders. If a delegation
already runs for this work, go through its owner instead of starting another.
A small suitable edit can stay direct. Semantic correctness and visual clarity
need their own evidence; author checks are not independent acceptance. Missing
visual capability or render access cannot be replaced by passing SVG lints.

## The visual-first workflow

The order matters: a figure planned around its text ends up as text in boxes.
Fix the takeaway and remove the prose first, then choose the form, then draw.

1. **Name one visual takeaway.** Write privately: "After seeing the figure, the reader should perceive ____." Examples: the three directions of SYN/SYN-ACK/ACK; every network header wrapping the preceding data; knowing one location versus having eight possibilities. Verify semantics against source material, code, or explicit assumptions.
2. **Remove prose before drawing.** Put chapter title, definition, caveats, citations, explanations, and conclusion in the *surrounding text*. Keep labels attached to actual shapes, regions, or arrows only. Default visible content: at most ~12 short labels / ~35 words, each label ideally 1–3 words. These are targets, not grounds to omit indispensable data; `visual_guard.py` only warns above 35 words or 24 labels, so passing it does not mean the figure is lean. If explaining requires several sentences inside the figure, split the figure or write those sentences outside it.
3. **Choose the representation before its layout.** Ask for every figure: **Which visual form explains this question most clearly? How can I draw it most cleanly?** Compare plausible alternatives against the same takeaway before choosing: containment, layers, timeline, sequence, state, queue, matrix, repeated slots, or a true dependency topology. Read [references/visual-patterns.md](references/visual-patterns.md). A table, short text, or no extra figure may be clearer. Choose by the relationship, never by habit or a quota for variety. Reusing boxes and arrows for every subject is not a visual system; consistent typography and geometry can unify different diagram types.
4. **Plan the geometry, then compose to the content.** Sketch the alignment axes, peer sizes, repeated gaps, group padding and connector channels before drawing details. Use a small spacing unit; align related centers or edges and give equal relationships equal spacing. Route each connector between intentional ports through free space, without passing through unrelated nodes, labels or borders. Prefer a short clear route to unexplained bends; use shared buses only for a real shared relationship. Fit a tight `viewBox` to the result and keep the frame free of what the [style contract](#the-style-contract-hard-defaults) excludes.
5. **Draw accurately with restrained visual grammar.** Use SVG primitives (`rect`, `circle`, `path`, `line`, `text`), clean route geometry, 2–4px arrows, enough spacing, consistent radii, blue/teal as default semantic accents. Show all labels at sizes readable at final embedding width. Read [references/svg-construction.md](references/svg-construction.md) when building or teaching.
6. **Handle color and backgrounds intentionally.** Keep the canvas transparent. Use neutral strokes/text plus a few meaningful accent fills. For static SVG, use dark text/strokes on light surroundings and light text/strokes in the explicit dark variant; use embedded `prefers-color-scheme` CSS only as progressive enhancement. Check with two different backgrounds. Do not assume `currentColor` in an external SVG `<img>` inherits the page theme; it does not.
7. **Validate, export, inspect, revise.** Resolve helper paths from the installed skill directory, not the current project folder:

   ```bash
   python scripts/preflight_svg.py figure.svg      # XML, accessibility, portable resources
   python scripts/visual_guard.py figure.svg       # text budget, full-canvas background
   python scripts/export_svg.py figure.svg --format png --scale 2
   python scripts/preview_themes.py figure.svg --dark figure.dark.svg --out theme-check.png
   ```

   Run `python scripts/build_examples.py` only when regenerating the bundled figures; it rewrites `assets/`. Then **open the light and dark renders** at actual display or print width and check:

   - alignment, repeated gaps, grouping, connector paths and endpoints;
   - typography, clipping, contrast and arrowheads;
   - with the labels ignored for a moment: does the geometry itself expose the intended order or relationship?

   Reconsider the diagram type if a tidy arrangement still needs awkward detours or diffuse placement. Fix and re-render every affected variant. Passing lints does not establish visual quality: if no renderer is available (previews need `cairosvg` and Pillow), report the visual check as open.
8. **Deliver usable assets without unnecessary commentary.** Return SVG and, when relevant, PNG/PDF or variants. Put factual caveats as adjacent prose/captions, not visible text drawn into the SVG. Describe what differs across variants where it matters.

## The style contract (hard defaults)

Each default protects the figure's job of showing one relationship; break one
only when the user asks for it.

- **No root background fill** (`<rect width="100%" height="100%" fill="#fff">`, etc.) unless the user explicitly asks for a fixed-background image. Keep SVG alpha transparent and let the destination own its page color.
- **No gratuitous text as graphics:** no explanatory paragraphs, title/subtitle, glossary, source attribution, legend or outcome prose inside the SVG by default. Semantic `<title>` and `<desc>` are *nonvisual metadata* and should remain.
- **No page furniture in the frame:** no floating whitespace, built-in title strip, decorative eyebrow, page-colored rectangle, giant footer or whole-document card frame. A host border belongs to the surrounding document.
- **No generic dashboards:** avoid multiple equal cards with filler text and icons if a single arrow, progression or state contrast conveys more.
- **No forced fixed artboard:** fit `viewBox` tightly; prefer shape-to-area and visual balance over defaulting to 960×600.
- **No gratuitous decorations:** a border or region boundary must encode a real entity, scope or intentional separator. Shadows, gradients and random brand palettes are off by default.
- **Not every figure requires an arrow:** the entropy example relies on marked versus possible positions; adding arrows there would confuse the meaning.
- **Respect sequence conventions:** time downward, actors aligned, clear sender/recipient, directional lines; simplified diagonals are valid for chronological messages, as in the bundled handshake. Use orthogonal routes for complex architectures when that improves readability.
- **No false technical semantics:** distinguish UDP from TCP; do not imply eight actual particles in an eight-position entropy illustration; ensure header nesting is logically accurate and label proportions as schematic if relevant.

## Test against references, not just SVG validity

[references/reference-contrast.md](references/reference-contrast.md) puts a
compact reference crop beside an earlier over-labeled output of the *same* TCP
handshake. The old figure is a regression example, not a style template: three
visible messages are the story, not large endpoint cards and paragraphs.

The owner also accepted three figures on 2026-10-23 as visual benchmarks:
[binary search](assets/accepted/binary-search.svg),
[cache hit/miss](assets/accepted/cache-hit-miss.svg) and
[debouncing](assets/accepted/debouncing.svg), each with an explicit dark
variant. Their editable SVGs are preserved from the supplied test archive; the
import manifest records their provenance. Compare the visual mechanism, not
identical styling: shrinking region, diverging paths, or input/output timing.

When asked to recreate a provided figure, inspect or crop the figure itself
rather than importing surrounding page chrome into the art.

## Assets and tools

| Resource | Purpose |
|---|---|
| [references/reference-contrast.md](references/reference-contrast.md) | Cropped positive vs negative example of the same diagram; failure modes |
| [references/visual-patterns.md](references/visual-patterns.md) | Visual metaphors and layout grammars (sequence, comparison, encapsulation, architecture) |
| [references/svg-construction.md](references/svg-construction.md) | Step-by-step SVG building, style classes, arrow geometry and responsive themes |
| [references/embedding-and-formats.md](references/embedding-and-formats.md) | Actual theme behavior in chat/HTML/README/LaTeX/Office; export recipes |
| `assets/tcp-handshake.svg`, `.dark.svg` | Minimal three-message explanation with no article text |
| `assets/entropy-possibilities.svg`, `.dark.svg` | Two-row state comparison: exactly one versus eight possibilities |
| `assets/packet-encapsulation.svg`, `.dark.svg` | Layering through actual colored band geometry |
| `assets/pc-connection.svg`, `.dark.svg` | Two endpoints, direction and ports |
| `assets/osi-layers.svg`, `.dark.svg` | Lean layer stack |
| `assets/codebase-architecture.svg`, `.dark.svg` | Deliberately generic 3-component example, not a verified codebase |
| `assets/starter.svg`, `.dark.svg` | Tiny editable starting point |
| `assets/accepted/` | The three accepted benchmark figures and their dark variants |
| `scripts/build_examples.py` | Deterministically rebuild the generated examples and variants |
| `scripts/preflight_svg.py` | XML/accessibility/portable-resource checks |
| `scripts/visual_guard.py` | Explanation-first text budget and full-background regression gate |
| `scripts/export_svg.py` | PNG/vector PDF export |
| `scripts/preview_themes.py` | Composite previews on light and dark surfaces |

## Learning mode

When the user wants to *learn* SVG, begin with `assets/starter.svg` or `assets/tcp-handshake.svg`. Explain `viewBox`, coordinate origin, primitives, paths, fills and classes **using a real pictured example**. Give one small edit (change arrow positions, add a fourth message, swap one highlight). Keep tutorial prose outside the SVG. If teaching a specific diagram, show the result as a diagram first, then annotated source excerpts separately.

## Scope relative to other skills

Choose by the graphic's purpose, not its file format or placement. This skill
owns diagrams that explain a concept, relationship, process or system, including
those embedded in websites, presentations and articles, with their editable SVG,
themes, exports and visual checks. A process diagram on a landing page belongs
here; the site's logo, icon set and decorative hero artwork do not.

Logos, icons, brand assets, decorative web graphics and the surrounding page
layout are design work, not explanatory figures. Hand those parts back to the
agent with the figure's purpose and space constraints, so it can take them to a
design method. Without one, follow the existing design system and keep this
work within the figure's scope.
