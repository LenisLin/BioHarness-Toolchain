# Contracts Blueprint

This directory stores public contract schemas for the substrate runtime blueprint.

The schemas define stable planning-layer objects that future harness code may depend on directly, plus lightweight engineering-stage artifacts used before runtime contracts are finalized:

- `SkillSpec`
- `ExecutionSurfaceSpec`
- `EnvironmentProfile`
- `BackendAdapterSpec`
- `RunRecord`
- `ValidationReport`
- `MethodEngineeringAudit`
- `MethodExecutionPlanningRecord v0.7.1`
- `EnvironmentPlan`
- `EnvironmentSubagentReport`
- `AcceptanceGate`

Current schema paths:

- `method_execution_planning_record_v0.7.1.schema.json` is the canonical current schema path for `MethodExecutionPlanningRecord v0.7.1`.
- `method_execution_planning_record_v0.7.schema.json` is retained for compatibility with v0.7-era records.
- `execution_surface_spec_v0.7.1.schema.json` is the v0.7.1-compatible Layer 3 planning schema.
- `backend_adapter_spec_v0.7.1.schema.json` is the v0.7.1-compatible Layer 4 planning schema.

The older `execution_surface_spec.schema.json` and `backend_adapter_spec.schema.json` files are retained for illustrative or legacy examples that still use older required fields. Prefer the v0.7.1-specific schema files for current Layer 3/4 method planning outputs.

`ExecutionSurfaceSpec` is a Layer 3 contract for stable callable surfaces. `BackendAdapterSpec` is a Layer 4 implementation-facing contract for adapter, wrapper, or rewrite bindings.

`MethodEngineeringAudit` is an engineering-stage artifact, not a runtime API. It captures repository/code inspection notes for promoted Layer 2 methods and feeds separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` drafts.

`MethodExecutionPlanningRecord v0.7.1` is the current generic Layer 3/4 method planning record. It is a small patch over v0.7 and remains a co-design and evidence ledger that must preserve separated Layer 3 and Layer 4 outputs. Method-specific intermediate instances belong in NAS results workspaces, not under project docs.

v0.7.1 adds explicit Layer3-to-Layer4 function surface binding coverage, evidence resolution levels, split acceptance statuses for template acceptance / implementation readiness / production readiness, draft-only unresolved backend symbol handling, stricter agent-facing parameter policy, and separate static/runtime acceptance gates.

Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs.

Example instances live under [contracts/examples](examples) so the contract layer can be reviewed before runtime code is written.
