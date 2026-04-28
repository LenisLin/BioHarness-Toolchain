# Substrate Working Buffer

## Purpose

This file remains a temporary discussion buffer for substrate-design questions that are not yet frozen into authority documents.

## Current Role

The following files now collect candidate blueprint material for later runtime design discussion:

- [docs/35_agent_runtime_reference.md](35_agent_runtime_reference.md)
- [docs/25_harness_architecture.md](25_harness_architecture.md)
- [docs/30_env_strategy.md](30_env_strategy.md)
- [docs/40_interface_contract.md](40_interface_contract.md)
- [docs/45_task_adapters.md](45_task_adapters.md)
- [docs/50_rewrite_policy.md](50_rewrite_policy.md)
- [docs/60_validation.md](60_validation.md)
- [docs/70_reliability_evaluation.md](70_reliability_evaluation.md)
- [docs/80_layer3_layer4_design.md](80_layer3_layer4_design.md)
- [docs/82_layer3_4_codesign.md](82_layer3_4_codesign.md)
- [docs/85_spatial_domain_layer3_entry_example.md](85_spatial_domain_layer3_entry_example.md)

These files do not replace the existing authority order in [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md), and they do not override topic-specific Layer 2 freezes stored as external NAS artifacts, such as `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_domain_identification_layer2_pilot.md`.

This buffer should now focus on unresolved policy questions, evidence gaps, and post-research decisions. It should not claim that the substrate architecture is already frozen.

Reusable `Layer 2` rules now belong in [docs/20_tool_taxonomy.md](20_tool_taxonomy.md), and the current `Layer 2 -> Layer 3` gate belongs in [docs/90_roadmap.md](90_roadmap.md).

## Confirmed Substrate Direction

- The first vertical remains spatial transcriptomics downstream analysis.
- The current phase is a bioagent-oriented tool substrate effort, not a continuation of broad Layer 1 registry expansion.
- The top-level project framing is now a dependency-aware, contract-based, auditable bioinformatics execution harness for reliable spatial transcriptomics downstream analysis by LLM agents.
- The intended execution scope is a curated set of roughly 10-20 high-frequency task adapters, not an open-ended generic biomedical agent.
- The current architecture uses four layers: Layer 1 toolbox catalog, Layer 2 method knowledge pack and decision tree, Layer 3 execution surface registry and callable contract, and Layer 4 backend adapter, wrapper, or rewrite implementation.
- The Layer 1 method registry remains the evidence layer for what methods exist; it is not the decision layer for which runtime surfaces should become stable BioHarness interfaces.
- The four-layer mapping is now documented formally rather than kept only in discussion notes.
- Topic-level `Layer 2` work now has a reusable repo-level contract, while topic-specific pilot details remain in NAS topic artifacts.

## Open Questions

- What evidence threshold should separate `Core Anchor`, `Wrapper Candidate`, `Rewrite Candidate`, and `Hold`?
- Which task families should be promoted first from Layer 2 selection schemas into Layer 3 surface manifests?
- How much code accessibility evidence is sufficient before a method moves from research object to implementation candidate?
- What parts of the current biomedical-agent burden should be measured explicitly: environment fragility, context burden, operator burden, or all three?

## Working Hypotheses Still Under Review

- Mature core libraries will usually enter through constrained adapters and fixed best-practice entry points rather than deep rewrites.
- More unstable peripheral tools are likelier rewrite or wrapper targets.
- Execution reliability and validation quality are better primary design pressures than prompt cleverness alone.
- The repository will probably need separate but linked views for knowledge organization, execution surfaces, and underlying implementation modules.
- Environment capsules should reduce, not eliminate, dependency and execution failures.

## Evidence Notes

Current local evidence still supports the shift from Layer 1 ecosystem mapping toward substrate design:

- [README.md](../README.md) frames the repository as tools and infrastructure.
- [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md) states that the current substrate phase is no longer just continued registry expansion.
- External NAS artifacts such as `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_domain_identification_layer2_pilot.md`, `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_layer2_field_registry.json`, and `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-18_domain_identification_layer2_supplement_review.md` provide the concrete Layer 2 pilot, field registry, and topic-level decision-tree supplement for future Layer 3 mapping.

## Post-Research Questions

The following still require concrete repository review and should stay outside the frozen architecture layer:

- final execution-surface counts
- per-family execution-surface partitioning
- per-tool adapter boundaries
- concrete callable signatures inside wrappers
- per-tool rewrite granularity
- internal module layout for rewritten or wrapped implementations
- final adapter implementation order after the first Layer 3-ready topics
