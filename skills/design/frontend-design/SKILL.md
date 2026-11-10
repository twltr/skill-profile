---
name: frontend-design
description: Visual direction for building a new website or app interface or reshaping an existing one — palette, typography, layout, motion and page copy chosen from the brief and its subject rather than templated defaults. Plans a compact token system, reviews the plan against the looks generated design keeps falling into, then builds and critiques the rendered result.
license: Complete terms in LICENSE.txt
metadata:
  skill-type: leaf
  skill-tree: design
---

# Frontend Design

**Leaf skill** in Design; reached through its domain or by name.

Generated interfaces cluster around a handful of looks that appear whatever the
subject, so a page can be competent and still read as a template. Distinctive
choices come from the brief's own subject — its materials, artifacts, audience
and vernacular — and from checking the plan against those defaults before any
code exists. Design from the actual brief and existing product; do not invent a
client's history, rejected concepts, budget or appetite for risk. Where the brief
pins down a direction, follow it exactly, even when it asks for a common look.

## A small worked direction

**Illustrative brief (fictional):** A ceramics studio wants a collection page.
The supplied photographs show warm clay bodies and varied glazes.

The first plan that comes to mind is a cream background, a high-contrast serif,
a terracotta accent and "01 / 02 / 03" markers over each collection. The review
catches it: that is the first calibration default below, and the collections have
no order for numbers to encode. Revised plan:

```text
Color   Slip #FAFAF8 · Shelf #E4E2DD · Iron #2A2927 · Celadon #4A6658 (links only)
        — the glazes in the photographs carry the color
Type    one humanist sans, two weights; captions name clay body and firing
Layout  photographs first, left-aligned captions, uneven two-column rhythm
        [ Tableware ......................... 14 pieces ]
        [ large photo      ][ photo ]
        [ photo ][ large photo      ]
Principle  nothing on the page competes with a glaze
```

**Check:** at a 360 px viewport each piece keeps its silhouette uncropped, name,
price and purchase action stay together, and keyboard focus is visible. Celadon
was darkened from a first pick of #7F9C8E (2.9:1 on Slip) to reach 6.0:1, because
links are text. The
direction follows the supplied work instead of a generic studio aesthetic.

## Ground it in the subject

If the brief does not say what the product or subject is, pin it down before
designing: one concrete subject, its audience and the page's single job, stated
as a proposal the user can correct. Use what you know of the person's
preferences, what they are building and earlier designs as a hint. The subject's
world is where distinctive choices come from — a toy for children aged 8–11 looks
nothing like a dashboard for financial analysts. Build with the brief's real
content throughout.

## Design principles

- **The hero opens with the most characteristic thing in the subject's world**,
  in whatever form fits: a headline, an image, an animation, a live demo. A big
  number with a small label, supporting stats and a gradient accent is the
  default treatment; use it only when it truly is the best option.
- **Typography carries the personality.** One family or two; if two, make them
  clearly distinct. Choose them for this project, not the families you would
  reach for anywhere, and set a clear scale with intentional weights, widths and
  spacing in the tradition of *The Elements of Typographic Style*. Keep lines
  under about 80 characters; serif body text tolerates slightly longer lines and
  wants slightly more line-height than sans.
- **Avoid the commonest typographic tells** of a generated page: one word of a
  headline accented in italic, bold or color; all-caps labels; labels above
  content that needs none.
- **Structure is information.** Borders, numbering, eyebrows, dividers and labels
  should encode something true about the content. Numbered markers belong to a
  real sequence such as a process or a timeline, not to any three items.
- **Motion that nobody triggered is spent sparingly**, to draw attention: one
  orchestrated page-load sequence or reveal lands better than scattered effects.
  Fade-and-slide-up on every section and hover transitions on every card are the
  generic default. Motion that answers a person's action — opening, expanding,
  confirming — is welcome when it shows what changed.
- **Match complexity to the vision.** Maximalist directions need elaborate
  execution; minimal ones need precision in spacing, type and detail.

## Process: plan, review against the brief, build, critique

For calibration, generated design currently clusters around these traits:

1. a warm cream background (near #F4F1EA) with a high-contrast serif display and
   a terracotta or warm-clay accent — often near #D97757, the accent of
   Anthropic's own Claude interface, so on someone else's brief it reads as a tell;
2. a near-black background with a single bright acid-green or vermilion accent;
3. a broadsheet layout with hairline rules, zero border-radius and dense
   newspaper-like columns;
4. the SaaS card kit: content chopped into identical rounded cards, one radius on
   everything, the same soft grey shadow under each, gradient washes as decoration;
5. template chrome: a tracked-out all-caps eyebrow above every heading, meta
   strings joined with middle dots, "WORD — fragment" labels, tinted near-black
   (#0B0B0B, #111) standing in for black, monospace for small data labels, and
   "→" appended to link and button text.

Each is legitimate for some brief, but they are defaults rather than choices.
Where the brief leaves an axis free, do not spend that freedom on one of them.

Work in two passes. First, write a compact plan from the brief:

- **Color:** the core palette as 4–6 named hex values.
- **Type:** the typefaces and their roles.
- **Layout:** a one-sentence concept plus an ASCII wireframe; compare
  alternatives this way, and state alignment (left, centered, justified).
- **Principles:** what makes this page specific to its subject.

Then review the plan against the brief. Run a similar prompt in your head: if a
part of the plan is what you would produce for any similar page, revise it and
say what you changed and why. Build only from the revised plan, deriving every
color and type decision from it.

In the CSS, watch selector specificity: a class such as `.section` and an
element-level rule such as `.cta` easily cancel each other out, most often in the
padding and margin between sections.

## Restraint and self-critique

Spend boldness in one place: let one element be memorable, keep everything
around it quiet, and cut decoration the brief does not need. Build to a quality
floor without announcing it — responsive down to mobile, visible keyboard focus,
reduced motion respected, sufficient contrast, a harmonious palette. Before
finishing, take a look in the mirror and remove one accessory.

Judging a design needs its rendered states. Take screenshots at the sizes and
themes that ship when the environment allows it; a picture shows what the source
cannot. If you cannot see rendered output, say so: passing source checks do not
show that the design works, so visual acceptance stays an open check. Your
critique of your own work is not independent acceptance; for substantial work the
Puppeteer core skill (agent delegation, not the browser library) can hand the
authoring or an independent visual review to a better-suited agent. Where you
have somewhere to keep notes between passes, record what you tried, so the next
pass does something new.

## Words in the design

Words are design material: they make the interface easier to understand and use.
Before writing, ask what the design needs to say and how that helps the person
find their way.

- Write from the user's side of the screen: people manage notifications, not
  webhook config. Describe what something does in plain terms instead of selling
  it; specific beats clever.
- A control says what happens: "Save changes", not "Submit". An action keeps its
  name through the flow — "Publish" produces "Published".
- Errors say what went wrong and how to fix it, in the interface's voice, without
  apologizing; an empty screen invites the next action.
- Plain verbs, sentence case, no filler, tone matched to brand and audience. Each
  element does one job.

Product microcopy that deserves its own pass — error and empty-state sets,
confirmation dialogs, copy in another language — is a separate microcopy method;
here the aim is page copy that does not read as templated.
