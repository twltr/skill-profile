---
name: svg-design
description: Design and refine SVG logos, icons, brand assets and visual graphics for websites and user interfaces. Use for visual identity, icon systems, decorative or animated web artwork and vector refinement. Explanatory diagrams belong to Editorial SVG Diagrams; full page layouts belong to Frontend Design.
metadata:
  skill-type: leaf
  skill-tree: design
---

# SVG Design

**Leaf skill** in Design; reached through its domain or by name.

Start with the graphic's role in the brand or interface. Choose its composition,
silhouette, proportions, typography and color for that setting, preserving an
established visual direction when one exists. Then express the design as clean,
minimal SVG markup. Every element and attribute should earn its place.

This skill owns logos, icon sets, brand assets and decorative or expressive web
graphics. Choose by purpose: a landing page's logo and decorative hero artwork
belong here; a diagram explaining how its product works belongs to
`editorial-svg-diagrams`. Page composition and interface layout belong to
`frontend-design`.

## A small logo decision

**Illustrative brief:** Make a mountain mark that remains recognizable in a
website header and a compact app icon. Begin with the outer silhouette and one
distinctive ridge cutout; omit fine snow lines that vanish when reduced. Check
the mark at both actual sizes and against each intended surface before adding
color or detail. If those uses need different detail levels, make an explicit
small-size variant instead of shrinking an unreadable mark.

Before substantial composition or visual review, assess the model's visual capability
and access to rendered use sizes and surfaces. If **Puppeteer** is available, use
its current phase/model routing for a better-suited author or independent reviewer,
passing the brief, established direction and target sizes. Reuse an active delegation
owner; a small suitable edit can stay direct. The designer's own checks are not
independent acceptance. Missing capability or rendered access leaves that check
open; valid SVG alone does not establish a good design.

## Topic Routing

| Task | Load reference |
|------|---------------|
| Arc flag combinations, common path shapes | [references/path-patterns.md](references/path-patterns.md) |
| Logo design, typography, negative space | [references/logo-techniques.md](references/logo-techniques.md) |
| Icon design, grid systems, pixel alignment | [references/icon-design.md](references/icon-design.md) |
| Gradients, masks, clips, filters, transforms (design decisions) | [references/advanced-techniques.md](references/advanced-techniques.md) |
| Animation (CSS keyframes, stagger, GPU, easing, SVG-specific) | [references/animation.md](references/animation.md) |
| Optimization, sprites, SVGO config | [references/optimization.md](references/optimization.md) |
| Accessibility, browser pitfalls | [references/accessibility-and-pitfalls.md](references/accessibility-and-pitfalls.md) |
| Editing workflow, boolean operations, combining SVGs | [references/editing-workflow.md](references/editing-workflow.md) |

## SVG Skeleton

