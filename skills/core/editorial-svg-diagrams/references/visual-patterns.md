# Visual patterns: relationships before boxes

Choose the pattern that allows the fewest labels without losing the causal or structural relation.

Before drawing, compare the plausible forms for the same reader question.
Ownership is often clearer as containment, occupancy as a queue or slots,
timing as a timeline, and differences as an aligned comparison. A connected
topology earns its arrows when the connections themselves are the subject.
Adding icons or rotating the same chain of boxes does not change its grammar.
Use the form that makes the relationship easiest to perceive and route cleanly;
choose a table or text when a picture adds no useful structure.

| Teaching goal | Illustration grammar | Shape carries meaning | Example |
|---|---|---|---|
| One possibility vs many | Repeated slots with 1 highlight / all candidates | Availability of positions, not a description paragraph | `entropy-possibilities.svg` |
| Request exchange / handshake | Actor lifelines; direction-marked arrows from top to bottom | Sender, recipient, ordering | `tcp-handshake.svg` |
| Data wraps data | Segmented, nested horizontal bands | Headers/trailer add around same payload | `packet-encapsulation.svg` |
| Endpoints and ports | Two minimal device illustrations with arrows | Which machine initiates and receives | `pc-connection.svg` |
| Protocol abstractions | Aligned colored rows / rank order | Discrete layers and dependency order | `osi-layers.svg` |
| Component dependencies | A small connected topology | Data path across components, not text boxes | `codebase-architecture.svg` |
| State transition | Two states sharing objects; only changed object highlighted | What changed, not every possible property | Create a compact before/after |
| Flow with a meaningful choice | Paths split at a decision with labeled conditions | Branching consequence | Handcrafted path geometry |
| Ownership / embedding | Nested regions with aligned contents | Which responsibility lives inside which host | A host boundary around an embedded library |
| Waiting / capacity | Occupied slots and an ordered waiting strip | Capacity, order and promotion | One active slot beside a FIFO queue |
| Timing / availability | Aligned time axes or intervals | When something exists or changes | Eager versus on-demand acquisition |
| Shared stages / validation | A rail with checkpoints or gates | What must pass before progress continues | Installation or request validation |
| Comparing independent conditions | A matrix with stable row/column meanings | Which condition affects which outcome | Resume causes versus continuation owners |
| Parts of a whole | One bar or area split in proportion, each part named with its number | Share of the total | `time-budget.svg` |
| Two ways to one result | Parallel aligned routes that merge into a shared node; only the differing step accented | What is the same and where the routes differ | `login-routes.svg` |
| One thing in several notations / a conversion | A chain whose nodes hold the literal value and whose arrows name the operation | The value itself changing form | `base64-roundtrip.svg` |
| A family of variants | A specimen grid: each tile shows the thing itself above its code or name | The variants and their system | `quadrant-glyphs.svg` |
| What a formula's terms do | Formula with one bracket or color per term, behaviour drawn beneath | Which term causes which effect | `backoff-formula.svg` |
| Splitting a set into groups | Adjacent regions holding the actual members | Membership, and what crosses the boundary | Variables `a, b` beside `c, d`, with the clauses that span both |
| One step inside a cycle or route | A short strip of stations with only the subject accented | Where the subject sits among its neighbours | A transition zone between running and a station |

## One subject, three candidate forms

Fictional question: *where does a password login differ from a passkey login?*

- A sequence diagram answers "who sends what when" and buries the difference
  in message seven of twelve.
- A two-column table lists properties but shows no route.
- Parallel routes into one shared node put the single differing step side by
  side and make the common result one shape. That is the takeaway, so that is
  the form (`login-routes.svg`).

The same subject would deserve the sequence if the question were about the
order of the exchange.

## Shared rules

- Default to one figure per explanatory beat. Split an overview from details rather than nest all details in an SVG.
- Establish alignment axes, equal peer dimensions and repeated gaps first. Reserve free routing channels before placing edge labels. A connector must meet its intended boundary cleanly and never hide behind an unrelated shape.
- Do not begin with a heading. Begin with shapes that instantiate the subject.
- For sequences, actor names and message labels stay; IPs, flags, thread state, retries, exact port numbers or timing metrics only appear if the question specifically requires them.
- For encapsulation, show payload continuity by repeating the same color/word, not by telling a story in each block.
- For quantities, use spatial repetition/size/position and minimal numeric labels. Never draw visually misleading counts; distinguish *possible states* from *physical entities*.
- For repository architecture, establish actual modules and call/data arrows from code inspection; if inaccessible, clearly mark the whole example as illustrative in accompanying prose.
- Use colored fills to indicate role (blue request/application, teal transport/response, green network, ochre medium); the exact hues are less important than contrast and consistent mapping.
- Compute proportional geometry from the numbers and keep the numbers visible. Name each part directly at or beside its mark; do not send the reader to a detached color key.
- In a specimen grid keep every tile the same size and vary only the specimen, so the differences the reader sees are the real ones.
- Borders are not inherently bad. A border that marks an endpoint or possibility slot is meaningful. A giant card around the entire figure, with a built-in footnote, is usually not.
