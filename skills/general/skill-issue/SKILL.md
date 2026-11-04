---
name: skill-issue
description: Create, revise or review agent skills with clear task descriptions, worked examples, usable workflows and justified supporting resources. Use for SKILL.md authoring, trigger boundaries, skill quality reviews and installation guidance; executing another skill's workflow remains with that skill.
metadata:
  short-description: Build and review practical skills with clear examples
---

# Skill Issue

Build a skill another agent can use without reconstructing the intended method.
Show a small successful application early, then explain the decisions that make
it work. Open with the problem the method solves and why its core choices help;
the reader needs causal understanding, not only a trigger and a list of commands.
Preserve the user's scope: a review produces findings; authorized edits
change only the named skills and their affected resources.

## A small worked example

**Request:** Improve a delegation skill whose only guidance is “give clear tasks.”

Put a usable handoff near the start of that skill:

```text
Task: Identify why the checkout test fails.
Inputs: The failing test, its error output and the checkout module.
Boundary: Read-only; no edits or additional agents.
Return: The likely cause, exact supporting locations, uncertainty and
        the smallest check that could distinguish competing explanations.
```

Then explain when that handoff is useful and when the main agent should do the
work directly. Keep this short example in `SKILL.md`; a separate file would add
a lookup to its central method. A longer comparison of delegation research may
remain a conditional reference. This is an example of authored skill content,
not an instruction to launch an agent during skill authoring.

## 1. Establish the task and owner

Confirm the skill's reader, input, useful outcome, likely request and boundaries.
Use actual user examples when available; otherwise propose realistic cases and
label assumptions. Resolve only gaps that change the outcome or authority.

Find the canonical source and intended runtime. Read the existing skill completely
and any resources affected by the change. Preserve unrelated edits, licenses,
provenance and native settings. An installed copy, upstream repository and host
plugin may have different owners; do not create a second maintained source.

For a review-only request, inspect without editing the reviewed skills. Record
specific findings and the smallest proposed changes at the task's existing owner.

## 2. Make discovery and presentation useful

Use a short lowercase, hyphenated name. In the YAML frontmatter, `description`
explains what the skill does and when it fits. Lead with the task; add a boundary
only where a nearby workflow could be confused with it. Keep essential trigger
information here because the body is read only after selection.

The human-facing short description states the concrete benefit in ordinary
language. “Write and revise texts for their audience and purpose” is useful;
“Auto: choose a writing method” spends the description on control information.

Keep technical invocation rules in the runtime's supported metadata, such as
`policy.allow_implicit_invocation` in `agents/openai.yaml`. Preserve those rules
unless changing them is authorized. Do not repeat “Auto,” “explicit-only” or a
policy explanation in descriptions. Functional routing and permission boundaries
still belong in the workflow where they affect decisions.

## 3. Teach through a short example

Include at least one realistic worked example near the beginning, before a long
ruleset or reference index. Show the input, the decisive action and the resulting
output or evidence. A few lines may be enough. For an interaction skill, show an
actual question or handoff; for a writing skill, a small transformation; for a
technical skill, a minimal valid operation with its expected result.

An example must teach a reusable choice, not just display a generic template or
repeat the rule in other words. Explain the relevant boundary beside it. Label
fictional facts and illustrative pseudocode; never invent tool APIs or claim a
sample was executed. If an output format matters, show its actual shape.

Keep short examples of the normal path inline. Move a collection of variants or
a lengthy walkthrough only when it would distract from the shared method. Do
not put the first usable example behind a link merely to shorten the main file.

## 4. Write the method and choose its precision

Explain how to obtain inputs, make the important decisions, act, verify and place
the result. Include the non-obvious reasons, invariants and failure consequences.
Assume the agent knows its general craft; omit generic coaching and repeated
rules that add no decision guidance.

Match precision to the task. Context-dependent design needs criteria and room for
judgment. A recurring transformation may need parameterized code. A fragile
operation needs its exact prerequisites, ordering and failure handling. Do not
turn a discretionary task into a rigid ceremony or a risky operation into advice.

