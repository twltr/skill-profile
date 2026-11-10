---
name: ux-copy
description: Write or review UX copy in any language — microcopy, button labels and CTAs, error messages, empty states, confirmation dialogs, tooltips, loading, success and onboarding text. Use when naming an action, wording an error or a destructive confirmation, filling an empty state or reviewing existing interface strings, including copy for German, French or other non-English interfaces and requests written in those languages. Long-form marketing copy, articles and emails are outside this method.
argument-hint: "<context or copy to review>"
metadata:
  skill-type: leaf
  skill-tree: design
---

# UX Copy

**Leaf skill** in Design; reached through its domain or by name.

Interface text is read in passing, mid-task and often under stress. It works
when the person knows what will happen and what to do next; generic words such as
"Submit", "OK" or "Something went wrong" make them guess. Write from the user's
situation and the action's actual outcome, in the interface's own language.

## A worked example

**Request (fictional product):** "People keep deleting projects by accident.
Review this dialog: *Are you sure?* [OK] [Cancel]"

```text
Delete "Q3 launch"?
Its 14 tasks and all files are removed for everyone on the team.
This can't be undone.
                                   [Cancel]  [Delete project]
```

The title names the action and the object, the body states the consequence that
makes it serious, and the destructive button repeats the verb so it reads on its
own. "Cancel" stays: it is the familiar way out, and renaming it adds nothing.

## Work from the situation

Establish the screen or flow, what the person is trying to do and how they
likely feel, the product's voice and existing terms, and constraints such as
character limits, platform conventions and target languages. Copy passed as
arguments is the text to review. When details are missing, write with stated
assumptions instead of sending a questionnaire; ask only where the answer
changes the copy, such as formal or informal address.

> Sections marked `~~` name a tool category, not a product: `~~design tool`
> (for example Figma) or `~~knowledge base` (for example Notion). Use whichever
> connected tool of that category the host provides; skip the step when none is.

With a `~~knowledge base`, read the brand voice, content style guide and
terminology first. With a `~~design tool`, look at the screen in its flow and
take character limits from the layout.

## Copy in other languages

Write natively in the interface's language; copy drafted in English and
translated keeps English structure and reads foreign. Reply in the language of
the request, but write the strings in the language of the interface — the two
can differ, as with an English question about a German app. The patterns below
hold in every language; these conventions change how they are expressed:

- **Form of address.** Many languages choose between a formal and an informal
  "you" (German, French, Spanish, Dutch). Follow the product's existing choice;
  without one, propose one and apply it everywhere, errors included.
- **Verb form on controls.** German, French and Spanish interfaces conventionally
  label buttons and menu items with the infinitive, not the imperative. Follow
  the platform's and the product's convention.
- **Capitalization.** Sentence case is an English rule. German capitalizes nouns
  anywhere in a sentence; never apply English title case to another language.
- **Typography and formats.** Use the language's quotation marks, spacing (French
  puts a space before `! ? : ;`), and number, date and currency formats.
- **Length.** German and French usually run a third longer than English, and
  short strings far more; long compounds do not wrap. Check against the real
  width and enable hyphenation with the correct `lang` attribute.

In a review, check these for consistency across all strings, not only within one.

## Patterns

| Element | What it must do | Example |
|---|---|---|
| Button, CTA | Verb plus object; name the outcome; keep the name through the flow | "Publish" → toast "Published" |
| Error | What happened and how to fix it; the cause only where it helps the fix; never blame, never a bare code | "Your bank declined this card. Try another card or contact your bank." |
| Field error | Say what is needed, not what is wrong | "Enter a date after today" |
| Empty state | What will appear here and how to start; no-results suggests changing the search | "No invoices yet. Create one or import from a CSV file." |
| Confirmation | Name the action and object, state the consequence, label the button with the verb | See the worked example |
| Tooltip | Add what the label cannot say; never repeat the label | — |
| Loading | Say what is happening; set expectations for long waits | "Importing 2,400 contacts. This can take a minute." |
| Success | Confirm the specific result | "Invoice sent to Dana" rather than "Success!" |
| Onboarding | One concept per step, tied to something the person does | — |

The voice stays the product's; the tone moves with the moment. Errors are calm
and specific: empathy means acknowledging the impact and helping fix it, not
apologizing by reflex or joking. Success is brief, warnings are direct.

## Output

For one element, give the recommendation and a sentence on why it fits the
person's situation. Offer alternatives only where the choice is genuinely open,
such as a tone or length trade-off:

```markdown
## UX copy: [context]

**[Element]:** [copy]
[Why this works for the person at this moment]

| Option | Copy | Best for |
|---|---|---|
| A | [copy] | [when to use] |

**Localization notes:** [only when the copy is translated or ships in several
languages: idioms to avoid, expansion, address form, cultural context]
```

For a review of several strings, use one table so each change is traceable:

```markdown
| Location | Current | Proposed | Why |
|---|---|---|---|
| Checkout, card error | "Error 402" | "Your bank declined this card. Try another card." | Says what happened and the next step |
```

Layout, typography and visual hierarchy are outside this method; so are long
marketing texts, articles and emails, which need a writing method rather than
microcopy patterns.
