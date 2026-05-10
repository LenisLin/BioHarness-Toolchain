# Layer 3/4 Co-design: Method Execution Planning Record

## Purpose

Clarify how BioHarness keeps Layer 3 and Layer 4 architecturally distinct while deriving them from the same engineering planning pass when a Layer 2 method is promoted for execution-surface planning.

## Status

This document is a blueprint. Draft method execution planning records may exist for pilot work, but they do not claim that any production Layer 3 surface, Layer 4 adapter, environment capsule, runtime validator, or rewrite implementation has been implemented.

## Core Principle

Layer 3 and Layer 4 are architecturally distinct:

- Layer 3 is the execution surface layer. It describes the stable semantic interface a task family or promoted method exposes to BioHarness and to the agent or harness after Layer 2 method selection.
- Layer 4 is the backend binding layer. It describes concrete backend functions, scripts, wrappers, parameters, call graphs, file I/O, environment binding, rewrite decisions, error translation, and implementation evidence.

Layer 3/4 are not merged in the architecture. They are co-designed in the engineering workflow and separated in the final artifacts.

Layer 3 and Layer 4 remain separate presentation/runtime layers, but are derived together from the same `MethodExecutionPlanningRecord`.

## Current Recommended Work Record

`MethodExecutionPlanningRecord v0.7.1` is the current recommended co-design work record for promoted methods. It is a small patch over v0.7, not a conceptual redesign. It is a planning artifact, not a runtime API. It gathers the Layer 2 handoff, canonical surface reference, hard constraints, evidence registry, code mind map, Layer 3 surface draft, Layer 4 adapter draft, independent environment plan, rewrite decision, validation/runtime plan, static/runtime acceptance gates, risk register, decision log, and split acceptance status in one auditable place.

The full protocol is [Layer 3/4 Method Execution Planning Protocol v0.7.1](83_layer3_4_method_execution_planning_protocol.md). A fillable YAML template is [Method Execution Planning Record Template v0.7.1](templates/method_execution_planning_record_v0.7.1.md). The older compatibility template path now points to v0.7.1.

`MethodEngineeringAudit` remains useful as a historical or lightweight audit concept. It can capture quick repository/code inspection notes, but the v0.7.1 record is the more complete engineering planning template for current Layer 3/4 method work.

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
MethodExecutionPlanningRecord v0.7.1 completed
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

Each promoted method must inherit from a canonical task-family execution surface before it becomes a method-specific Layer 3 surface. The canonical surface defines the shared semantic interface, standard outputs, common failure modes, validation expectations, and provenance expectations for the task family.

The method-specific realization adds only execution-relevant scientific constraints: required or forbidden modalities, coordinate expectations, image or reference requirements, bounded semantic parameters, output artifacts, typed failures, and validation hooks. It must not expose backend file paths, raw functions, package-private parameters, or implementation call graphs. Those details stay in Layer 4.

For spatial domain identification, `spatial_domain_identification.banksy.v1` should inherit from `spatial_domain_identification.canonical.v1` when BANKSY is used as a promoted planning pilot.

## Same Record, Separate Artifacts

One method/code planning pass should produce several artifacts.

### MethodExecutionPlanningRecord

Current recommended engineering-stage planning record. It is not a runtime layer and not agent-facing by default. It is the shared evidence and decision ledger from which separate Layer 3 and Layer 4 drafts are produced.

### MethodEngineeringAudit

Historical or lightweight raw engineering notes extracted from README files, installation files, examples, notebooks, package modules, scripts, input/output examples, environment files, and issue signals if inspected.

This is an engineering-stage artifact, not a runtime layer and not an agent-facing default contract.

Current audit notes should record evidence resolution as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`, with `implementation_ready: true | false` where the evidence supports backend entrypoints, parameter mappings, or output mappings.

### ExecutionSurfaceSpec

Layer 3 artifact. Describes the aligned execution surface for a task family or promoted method: semantic inputs, semantic parameters, semantic outputs, preflight checks, post-run checks, typed failure modes, artifacts, provenance expectations, and environment profile. A method-specific surface must include `inherits_from` pointing to the canonical family surface.

The surface may include functional coverage for validation, method-local preprocessing, graph or structure construction, model fitting, inference, output writing, visualization, artifact generation, and validation, but those coverage points are not backend functions.

### BackendAdapterSpec

Layer 4 artifact. Describes backend entrypoints, function-surface bindings, parameter mappings, input conversion, output mapping, artifact mapping, call graph, filesystem policy, environment binding, error translation, smoke tests, fidelity checks, and rewrite level. `function_surface_bindings` records how a method satisfies the Layer3 execution surface through backend functions, wrappers, or explicit non-applicability. Critical `requires_followup` bindings block implementation readiness.

Layer4 drafts can use `source_symbol_not_resolved_in_current_inventory` only as draft evidence debt. It must be paired with `implementation_blocker: true` and `resolution_required_before: MVP_adapter_implementation`, and it prevents implementation readiness when it affects model fitting, inference, output assignment, or parameter mapping.

Evidence resolution is recorded as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`. File-level evidence can support co-design review, but MVP adapter implementation requires symbol-level or line-level evidence for critical entrypoints, parameter mappings, and output mappings. Runtime support requires runtime-observed evidence.

