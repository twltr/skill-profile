---
name: golden-comments
description: "Preserve named design intent, pattern relationships, system context and reasons beside source code so future maintainers can extend it correctly. Use whenever writing, changing, debugging, refactoring or reviewing source code, including ordinary feature and bug-fix tasks without a comment request."
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# Golden Comments

**Leaf skill** in Software Engineering; reached through its domain or by name.

Make source code carry the understanding needed to continue its design after the
conversation is gone. The next maintainer, human or agent, reads the code without
the chat, the review thread or the plan that produced it. They need what the code
cannot say by itself: what this unit serves in the larger system, why it has this
shape and what a seemingly harmless change would break.

Naming the actual pattern and its participants gives that reader a searchable
handle for related code and established knowledge; explaining their relationship
shows how to continue the design. An unnamed construction leaves the next change
to guesswork, and a pattern label without its local reason leaves the same gap.

## When it applies

This is part of implementation, not a later writing pass. Apply it to each new
or substantively changed source file, without waiting for a documentation request:

1. **Before editing,** read the affected unit's existing briefing and comments.
   Note the named construction and decisions the change must preserve.
2. **While implementing,** write or update the explanation together with the
   mechanism it explains.
3. **Before finishing,** check for accepted reasons that still live only in the
   conversation, plan or final reply, and move them beside the code.

Judge coverage by what a future reader would have to reconstruct, not by a
comment count. Important modules, public boundaries and policy owners need a
local explanation; a self-explanatory leaf needs none. A spelling or
formatting-only edit keeps existing explanations and adds no design prose. A
comment-only assignment does not authorize redesigning the code.

## Example: the reason at its mechanism

Fictional task: users who click "Pay" twice are charged twice. The fix adds a
deduplication check. A typical comment restates the code:

```python
# Check if charge exists, otherwise create it
with db.transaction():
    if existing := charges.find_by_attempt(attempt_id):
        return existing
    return charges.create(attempt_id, order, provider.capture(order))
```

The reader can see that much. What they cannot see is why the key is the
attempt rather than the order, and why the check sits inside the transaction:

```python
# Critical: deduplicate on the client's payment-attempt ID, not the order ID.
# A double click or network retry resends the same attempt and must receive the
# first charge; a deliberate new attempt (another card after a decline) carries
# a new ID and must reach the provider. Check and insert share one transaction
# so two concurrent retries cannot both pass the check.
with db.transaction():
    if existing := charges.find_by_attempt(attempt_id):
        return existing
    return charges.create(attempt_id, order, provider.capture(order))
```

The comment names the decision, the rejected alternative, the case that tells
them apart and the invariant a refactoring could break. It leaves out what the
code already says, the ticket number and who decided. Before writing such a
claim, verify it against the real code: here, that `find_by_attempt` and
`create` really run in the same transaction.

## Find the explanation's local owner

Read the mechanism and its requirements before writing about it. Identify what a
new maintainer cannot safely infer — the architectural model, dependency
direction, invariant, assumption, ordering or failure mode — and explain it at
the narrowest place that owns the reason.

Recover accepted decisions from the current conversation, design review or
handoff while that evidence is still available. Translate the settled rationale
into durable prose; do not paste the conversation or its participants into code.
Keep any meaningful condition for revisiting the decision. Alternatives that are
still open stay with whoever owns the decision; they must not become an invented
account of why the code is right.

Name the established patterns the unit actually implements, with their concrete
participants, and explain why they were chosen here and how they interact with
adjacent mechanisms. "Command dispatcher, state machine, Gateway" is a list; the
design is how the dispatcher hands transitions to the state machine and why the
Gateway keeps provider fields out of both. Check a pattern's defining roles in
the code before naming it. Give a genuinely local mechanism an honest descriptive
name, and mark an uncertain mapping as uncertain.

If an explanation contradicts the code, establish whether the code is wrong, the
explanation stale or the requirement changed. A comment never justifies a known
defect; surface an unresolved behavior decision instead of inventing a reason.

## Brief the important entrypoints

A package docstring, important script header or migration header is a compact
local architecture briefing. Pick the questions this entrypoint actually needs
answered; they are not mandatory headings:

