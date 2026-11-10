---
name: skill-issue
description: Create, revise, review or audit agent skills, from capturing intent through drafting, realistic test prompts, trigger tuning and iteration. Use whenever someone wants to turn a workflow into a skill, improve or restructure a SKILL.md, fix a skill that fires too often or too rarely, design a router, domain or flow over sibling skills, untangle dependencies inside a skill collection, or review skills for quality, even when they only say "this skill is bad" or "make my skills better". Executing another skill's own workflow stays with that skill.
metadata:
  short-description: "Core: Build, test and sharpen skills agents actually use"
  skill-type: core
---

# Skill Issue

**Core skill.** Usable in any context; loads no other skills.

A skill is a briefing for a capable colleague who has never met you. It is read
at the moment of need by an agent that knows its craft but not your situation,
your conventions or the mistakes you already made. Everything in it should either
change a decision or save work; everything else is noise the agent must read past.

Creating or improving a skill is a loop:

1. Capture what the skill should do, for whom, and when it should fire.
2. Draft or revise it.
3. Run realistic prompts with the skill, and with a baseline.
4. Evaluate the results with the user: qualitatively, and quantitatively where
   outputs are verifiable.
5. Revise from what the runs showed, not from what the draft promised.
6. Repeat; then widen the test set and tune the description.

Figure out where the user is in this loop and pick up from there. Someone with
an idea needs interviewing and a draft; someone with a draft needs test runs;
someone with a working skill may only need its triggering fixed. If the user says
"skip the evals, just improve it with me", do that — the loop serves the skill,
not the other way round.

## Principles

These are the ideas behind every later section. When a specific rule seems not
to fit, reason from these instead.

- **Progressive disclosure.** A skill loads in three levels: metadata (name and
  description, always in context), the `SKILL.md` body (loaded when the skill
  triggers) and bundled resources (read or executed only when needed). Put each
  piece of guidance at the cheapest level where it still arrives in time.
- **Explain the why.** Today's models have good theory of mind. A reason lets
  them handle the case you did not foresee; a bare MUST only covers the case you
  did. If you find yourself writing ALWAYS or NEVER in capitals, treat it as a
  yellow flag: reframe it and explain what goes wrong without it.
- **Principle of lack of surprise.** A skill's contents should not surprise the
  user if its intent were described to them. No hidden side effects, no actions
  beyond the stated purpose, nothing that grants itself authority, credentials or
  tools the runtime does not provide.
- **Keep the prompt lean.** Every line must pull its weight. Read the transcripts
  of test runs, not just the outputs: if the skill makes the agent waste effort,
  remove the part that causes it and see what happens.
- **Generalize, don't overfit.** A skill will be used across far more prompts
  than the few you test with. Fix the cause behind a failed example rather than
  patching that example; if a problem is stubborn, try a different metaphor or
  working pattern instead of another constraint.
- **Bundle repeated work.** When every test run independently writes the same
  helper script or takes the same multi-step detour, ship that work once in
  `scripts/` and tell the skill to use it.
- **One owner per fact.** Each decision, rule or procedure lives in exactly one
  place. Other places link to it. Duplicates drift apart and contradict each other.
- **Trees, not meshes.** Skills compose downward from a few implicit roots: a
  routing skill names the skills it uses; a child never names its caller, and no
  edge crosses into another tree. A collection where everything mentions
  everything is expensive to load and impossible to reason about.

## A small worked example

**Request:** "My commit-message skill never fires."

The description is the only thing the agent sees before deciding, and this one
names a topic, not a task or a moment:

```yaml
description: Commit message conventions.
```

Rewrite it to say what the skill does and the situations where it helps,
including phrasings that never mention the skill:

```yaml
description: Write commit messages in this repository's Conventional Commits
  style with scope, imperative summary and breaking-change footer. Use whenever
  committing, amending, squashing or preparing a PR, even if the user just says
  "commit this" or "save my work".
```

Then check it against two prompts: *"ok commit the auth changes and push"*
should trigger it; *"what does git commit --amend do?"* is a near-miss that
asks for an explanation, not a message, and should not. The example teaches the
reusable choice — describe the moment of use, then test both sides of the
boundary — rather than a template to copy.

## Anatomy of a skill

```text
skill-name/
├── SKILL.md            required: YAML frontmatter + Markdown instructions
├── agents/openai.yaml  optional: Codex presentation and invocation policy
├── scripts/            executable code for deterministic or repetitive work
├── references/         documentation read into context when needed
├── assets/             files used in the output: templates, icons, fonts
├── evals/              test cases (see references/evaluation.md)
└── NOTICE.md, LICENSE* provenance and licenses of adapted material
```

The frontmatter needs `name` (lowercase, hyphenated, matches the directory) and
`description`. Host-specific fields carry host-specific policy: Claude Code reads
`disable-model-invocation: true` to keep a skill explicit-only, Codex reads
`policy.allow_implicit_invocation` from `agents/openai.yaml`. Keep such policy in
metadata and out of the description text, which is for the task.

