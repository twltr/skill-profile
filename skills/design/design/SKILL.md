---
name: design
description: Entry point for design decisions — how an interface looks, reads and moves; use it before acting, and alongside software engineering when the design is built in code. Covers layout and visual direction, themes and design tokens, logos and icons, animations and transitions, UX copy such as button labels, error messages and empty states, developer handoff specs, and design critique or accessibility review, even when the user only says "make this prettier", "this looks off" or "what should this button say". Not for system or architecture figures, slide decks, or code changes that raise no design question.
metadata:
  skill-type: domain
  skill-tree: design
---

# Design

**Domain skill** for Design. If the child a request needs is missing, say which
one and keep the request open rather than imitating it.

Design requests share vocabulary — "make it look better" can mean a layout, a
logo, an animation or a button label — so separate design skills competed for
the same requests and the wrong one often won. This domain is the single entry:
it decides what is being made or judged and loads the one method that owns it.

## A request, routed

**Request:** "the pricing page feels cheap and the 'Go' button is confusing"

Two jobs: the page's visual direction belongs to Frontend Design, the button
label to UX Copy. Load both, give each its part of the request, and combine the
results — a calmer layout with a clear hierarchy, and "Start free trial" instead
of "Go".

## Choose the method

| What is being made or judged | Load |
|---|---|
| Website or app interface, layout, visual direction, theming | `frontend-design` |
| Design tokens, component library, naming and consistency | `design-system` |
| Logo, icon set, brand mark, decorative web graphic | `svg-design` |
| Animation, transition, micro-interaction, timing | `motion-design`; add `gsap` when it is built with GSAP |
| Microcopy, error messages, empty states, button labels | `ux-copy` |
| Spec sheet for engineers from a finished design | `design-handoff` |
| Feedback on a design, or an accessibility audit | `design-review` |

Choose by the result, not the file type: an SVG logo is `svg-design`, an SVG
that explains a system is a diagram for Editorial SVG Diagrams. A request with
several parts loads one method per part.

## Load and hand over

The methods are explicit-only; load the chosen one through the host's skill tool
where it accepts an explicit-only skill by name, otherwise read its `SKILL.md`
from the installed skill root. Pass the request's part, the audience and any
existing design system or brand, and return the method's result to the user.
Methods do not call each other or this domain; when one needs another's work,
it reports that back here.

Building the interface in code is software engineering work. A design method can
deliver direction, tokens, copy or a handoff spec; the implementation itself
goes through the software engineering domain.
