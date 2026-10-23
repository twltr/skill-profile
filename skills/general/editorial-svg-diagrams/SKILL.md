---
name: editorial-svg-diagrams
description: >-
  Create and teach explanation-first diagrams: clean visual aids with very few words, meaningful geometry, restrained color and theme-aware presentation. Use for short illustrative figures within explanations, documentation, papers, READMEs, software architecture, protocol handshakes, OSI layers, encapsulation, uncertainty/entropy, state changes or scientific concepts. Produce real standalone transparent SVGs plus optional dark/light variants, PNG or PDF exports when files are requested; in supported chat interfaces, prefer native theme-aware UI and inline SVG. Also use to refactor overly text-heavy diagram graphics into visual-first figures, or to learn SVG construction.
---

# Editorial SVG Diagrams — explanation first

**A diagram is a visual sentence, not a document in miniature.** Match the user's demonstrated reference: visual structure carries the idea; supporting prose lives *outside* the figure. Do not mistake more labels, bigger cards, longer descriptions or a giant canvas for higher fidelity.

## Choose the output mode before drawing

- **In a chat with native UI/diagram primitives:** prefer native host layout elements and inline SVG when they create the clearest illustration. Host-managed text, backgrounds, padding and semantic colors can follow the host theme. Use plain text outside the illustration for explanation. Never force the user into a downloadable PNG just to show a diagram in chat. Respect the host's supported component system; do not emit unsupported tags.
- **For a repository, paper, documentation, download, reuse, or user-requested SVG:** create a *real standalone* transparent `.svg`. Treat the output as the small reusable visual portion, not the whole surrounding article. Also supply a PNG preview when useful and an explicitly colored `.dark.svg` for dark surfaces when helpful.
- **For HTML pages with native design tokens:** inline the SVG and inherit `currentColor`/CSS variables or use native UI layouts; if embedding with `<img>`, document theme limitations. A standalone SVG with `@media (prefers-color-scheme: dark)` can follow the browser/OS preference; it does **not necessarily** follow a site's manual theme override. For dependable manual themes use two SVG assets with a theme-controlled source switch.
- **For print/Office/PDF:** export the light SVG as a vector PDF if supported, or a sized PNG fallback. Transparency is still the default in the SVG file; choose a page background in the document, not inside the illustration.

## The mandatory visual-first workflow

1. **Name one visual takeaway.** Write privately: “After seeing the figure, the reader should perceive ____.” Examples: the three directions of SYN/SYN-ACK/ACK; every network header wrapping the preceding data; knowing one location versus having eight possibilities. Verify semantics against source material, code, or explicit assumptions.
2. **Remove prose before drawing.** Put chapter title, definition, caveats, citations, explanations, and conclusion in the *surrounding text*. Keep labels attached to actual shapes, regions, or arrows only. Default visible content: at most ~12 short labels / ~35 words. Each label ideally 1–3 words. These are targets, not grounds to omit indispensable data. If explaining requires several sentences inside the figure, split the figure or write those sentences outside it.
3. **Select a visual metaphor before a box layout.** Prefer position / size / path / containment / sequence / color / changes between states. A grid of text cards is not an explanatory picture. Read [references/visual-patterns.md](references/visual-patterns.md). For complex architecture, choose a true topology, not a 3-card template.
4. **Compose to the content.** Use a tight, meaningful `viewBox` sized to the geometry (e.g., a 760×380 handshake or 770×390 two-row state comparison). Visuals dominate the occupied area; eliminate floating whitespace. No built-in title strip, decorative eyebrow, global white paper rectangle, giant footer, or whole-document card frame. A border/card around the illustration, if warranted, belongs to the host layout, not the standalone SVG.
5. **Draw accurately with restrained visual grammar.** Use SVG primitives (`rect`, `circle`, `path`, `line`, `text`), clean route geometry, 2–4px arrows, enough spacing, consistent radii, blue/teal as default semantic accents. Show all labels at sizes readable at final embedding width. Read [references/svg-construction.md](references/svg-construction.md) when building or teaching.
6. **Handle color and backgrounds intentionally.** **Transparent canvas is the default.** Never add a full-canvas `rect` merely to create a white/paper/dark background. Use neutral strokes/text plus a few meaningful accent fills. For static SVG, use dark text/strokes on light surroundings and light text/strokes in the explicit dark variant; use embedded `prefers-color-scheme` CSS only as progressive enhancement. Check with two different backgrounds. Never assume `currentColor` in an external SVG `<img>` automatically inherits the page theme.
7. **Validate, export, inspect, revise.** Resolve helper paths from the installed skill directory, not the current project folder. For file outputs: run `python scripts/build_examples.py` if regenerating bundled figures, then `python scripts/preflight_svg.py figure.svg` and `python scripts/visual_guard.py figure.svg`. Render PNG via `python scripts/export_svg.py figure.svg --format png --scale 2`, composite preview over light/dark, and **open both images**. Check typography, clipping, contrast, arrowheads, label crowding, explanatory clarity at real display/print size. Fix failures and repeat. The lint scripts cannot replace visual inspection.
8. **Deliver usable assets without unnecessary commentary.** Return SVG and, when relevant, PNG/PDF or variants. Put factual caveats as adjacent prose/captions, not visible text drawn into the SVG. Describe what differs across variants where it matters.

