---
name: software-engineering
description: Entry point for all software engineering work in a code repository; use it before acting. Covers building, fixing, debugging and refactoring code; reviewing a diff, branch or PR; diagnosing failing tests, builds or CI; planning a multi-step change; and updating a README or architecture doc to match the code — including quick asks like "fix this quickly", "review my branch" or "why does the build fail", even when no method is named. Picks your role (implementer, reviewer, orchestrator, documenter) and loads that role's method pack. Not for explaining programming concepts without a codebase, or for non-software engineering.
metadata:
  skill-type: domain
  skill-tree: software-engineering
  skill-requires: engineering-practices golden-comments vertical-slices road-to-glory engineering-review engineering-documentation
---

# Software Engineering

**Domain skill** for Software Engineering. Requires: engineering-practices, golden-comments, vertical-slices, road-to-glory, engineering-review, engineering-documentation. If one is missing, stop and say this skill is incomplete without it.

Engineering methods only help when they are applied together and at the right
moment: the reason behind a construction is written while the code is fresh,
ownership is decided before files are cut, and review checks both. Loaded one by
one through their own triggers, they fire unevenly — a quick fix gets none, a
large change gets several that each restate the others. This router replaces
that with one decision: **which role are you in right now?** Each role has a
fixed pack of methods that always applies, plus a few that apply when the
situation calls for them.

## A quick fix, routed

**Request:** "fix the double charge when users click pay twice, quickly pls"

The role is **implementer**: the task changes behavior in a known place. Load
the implementer pack, scaled to a small change. Engineering Practices picks the
mechanism (an idempotency key on the payment intent, not a disabled button
alone). Vertical Slices keeps the guard inside the payment capability instead of
the click handler. Golden Comments leaves one comment at the guard saying why
the key exists and what breaks without it. The result is a small diff, a
regression test, and a reason a later maintainer can find — no roadmap, no
delegation, no ceremony.

## Choose the role

| You are… | Typical request | Load always | Load when the situation needs it |
|---|---|---|---|
| **Implementer** — including every delegated worker | Build, fix, debug, refactor, migrate | `engineering-practices`, `golden-comments`, `vertical-slices` | `domain-modeling` when names or lifecycle are ambiguous; `all-or-nothing` when a change supersedes an existing owner; `marshmallow-tests` when choosing test boundaries or adding tests; `state-of-the-art` for a consequential current-practice question |
| **Orchestrator** — the lead of substantial work | A feature across capabilities, a cross-system investigation, work that needs resumable state | `road-to-glory` | `puppeteer` to delegate; for ownership, concept or technology decisions, take the implementer role |
| **Reviewer** | Review a diff, PR or finished package | `engineering-review` | The methods whose criteria apply to the change (`engineering-practices`, `golden-comments`, `vertical-slices`, `domain-modeling`, `marshmallow-tests`, `all-or-nothing`, `engineering-documentation`); Engineering Review adds its lenses itself |
| **Documenter** | README, agent instructions, architecture or SDK docs maintained with code | `engineering-documentation` | — |

Pick the role from what you will do next, not from the size of the repository.
A one-line request can need an orchestrator when it crosses capabilities or
public contracts; a large repository can need only an implementer. Roles change
during work: Road to Glory moves the lead from orchestrating to reviewing to
documenting, and each switch loads that role's pack.

Two methods are never loaded by this router on its own initiative:
`improve-codebase-architecture` and `minmax-codebase` run when the user asks for
an architectural reassessment or deliberate simplification, or when Engineering
Review selects them as lenses.

## Load a pack

Read the role's pack right after choosing the role, before you explore the
code — also for a one-line fix. The methods decide where to look and what to
record, so reading them after exploring is too late; and quick fixes are
exactly where reasons go unrecorded and ownership erodes. The pack's
methods are explicit-only, so they do not compete for selection; this router
loads them deliberately. Use the host's skill tool where it accepts an
explicit-only skill by name; otherwise read the files from the installed skill
root, for example:

```bash
cat ~/.claude/skills/{engineering-practices,golden-comments,vertical-slices}/SKILL.md
```

Read each method completely before claiming it was applied. If one is
unavailable, say which, and keep its intent through your own direct check
rather than skipping the concern.

Scaling applies to what you do with the methods, not to whether you read them.
A one-line fix still gets its reason comment where the mechanism is not
obvious, but no plan, no new module and no research.

When you delegate, put the delegate's role pack in the brief's `Skills:` field,
so the delegate loads the methods itself instead of receiving your paraphrase.

## Stay in the flow

Return each method's result to the role that loaded it. Methods do not call this
router back and do not load each other's packs; when one method needs another
role's work — an implementer who finds a review question, a reviewer who finds
missing docs — hand it to the lead, which switches role. That keeps every load
a step down the tree rather than a loop.
