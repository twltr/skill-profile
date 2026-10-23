# Visual patterns: relationships before boxes

Choose the pattern that allows the fewest labels without losing the causal or structural relation.

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

## Shared rules

- Default to one figure per explanatory beat. Split an overview from details rather than nest all details in an SVG.
- Do not begin with a heading. Begin with shapes that instantiate the subject.
- For sequences, actor names and message labels stay; IPs, flags, thread state, retries, exact port numbers or timing metrics only appear if the question specifically requires them.
- For encapsulation, show payload continuity by repeating the same color/word, not by telling a story in each block.
- For quantities, use spatial repetition/size/position and minimal numeric labels. Never draw visually misleading counts; distinguish *possible states* from *physical entities*.
- For repository architecture, establish actual modules and call/data arrows from code inspection; if inaccessible, clearly mark the whole example as illustrative in accompanying prose.
- Use colored fills to indicate role (blue request/application, teal transport/response, green network, ochre medium); the exact hues are less important than contrast and consistent mapping.
- Borders are not inherently bad. A border that marks an endpoint or possibility slot is meaningful. A giant card around the entire figure, with a built-in footnote, is usually not.
