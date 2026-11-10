# Evaluate a skill

Read this before writing the first test case, running a comparison or tuning a
description. It holds the formats and procedures; the reasons are in `SKILL.md`.

- [Test cases](#test-cases)
- [Runs and workspace](#runs-and-workspace)
- [Grading and reporting](#grading-and-reporting)
- [Trigger evaluation](#trigger-evaluation)
- [Blind comparison](#blind-comparison)

## Test cases

Store each test as its own folder under `evals/` in the skill. The layout is the
one `claude plugin eval` reads, so the same cases can later run from a terminal
or CI without conversion. Plain files work on every host.

```text
my-skill/evals/
└── flags-negative-quantity/   case name: lowercase-with-hyphens, says what is tested
    ├── prompt.md              settings block, then the user's prompt verbatim
    ├── case.yaml              name and a description of success
    ├── graders/               one file per assertion
    └── files/                 input files, only if the test needs any
```

Case names start with a letter and use lowercase letters, digits and hyphens.
Avoid `results`, `mocks`, `node_modules`, `files`, `true`, `false` and `null`.

`prompt.md` — the settings block is read only by the CLI; an unknown key there
makes the case fail to load, and the block ends at the first `---`, so keep free
text out of it:

```markdown
---
tags: [my-skill]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

ok so the orders export in files/orders.csv has some negative quantities, can you
flag them and give me the total revenue without them
Input files: orders.csv
```

`case.yaml` — quote the version, or it parses as a number:

```yaml
schema_version: "1.1"
name: flags-negative-quantity
expected_outcome: |
  Lists the rows with negative quantity and reports revenue excluding them.
```

`graders/NN-few-words.md` — one verifiable statement per file, numbered to keep
order. Phrase it about the result ("summary.md states a total revenue of 693.5"),
not about where a workflow saved it:

```markdown
---
type: llm
focus: trace
weight: 1
---

summary.md states a total revenue of 693.5
```

A case without a grader fails to load. Until real assertions exist, keep a
placeholder `graders/01-expected-output.md` with the same header and the body
`The result matches this description: <expected outcome>`; do not grade it
yourself. Leave graders of other types (`regex`, `file_exists`, `tool_used`,
`tool_order`, `baseline`) as written and grade what each describes.

For input files, add `place-files.sh` beside `prompt.md` and name it in
`case.yaml` under `context: { scaffold_script: place-files.sh }`:

```bash
#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
```

An older `evals/evals.json` still counts as tests; it belongs to the user, so do
not convert or delete it unless asked. Add new cases as folders.

With Claude Code available, `claude plugin eval . --allow-tools Write,Edit,Bash`
(plus `--scaffold` when cases have input files) runs every case with and without
the skill and writes its report under `evals/results/`. These are real, billed
model runs; offer them rather than starting them unasked. Check `--help` of the
installed version before relying on these flags.

## Runs and workspace

Keep results out of the skill and out of every active skill root, for example in
a repository's ignored `.tmp/` or a scratch directory:

```text
<skill-name>-workspace/
├── skill-snapshot/                  the previous version, for a revision baseline
└── iteration-1/
    └── flags-negative-quantity/
        ├── with_skill/outputs/
        └── old_skill/outputs/       or without_skill/ for a new skill
```

Keep case directory names stable across iterations so outputs can be compared.
Snapshot the skill before editing it (`cp -r <skill> <workspace>/skill-snapshot`).

Launch the with-skill run and its baseline in the same turn so they finish
together. A run handoff:

```text
Execute this task:
- Skill path: <path to the skill, or "none" for the baseline>
- Task: <prompt from prompt.md, without the settings block>
- Input files: <absolute paths, or "none">
- Save outputs to: <workspace>/iteration-<N>/<case>/<configuration>/outputs/
- Outputs to save: <what the user cares about, e.g. "the final CSV">
```

When a subagent finishes, record its reported token count and duration beside
its outputs immediately; hosts often report them only in the completion notice.

Without subagents, run each case yourself by reading the skill and following
it. Skip baselines and quantitative comparison, and say that the result is a
sanity check, not an independent trial.

## Grading and reporting

Grade assertions against outputs and transcripts. For anything a script can
check — a value in a file, a passing test, a valid schema — write the check and
run it; scripts are faster, repeatable and reusable across iterations. Note
assertions that pass with and without the skill: they do not discriminate and
should be sharpened or dropped. Note high-variance cases before trusting a mean.

Report to the user in the conversation, one block per case:

```markdown
### flags-negative-quantity
Prompt: "ok so the orders export … total revenue without them"
With skill: flags rows 14, 37; revenue 693.50 — 3/3 assertions
Baseline:   flags row 14 only; revenue 701.20 — 1/3 assertions
Difference: the skill's validation step catches negative values in column F
Cost: 41k tokens / 38 s vs 29k tokens / 25 s
```

Then ask what they would change. Empty feedback means a case looked fine;
concentrate revisions where the user had specific complaints.

If Anthropic's `skill-creator` is installed and the user wants its browser
viewer and benchmark aggregation, read its `SKILL.md` and follow its own
workspace and file formats instead of mixing them with these.

## Trigger evaluation

Write about twenty queries as JSON, roughly half that should trigger the skill:

```json
[
  {"query": "ok so my boss sent me 'Q4 sales final FINAL v2.xlsx' (in downloads) and wants a profit margin column, revenue is col C, costs col D i think", "should_trigger": true},
  {"query": "what's the difference between xlsx and csv for a 2 GB export?", "should_trigger": false}
]
```

Make queries concrete and specific: file paths, personal context, column names,
company names, a little backstory, casual phrasing, abbreviations and the odd
typo. Vary length. Bad: `"Format this data"`, `"Create a chart"`.

- **Should trigger:** different phrasings of the same intent, formal and casual;
  requests that never name the skill or file type but clearly need it; uncommon
  uses; cases where this skill competes with a neighbor and should win.
- **Should not trigger:** near-misses that share keywords but need something
  else — adjacent domains, ambiguous phrasing a keyword match would catch, the
  skill's topic in a context where another tool fits better. Obviously unrelated
  queries test nothing.

Review the set with the user; bad queries produce bad descriptions.

To run it, give each query to a fresh agent that sees the full skill catalog but
no hint which skill is under test, and record whether it consults the skill. Run
each query about three times, since selection is not deterministic. Hold out
about 40% of the queries, propose description changes only from failures in the
other 60%, and choose the final description by its held-out score so the wording
is not fitted to the examples. Report before/after descriptions and both scores.

Anthropic's `skill-creator` automates this loop in Claude Code through `claude -p`
(`python -m scripts.run_loop --eval-set <json> --skill-path <skill> --model <id>
--max-iterations 5 --verbose`, run from the skill-creator directory). Read its
current `SKILL.md` before using it; use the model that powers the user's actual
sessions so results match what they experience.

## Blind comparison

When the question is "is the new version actually better?", give the outputs of
both versions for the same prompt to an independent agent without saying which
is which, ask it to judge them against the case's expected outcome, then analyze
why the winner won. This needs subagents and is rarely necessary; the human
review usually suffices.