For a stroked UI icon, start from this structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- content -->
</svg>
```

Adjust `viewBox` to match the design canvas. Omit `width`/`height` attributes to let the SVG scale with its container (add them only when a fixed size is needed).

For logos and web artwork, choose the canvas, fills and strokes from the
composition rather than inheriting the icon defaults.

## Canvas Size Conventions

| Size | Use case | Notes |
|------|----------|-------|
| `0 0 16 16` | Micro icons, favicons | Heroicons micro, GitHub Octicons |
| `0 0 20 20` | Small UI icons, form elements | Heroicons mini |
| `0 0 24 24` | Standard icons (most common) | Lucide, Heroicons outline, Material |
| `0 0 32 32` | Medium icons, navigation | Phosphor uses 256x256 internally |
| `0 0 48 48` | Large display icons | App icons, illustrations |
| Custom | Logos, illustrations | Match the natural aspect ratio |

For standard UI icons, default to 24x24 unless the surrounding icon system uses
another grid. Logos and web graphics use a canvas that fits their composition.

## Shape vs Path Decision

| Use shape primitive when... | Use `<path>` when... |
|---|---|
| The shape is a basic geometric form | The shape has curves, complex outlines |
| Readability matters (a circle should look like `<circle>`) | You need to minimize element count |
| You need to animate individual properties (r, cx, cy) | Combining multiple shapes into one element |
| The shape will be programmatically modified | Exporting from design tools (paths are universal) |

## Styling Defaults

Set these on the root `<svg>` element to avoid repetition on children:

| Attribute | Icon default | Logo default | Why |
|-----------|-------------|--------------|-----|
| `fill` | `none` | varies | Icons are typically stroked, logos are filled |
| `stroke` | `currentColor` | `none` or `currentColor` | Inherits text color from parent |
| `stroke-width` | `2` (on 24x24) | varies | Consistent weight across icons |
| `stroke-linecap` | `round` | `round` or `butt` | Rounded ends look cleaner at small sizes |
| `stroke-linejoin` | `round` | `round` or `miter` | Prevents sharp spikes at joins |

**`currentColor` is your friend.** It lets the SVG inherit whatever color the parent element has, making icons themeable with zero extra CSS.

## Stroke-Width Relative to ViewBox

`stroke-width` is in viewBox units, not pixels. Always set relative to your canvas dimensions:

| viewBox | Typical stroke-width | Visual result |
|---------|---------------------|---------------|
| 16x16 | 1.5 | ~9.4% of canvas |
| 24x24 | 2 | ~8.3% of canvas |
| 32x32 | 2-2.5 | ~6.3-7.8% of canvas |
| 48x48 | 3 | ~6.3% of canvas |
| 256x256 | 16 | ~6.3% of canvas |

## When to Convert Shapes to Paths

**Convert when:**
- Combining multiple shapes into a single compound path (boolean operations)
- You need the shape as part of a larger path composition
- Distributing to environments that only support `<path>`
- Optimizing for minimal DOM elements

**Keep as shapes when:**
- Code readability matters (a `<circle>` is self-documenting)
- You need to animate specific properties (animating `r` on a circle is cleaner than animating path data)
- The SVG will be programmatically modified

### Rounded rect-to-path template

The arc parameters here are error-prone to derive. Use this as a reference:

```xml
<!-- <rect x="2" y="2" width="20" height="20" rx="3" /> becomes: -->
<path d="M 5 2 h 14 a 3 3 0 0 1 3 3 v 14 a 3 3 0 0 1 -3 3 h -14 a 3 3 0 0 1 -3 -3 v -14 a 3 3 0 0 1 3 -3 Z" />
```

## fill-rule: evenodd vs nonzero

Use `evenodd` when you have compound shapes with holes. It's simpler because you don't need to worry about winding direction:

```xml
<!-- Donut using evenodd (direction doesn't matter) -->
<path fill-rule="evenodd" d="
  M 12 2 A 10 10 0 1 1 12 22 A 10 10 0 1 1 12 2 Z
  M 12 7 A 5 5 0 1 1 12 17 A 5 5 0 1 1 12 7 Z
" fill="black" />
```

With `nonzero` (default), the inner circle must wind in the opposite direction to create the hole.

## Logo Design Process

When creating logos (not icons), follow this process:

0. **Resolve only a material gap in the brief.** Reuse a supplied brand direction,
   name, audience, use cases and reference. If one missing choice would materially
   change the design, ask a short question using the current host's supported
   interaction. Use a sensible reversible default for secondary choices; never
   assume a particular question tool or require a mood-board interview.

1. **Explore multiple metaphors, not multiple layouts of one metaphor.** Conceptual diversity matters more than layout variations. Follow the full ideation process in [references/logo-techniques.md](references/logo-techniques.md), which covers domain-specific brainstorming, category diversity requirements, and cliche avoidance.
2. **Guarantee structural variety.** Every logo set must span multiple *categories* of approach, not just multiple metaphors within the same style. Include at least one from each column when presenting 5+ options: a typographic/wordmark approach, a symbolic icon, an abstract geometric mark, and a letterform-meets-metaphor hybrid. See the category diversity table in [references/logo-techniques.md](references/logo-techniques.md).
3. **Preview through the available host.** When progressive comparison will help,
   use this skill's `assets/preview.html` and the structure in
   [references/editing-workflow.md](references/editing-workflow.md). Show or inspect
   the preview through a viewer supported by the current host; do not assume a
   browser, shell command or foreground window is available. If no viewer can
   render it, state the boundary and provide the SVG files and a rendered preview
   where supported. Never claim an unobserved preview was visually verified.
4. **For colored logos, always create a `-dark.svg` variant.** Dark navy edges (#1E3A5F) that look great on white disappear on dark backgrounds. Dark variants need lighter edges (#4B8BBE), lighter rings (#3B6B8A), and off-white centers (#E2E8F0).
5. **Plan your vertical budget before drawing.** On a 32x32 canvas with 3 stacked elements, you have ~30 usable units. Sketch the vertical distribution first (e.g., box=12, gap=2, layer=5, gap=2, layer=5) to avoid clipping at viewBox edges.

## Anti-Patterns

| Don't | Do instead |
|-------|-----------|
| Hardcode `width="24" height="24"` without `viewBox` | Use `viewBox` always; add width/height only if needed |
| Set `fill="none"` on a `<g>` group | Set fill on individual elements or the root `<svg>` |
| Use `px` units inside SVG | SVG coordinates are unitless; they map to viewBox |
| Include editor metadata (`<sodipodi:*>`, `<inkscape:*>`) | Strip all editor cruft |
| Use `<text>` for logo wordmarks in distributed SVGs | Convert text to paths for portability |
| Nest transforms three levels deep | Flatten transforms into path coordinates |
| Use `xlink:href` | Use `href` (xlink is deprecated) |
| Forget `xmlns` on standalone SVG files | Always include `xmlns="http://www.w3.org/2000/svg"` |
| Use decimal precision beyond 2-3 places for icons | Round to 2 decimals for icons, 3 max for complex art |

## Cross-References

- Surrounding website or interface design is not this skill's work. Hand it
  back to whoever asked for the graphic, with the graphic's role and size
  constraints, and follow the established typography, colors and visual
  hierarchy or the project's existing design system meanwhile.
- If `editorial-svg-diagrams` is available, use it for figures that explain
  concepts, relationships, processes or systems. Otherwise, keep this skill's
  output focused on brand and interface graphics, and explain the unavailable
  diagram capability if the requested outcome depends on it.
