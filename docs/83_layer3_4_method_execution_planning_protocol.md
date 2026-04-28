# Layer 3/4 Method Execution Planning Protocol v0.6

## Status

Blueprint / protocol draft. This document freezes the current planning protocol and record shape for Layer 3/4 method engineering, but it does not claim that any production Layer 3 surface, Layer 4 adapter, environment capsule, wrapper, rewrite, runtime dispatcher, or validation runner has been implemented.

## Purpose

Given a Layer 2 promoted method name, such as `BANKSY`, this protocol guides code reading and subagent-style work decomposition to produce a `MethodExecutionPlanningRecord`. The record is an engineering-stage planning object. It gathers the Layer 2 handoff, canonical surface inheritance, method-specific Layer 3 surface plan, Layer 4 adapter draft, environment plan, rewrite plan, validation/runtime plan, risks, decisions, and evidence ledger into one auditable record.

The record is not a runtime API. Its downstream outputs are separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` drafts.

## Core Principles

- Layer 3 is agent-visible by default. It should describe the method-specific execution surface in semantic BioHarness terms.
- Layer 4 is hidden by default and exposed only for implementation, debugging, or audit. It records concrete backend files, functions, entrypoints, parameters, I/O, error behavior, and fidelity checks.
- Layer 3 is a method-specific realization, but it must inherit from a canonical task-family surface.
- Layer 3 uses the BioHarness unified `execution_stage_vocab` defined in this protocol.
- Layer 4 records the real backend binding evidence and must stay separate from the agent-facing Layer 3 surface.
- BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.
- Scientific review is bounded. The planning record checks evidence boundaries and claim boundaries, but it does not perform a paper-level scientific re-review or claim biological correctness.
- Layer 2 method-comparison reasoning should not be copied wholesale into Layer 3. Layer 2 hard constraints required for execution must be carried forward.

## Canonical Surface Reference

Every promoted method must first identify the canonical task-family surface that it realizes.

For spatial domain identification:

```yaml
canonical_surface_reference:
  task_family: spatial_domain_identification
  canonical_surface_id: spatial_domain_identification.canonical.v1
  method_surface_id: spatial_domain_identification.banksy.v1
  inheritance_rule: method_surface_inherits_canonical_stages_and_standard_outputs
