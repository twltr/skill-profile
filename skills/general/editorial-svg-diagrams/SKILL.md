---
name: editorial-svg-diagrams
description: "Create, revise, export and teach standalone SVG diagrams for architecture, protocols, processes, research papers, reports, READMEs, slides and PDFs. Use for layer stacks, sequences, encapsulation, component maps and converting existing diagrams into editable SVG with verified PNG/PDF exports. Automatic selection enabled; explicit use also supported."
---

# Editorial SVG Diagrams

Produce **real, self-contained `.svg` files**, not rasterized approximations, screenshots, UI-specific markup, or diagram-code pretending to be SVG. Use semantic content and exact geometry to create images that can be placed in a paper, README, slide, report, or project documentation. Favor legibility and precision over decoration.

## Operating contract

1. **Understand the actual system.** Identify subject, audience, source of truth, required relationships, desired destination, and language. Match in-diagram text to the user's/document's language (German, English, etc.). For a codebase diagram, inspect repository artifacts when accessible; otherwise label every assumption. For a conversion, preserve all material relationships and labels; do not invent. Do not ask for details already available; make reasonable, disclosed defaults.
2. **Choose the correct visual grammar.** Use a layer stack for abstraction layers; sequence for ordered exchanges; nested strips for encapsulation; architecture for components + interfaces; process/decision for conditions. If user supplied an existing diagram type, retain it. Read [references/visual-patterns.md](references/visual-patterns.md) for placement and semantic rules.
3. **Choose an export target** before sizing. Default to a portable `960x600` or content-specific `viewBox` on a light paper background, with a PNG preview. For narrow paper columns simplify or compose a separate narrower variant. Read [references/embedding-and-formats.md](references/embedding-and-formats.md) when embedding/exporting.
4. **Draw with deliberate SVG geometry.** Use `<svg viewBox>`, `<title>`, `<desc>`, `<defs>`, `<g>`, `<rect>`, `<line>`, `<path>`, `<circle>`, and `<text>`. Coordinates determine layout; the order determines paint layering. Use explicit backgrounds, reusable arrow markers, consistent edge attachments, restrained color, and adequate typography. Read [references/svg-construction.md](references/svg-construction.md) to build or teach from first principles.
5. **Create the file and verify it.** Resolve `diagram_skill_dir` to the directory containing this loaded `SKILL.md`; use its absolute path, not the project's working directory. Write the standalone `.svg` into the requested output folder. Run `python3 "$diagram_skill_dir/scripts/preflight_svg.py" path.svg`; fix structural failures. Run `python3 "$diagram_skill_dir/scripts/export_svg.py" path.svg --format png --scale 2` and, if requested, `--format pdf`. Open and visually inspect the rendered result; correct clashes, clipping, scale, stroke continuity, arrow tips, contrast, and actual terminology. The script checks structural correctness; it cannot replace visual inspection. If no supported renderer is available, report that boundary and leave render verification open; do not claim an unrendered asset is verified.
6. **Deliver both semantics and artifacts.** Return links to verified SVG and optionally PNG/PDF. Mention the intended embedding width, any assumptions, and whether source content was verified. If asked how it was built, refer to the concrete SVG elements and geometry in the included examples rather than giving only a vague tool description.

## Target aesthetic

Model the clear in-chat technical diagrams shown in the examples: dark jewel-tone rows for distinct protocol layers, lighter paper outside, small disciplined labels, strong visual hierarchy, and soft rounded geometry. This is a design direction, **not a dependency on ChatGPT-specific UI components**.

- **Structure:** A short eyebrow (optional), one descriptive heading, and one readable diagram. Use whitespace to group; add a caption only if it explains ambiguity or assumptions.
- **Palette:** Prefer paper `#F7F9FC`, ink `#172738`, muted `#566779`, rule `#D5DFE7`; blue `#356F9F` for request/application, teal `#237C77` for transport/exchange, green `#3E805C` for routing/network, ochre `#A67637` for media. Choose one lead/accent, with colors tied to meaning; do not use every color in every graphic. Dark output must be explicitly requested or contextually appropriate.
- **Cards:** 8-12 px radii for substantial blocks; 4-6 px for chips. Fine 1-1.5 px borders; flat surfaces rather than drop shadows, glows, or neon gradients.
- **Text:** Use common local sans-serif fallbacks (`Arial`, `Helvetica`, `sans-serif`) for portability; monospace only for IP addresses, ports, commands, IDs, and code. Primary text must survive physical reduction; target >=9 pt at its real output size (>=10 pt preferred). Do not put long body prose inside a diagram.
- **Grid:** Establish margins and baselines before nodes. Use 8 px spacing rhythm with 4 px refinements; preserve equal row heights, gutters, alignment, and consistent visual weight. Treat viewBox as an internal coordinate system, not fixed printed size.
- **Arrows:** Signal direction and causality. Align ports/attachments deliberately. Use orthogonal or horizontal routed arrows for component flow; a conventional message arrow for sequences. Prefer 2 px strokes and explicit `marker-end` arrowheads. Draw lines under foreground blocks, not through labels. Label mask backgrounds when connectors pass behind text.
- **Density:** Aim for 3-9 substantive items per frame. When labels shrink or arrows cross confusingly, split into overview and detail. Never cram everything into a single figure.
- **Accuracy:** A TCP SYN is not an application message; UDP has no handshake; controls and security boundaries must not be inferred. A diagram must remain factually correct even when simplified.