When a skill supports several domains or frameworks, organize references by
variant so the agent reads only the one it needs:

```text
cloud-deploy/
├── SKILL.md        workflow + how to select the provider
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Keep `SKILL.md` under about 500 lines. When you approach that, add a layer of
hierarchy with clear pointers about where the agent should go next, instead of
compressing the prose until it stops explaining. Give a reference file longer
than about 300 lines a table of contents.

## How skill triggering works

An agent sees the name and description of every available skill and decides
from those alone whether to consult one. Two consequences shape every description:

- **Agents consult skills for work they cannot easily do alone.** A one-step
  request such as "read this file" rarely triggers a skill even when the
  description matches, because the agent can just do it. Complex, multi-step or
  specialized requests trigger reliably when the description matches.
- **Agents tend to undertrigger.** Make descriptions a little pushy: state what
  the skill does, then the contexts where it applies, including requests that
  never name it. "Use whenever the user mentions dashboards, metrics or wants to
  display company data, even without asking for a dashboard" beats "How to build
  dashboards."

Pushy is not greedy. The more skills share a trigger surface, the more each
description must state its nearest neighbor: "Explanatory diagrams belong here;
logos and icons belong to the brand-graphics skill." Name a boundary only where confusion is
plausible, or the description fills up with exclusions.

Write the description in one to three sentences, under the 1024-character limit
of the skill specification. Lead with the task and outcome. The human-facing
short description (`metadata.short-description`, or `short_description` in
`agents/openai.yaml`) starts with the skill's type and then states the concrete
benefit in plain words: "Domain: Write and revise texts for their audience and
purpose", not "Auto: choose a writing method".

## Place the skill in the tree

Every skill in a collection has one of five types. The type decides how it is
selected, what it may load, and where it sits:

| Type | Role in the tree | Selection | Loads |
|---|---|---|---|
| **Core** | Stands in the middle; useful in any context | Implicit | Nothing |
| **Domain** | Root of a tree; establishes the context and routes into it | Implicit | Its children |
| **Parent** | Inner node; applies its children together | Explicit-only | Its children |
| **Flow** | Inner node; runs steps left to right with roles | Explicit-only or via its domain | Its step skills |
| **Leaf** | Self-contained method | Explicit-only | Nothing |

Domain, parent and flow skills are **routing skills**. The agent starts in the
middle, with core skills and domain roots; it moves down a tree, never up and
never across into another tree. A leaf must work when a user calls it by name,
so it never assumes or names a caller. A flow orders skills that stay usable
without it. The full rules, the reasons, role packs, how to resolve shared
children, and how to declare type and dependencies are in
[references/skill-architecture.md](references/skill-architecture.md); read it
before creating a skill, adding a router or restructuring a collection.

A domain routes in one of two ways. It **selects** one child for the result —
a writing domain picks the specialist that owns the text. Or it selects by **role** and loads
that role's pack of methods that always apply together:

```markdown
| Signal in the request          | Load              | Owns                         |
|--------------------------------|-------------------|------------------------------|
| Explains a system or workflow  | concept-diagrams  | Concept figures, exports     |
| Logo, icon, brand mark         | brand-graphics    | Identity and web graphics    |
| Movement, transition, timing   | ui-motion         | Motion principles            |
```

Keep a routing skill a switchboard, not a manual: its table, the few rules
every route shares, and what to hand the child. A routing node costs one hop on
every use; it pays off when siblings share a trigger surface and misrouting is
common or expensive. Because one broad domain description then carries a whole
context, measure it: run a trigger evaluation against the current configuration
before you make its children explicit-only.

When a skill loads a child, say the condition, what to pass, what comes back
and the honest fallback if the child is missing. Resolve and read the child
before claiming it was applied. An explicit-only skill stays out of implicit
selection, but its routing parent may read it deliberately; a reference grants
no authority the runtime does not give.

To audit a collection, run [scripts/skill_graph.py](scripts/skill_graph.py) on
its skill roots. It counts cross-references and lists mutual pairs and the most
referenced skills. A mutual pair or an edge into another tree is a defect to
explain; a count shows a mention, not a real call.

## Write the body

Open with the problem the skill solves and why its core choices address it. The
reader needs causal understanding, not only a trigger and a list of commands.
Show a small successful application early — a few lines of input, decisive action
and resulting output — before any long ruleset. An example must teach a reusable
choice, not repeat a rule in other words. Label fictional facts and illustrative
pseudocode; never invent tool APIs or claim a sample was executed.

Use the imperative form. When an output format matters, show its exact shape:

```markdown
## Report structure
Use this template:
# [Title]
## Summary
## Findings
## Recommendations
```

Show examples as input and output where that fits:

```markdown
**Example:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

Match precision to fragility. Context-dependent design needs criteria and room
for judgment. A recurring transformation may need a parameterized script. A
fragile operation needs exact prerequisites, ordering and failure handling. Do
not turn a discretionary task into a ceremony, or a risky operation into advice.

