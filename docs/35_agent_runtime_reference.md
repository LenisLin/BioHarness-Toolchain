# Agent Runtime Reference

## Purpose

Record a working blueprint for how the April 15, 2026 agent-runtime guidance may inform Round 2 without reassigning current document authority.

## Status

This document is a working blueprint and not a current authority document.

- It does not override [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md).
- It does not override the Layer 2 freeze archived in `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md`.
- It records candidate mapping ideas and blueprint assets that may support later Round 2 design work if they are explicitly accepted.

## External References

- [OpenAI: The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI: Agents sandboxes guide](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- [OpenAI: Tools and skills guide](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI: Agents orchestration guide](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [Modal: Building with Modal and the OpenAI Agent SDK](https://modal.com/blog/building-with-modal-and-the-openai-agent-sdk)
- [TechCrunch: OpenAI updates its agents SDK to help enterprises build safer, more capable agents](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)

These sources are treated as design references for Round 2 architecture. They do not force BioHarness into an OpenAI-only or Modal-only implementation.

## Candidate Mapping

- Layer 1 = agent-facing skill catalog
- Layer 2 = method knowledge packs / selection schema
- Layer 3 = execution surface registry
- Layer 3 below the information surface = adapters / wrappers / sandbox bindings

This mapping keeps the human-readable selection logic separate from the lower execution machinery while preserving a clear bridge between them.

## Runtime Interpretation

### Harness

The harness is the coordinating layer. It chooses skills, resolves execution surfaces, tracks approvals, stores structured state, and interprets validation outcomes.

### Compute

The compute layer is the isolated execution target. It runs the selected surface with a declared environment profile and returns artifacts, logs, and failure signals.

### Memory and Compaction

Long-running workflows should resume from `RunRecord` state instead of from unbounded conversation replay. Compaction is therefore treated as a state-management concern, not only as a prompt-management concern.

## Repository Blueprint

The current repository blueprint is intentionally static and planning-oriented:

- [skills](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/skills) stores task-level instructions and selection rules
- [contracts](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/contracts) stores public contract schemas and example instances
- [surface_registry](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/surface_registry) stores execution manifests
- [evals](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/evals) stores golden scenarios for regression-style validation

Only after these static artifacts settle should BioHarness decide whether a runtime package belongs under `src/bioharness_toolchain/runtime`.

## Round 2 Design Principles

- OpenAI Agents SDK is the primary external reference, but the BioHarness contract layer stays provider-neutral.
- Modal is a deployment and separation reference, not a required dependency.
- Round 1 scripts and tests remain the evidence layer rather than becoming the runtime itself.
- The first production-quality surfaces should emerge from high-value task families where Layer 2 selection criteria are already concrete.

## Non-Goals

- This document does not define production SDK integration code.
- This document does not freeze per-method adapter internals.
- This document does not commit to a single model provider, sandbox product, or infrastructure vendor.
- This document does not upgrade any current Layer 2 pilot into an accepted Layer 3 default.
