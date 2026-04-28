# Interface Contract

## Purpose

Record a working blueprint for the public contract layer that may later link agent-facing selection logic to executable tool surfaces.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md).

## Current Working Direction

The current blueprint discusses six candidate public or implementation-facing contracts plus engineering-stage planning artifacts. They are planning-layer objects that may later become stable if the substrate architecture is formally accepted.

These contracts are intended to connect the planned task adapters in [docs/45_task_adapters.md](45_task_adapters.md) to explicit environments, validation hooks, provenance records, and resumable execution state.

## MethodExecutionPlanningRecord

`MethodExecutionPlanningRecord` is the current engineering-stage planning record for Layer 3/4 method work. It is not a runtime API and is not itself an `ExecutionSurfaceSpec` or a `BackendAdapterSpec`.

The record gathers the Layer 2 handoff, canonical surface reference, Layer 3 surface draft, Layer 4 adapter draft, `environment_plan`, `rewrite_plan`, `validation_runtime_plan`, `risk_register`, and `decision_log` into one auditable planning object.

It produces separate downstream artifacts:

- Layer 3 `ExecutionSurfaceSpec`
- Layer 4 `BackendAdapterSpec`

The record itself is a co-design and evidence ledger. It should preserve Layer 3/Layer 4 separation rather than becoming a mixed runtime contract.

## MethodEngineeringAudit

`MethodEngineeringAudit` is a proposed engineering audit note format, not a runtime layer and not a required production API.

In current v0.6 language, `MethodEngineeringAudit` can be treated as a historical or lightweight audit concept. `MethodExecutionPlanningRecord` is the fuller engineering planning template for promoted method work.

It captures raw findings from repository and code inspection for promoted Layer 2 candidates. Those findings then feed both:

- `ExecutionSurfaceSpec`
- `BackendAdapterSpec`

Typical audit inputs include README files, installation files, examples, notebooks, package modules, scripts, input/output examples, environment files, and issue signals if inspected.

Relationship summary:

```text
Layer 2 MethodKnowledgePack selects candidates.
MethodExecutionPlanningRecord plans promoted candidates.
MethodEngineeringAudit may provide lightweight inspection notes.
ExecutionSurfaceSpec exposes Layer 3 functional surfaces.
BackendAdapterSpec binds Layer 4 implementation details.
RewriteDecision records adapter/wrapper/rewrite scope.
EnvironmentProfile constrains dependency execution.
ValidationReport judges outputs.
RunRecord remembers execution.
```

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

For adapter-backed surfaces, this contract should bind a task-level adapter to its input contract, output contract, environment profile, primary backend tools, typed failure modes, and produced artifacts.

`ExecutionSurfaceSpec` is a Layer 3 contract. It should be readable after Layer 2 method selection without requiring access to backend package internals.

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

### `BackendAdapterSpec`

`BackendAdapterSpec` defines the candidate implementation-facing contract for binding a Layer 3 execution surface to Layer 4 backend adapter, wrapper, or rewrite logic.

Candidate fields:

- `adapter_id`
- `surface_id`
- `backend_method`
- `runtime_language`
- `environment_profile`
- `entrypoint`
- `call_graph`
- `parameter_mapping`
- `input_conversion`
- `output_mapping`
- `artifact_mapping`
- `failure_translation`
- `smoke_test`
- `fidelity_test`
- `rewrite_level`
- `visibility`
- `example_status`
- `authority_note`

`BackendAdapterSpec` is a Layer 4 contract. It should usually not be exposed to the default LLM brain. It exists for implementation, debugging, audit, and reproducibility.

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

- `SkillSpec` routes.
- Layer 2 method knowledge selects.
- `MethodExecutionPlanningRecord` gathers promoted-method planning evidence and feeds separate Layer 3 and Layer 4 artifacts.
- `MethodEngineeringAudit` remains a lightweight or historical inspection artifact.
- `ExecutionSurfaceSpec` plans.
- `EnvironmentProfile` isolates.
- `BackendAdapterSpec` binds.
- `ValidationReport` judges.
- `RunRecord` remembers.

The contract layer is not a runtime by itself. It defines the public shape that future harness code, manifests, and tests can share.

## Serialization Rules

- Every candidate public contract should be JSON-serializable and versionable.
- Required fields are not yet frozen.
- Provider-specific details belong in values and examples, not in contract names.
- Topic-level `ExecutionSurfaceSpec` work should begin only after the topic completes the current Layer 2 artifact set and transition gate in [docs/90_roadmap.md](90_roadmap.md).
- MCP-style tool schemas may expose capabilities to an agent, but a schema is not an execution guarantee. The harness contract should bind capability exposure to data contracts, environment resolution, adapter logic, validation, and provenance.

## Repository Blueprint Mapping

- Schemas live under [contracts](../contracts).
- Example instances live under [contracts/examples](../contracts/examples).
- Example execution manifests live under [surface_registry](../surface_registry).
