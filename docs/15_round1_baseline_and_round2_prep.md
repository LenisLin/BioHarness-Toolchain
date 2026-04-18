# Round 1 Baseline And Round 2 Preparation

## Purpose

This document is the sole authority inside `docs/` for the current Round 1 baseline and the minimum agreed Round 2 transition note.

It replaces the earlier split between:

- `docs/05_working_topics.md` as an early discussion board
- `docs/15_round1_retrieval_protocol.md` as an active retrieval-phase rule document

It is intentionally a state document, not a run log and not a detailed Round 2 architecture spec.

## Authority And Current Source Of Truth

### Current formal state

Use the following evidence order when sources conflict:

1. Current NAS reports and current script/test encoded behavior.
2. Current master-registry contents.
3. Repository-level framing documents such as `README.md` and `docs/00_overview.md`.
4. Older discussion text only as historical context.

For the current baseline, the strongest evidence comes from:

- `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-10_spatial_method_survey_v1.csv`
- `/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/2026-04-11_round1_expanded_summary_v2.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/2026-04-13_round2_targeted_completion_audit.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/2026-04-13_round2_consolidation_report.md`
- `scripts/build_round1_expanded_outputs.py`
- `scripts/build_round2_targeted_consolidation.py`
- `tests/test_round1_registry_generator.py`
- `tests/test_round2_targeted_consolidation.py`

### Historical background

The old working-notes and retrieval-protocol documents were useful during earlier discussion and execution phases, but they are no longer the current local authority after this migration.

### Still open

Round 2 detailed architecture, core-library selection, rewrite scope, unified-interface details, and environment-strategy details are not frozen here and must remain open.

## Round 1 Baseline Status

### Current formal state

- Round 1 formal scope is 15 analysis problems, not the early 8-topic working version.
- The current master registry is a first-layer overview registry, not a stable-core-only registry.
- The registry row unit remains `Analysis Problem + Subtask + Method Name`.
- Round 1 inclusion records that a method belongs in the current Round 1 baseline registry. It does not by itself mean stable-core status, framework-ready status, or round2 core candidacy.

Current evidence is internally consistent on the 15-analysis-problem baseline:

- the current master CSV contains 137 rows across 15 analysis problems
- the 2026-04-11 NAS expanded summary reports all 15 topics as covered
- the current scripts and tests encode the 15-topic taxonomy, including `Spatial Trajectory Analysis` and `Spatial Clonal Analysis`

### Historical background

Earlier working notes framed Round 1 as an 8-topic first pass and deferred several now-included problems. That framing is obsolete as a description of the current baseline.

### Still open

Round 1 baseline status does not settle how Round 2 will prioritize methods, libraries, or execution surfaces.

## What Has Changed Since Early Working Notes

### Current formal state

- The early statement that Round 1 covered only 8 topics is no longer current.
- The early statement that the authoritative NAS CSV should be treated as a stable-core-only list is no longer current.
- The retrieval-protocol document contributed valid baseline rules for the expanded retrieval phase, but its identity as an active execution protocol is no longer the right framing for the present state.

### Historical background

`docs/05_working_topics.md` captured early hypotheses, provisional scope cuts, and pilot-era assumptions that were later revised.

`docs/15_round1_retrieval_protocol.md` correctly captured the expanded Round 1 execution rules for that phase, including the move from the earlier narrow batch logic to the 15-topic expanded baseline.

### Still open

The transition from Round 1 baseline curation to Round 2 implementation planning is not the place to backfill new method-expansion rules into this document.

## Current Interpretation Of The Master Registry

### Current formal state

The primary registry file remains:

- `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-10_spatial_method_survey_v1.csv`

The most defensible reading of the current file is:

- it is the operative first-layer master registry for the current baseline
- its filename has not changed, but its present contents are newer than the date in the filename
- based on the current file contents together with the 2026-04-13 NAS audit and consolidation reports, it can be confirmed or strongly inferred that the file already absorbed the documented 2026-04-13 targeted completion and consolidation writeback

The evidence for that interpretation is concrete:

- the current file has 137 rows across 15 analysis problems
- the current file contains `STT`, `spVelo`, `CalicoST`, `FICTURE`, and `CONCERT`
- the current file places `segger` under `Segmentation / Cell segmentation / transcript assignment`, matching the documented move in the 2026-04-13 reports

Therefore, the current file should be interpreted by content and supporting reports, not by filename alone.

### Historical background

An earlier interpretation treated the master CSV as a narrower stable-core-only registry. That interpretation is deprecated.

### Still open

This migration does not rename the CSV, does not change CSV schema, and does not redefine future registry versioning policy.

## Round 2 Transition Note

### Current formal state

Round 2 is no longer framed as simply continuing Round 1 table expansion.

The current high-level direction is to use Round 1 results as input for a bioagent-oriented tool substrate:

- choose part of the ecosystem as core lower-layer libraries
- selectively rewrite, wrap, unify interfaces for, or accelerate part of the surrounding tool surface
- reduce agent burden from heterogeneous environment setup, fragmented execution knowledge, and long-context tool handling

Round 1 inclusion does not imply round2 core candidacy. Round 2 selection will use a different decision layer from Round 1 method inclusion.

### Historical background

Earlier discussion often tied later work closely to additional method surveying and registry growth. That is no longer the correct top-level description of the current Round 2 direction.

### Still open

The following remain intentionally undecided here:

- the concrete Round 2 core-library list
- the rewrite shortlist
- unified-interface details
- acceleration strategy details
- environment strategy details
- the exact mapping from Round 1 registry entries to Round 2 implementation units

## Out-Of-Scope / Still Open

This document does not do any of the following:

- freeze the Round 2 architecture
- freeze the core-library list
- freeze the rewrite list
- freeze interface-contract details
- freeze environment-policy details
- expand `docs/20_tool_taxonomy.md`, `docs/30_env_strategy.md`, `docs/40_interface_contract.md`, `docs/50_rewrite_policy.md`, or `docs/60_validation.md`
- rename or edit the NAS CSV

## Historical Migration Note

This document absorbs the parts of the older documents that still remain valid for the current state summary and retires the outdated framing.

Migration result:

- `docs/05_working_topics.md` is removed because it contained early working assumptions that now conflict with the current baseline if treated as active authority.
- `docs/15_round1_retrieval_protocol.md` is removed because its remaining valid conclusions are carried forward here, while its retrieval-execution framing is no longer current.
- NAS run reports remain the detailed historical evidence for how the baseline evolved.

After this migration, current readers should use this file for the local Round 1 baseline and Round 2 preparation summary, and use NAS reports plus current scripts/tests when they need the underlying evidence.