### RewritePlan / RewriteDecision

Engineering decision about whether the method should be connected through:

- `core_anchor`
- `thin_adapter`
- `strong_wrapper`
- `compatibility_rewrite`
- `algorithmic_rewrite`
- `legacy_capsule`
- `hold`

The v0.7.1 record separates interface standardization from algorithmic rewrite. BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.

### EnvironmentPlan / EnvironmentProfile Assignment

Maps the method to `scverse-core`, `r-seurat-core`, `r-bioc-spatial`, `deep-spatial`, `image-spatial`, `reporting`, or another explicitly defined capsule.

Environment planning is independent from rewrite planning. Environment conflict does not automatically imply algorithmic rewrite. Static dependency risk does not justify final environment hold; environment risk may trigger a future execution check, a dedicated capsule, a wrapper boundary, or an optional-path exclusion.

### Acceptance Gates

Layer3/4 co-design review separates static acceptance from runtime acceptance. Static acceptance can pass when required files exist, YAML is valid, Layer3/Layer4 separation holds, evidence authority is present, required sections exist, and production claims are absent. Runtime acceptance remains blocked until environment import checks, minimal fixture smoke runs, runtime and memory measurement, output schema observation, and provenance observation exist.

The top-level `acceptance_gate` records `template_acceptance_status`, `implementation_readiness_status`, and `production_readiness_status`. A method can pass template acceptance while failing implementation readiness. Production readiness remains `fail` until runtime implementation, validation, and provenance are complete.

## Default Visibility Boundary

- Layer 3 is agent/harness visible after Layer 2 method selection.
- Layer 4 is hidden from the default LLM brain.
- Layer 4 can be exposed to adapter developers, debugging agents, audit workflows, or coding agents.
- The default LLM brain should receive typed success/failure summaries instead of raw backend traces.
- Layer 4 debug views should be limited and intentional.

## Repository Placement

- The current protocol lives in [docs/83_layer3_4_method_execution_planning_protocol.md](83_layer3_4_method_execution_planning_protocol.md).
- The current planning template lives in [docs/templates/method_execution_planning_record_v0.7.1.md](templates/method_execution_planning_record_v0.7.1.md).
- The v0.7.1 static/implementation/production checklist lives in [docs/templates/layer3_4_v0.7.1_acceptance_checklist.md](templates/layer3_4_v0.7.1_acceptance_checklist.md).
- Historical or lightweight audit note templates live under [docs/templates](templates).
- Contract schema blueprints live under [contracts](../contracts).
- Stable or promoted Layer 3 surface manifests belong under [surface_registry](../surface_registry).
- Layer 4 adapter blueprints currently belong in `BackendAdapterSpec` schemas/examples or a future implementation-facing registry when a reviewable implementation-facing draft is needed.
- Method-specific intermediate co-design packs, including audits, review packs, draft surfaces, adapter drafts, and environment notes, must live in the external NAS results workspace unless a higher-authority project document promotes them into repo state. Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs.

The presence of a draft planning record, audit, surface, adapter spec, or rewrite decision is not an implementation claim.

Current pilot reference:

- BANKSY v0.7.0 accepted template-trial target: `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/BANKSY/v0.7.0/`
- BANKSY v0.6.1 recovery package: historical failed/stress-test material only.
- BANKSY source retrieval outputs: `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/banksy/`
- Next intended co-design target after the v0.7.1 patch: SpaGCN.

These pilot artifacts are evidence for co-design validation only. They do not freeze a production Layer 3 surface, Layer 4 adapter, environment capsule, runtime validator, or runtime-cost claim. BANKSY is not MVP implementation-ready, and SpaGCN is not complete.
