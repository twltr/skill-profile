---
name: workspace-management
description: Manage host-local, provider-neutral Workspace context folders and their AI-project bindings. Use when creating, renaming, moving, auditing, or retiring a Workspace; adding, removing, or moving one of its repositories or document roots; changing an AI project's local path; or when current work reveals stale Workspace context. Do not use to implement work inside the referenced repositories.
metadata:
  skill-type: core
---

# Workspace Management

**Core skill.** On the agent's surface and usable in any context.

Maintain one stable local context entry for a body of work that may span several
repositories, document roots and agent providers. A Workspace explains and
routes; it does not copy or replace the sources it references.

## A small finished map

**Illustrative host-local map:**

| Source | Canonical owner | This Mac | Cloud |
|---|---|---|---|
| Application repository | Git checkout and its `AGENTS.md` | Path checked | Not checked |
| Business records | Connected document store | Provider read verified | Not checked |

The Workspace links to both owners; it stores neither their contents nor a second
copy. “Not checked” records uncertainty; it does not assert that cloud access is
impossible. A provider read proves only the named account and route that were tested.

## Contract

- Use `${HOME}/Workspaces/<workspace-name>` unless the host has an established
  alternative. Names are short, descriptive and stable.
- `README.md` owns the human-readable context map. `AGENTS.md` owns instructions
  for agents entering through the Workspace.
- Source repositories, operational records and secrets retain their own owners.
  Do not put source code, customer files, credentials, generated output or
  transient plans in the Workspace.
- Provider-specific binding files are allowed only when a provider requires
  local configuration. Keep them minimal and treat them as consumers of the
  Workspace, never as its canonical description.
- A Workspace is local to the current host. Its existence proves nothing about
  another computer or a cloud execution environment.

## Establish or reconcile a Workspace

1. Resolve the current host, Workspace root and intended body of work. Inspect
   existing AI projects and nearby metadata before creating another owner.
2. Inventory every canonical source needed for the work: repository, document
   root, service configuration or shared system. Record its role, absolute
   local path and its own instruction entrypoint. Never infer a missing source
   from an old path.
3. Write or update `README.md` with:
   - purpose and ownership boundary;
   - a `Local host scope` section stating that paths apply only here;
   - a `Canonical sources` table with kind, role, path and instruction owner;
   - important separation rules and prohibited data placement;
   - a `Provider availability` table for local and cloud use.
4. Write or update `AGENTS.md` so an entering agent reads the Workspace map,
   selects the correct canonical source, then reads that source's own
   instructions before acting. It must not let Workspace instructions override
   a repository's or records system's local rules.
5. Configure each requested AI application to use the Workspace directory as
   its project root. Preserve a necessary provider binding, but remove the old
   project-context owner once the replacement has been verified.
6. Check every referenced path on the current host. Test provider discovery at
   the provider boundary; a readable local file is not proof that a saved
   project loaded it.

## Local and cloud boundary

Treat cloud access as unverified until checked for the named provider, account,
sync or upload mechanism, destination and access mode. Record the result, mechanism
and verification date in `README.md`. Use `unavailable` only when the relevant route
has been checked and found unavailable; otherwise retain `not checked`. Never
generalize one provider's sync to another provider, host or account.

If a synced Workspace contains local absolute paths, label them as local
mappings. A cloud agent must receive an explicit cloud-side mapping or stop at
the unverified source; it must not guess a checkout or silently operate on a
different copy.

## Keep context current

When authorized work creates, moves, replaces or retires a canonical source,
reconcile the affected Workspace in the same task. Automatic invocation means
the agent performs this reconciliation when a relevant task exposes the
change; it is not a background filesystem watcher.

For a path migration, record dirty Git state and linked worktrees, check active
processes and provider projects, update consumers, repair path-sensitive Git
metadata, and verify the new path before retiring the old one. Preserve user
work byte-for-byte and leave historical logs unchanged unless they are active
configuration.

## Completion

A Workspace change is complete when its two canonical files agree, every live
source path resolves on the current host, requested provider projects enter
through the Workspace, provider availability claims are verified, and no
active project metadata still owns the superseded path. Report any cloud,
process-restart or provider-UI boundary that remains.
