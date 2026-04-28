# Spatial Domain Identification Skill Blueprint

## Purpose

Provide a future Layer 1 skill entry for spatial domain identification tasks.

This file is illustrative only and does not freeze a current Layer 3 default.

This is a Layer 1 routing/skill blueprint. It routes to Layer 2 method selection before any Layer 3 execution surface can be accepted. It does not implement Layer 3 or Layer 4.

## Selection Rules

- prefer this skill when the user goal is tissue-domain calling or domain-level clustering
- route through histology-aware defaults when histology is available
- keep Layer 2 comparison cues in sync with `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_domain_identification_layer2_pilot.md`

## Illustrative Candidate Surface

- `example.spatial_domain_identification.spagcn`

This candidate does not freeze SpaGCN or any other default surface. After Layer 2 selection, a Layer 3 Entry Review is required before any execution surface is accepted.

After Layer 2 selection, promoted methods should enter Layer 3/4 co-design through a `MethodExecutionPlanningRecord`. Any listed surface or backend is illustrative unless backed by a formal surface registry file and adapter planning record.

## Validation Notes

- require schema preflight before dispatch
- require domain-label post-run checks before release
