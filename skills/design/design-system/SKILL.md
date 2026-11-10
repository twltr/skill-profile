---
name: design-system
description: Audit, document, or extend a design system's tokens, components and patterns. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, props and accessibility, or designing a new component or pattern that fits the existing system instead of duplicating one.
argument-hint: "[audit | document | extend] <component or system>"
metadata:
  skill-type: leaf
  skill-tree: design
---

# Design System

**Leaf skill** in Design; reached through its domain or by name.

A design system saves decisions only while teams trust it. Drift erodes that
trust quietly: three names for one component, raw hex values beside the tokens
they duplicate, states nobody documented. Once people stop trusting the system,
they build around it. This method works in three modes — **audit** the system as
it is, **document** a component so it can be used correctly, **extend** it
with a pattern that fits — and grounds each in the actual source: token files,
component code and the design file, not a generic idea of a design system.

## A worked audit finding

**Situation (fictional):** a React library with a tokens file; the request is
"audit our buttons and cards".

```text
Naming    Button, IconBtn and .btn-link name one concept three ways.
          → Adopt Button with an `icon` and a `link` variant; alias the old
            names for one release.
Tokens    23 hardcoded colors in Card and Modal. 18 equal an existing token
          (replace mechanically); 5 match none.
          → The 5 need a decision: a missing token, or a design error to fix.
States    Card has no focus state although it is clickable.
```

The reusable choice is the split between a value that duplicates a token, which
is a mechanical fix, and one that matches no token, which is a design question to
put in front of a person instead of guessing.

## Gather the system

Read what exists before judging it: the token source, the component code or
library, and the documentation. A search such as
`rg -n '#[0-9a-fA-F]{3,8}\b|[0-9]+px' src/components` finds hardcoded values in
code; adapt the pattern to the stack.

> Sections marked `~~` name a tool category, not a product: `~~design tool` (for
> example Figma) or `~~knowledge base` (for example Notion). Use whichever
> connected tool of that category the host provides; skip the step when none is.

With a `~~design tool`, inspect component names, variants, layer structure and
token use in the design file and compare them with the code. With a
`~~knowledge base`, find existing component pages and usage guidelines, and
publish updated documentation there only when the person asked for that.

A system has three layers; the audit and the documentation cover each:

| Layer | Contents |
|---|---|
| Tokens | Color (brand, semantic, neutral), typography, spacing, radius and border, elevation, motion durations and easings |
| Components | Variants, states (default, hover, focus, active, disabled, loading, error), sizes, behavior, accessibility |
| Patterns | Forms, navigation, data display, feedback — components combined to solve a recurring problem |

When tokens move between tools, the Design Tokens Community Group format (first
stable version 2025.10, October 2025) is the common interchange format; follow
the format the project already uses.

## Principles

1. **Consistency over novelty.** The system exists so teams stop re-deciding the
   same things; a one-off variant needs a reason the system lacks.
2. **Composable within constraints.** Prefer a variant or a composition of
   existing components over a new component.
3. **Undocumented means unusable.** A state or variant nobody can find gets
   rebuilt.
4. **Version and migrate.** A breaking rename or removal needs a migration path,
   such as an alias for a release and a codemod or a search to find uses.

## Audit

Report counts and evidence, not a score: a number without criteria hides which
problem matters.

```markdown
## Design system audit: [scope]

**Reviewed:** [components, token files] | **Findings:** [count by category]

### Naming
| Issue | Where | Recommendation |
|---|---|---|

### Token coverage
| Category | Tokens defined | Hardcoded values | Matching an existing token |
|---|---|---|---|

### Component completeness
| Component | States | Variants | Docs | Accessibility |
|---|---|---|---|---|
| Button | complete | partial: no icon-only size | missing | focus ring present |

### Priority actions
1. [Highest user or team impact first, with the effort it takes]
```

## Document

Document a reusable component for everyone who consumes it. Take props and the
code example from the real component, not an invented API.

```markdown
## Component: [Name]

[What it is and when to use it — and when to use something else]

### Variants
| Variant | Use when |
|---|---|

### Props
| Prop | Type | Default | Description |
|---|---|---|---|

### States
| State | Visual | Behavior |
|---|---|---|

### Accessibility
- **Role:** [role or native element]
- **Keyboard:** [Tab, Enter, Space, Escape, arrows]
- **Screen reader:** [announced as …]

### Do and don't
| Do | Don't |
|---|---|

### Example
[A short snippet in the project's framework]
```

## Extend

Before proposing anything new, list the existing components that come close and
say why each is not enough; most requests end as a new variant. A new component
reuses existing tokens and only proposes a new token with its reason.

```markdown
## Proposed component: [Name]

### Problem
[The user need or gap]

### Existing options
| Component | What it shares | Why it is not enough |
|---|---|---|

### Design
Props, variants and states as in the documentation template; tokens used.

### Accessibility
Role, keyboard and screen-reader behavior.

### Open questions
[Decisions that need design review]
```

The system's components and tokens are this method's subject. A spec sheet for
one feature or screen, and a new product's visual direction, are separate design
work; a system audit does not replace a WCAG audit either.
