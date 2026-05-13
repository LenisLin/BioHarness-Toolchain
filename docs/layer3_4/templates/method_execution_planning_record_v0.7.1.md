# Method Execution Planning Record Template v0.7.1

`MethodExecutionPlanningRecord v0.7.1` is a small patch over v0.7, not a conceptual redesign. It preserves the same Layer3/Layer4 architecture while tightening review, implementation-readiness, and runtime-readiness rules. It supersedes v0.5 and v0.6 planning language. It is an engineering-stage co-design record, not a runtime API and not a production-support claim.

Canonical schema path: [contracts/method_execution_planning_record_v0.7.1.schema.json](../../../contracts/method_execution_planning_record_v0.7.1.schema.json). The v0.7 schema path is retained only for compatibility.

Method-specific Layer3/4 audit outputs are intermediate engineering artifacts. They must be stored in the NAS results workspace, not under project docs. The project repository may contain only generic templates, schemas, design documentation, and explicitly synthetic or illustrative examples. Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs.

## v0.7.1 Patch Notes

v0.7.1 adds:
1. required Layer4 binding status for every Layer3 functional surface;
2. evidence resolution levels;
3. split acceptance statuses for template review, implementation readiness, and production readiness;
4. unresolved backend symbol handling;
5. tighter agent-facing parameter policy;
6. static vs runtime acceptance gate separation;
7. clearer NAS-only boundary for method-specific intermediate artifacts.

## Storage Policy

```yaml
storage_policy:
  generic_template_location: project_repo_allowed
  method_specific_intermediate_location: NAS_required
  project_docs_allowed: false_for_method_specific_intermediates
  production_claim_allowed: false_unless_runtime_implementation_exists
```

Generic templates, schemas, and design docs may live in the project repository. Method-specific intermediate artifacts, including audits, review packs, surface drafts, adapter drafts, environment notes, validation plans, and risk logs, must live in the external NAS workspace unless a higher-authority document explicitly promotes them.

## Layer3 / Layer4 Separation

Layer3 and Layer4 are co-designed from one method engineering audit, but final artifacts remain separated.

Layer3 is agent/harness readable. It describes functional execution surfaces, semantic inputs, semantic parameters, semantic outputs, validation expectations, provenance expectations, and typed failure behavior. It must not expose raw backend function names, backend file paths, package-private knobs, or low-level backend parameters.

Layer4 is implementation/debug/audit visible only. It binds Layer3 surfaces to concrete backend functions, scripts, packages, notebooks, parameter mappings, call graphs, filesystem policy, environment binding, and failure translation. Layer4 claims must be evidence-backed and may contain backend paths and symbols.

## Active Artifact Selection

```yaml
active_artifact_selection_policy:
  selection_priority:
    - schema_validity
    - required_section_completeness
    - evidence_traceability
    - normalization_compliance
    - source_recency
    - source_origin_priority
  source_origin_priority:
    - manual_input
    - nas_existing
    - active_file
    - git_head
    - git_history
    - previous_export
    - tmp_or_workdir
  rule: source origin priority must not override section completeness or validity
```

A shorter NAS-existing file must not be selected over a richer recovered/exported file if the richer file contains required Layer4 sections and can be normalized. Select the most complete valid artifact, then apply v0.7.1 normalization.

## Canonical Surface Requirement

Every method-specific Layer3 surface must either inherit from a canonical task-family surface or explicitly justify why no canonical surface exists.

```yaml
canonical_surface_reference:
  surface_id:
  status: existing | created_for_this_task | missing_requires_followup
  inherits_from:
  no_canonical_surface_justification:
```

For spatial domain identification, the canonical surface should be method-neutral and include:

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

Use `method_preprocessing` for method-local preprocessing. If an older surface keeps the shorter term, it must explicitly define that term as method-local preprocessing rather than global upstream preprocessing.

## Coordinate Boundary

Layer3-facing `coordinate_key_pair` is prohibited. Layer3 exposes only a semantic coordinate source:

```yaml
spatial_coordinate_source:
  allowed_modes:
    - obsm_spatial
    - obs_x_y_columns
    - adapter_validated_custom_mapping
```

Layer4 may map that semantic source to backend-specific coordinate keys or tuples:

