# Visual Grammars and How to Select Them

| Reader needs to see | Use | Layout grammar | Typical applications |
|---|---|---|---|
| Ordered abstractions | Layer stack | Uniform numbered bands; top to bottom | OSI layers, access control, application stack |
| Time-ordered exchanges | Sequence | Actors across x; time down y; arrows indicate messages | TCP handshake, API calls, async jobs |
| Composition / encapsulation | Nested strips | Payload + progressively added header/trailer | Ethernet/IP/TCP, message envelopes, binary formats |
| Component topology | Architecture | Few cards grouped by trust/runtime boundaries, routed connectors | Services, codebases, deployment |
| Steps and branches | Process/flow | One direction, clear decision nodes and labeled outcomes | CI/CD, onboarding, escalation |
| Cause / status evolution | Timeline/state | State labels and transition triggers | Incident lifecycle, job retries |

## Layer stack

- Each row has an index, semantic title, brief example; equal line lengths across rows.
- Progress from top = consumer/abstract to bottom = physical/fundamental when appropriate.
- A color ramp may distinguish functional groups. Do not imply each layer runs on a separate device.
- Use a two-line label only when a third column would be unreadable.
- **Source:** `assets/osi-layers.svg`.

## Sequence exchange

- Actors align to vertical dotted lifelines; events are ordered from top to bottom.
- Arrows originate at sender and end at receiver. Reuse a semantic return color if useful.
- Number the transport messages if order is central. Avoid arrows that accidentally imply the API function call itself travels over the network.
- Keep at most 6-8 distinct messages in one frame. Split normal + error path into separate figures when necessary.
- **Source:** `assets/tcp-handshake.svg`.

## Encapsulation / composition

- Preserve nested logical contents: TCP segment (header + data), IP packet (IP header + TCP segment), Ethernet frame (Ethernet header + IP packet + FCS).
- Show header blocks with distinct widths and colors. Relative widths are **schematic**, not actual byte proportions unless explicitly stated.
- Label what is physically present and what is conceptual. For example, Ethernet FCS is a trailer, not an IP field.
- **Source:** `assets/packet-encapsulation.svg`.

## Software/codebase architecture

- Map names from actual source tree when accessible; place public entrypoints on one side, core logic center, external dependencies on the other.
- Separate data path (solid arrows) from optional/event path (dashed arrows). Label protocols or actions only when known.
- Group module boundaries, runtimes and trust boundaries deliberately; a module is not automatically a separate deployment.
- Choose nesting for ownership, arrows for invocation/data movement, and line style for optionality; do not rely only on color.
- **Source:** `assets/codebase-architecture.svg` (fictional generic topology, not a claim about any real codebase).

## Process / decision

- Use rounded rectangles for actions, diamonds or clearly styled decision cards for branching. Label edges as conditions (true/false) instead of using unexplained color changes.
- Keep decisions ≤3 per frame; more usually needs decomposition.

## Completeness and fidelity

Record factual source and any omissions in nearby prose; figures alone can omit details, but must not contradict reality. Convert Mermaid or draw.io by extracting actors, nodes, edges and labels, then rebuild geometry. Redesign is not a license to remove necessary states, failure branches, or security controls.
