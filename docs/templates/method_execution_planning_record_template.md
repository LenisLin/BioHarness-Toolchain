# MethodExecutionPlanningRecord v0.6 Template

```yaml
method_execution_planning_record:
  # Stable planning identifier, not a runtime run id.
  record_id: ""
  record_version: "0.6"
  method_id: ""
  task_family: ""
  planning_status: "blueprint"
  authority_status: "blueprint_only_no_production_adapter"

  # Layer 2 artifacts that promoted this method and define execution constraints.
  source_layer2_artifacts:
    - artifact_id: ""
      path_or_uri: ""
      role: ""
      last_checked: ""
      evidence_refs: []
      confidence: ""

  # Method surface must inherit from the task-family canonical surface.
  canonical_surface_reference:
    canonical_surface_id: ""
    method_surface_id: ""
    inherits_from: ""
    inheritance_scope:
      execution_stages: true
      standard_outputs: true
      common_failure_modes: true
      common_validation_hooks: true
    method_specific_extensions:
      allowed:
        - "method_constraints"
        - "semantic_parameters"
        - "method_local_artifacts"
        - "method_specific_validation"
      forbidden_in_layer3:
        - "backend_file_paths"
        - "raw_backend_function_names"
        - "package_private_parameters"
        - "implementation_call_graph"
    evidence_refs: []
    confidence: ""

  # Compact handoff from Layer 2; do not paste full Layer 2 reasoning here.
  layer2_to_layer3_handoff:
    promoted_method_name: ""
    layer2_role: []
    selection_reason_summary: ""
    claim_boundary: ""
    evidence_boundary: ""
    unresolved_layer2_questions:
      - question: ""
        impact_on_layer3: ""
    evidence_refs: []
    confidence: ""

  # Execution constraints that Layer 3 must honor.
  hard_constraints_for_layer3:
    required_modalities:
      - modality: ""
        reason: ""
        evidence_refs: []
        confidence: ""
    forbidden_modalities:
      - modality: ""
        reason: ""
        evidence_refs: []
        confidence: ""
    required_input_object:
      object_type: ""
      accepted_variants: []
      disallowed_variants: []
      evidence_refs: []
      confidence: ""
    required_spatial_information:
      coordinate_keys: []
      coordinate_system: ""
      library_id_policy: ""
      scale_factor_policy: ""
      evidence_refs: []
      confidence: ""
    histology_requirement:
      status: ""
      accepted_image_inputs: []
      fallback_policy: ""
      evidence_refs: []
      confidence: ""
    reference_requirement:
      status: ""
      accepted_reference_types: []
      species_or_modality_constraints: []
      evidence_refs: []
      confidence: ""
    gpu_requirement:
      status: ""
      gpu_type_or_cuda_notes: ""
      cpu_fallback_policy: ""
      evidence_refs: []
      confidence: ""
    multi_slice_requirement:
      status: ""
      slice_key_policy: ""
      batch_or_library_policy: ""
      evidence_refs: []
      confidence: ""
    minimum_dataset_assumptions:
      min_observations: ""
      min_features: ""
      min_domains_or_clusters: ""
      sparse_dense_policy: ""
      other_assumptions: []
      evidence_refs: []
      confidence: ""

  # Shared evidence ledger. Every substantive claim should point here.
  audit_evidence_registry:
    evidence_refs: []
    confidence: ""
    sources:
      - ref_id: ""
        source_type: ""
        path_or_uri: ""
        version_or_commit: ""
        inspected_items: []
        supports_claims: []
        limitations: []
        evidence_refs: []
        confidence: ""
    unresolved_evidence_gaps:
      - gap: ""
        planned_resolution: ""
        impact_if_unresolved: ""
        evidence_refs: []
        confidence: ""

  # Map the codebase before drafting bindings.
  code_mind_map:
    evidence_refs: []
    confidence: ""
    repository:
      url: ""
      commit_or_release: ""
      license: ""
      last_checked: ""
      evidence_refs: []
      confidence: ""
    install_and_environment_files:
      - path: ""
        role: ""
        evidence_refs: []
        confidence: ""
    examples_and_entrypoints:
      - path_or_uri: ""
        entrypoint_type: ""
        demonstrated_inputs: []
        demonstrated_outputs: []
        evidence_refs: []
        confidence: ""
    backend_modules_and_files:
      - path: ""
        responsibility: ""
        evidence_refs: []
        confidence: ""
    data_flow_notes:
      - stage: ""
        observed_behavior: ""
        evidence_refs: []
        confidence: ""

  # Bridge semantic Layer 3 stages to implementation-only Layer 4 bindings.
  function_surface_map:
    stage_bindings:
      - execution_stage: ""
        layer3_semantic_operation: ""
        layer4_backend_binding_refs: []
        parameter_policy_refs: []
        evidence_refs: []
        confidence: ""
    unmapped_backend_functions:
      - backend_ref: ""
        reason_not_exposed_to_layer3: ""
        evidence_refs: []
        confidence: ""

  # Agent-visible method-specific surface. Keep backend internals out.
  layer3_agent_surface:
    surface_id: ""
    visibility: "agent_visible"
    inherits_from: ""
    task_family: ""
    method_id: ""
    execution_stage_vocab:
      - "input_check"
      - "method_preprocessing"
      - "core_structure_building"
      - "model_fit_or_inference"
      - "output_assignment"
      - "artifact_export"
      - "final_validation"
      - "visualization"
    semantic_inputs:
      - input_id: ""
        object_contract: ""
        required: true
        constraints: []
    semantic_parameters:
      - parameter_id: ""
        meaning: ""
        policy: "" # expose_to_agent | infer_from_input | fixed_by_adapter | backend_default | forbidden_for_agent
        allowed_values_or_range: ""
        default_strategy: ""
        agent_visibility: ""
    semantic_outputs:
      - output_id: ""
        object_location: ""
        required: true
        validation_hook: ""
    standard_artifacts:
      - artifact_id: ""
        artifact_type: ""
        required: true
        provenance_fields: []
    typed_failure_modes:
      - failure_id: ""
        meaning: ""
        agent_action: ""
    layer3_exclusions:
      - "backend_file_paths"
      - "raw_backend_function_names"
      - "package_private_parameters"
      - "implementation_call_graph"
    evidence_refs: []
    confidence: ""

  # Implementation/debug/audit-only binding draft.
  layer4_adapter_draft:
    adapter_id: ""
    visibility: "implementation_debug_audit_only"
    integration_mode: ""
    filesystem_policy:
      working_directory: ""
      input_mounts: []
      output_directory: ""
      temp_storage: ""
      cache_policy: ""
      cleanup_policy: ""
    function_surface_bindings:
      - binding_id: ""
        layer3_stage: ""
        backend_file: ""
        backend_function_or_entrypoint: ""
        call_signature_notes: ""
        evidence_refs: []
        confidence: ""
    parameter_mapping:
      - parameter_id: ""
        layer3_parameter: ""
        backend_parameter: ""
        policy: "" # expose_to_agent | infer_from_input | fixed_by_adapter | backend_default | forbidden_for_agent
        conversion_rule: ""
        evidence_refs: []
        confidence: ""
    input_conversion:
      - input_id: ""
        source_contract: ""
        backend_expected_format: ""
        conversion_steps: []
        evidence_refs: []
        confidence: ""
    output_mapping:
      - output_id: ""
        backend_output: ""
        layer3_output: ""
        extraction_rule: ""
        evidence_refs: []
        confidence: ""
    artifact_mapping:
      - artifact_id: ""
        backend_artifact: ""
        standard_artifact: ""
        export_rule: ""
        evidence_refs: []
        confidence: ""
    failure_translation:
      - backend_signal: ""
        typed_failure: ""
        agent_visible_summary: ""
        evidence_refs: []
        confidence: ""
    smoke_test:
      fixture: ""
      command_or_entrypoint: ""
      expected_observable_io: []
      evidence_refs: []
      confidence: ""
    fidelity_test:
      required: ""
      comparison_target: ""
      metrics_or_checks: []
      evidence_refs: []
      confidence: ""

  # Environment planning is independent from rewrite planning.
  environment_plan:
    environment_profile_candidate: ""
    expected_capsule: ""
    native_package_manager: ""
    install_files: []
    lock_or_container_available: ""
    dependency_conflict_risk: ""
    known_conflicting_dependencies:
      - dependency: ""
        conflict: ""
    gpu_policy: ""
    cuda_policy: ""
    cpu_fallback_policy: ""
    shared_environment_feasibility: ""
    isolation_strategy: ""
    environment_decision: "" # shared_capsule | dedicated_capsule | legacy_capsule | wrapper_boundary | compatibility_rewrite_considered | hold_due_to_environment
    evidence_refs: []
    confidence: ""

  # Split interface standardization from algorithmic rewrite.
  rewrite_plan:
    interface_standardization:
      needed: ""
      scope: []
      rationale: ""
      validation_required: []
      evidence_refs: []
      confidence: ""
    algorithmic_rewrite:
      needed: ""
      touched_algorithm_core: false
      approval_required_if_touched: true
      fidelity_required_if_touched: true
      rationale: ""
      excluded_algorithmic_components: []
      evidence_refs: []
      confidence: ""
    rewrite_decision: ""
    revisitable: true
    unresolved_questions: []

  # Runtime validation planning; visual sanity is not correctness.
  validation_runtime_plan:
    callability_check:
      installable:
        check: ""
        expected_evidence: ""
      runnable_example:
        check: ""
        expected_evidence: ""
      observable_io:
        check: ""
        expected_evidence: ""
    smoke_test:
      fixture: ""
      success_criteria: []
    contract_test:
      input_contract_checks: []
      output_contract_checks: []
    visual_checks:
      visual_sanity_scope: ""
      not_biological_correctness: true
      not_algorithmic_equivalence: true
      checks: []
    reproducibility_checks:
      random_seed_policy: ""
      determinism_policy: ""
      repeated_runs: ""
      label_permutation_awareness: ""
      stochastic_components: []
    rewrite_comparison:
      required: ""
      schema_equivalence: ""
      domain_count: ""
      no_empty_domain: ""
      label_permutation: ""
      ari_nmi_ami: ""
      spatial_pattern_sanity: ""
      runtime_memory_delta: ""
    runtime_cost_record:
      wall_time: ""
      peak_memory: ""
      device_used: ""
      fixture_size: ""
    evidence_refs: []
    confidence: ""

  # Track risks by type, with mitigation and evidence.
  risk_register:
    scientific_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""
    engineering_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""
    environment_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""
    reproducibility_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""
    licensing_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""
    agent_misuse_risks:
      - risk: ""
        mitigation: ""
        evidence_refs: []
        confidence: ""

  # Every material choice should be revisitable or explicitly fixed.
  decision_log:
    - decision_id: ""
      decision: ""
      options: []
      rationale: ""
      evidence_refs: []
      revisitable: true
      revisit_trigger: ""
      confidence: ""

  # Use when multiple code-reading or evidence tasks are split up.
  subagent_work_plan:
    shared_evidence_ledger:
      location: ""
      update_rule: ""
    source_priority:
      - priority: 1
        source_type: ""
        reason: ""
    subagent_tasks:
      - task_id: ""
        assignment: ""
        inputs: []
        expected_output:
          must_include:
            - "evidence_refs"
            - "confidence"
            - "unresolved_questions"
            - "proposed_layer3_implications"
            - "proposed_layer4_implications"
        handoff_notes: ""
    integration_rule: ""
    unresolved_questions: []

  # Next planning action only; this is not an implementation claim.
  next_action_decision:
    decision: ""
    allowed_values:
      - "draft_layer3_surface"
      - "draft_layer4_adapter"
      - "request_more_evidence"
      - "run_environment_probe"
      - "hold_due_to_environment"
      - "hold_due_to_api_or_licensing"
      - "reject_for_current_cycle"
    rationale: ""
    evidence_refs: []
    confidence: ""
```
