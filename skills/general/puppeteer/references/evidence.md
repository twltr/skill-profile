# Evidence and limits

The operational rules above are design choices. These sources inform them; none proves that this particular skill is optimal.

- [Towards a Science of Scaling Agent Systems, v3](https://arxiv.org/html/2512.08296v3) compares 260 configurations over six benchmarks. Task structure and coordination affect the result, so more agents are not a universal improvement.
- [Why Do Multi-Agent LLM Systems Fail?, MAST](https://arxiv.org/html/2503.13657v3) categorizes observed design, coordination, and verification failures. The taxonomy motivates explicit contracts and checks; it does not measure this skill's effectiveness.
- [Intelligent AI Delegation](https://arxiv.org/html/2602.11865v1) is a conceptual framework for authority, responsibility, and verifiability, not a benchmark of a production agent workflow.
- [Vertical Slice Architecture](https://www.jimmybogard.com/vertical-slice-architecture/) and [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) inform coherent code ownership. Applying them to agent assignments is an engineering heuristic, not a scientific result that every slice or context needs one agent.
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code subagents](https://code.claude.com/docs/en/sub-agents), and [Kimi Code agents](https://moonshotai.github.io/kimi-code/en/customization/agents) document different runtime controls. A shared skill cannot itself enforce fresh context, model choice, read-only execution, or recursion depth across them.
