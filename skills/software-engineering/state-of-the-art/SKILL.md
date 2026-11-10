---
name: state-of-the-art
description: Research current practice and evidence for a defined engineering question, then return a scoped, cited decision handoff with alternatives and limits. Use when a language, framework, dependency, protocol, pattern, architecture or security choice should rest on current primary sources rather than memory, including version support, deprecations, advisories and published research.
metadata:
  skill-type: leaf
  skill-tree: software-engineering
---

# State of the Art

**Leaf skill** in Software Engineering; reached through its domain or by name.

Research only as far as the decision needs. Start from the user's outcome and
actual system, then work down to the specific question evidence can answer. The
state of the art is not whatever was published most recently: it is the best
supported, current fit for this problem, its constraints and its maintenance
horizon. Remembered facts about versions and support go stale quickly, which is
why the owner of each claim is checked rather than recalled.

## A small example

Fictional request: "Should this new support tool use a separate vector database
for search?" The product has about five thousand documents, an existing
database, strict per-customer access rules and no agreed search-quality target.

Do not begin by searching "best vector database". Reframe the decision:

```text
Outcome: agents find relevant support documents without crossing customer boundaries.
Unknowns: semantic retrieval need, corpus growth and update rate, latency and recall target.
Alternatives: the existing database's search features; a separately operated index;
keyword search, if it meets the need.
Evidence: official docs for filtering, updates and access control at the deployed
versions; research on comparable retrieval tasks; a small test on permitted data.
```

The handoff then takes this shape. Its findings are invented for illustration,
and the angle brackets mark where real citations belong:

```markdown
## Decision question
Does support search need a separate vector index for ~5k documents under
per-customer access rules?

## Findings
- The deployed database filters vector and full-text queries by row-level access
  rules. <official docs, version, checked date> Does not establish relevance.
- Comparable small-corpus studies show hybrid keyword and vector retrieval close
  to dedicated indexes. <paper, venue, year> Workload differs; preprint.

## Alternatives
Existing database search (keyword or hybrid); a separate managed index.

## Recommendation
Stay on the existing database for now. A separate index adds a second copy of
access rules to keep in sync and has no measured gap to justify it.

## Limits
No relevance target agreed; corpus growth unknown.

## Next check
Fifty real queries with expected documents against keyword and hybrid search.
Revisit the index only if both miss the agreed target.
```

This is a conditional example, not a default recommendation about databases.
The handoff states what the evidence did and did not establish and leaves
implementation to its own task.

## Frame the question before searching

1. **Name the outcome and scope.** A new system, a substantial feature, a
   decision inside an existing repository or a small local change? Match depth
   to consequence: a local choice may need only the repository's contract and
   current official documentation; a new system may need broader alternatives,
   research and an operational comparison.
2. **Read the actual context.** When a repository exists, inspect its relevant
   architecture, contracts, supported environment, dependencies, decisions and
   tests, so you do not research a greenfield system on top of a working one.
3. **Write a decision question.** Start with the user or system need, then add the
   constraints that change the answer: workload, data and trust boundary,
   latency and availability, deployment, team experience, growth, budget and
   lifetime. Separate verified facts from assumptions and missing evidence.
4. **Break it into answerable parts.** Name the mechanism or behavior to
   establish, the viable alternatives and the evidence that could distinguish
   them. Search by problem, constraint and mechanism, including credible failure
   modes, not only for support of the first proposed solution.

"Which framework is best?" becomes "For this team's deployment target and
required background jobs, what do the maintained candidates support, which
compatibility or lifecycle constraints apply, and what must a representative
slice prove?" Likewise, "Which persistence pattern should we add?" becomes "What
must remain true after this work is interrupted, and what can the system actually
establish?" — a reproducible calculation may simply restart, while an external
action whose result was lost stays uncertain until evidence settles it. Include
evidence that could justify keeping the simpler design.