## Portable SVG requirements

- Root must declare `xmlns="http://www.w3.org/2000/svg"`, meaningful `viewBox`, `role="img"`, `aria-labelledby="..."`, unique `<title id>` and `<desc id>`. IDs must be unique and in-document references resolvable.
- Prefer **standalone SVG 1.1-compatible** constructs. Avoid `<foreignObject>`, scripts, external images/fonts/stylesheets, animations, external URLs, browser-only filters and CSS layout. Avoid emoji/icon fonts; render symbols as simple vector paths if needed.
- Use local, explicit fills/strokes and escape XML special characters in generated text. `<text>` stays editable and selectable. Don't convert text to paths unless an output tool absolutely requires it, and then also preserve an editable source.
- Background: solid light paper for documents; use transparent only on request. Background should not be transparent by accident because different PDF/dark readers will render it differently.
- Do not disguise unsupported rendering, convert to PNG as the only deliverable, or deliver unverified assets.

## How to learn or recreate the technique

Read [references/svg-construction.md](references/svg-construction.md), then inspect the bundled examples as actual SVG source. Begin by changing node text and positions in `assets/starter.svg`. Recreate the layer stack and TCP handshake in `assets/osi-layers.svg` and `assets/tcp-handshake.svg`. The tutorial includes viewBox coordinates, primitive markup, arrow markers, and failure checks. When the user explicitly asks to *learn*, show the construction steps and point to concrete source lines, then give one small exercise to modify.

## Bundled references and reusable assets

| Resource | Purpose |
|---|---|
| [references/svg-construction.md](references/svg-construction.md) | Learn SVG geometry and build a handshake diagram from scratch |
| [references/visual-patterns.md](references/visual-patterns.md) | Choose layout grammar for layers, sequences, encapsulation, architectures, and flows |
| [references/embedding-and-formats.md](references/embedding-and-formats.md) | Insert SVG into Markdown, HTML, LaTeX, Office, and PDFs; export sizing |
| `assets/icon.svg` | Small reusable skill icon drawn entirely with SVG |
| `assets/starter.svg` | Minimal accessible SVG skeleton with arrow marker |
| `assets/osi-layers.svg` | Colored OSI layer stack with consistent bands |
| `assets/tcp-handshake.svg` | Client/server lifelines, SYN/SYN-ACK/ACK, application boundary |
| `assets/packet-encapsulation.svg` | Nested packet contents through transport/IP/Ethernet |
| `assets/codebase-architecture.svg` | Generic clean codebase/service architecture |
| `scripts/preflight_svg.py` | Inspect structure, references, portable SVG elements, and approximate geometry |
| `scripts/export_svg.py` | Validate then export to PNG or vector PDF (CairoSVG/Inkscape) |

## Relationship to other diagram tools

This skill owns semantic layout selection, the portable `.svg`, educational SVG construction, export presets and image-level QA. Use the bundled visual patterns with the verified source model. Mermaid/draw.io/Excalidraw can supply relationships; preserve required notation and automated consumers when converting them. The final SVG uses deliberate geometry without requiring an HTML wrapper or another diagram skill.

## Quality gate before delivery

- Reader can state the main relationship in 5 seconds; no ambiguous labels or implied invented links.
- Color has meaning; typography/contrast readable at target size, including grayscale print when needed.
- Arrow endpoints, return directions, labels, and time order verified.
- No text outside viewBox, cut arrowheads, hidden lines, collisions, overflow, or dependency on remote assets.
- Validates and renders without network access; visually inspected PNG at target scale.
- Source SVG and preview (if appropriate) share the same content; no unreported raster-only edits.