```yaml
spatial_coordinate_source:
  backend_parameter: coordinate_key_representation
  mapping_rule: convert BioHarness coordinate source into backend-compatible coordinate keys
  visibility: layer4_only
```

Raw backend coordinate tuple/key details are Layer4-only.

## Multi-Sample Policy

Avoid ambiguous `multi_slice_requirement` wording. Use:

```yaml
multi_sample_policy:
  status: examples_observed_but_bioharness_contract_not_validated | supported_by_surface_contract | unsupported | unknown
  supported_claim:
  agent_visible_summary:
```

When examples exist but BioHarness has not frozen a joint or multislice contract, use:

```yaml
status: examples_observed_but_bioharness_contract_not_validated
supported_claim: no_joint_multislice_contract_claim
agent_visible_summary: multi-sample usage requires additional review before default surface exposure
```

## Target Domain Count Policy

Domain granularity parameters do not always guarantee exact domain counts.

```yaml
target_domain_count_policy:
  status: directly_supported | not_directly_guaranteed | unsupported | unknown
  mapping:
  agent_action:
```

When exact domain count is not directly guaranteed, use:

```yaml
status: not_directly_guaranteed
mapping: may require resolution search or post-hoc selection
agent_action: ask user whether approximate granularity is acceptable
```

## Parameter Policy

Every Layer3 surface must include:

```yaml
parameter_policy:
  expose_to_agent:
  expose_to_agent_with_constraints:
  infer_from_input:
  fixed_by_adapter:
  backend_default:
  forbidden_for_agent:
```

Agent-visible parameters must be semantic and constrained. Backend low-level parameters must be hidden unless explicitly promoted through `expose_to_agent_with_constraints`. Raw file paths, temporary file names, internal object keys, unsafe memory flags, and backend internal optimization parameters should be `forbidden_for_agent`.

Do not let the agent freely set low-level `output_namespace`, directory layout, temporary paths, or backend output prefixes. If users need naming control, expose only a safe semantic alias such as:

```yaml
output_label_key_alias_optional
```

Adapter-controlled output and filesystem fields should remain fixed:

```yaml
fixed_by_adapter:
  - BioHarness_output_field_prefix
  - output_directory_layout
  - temporary_directory_policy
  - log_file_policy
```

Optional clustering/runtime backends must be explicit:

```yaml
clustering_backend_policy:
  allowed_values:
    - default_validated_path
    - optional_backend_disabled_until_verified
    - method_specific_requires_followup
```

If an optional backend requires R, rpy2, mclust, or a similar optional runtime, it must not be agent-selectable until verified by environment probe.

## Audit Evidence Registry

Every method engineering audit must include:

```yaml
audit_evidence_registry:
  repository_snapshot:
    url:
    commit_or_release:
    local_path_if_present:
    last_checked:
  evidence_items:
    - evidence_id:
      source_type: source_code | readme | package_docs | notebook | example | install_file | layer2_artifact | inferred
      path_or_url:
      symbol_or_section:
      line_range:
      summary:
      confidence: high | medium | low
      evidence_resolution:
        level: file_level | symbol_level | line_level | runtime_observed
        implementation_ready: true | false
```

Evidence resolution levels mean:

- `file_level`: evidence points to a file, README section, notebook, or module-level source.
- `symbol_level`: evidence identifies a function, class, object, CLI command, or exported API symbol.
- `line_level`: evidence includes line ranges or precise source locations.
- `runtime_observed`: evidence is confirmed by an actual install, import, or run probe.

File-level evidence is acceptable for co-design review. Symbol-level or line-level evidence is required before MVP adapter implementation for backend entrypoints, parameter mappings, and output mappings. Runtime-observed evidence is required before claiming runtime support. `inferred` evidence must not be treated as implementation-ready.

Layer4 claims must cite evidence IDs. Layer4 adapter drafts must include:

```yaml
evidence_authority:
  registry_file:
  registry_section: Audit Evidence Registry
```

## Layer4 Completeness Contract

Layer4 adapter drafts must include at least:

