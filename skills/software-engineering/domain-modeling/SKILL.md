---
name: domain-modeling
description: Clarify domain concepts, names, relationships and lifecycle rules while designing or changing software. Resolve overloaded terms through concrete scenarios and actual behavior, and keep the agreed vocabulary with its canonical owner.
---

# Domain Modeling

Make the system's language express the actual concepts. Use this method when a
design or change introduces meanings, relationships or names; an ordinary edit
with already-settled vocabulary only needs to follow that vocabulary.

## A worked distinction

Fictional request: "An account can invite another account."

```text
Counterexample: Can one customer organization have several people who sign in?
Answer from the brief: yes. One person can also belong to two organizations.

Resolved concepts:
Organization — the customer entity that owns the subscription.
User — a person who can authenticate.
Membership — a user's association with an organization and its role.

Consequence: inviting someone creates or updates a Membership; it does not
create another Organization. Avoid "account" where it hides this distinction.
```

Check the actual identity and billing behavior before adopting these definitions.
A precise name follows the distinction; renaming a folder cannot repair a model
that still merges the concepts.

## Establish the current language

Read the affected requirements, existing glossary/context explanation, important
decisions and representative behavior. Identify who uses each term and where its
meaning changes. A public product name, a repository name and an internal domain
concept need not be the same name.

If a term has different meanings in different contexts, name those contexts and
the mapping between them. Do not force a single global meaning where the system
contains different concepts. Distinguish established facts, intended changes and
assumptions; an existing implementation can itself contradict the requirement.

## Resolve terms through scenarios

For an overloaded or vague term, ask what it is, what identity it keeps, when it
begins and ends, what can change independently and which rules it owns. Test the
candidate definition with a normal case and a counterexample. For example:

- A reservation can expire without a physical checkout ever occurring.
- Cancelling an order is distinct from a refund being confirmed.
- A customer organization can survive a particular user's departure.

Use the brief and accessible evidence to settle clear choices. Do not ask the
user for facts available in code, records or documentation. Escalate only a real
business-policy or preference ambiguity; do not silently turn a recommendation
into a fact the user supplied.

Choose honest, specific names in the repository's language and idiom. Reject
generic manager/helper/account labels when they hide several jobs, but do not
rename established public contracts simply because another word sounds nicer.
Check consumers, stored forms and migration cost when the change affects identity
or external vocabulary.

## Record the resolved model at its owner

Update the existing glossary or capability explanation as meanings settle. Keep
one owner for each definition; link from consumers. A compact glossary is useful
when the project lacks a suitable owner and the terms merit it, but GLOSSARY.md,
CONTEXT.md and a new documentation tree are not mandatory conventions.

A useful definition states the concept and its distinctions in a few sentences.
Record misleading synonyms where they prevent a recurring mistake. Keep ordinary
language/runtime vocabulary out of a domain glossary. Implementation plans, research
notes and session history belong elsewhere.

Record a lasting design decision when a real trade-off would otherwise be lost,
especially if reversing it is costly or the reason is surprising. Reuse the
repository's decision owner; an ADR can be short and is not required for every name.
Decisions do not disappear when their temporary plan is deleted.

## Hand off the model without duplicating architecture rules

If **Vertical Slices** is available and the clarified model changes ownership or
module structure, pass the concepts, relationships, lifecycle rules and invariants
to it. Receive the structural consequences; do not impose a folder per noun. If
Vertical Slices called this skill, return the resolved model directly to that call.

If **Engineering Practices** is available and a technology or protocol decision
is genuinely unresolved, pass the constraints to it. Naming alone does not require
a fresh stack comparison. If **Grilling with Agents** is already conducting the
discussion, report domain questions to its lead rather than starting a human interview.

If **Puppeteer** is available for a large existing system, use bounded scouts to
compare meanings and behavior across contexts. Return exact evidence and conflicts;
the lead owns the reconciled model. If **All or Nothing** is available and a model
correction is authorized, use it to carry the correction through affected declarations
and consumers. A model review alone does not authorize migration.

Use available methods only for their distinct needed contribution. Without one,
continue the bounded domain analysis and state any resulting limit. Avoid recursive
skill calls. Deliver settled vocabulary, relations, naming choices, unresolved
business questions and affected owners. Check the normal case and counterexample
again against the resulting model.

Source attribution is recorded in [NOTICE.md](NOTICE.md).
