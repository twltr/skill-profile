# Constructing SVG Diagrams from First Principles

This guide teaches the exact *public* SVG technique behind clean technical chat-style illustrations, independent of any proprietary UI renderer. The resulting `*.svg` works as a standalone vector image in other systems.

## 1. Start with a coordinate canvas

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     width="960" height="600" viewBox="0 0 960 600"
     role="img" aria-labelledby="tcp-title tcp-desc">
  <title id="tcp-title">TCP handshake</title>
  <desc id="tcp-desc">Client sends SYN, server responds SYN-ACK, client acknowledges.</desc>
  <rect width="960" height="600" fill="#F7F9FC" />
  <!-- elements go here -->
</svg>
```

`viewBox="min-x min-y width height"` defines a coordinate system. `x` runs right; `y` runs down. Setting a fixed `width` and `height` is optional, but convenient for predictable standalone previews. Scaling keeps vector shapes sharp. For narrow printed figures, reduce semantic density or recreate at narrower viewBox; don't simply shrink small letters.

## 2. Make a card with shape + text

```xml
<rect x="48" y="96" width="256" height="100" rx="12"
      fill="#E9F2F8" stroke="#356F9F" stroke-width="1.5" />
<text x="68" y="135" font-family="Arial, Helvetica, sans-serif"
      font-size="24" font-weight="700" fill="#172738">Client</text>
<text x="68" y="165" font-family="Arial, Helvetica, sans-serif"
      font-size="18" fill="#566779">192.168.1.20</text>
```

Place text using a *baseline*, not a top-left coordinate. Use `text-anchor="middle"` for labels centered on a known `x`. Set `dominant-baseline` only when checked with your actual SVG renderer. Use `&amp;`, `&lt;`, `&gt;` to escape XML characters. Avoid wrapping text by CSS; manually create two `<text>` lines or `<tspan x="..." dy="...">`.

## 3. Create arrows deliberately

Define the marker once:

```xml
<defs>
  <marker id="tcp-arrow" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 1 1 L 9 5 L 1 9 Z" fill="#356F9F" />
  </marker>
</defs>
```

Then reference it from a route:

```xml
<path d="M 320 250 H 640" fill="none" stroke="#356F9F"
      stroke-width="3" marker-end="url(#tcp-arrow)" />
```

In path syntax `M` means move, `L` line, `H` horizontal, `V` vertical; `Q` quadratic curve, `C` cubic curve. Arrows should stop at a surface boundary, not bury their tip behind a box. The marker should point to the recipient. For return direction, draw the path in reverse, not just change label wording. Draw routes before foreground nodes when they would otherwise intersect.

## 4. Put a label above a line

A connector through bare text is ugly. Use a small paper-colored label mask if text is placed on top of a route:

```xml
<rect x="430" y="219" width="100" height="32" rx="5" fill="#F7F9FC" />
<text x="480" y="241" text-anchor="middle" font-size="17"
      font-weight="700" fill="#172738">SYN</text>
```

Position against a measured segment and use a clear 6-8 px breathing gap. Do not use a large blank mask that hides meaningful geometry.

## 5. Build a sequence diagram step by step

**Example geometry:** viewBox `0 0 960 600`; client anchor `x=220`, server anchor `x=740`; common horizontal margins `56`.

1. Draw title, explanatory subheading, client/server cards at `x=100` and `x=620`.
2. Draw dashed lifelines with `stroke-dasharray="6 8"` from y=`180` to y=`500` at x=`220` and x=`740`.
3. Put `SYN` on y=`265` from `(220,265)` to `(740,265)`, arrow to server.
4. Put `SYN + ACK` on y=`365` from `(740,365)` to `(220,365)`, arrow to client (different hue).
5. Put `ACK` on y=`465` from `(220,465)` to `(740,465)`, arrow to server.
6. Label numbering, emphasize transport vs application separation, and optionally add a completion bar at bottom. `accept()` returns a connected socket after the connection handshake; it is not a TCP packet.
7. Check the semantics before decorating. See `assets/tcp-handshake.svg` for a fully composed result. Its spacing differs slightly to balance captions and callouts.

For a layer stack, replace lifelines with equal-height rounded rows. Number layers 7 down to 1, assign background hues deliberately, and left-align descriptions. Inspect `assets/osi-layers.svg`.

For packet encapsulation, show **composition** rather than arbitrary sequential cards: each successive row must explicitly contain the previous unit as payload; do not suggest that Ethernet encapsulates IP without its own header/trailer. Inspect `assets/packet-encapsulation.svg`.

## 6. Compose for readability

- Use an 8 px layout rhythm; plan margins, row/card heights and centerlines before writing markup.
- Establish hierarchy with exactly three levels: title (28-36 px), node names (21-25 px), small labels (14-19 px), adjusted for target display width.
- Use solid fills and subtle borders. Heavy gradients, drop shadows, multiple unrelated fonts, decorative doodles, and packed legends are seldom useful for technical diagrams.
- Use colors by semantic category; arrows retain meaning without color through arrowheads and labels.
- Prefer fewer shapes. If paths cross or labels become tiny, split the diagram.

## 7. Learn by modifying

Start with `assets/starter.svg`; change text, positions and fill colors. Next copy `assets/tcp-handshake.svg`, swap endpoint names/IPs, and add a fourth message. Observe how the arrow marker, lifeline and y-order change. After every edit, validate and re-render:

```bash
python scripts/preflight_svg.py assets/tcp-handshake.svg
python scripts/export_svg.py assets/tcp-handshake.svg --format png --scale 2
```

A diagram rendered once is only an initial draft. View the PNG at document size and check the meaning, clipping, and legibility.
