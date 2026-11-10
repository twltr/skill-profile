---
name: workspace-management
description: Find, read and keep current the local Workspace that maps a body of work spanning several repositories, systems, providers or document stores, so the agent is onboarded without being told. Use at the start of any work on a project, client, product or system — even when the user only says "let's work on X" — and whenever work changes where its parts live or what state they are in. Also keeps the machine's agent environment — instruction files, agent profile, skill collection — current at session start. Propose, never create unasked, a Workspace when multi-part work has none; a single repository never needs one.
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
   its repositories, at a recorded path, with its own `AGENTS.md`; its role
   agents run on a server reached through an MCP connection; shared notes live
   in a named knowledge base.
3. Check the Workspace's required access: the MCP connection to that server is
   not configured in this client. Say so before starting — "I can read the
   dispatcher code, but I cannot reach the role agents without the MCP
   connection" — instead of working around it.
4. Enter the dispatcher repository and read its own instructions before acting.
5. After the work, if a part moved, appeared, retired or changed state, update
   the Workspace in the same task.

**A single repository is not a Workspace.** "Fix the login bug in my notes app"
— one repository with its own `README.md` and `AGENTS.md` — needs no Workspace;
the repository is its own map. It becomes Workspace-worthy only when the work
grows into several important parts that belong together.

## What is Workspace-worthy

A Workspace covers one coherent body of work made of **more than one important
part**: several repositories, running systems and their providers, servers with
their agents, scheduled automations, document roots, shared drives,
infrastructure, or accounts that together serve one purpose — a client, a product line, an operating model, an agent system. Ask:
would an agent entering one part miss something it needs from another? If yes,
it is Workspace-worthy. If everything lives in one repository, it is not.

## Layout

```text
~/Workspaces/
├── README.md        this machine's view: its agent environment, clusters of
│                    Workspaces, where shared knowledge lives
├── AGENTS.md        rules for every Workspace on this machine
├── CLAUDE.md        a pointer to AGENTS.md (one line: @AGENTS.md)
└── <workspace>/
    ├── README.md    the map: purpose, parts, their state, boundaries
    ├── AGENTS.md    how an agent enters: which part to open for what
    └── CLAUDE.md    a pointer to AGENTS.md
```

Use `${HOME}/Workspaces/` unless the host has an established alternative.
Workspace names are short, descriptive and stable. The root `README.md` groups
the Workspaces into clusters — clients, products, internal operations — so an
agent can find the right one from a vague request. Provider-specific binding
files are allowed only where a provider needs local configuration; they consume
the Workspace and never describe it.

## The agent environment

The root `README.md` also describes how agents are set up on this machine, in
an **Agent environment** section: the repository that owns the global agent
profile, the repository that owns the skill collection, the command that
installs both into the local clients, and where the local checkouts live. These
are parts of the machine's view like any other, and they change how every
session behaves.

**One instruction file per level, the others point to it.** At the root, in
each Workspace and in the global profile, `AGENTS.md` is the canonical
instruction file. Files that other agents read — `CLAUDE.md`, `GEMINI.md` and the
like — contain only a pointer to it, such as Claude Code's `@AGENTS.md` import,
or are generated from it by the profile's installer. Never maintain two copies:
they drift, and each agent then follows different rules.

**Check it once at the start of a session.** When the root `README.md` names an
agent environment:

1. Fetch the profile and skill repositories and compare the local checkouts with
   their remotes.
2. If a remote has new commits and the local checkout is clean, fast-forward it
   and run the named install command, then read its result.
3. If nothing is new and the install command's audit reports no difference,
   assume the machine is current and go on with the task — no further checks.
4. If a checkout has local changes, is ahead of or diverged from its remote, or
   the audit reports a conflict, report that and do not overwrite anything.

A plain fetch and audit cost seconds; skip the check when the session already
ran it. Changing the profile or the skills themselves remains work in their own
repositories, under their own instructions.

## What a Workspace README holds

| Section | Holds |
|---|---|
| Purpose and boundary | What this body of work is, and what belongs elsewhere |
| Local host scope | That every path applies to this machine only |
| Parts | A table: kind, role, location (path, URL, host or provider), instruction owner — including running systems and scheduled automations |
| Agents and accounts | Which agents act on this work — automations, role agents on a server, the owner's local assistants — with which account or seat, and which of them may process customer data under which agreement |
| Access and credentials | For every part: how it is reached — provider, management CLI, SSH alias, console — and where its credentials are kept — keychain item, password-manager vault and entry, path on a server. Locations and names only, never values |
| Required access | The tools, connectors, MCP servers and logins an agent needs to work here, and whether each is set up in the clients on this machine |
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

**While no shared knowledge system is connected**, a Workspace may also hold the
owner's current view of the wider system: a known dependency on one provider, an
option under consideration, a part whose future is open. That is still state,
seen from here, but it can change or turn out wrong. Put it under **Current
state** in its own subsection marked provisional, with its date, and say that it
moves to the knowledge system once one exists. The exception ends when the
**Shared knowledge** row names a connected system: then move such subsections
there and leave a pointer. Never turn the exception into a roadmap or to-do
list; open work still belongs to its repository's issues or roadmap.

Record which account an agent uses, never its credentials. When customer data is
involved, the **Agents and accounts** row decides which agent may touch it; a
local assistant without that agreement works through the agents that have it.

Never put source code, customer files, credentials, generated output, issued
documents or transient work notes in a Workspace. They keep their own owners.

## The agent's duties

- **Enter through it.** At the start of work on a project, client, product or
  system, read the root `README.md`, find the matching Workspace and read its
  `README.md` and `AGENTS.md`, then the instructions of the part you enter. A
  part's own rules always win over the Workspace's.
- **Check the required access first.** If a tool, connector or login the
  Workspace lists is missing in this client, report it at once with what it
  blocks; do the work it does not block, and never pretend a missing route was
  used.
- **Keep it current.** When the work creates, moves, renames, retires or changes
  the state of a part, update the affected Workspace in the same task, and the
  root `README.md` when clusters change.
- **Record what you had to find out.** When you discover how a part is reached
  or where its credentials live — a provider console, a CLI, an SSH alias, a
  keychain item, a vault entry — add it to **Access and credentials** in the same
  task. The owner should never have to remember it; the next agent should never
  have to search for it again. This happens when a task exposes the
  change; it is not a background watcher.
- **Propose, never create unasked.** When work spans several important parts
  and no Workspace covers it, say so once, with the parts you found: "This work
  spans the control-plane, network and runner repositories and a deployment at
  one provider; shall I create a Workspace for it?" Create it only after the
  user agrees. Never create one for a single repository, and never rename,
  merge or retire a Workspace on your own.
- **Keep instruction files single.** When you change a Workspace's rules, edit
  its `AGENTS.md`; make sure every other agent's instruction file there is only
  a pointer to it.
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
3. Write `README.md` with the sections above, `AGENTS.md` so an entering agent
   reads the map, selects the right part and then that part's own rules, and a
   `CLAUDE.md` (or the host's equivalent) that only points to `AGENTS.md`.
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

The root and the Workspace's files agree, and every non-canonical instruction
file only points to `AGENTS.md`; every live part's location
resolves on this host; the current state matches reality; plans and notes are
referenced, not copied, and any provisional view is dated and marked; requested AI projects enter through the Workspace; and
provider claims are verified. Report any cloud, restart or provider-interface
boundary that remains.
