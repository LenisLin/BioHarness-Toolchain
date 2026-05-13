# Layer 1 Method Registry And Substrate Transition

## Purpose

This document is the current authority inside `docs/` for the Layer 1 method-registry baseline and the agreed transition from broad ecosystem evidence toward BioHarness substrate design.

For agent-facing Layer 1/2 routing and method-selection entry, use the repo `knowledge_registry/`.

It is intentionally a state document. It is not a run log and not a detailed Layer 3/4 architecture spec.

## Authority And Current Source Of Truth

### Current state

Use the following evidence order when sources conflict:

1. `knowledge_registry/` for current agent-facing Layer 1/2 routing and method-selection presentation.
2. Current NAS source/evidence artifacts and current script/test encoded behavior.
3. Current Layer 1 method-registry contents.
4. Repository-level framing documents such as `README.md` and `docs/overview.md`.
5. Older discussion text only as historical context.

For the current Layer 1 registry baseline, the strongest evidence comes from:

- `knowledge_registry/layer1/task_catalog.md`
- `knowledge_registry/layer2/method_selection_standard.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/registry/layer1_spatial_method_registry.csv`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/registry/2026-05-06_layer1_layer2_reconciliation_note.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/2026-05-06_layer1_layer2_reconciliation_report.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/2026-05-06_layer2_topic_confirmation_status.csv`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/reports/2026-04-26_layer1_method_registry_current_summary.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/registry/2026-05-01_six_topic_layer1_supplement_manual_validation.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/registry/2026-05-01_high_priority_journal_sweep_and_backbone_correction.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/2026-05-02_layer2_manual_science_confirmation_report.md`
- `scripts/build_round1_expanded_outputs.py`
- `scripts/build_round2_targeted_consolidation.py`
- `tests/test_round1_registry_generator.py`
- `tests/test_round2_targeted_consolidation.py`

### Historical background

Older working notes and retrieval-protocol documents were useful during earlier discussion and execution phases, but they are no longer current local authority after this migration.

### Still open

Layer 3/4 execution-surface design, backend-binding evidence thresholds, method-specific adaptation levels, environment-profile assignments, and evaluation details are not frozen in this Layer 1 state document.

## Layer 1 Registry Baseline Status

### Current state

- The repo-authoritative agent-facing Layer 1/2 knowledge registry covers 20 active `Analysis Problem` routes under `knowledge_registry/`.
- The current broad Layer 1 method source registry still covers 15 analysis problems.
- The current master registry is a first-layer overview registry, not a stable-core-only registry.
- The registry row unit remains `Analysis Problem + Subtask + Method Name`.
- Layer 1 registry inclusion records that a method belongs in the current broad evidence registry. It does not by itself mean core/basic package status, framework-ready status, Layer 3 surface candidacy, or adaptation priority.

Current evidence is internally consistent when separating the 20-topic agent-facing knowledge registry from the older 15-analysis-problem broad source registry:

- the current master CSV contains 140 data rows across 15 analysis problems
- `knowledge_registry/layer1/task_catalog.md` records 20 active agent-facing `Analysis Problem` routes from the 2026-05-06 reconciliation
- the current NAS Layer 1 registry file is the row-count authority; supporting NAS notes record retained summaries, later Layer 1 supplement decisions, and later manual science confirmations
- the current scripts and tests encode the 15-topic taxonomy, including `Spatial Trajectory Analysis` and `Spatial Clonal Analysis`

### Historical background

Earlier working notes framed the ecosystem map as a smaller first pass and deferred several now-included problems. That framing is obsolete as a description of the current baseline.

### Still open

Layer 1 registry status does not settle how later substrate work will prioritize methods, libraries, or execution surfaces.

## Current Interpretation Of The Master Registry

### Current state

The primary registry file is:

- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/registry/layer1_spatial_method_registry.csv`

The most defensible reading of the current file is:

- it is the operative first-layer master registry for the current baseline
- it is a broad method evidence registry, not a default agent-facing toolbox catalog
- it does not override the current 20-topic agent-facing `knowledge_registry/`
- it should be interpreted by current content and the current Layer 1 summary, not by older staged report filenames

The evidence for that interpretation is concrete:

- the current file has 140 data rows across 15 analysis problems
- the current file contains `STT`, `spVelo`, `CalicoST`, `FICTURE`, `CONCERT`, and `Renoir`
- the current file places `segger` under `Segmentation / Cell segmentation / transcript assignment`

### Historical background

An earlier interpretation treated the master CSV as a narrower stable-core-only registry. That interpretation is deprecated.

### Still open

This migration does not change CSV schema and does not define future registry versioning policy.

## Substrate Transition Note

### Current state

The project is no longer framed as continued broad method-table expansion.

The current high-level direction is to use the Layer 1 method registry as input for a bioagent-oriented tool substrate:

- identify core/basic package anchors and surrounding method candidates
- selectively connect, wrap, or rewrite parts of the surrounding tool surface where evidence supports that adaptation level
- reduce agent burden from heterogeneous environment setup, fragmented execution knowledge, and long-context tool handling

Layer 1 registry inclusion does not imply later core candidacy. Layer 2 method selection and Layer 3/4 engineering review use different decision layers from broad Layer 1 method inclusion.

### Historical background

Earlier discussion often tied later work closely to additional method surveying and registry growth. That is no longer the correct top-level description of the current substrate direction.

### Still open

The following remain intentionally undecided here:

- method-specific adaptation levels
- Layer 3 execution-surface grouping
- Layer 4 backend binding scope
- environment-profile assignments
- validation or evaluation requirements for promoted methods
- the exact mapping from Layer 1 registry entries to later implementation units

## Out-Of-Scope / Still Open

This document does not do any of the following:

- revise the current substrate architecture
- assign method-specific adaptation levels
- freeze Layer 3/4 execution-surface counts
- freeze Layer 4 backend adapter boundaries
- freeze environment-profile assignments
- revise `docs/layer1_2/tool_taxonomy.md`, `docs/substrate/environment_strategy.md`, `docs/substrate/adaptation_policy.md`, or `docs/substrate/evaluation.md`
- change the Layer 1 registry CSV schema

## Migration Note

This document carries forward the valid state summary from earlier baseline/preparation documents while removing staged progress terminology from current project framing.

Current readers should use this file for the local Layer 1 method-registry baseline and substrate-transition summary, and use the current NAS result artifacts plus current scripts/tests when they need the underlying evidence.

Current agents should use `knowledge_registry/` for Layer 1/2 problem routing and method-selection handoff.
