---
name: design-handoff
description: Generate a developer handoff spec from a finished design. Use when a screen or feature is ready for engineering and needs a spec sheet covering layout, design tokens, components and props, interaction states, responsive breakpoints, content limits, edge cases, motion and accessibility notes, so developers build it without guessing.
argument-hint: "<design file URL or design description>"
metadata:
  skill-type: leaf
  skill-tree: design
---

# Design Handoff

**Leaf skill** in Design; reached through its domain or by name.

Whatever a design leaves unspecified, the developer decides under deadline, and
the result drifts from the design in exactly the places nobody looked: hover and
error states, long names, slow networks, the narrow breakpoint. A handoff spec
closes those gaps. It references tokens and components instead of raw values,
so the build stays connected to the system, and it says why a decision was made,
so developers can judge cases the spec did not foresee.

## A worked excerpt

**Design (fictional):** a team member list with an invite button.

```markdown
| Element | State | Behavior |
|---|---|---|
| Invite button | Loading | Label stays, spinner replaces icon, button disabled; prevents double invites |
| Member row | Long name | Truncate at one line with ellipsis; full name in the row's accessible name |
| List | Empty | "No members yet" plus the invite button; never an empty table header |

Edge case: 500+ members — paginate at 50; the design shows one page, not a scroll.
```

The reusable choice: each line states the behavior and, where it is not obvious,
the reason, so the developer can apply the same logic elsewhere.

## Gather the design

Work from a design file link (pull it with a connected `~~design tool`), a
screenshot or a description. Use the project's own breakpoints, token names and
component library; the values in the template below are placeholders. Where the
design is silent on a state or edge case, propose the behavior and mark it
**proposed** so the designer confirms it, rather than presenting a guess as the
design.

> Sections marked `~~` name a tool category, not a product: `~~design tool` (for
> example Figma) or `~~project tracker` (for example Linear or Jira). Use
> whichever connected tool of that category the host provides; skip the step
> when none is.

With a `~~design tool`, take measurements, tokens, component properties and
assets from the file instead of estimating from an image. With a
`~~project tracker`, link the spec to the implementation ticket, and create
sub-tasks only when the person asks.

## What the spec covers

| Area | Include |
|---|---|
| Layout | Grid, spacing, widths, alignment, responsive behavior per breakpoint |
| Tokens | Color, type, spacing, radius, elevation, motion — by token name |
| Components | Which library component, variant and props; anything custom |
| States | Default, hover, focus, active, disabled, loading, error, empty, success |
| Content | Character limits, truncation, wrapping, translated and longer strings, missing data |
| Interaction | Click, tap, keyboard, gestures; what happens on slow or failed requests |
| Motion | Trigger, property, duration and easing as tokens; reduced-motion behavior |
| Accessibility | Focus order, accessible names and roles, keyboard behavior, announcements |

Principles: specify what the developer would otherwise guess; reference
`spacing-md`, not `16px`; show every state; and give the reason where a decision
is not self-evident ("collapses on mobile because most use is one-handed").

## Output

```markdown
## Handoff spec: [feature or screen]

### Overview
[What it does, who uses it, link to the design]

### Layout
[Grid, breakpoints, responsive behavior]

### Tokens used
| Token | Value | Usage |
|---|---|---|
| `color-primary` | [value] | Primary buttons, links |

### Components
| Component | Variant | Props | Notes |
|---|---|---|---|

### States and interactions
| Element | State | Behavior |
|---|---|---|

### Responsive behavior
| Breakpoint | Changes |
|---|---|
| [project breakpoint] | [what changes] |

### Content and edge cases
- **Empty:** [what to show]
- **Long text:** [truncation or wrapping rule]
- **Loading and failure:** [skeleton, spinner, retry]

### Motion
| Element | Trigger | Animation | Duration | Easing | Reduced motion |
|---|---|---|---|---|---|

### Accessibility
- [Focus order, accessible names, keyboard interactions, announcements]

### Open questions
- [Every behavior marked **proposed**, for the designer to confirm]
```

The spec records decisions the design already made. Choosing the motion, the
copy or a new component is design work to finish first; documenting a reusable
component for every consumer is design system documentation, not a feature
handoff.