Resolve real tool names, arguments, dependencies and paths against the target
environment. Missing access or unresolved authority needs a clear stop or
fallback.

Format for both readers. Humans scan headings, tables and code blocks; agents
follow steps and examples. Use numbered steps for sequences, a table for a
selection, a fenced block for anything to be copied, and prose for the reasons.
Avoid decorative bold and walls of bullets that hide which point carries weight.

Write a draft, then reread it with fresh eyes as the agent who will receive it:
what would you misread, skip or not know how to start?

## Give every supporting file a reason

| Material | Placement |
|---|---|
| Core decisions, common workflow, first worked example | `SKILL.md` |
| Brief examples needed on most uses | Beside the relevant step in `SKILL.md` |
| Substantial optional variants, schemas, provider details | A directly linked reference with a stated reading condition |
| Repeated mechanics that need deterministic execution | A script with explicit inputs, outputs and failure behavior |
| Files copied into the user's result | `assets/` |
| Attribution, licenses, source records | `NOTICE.md` and license files |

A separate file should save irrelevant reading, not merely add a lookup. Link
each resource directly from `SKILL.md` and state when to read it. Avoid chains
of references on the normal path, and never put the first usable example behind
a link just to shorten the main file.

## Test, evaluate, improve

After a draft, write two or three realistic test prompts — what a real user
would type, with real-sounding detail — and share them with the user before
running. Then run each prompt with the skill and against a baseline: no skill
for a new skill, the previous version for a revision. Use parallel subagents
when available so runs finish together; otherwise run them yourself in sequence
and say that this is weaker, because you know the skill's intent.

While runs are in progress, draft assertions for outputs that can be checked
objectively, with names that say what they check. Leave subjective qualities —
style, visual design — to human judgment rather than forcing assertions onto them.

Review the results with the user directly in the conversation: per case, the
prompt, what the skill run produced, how it differed from the baseline, and
which assertions passed. Read the transcripts too. Then improve:

1. **Generalize from the feedback** instead of fitting the examples.
2. **Remove what does not pull its weight**, especially parts that cause wasted work.
3. **Explain the why** behind anything the agent got wrong.
4. **Bundle work the runs kept repeating.**

Rerun into a new iteration and continue until the user is satisfied, the
feedback is empty, or progress stalls. Exact test-case layout, workspace
structure, grading and the trigger-tuning procedure are in
[references/evaluation.md](references/evaluation.md); read it before writing the
first test case or trigger eval set.

## Tune the description

Once the skill works, test its triggering. Write about twenty realistic queries:
eight to ten that should trigger it and eight to ten near-misses that share its
vocabulary but need something else. Near-misses are the valuable half. "Write a
fibonacci function" is a useless negative for a PDF skill; "convert this PDF's
tables into a pandas DataFrame and plot revenue" may be a real one for a PDF skill
that only covers forms. Review the set with the user, then run it as described
in [references/evaluation.md](references/evaluation.md#trigger-evaluation).

## Review a skill or a collection

For a review-only request, inspect without editing. Read each skill as a new
user of its method and check:

- Does the description name a concrete task and moment of use, and distinguish
  its nearest neighbor — including a library, tool or product with the same name?
- Does the opening explain the problem and why the core choices address it?
- Does an early example show useful work and its result?
- Can the ordinary path run without opening every supporting file?
- Is each reference conditional, substantial or independently reusable?
- Are tools and paths real, constraints coherent and dependencies available?
- Are reasons given where the skill uses MUST, ALWAYS or NEVER?
- Does verification distinguish a useful outcome from the relevant failure?
- Is there an honest fallback when a tool, skill or host capability is missing?
- Is the type declared in `metadata`, the first body line and the short
  description, and do its edges follow the tree rules?

Then walk four requests through the description and workflow without doing the
downstream work: a normal one, a different valid one, a near-miss and, where
authority or access matters, a blocked one. Near-misses expose trigger
collisions that reading alone misses. Parse the metadata and check names, links
and referenced assets.

For a collection, also run the graph script, look for overlapping trigger
surfaces that want a router, and for skills that repeat a fact another skill owns.

Write findings as **observed passage → consequence → smallest improvement**.
Include a candidate example where its absence is the issue. Keep proposals
separate from edits and avoid numeric scores without criteria. Report desk
review, executed checks and fresh model trials separately: a metadata check
does not prove reliable selection or good output.

If **Grilling with Agents** is available and an authorized collection review
needs deeper challenge, give independent agents bounded skills to test against
realistic uses; the lead answers and fixes supported issues.

## Install only when that is part of the task

For an authorized installation, update or distribution, read
[references/installation.md](references/installation.md). Authoring or reviewing
a skill does not require installing anything.

Deliver the revised skill or the requested review, the checks actually performed,
and any open activation boundary. Source influences and adaptation choices are
recorded in [NOTICE.md](NOTICE.md).