```yaml
backend_adapter_id:
linked_surface_id:
backend_method:
authority_status:
implementation_status:
native_repository:
evidence_authority:
runtime_language:
environment_profile_candidate:
integration_mode:
backend_entrypoints:
call_graph:
function_surface_bindings:
parameter_mapping:
input_conversion:
output_mapping:
artifact_mapping:
filesystem_policy:
failure_translation:
environment_binding:
smoke_test:
fidelity_test:
rewrite_level:
rewrite_rationale:
algorithm_core_touched:
visibility:
blocking_issues:
authority_note:
```

Every Layer3 functional surface must be represented in Layer4:

```yaml
function_surface_bindings:
  - layer3_stage:
    binding_status: backend_bound | wrapper_added | not_applicable | requires_followup
    backend_files_or_functions:
    adapter_responsibility:
    evidence_refs:
    implementation_blocker:
```

No Layer3 stage may be silently omitted from Layer4. If a stage is BioHarness-added rather than native to the backend, mark `wrapper_added`. If a stage does not apply to a method, mark `not_applicable` with rationale. If a stage cannot yet be bound to backend code, mark `requires_followup`. Missing binding coverage should not necessarily fail template acceptance, but it must block implementation readiness if critical.

Example:

```yaml
function_surface_bindings:
  - layer3_stage: artifact_export
    binding_status: wrapper_added
    backend_files_or_functions: []
    adapter_responsibility: "BioHarness adapter standardizes plots, summary files, logs, and provenance."
    evidence_refs: []
    implementation_blocker: false

  - layer3_stage: model_fit_or_inference
    binding_status: requires_followup
    backend_files_or_functions:
      - source_symbol_not_resolved_in_current_inventory
    adapter_responsibility: "Resolve exact backend entrypoint before implementation."
    evidence_refs:
      - E_SOURCE_FILE
    implementation_blocker: true
```

Layer4 draft artifacts may temporarily use:

```yaml
backend_function_or_entrypoint: source_symbol_not_resolved_in_current_inventory
implementation_blocker: true
resolution_required_before: MVP_adapter_implementation
```

`source_symbol_not_resolved_in_current_inventory` is allowed in review drafts only. It is not allowed in implementation-ready adapter specs. If present for model fitting, inference, output assignment, or parameter mapping, implementation readiness must be `fail`, and the review pack must list the unresolved backend symbol as a blocker.

Layer4 drafts may be accepted for planning with file-level evidence, but implementation cannot start until critical backend entrypoints and output mappings reach symbol-level or line-level evidence.

`implementation_status` must remain `not_implemented` unless actual runtime code exists. `authority_status` must remain `blueprint` unless formally promoted. If any major section is missing, the review pack cannot be `ready_for_review`; it must be `requires_followup` or `partial`.

## Environment Plan

Environment feasibility is independent from rewrite planning.

```yaml
environment_plan:
  method_id:
  environment_profile_candidate:
  expected_capsule:
  native_package_manager:
  install_files:
  lock_or_container_available:
  dependency_conflict_risk:
  known_dependency_risks:
  gpu_policy:
  cuda_policy:
  cpu_fallback_policy:
  shared_environment_feasibility:
  capsule_uncertainty:
  isolation_strategy:
  optional_paths:
  environment_decision:
  environment_hold_status:
  environment_subagent_report:
  required_probes:
  evidence_refs:
  open_questions:
```

Static dependency risk does not justify final environment hold. `hold_due_to_environment` may appear only as historical context or as a justified decision after a failed probe or impossible dependency constraint.

Preferred pre-probe decision:

```yaml
environment_decision:
  - environment_probe_required
  - shared_capsule_unknown
  - dedicated_capsule_may_be_required
  - wrapper_boundary_required
environment_hold_status: not_justified_yet
```

Optional paths, such as mclust/rpy2, should be separated from the core path.

If no environment probe has run, `environment_hold_status` must be `not_justified_yet` or `unknown`, not `justified`. Environment risk may trigger a probe, a dedicated capsule, a wrapper boundary, or an optional-path exclusion. It should not automatically trigger method hold.

## Environment Subagent Report

```yaml
environment_subagent_report:
  method_id:
  report_status: draft | complete | requires_probe
  authority_status: blueprint
  reviewed_inputs:
  conclusion:
    environment_hold_status: not_justified_yet | justified | unknown
    recommended_decision:
  rationale:
  required_probes:
  do_not_claim:
```

