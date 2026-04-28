# Layer 1 Method Registry And Substrate Transition

## Purpose

This document is the current authority inside `docs/` for the Layer 1 method-registry baseline and the agreed transition from broad ecosystem evidence toward BioHarness substrate design.

It is intentionally a state document. It is not a run log and not a detailed Layer 3/4 architecture spec.

## Authority And Current Source Of Truth

### Current formal state

Use the following evidence order when sources conflict:

1. Current NAS result artifacts and current script/test encoded behavior.
2. Current Layer 1 method-registry contents.
3. Repository-level framing documents such as `README.md` and `docs/00_overview.md`.
4. Older discussion text only as historical context.

For the current Layer 1 registry baseline, the strongest evidence comes from:

- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1_method_registry/registry/layer1_spatial_method_registry.csv`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1_method_registry/reports/2026-04-26_layer1_method_registry_current_summary.md`
- `scripts/build_round1_expanded_outputs.py`
- `scripts/build_round2_targeted_consolidation.py`
- `tests/test_round1_registry_generator.py`
- `tests/test_round2_targeted_consolidation.py`

### Historical background

Older working notes and retrieval-protocol documents were useful during earlier discussion and execution phases, but they are no longer current local authority after this migration.

### Still open

Layer 3/4 detailed architecture, core-library selection, rewrite scope, unified-interface details, and environment-strategy details are not frozen here and must remain open.

## Layer 1 Registry Baseline Status

### Current formal state

- The current Layer 1 method registry covers 15 analysis problems.
- The current master registry is a first-layer overview registry, not a stable-core-only registry.
- The registry row unit remains `Analysis Problem + Subtask + Method Name`.
- Layer 1 registry inclusion records that a method belongs in the current broad evidence registry. It does not by itself mean stable-core status, framework-ready status, Layer 3 surface candidacy, or rewrite priority.

Current evidence is internally consistent on the 15-analysis-problem baseline:

- the current master CSV contains 137 rows across 15 analysis problems
- the current NAS Layer 1 summary records the current registry state
- the current scripts and tests encode the 15-topic taxonomy, including `Spatial Trajectory Analysis` and `Spatial Clonal Analysis`

### Historical background

Earlier working notes framed the ecosystem map as a smaller first pass and deferred several now-included problems. That framing is obsolete as a description of the current baseline.

### Still open

Layer 1 registry status does not settle how later substrate work will prioritize methods, libraries, or execution surfaces.

## Current Interpretation Of The Master Registry

### Current formal state

The primary registry file is:

- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1_method_registry/registry/layer1_spatial_method_registry.csv`

The most defensible reading of the current file is:

- it is the operative first-layer master registry for the current baseline
- it is a broad method evidence registry, not a default agent-facing toolbox catalog
- it should be interpreted by current content and the current Layer 1 summary, not by older staged report filenames

The evidence for that interpretation is concrete:

- the current file has 137 rows across 15 analysis problems
- the current file contains `STT`, `spVelo`, `CalicoST`, `FICTURE`, and `CONCERT`
- the current file places `segger` under `Segmentation / Cell segmentation / transcript assignment`

### Historical background

An earlier interpretation treated the master CSV as a narrower stable-core-only registry. That interpretation is deprecated.

### Still open

This migration does not change CSV schema and does not define future registry versioning policy.

## Substrate Transition Note

### Current formal state

The project is no longer framed as continued broad method-table expansion.

The current high-level direction is to use the Layer 1 method registry as input for a bioagent-oriented tool substrate:

- choose part of the ecosystem as core lower-layer libraries
- selectively rewrite, wrap, unify interfaces for, or accelerate part of the surrounding tool surface
- reduce agent burden from heterogeneous environment setup, fragmented execution knowledge, and long-context tool handling

Layer 1 registry inclusion does not imply later core candidacy. Layer 2 method selection and Layer 3/4 engineering review use different decision layers from broad Layer 1 method inclusion.

### Historical background

Earlier discussion often tied later work closely to additional method surveying and registry growth. That is no longer the correct top-level description of the current substrate direction.

### Still open

The following remain intentionally undecided here:

- the concrete core-library list
- the rewrite shortlist
- unified-interface details
- acceleration strategy details
- environment strategy details
- the exact mapping from Layer 1 registry entries to later implementation units

## Out-Of-Scope / Still Open

This document does not do any of the following:

- freeze the Layer 3/4 architecture
- freeze the core-library list
- freeze the rewrite list
- freeze interface-contract details
- freeze environment-policy details
- expand `docs/20_tool_taxonomy.md`, `docs/30_env_strategy.md`, `docs/40_interface_contract.md`, `docs/50_rewrite_policy.md`, or `docs/60_validation.md`
- change the Layer 1 registry CSV schema

## Migration Note

This document carries forward the valid state summary from earlier baseline/preparation documents while removing staged progress terminology from current project framing.

Current readers should use this file for the local Layer 1 method-registry baseline and substrate-transition summary, and use the current NAS result artifacts plus current scripts/tests when they need the underlying evidence.
