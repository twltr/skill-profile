---
name: state-of-the-art
description: Research current practice and evidence for a defined engineering question, then return a scoped, cited decision handoff with alternatives and limits.
---

# State of the Art

Research only as far as the decision needs. Start from the user's outcome and
actual system, then work down to the specific question evidence can answer. The
state of the art is not whatever was published most recently: it is the best
supported, current fit for this problem, constraints and maintenance horizon.

## A small example

Fictional request: “Should this new support tool use a separate vector database
for search?” The product has a small document collection, an existing database,
strict per-customer access rules and no measured search-quality target.

Do not begin by searching “best vector database.” Reframe the decision:

```text
Outcome: agents can find relevant support documents without crossing customer boundaries.
Unknowns: semantic retrieval need, corpus growth/update rate, latency and recall target.
Alternatives: existing search facilities; a separately operated index; keep keyword
search if it meets the need.
Evidence to gather: current official docs for filtering, update and access behavior;
research on comparable retrieval tasks; a small test on representative, permitted data.
```

If the existing search passes the agreed relevance and access tests, a separate
service has not earned its operational cost yet. If it fails, compare supported
index options against the measured gap. This is a conditional example, not a
default recommendation about databases. The handoff should link exact sources,
state what the test did and did not establish, and leave implementation to its
own task owner.

## Frame the question before searching

1. **Name the outcome and scope.** Is this a new system, a substantial feature,
   a decision inside an existing repository, or a small local change? Match search
   depth to the consequence: a local choice may need the repository contract and
   current official documentation; a new system may need broader alternatives,
   research and an operational comparison.
2. **Read the actual context.** When a repository exists, inspect its relevant
   architecture, contracts, supported environment, dependencies, decisions and
   tests. Do not research a greenfield system on top of a working system by mistake.
3. **Write a decision question.** Start with the user or system need, then add the
   constraints that change the answer: users and workload, data and trust boundary,
   latency/availability, deployment, team experience, growth, budget and lifetime.
   Separate verified facts from assumptions and missing evidence.
4. **Break the question into answerable parts.** Identify the mechanism or behavior
   to establish, the viable alternatives, and which evidence could distinguish them.
   Search by problem + constraint + mechanism, including credible failure modes;
   do not only search for support for the first proposed solution.

For example, replace “Which framework is best?” with “For this team's existing
deployment target and required background jobs, what do the maintained candidate
frameworks support, what compatibility or lifecycle constraints apply, and what
must a representative slice prove?”

## Find and judge evidence

Prefer the source that owns the claim:

- For current language, framework, SDK, protocol or standards behavior, consult
  its official specification, API documentation, support policy, migration guide,
  release notes and authoritative change announcements. Verify exact versions and
  support dates when they affect the decision. A spec, SDK and provider service are
  separate claims.
- For measured or generalizable claims, discover relevant scholarly work and inspect
  the paper itself, its methods, sample, date, venue/review status, limitations and
  later work. Search services and citation tools help find and contextualize papers;
  their rankings or generated summaries are leads, not substitutes for the papers.
- For established patterns and design language, use the original or authoritative
  catalogue/book where possible. A pattern describes forces and a possible response;
  it is not a requirement to install that architecture.
- For operational lessons, first-person engineering accounts can reveal failure
  modes and questions worth checking. Label them as experience or opinion, verify
  current technical claims independently, and do not elevate one company's scale
  or practice into a universal standard.

Examples of discovery places include arXiv, ACM's Digital Library and scite. They
are examples only: verify that a service exists, is accessible and has the relevant
coverage at the time of use. arXiv hosting or moderation does not itself mean peer
review; citation context from a tool does not prove a result is correct. Verify
publication status, corrections/retractions and the work's actual scope.

Check disagreement rather than flattening it. Compare the systems, eras, workload,
definitions and assumptions behind each claim. Search for credible counterevidence
and alternatives, follow primary citations, and distinguish a normative requirement,
documented capability, empirical result, maintainer recommendation and anecdote.
Check an author's current role or an organization's current ownership only when
that authority is material to the claim.

No result should be called current merely because it is recent. Check the owner's
latest release/support information and any applicable migration or deprecation
notice; a newer release can be unsuitable, incompatible or less supported for this
use. Do not infer a governing body's decision from a video, forum post or search
snippet when the decision itself matters.

For source discovery tactics, research-quality checks and a compact evidence
record, read [Research methods](references/research-methods.md) when the decision
is consequential, claims are contested, or the search is broader than a direct
documentation check.

## Compose the handoff

Return the decision question, scope and constraints; the findings with direct
citations and dates/versions; credible alternatives; recommendation and reasons;
uncertainty, source limitations and what would change the conclusion; and the
smallest useful experiment or verification. Make a choice when the caller's brief
and evidence support one. Keep unknown facts unknown and distinguish a preference
or authorization boundary from an engineering conclusion.

Put scratch research only in `.tmp/research/<topic>/` or another explicitly
approved temporary owner. A compact note should capture the question, useful
evidence, source identity/date/version, competing interpretations and conclusion;
do not make a permanent URL collection or research diary. Move accepted decisions
and primary citations to their canonical plan, issue or maintained documentation,
then clean temporary notes when their job is done. If the result belongs to an
active caller's plan, return it there instead of creating a parallel owner.

## Use related methods only when they fit

- If **Engineering Practices** is available, use it for evaluating the actual
  engineering trade-offs; this skill supplies the scoped evidence and citations.
  If it is already the caller or an active ancestor, return the evidence and
  recommendation to that owner instead of invoking it again.
- If **Puppeteer** is available, delegate independent, meaningful research questions
  or a second design comparison before loading large source sets into the lead's
  context. Keep briefs bounded, prohibit recursive delegation, and verify decisive
  returned claims against their cited sources. Do not delegate a simple lookup.
- If **Grilling with Agents** is available and the decision is technical and
  consequential, use it to challenge the evidence and candidate decision. It always
  returns a reasoned report without user questions; no mode selection is needed.
  Return decisions, reasons and unresolved prerequisites to the caller and its
  existing plan; do not relay council questions to the user or launch
  another council if one is already active in the calling workflow. Without it, challenge the strongest
  alternative and assumptions directly.
- If **Domain Modeling** is available and concepts or names are unsettled, use it
  only for those questions. If **Vertical Slices** is available and boundaries or
  module structure are in scope, use it for structure. Do not duplicate their
  methods in this research or invent a glossary/architecture owner here.
- If **Road to Glory** is available and accepted downstream work is substantial,
  hand its owner the settled evidence and decisions. If this research was requested
  by an active Road to Glory plan, return there; do not create a second plan or
  start implementation. Small verified choices need no roadmap entry.

If a supporting skill or research service is unavailable, continue with the
bounded work possible, say what was not applied or accessible, and do not imply it
was used. These skills do not grant access, permission or credentials.
Carry the active workflow names into delegated briefs. A method already active
in the call chain receives the result; it is not entered again as a new workflow.
