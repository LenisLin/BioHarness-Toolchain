# Round 2 Working Buffer

## Purpose

This file remains a temporary discussion buffer for Round 2 questions that are not yet frozen into authority documents.

## Current Role

The following files now collect candidate blueprint material for later Round 2 runtime design discussion:

- [docs/35_agent_runtime_reference.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/35_agent_runtime_reference.md)
- [docs/30_env_strategy.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/30_env_strategy.md)
- [docs/40_interface_contract.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/40_interface_contract.md)
- [docs/50_rewrite_policy.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/50_rewrite_policy.md)
- [docs/60_validation.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/60_validation.md)

These files do not replace the existing authority order in [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md), and they do not override topic-specific Layer 2 freezes such as `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md`.

This buffer should now focus on unresolved policy questions, evidence gaps, and post-research decisions. It should not claim that Round 2 architecture is already frozen.

## Confirmed Round 2 Direction

- The first vertical remains spatial transcriptomics downstream analysis.
- Round 2 is a bioagent-oriented tool substrate effort, not a continuation of broad Round 1 registry expansion.
- Round 1 remains the evidence layer for what methods exist; it is not the decision layer for which runtime surfaces should become stable BioHarness interfaces.
- The frozen three-layer information mapping plus lower implementation layer is now documented formally rather than kept only in discussion notes.

## Open Questions

- What is the final Round 2 top-level problem statement and non-goal set for publication-quality wording?
- What evidence threshold should separate `Core Anchor`, `Wrapper Candidate`, `Rewrite Candidate`, and `Hold`?
- Which task families should be promoted first from Layer 2 selection schemas into Layer 3 surface manifests?
- How much code accessibility evidence is sufficient before a method moves from research object to implementation candidate?
- What parts of the current biomedical-agent burden should be measured explicitly: environment fragility, context burden, operator burden, or all three?

## Working Hypotheses Still Under Review

- Mature core libraries will usually enter through constrained adapters and fixed best-practice entry points rather than deep rewrites.
- More unstable peripheral tools are likelier rewrite or wrapper targets.
- Execution reliability and validation quality are better primary design pressures than prompt cleverness alone.
- The repository will probably need separate but linked views for knowledge organization, execution surfaces, and underlying implementation modules.

## Evidence Notes

Current local evidence still supports the shift from Round 1 ecosystem mapping toward Round 2 substrate design:

- [README.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/README.md) frames the repository as tools and infrastructure.
- [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md) states that Round 2 is no longer just continued registry expansion.
- `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md` and `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_layer2_field_registry.json` now provide the concrete Layer 2 pilot and registry archive for future Layer 3 mapping.

## Post-Research Questions

The following still require concrete repository review and should stay outside the frozen architecture layer:

- final execution-surface counts
- per-family execution-surface partitioning
- per-tool adapter boundaries
- concrete callable signatures inside wrappers
- per-tool rewrite granularity
- internal module layout for rewritten or wrapped implementations
