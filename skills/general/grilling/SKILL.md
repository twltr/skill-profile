---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

# Grilling

Expose the assumptions and dependent decisions that an attractive plan can hide.
Interview the user until you reach a shared understanding. Map this as a **design
tree**: every decision branches into the decisions that hang off it. Working only
on questions whose prerequisites are settled prevents asking the user to decide
against facts or choices that may change in the next answer.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

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

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
