# Method Execution Planning Record Template v0.7

This historical v0.7 template is retained for compatibility. The current generic template is [Method Execution Planning Record Template v0.7.1](method_execution_planning_record_v0.7.1.md).

`MethodExecutionPlanningRecord v0.7` supersedes v0.5 and v0.6 planning language. It is an engineering-stage co-design record, not a runtime API and not a production-support claim.

Method-specific Layer3/4 audit outputs are intermediate engineering artifacts. They must be stored in the NAS results workspace, not under project docs. The project repository may contain only generic templates, schemas, and design documentation.

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

A shorter NAS-existing file must not be selected over a richer recovered/exported file if the richer file contains required Layer4 sections and can be normalized. Select the most complete valid artifact, then apply v0.7 normalization.

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
  infer_from_input:
  fixed_by_adapter:
  backend_default:
  forbidden_for_agent:
```

Agent-visible parameters must be semantic. Backend low-level parameters must be hidden unless explicitly promoted. Unsafe memory flags, raw file paths, temporary file names, and backend internal knobs must be forbidden for default agent use.

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
```

`inferred` evidence must not be treated as firm implementation fact. Layer4 claims must cite evidence IDs. Layer4 adapter drafts must include:

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

`hold_due_to_environment` must not be used as a final decision unless an environment subagent report cites a failed probe or impossible dependency constraint.

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
  required_files_exist:
  layer3_surface_yaml_valid:
  layer4_adapter_yaml_valid:
  environment_plan_valid:
  review_pack_links_valid:
  evidence_authority_present:
  layer3_no_backend_function_names:
  layer4_required_sections_present:
  environment_hold_not_final_without_probe:
  coordinate_contract_normalized:
  multi_sample_policy_normalized:
  target_domain_count_policy_present:
  validation_taxonomy_complete:
  risk_register_present:
  decision_log_present:
  production_claim_absent:
  status: pass | partial | fail
```

A review pack cannot mark itself `ready_for_review` unless the acceptance gate is `pass` or explicitly `partial_with_known_blockers`. Missing Layer4 required sections should produce `partial` or `fail`. Invalid YAML should produce `fail`. Broken links should produce `fail` or `partial`, depending on severity. `ready_for_review` is not a manual label; it is derived from the acceptance gate.

## Full Record Skeleton

```yaml
method_execution_planning_record:
  record_id:
  record_version: v0.7
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
      infer_from_input:
      fixed_by_adapter:
      backend_default:
      forbidden_for_agent:
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
  risk_register:
  decision_log:

  subagent_work_plan:
  acceptance_gate:
  next_action_decision:
```
