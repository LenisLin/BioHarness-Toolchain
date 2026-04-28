# Spatial Domain Layer 3 Entry Example

## Purpose

Show how the spatial domain identification Layer 2 pilot could move into Layer 3 planning.

## Status

This document is illustrative only. It does not mutate or supersede the external NAS Layer 2 pilot, does not freeze a default method, and does not claim implementation.

## External Layer 2 Inputs

The current spatial domain identification Layer 2 pilot lives outside this repository in NAS artifacts, including:

- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_domain_identification_layer2_pilot.md`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-16_layer2_field_registry.json`
- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/spatial_domain_identification/2026-04-18_domain_identification_layer2_supplement_review.md`

These are external authority artifacts, not portable repo content.

## Illustrative Entry Review

```yaml
task_family: spatial_domain_identification
candidate_method: SpaGCN
candidate_status: illustrative_only
input_contract_candidate: SpatialAnnDataContract
output_contract_candidate: DomainLabelsContract
environment_candidate: deep-spatial
adapter_candidate_status: strong_wrapper
layer2_role:
  - histology-aware graph baseline
  - single-slice domain candidate
blocking_issues:
  - confirm current maintained API or callable path
  - define histology optional/fallback behavior
  - define deterministic smoke dataset
  - define domain-label output key
promotion_decision: enter_layer3_planning
implementation_status: not_implemented
default_status: not_default
```

## Interpretation

Layer 2 provides the method-selection rationale. Layer 3 planning would define a stable `ExecutionSurfaceSpec` only after execution readiness review. Layer 4 implementation would remain a separate backend adapter, wrapper, or rewrite decision.

If this illustrative candidate were promoted, the next step would be a Layer 3/4 `MethodExecutionPlanningRecord`. That planning record would derive the Layer 3 surface draft and Layer 4 backend binding draft together while keeping the final artifacts and default visibility boundary separate.
