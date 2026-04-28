# Layer 3/4 Method Execution Planning Protocol v0.7.1

## Status

Blueprint / protocol draft. `MethodExecutionPlanningRecord v0.7.1` is the current generic planning protocol for Layer 3/4 method engineering. v0.7.1 is a small patch over v0.7, not a conceptual redesign. It supersedes v0.5 and v0.6 planning language, but it does not claim that any production Layer 3 surface, Layer 4 adapter, environment capsule, wrapper, rewrite, runtime dispatcher, or validation runner has been implemented.

Earlier BANKSY v0.6.1 artifacts are now treated as a failed recovery / stress-test example for the protocol. BANKSY v0.7.0 is accepted as a template trial, not as implementation-ready support. Fresh method-specific artifacts must be generated from the current template and stored in NAS, not under project `docs/`.

## Purpose

Given a Layer 2 promoted method, this protocol guides one engineering audit that co-designs a Layer 3 surface and a Layer 4 backend binding while keeping final artifacts separate. The record gathers the Layer 2 handoff, callability constraints, canonical surface reference, evidence registry, code mind map, function surface map, Layer 3 draft, Layer 4 adapter draft, environment plan, rewrite decision, validation/runtime plan, risks, decisions, work plan, and acceptance gate into one auditable planning object.

The record is not a runtime API. Its downstream outputs are separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` drafts.

## Storage Policy

Generic templates, schemas, and design documents may live in the project repository. Method-specific intermediate artifacts, including audit notes, review packs, draft surfaces, adapter drafts, environment reports, and validation plans, must live in the NAS results workspace unless a higher-authority document explicitly promotes them.

Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. If a method-specific artifact is included as a project example, it must be explicitly marked synthetic or illustrative, not a live audit output.

```yaml
storage_policy:
  generic_template_location: project_repo_allowed
  method_specific_intermediate_location: NAS_required
  project_docs_allowed: false_for_method_specific_intermediates
  production_claim_allowed: false_unless_runtime_implementation_exists
```

## Core Principles

- Layer 3 is agent/harness readable by default after Layer 2 method selection.
- Layer 4 is hidden by default and exposed only for implementation, debugging, or audit.
- Layer 3 and Layer 4 are co-designed from one method engineering audit, but final artifacts remain separated.
- Layer 3 must inherit from a canonical task-family surface or justify why no canonical surface exists.
- Layer 2 reasoning should not be copied wholesale into Layer 3. Hard constraints that affect callability must be preserved.
- BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.
- Static dependency risk alone does not justify a method-level environment hold.
- Acceptance status is split across template acceptance, implementation readiness, and production readiness, and is derived from checks rather than manually assigned.
- Every Layer3 functional surface must have an explicit Layer4 binding status.
- File-level evidence can support co-design review, but implementation-critical entrypoints and output mappings require symbol-level or line-level evidence before MVP adapter implementation.

## Current Template

The fillable template is [Method Execution Planning Record Template v0.7.1](templates/method_execution_planning_record_v0.7.1.md). The compatibility path [method_execution_planning_record_template.md](templates/method_execution_planning_record_template.md) points to the same current template.

The canonical current JSON schema path is [contracts/method_execution_planning_record_v0.7.1.schema.json](../contracts/method_execution_planning_record_v0.7.1.schema.json). The older [contracts/method_execution_planning_record_v0.7.schema.json](../contracts/method_execution_planning_record_v0.7.schema.json) path is retained for compatibility.

Separate v0.7.1-compatible downstream schemas are available for Layer 3 and Layer 4 drafts:

- [contracts/execution_surface_spec_v0.7.1.schema.json](../contracts/execution_surface_spec_v0.7.1.schema.json)
- [contracts/backend_adapter_spec_v0.7.1.schema.json](../contracts/backend_adapter_spec_v0.7.1.schema.json)

Top-level record shape:

```yaml
method_execution_planning_record:
  record_id:
  record_version: v0.7.1
  method_id:
  task_family:
  planning_status:
  authority_status:
  storage_policy:
  source_layer2_artifacts:

  layer2_to_layer3_handoff:
  hard_constraints_for_layer3:

  audit_evidence_registry:
  code_mind_map:
  function_surface_map:

  canonical_surface_reference:
  layer3_agent_surface:
  layer4_adapter_draft:

  environment_plan:
  rewrite_decision:
  validation_runtime_plan:
  static_acceptance_gate:
  runtime_acceptance_gate:
  risk_register:
  decision_log:

  subagent_work_plan:
  acceptance_gate:
  next_action_decision:
```

## Layer 2 Handoff

Use the full handoff to retain selection context without copying the whole Layer 2 method-comparison artifact into the Layer 3 agent card:

```yaml
layer2_to_layer3_handoff:
  full_handoff:
    layer2_branch:
    method_role:
    selection_context:
    caveats:
    evidence_summary:
    hardware_resource_tag:
    applicability_notes:

hard_constraints_for_layer3:
  required_modalities:
  forbidden_modalities:
  required_input_object:
  required_spatial_information:
  histology_requirement:
  reference_requirement:
  gpu_requirement:
  multi_sample_policy:
  minimum_dataset_assumptions:
```

## Layer 3 Rules

Layer 3 describes semantic execution behavior. It must not expose raw backend function names, backend file paths, package-private parameters, implementation call graphs, unsafe memory flags, temporary filenames, or raw backend coordinate tuple/key details.

For spatial domain identification, the canonical functional surfaces are:

```yaml
functional_surfaces:
  - input_check
  - method_preprocessing
  - core_structure_building
  - model_fit_or_inference
  - output_assignment
  - artifact_export
  - final_validation
  - visualization
```

Use `method_preprocessing` for method-local preprocessing.

Layer 3 coordinate handling uses semantic source modes only:

```yaml
spatial_coordinate_source:
  allowed_modes:
    - obsm_spatial
    - obs_x_y_columns
    - adapter_validated_custom_mapping
```

Layer 3 must include normalized policies for:

- `multi_sample_policy`
- `target_domain_count_policy`
- `parameter_policy`
- `clustering_backend_policy` where a method exposes or depends on optional clustering runtimes
- `layer4_reference_policy`
- `validation_contract`
- `failure_policy`
- `provenance_policy`

Agent-visible parameters must be semantic and constrained. Low-level backend knobs, raw file paths, temporary filenames, internal object keys, unsafe memory flags, backend optimization parameters, low-level output namespaces, directory layouts, and backend output prefixes should be forbidden for agent control. If user naming control is needed, expose a safe semantic alias such as `output_label_key_alias_optional`; the adapter controls output field prefixes, directory layout, temporary directories, and log-file policy.

## Layer 4 Rules

Layer 4 binds the semantic surface to concrete backend implementation details. It may contain backend functions, scripts, notebooks, file paths, parameter mappings, call graphs, filesystem policy, and failure translation. Every major backend claim must cite the audit evidence registry.

Layer 4 adapter drafts must include at least the fields listed in the v0.7.1 template's Layer4 completeness contract. `implementation_status` remains `not_implemented` unless actual runtime code exists. `authority_status` remains `blueprint` unless formally promoted.

Every Layer3 functional surface must be represented by `function_surface_bindings` with one of `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`. No Layer3 stage may be silently omitted from Layer4. Missing binding coverage can still pass static template review if explicit, but critical unresolved bindings block implementation readiness.

The draft-only sentinel `source_symbol_not_resolved_in_current_inventory` is allowed only when paired with `implementation_blocker: true` and `resolution_required_before: MVP_adapter_implementation`. It is not allowed in implementation-ready adapter specs. If it appears for model fitting, inference, output assignment, or parameter mapping, implementation readiness must be `fail`.

Evidence resolution must be recorded as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`. A Layer4 draft may be accepted for planning with file-level evidence, but implementation cannot start until critical backend entrypoints and output mappings reach symbol-level or line-level evidence. Runtime-observed evidence is required before runtime support can be claimed.

## Environment Rules

Environment planning is independent from rewrite planning. Use `environment_plan` as the top-level holder for installability, dependency, GPU/CUDA, shared-capsule, isolation, optional-path, and probe requirements.

Static dependency risk does not justify final environment hold. `hold_due_to_environment` must not be used as a final decision unless an environment subagent report cites a failed probe or impossible dependency constraint. Preferred pre-probe state:

```yaml
environment_decision:
  - environment_probe_required
  - shared_capsule_unknown
  - dedicated_capsule_may_be_required
  - wrapper_boundary_required
environment_hold_status: not_justified_yet
```

Optional backend paths, such as mclust/rpy2, should be separated from the core path.

Environment risk may trigger a probe, a dedicated capsule, a wrapper boundary, or an optional-path exclusion. It should not automatically trigger method hold.

## Validation And Acceptance

The validation plan must separate callability checks, preflight checks, postrun checks, contract tests, visual sanity checks, reproducibility checks, runtime-cost records, output schema observation, provenance observation, and rewrite comparison. Visual plausibility is not biological correctness, and visual similarity does not prove algorithmic equivalence. Runtime measurement cannot be faked or inferred from static docs.

Static acceptance and runtime acceptance are separate. A Layer3/4 review pack can pass static acceptance with valid YAML, separated Layer3/Layer4 artifacts, evidence authority, required sections, and no production claims. Runtime acceptance remains blocked until environment import probes, minimal fixture smoke runs, runtime measurement, output schema observation, and provenance observation exist.

The acceptance gate derives three statuses:

- `template_acceptance_status` checks structural review validity.
- `implementation_readiness_status` checks whether MVP adapter implementation can start.
- `production_readiness_status` checks whether runtime support can be claimed.

A method can pass template acceptance while failing implementation readiness. Missing environment probe, fixture, runtime measurement, output schema freeze, or symbol-level bindings should block implementation readiness but not necessarily template acceptance. Production readiness must remain `fail` unless actual runtime implementation, validation, and provenance are complete. `ready_for_review` is not a manual label; it requires `template_acceptance_status: pass` or `overall_status: partial_with_known_blockers` with explicit blockers. Invalid YAML, missing required Layer4 sections, broken critical links, unnormalized coordinate/multi-sample/domain-count fields, or production-support claims must block review readiness.

## Pilot Interpretation

BANKSY v0.7.0 is accepted as a Layer3/4 template trial but is not MVP implementation-ready. BANKSY v0.6.1 remains historical stress-test evidence for the protocol only, not a source of current final artifacts and not a production support claim. SpaGCN is the next intended Layer3/4 co-design target after this v0.7.1 patch; it is not complete and should not be started by this documentation patch.
