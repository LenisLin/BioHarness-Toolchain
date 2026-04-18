# Interface Contract

## Purpose

Record a working blueprint for the public contract layer that may later link agent-facing selection logic to executable tool surfaces.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md).

## Current Working Direction

The current blueprint discusses five candidate public contracts. They are planning-layer objects that may later become stable if Round 2 architecture is formally accepted.

## Public Contracts

### `SkillSpec`

`SkillSpec` defines the candidate agent-facing entry point for a bounded task family.

Required fields:

- `skill_id`
- `analysis_problem`
- `selection_signals`
- `default_surface`

Typical additional fields include prerequisites, approval level, linked Layer 2 references, and operator notes.

### `ExecutionSurfaceSpec`

`ExecutionSurfaceSpec` defines the candidate smallest stable callable unit that a future harness might invoke directly without reasoning about package internals.

Required fields:

- `surface_id`
- `analysis_problem`
- `input_contract`
- `parameter_template`
- `environment_profile`
- `output_artifacts`
- `validation_hooks`

An execution surface must also document failure semantics, emitted logs, and any approval gates that the harness must honor before dispatch.

### `EnvironmentProfile`

`EnvironmentProfile` defines the candidate dependency stack, isolation model, resource class, storage behavior, secret boundary, and provider tag used by one or more execution surfaces.

Required fields:

- `profile_id`
- `isolation_mode`
- `base_stack`
- `resource_class`
- `storage_policy`
- `secrets_policy`
- `provider`

### `RunRecord`

`RunRecord` is the candidate structured state object for long-running or resumable workflows. It exists so a future harness can restore intent and progress from structured state instead of replaying an entire prompt transcript.

Required fields:

- `run_id`
- `skill_id`
- `surface_id`
- `status`
- `state_summary`

`state_summary` should capture checkpoints, pending approvals, artifact handles, and the resume strategy needed after compaction.

### `ValidationReport`

`ValidationReport` records what was checked before and after execution, what failed, and whether manual review is required before the workflow can continue.

Required fields:

- `report_id`
- `run_id`
- `preflight`
- `post_run`
- `final_status`
- `manual_review_required`

Optional fields may include blocking reasons, reviewer action, waived checks, and linked artifact identifiers. When a report indicates manual review, downstream automation must stop rather than silently proceed.

## Contract Boundaries

- `SkillSpec` chooses.
- `ExecutionSurfaceSpec` runs.
- `EnvironmentProfile` isolates.
- `RunRecord` resumes.
- `ValidationReport` gates release and manual review.

## Serialization Rules

- Every candidate public contract should be JSON-serializable and versionable.
- Required fields are not yet frozen.
- Provider-specific details belong in values and examples, not in contract names.

## Repository Blueprint Mapping

- Schemas live under [contracts](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/contracts).
- Example instances live under [contracts/examples](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/contracts/examples).
- Example execution manifests live under [surface_registry](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/surface_registry).
