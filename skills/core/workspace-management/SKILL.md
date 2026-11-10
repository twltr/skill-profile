---
name: workspace-management
description: Find, read and keep current the local Workspace that maps a body of work spanning several repositories, systems, providers or document stores, so the agent is onboarded without being told. Use at the start of any work on a project, client, product or system — even when the user only says "let's work on X" — and whenever work changes where its parts live or what state they are in. Propose, never create unasked, a Workspace when multi-part work has none; a single repository never needs one.
metadata:
  short-description: "Core: Onboard from local Workspaces and keep them current"
  skill-type: core
---

# Workspace Management

**Core skill.** On the agent's surface and usable in any context.

A body of work rarely lives in one place. A client project can span five
repositories, three running systems at two providers, a shared drive folder and
a knowledge base. Without a map, every new session starts with the user
explaining where things are. A **Workspace** is that map, written from the
viewpoint of this machine: what belongs together, where each part lives, what
state it is in, and which instructions own it. The agent reads it before acting
and is onboarded; the user never has to brief it again.

A Workspace is a viewpoint, not a source. It points outward from this machine
to the places that own the work and keeps none of their content.

## Entering work, onboarded

**Request:** "let's continue with the dispatcher for the freelance stuff"

1. Read the Workspace root's `README.md`: a Workspace named for the freelance
   operations exists.
2. Read that Workspace's `README.md` and `AGENTS.md`: the dispatcher is one of
   its repositories, at a recorded path, with its own `AGENTS.md`; the business
   records live in a document store; shared notes live in a named knowledge base.
3. Enter the dispatcher repository and read its own instructions before acting.
4. After the work, if a part moved, appeared, retired or changed state, update
   the Workspace in the same task.

**A single repository is not a Workspace.** "Fix the login bug in my notes app"
— one repository with its own `README.md` and `AGENTS.md` — needs no Workspace;
the repository is its own map. It becomes Workspace-worthy only when the work
grows into several important parts that belong together.

## What is Workspace-worthy

A Workspace covers one coherent body of work made of **more than one important
part**: several repositories, running systems and their providers, document
roots, shared drives, infrastructure, or accounts that together serve one
purpose — a client, a product line, an operating model, an agent system. Ask:
would an agent entering one part miss something it needs from another? If yes,
it is Workspace-worthy. If everything lives in one repository, it is not.

## Layout

```text
~/Workspaces/
├── README.md        this machine's view: its environment, clusters of
│                    Workspaces, where shared knowledge lives
├── AGENTS.md        rules for every Workspace on this machine
└── <workspace>/
    ├── README.md    the map: purpose, parts, their state, boundaries
    └── AGENTS.md    how an agent enters: which part to open for what
```

Use `${HOME}/Workspaces/` unless the host has an established alternative.
Workspace names are short, descriptive and stable. The root `README.md` groups
the Workspaces into clusters — clients, products, internal operations — so an
agent can find the right one from a vague request. Provider-specific binding
files are allowed only where a provider needs local configuration; they consume
the Workspace and never describe it.

## What a Workspace README holds

| Section | Holds |
|---|---|
| Purpose and boundary | What this body of work is, and what belongs elsewhere |
| Local host scope | That every path applies to this machine only |
| Parts | A table: kind, role, location (path, URL or provider), instruction owner |
| Current state | Each part's actual status — live, in development, planned, retired — as it is now |
| Shared knowledge | Where notes, lore, cross-cutting to-dos and direction live, such as a Notion or Obsidian space, or "none yet" |
| Provider availability | Which routes were checked for local and cloud agents, with date and result |

**It records what is, never what is planned.** A Workspace is local: two
machines can each hold one for the same project. A roadmap, a to-do list or a
notebook written into it would diverge between them and contradict itself.
Plans, notes, shared to-dos, lore and the direction of the work belong to a
shared knowledge system — a Notion or Obsidian space, an issue tracker, a
repository's roadmap — which the Workspace names in its **Shared knowledge**
row so agents with a connector can read it. A planned part may appear in
**Parts** with the status "planned": that is the current state of the map, not
a plan.

Never put source code, customer files, credentials, generated output, issued
documents or transient work notes in a Workspace. They keep their own owners.

## The agent's duties

- **Enter through it.** At the start of work on a project, client, product or
  system, read the root `README.md`, find the matching Workspace and read its
  `README.md` and `AGENTS.md`, then the instructions of the part you enter. A
  part's own rules always win over the Workspace's.
- **Keep it current.** When the work creates, moves, renames, retires or changes
  the state of a part, update the affected Workspace in the same task, and the
  root `README.md` when clusters change. This happens when a task exposes the
  change; it is not a background watcher.
- **Propose, never create unasked.** When work spans several important parts
  and no Workspace covers it, say so once, with the parts you found: "This work
  spans the control-plane, network and runner repositories and a deployment at
  one provider; shall I create a Workspace for it?" Create it only after the
  user agrees. Never create one for a single repository, and never rename,
  merge or retire a Workspace on your own.
- **Stay local.** A Workspace describes this machine. Its existence proves
  nothing about another computer or a cloud session; a cloud agent without a
  verified mapping must stop at an unverified source instead of guessing a copy.

## Create or reconcile a Workspace

1. Confirm the user wants it, then resolve the host, the Workspace root and the
   body of work. Inspect existing Workspaces and AI-project settings before
   creating another owner.
2. Inventory every important part: repository, running system, provider,
   document root, shared drive, knowledge base. Record its role, location and
   instruction owner. Never infer a missing part from an old path.
3. Write `README.md` with the sections above and `AGENTS.md` so an entering
   agent reads the map, selects the right part and then that part's own rules.
4. Add the Workspace to the root `README.md` under its cluster; create the root
   files first if this is the machine's first Workspace.
5. Point requested AI applications at the Workspace directory as their project
   root; remove an old project-context owner once the new one is verified.
6. Check every path on this host and test provider access at the provider: a
   readable local file does not prove a saved project loaded it.

## Local and cloud boundary

Treat cloud access as unverified until checked for the named provider, account,
sync or upload route, destination and access mode. Record result, route and date
in **Provider availability**. Write `unavailable` only when the route was checked
and failed; otherwise keep `not checked`. One provider's sync proves nothing for
another provider, host or account. If a synced Workspace contains local absolute
paths, label them as local mappings.

## Moving a part

For a path migration, record dirty Git state and linked worktrees, check active
processes and provider projects, update consumers, repair path-sensitive Git
metadata, and verify the new path before retiring the old one. Preserve user
work byte for byte and leave historical logs unchanged unless they are active
configuration.

## Done when

The root and the Workspace's two files agree; every live part's location
resolves on this host; the current state matches reality; plans and notes are
referenced, not copied; requested AI projects enter through the Workspace; and
provider claims are verified. Report any cloud, restart or provider-interface
boundary that remains.
