---
name: accessibility-review
description: Run a WCAG 2.1 AA accessibility audit on a design or page, citing the success criterion for every finding — "audit accessibility", "check a11y", "is this accessible?". Use when checking color contrast, keyboard access and focus, touch target size, form labels and errors, zoom and reflow, or screen reader behavior before handoff or release; extends to WCAG 2.2 AA when that is the requirement.
argument-hint: "<design file URL, page URL, or description>"
metadata:
  skill-type: leaf
  skill-tree: design
---

# Accessibility Review

**Leaf skill** in Design; reached through its domain or by name.

A design can work well with a mouse and good eyesight and still shut out people
who use a keyboard, a screen reader, magnification or simpler language. An audit
finds those barriers and makes each one checkable: every finding names its WCAG
success criterion, the measured value and the fix. WCAG 2.1 AA is the default
standard because many legal and contractual baselines reference it, among them
EN 301 549 in the EU and the 2024 US ADA Title II rule; check which requirement
actually applies. The audit is also honest about its medium: a mockup shows
contrast and target sizes but not keyboard or screen-reader behavior, so it
reports what it could not verify instead of passing it.

## A worked finding

**Design (fictional):** a sign-up form mockup.

```text
#  Issue                                   Criterion                  Severity  Fix
1  Inputs are labeled only by placeholder  3.3.2 Labels or            Critical  Visible labels above
   text, which disappears on typing           Instructions (A)                    each field
2  Placeholder #9CA3AF on #FFFFFF: 2.5:1   1.4.3 Contrast (Minimum)   Major     #4B5563 gives 7.6:1
                                              (AA), needs 4.5:1
Not verifiable from a mockup: focus order, error announcement, name/role/value.
```

The reusable choices: measure instead of estimating, cite the criterion and its
level, and list what the medium could not show.

## Get the design and choose the depth

Work from what is shared: a design file link (pull it with a connected
`~~design tool`), screenshots, a live URL or a description. A rendered page
allows the full approach below; a static design allows the visual criteria and
an annotated plan for the rest.

> Sections marked `~~` name a tool category, not a product: `~~design tool` (for
> example Figma) or `~~project tracker` (for example Linear or Jira). Use
> whichever connected tool of that category the host provides; skip the step
> when none is.

With a `~~design tool`, read exact colors, font sizes and target dimensions
instead of sampling a screenshot, and check annotated roles and keyboard
behavior in the spec. With a `~~project tracker`, create one ticket per finding
with its criterion and severity only when the person asks for tickets.

Test in this order, and report which steps actually ran:

1. **Contrast**, computed from real color values.
2. **Keyboard only:** reach and operate everything, see focus, escape every
   component.
3. **Zoom and reflow:** 200% text zoom, and a 320 CSS px wide viewport without
   two-dimensional scrolling.
4. **Automated scan** (for example axe or Lighthouse). It finds only part of the
   issues, so a clean scan is not a pass.
5. **Screen reader** (VoiceOver, NVDA) on the main tasks. The audit does not
   replace testing with assistive technology or with disabled users.

## WCAG 2.1 criteria to check

Level in brackets. Not exhaustive: these are the criteria most designs fail.

| Principle | Criteria |
|---|---|
| Perceivable | 1.1.1 Non-text content has a text alternative (A) · 1.3.1 Structure conveyed semantically (A) · 1.3.5 Input purpose identifiable (AA) · 1.4.1 Color not the only means (A) · 1.4.3 Text contrast 4.5:1, large text 3:1 (AA) · 1.4.4 Resize text to 200% (AA) · 1.4.10 Reflow at 320 CSS px (AA) · 1.4.11 Non-text contrast 3:1 for controls and graphics (AA) · 1.4.12 Text spacing (AA) · 1.4.13 Content on hover or focus (AA) |
| Operable | 2.1.1 Keyboard (A) · 2.1.2 No keyboard trap (A) · 2.2.2 Pause, stop, hide moving content (A) · 2.4.3 Focus order (A) · 2.4.4 Link purpose (A) · 2.4.7 Focus visible (AA) · 2.5.3 Label in name (A) |
| Understandable | 3.2.1 No change of context on focus (A) · 3.3.1 Error identified in text (A) · 3.3.2 Labels or instructions (A) · 3.3.3 Error suggestion (AA) |
| Robust | 4.1.2 Name, role, value (A) · 4.1.3 Status messages announced (AA) |

Large text means at least 18 pt (24 CSS px), or 14 pt (about 18.7 CSS px) bold.

**Target size is not an AA criterion in WCAG 2.1:** 2.5.5 (44 × 44 CSS px) is
Level AAA. Report smaller targets as a usability finding against platform
guidance (Apple 44 pt, Material 48 dp), not as an AA failure — unless the
requirement is WCAG 2.2.

**When the requirement is WCAG 2.2 AA**, also check 2.4.11 Focus not obscured
(AA), 2.5.7 Dragging movements (AA), 2.5.8 Target size minimum 24 × 24 CSS px
with its spacing exceptions (AA), 3.2.6 Consistent help (A), 3.3.7 Redundant
entry (A) and 3.3.8 Accessible authentication (AA). WCAG 2.2 removed 4.1.1
Parsing.

## Severity

Use one scale, so the findings can be merged with a design critique:

| Severity | Meaning for accessibility |
|---|---|
| Critical | Blocks a task for some people: keyboard trap, unlabeled required field, no text alternative for essential content |
| Major | Possible but hard or error-prone: low contrast, missing focus indicator, unannounced errors |
| Minor | Friction that does not stop anyone: redundant alt text, inconsistent heading levels |

## Output

```markdown
## Accessibility audit: [design or page]
**Standard:** WCAG 2.1 AA | **Medium:** [mockup / rendered page] | **Date:** [date]

**Summary:** [count] findings — Critical [n], Major [n], Minor [n]

### Findings
| # | Issue | Criterion (level) | Severity | Fix |
|---|---|---|---|---|

### Contrast
| Element | Foreground | Background | Ratio | Required | Result |
|---|---|---|---|---|---|

### Keyboard and screen reader
| Element | Tab order | Keys | Announced as | Issue |
|---|---|---|---|---|

### Not verified
[What this medium or session could not test, and how to test it]

### Priority fixes
1. **[Critical fix]** — affects [who], blocks [what]
```

Leave out the keyboard and screen-reader table for a static mockup and list
those checks under "Not verified" instead. The audit judges the design and its
rendered behavior; usability and visual hierarchy belong to a design critique.
