---
name: engineering-mindset
description: Guide software work with minimum surface, truthful models, canonical ownership and meaningful evidence. Use whenever implementing, maintaining, testing or assessing software, including small code changes.
---

# Engineering Mindset

Build the full intended capability with the smallest coherent system that can
honestly own it. Apply this mindset to the authorized Engineering task, including
ordinary implementation and self-checks. It does not grant permission for a
separate redesign, refactoring, publication or production action.

## The governing rule: Minimum Surface

The objective is **Min-Max Engineering**: maximum useful behavior for the state,
code, modules, dependencies, configuration and operational moving parts needed
to deliver it. The same capability with less system is a first-class improvement.
"Smallest" means least error, state and search surface, not fewest lines.
A shared choke point may add code while making a wrong behavior have one address.

**Surface is context.** A system, test suite or explanation that cannot be held
in view cannot be changed confidently. Keep the understanding needed for a
change local and the architecture able to evolve. Ask before and after a change:
what can be reduced, what now has one owner, and what becomes easier to change
without losing capability, robustness or safety?

Before adding code, consider deleting an obsolete surface, consolidating owners,
reusing a boundary, table-driving genuinely repeated behavior or applying a
proven pattern. Compatibility layers, broad abstractions, fallback paths and
parallel workflows each need to justify the states and maintenance they add.
A green suite does not excuse retaining unnecessary parallel machinery.

There are no arbitrary file-count or line-count targets. Every file protects a
responsibility, boundary or capability. Useful comments, module briefings and
explanations are not code volume to shave away. Remove repetition and stale
claims without deleting the model, the reasons or the invariants they explain.

## Model Truth Over Diff Size

When the model is corrected, its declarations must change: types, schemas,
registries, persisted shapes, lookups and names must stop stating the false
premise. A filter, special-case lookup or compatibility flag is not a correction
if a new reader can still infer the wrong model from the code.

Apply the declaration test: **could someone still derive the false premise from
any type, field, registry entry or lookup after this change?** If yes, the model
has not been corrected. Do not silently choose that outcome because the truthful
rewrite is larger. Make a material scope or behavior decision visible instead.
Code must describe its real concepts; comments cannot excuse false declarations.

**One name, one job.** Two meanings need two honest names even while their values
happen to agree. A cap is not also a fetch page size; a floor is not also a server
default; a timeout is not also an embedding budget. A comment explaining the
double duty does not repair it.

**Withhold, never fabricate.** Unreadable or undetermined is distinct from absent,
empty, false or expired. Represent that distinction in the contract, including
the type where appropriate, and let the consumer handle it deliberately.
A fallback may give a less useful answer; it must still keep the contract's
promises. Missing configuration is no excuse to break a timeout nesting, budget
pairing or other invariant precisely when something has already gone wrong.

## One canonical owner

Give each responsibility and maintained truth one owner. Multiple inputs are
legitimate; competing implementations or independent writers of the same truth
are drift. Identify the canonical owner and the migration or removal needed
before building another implementation of its job.

Genuinely shared behavior has one responsibility and reason to change. Similar
code alone does not establish that. Apply [Vertical Slices](../vertical-slices/SKILL.md)
when building or changing repository code, including work inside existing features
and modules. Read it if its full text is not already in context, then continue
the current task. Use the existing capability boundaries where they fit; the
size of the task determines the depth of architectural work, not whether the
vertical structure applies.

## Evidence and coherent completion

Prove the behavior at the boundary that can expose the relevant failure.
A check must distinguish the defect from correct behavior, including interactions
that isolation cannot show. A regression guard must fail for the relevant reason
against the unfixed behavior and pass after the repair. A double that cannot
represent the difference cannot prove it. State what actually ran and its limits;
a local configuration check is not evidence of acceptance by a remote system.
[Marshmallow Tests](../marshmallow-tests/SKILL.md) owns designing that evidence
when new test boundaries, cases or suite changes are needed.

Carry a change through its affected model, data, consumers, configuration and
maintained explanations. Remove the old surface once its replacement owns the
work. Temporary coexistence needs an agreed purpose, owner and removal condition.
Keep useful reasons current beside the mechanisms they explain; source commentary
follows [Golden Comments](../golden-comments/SKILL.md), while substantial system
explanations follow [Synopsis](../synopsis/SKILL.md). Load their method when doing
that work, without starting an unrelated documentation project.

Keep operational scripts and contract checks with the system they protect.
Temporary authoring aids and convention checks must be removable without breaking
its build, tests or operation. A one-off verification remains a one-off. Use the
repository's normal commands and actual requirements; do not invent a build
system, permanent gate or administrative apparatus merely to finish an edit.

Perform ordinary self-checks and finish the associated cleanup in the same work.
Report the resulting capability or improvement, the evidence and unresolved
limits. A dedicated Min-Max/refactoring assignment needs an explicit human
request; this mindset never starts one on its own.