```

`spatial_domain_identification.banksy.v1` should inherit from `spatial_domain_identification.canonical.v1`. The canonical family surface should at minimum define:

- the unified execution stages used by all spatial domain identification methods
- standard semantic inputs such as spatial expression data and spatial coordinate information
- standard semantic outputs such as domain labels, output object field locations, summary metadata, diagnostic artifacts, validation report, and provenance record
- common failure categories and validation expectations

A method-specific Layer 3 realization may add method-specific constraints, parameters, optional artifacts, and validation checks. It must not expose backend source file paths, raw backend function names, package-private parameters, or call graphs; those belong in Layer 4.

## Execution Stage Vocabulary

Layer 3 records must use this shared `execution_stage_vocab`:

| Stage | Meaning |
| --- | --- |
| `input_check` | Validate required input object, modalities, spatial keys, requested parameters, and method constraints before execution. |
| `method_preprocessing` | Method-local preprocessing required by the selected method. This is not global Scanpy/ST preprocessing such as general QC, normalization, HVG selection, PCA, or generic clustering unless the method itself requires a local transformation. |
| `core_structure_building` | Build method-specific structures such as neighborhood graphs, spatial kernels, multiscale neighborhoods, histology features, or internal matrices. |
| `model_fit_or_inference` | Run the main fitting, optimization, inference, clustering, or prediction step. |
| `output_assignment` | Assign semantic outputs into the agreed object fields or result tables. |
| `artifact_export` | Export standard artifacts such as summaries, plots, metrics, logs, and provenance files. |
| `final_validation` | Check output schema, labels, counts, artifacts, reproducibility metadata, and typed failure conditions. |
| `visualization` | Generate optional or required visual artifacts for human sanity inspection. |

## Parameter Policy

Layer 3 parameter plans must classify every parameter using this vocabulary:

| Policy | Meaning |
| --- | --- |
| `expose_to_agent` | Safe, bounded semantic parameter visible to the agent or harness. |
| `infer_from_input` | Derived from the input object or Layer 2 hard constraints. |
| `fixed_by_adapter` | Fixed by the BioHarness method realization to keep behavior stable. |
| `backend_default` | Intentionally passed through as the backend default and documented as such in Layer 4. |
| `forbidden_for_agent` | Backend/internal parameter that must not be agent-controlled. |

## Evidence And Confidence Rules

`audit_evidence_registry` is the shared ledger for all claims made during planning. `code_mind_map` records where relevant code, examples, environment files, and I/O behavior were observed. Both sections must carry `evidence_refs` and `confidence`.

Evidence references should be local, inspectable, and specific when possible: repository files, line ranges when available, release tags, local docs, package metadata, example notebooks, scripts, or test fixtures. If evidence is absent or indirect, the record must say so and lower confidence.

Use confidence values consistently:

- `high`: directly observed in source, examples, metadata, or tests.
- `medium`: inferred from multiple partial sources.
- `low`: plausible but weakly evidenced; must remain unresolved or revisitable.

## MethodExecutionPlanningRecord v0.6

The following YAML skeleton defines the complete planning record shape. A fillable copy lives in [docs/templates/method_execution_planning_record_template.md](templates/method_execution_planning_record_template.md).

```yaml
method_execution_planning_record:
  record_id:
  record_version: "0.6"
  method_id:
  task_family:
  planning_status:
  authority_status:
  source_layer2_artifacts:
    - artifact_id:
      path_or_uri:
      role:
      last_checked:
      evidence_refs:
        - ref_id:
      confidence:

  canonical_surface_reference:
    canonical_surface_id:
    method_surface_id:
    inherits_from:
    inheritance_scope:
      execution_stages: true
      standard_outputs: true
      common_failure_modes: true
      common_validation_hooks: true
    method_specific_extensions:
      allowed:
        - method_constraints
        - semantic_parameters
        - method_local_artifacts
        - method_specific_validation
      forbidden_in_layer3:
        - backend_file_paths
        - raw_backend_function_names
        - package_private_parameters
        - implementation_call_graph
    evidence_refs:
      - ref_id:
    confidence:

  layer2_to_layer3_handoff:
    promoted_method_name:
    layer2_role:
    selection_reason_summary:
    claim_boundary:
    evidence_boundary:
    unresolved_layer2_questions:
      - question:
        impact_on_layer3:
    evidence_refs:
      - ref_id:
    confidence:

  hard_constraints_for_layer3:
    required_modalities:
      - modality:
        reason:
        evidence_refs:
          - ref_id:
        confidence:
    forbidden_modalities:
      - modality:
        reason:
        evidence_refs:
          - ref_id:
        confidence:
    required_input_object:
      object_type:
      accepted_variants:
        - variant:
      disallowed_variants:
        - variant:
      evidence_refs:
        - ref_id:
      confidence:
    required_spatial_information:
      coordinate_keys:
        - key:
      coordinate_system:
      library_id_policy:
      scale_factor_policy:
      evidence_refs:
        - ref_id:
      confidence:
    histology_requirement:
      status:
      accepted_image_inputs:
        - image_type:
      fallback_policy:
      evidence_refs:
        - ref_id:
      confidence:
    reference_requirement:
      status:
      accepted_reference_types:
        - reference_type:
      species_or_modality_constraints:
        - constraint:
      evidence_refs:
        - ref_id:
      confidence:
    gpu_requirement:
      status:
      gpu_type_or_cuda_notes:
      cpu_fallback_policy:
      evidence_refs:
        - ref_id:
      confidence:
    multi_slice_requirement:
      status:
      slice_key_policy:
      batch_or_library_policy:
      evidence_refs:
        - ref_id:
      confidence:
    minimum_dataset_assumptions:
      min_observations:
      min_features:
      min_domains_or_clusters:
      sparse_dense_policy:
      other_assumptions:
        - assumption:
      evidence_refs:
        - ref_id:
      confidence:

  audit_evidence_registry:
    evidence_refs:
      - ref_id:
    confidence:
    sources:
      - ref_id:
        source_type:
        path_or_uri:
        version_or_commit:
        inspected_items:
          - item:
        supports_claims:
          - claim_id:
        limitations:
          - limitation:
        evidence_refs:
          - ref_id:
        confidence:
    unresolved_evidence_gaps:
      - gap:
        planned_resolution:
        impact_if_unresolved:
        evidence_refs:
          - ref_id:
        confidence:

  code_mind_map:
    evidence_refs:
      - ref_id:
    confidence:
    repository:
      url:
      commit_or_release:
      license:
      last_checked:
      evidence_refs:
        - ref_id:
      confidence:
    install_and_environment_files:
      - path:
        role:
        evidence_refs:
          - ref_id:
        confidence:
    examples_and_entrypoints:
      - path_or_uri:
        entrypoint_type:
        demonstrated_inputs:
          - input:
        demonstrated_outputs:
          - output:
        evidence_refs:
          - ref_id:
        confidence:
    backend_modules_and_files:
      - path:
        responsibility:
        evidence_refs:
          - ref_id:
        confidence:
    data_flow_notes:
      - stage:
        observed_behavior:
        evidence_refs:
          - ref_id:
        confidence:

  function_surface_map:
    stage_bindings:
      - execution_stage:
        layer3_semantic_operation:
        layer4_backend_binding_refs:
          - binding_id:
        parameter_policy_refs:
          - parameter_id:
        evidence_refs:
          - ref_id:
        confidence:
    unmapped_backend_functions:
      - backend_ref:
        reason_not_exposed_to_layer3:
        evidence_refs:
          - ref_id:
        confidence:

  layer3_agent_surface:
    surface_id:
    visibility: agent_visible
    inherits_from:
    task_family:
    method_id:
    execution_stage_vocab:
      - input_check
      - method_preprocessing
      - core_structure_building
      - model_fit_or_inference
      - output_assignment
      - artifact_export
      - final_validation
      - visualization
    semantic_inputs:
      - input_id:
        object_contract:
        required:
        constraints:
          - constraint:
    semantic_parameters:
      - parameter_id:
        meaning:
        policy:
        allowed_values_or_range:
        default_strategy:
        agent_visibility:
    semantic_outputs:
      - output_id:
        object_location:
        required:
        validation_hook:
    standard_artifacts:
      - artifact_id:
        artifact_type:
        required:
        provenance_fields:
          - field:
    typed_failure_modes:
      - failure_id:
        meaning:
        agent_action:
    layer3_exclusions:
      - backend_file_paths
      - raw_backend_function_names
      - package_private_parameters
      - implementation_call_graph
    evidence_refs:
      - ref_id:
    confidence:

  layer4_adapter_draft:
    adapter_id:
    visibility: implementation_debug_audit_only
    integration_mode:
    filesystem_policy:
      working_directory:
      input_mounts:
        - mount:
      output_directory:
      temp_storage:
      cache_policy:
      cleanup_policy:
    function_surface_bindings:
      - binding_id:
        layer3_stage:
        backend_file:
        backend_function_or_entrypoint:
        call_signature_notes:
        evidence_refs:
          - ref_id:
        confidence:
    parameter_mapping:
      - parameter_id:
        layer3_parameter:
        backend_parameter:
        policy:
        conversion_rule:
        evidence_refs:
          - ref_id:
        confidence:
    input_conversion:
      - input_id:
        source_contract:
        backend_expected_format:
        conversion_steps:
          - step:
        evidence_refs:
          - ref_id:
        confidence:
    output_mapping:
      - output_id:
        backend_output:
        layer3_output:
        extraction_rule:
        evidence_refs:
          - ref_id:
        confidence:
    artifact_mapping:
      - artifact_id:
        backend_artifact:
        standard_artifact:
        export_rule:
        evidence_refs:
          - ref_id:
        confidence:
    failure_translation:
      - backend_signal:
        typed_failure:
        agent_visible_summary:
        evidence_refs:
          - ref_id:
        confidence:
    smoke_test:
      fixture:
      command_or_entrypoint:
      expected_observable_io:
        - observation:
      evidence_refs:
        - ref_id:
      confidence:
    fidelity_test:
      required:
      comparison_target:
      metrics_or_checks:
        - check:
      evidence_refs:
        - ref_id:
      confidence:

  environment_plan:
    environment_profile_candidate:
    expected_capsule:
    native_package_manager:
    install_files:
      - path:
    lock_or_container_available:
    dependency_conflict_risk:
    known_conflicting_dependencies:
      - dependency:
        conflict:
    gpu_policy:
    cuda_policy:
    cpu_fallback_policy:
    shared_environment_feasibility:
    isolation_strategy:
    environment_decision:
    evidence_refs:
      - ref_id:
    confidence:

  rewrite_plan:
    interface_standardization:
      needed:
      scope:
        - scope_item:
      rationale:
      validation_required:
        - check:
      evidence_refs:
        - ref_id:
      confidence:
    algorithmic_rewrite:
      needed:
      touched_algorithm_core:
      approval_required_if_touched:
      fidelity_required_if_touched:
      rationale:
      excluded_algorithmic_components:
        - component:
      evidence_refs:
        - ref_id:
      confidence:
    rewrite_decision:
    revisitable:
    unresolved_questions:
      - question:

  validation_runtime_plan:
    callability_check:
      installable:
        check:
        expected_evidence:
      runnable_example:
        check:
        expected_evidence:
      observable_io:
        check:
        expected_evidence:
    smoke_test:
      fixture:
      success_criteria:
        - criterion:
    contract_test:
      input_contract_checks:
        - check:
      output_contract_checks:
        - check:
    visual_checks:
      visual_sanity_scope:
      not_biological_correctness: true
      not_algorithmic_equivalence: true
      checks:
        - check:
    reproducibility_checks:
      random_seed_policy:
      determinism_policy:
      repeated_runs:
      label_permutation_awareness:
      stochastic_components:
        - component:
    rewrite_comparison:
      required:
      schema_equivalence:
      domain_count:
      no_empty_domain:
      label_permutation:
      ari_nmi_ami:
      spatial_pattern_sanity:
      runtime_memory_delta:
    runtime_cost_record:
      wall_time:
      peak_memory:
      device_used:
      fixture_size:
    evidence_refs:
      - ref_id:
    confidence:

  risk_register:
    scientific_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:
    engineering_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:
    environment_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:
    reproducibility_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:
    licensing_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:
    agent_misuse_risks:
      - risk:
        mitigation:
        evidence_refs:
          - ref_id:
        confidence:

  decision_log:
    - decision_id:
      decision:
      options:
        - option:
      rationale:
      evidence_refs:
        - ref_id:
      revisitable:
      revisit_trigger:
      confidence:

  subagent_work_plan:
    shared_evidence_ledger:
      location:
      update_rule:
    source_priority:
      - priority:
        source_type:
        reason:
    subagent_tasks:
      - task_id:
        assignment:
        inputs:
          - input:
        expected_output:
          must_include:
            - evidence_refs
            - confidence
            - unresolved_questions
            - proposed_layer3_implications
            - proposed_layer4_implications
        handoff_notes:
    integration_rule:
    unresolved_questions:
      - question:

  next_action_decision:
    decision:
    allowed_values:
      - draft_layer3_surface
      - draft_layer4_adapter
      - request_more_evidence
      - run_environment_probe
      - hold_due_to_environment
      - hold_due_to_api_or_licensing
      - reject_for_current_cycle
    rationale:
    evidence_refs:
      - ref_id:
    confidence:
