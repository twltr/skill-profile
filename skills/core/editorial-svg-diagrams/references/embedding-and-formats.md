# Transparent SVG, theme behavior, and embedding

## Important distinctions

**Native chat UI:** A host can render layout components and inline SVG within its actual theme. If host controls have theme-aware text, surfaces, borders and spacing, use them directly. This is why a ChatGPT-native explanatory widget may look more naturally integrated than a portable file.

**Standalone `.svg` in `<img>`:** The SVG is a separate image document; it does **not automatically inherit arbitrary CSS variables, `currentColor`, or the site's manually selected theme**. CSS `@media (prefers-color-scheme: dark)` inside the SVG often reacts to the browser/OS preference but may be independent of the site's light/dark toggle, renderer or SVG embedding method.

**Reliable manual theme:** Generate explicit `.svg` light and `.dark.svg` variants and switch the `<img src>` using the host app's actual theme state or theme class. A `<picture>` with `media="(prefers-color-scheme: dark)"` works for OS/browser preference when the site follows it:

```html
<picture>
  <source srcset="figure.dark.svg" media="(prefers-color-scheme: dark)">
  <img src="figure.svg" alt="Description of key relationship">
</picture>
```

For an app with a manual theme stored independently of OS preference, update `src` from that theme state; do not claim `<picture>` solves the manual override.

## Transparent background as a contract

All bundled `.svg` files have no background rectangle and no full-viewBox dark/light fill. This is deliberate: the surrounding ChatGPT, Markdown, paper or slide canvas owns the background. Text and guide colors do need a compatible foreground palette; transparency by itself **does not make an SVG theme-aware**.

For a paper use the light SVG on the paper. For a dark deck use `.dark.svg` or recolor an inline SVG from host design tokens. PNG previews can be composited against either background **without altering the original SVG**.

## Embedding targets

| Destination | Delivery | Detail |
|---|---|---|
| Chat UI | Native host components / inline SVG | Theme from the host; keep prose outside figure |
| GitHub README | `.svg` (plus optional `.png`) | Relative link `![...](docs/figures/example.svg)`; README renderer may not follow app theme |
| Website / HTML docs | Theme-aware inline SVG or light/dark asset switch | Use `<img>` + CSS/theme logic, or `<picture>` for OS preference |
| Academic papers / LaTeX | Light variant as vector PDF or PNG | `\includegraphics[width=\linewidth]{figure.pdf}` |
| Word / PowerPoint | SVG if tool supports it, else PNG | Inspect final export at target size |
| Reports / slides | Inline SVG or vector PDF | Put figure title and explanatory caption in document layout |

## Formulas

Prefer the destination's own math rendering for formulas in running text, and
verify it on the actual destination: Markdown itself defines no math syntax
(CommonMark has none), so support is a host feature.

| Destination | Native math (checked 2026-11-11) | Otherwise |
|---|---|---|
| GitHub Markdown | `$…$` inline, `$$…$$` or a `math` fenced block; rendered with MathJax. Use the `` $`…`$ `` inline form when the expression clashes with Markdown syntax. [Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) | n/a |
| GitLab Markdown | Same delimiters; rendered with KaTeX, which supports a subset of LaTeX. [Docs](https://docs.gitlab.com/user/markdown/) | n/a |
| npm package page, other Markdown viewers | No documented support found | Single-line notation in a code span or block, or a figure |
| LaTeX, Word, slides | The document's own equation tools | n/a |

Draw the formula as a figure when its terms need labels or no native rendering
exists. A hand-written SVG carries single-line notation reliably; for built-up
layout use a TeX-to-SVG renderer such as the `tex2svg` tool in
[MathJax's Node demos](https://github.com/mathjax/MathJax-demos-node), and keep
the TeX source with the figure, because the output is outlines, not editable
text. That tool was identified from its documentation, not run for this skill.

## Output dimensions and text

Fit the SVG's `viewBox` to the actual content. A wide 820×350 colored band figure becomes illegible at 8cm print width; in narrow columns reduce nodes and labels rather than squeezing. Test at actual expected final insertion width; 16–22 SVG-unit text sizes are good starting points but physical size matters. Preserve editable `<text>` and never require remote font downloads.

## Useful commands

```bash
python scripts/preflight_svg.py figure.svg
python scripts/visual_guard.py figure.svg
python scripts/export_svg.py figure.svg --format png --scale 2
python scripts/export_svg.py figure.svg --format pdf --out figure.pdf
python scripts/preview_themes.py figure.svg --dark figure.dark.svg --out theme-check.png
```

Python requirements for previews: `cairosvg` and `Pillow` (PIL). The PDF/PNG exporter also supports Inkscape as a fallback where noted.

SVG is the source of truth. PNG and PDF are generated outputs, not substitutes for a structurally editable original. `preflight_svg.py` is not a hostile-input sanitizer; untrusted imported SVG needs sandboxing/sanitization outside this skill.