| The briefing answers | Worth it when |
|---|---|
| What does this unit do, and which way does work flow? | Always, in a sentence |
| Who calls it, what does it rely on, which decision does it own? | The unit is small but holds a boundary, e.g. the only writer of a transition |
| Which pattern does it implement, with which participants? | A named construction spans several files or types |
| Why this construction instead of the obvious alternative? | A simpler-looking option was rejected for a reason |
| What do its names, states and outcomes mean here? | A term means something narrower than its everyday sense |
| What must remain true? What must it never start owning? | Drift would create a second truth |
| When should the decision be revisited? | The choice depends on a load, scale or requirement that may change |

Fictional briefing for a module that connects several mechanisms:

```python
"""Dispatch Commands while lifecycle.py owns the task state machine.

The registry selects a handler for each decoded command. Handlers request state
changes through lifecycle.transition and call providers through CatalogGateway.
Command dispatch keeps transport parsing out of execution; the state machine
prevents handlers from inventing transitions; the Gateway keeps provider fields
out of both. These boundaries let several transports share one lifecycle policy.

Add a command through its registry entry. Change lifecycle policy at its
transition owner, not in a second handler branch. Reassess this synchronous
dispatch if commands need durable delivery: the registry provides no persistence
or replay. See docs/architecture.md#patterns for the system view.
"""
```

It names the participants, says what each boundary prevents, tells the next
maintainer where to extend and when to reconsider, and links the wider view
instead of copying it. Write coherent prose like this rather than a stack of
labels, and name relevant siblings only where they give a useful route, not as
an inventory of the package. Detailed local reasons still belong beside their
mechanism further down.

## Explain where the voltage is

Ordinary design decisions deserve a reason as much as dangerous ones: why a
factory centralizes construction, why an observer is unsubscribed at this
lifetime boundary, why a pipeline owns ordering. Security and concurrency are
not the only reasons to leave a useful comment.

Where a small change can create a second truth, a race or data loss, a comment
is required. Look closely at optimistic concurrency, idempotency, event
append/load boundaries, projection cursors, transactions, retry, claim and lease
logic, deletion gates, authentication and secrets, reconciliation, cross-system
calls, semantic nil/default branches, silent skips, ID conversions and migration
bridges. The list says where to look, not where to add comments mechanically.
When a severity cue helps, start with `Important:` or `Critical:` and name the
consequence, as in the example above.

If documentation says "must" while the code permits the opposite, a reassuring
comment is not a repair: state the real invariant, or fix the construction
within the authorized scope.

## What stays out of source

Source prose serves the product's next developer. It is written in the
repository's language, in complete sentences, and says nothing about how it was
produced:

| Instead of | Because | Write |
|---|---|---|
| `# Golden comment:` or `# agent note:` | Authoring categories are not product language | The reason itself |
| `# Added after review with Claude` | Process and authorship, not design | Why the construction is safe |
| `# Fix for CC16, wave 3` | Planning coordinates expire | The behavior, linked to its contract or chapter |
| `# Increment retry counter` | Restates the code | Nothing, or why the retry is safe |
| `# Never null here` while a branch returns `None` | Reassurance over a defect | The real invariant, or a fix |
| A pasted design discussion | Participants and dead ends are noise | The settled decision and its revisit condition |

An agent that is an actual domain or runtime concept can of course be named.
Use section banners only at real phase boundaries. In migration code, name the
target owner, the temporary bridge and the retiring implementation, and state
the bridge's removal condition.

## Keep one owner per explanation

Detailed construction and decision reasons live beside their implementation.
Repository documentation owns the overall architecture, pattern navigation,
cross-module contracts and operating procedures. Link between them instead of
copying: a short orientation in both places helps, two independently maintained
accounts of the same rule drift apart. When a change affects a repository
explanation, update it or report the verified change and its source anchors to
the lead.

When behavior changes, revise the nearby explanation in the same work.
Consolidate corrections into one coherent comment rather than stacking defensive
paragraphs after each edit; removing repetition is good, removing reasons is not.

## Check before finishing

Read each affected important file as a maintainer with no chat history:

- Can they name its patterns and participants and say how they cooperate?
- Can they find where to extend it and when to reconsider the decision?
- Does every ownership, ordering and failure claim match the mechanism, and does
  every referenced path exist?
- Is any accepted reason still only in the plan or final reply?

Return the revised commentary and any unresolved model question to whoever
loaded this method. Use the work's ordinary verification; a prose-only change
does not need new tests.
