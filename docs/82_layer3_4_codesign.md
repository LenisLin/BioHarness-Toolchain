# Layer 3/4 Co-design: Method Execution Planning Record

## Purpose

Clarify how BioHarness keeps Layer 3 and Layer 4 architecturally distinct while deriving them from the same engineering planning pass when a Layer 2 method is promoted for execution-surface planning.

## Status

This document is a blueprint. It does not claim that any production Layer 3 surface, Layer 4 adapter, method execution planning record, environment capsule, or rewrite has been implemented.

## Core Principle

Layer 3 and Layer 4 are architecturally distinct:

- Layer 3 is the functional execution surface. It describes the stable functional capabilities a method exposes to BioHarness and to the agent or harness after Layer 2 method selection.
- Layer 4 is the backend implementation binding. It describes concrete backend functions, scripts, parameters, call graphs, file I/O, environment binding, wrapper or rewrite decisions, error translation, and implementation details.

Layer 3/4 are not merged in the architecture. They are co-designed in the engineering workflow and separated in the final artifacts.

Layer 3 and Layer 4 remain separate presentation/runtime layers, but are derived together from the same `MethodExecutionPlanningRecord`.

## Current Recommended Work Record

`MethodExecutionPlanningRecord v0.6` is the current recommended co-design work record for promoted methods. It is a planning artifact, not a runtime API. It gathers the Layer 2 handoff, canonical surface reference, hard constraints, evidence ledger, code mind map, Layer 3 surface draft, Layer 4 adapter draft, environment plan, rewrite plan, validation/runtime plan, risk register, decision log, and work decomposition in one auditable place.

The full protocol is [Layer 3/4 Method Execution Planning Protocol v0.6](83_layer3_4_method_execution_planning_protocol.md). A fillable YAML template is [MethodExecutionPlanningRecord v0.6 Template](templates/method_execution_planning_record_template.md).

`MethodEngineeringAudit` remains useful as a historical or lightweight audit concept. It can capture quick repository/code inspection notes, but the v0.6 record is the more complete engineering planning template for current Layer 3/4 method work.

## Why Co-design?

Reading a method repository naturally reveals both functional surfaces and implementation details. The README, examples, notebooks, package modules, scripts, output files, and environment metadata usually show both what the method can do and how it must be run.

Layer 3 needs some awareness of the method workflow to avoid abstract surfaces that cannot be implemented. Layer 4 needs the Layer 3 abstraction to avoid simply exposing raw backend APIs to the agent.

Co-design reduces duplicate repository audits. BioHarness should not ask engineers to inspect the same method once for the functional surface and again for the backend binding.

Final artifacts remain separated so the default agent context does not include backend internals.

## Co-design Workflow

```text
Layer 2 method selected
|
Canonical task-family surface identified
  e.g. spatial_domain_identification.canonical.v1
|
Method-specific Layer 3 realization drafted
  e.g. spatial_domain_identification.banksy.v1 inherits_from canonical
|
Layer 4 backend binding drafted from the same evidence ledger
|
MethodExecutionPlanningRecord v0.6 completed
|
Artifact A: Layer 3 ExecutionSurfaceSpec
Artifact B: Layer 4 BackendAdapterSpec
Artifact C: RewritePlan / RewriteDecision
Artifact D: EnvironmentPlan / EnvironmentProfile assignment
Artifact E: ValidationRuntimePlan
|
Agent/harness sees Layer 3 by default
Runtime/developer/audit sees Layer 4 when needed
```

## Canonical Surface To Method-Specific Realization

Each promoted method must inherit from a canonical task-family surface before it becomes a method-specific Layer 3 surface. The canonical surface defines the shared execution stages, standard outputs, common failure modes, and validation expectations for the task family.

The method-specific realization adds only semantic method differences that the agent or harness needs: constraints, bounded parameters, optional requirements, artifacts, typed failures, and validation hooks. It must not expose backend file paths, raw functions, package-private parameters, or implementation call graphs. Those details stay in Layer 4.

For spatial domain identification, `spatial_domain_identification.banksy.v1` should inherit from `spatial_domain_identification.canonical.v1` when BANKSY is used as a promoted planning pilot.

## Same Record, Separate Artifacts

One method/code planning pass should produce several artifacts.

### MethodExecutionPlanningRecord

Current recommended engineering-stage planning record. It is not a runtime layer and not agent-facing by default. It is the shared evidence and decision ledger from which separate Layer 3 and Layer 4 drafts are produced.

### MethodEngineeringAudit

Historical or lightweight raw engineering notes extracted from README files, installation files, examples, notebooks, package modules, scripts, input/output examples, environment files, and issue signals if inspected.

This is an engineering-stage artifact, not a runtime layer and not an agent-facing default contract.

### ExecutionSurfaceSpec

Layer 3 artifact. Describes functional surfaces, semantic inputs, semantic parameters, semantic outputs, preflight checks, post-run checks, typed failure modes, artifacts, provenance expectations, and environment profile. A method-specific surface must include `inherits_from` pointing to the canonical family surface.

Functional surfaces may include validation, method-local preprocessing, graph or structure construction, model fitting, inference, output writing, visualization, artifact generation, and validation.

### BackendAdapterSpec

Layer 4 artifact. Describes backend entrypoints, function bindings, parameter mappings, input conversion, output mapping, artifact mapping, call graph, filesystem policy, environment binding, error translation, smoke tests, fidelity checks, and rewrite level.

### RewritePlan / RewriteDecision

Engineering decision about whether the method should be connected through:

- `core_anchor`
- `thin_adapter`
- `strong_wrapper`
- `compatibility_rewrite`
- `algorithmic_rewrite`
- `legacy_capsule`
- `hold`

The v0.6 record separates interface standardization from algorithmic rewrite. BioHarness standardizes interfaces, contracts, validation, artifacts, and provenance aggressively, but rewrites scientific algorithms conservatively.

### EnvironmentPlan / EnvironmentProfile Assignment

Maps the method to `scverse-core`, `r-seurat-core`, `r-bioc-spatial`, `deep-spatial`, `image-spatial`, `reporting`, or another explicitly defined capsule.

Environment planning is independent from rewrite planning. Environment conflict does not automatically imply algorithmic rewrite.

## Default Visibility Boundary

- Layer 3 is agent/harness visible after Layer 2 method selection.
- Layer 4 is hidden from the default LLM brain.
- Layer 4 can be exposed to adapter developers, debugging agents, audit workflows, or coding agents.
- The default LLM brain should receive typed success/failure summaries instead of raw backend traces.
- Layer 4 debug views should be limited and intentional.

## Repository Placement

- The current protocol lives in [docs/83_layer3_4_method_execution_planning_protocol.md](83_layer3_4_method_execution_planning_protocol.md).
- The current planning template lives in [docs/templates/method_execution_planning_record_template.md](templates/method_execution_planning_record_template.md).
- Historical or lightweight audit note templates live under [docs/templates](templates).
- Contract schema blueprints live under [contracts](../contracts).
- Layer 3 surface manifests belong under [surface_registry](../surface_registry).
- Layer 4 adapter blueprints currently belong in `BackendAdapterSpec` schemas/examples or a future implementation-facing registry.

The presence of a draft planning record, audit, surface, adapter spec, or rewrite decision is not an implementation claim.
