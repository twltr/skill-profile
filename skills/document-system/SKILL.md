---
name: document-system
description: Write or restructure system documentation around reader questions and verified behavior. Use for architecture explanations, documentation books and substantial README work; a small factual correction does not need a new documentation structure.
---

# Document System

Explain how the system works and why it has this shape so a new maintainer can
find the relevant context and change it safely.

## Find the question and its owner

Establish the intended reader and the question the text must answer. Read the
existing documentation map and the relevant implementation or contract. Resolve
disagreement as stale explanation, incorrect behavior or a changed requirement;
do not make documentation endorse an implementation defect. Mark unbuilt intent
as such, and preserve uncertainty when authoritative evidence is unavailable.

Locate the existing owner before creating a page. A chapter earns its place
when it explains a coherent capability, mechanism or contract that can be
understood independently. Details of that owner belong inside it; a central
duplicate inventory of every local invariant is not a new capability.

## Shape the explanation

For a multi-part system book, keep a stable numbered order from orientation and
prerequisite concepts through relationships to detail. Its map should support
both a human reading forward and a reader looking up one question. The order
does not require agents to read every earlier chapter for each task. Preserve
an established structure outside the requested change.

Choose the text's job: tutorial, how-to, explanation or reference. Use only the
chapter elements that answer that job: purpose, construction, reasons and
meaningful alternatives, invariants, patterns, failure modes and sources.
Do not apply the same checklist to every page. Prefer a table or diagram when
it explains relationships more clearly than prose.

Explain the model and the reason behind the choice, not a line-by-line copy of
the code. State the assumptions a newcomer must not make. Place an invariant
beside the capability that enforces it, naming the mechanism and consequence;
keep only system-wide invariants at the architectural level. Link the primary
source of a meaningful applied pattern through the project's existing reference
owner rather than duplicating a catalog throughout the book.

Write critical code comments where separating the explanation would hide a
risk, especially ordering, concurrency, retries, deletion and external calls.
Explain why the construction must work this way. Consolidate stale corrections
in place and use durable domain vocabulary instead of authoring history.

## Orient and verify

A README should quickly explain the purpose, distinctive constraints, working
entry commands and prerequisites, then route readers into the deeper material.
Cover only environments the project actually supports. Give configuration or
deployment its own explanation when its complexity earns it; keep one-time
operational records with history rather than inside the system book.

Verify named paths, interfaces and states against their owners. Exercise safe
documented commands in the relevant environment; identify commands that cannot
be verified without unavailable access or an external effect. Check the map
and links after moves, and recheck a claim whose evidence pointer was broken.

Deliver the revised canonical text and the observed checks. Keep useful reasons
and failure information while removing repetition; documentation volume is not
a reason to erase information a maintainer needs.