## The style contract (hard defaults)

- **No root background fill** (`<rect width="100%" height="100%" fill="#fff">`, etc.) unless user explicitly asks for a fixed-background image. Keep SVG alpha transparent and allow the destination to own its page color.
- **No gratuitous text as graphics:** no explanatory paragraphs, title/subtitle, glossary, source attribution, legend or outcome prose inside the SVG by default. Semantic `<title>` and `<desc>` are *nonvisual metadata* and should remain.
- **No generic dashboards:** avoid multiple equal cards with filler text and icons if a single arrow, progression or state contrast conveys more.
- **No forced fixed artboard:** fit `viewBox` tightly; prefer shape-to-area and visual balance over defaulting to 960×600.
- **No gratuitous decorations:** borders only to encode an entity, region or intentional separator. Shadows, gradients and random brand palettes are off by default.
- **Not every figure requires an arrow:** the entropy example relies on marked versus possible positions; adding arrows there would confuse the meaning.
- **Respect sequence conventions:** time downward, actors aligned, clear sender/recipient, directional lines; simplified diagonals are valid for chronological messages as in the supplied reference. Use orthogonal routes for complex architectures when that improves readability.
- **No false technical semantics:** distinguish UDP from TCP; do not imply eight actual particles in an eight-position entropy illustration; ensure header nesting is logically accurate and label proportions as schematic if relevant.

## Test the reference, not just SVG validity

Compare the user's desired illustration against the earlier failure with [references/reference-contrast.md](references/reference-contrast.md). The old figure is **not** a style template to copy; it is a regression example. Look at the *same TCP handshake*: three visible messages are the story, not large endpoint cards and paragraphs. When asked to recreate a provided figure, inspect/crop the figure itself rather than importing surrounding page chrome into the art.

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
| `scripts/build_examples.py` | Deterministically rebuild all examples/variants |
| `scripts/preflight_svg.py` | XML/accessibility/portable-resource checks |
| `scripts/visual_guard.py` | Explanation-first text budget and full-background regression gate |
| `scripts/export_svg.py` | PNG/vector PDF export |
| `scripts/preview_themes.py` | Composite previews on light and dark surfaces |

## Accepted regression references

The user accepted three further examples on 2026-10-23. Use these as visual
benchmarks alongside the handshake contrast: [binary search](assets/accepted/binary-search.svg),
[cache hit/miss](assets/accepted/cache-hit-miss.svg), and
[debouncing](assets/accepted/debouncing.svg), each with an explicit dark variant.
Their editable SVGs are preserved from the supplied test archive; the import
manifest records their provenance. Compare the visual mechanism, not identical
styling: shrinking region, diverging paths, or input/output timing.

## Learning mode

When the user wants to *learn* SVG, begin with `assets/starter.svg` or `assets/tcp-handshake.svg`. Explain `viewBox`, coordinate origin, primitives, paths, fills and classes **using a real pictured example**. Give one small edit (change arrow positions, add a fourth message, swap one highlight). Keep tutorial prose outside the SVG. If teaching a specific diagram, show the result as a diagram first, then annotated source excerpts separately.

## Scope relative to other skills

Use broader diagram-design skills for unusual or complicated graph semantics when available. This skill owns the **visual-minimal explainer**, portable SVG source, theming strategy, rendering, and QA. The user did not ask for dashboard layouts, default title cards or an SVG that is secretly a paragraph.