Use the scoped questions you were given, when there are any. Otherwise pick the
dimensions that could change this outcome — data lifecycle, consistency, failure
and recovery, communication contracts, security, language and architecture fit,
operational and human constraints — across the full spectrum for a new
application, and along the affected guarantees for a feature. A settled choice
may need no new research.

## Find and judge evidence

Prefer the source that owns the claim:

| Claim | Start with | Watch for |
|---|---|---|
| Current language, framework, SDK, protocol or standard behavior | Official specification, API docs, support policy, release and migration notes | Exact versions and support dates; a spec, an SDK and a provider service are separate claims |
| Measured or general claims | The paper itself: method, sample, date, venue, limitations, later work | Search rankings and generated summaries are leads, not evidence |
| Pattern meaning and design language | The original or authoritative catalogue or book | A pattern describes forces and a response, not an obligation |
| Operational lessons | First-person engineering accounts | Label as experience; verify current claims; one company's scale is not a standard |

Check disagreement rather than flattening it. Compare the systems, eras,
workloads, definitions and assumptions behind each claim, search for credible
counterevidence, follow primary citations, and distinguish a normative
requirement, documented capability, empirical result, maintainer recommendation
and anecdote. Check an author's role or an organization's ownership only when
that authority matters to the claim.

For security-relevant decisions, check current maintainer or vendor advisories
and authoritative vulnerability records for the actual component and version:
affected and fixed ranges, configuration and exploit prerequisites, exposure,
mitigations, support status and verified exploitation. Distinguish a confirmed
match, an evidence-backed exclusion and an open applicability question. A
severity score or known-exploited list helps prioritize but does not replace that
analysis, and finding no results is not proof of safety. Record the check date.
Scale the work to the changed trust boundary; a small unrelated edit does not
need a whole-system audit.

Recent is not the same as current. Check the owner's latest release and support
information and any migration or deprecation notice; a newer release can be
unsuitable or less supported for this use. Do not infer a governing body's
decision from a video, forum post or search snippet when the decision itself
matters.

For search patterns, scholarly discovery services and their caveats, research
appraisal and a per-claim evidence record, read
[Research methods](references/research-methods.md) when the decision is
consequential, claims are contested, or the search goes beyond a direct
documentation check.

## Compose the handoff

Return the handoff in the shape the example shows: decision question with scope
and constraints; findings with direct citations and dates or versions; credible
alternatives; the recommendation and its reasons; uncertainty, source limits and
what would change the conclusion; and the smallest useful next check. Make a
choice when the brief and the evidence support one. Keep unknown facts unknown,
and separate a preference or authorization boundary from an engineering
conclusion.

Keep scratch research in `.tmp/research/<topic>/` or another temporary location
the task allows, as a compact note rather than a link collection or diary. Move
accepted decisions and primary citations to the canonical plan, issue or
maintained documentation, then remove the notes once their job is done. If the
research was requested for an existing plan, return the result there rather than
creating a parallel record.

## Boundaries

- This method supplies scoped evidence, citations and a recommendation; weighing
  the engineering trade-offs and implementing the choice stay with the lead.
  Return the handoff to whoever loaded this method; do not start a new plan,
  council or implementation of your own.
- When the decision is technical and consequential, challenge your own candidate:
  argue the strongest alternative and test the assumptions against the evidence,
  without turning that into questions for the user.
- When concepts, names, module boundaries or structure turn out to be unsettled,
  report them as open questions instead of settling them inside the research.
- If **Puppeteer** is available and the research splits into independent,
  substantial questions, delegate them before loading large source sets into the
  lead's context. Give every investigator the same requirements and cross-topic
  constraints, keep briefs bounded, forbid further delegation and verify decisive
  returned claims against their cited sources. Reconcile incompatible assumptions
  before the handoff: separate plausible reports do not yet make a coherent
  design. Do not delegate a simple lookup.
- If a research service, source or supporting skill is unavailable, continue with
  what is possible and say what was not accessible; never imply it was used. This
  method grants no access, permission or credentials.