```

## Top-Level Field Reference

| Field | Required interpretation |
| --- | --- |
| `record_id` | Stable identifier for this planning record. It should include task family, method, and version or date if useful. |
| `record_version` | Protocol version. For this document, use `0.6`. |
| `method_id` | Stable method identifier normalized for BioHarness planning. |
| `task_family` | Layer 2 task family that promoted the method, such as `spatial_domain_identification`. |
| `planning_status` | Draft state such as `blueprint`, `protocol_draft`, `planning_in_progress`, `blocked`, or `ready_for_surface_draft`; it is not implementation status. |
| `authority_status` | Authority boundary statement, for example `blueprint_only_no_production_adapter`. |
| `source_layer2_artifacts` | Layer 2 files or records that justify method promotion and provide hard constraints. |
| `canonical_surface_reference` | The canonical task-family surface inherited by the method-specific surface, plus what is inherited and what remains method-specific. |
| `layer2_to_layer3_handoff` | Condensed Layer 2 role, selection rationale, evidence boundary, claim boundary, and unresolved questions needed for Layer 3 planning. |
| `hard_constraints_for_layer3` | Execution-relevant constraints from Layer 2 and code evidence, including modalities, input object, spatial information, histology, reference, GPU, multi-slice, and minimum dataset assumptions. |
| `audit_evidence_registry` | Shared ledger of all inspected sources, their support for claims, limitations, evidence references, and confidence. |
| `code_mind_map` | Navigational map of repository structure, installation files, examples, backend files, entrypoints, data flow, and observed I/O behavior. |
| `function_surface_map` | Engineering bridge that maps Layer 3 semantic stages to Layer 4 backend bindings without putting backend details into the Layer 3 surface. |
| `layer3_agent_surface` | Draft method-specific Layer 3 surface, inheriting the canonical family surface and exposing only agent/harness-safe semantic inputs, parameters, outputs, artifacts, failures, and validation hooks. |
| `layer4_adapter_draft` | Draft Layer 4 binding, including integration mode, filesystem policy, real backend bindings, parameter mapping, input/output/artifact mapping, failure translation, smoke test, and fidelity test. |
| `environment_plan` | Independent environment planning artifact. It records package manager, install evidence, capsule candidate, conflicts, GPU/CUDA/CPU policy, shared-environment feasibility, isolation strategy, and decision. |
| `rewrite_plan` | Separate plan for interface standardization and algorithmic rewrite. Interface standardization is expected; algorithmic rewrite is conservative and requires fidelity and approval when touching algorithm core. |
| `validation_runtime_plan` | Plan for installability, runnable example, observable I/O, smoke tests, contract tests, visual sanity, reproducibility, rewrite comparison, and runtime cost recording. |
| `risk_register` | Risk inventory separated into scientific, engineering, environment, reproducibility, licensing, and agent-misuse risks. |
| `decision_log` | Auditable list of decisions, considered options, rationale, evidence references, confidence, and whether the decision is revisitable. |
| `subagent_work_plan` | Decomposition plan for code-reading or evidence-gathering workers, including shared evidence ledger, source priority, required output contract, and integration rule. |
| `next_action_decision` | Recommended next planning action. It must stay within blueprint/protocol state unless implementation is separately approved. |

## Subagent Work Requirements

When work is split across reviewers or subagents, every output must update or reference the same shared evidence ledger. Source priority should be explicit and should favor current source code, released package metadata, installation files, examples, tests, and local project documents over secondary descriptions.

Subagent outputs must include:

- `evidence_refs`
- `confidence`
- `unresolved_questions`
- proposed Layer 3 implications
- proposed Layer 4 implications

Subagent outputs must not independently freeze architecture. The integrating record owner decides whether an implication becomes part of the planning record.

## Test / Pilot Plan

Pilot 1: `BANKSY`.

- Goal: exercise the template end to end for a CPU-first, multiscale, context-aware spatial domain method.
- Planning emphasis: canonical inheritance, multiscale/context constraints, method-local preprocessing, parameter contract, standard domain-label outputs, and CPU-first environment feasibility.
- Expected output: a complete `MethodExecutionPlanningRecord v0.6` draft, not a production adapter claim.

Pilot 2: `SpaGCN`.

- Goal: stress test the protocol on histology-aware graph/deep learning execution.
- Planning emphasis: histology requirement, graph construction, GPU/CUDA policy, wrapper boundary, stochastic training behavior, visual sanity limits, and rewrite/fidelity pressure.
- Expected output: a complete planning record that clarifies whether the method enters wrapper planning, dedicated capsule planning, or hold.

Pilot 3: hold / legacy / no-clean-API negative case.

- Goal: verify that the template can refuse, hold, or defer a method rather than forcing an adapter path.
- Planning emphasis: weak callable API, missing install evidence, brittle filesystem assumptions, licensing uncertainty, opaque outputs, or environment conflicts.
- Expected output: a record whose `next_action_decision` is hold or reject for the current cycle, with evidence and unresolved questions.
