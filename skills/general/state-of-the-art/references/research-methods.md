# Research methods for a bounded engineering decision

Read this reference when current claims are consequential or contested, when a
decision spans several source types, or when the ordinary documentation check
does not settle the alternatives. It teaches search and appraisal patterns; it
is not a permanent collection of recommended URLs or a substitute for live
source verification.

## Build the search from the question

Use a small search set that can find both support and disconfirmation:

| Search lens | Example shape |
|---|---|
| User need + constraint | `document retrieval tenant isolation small corpus latency` |
| Mechanism + failure mode | `vector index update filtering stale authorization behavior` |
| Candidate + official owner | `<candidate> official docs support lifecycle migration` |
| Alternative and baseline | `existing database search vs dedicated index operational cost` |
| Evidence that could challenge the proposal | `retrieval benchmark access filters update workload limitations` |
| Required guarantee + failure condition | `<actual mechanism> documented durability recovery interrupted operation guarantees` |
| Protection need + current component | `<component> <version> official security advisories affected configuration mitigation` |

Replace placeholders with the actual product, load, deployment, data and failure
conditions. Search synonyms when teams use different terms for the same mechanism.
Start with a few queries, inspect useful results and citations, then refine. Do
not use result count, rank or search-engine summaries as an evidence threshold.

## Select the source by claim

| Claim being checked | Best starting evidence | Check before relying on it |
|---|---|---|
| What a specification requires | The currently authoritative specification and its change history | Version, normative language, scope, compatibility and supersession |
| What a language, framework or SDK currently supports | Maintained official docs, API reference, release/support and migration notes | Exact version, runtime/environment, supported combinations, end-of-life and issue status |
| Whether a governing organization changed a policy | Its official decision, release, meeting record or announcement | Authority, date, what changed, effective date and affected component/version |
| Whether a method works under measured conditions | The study itself and, where available, independent replication or later research | Research question, sample/workload, comparison, metrics, threats to validity and publication status |
| Why a design failed operationally | A specific, first-person postmortem or engineering account | Author's role/date/context, observable evidence, selection bias and whether claim still holds |
| What a pattern means | Original paper/book or a reputable catalogue grounded in it | Intended forces, context, costs and whether it addresses the current need |
| Whether a known vulnerability applies | Maintainer/vendor advisory and authoritative vulnerability record | Exact affected/fixed versions, configuration, exposure, exploit prerequisites, mitigation and unresolved applicability |

Primary does not mean infallible: official documentation is authoritative for a
project's intended contract, while independent evidence may reveal gaps between
that contract and actual outcomes. Use the source appropriate to each claim and
state the distinction.

## Use scholarly discovery tools carefully

Discovery services can reveal terminology, papers and citation context. Examples
include arXiv, the ACM Digital Library and scite; availability, access, coverage
and product behavior can change, so verify them when used. Do not treat any one
search service as a vetted bibliography.

For each candidate paper, follow the title, DOI or stable identifier to the
publisher or author copy. Check whether it is peer reviewed, a preprint, workshop
paper, survey, benchmark or position paper. Read the abstract to triage, then the
method/results/limitations relevant to the claim. Inspect cited work and later
work, including replications or contradictory results where feasible. Citation
counts and “supporting/contrasting” labels help navigate; they do not establish
method quality or prove a claim.

For preprint repositories, verify the repository's moderation and review policy.
For example, check arXiv's own About or submission-policy pages for the distinction
between subject moderation and peer review. Do not infer one from the other.
A preprint can still be valuable; label its status and evaluate the work itself.
Verify publication or revision status at the publisher or conference when that
changes confidence.

## Appraise without manufacturing certainty

- Prefer direct evidence for the decisive constraint. Vendor comparison charts
  can establish product claims, not a neutral ranking among vendors.
- Separate normative requirements from recommendations, measured results and
  anecdotes. Preserve a source's qualifiers when paraphrasing it.
- Note publication date and relevant software version. For a current capability,
  locate the latest supported version and any breaking/deprecation notice rather
  than trusting an old tutorial.
- Evaluate research against its actual design: representative population/workload,
  baselines, operationalization of metrics, sample size, confounders, reproducible
  artifacts and stated validity threats. Do not demand one study prove a universal
  rule.
- For a practitioner's account, retain concrete context and label the author's
  experience as a lead or heuristic. Verify factual claims about current status,
  availability or organizational authority at the owner.
- If sources disagree, compare definitions, environment, workload, versions,
  incentives and time horizon. Explain whether they truly conflict, answer
  different questions or leave the issue unsettled. Don't let recency alone win.

## Keep a compact evidence record

For each decision-relevant assertion, record:

```text
Claim:
Source and author/owner:
Source type and publication/revision date:
Version, sample or context:
What it directly supports:
What it does not establish:
Competing or corroborating source:
Effect on this decision:
```

Use a research note only while the task needs it, under `.tmp/research/<topic>/`
or another approved temporary owner. Report useful primary citations in the
decision handoff; do not preserve raw search results as durable product docs.
