# Exporting and Embedding Standalone SVG Diagrams

## Preferred deliverables

- **Canonical:** editable vector `.svg` with live text, accessible `<title>` and `<desc>`, no linked fonts/assets.
- **Preview / web fallback:** anti-aliased `.png` rendered at 2x or fixed pixel width.
- **PDF vector figures:** `.pdf` export when required for LaTeX print/publish or office document pipelines with poor SVG support. Confirm font substitution and print scale.

## Typical targets

| Destination | Primary file | How to embed | Notes |
|---|---|---|---|
| GitHub README | PNG for broad compatibility, SVG when supported | `![Diagram](docs/diagram.svg)` or `.png` | Prefer relative repository paths; verify hosting's SVG sanitization/support |
| Web documentation | SVG | `<img src="diagram.svg" alt="...">` | Keep caption/alt text; don't assume title alone satisfies alt text |
| Markdown knowledge docs | SVG or PNG | `![...](diagram.svg)` | Renderer-specific: verify; use PNG fallback |
| PowerPoint/Word | SVG when supported; else high-res PNG | Insert image normally | Verify font substitution and clipping on exported PDF |
| LaTeX / academic paper | PDF vector or PNG fallback | `\includegraphics[width=\linewidth]{diagram.pdf}` | Export with CairoSVG/Inkscape; verify final PDF at target size |
| PDF report | Vector PDF or PNG | Insert into authoring app before exporting | Inspect produced PDF; don't assume a PDF generator supports SVG natively |

## Size and physical legibility

SVG coordinates are not printing points. Example: a 22 px source label in a 960-wide viewBox used at 480 physical px is effectively 11 px. In a two-column paper's single column (~85-90 mm), complex 960-wide SVGs become illegible. For a single narrow column, prefer **520 px viewBox with 18-22 px labels and only 3-5 nodes**. For full-page figures (150-180 mm) 960 px viewBox often works if labels are >=20-24 px.

Before delivering, preview at actual intended width, not just a 4K monitor zoomed in. Avoid line strokes thinner than ~0.7 pt once printed. Grayscale and monochrome exports must still communicate arrows/labels.

## Commands

Resolve `diagram_skill_dir` to the absolute directory containing the loaded
`SKILL.md`. Keep the diagram and output paths relative to the project, or pass
absolute paths. Run with Python 3:

```bash
python3 "$diagram_skill_dir/scripts/preflight_svg.py" my-diagram.svg
python3 "$diagram_skill_dir/scripts/export_svg.py" my-diagram.svg --format png --scale 2
python3 "$diagram_skill_dir/scripts/export_svg.py" my-diagram.svg --format png --width 1800 --out preview.png
python3 "$diagram_skill_dir/scripts/export_svg.py" my-diagram.svg --format pdf --out figure.pdf
```

`scripts/export_svg.py` uses Python CairoSVG when importable, or Inkscape CLI when CairoSVG cannot be imported. A CairoSVG rendering error is reported and stops the export; it does not silently switch renderers. The script performs preflight automatically. PNG image pixels are not an SVG substitute; preserve the original source. PDFs preserve vector shapes in typical cases, but embedding fonts and font substitution depend on export backend and environment.

## Team repository organization

A reasonable layout:

```text
docs/
  diagrams/
    README.md                 # factual sources and explanation
    transport-handshake.svg  # editable source of truth
    transport-handshake.png  # reproducible preview / compatibility
```

For regeneration, commit SVG and exporter command in documentation; avoid manually drifting SVG/PNG versions. If sources are generated programmatically, commit the script, not only the render. Keep diagrams close to relevant architecture docs or modules rather than creating a parallel documentation universe.

## Security and portability

Treat imported SVG as untrusted markup. Do not execute embedded scripts or fetch remote assets. The included preflight rejects script/foreignObject and external references; it is a *structural linter*, not a complete hostile-input sanitizer. Use a hardened sanitization and rendering environment for attacker-controlled files. Keep generated SVG self-contained for stable CI and reproducible papers.
