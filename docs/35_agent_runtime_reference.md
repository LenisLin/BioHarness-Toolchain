# Agent Runtime Reference

## Purpose

Record a working blueprint for how the April 15, 2026 agent-runtime guidance may inform substrate design without reassigning current document authority.

## Status

This document is a working blueprint and not a current authority document.

- It does not override [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md).
- It does not override [docs/20_tool_taxonomy.md](20_tool_taxonomy.md) or [docs/90_roadmap.md](90_roadmap.md).
- It does not override the Layer 2 freeze stored as an external NAS artifact at `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_domain_identification_layer2_pilot.md`.
- It records candidate mapping ideas and blueprint assets that may support later substrate design work if they are explicitly accepted.

## External References

- [OpenAI: The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI: Agents sandboxes guide](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- [OpenAI: Tools and skills guide](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI: Agents orchestration guide](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [Modal: Building with Modal and the OpenAI Agent SDK](https://modal.com/blog/building-with-modal-and-the-openai-agent-sdk)
- [TechCrunch: OpenAI updates its agents SDK to help enterprises build safer, more capable agents](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)

These sources are treated as design references for substrate architecture. They do not force BioHarness into an OpenAI-only or Modal-only implementation.

Related biomedical and scientific-agent work motivates the broader move from prompt-only interaction toward tool-aware systems and execution assistance. Examples include [SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration](https://www.nature.com/articles/s43588-025-00849-y), [CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data](https://www.nature.com/articles/s41592-026-03029-6), [Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://pubmed.ncbi.nlm.nih.gov/41912700/), [Agentic AI and the rise of in silico team science in biomedical research](https://www.nature.com/articles/s41587-026-03035-1), and [Making large language models reliable data science programming copilots for biomedical research](https://www.nature.com/articles/s41551-025-01587-2). BioHarness-Toolchain takes a narrower role than these broad systems: it focuses on the execution substrate for spatial transcriptomics downstream analysis.

## Candidate Mapping

- Layer 1 = agent-facing toolbox catalog
- Layer 2 = task-family method knowledge pack and decision tree
- Layer 3 = execution surface registry and callable contract
- Layer 4 = backend adapter, wrapper, or rewrite implementation

This mapping keeps the human-readable selection logic separate from the lower execution machinery while preserving a clear bridge between them.

## Agent Context Policy

- The agent runtime should reveal only the minimum layer needed for the current decision.
- The agent sees Layer 1 first.
- The agent then sees selected Layer 2 material after task-family routing.
- The agent then sees selected Layer 3 execution surfaces after method selection.
- The agent does not normally see Layer 4.
- Layer 4 should not be loaded into default reasoning context.
- A failure should return typed error information and suggested repairs before exposing backend traces.
- Layer 4 may be inspected only by runtime, debugging, audit, adapter-development, or coding-agent workflows.

Although Layer 3 and Layer 4 may be co-designed by engineers during method onboarding, the runtime presentation remains separated. The default brain reasons over Layer 3 surfaces, not raw backend function graphs.

## Runtime Interpretation

### Harness

The harness is the coordinating layer. It chooses skills, resolves execution surfaces, tracks approvals, stores structured state, and interprets validation outcomes.

### Compute

The compute layer is the isolated execution target. It runs the selected surface with a declared environment profile and returns artifacts, logs, and failure signals.

### Memory and Compaction

Long-running workflows should resume from `RunRecord` state instead of from unbounded conversation replay. Compaction is therefore treated as a state-management concern, not only as a prompt-management concern.

## Repository Blueprint

The current repository blueprint is intentionally static and planning-oriented:

- [skills](../skills) stores task-level instructions and selection rules
- [contracts](../contracts) stores public contract schemas and example instances
- [surface_registry](../surface_registry) stores execution manifests
- [evals](../evals) stores golden scenarios for regression-style validation
- [docs/25_harness_architecture.md](25_harness_architecture.md) and [docs/45_task_adapters.md](45_task_adapters.md) describe the planned harness and adapter surface

Only after these static artifacts settle should BioHarness decide whether a runtime package belongs under `src/bioharness_toolchain/runtime`.

## Substrate Design Principles

- OpenAI Agents SDK is the primary external reference, but the BioHarness contract layer stays provider-neutral.
- Modal is a deployment and separation reference, not a required dependency.
- Layer 1 registry scripts and tests remain the evidence layer rather than becoming the runtime itself.
- The first production-quality surfaces should emerge only after a topic has completed the repo-level Layer 2 artifact set and Layer 2 entry gate.

## Non-Goals

- This document does not define production SDK integration code.
- This document does not freeze per-method adapter internals.
- This document does not commit to a single model provider, sandbox product, or infrastructure vendor.
- This document does not upgrade any current Layer 2 pilot into an accepted Layer 3 default.
