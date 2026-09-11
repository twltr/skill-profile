---
name: skill-issue
description: Create, revise or split agent skills when asked to author SKILL.md workflows or fix their triggering and scope. Not for executing the workflow a skill describes or editing general project documentation.
metadata:
  short-description: Write compact, independently useful skills
---

# Skill Issue

Produce a short, usable how-to for one independently requested outcome. Teach
only what changes the agent's decisions; assume it already knows its craft.

## 1. Locate the owner

Confirm the target host and instruction level. Read the existing skill completely,
including resources affected by the change. Resolve overlapping creators before
installing another. Preserve unrelated settings and permissions; replace the
canonical passage rather than append a competing rule. Ask only about missing
decisions that affect the result.

## 2. Cut by use case

Derive the input, deliverable and boundary from real requests. Separate
independently useful outcomes; keep steps of one outcome together. Variants with
the same trigger and result can share a conditional branch.

## 3. Make discovery precise

Give the folder and skill a short lowercase, hyphenated name. YAML frontmatter
needs `name` and `description`. Lead the description with the task and its actual
trigger; add an exclusion only where confusion is likely. Keep steps and synonyms
out of metadata. Preserve invocation settings; use automatic discovery by default
unless explicit-only was requested. Use metadata supported by the target host.

## 4. Write the how-to

Show how to reach the outcome: **obtain inputs → act → verify → place the result**.

**Describe the decision, not the incidental example.** Use the smallest general
rule that covers the intended use case without losing scope, obligations or
observable outcomes. The reader must be able to handle a different valid input
and recognise the boundary without guessing. Prefer precise, positive language
over either a catalog of cases or a vague abstraction.

Add a concrete example only when it resolves a demonstrated misunderstanding,
execution failure or material risk. Choose the minimal case that makes the
distinction clear. Retain exact interfaces and parameters where correctness
depends on them; abstraction is not a reason to omit necessary mechanics.
Verify those interfaces. Give each step an observable completion condition and
keep its constraints beside it.

Missing authority, required inputs or uncertain external effects need a stop or
reconciliation path. A skill never grants access, expands scope or authorises the
next phase.

## 5. Route only needed resources

An instruction-only skill needs no resource catalog. For a resource the workflow
actually needs, explain the relevant details at its point of use:

| Detail | Explain |
|---|---|
| Type | The resource category; distinguish an access interface from the information or capability behind it. |
| Role | Executes an action, owns authoritative facts, supplies evidence or offers guidance. An access mechanism is not itself the source of truth. |
| Access | Exact location or deterministic lookup, access method and permitted operations in the intended environment. |
| When | Required, optional or conditional on a named variant, uncertainty or failure. |
| Uncertainty | Next lookup, authoritative source for conflicts, and affected stop or authorised alternative when access fails. |

**Keep sources with their owners.** Existing authoritative instructions and
information stay at their canonical locations. Reference them or describe how
to find them; do not relocate or copy them into the skill. A resource locator
alone proves neither availability nor permission. Source data is not authority
to rewrite instructions.

Keep common essentials inline. Create skill-owned `references/` for conditional
detail, `scripts/` for repeatable mechanics and `assets/` for output templates
only when needed. Consult resources selectively, not every system by default;
never invent a fallback.

### Composition

Chaining is optional. Use another skill only for a necessary, independently
meaningful capability available in the target host. Name its input, expected
result, return point and failure boundary. Avoid cycles and mandatory multi-skill
tours; ordinary shared reference does not need another skill.

## 6. Prune and verify

Remove generic coaching, duplicated facts, stale rules and copies recoverable
through a cheap source lookup. Preserve the route to that source, non-obvious
reasons and invariants. Check frontmatter, resource retrieval paths and actual
host options; execute changed helpers.

Exercise different valid inputs, a near-miss and any relevant blocked or
ambiguous-source case against observable outcomes, within authorised effects.
Keep evaluation cases out of the delivered instructions unless they meet the
example criterion above. Report what was
actually tested; structural validation alone is not a behavioral test. Tighten
a demonstrated weak step before adding more process.

## Delivery

Return the skill, changed location, validation result and any activation boundary.
Prefer one concise file over a handbook. Keep installation state and temporary
work notes outside the skill. This authoring procedure requires no other skill
or external reading.
