---
name: design-review
description: Review a design or interface for usability, visual hierarchy, consistency and accessibility, combining a structured design critique with a WCAG 2.2 AA audit. Use for reviewing screens, mockups or rendered pages before handoff or release.
metadata:
  skill-type: parent
  skill-tree: design
  skill-requires: design-critique accessibility-review
---

# Design Review

**Parent skill** in Design. Requires: design-critique, accessibility-review. If
one is missing, stop and say this review is incomplete without it.

A design that reads well can still fail people who use a keyboard or low
vision, and an accessible design can still be confusing. Reviewing one without
the other approves half a design. This parent applies both and merges their
findings into one list.

## Run the review

1. Get the design: a URL, screenshot, rendered states or a description. Prefer
   rendered states at the sizes and themes that ship.
2. Load `design-critique` for usability, hierarchy and consistency, and
   `accessibility-review` for the WCAG 2.2 AA audit. Load only one when the
   request names it ("just check contrast").
3. Merge the findings: one list ordered by impact on the user, each with the
   location, the problem, the source (critique or accessibility) and the
   smallest fix. Remove duplicates where both found the same issue.

Load the children through the host's skill tool or by reading their `SKILL.md`
from the installed skill root. This review judges the design; whether the code
behind it is correct is software engineering review, which the agent runs
separately.
