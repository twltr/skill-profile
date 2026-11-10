---
name: workspace-writing
description: "Write or reconcile shared working notes and knowledge in OpenAI ChatGPT Pages and Spaces. Group related topics into useful hierarchies, keep current decisions and next actions visible, and link to established owners. Native Page operations belong to the host's Pages skills."
---

# Workspace Writing

Use this method only when explicitly requested by the user or selected by Good
Writing. An ordinary matching request goes through that router.

Treat **OpenAI ChatGPT Pages and Spaces** as a shared working and knowledge
surface for the person and agent. Help them find what matters and what comes
next. This skill owns content and organization, not host-local Workspace folders
or repository bindings. Accept the brief from Good Writing or a direct request;
do not route back to Good Writing.

Before writing or revising, check the target Space and the surrounding system or
workspace context available to this task for applicable instructions, conventions
and templates. Use supplied context and the host's available read/search tools;
start with the Space's entry or guidance Pages, template references and the target
content. Read relevant guidance before choosing the structure, terminology or
required fields. This keeps the writing consistent with how that Space is run.

Apply those rules within the task's authorization and the host's instruction
hierarchy. Keep their canonical sources in the Space or system. Use discovered
links in the current task context when helpful; do not append Space-specific
rules, templates or their locations to this reusable skill, its installed copies
or the Agent Profile repository. No permanent local overlay is needed. If relevant
guidance is inaccessible, distinguish that from finding none: report the material
gap and leave dependent choices open while continuing independent work.

Before drafting, reuse the caller's source-selection handoff. If none is supplied,
use Writing Fragments when available to select the relevant material, sources,
qualifiers and gaps at the scale of this task. Otherwise perform that bounded
selection directly without claiming the skill was applied. A direct invocation
needs the same preparation, not a return to Good Writing or repeated scouting.

**Apply `unslop` when available**, including during direct use. Load it once through the
host's skill catalog and returned path or read interface unless already loaded.
If unavailable, use this skill's clarity and preservation checks and report
that Unslop was not applied.

**Example:** Notes say the welcome message is drafted, launch still needs a
support owner, and technical migration progress lives in a repository issue.
The overview links to customer communication and support readiness, and points
to the migration issue instead of copying its status:

```text
Launch
  Welcome message: drafted -> Customer communication
  Support coverage: owner needed -> Support readiness
  Technical migration: progress -> existing repository issue
```

Keep this map together. Create linked Pages only when a subject needs its own
reading path. Any cloud access not checked remains unknown.

For example, if this Space has a launch-note template requiring an owner and a
next checkpoint, use those fields in the launch note and preserve an unknown
owner as unresolved. The template stays in that Space; its fields do not become
requirements for every other Space or additions to this skill.

## Cluster by meaning

Use a hierarchy of related topics, like hierarchical clustering: group the
closest subjects, then name their common parent. Group by the reader's actual
work or question, not merely by matching words, date or document format.

1. Identify the distinct subjects and which information belongs together.
2. Give each coherent subject a section or linked Page. Split when it has its
   own useful reading path; keep small related notes together.
3. Put orientation, shared facts and links at the parent. Put subject-specific
   decisions, context and actions with that subject.
4. Link across clusters where needed. Keep each fact at one owner, rather than
   copying it into every related branch.

Do not flatten five unrelated topics into a continuous Markdown note. Do not
create a Page for every sentence either. Use headings within a short Page and
linked detail Pages for independently useful subjects. Map the logical hierarchy
to the host's supported Page/Space structure; do not invent nested-folder support.
Change an existing Page structure only within an authorized organization task.

## Keep the working surface current

Retain useful general tasks, decisions, reminders and context. There are no
mandatory fields, fixed page trees or required status sections imposed by this
method. Applicable local guidance or a template may require them. An empty Page
can be the right result when the task and local guidance require no content.

Code and infrastructure work belongs in its repository. Link to its current
plan or issue when useful; keep no second roadmap here. Durable information
stays at its subject's established owner, such as finance documents in Drive.
Improving a note does not authorize moving those records.

For an authorized update, read the current content and reconcile in place.
Update existing statements; remove completed, obsolete or duplicate material
within the requested maintenance scope. Do not append recurring review reports
or build archive Pages by default.

Preserve manual edits and conversation notes. Missing evidence does not mean
finished, wrong or safe to delete. Keep unresolved material and its conditions
visible; clarify a necessary ambiguous change instead of silently discarding it.

## Make the map visible

Use meaningful headings, grouped lists, real action checkboxes, emphasis, links
and comparable tables as the content warrants. Keep context near its decision.
Avoid technical IDs, hash lists, test logs and agent reports on the human overview
unless needed there. Link useful sources beside the supported point.

Load `editorial-svg-diagrams` for relationships, dependencies or workflows that become
clearer visually. Pass the verified model, reader and intended output; it owns
editable sources, export and visual checks. Keep large diagrams in linked
detail. If unavailable, disclose that limit and use a readable list, table or
prose; an explicitly requested diagram remains open.

## Save only the requested result

Use the applicable host-managed Pages writing, maintenance or organization
skill for authorized native operations and verification. A chat draft or open
Page alone is not a write request. Before saving, check topic ownership,
links, conditions and protected manual content. Read back the affected content
to establish what was saved; report any unsupported operation precisely.
