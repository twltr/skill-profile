# SVG construction: compact visual explanations

This is a practical tutorial for building the compact TCP handshake shown in `assets/tcp-handshake.svg`. Load the actual SVG source while following the steps.

## 1. Define the coordinate system

```svg
<svg xmlns="http://www.w3.org/2000/svg"
     width="800" height="398" viewBox="0 0 800 398"
     role="img" aria-labelledby="handshake-title handshake-desc">
  <title id="handshake-title">TCP handshake</title>
  <desc id="handshake-desc">Client SYN, server SYN-ACK, client ACK.</desc>
  <!-- visual elements -->
</svg>
```

`width`/`height` establish a convenient default aspect ratio, while `viewBox` controls the internal coordinate space. `x` grows to the right and `y` grows downward. The visible SVG has **no page-colored background**. `<title>` and `<desc>` are accessibility metadata, not decorative text on the image.

## 2. Put actors far enough apart to see motion

```svg
<text x="146" y="32" text-anchor="middle">Client</text>
<text x="650" y="32" text-anchor="middle">Server</text>
<path d="M146 56 V357" stroke="#9CA8B0" stroke-dasharray="7 10"/>
<path d="M650 56 V357" stroke="#9CA8B0" stroke-dasharray="7 10"/>
```

The two vertical lifelines are a scaffold. Keep the visual field mostly open; a machine does not need a heavy rectangle.

## 3. Use paths for three movements

```svg
<path d="M146 118 L650 163" stroke="#397DA9" stroke-width="4"
      fill="none" marker-end="url(#arrow-blue)"/>
<path d="M650 190 L146 235" stroke="#0E8981" stroke-width="4"
      fill="none" marker-end="url(#arrow-teal)"/>
<path d="M146 270 L650 315" stroke="#397DA9" stroke-width="4"
      fill="none" marker-end="url(#arrow-blue)"/>
```

Create matching markers once in `<defs>` with IDs that exist and do not collide with other diagrams. Labels `SYN`, `SYN-ACK`, `ACK` should sit above the corresponding strokes without colliding. For ordered exchanges, slight diagonals can reinforce time progression; they are valid here even if architecture diagrams use orthogonal connectors.

## 4. Only two small API cues

Small chips marked `connect()` and `accept()` distinguish calling into the TCP stack from on-wire packets. Do not add an explanatory footer into the canvas saying what these do; explain that in the text alongside the SVG.

## 5. Class-based adaptive paint

The bundled default SVG contains semantic CSS classes with a light palette and a dark override:

```css
.f-ink { fill: #1C2936; }
.s-blue { stroke: #397DA9; }
@media (prefers-color-scheme: dark) {
  .f-ink { fill: #F1F4F6; }
  .s-blue { stroke: #4988B4; }
}
```

This follows the browser/OS `prefers-color-scheme` when honored by the SVG renderer. **It is not equivalent to inheriting a parent ChatGPT app theme.** For inline SVG in a host, prefer styling via the host's actual theme system; when using an external `.svg` in an `<img>`, use the authored light/dark variants if the site offers a manual theme toggle. Most raster/PDF converters render one static scheme; use the explicit variant appropriate to the destination.

## 6. Rebuild and test

From the skill folder:

```bash
python scripts/build_examples.py
python scripts/preflight_svg.py assets/tcp-handshake.svg
python scripts/visual_guard.py assets/tcp-handshake.svg
python scripts/export_svg.py assets/tcp-handshake.svg --format png --scale 2
python scripts/preview_themes.py assets/tcp-handshake.svg --dark assets/tcp-handshake.dark.svg --out handshake-preview.png
```

Open the composite preview. Check arrow direction, readable labels, no text collision, no white rectangle and natural space usage.

## 7. Exercise

Change the second arrow's label to `SYN + ACK` and shift its endpoints 15 SVG units downward. Verify that the label remains separated from the stroke. Then restore the correct original. If the label forces a long paragraph into the drawing, stop and move the explanation to prose.

## Make other figure types

- **Entropy:** 8 slot `<rect>` shapes per row, 1 selected `<circle>` on first row, all candidate circles on second. Keep all circles count-correct.
- **Packet encapsulation:** preserve blue payload identity, add only one new header/trailer per row; align segment widths to communicate composition.
- **OSI:** 7 aligned colored bands and one short protocol exemplar per row; no visible title or prose in SVG.

Do not use SVG as an excuse to reconstruct an entire article out of `<text>` tags.