Static dependency risk alone does not justify a hold. If no probe was run, use `not_justified_yet` or `unknown`, not `justified`. Do not run heavy probes unless explicitly authorized.

## Rewrite Decision

Rewrite decisions must separate interface standardization from algorithmic rewriting.

```yaml
rewrite_decision:
  method_id:
  decision_status:
  interface_standardization:
    wrap_io_only:
    normalize_parameters:
    redesign_entrypoint:
    rewrite_glue_code:
    standardize_logging:
    standardize_artifacts:
    standardize_failure_translation:
  algorithmic_rewrite:
    compatibility_reimplement_function:
    algorithm_core_touched:
    do_not_rewrite_algorithm:
    algorithmic_rewrite_risk:
    scientific_equivalence_risk:
  final_rewrite_level:
  rationale:
  fidelity_required:
  approval_required_before_implementation:
  evidence_refs:
  blocking_issues:
```

BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.

Interface standardization is expected. Algorithmic rewrite requires explicit rationale and fidelity checks. Strong wrappers may be implementation-ready only after environment probe, smoke fixture, and output schema observation. Compatibility rewrite requires comparison against original behavior. Algorithmic rewrite should default to hold/manual review unless scientific equivalence can be evaluated.

## Validation Taxonomy

```yaml
validation_runtime_plan:
  callability_check:
    installable:
    runnable_example:
    observable_io:
  preflight_checks:
  postrun_checks:
  contract_tests:
  visual_checks:
    purpose: sanity_only
    known_limitations:
      - visual plausibility is not biological correctness
      - visual similarity does not prove algorithmic equivalence
  reproducibility_checks:
    random_seed_control:
    deterministic_mode_available:
    repeated_run_policy:
    expected_variability:
    label_permutation_awareness:
    stochastic_components:
  runtime_cost_record:
    wall_time:
    peak_memory:
    device_used:
    fixture_size:
    measurement_source:
    must_be_runtime_observed: true
  output_schema_observation:
    observed_fields:
    observed_artifacts:
    observation_source:
  provenance_observation:
    random_seed_capture:
    package_version_capture:
    input_output_identifier_capture:
  rewrite_comparison:
    output_schema_equivalence:
    domain_count_equivalence:
    no_empty_domain_equivalence:
    label_permutation_handling:
    clustering_similarity_metrics:
      - ARI
      - NMI
      - adjusted_mutual_information
    spatial_pattern_similarity:
    figure_sanity:
    runtime_delta:
    memory_delta:
    known_non_equivalence:
```

Validation must distinguish smoke, contract, visual sanity, fidelity, and runtime evidence. Runtime measurement cannot be faked or inferred from static docs. For clustering or domain identification, validation must include label permutation awareness, random seed capture, and a repeated-run policy appropriate to the method's stochastic components.

## Risk Register And Decision Log

```yaml
risk_register:
  scientific_risks:
  engineering_risks:
  environment_risks:
  reproducibility_risks:
  licensing_risks:
  agent_misuse_risks:

decision_log:
  - decision_id:
    decision:
    options_considered:
    rationale:
    evidence_refs:
    decided_by:
    date:
    revisitable:
```

## Acceptance Gate

```yaml
acceptance_gate:
  template_acceptance_status: pass | partial | fail
  implementation_readiness_status: pass | partial | fail
  production_readiness_status: pass | partial | fail
  overall_status:
  rationale:
```

`template_acceptance_status` evaluates whether the Layer3/4 co-design pack is structurally valid for review. `implementation_readiness_status` evaluates whether an MVP adapter implementation can start. `production_readiness_status` evaluates whether runtime support can be claimed. A method can pass template acceptance while failing implementation readiness. Missing environment probe, fixture, runtime measurement, output schema freeze, or symbol-level bindings should block implementation readiness but not necessarily template acceptance. Production readiness must remain `fail` unless actual runtime implementation, validation, and provenance are complete.

Example:

```yaml
acceptance_gate:
  template_acceptance_status: pass
  implementation_readiness_status: fail
  production_readiness_status: fail
  overall_status: partial_with_known_blockers
  rationale:
    - Layer3/Layer4 artifacts are structurally valid.
    - Environment probe has not been run.
    - Minimal smoke fixture has not been executed.
    - Critical Layer4 bindings are file-level rather than symbol-level.
```

