---
name: grilling
description: Stress-test a plan, decision or idea by interviewing the user in prerequisite-aware rounds with recommended answers. Use for a requested human interview; a council that questions the lead agent belongs to Grilling with Agents.
metadata:
  skill-type: leaf
---

# Grilling

**Leaf skill** outside every tree; a person starts it by name.

Expose the assumptions and dependent decisions that an attractive plan can hide.
Interview the user until you reach a shared understanding. Map this as a **design
tree**: every decision branches into the decisions that hang off it. Working only
on questions whose prerequisites are settled prevents asking the user to decide
against facts or choices that may change in the next answer.

Keep the tree within the requested outcome and consequential decisions. Reuse
answers the user already supplied; unrelated possibilities do not create branches
to exhaust. Work the tree in **rounds**. The **frontier** is the in-scope decisions
whose prerequisites are settled: questions you can ask now without guessing at
answers you have not heard. Ask that frontier together, number each question and
give your recommended answer. Then wait for the user's answers before the next round.

## A dependent decision in two rounds

Fictional brief: decide access rules for a shared equipment reservation service.
The user has said it is for an internal team; whether guests may reserve is open.

```text
Round 1 — May guests reserve equipment, or only team members?
Recommendation: members only for the stated internal-team purpose.

User — Guests may reserve too, but a team member must sponsor each reservation.

Round 2 — Does sponsorship need approval before a reservation holds equipment?
Recommendation: yes, so an unapproved guest request cannot block team inventory.
```

The approval question depends on the guest-access answer. If the user had chosen
members only, that guest-specific branch would disappear. Other independent
questions can share a round; dependent questions wait for their prerequisite.

## Run the interview

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. Resolve straightforward environment
facts with the available tools. For a substantial independent investigation, use
Puppeteer when available to dispatch a bounded scout; a deterministic lookup does
not automatically need an agent. Do not ask the user for facts you can retrieve.
A running exploration is an unsettled prerequisite, so only downstream questions
wait for its result; ask the rest of the frontier now. The _decisions_ in this
human interview are the user's: put each to them and wait. Without Puppeteer,
keep the investigation bounded and distinguish checked facts from open evidence.

The session is done when the in-scope frontier is empty and consequential
assumptions are settled or explicitly unresolved. State any unresolved prerequisite
and the work it blocks; an inaccessible fact is not an answer. Summarize the
decisions and confirm shared understanding with the user before acting on the plan.
