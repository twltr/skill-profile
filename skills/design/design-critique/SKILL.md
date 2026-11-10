---
name: design-critique
description: Give structured design feedback on usability, visual hierarchy and consistency, at any stage from exploration to final polish. Use when someone shares a mockup, screenshot, design file link or live screen and asks what works, what does not, or what to change — "review this design", "critique this mockup", "what do you think of this screen?".
argument-hint: "<design file URL, screenshot, or description>"
metadata:
  skill-type: leaf
  skill-tree: design
---

# Design Critique

**Leaf skill** in Design; reached through its domain or by name.

Feedback such as "the layout feels busy" gives the designer nothing to act on.
Useful critique names the location, what a person would experience there, why
that matters for their goal, and a concrete alternative — and it matches the
design's stage, because exploration needs direction while final polish needs
detail. This method walks the design through a fixed set of lenses so the
feedback is specific, ranked and complete.

## A worked finding

**Design (fictional):** a checkout screen at final polish.

```text
Location   Order summary, "Apply coupon"
Observed   Styled as a filled button in the brand color, the same weight as
           "Pay now"; on mobile it sits directly above it.
Why        Two primary-looking actions compete at the moment of payment, and
           a coupon field invites people without a code to leave and search.
Severity   Major
Change     Make it a text link under the subtotal that expands into a field;
           keep "Pay now" the only filled button on the screen.
```

The reusable choice: the finding ties a visual property to a user consequence,
then proposes the smallest change that removes it.

## Get the design and its context

Work from what is shared: a design file link (pull it with a connected
`~~design tool`), a screenshot or file (read it), or a live URL. Prefer rendered
states at the sizes and themes that ship. If nothing is shared, ask for it.
Establish what the design is for, who uses it, the stage (exploration,
refinement, final) and any focus the person asked for. Missing context does not
block a critique; state the assumption it rests on.

> Sections marked `~~` name a tool category, not a product: `~~design tool` (for
> example Figma), `~~user feedback` (for example a support or survey tool). Use
> whichever connected tool of that category the host provides; skip the step when
> none is.

With a `~~design tool`, inspect components, tokens and layers and compare them
with the existing design system. With `~~user feedback`, check recent feedback
and tickets for problems the design should answer.

## The lenses

1. **First impression (two seconds).** What draws the eye first, and should it?
   Is the purpose clear at once?
2. **Usability.** Can the person reach their goal? Are interactive elements
   recognizable, navigation predictable, steps necessary?
3. **Visual hierarchy.** Is there a clear reading order? Are the right things
   emphasized? Does spacing group what belongs together? Does typography carry
   the hierarchy?
4. **Consistency.** Does it follow the design system? Do similar elements look
   and behave alike in spacing, color, type and interaction?
5. **Obvious accessibility problems** you notice along the way — text that is
   hard to read, tiny targets, meaning carried by color alone. Note them; a
   systematic WCAG audit is separate work, and this critique does not certify
   compliance.

Rate each problem on one scale, so findings from different reviews can be
merged:

| Severity | Meaning |
|---|---|
| Critical | Blocks a task, misleads, or loses data or money |
| Major | Slows or confuses many people; works against the design's goal |
| Minor | Polish: inconsistency or roughness most people get past |

Be specific, explain why, propose an alternative, say what works and keep it,
and match the stage: at exploration, question the direction instead of pixel
values.

## Output

```markdown
## Design critique: [design name and stage]

**Overall:** [one or two sentences: what works, the biggest opportunity]

### Findings
| # | Location | Issue and why it matters | Severity | Recommendation |
|---|---|---|---|---|

### Visual hierarchy
- **Draws the eye first:** [element], [right or wrong, and why]
- **Reading flow:** [how the eye moves through the layout]

### What works
- [Strengths to keep, so a revision does not lose them]

### Priorities
1. **[Most impactful change]** — [why and how]
```

For a small screen, keep everything in the findings table instead of adding
sections the design does not need. The critique judges the design; whether code renders it
correctly is a separate review.