Static acceptance and runtime acceptance must stay separate:

```yaml
static_acceptance_gate:
  required_files_exist:
  yaml_valid:
  layer3_layer4_separation_valid:
  evidence_authority_present:
  required_sections_present:
  no_production_claims:
  status:

runtime_acceptance_gate:
  environment_import_probe:
  minimal_fixture_smoke_run:
  runtime_measurement:
  output_schema_observed:
  provenance_observed:
  status:
```

A Layer3/4 review pack can pass static acceptance. Runtime acceptance remains blocked until probes and fixtures run. Production support requires runtime acceptance.

A review pack cannot mark itself `ready_for_review` unless `template_acceptance_status` is `pass`, or `overall_status` is `partial_with_known_blockers` with explicit blockers. Missing Layer4 required sections should produce `partial` or `fail`. Invalid YAML should produce `fail`. Broken links should produce `fail` or `partial`, depending on severity. `ready_for_review` is not a manual label; it is derived from the acceptance gate.

## Full Record Skeleton

```yaml
method_execution_planning_record:
  record_id:
  record_version: v0.7.1
  method_id:
  task_family:
  planning_status:
  authority_status:
  storage_policy:
    generic_template_location: project_repo_allowed
    method_specific_intermediate_location: NAS_required
    project_docs_allowed: false_for_method_specific_intermediates
    production_claim_allowed: false_unless_runtime_implementation_exists
  source_layer2_artifacts:

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

  audit_evidence_registry:
    repository_snapshot:
      url:
      commit_or_release:
      local_path_if_present:
      last_checked:
    evidence_items:
      - evidence_id:
        source_type:
        path_or_url:
        symbol_or_section:
        line_range:
        summary:
        confidence:
        evidence_resolution:
          level:
          implementation_ready:
  code_mind_map:
  function_surface_map:

  canonical_surface_reference:
    surface_id:
    status:
    inherits_from:
  layer3_agent_surface:
    surface_id:
    inherits_from:
    visibility: agent_readable
    spatial_coordinate_source:
      allowed_modes:
        - obsm_spatial
        - obs_x_y_columns
        - adapter_validated_custom_mapping
    multi_sample_policy:
    target_domain_count_policy:
    parameter_policy:
      expose_to_agent:
      expose_to_agent_with_constraints:
      infer_from_input:
      fixed_by_adapter:
      backend_default:
      forbidden_for_agent:
    clustering_backend_policy:
    layer4_reference_policy:
    validation_contract:
    failure_policy:
    provenance_policy:
  layer4_adapter_draft:
    backend_adapter_id:
    linked_surface_id:
    backend_method:
    authority_status: blueprint
    implementation_status: not_implemented
    native_repository:
    evidence_authority:
      registry_file:
      registry_section: Audit Evidence Registry
    runtime_language:
    environment_profile_candidate:
    integration_mode:
    backend_entrypoints:
    call_graph:
    function_surface_bindings:
      - layer3_stage:
        binding_status:
        backend_files_or_functions:
        adapter_responsibility:
        evidence_refs:
        implementation_blocker:
    parameter_mapping:
    input_conversion:
    output_mapping:
    artifact_mapping:
    filesystem_policy:
    failure_translation:
    environment_binding:
    smoke_test:
    fidelity_test:
    rewrite_level:
    rewrite_rationale:
    algorithm_core_touched:
    visibility: implementation_debug_audit_only
    blocking_issues:
    authority_note:

  environment_plan:
  rewrite_decision:
  validation_runtime_plan:
  static_acceptance_gate:
    required_files_exist:
    yaml_valid:
    layer3_layer4_separation_valid:
    evidence_authority_present:
    required_sections_present:
    no_production_claims:
    status:
  runtime_acceptance_gate:
    environment_import_probe:
    minimal_fixture_smoke_run:
    runtime_measurement:
    output_schema_observed:
    provenance_observed:
    status:
  risk_register:
  decision_log:

  subagent_work_plan:
  acceptance_gate:
    template_acceptance_status:
    implementation_readiness_status:
    production_readiness_status:
    overall_status:
    rationale:
  next_action_decision:
```
