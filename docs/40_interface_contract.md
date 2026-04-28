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

The current v0.7.1 record is a small patch over v0.7. It gathers the Layer 2 handoff, hard constraints, canonical surface reference, Layer 3 surface draft, Layer 4 adapter draft, `environment_plan`, `rewrite_decision`, `validation_runtime_plan`, `static_acceptance_gate`, `runtime_acceptance_gate`, `risk_register`, `decision_log`, and split `acceptance_gate` statuses into one auditable planning object.

The canonical current schema path is [contracts/method_execution_planning_record_v0.7.1.schema.json](../contracts/method_execution_planning_record_v0.7.1.schema.json). The v0.7 schema path is retained for compatibility with older records.

It produces separate downstream artifacts:

- Layer 3 `ExecutionSurfaceSpec`
- Layer 4 `BackendAdapterSpec`

The record itself is a co-design and evidence ledger. It should preserve Layer 3/Layer 4 separation rather than becoming a mixed runtime contract.

## MethodEngineeringAudit

`MethodEngineeringAudit` is a proposed engineering audit note format, not a runtime layer and not a required production API.

In current v0.7.1 language, `MethodEngineeringAudit` can be treated as a historical or lightweight audit concept. `MethodExecutionPlanningRecord` is the fuller engineering planning template for promoted method work.

It captures raw findings from repository and code inspection for promoted Layer 2 candidates. Those findings then feed both:

- `ExecutionSurfaceSpec`
- `BackendAdapterSpec`

Typical audit inputs include README files, installation files, examples, notebooks, package modules, scripts, input/output examples, environment files, and issue signals if inspected.

Audit evidence should record resolution as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`, plus `implementation_ready: true | false`. File-level evidence can support co-design review, but implementation-critical backend entrypoints and output mappings need symbol-level or line-level evidence before MVP adapter implementation.

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

Method-specific intermediate co-design artifacts are not repository docs by default. They must remain in the external NAS results workspace unless explicitly promoted.

Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. If a method-specific artifact is included as an example, it must be explicitly marked synthetic or illustrative, not a live audit output.

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

The legacy schema path [contracts/execution_surface_spec.schema.json](../contracts/execution_surface_spec.schema.json) retains the older illustrative shape with fields such as `analysis_problem`, `parameter_template`, `environment_profile`, `output_artifacts`, and `validation_hooks`.

The current v0.7.1-compatible schema path is [contracts/execution_surface_spec_v0.7.1.schema.json](../contracts/execution_surface_spec_v0.7.1.schema.json). Its suggested required fields are:

- `surface_id`
- `task_family`
- `visibility`
- `input_contract`
- `parameter_policy`
- `validation_contract`
- `failure_policy`
- `authority_status`

Typical v0.7.1 fields include `inherits_from`, `method_id`, `spatial_coordinate_source`, `multi_sample_policy`, `target_domain_count_policy`, `clustering_backend_policy`, `semantic_inputs`, `semantic_parameters`, `semantic_outputs`, `layer4_reference_policy`, `provenance_policy`, `surface_status`, and `authority_note`.

An execution surface must also document failure semantics, emitted logs, and any approval gates that the harness must honor before dispatch.

For adapter-backed surfaces, this contract should bind a task-level adapter to its input contract, output contract, environment profile, primary backend tools, typed failure modes, and produced artifacts.

`ExecutionSurfaceSpec` is a Layer 3 contract. It should be readable after Layer 2 method selection without requiring access to backend package internals.

Layer 3 parameter policy should expose only semantic, constrained controls. Raw backend function names, low-level output namespaces, directory layouts, temporary paths, backend output prefixes, unsafe memory flags, internal object keys, and backend optimization knobs are not agent-facing by default. If naming control is useful, prefer a safe semantic alias such as `output_label_key_alias_optional`, with the adapter retaining control over output field prefixes, directory layout, temporary directories, and log-file policy.

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

The legacy schema path [contracts/backend_adapter_spec.schema.json](../contracts/backend_adapter_spec.schema.json) retains the older illustrative shape with fields such as `adapter_id`, `surface_id`, `environment_profile`, and `entrypoint`.

The current v0.7.1-compatible schema path is [contracts/backend_adapter_spec_v0.7.1.schema.json](../contracts/backend_adapter_spec_v0.7.1.schema.json). Candidate fields include:

- `backend_adapter_id`
- `linked_surface_id`
- `backend_method`
- `authority_status`
- `implementation_status`
- `evidence_authority`
- `evidence_resolution`
- `runtime_language`
- `integration_mode`
- `backend_entrypoints`
- `function_surface_bindings`
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

Blueprint Layer 4 drafts should keep `implementation_status: not_implemented` unless runtime code exists, but the schema keeps the field as a string so non-blueprint records can evolve without changing the schema.

`BackendAdapterSpec` is a Layer 4 contract. It should usually not be exposed to the default LLM brain. It exists for implementation, debugging, audit, and reproducibility.

Every Layer3 functional surface must have a Layer4 binding entry with `binding_status: backend_bound | wrapper_added | not_applicable | requires_followup`. Missing binding coverage can be acceptable for static template review when explicit, but critical `requires_followup` entries block implementation readiness.

Backend adapter evidence should record `evidence_resolution.level` as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`. A Layer4 draft may be accepted for planning with file-level evidence, but implementation cannot start until critical backend entrypoints, parameter mappings, and output mappings reach symbol-level or line-level evidence. Runtime-observed evidence is required before runtime support can be claimed.

Draft adapter specs may use `backend_function_or_entrypoint: source_symbol_not_resolved_in_current_inventory` only when paired with `implementation_blocker: true` and `resolution_required_before: MVP_adapter_implementation`. The sentinel is not allowed in implementation-ready adapter specs.

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

Optional fields may include blocking reasons, reviewer action, waived checks, linked artifact identifiers, runtime measurement, output schema observation, provenance observation, and static/runtime acceptance state. When a report indicates manual review, downstream automation must stop rather than silently proceed. Runtime measurement cannot be faked or inferred from static docs.

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