Resolve real tool names, supported arguments, dependencies and paths against the
target environment. Missing access or unresolved authority must have a clear stop
or fallback appropriate to the task. A skill never grants permission, credentials
or access to tools that the runtime does not expose.

## 5. Give every supporting file a reason

| Material | Placement |
|---|---|
| Core decisions, common workflow, first worked example | `SKILL.md` |
| Brief examples needed on most uses | Beside the relevant step in `SKILL.md` |
| Substantial optional variants, schemas or provider details | A directly linked reference with a stated reading condition |
| Repeated mechanics that need deterministic execution | A script with explicit inputs, outputs and failure behavior |
| Files copied into the user's result | Assets or templates |
| Attribution, licenses and source records | The skill's provenance files |

Ask whether a separate file saves irrelevant reading or merely adds a lookup.
There is no required number of references and no benefit in splitting by file
count alone. Keep one owner for each fact; move material rather than copying it
into both the body and a reference. Link resources directly from `SKILL.md` and
state when to read them. Avoid chains of references for the normal path.

Use another skill only for an independently useful capability. State "if available"
or its equivalent, the condition that needs it, the input, expected result and
honest fallback. Resolve and read the actual method before claiming it was used.
An absent skill is not an excuse to fabricate capabilities or omit a required check.
Do not re-enter the caller or any active ancestor, or create a mandatory tour
through several skills. Include active workflow names in delegated handoffs.
Explicit-only discovery and deliberate composition are different routes: native
policy still applies, and a workflow reference does not grant missing authority.

Keep one owner for decisions, mechanics and lifecycle. For example, an independent
review method can return findings to a planning method; the planning method owns
cleanup and merge sequencing. Explain why distinct stages exist when their order
prevents rework or loss of evidence. Use steps for sequential work and examples
to show the decisive choice rather than accumulating unsupported rules.

## 6. Review and verify

Read the finished skill as a new user of its method. Check these questions:

- Does the description identify a concrete task and distinguish its nearest neighbor?
- Does the opening explain the problem and why the method's core choices address it?
- Does the opening example show useful work and the expected result?
- Can the ordinary path run without opening every supporting file?
- Is each reference conditional, substantial or independently reusable?
- Are tools and paths real, constraints coherent and dependencies available?
- Does verification distinguish a useful outcome from the relevant failure?

Parse the metadata and check names, links and referenced assets. Run changed
helpers on representative inputs. Exercise a normal request, a different valid
request and a near-miss; include a blocked case when authority or access matters.
For an audit, use these cases to expose ambiguities without doing the downstream
work. Report desk review, executed checks and fresh model trials separately.
A metadata check cannot establish reliable model selection or good output.

Write findings as **observed passage → consequence → smallest improvement**.
Include a concrete candidate example where its absence is the issue. Distinguish
an absent example from one that is late, too generic or unnecessarily external.
Keep proposals separate from edits and avoid a numeric score without criteria.

## 7. Install only when that is part of the task

For an authorized installation, update or distribution, read
[references/installation.md](references/installation.md). It covers source and
runtime ownership, complete-tree copies, native metadata and loader checks.
Authoring or reviewing a skill does not require installing an external creator.

Deliver the revised skill or the requested review, the checks actually performed
and any open activation boundary. Improve the method from observed use; do not
add instructions merely to make the package look comprehensive. Source influences
and adaptation choices are recorded in [NOTICE.md](NOTICE.md).

If **Grilling with Agents** is available and an authorized collection review calls
for deeper challenge, give independent agents bounded skills and ask them to test
the problem, rationale, workflow and examples against realistic uses. The lead
answers and fixes supported issues; council questions stay between agents. Report
decisions, reasons and any unresolved prerequisite to the user or existing plan
without turning the audit into a user interview. Do not mistake a desk audit for
a fresh behavioral trial.
