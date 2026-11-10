# Install and verify a skill

Read this reference when the user has requested installation, an update or runtime
distribution. It is not a prerequisite for writing or reviewing a skill.

## Resolve the source and target

Identify the maintained source, revision and complete skill directory. For an
external package, read its instructions, scripts and dependencies before installing;
retain its notices and licenses. Inspect existing target files before replacement.
A host-managed plugin should use its supported update mechanism rather than an
edit to a disposable cache. If ownership is unclear, resolve that before writing.

Discover the target client's active skill roots and metadata format. Current
Codex documentation describes `.agents/skills` locations, while the OpenAI
installer also supports `$CODEX_HOME/skills` and an explicit destination. Existing
installations can use either mechanism. Verify this runtime rather than moving
working copies because another path appears in documentation. Avoid duplicate
active copies with the same skill name.

Claude Code reads personal skills from `~/.claude/skills/<name>/SKILL.md`,
project skills from `.claude/skills/` and plugin skills from installed plugins.
Its explicit-only policy is the frontmatter field `disable-model-invocation: true`.
Skills uploaded to a claude.ai account are a separate store: the app's skill
settings list those, and the host syncs them down to Claude Code, while a local
`~/.claude/skills` folder does not appear in the app's skill list. A skill that
works in Claude Code but is "missing in the app" is usually in the wrong store,
not broken. Uploading to the account is an account change; confirm it first.

For other clients, inspect their current native mechanism. A directory accepted
by one host does not prove discovery by another. Copying a skill does not install
its tools, credentials, runtimes or account connections.

## Preserve and copy

1. Record the source revision and the target's current contents. Preserve differing
   installed files outside all active skill roots before replacing them.
2. Copy the complete approved skill tree, including metadata, scripts, references,
   assets, licenses and notices. Do not install only `SKILL.md`.
3. Apply an explicitly maintained host overlay by merging its named fields. Preserve
   unrelated interface values and policies; an update is not authority to change
   invocation, permissions or dependencies.
4. Compare relative filenames and file hashes. Identify intentional host-generated
   differences separately; do not silently treat unequal trees as identical.

When a supported installer is available, read its current instructions and command
help before calling it. OpenAI's installer can fetch an exact repository path and
revision, but its scripts are not bundled with Skill Issue. Do not assume a script
path exists or install Skill Creator merely to gain a command. Existing target
conflicts need reconciliation, not a forced overwrite.

## Keep descriptions separate from invocation policy

A `SKILL.md` begins with YAML metadata describing the task:

```yaml
---
name: interface-audit
description: Review a proposed interface for usability, visual hierarchy and consistency with its design system.
---
```

For Codex, a separate `agents/openai.yaml` can configure presentation and policy:

```yaml
interface:
  display_name: "Interface Audit"
  short_description: "Review interface usability and visual design"
policy:
  allow_implicit_invocation: false
```

The description explains the work. The policy restricts selection to an explicit
invocation. In Codex, omitting this policy defaults to allowing implicit selection.
The upstream metadata guide recommends a 25–64-character short description. Keep
supported icons, product fields and prompts when updating an existing package;
check the actual host schema before introducing or removing fields.

## Verify at each boundary

- **Files:** the intended complete tree is installed and preserved backups are outside discovery roots.
- **Metadata:** frontmatter and native metadata parse; the actual loader accepts the relevant fields and policy.
- **Discovery:** the target host reports the expected skill, path, description and invocation policy where exposed.
- **Behavior:** a fresh safe trial handles a matching request and avoids a nearby non-matching one. An explicit-only skill stays directly selectable.

Report which checks ran. File equality is not discovery; discovery is not a
successful model trial. Codex's current installer says changes are available on
the next turn. Other documentation suggests a restart if a change fails to appear.
Verify the actual catalog refresh before recommending disruption; never promise
that the current conversation's already-loaded instructions were replaced.

A local installation does not update Cloud, other machines or other clients.
Report distribution only for targets independently checked.

## Sources

- [OpenAI Skill Installer](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-installer/SKILL.md): repository install options and conflict behavior, reviewed 2026-11-04.
- [OpenAI metadata guide](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/references/openai_yaml.md): interface fields and short descriptions.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): current discovery paths, invocation policy and host behavior. Recheck version-sensitive guidance before a new rollout.
