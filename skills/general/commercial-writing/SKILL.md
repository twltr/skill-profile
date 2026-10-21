---
name: commercial-writing
description: "Create or revise sales and marketing copy, proposals, business cases, pricing narratives, positioning, executive decisions, fundraising materials, landing pages and campaigns. Routine external correspondence belongs to Customer Writing. Automatic selection disabled; use only by explicit user request or through Good Writing."
---

# Commercial Writing

Use this method only when explicitly requested by the user or selected by Good
Writing. An ordinary matching request goes through that router.

## Role

Turn source material or an existing draft into persuasive commercial communication. Make the value legible, the evidence credible, the decision easy, and the next action concrete.

Use the audience, purpose, supplied facts, conditions, requested length and
assigned task from Good Writing. If invoked directly, infer those from the
request and ask only about a gap that changes the offer or claim. Do not route
back to Good Writing or repeat source preparation. Write in the requested
language and preserve responsibilities assigned to other contributors.

## Load only needed resources

**Always apply `unslop`**, including during direct use. Load it once through the
host's skill catalog and returned path or read interface unless already loaded.
If unavailable, name the missing dependency and leave the language review open;
continue independent preparation without claiming the full method was applied.

- Read [commercial-standard.md](references/commercial-standard.md) for substantial,
  high-stakes, financial or decision-oriented work.
- Read [patterns.md](references/patterns.md) when a concrete transformation example
  would help. Example numbers and promises are fictional, not reusable evidence.
- Use `scripts/copy_audit.py` only when its diagnostic would help locate repetition
  or generic phrasing. It is optional and does not establish factual quality.

## Respect the assigned task

Create new text from the available material, edit while preserving the draft's
facts and purpose, or rebuild around an explicitly changed reader or job.
Do not expand an offer, invent proof or replace an argument during a simple edit.

A request for a brief returns material needs; a contribution covers only its
assigned part; a review returns defects and corrections; integration produces
one coherent final text. These are optional jobs, not a required sequence.

## Core rule

Make the strongest case the evidence supports.

- Frame the strongest defensible opportunity.
- Never invent a result, price, saving, deadline, eligibility condition, customer fact, testimonial, or guarantee.
- Resolve factual gaps through authorized research, calculation or a concrete verification action. If a material gap remains, state its effect on the offer or decision; omit unsupported promises.
- Keep internal evidence work separate from audience-facing copy.
- Do not make the reader perform analysis the agent can do first.

## Direct the commercial argument

### 1. Define the decision

State internally, in one sentence:

- who must act,
- what they should decide or do,
- what they gain,
- why acting now is rational,
- what proof earns the ask.

If the text has no meaningful desired action, identify one before drafting.

### 2. Build a claim ledger

Classify every consequential claim as:

- **Verified:** supported by a current, applicable source or user-approved fact.
- **Derived:** calculated transparently from verified inputs.
- **Unresolved:** not yet fit for publication as fact.

Apply the verification triad in `commercial-standard.md` to claims involving money, law, regulation, eligibility, deadlines, safety, performance, or binding commitments. Research unstable claims using current primary sources when permitted.

### 3. Follow the value trail

Look beyond the user's first wording. Test the relevant value dimensions:

- revenue or demand created
- cost removed or avoided
- time or capacity released
- risk reduced
- control, optionality, or switching power gained
- status, confidence, or strategic opportunity created

For money-sensitive material, build the appropriate baseline, change cost, future run rate, time horizon, scenario range, and payback logic. Keep conditional upside separate from the base case.

### 4. Think three moves ahead

Do not stop at “needs review.” For every material unknown, prepare:

1. the authoritative source, person, or dataset that resolves it,
2. the exact request, calculation, document set, or test required,
3. the decision or commercial opportunity unlocked afterward.

Surface adjacent opportunities only when they improve the real decision: a stronger offer, a better commercial route, a smaller paid first step, a partnership, a financing path, a clearer comparison, or reusable proof.

### 5. Choose the commercial architecture

Lead with one of these, whichever is strongest and defensible:

- measurable outcome
- money or time at stake
- costly current problem
- differentiated mechanism
- decision or strategic control

Then arrange the argument:

1. outcome or opportunity,
2. relevance and why now,
3. economic or practical mechanism,
4. offer or bounded first step,
5. proof and objections,
6. low-friction action.

Lead with the reader's decision or defensible opportunity. Keep a material limitation or unknown beside the affected claim, including in the opening when it changes the decision. Keep internal process details out of the copy.

### 6. Preserve the commercial meaning

Use the recipient's language and established tone. Show value through the
supported mechanism and evidence. Do not manufacture praise, urgency or a
commercial commitment. Apply Unslop for language and compression; keep every
condition that changes the offer, eligibility or decision. There is no target
percentage to cut.

### 7. Check the argument

Check value, proof, objections, action and consistency in the completed text.
Resolve duplicated or conflicting claims at their owner. A shorter draft fails
if it hides a material condition or turns an unresolved claim into a fact.

### 8. Make the argument visible

Group related claims around the reader's decision. Use the destination's
supported formatting: meaningful headings, parallel lists, ordered steps,
emphasis and tables for exact comparisons. Let the strongest supported value
receive the strongest visual weight. Keep material conditions beside the claim;
link optional proof and detail without hiding a limitation that changes the offer.

Load `editorial-svg-diagrams` when a mechanism, comparison of relationships or process
becomes clearer as a graphic. Pass the verified model, audience and output needs;
it owns editable source, design, export and visual checks. If unavailable,
disclose the limit and use a readable supported form; an explicitly requested
diagram remains open. Verify the actual render for formatted artifacts.

### 9. Deliver cleanly

Return the finished audience-facing copy or artifact first. Add a short, clearly separated internal evidence/action note only when unresolved facts materially affect publication or execution.

If the user asks for final copy only, return only publishable copy and omit unsupported claims.

## Release gate

Before delivery, require all of the following:

- The audience can identify value and intended action within seconds.
- The commercial case is specific enough to compare or decide.
- Material claims are verified or transparently derived. Unsupported promises are removed, while material conditions and unresolved status remain explicit.
- Important unknowns have executable resolution paths.
- The copy sounds human and domain-aware, not generically “professional.”
- The strongest message receives the strongest visual weight.
- The final ask is concrete, proportionate, and easy to act on.
