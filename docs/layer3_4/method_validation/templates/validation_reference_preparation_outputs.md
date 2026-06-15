# Validation Reference Preparation Outputs

## Required Method Result

```yaml
validation_reference_preparation_result:
  method:
  accepted_status: REFERENCE_READY | REFERENCE_FAIL
  reference_mode: static_expected_result | author_workflow_generated_in_run
  reference_status: available | failed
  stage_handoff_evidence:
    instantiated_method_prompt:
    stage1_input_preparation_result:
    canonical_input_path:
  analysis_problem_reference_expectation:
  reference_target_discovery:
    inspected_locators:
    discovered_output_candidates:
    selected_primary_target:
    expected_artifact_class:
    selection_rationale:
    acquisition_route:
    fallback_policy:
    export_only_scope:
  reference_acquisition:
    provenance_class:
    static_route:
    generation_route:
    environment_invocation:
      reviewed_environment_source:
      conda_prefix:
      executable:
      environment_variables:
      bare_prefix_check:
      full_invocation_check:
      final_invocation_used:
      invocation_status:
    author_parameter_fidelity:
      reviewed_author_parameter_sources:
      author_default_or_tutorial_parameters:
      actual_execution_parameters:
      parameter_differences:
      output_affecting_parameter_changes:
      runtime_only_adjustments:
      reviewed_acceptance_for_differences:
      fidelity_status:
    gpu_resource_retry_evidence:
      required:
      author_device:
      author_batch_size:
      author_epochs:
      oom_log_paths:
      gpu_memory_snapshots:
      retry_candidates:
      retry_results:
      selected_device:
      selected_batch_size:
      selected_batch_size_rationale:
      preserved_author_parameters:
      cpu_fallback_attempted:
      cpu_fallback_rationale:
      status:
    compatibility_patch_evidence:
      applied:
      patch_scope:
      allowed_patch_classes:
      patched_files:
      diff_paths:
      rationale:
      author_repo_modified: true | false
      preprocessing_parameter_consistency:
      output_affecting_parameter_changed: true | false
      retry_logs:
      reviewed_acceptance:
    native_command_or_loader:
    native_input_layout_materialization:
      required:
      scope:
      reviewed_locators:
      source_artifacts:
      actions:
      materialized_paths:
      path_format_usability_checks:
      canonical_input_changed: true | false
      status:
    runtime_monitoring:
      required:
      pid:
      heartbeat_interval:
      reviewed_timeout:
      no_progress_threshold:
      host_snapshots:
      progress_log:
      termination_reason:
    bioharness_surface_used:
    bioharness_surface_use_scope:
    route_contamination_evidence:
    retry_attempts:
    export_only_modification:
    acquisition_status:
  reference_artifacts:
    primary:
      artifact_class:
      raw_artifact:
      standardized_artifact:
      key_field_or_slot:
      structure_summary:
    auxiliary:
  acquisition_evidence:
    actual_paths:
    commands_or_loader_calls:
    logs:
    host_monitoring_logs:
    return_codes:
    parser_or_loader_summary:
  generation_evidence:
  failure_evidence:
    failure_reason:
    planning_requirement_checked:
      analysis_problem_reference_expectation:
      expected_result_class:
      acceptable_artifact_classes:
    target_discovery_attempt:
      inspected_locators:
      author_output_candidates:
      selected_primary_target:
      rejected_candidates:
      decision:
      evidence_summary:
    static_artifact_attempt:
      searched_paths:
      matched_artifacts:
      read_or_load_attempted:
      read_or_load_result:
      log_paths:
    native_workflow_attempt:
      required:
      command_or_api:
      workdir:
      environment:
      input_layout_checks:
        required_files:
        existing_files:
        missing_files:
        materialization_attempted:
        materialization_result:
        canonical_input_changed:
        log_paths:
      output_dir:
      started:
      return_code:
      log_paths:
      produced_artifacts:
      runtime_monitoring:
        required:
        pid:
        heartbeat_interval:
        reviewed_timeout:
        no_progress_threshold:
        progress_log:
        host_snapshots:
        termination_reason:
    export_or_parser_attempt:
      required:
      export_scope:
      attempted_exports:
      parser_or_loader_calls:
      result:
      log_paths:
    retry_attempts:
    final_failure_boundary:
      last_completed_step:
      unresolved_failure:
      why_not_reference_ready:
  files_written:
```

## Output Rule

`REFERENCE_READY` requires target discovery evidence, a selected primary target, completed native/static acquisition route, materialized primary or reviewed alternate reference artifact, parser or loader summary, and written output records.

Every method result must record `stage_handoff_evidence.instantiated_method_prompt`, `stage_handoff_evidence.stage1_input_preparation_result`, and `stage_handoff_evidence.canonical_input_path`.

`REFERENCE_READY` requires native/static provenance. `bioharness_surface_used: true` cannot satisfy primary reference acquisition.

BioHarness-generated artifacts may be listed only as auxiliary or diagnostic evidence during Stage 2 reference preparation.

Static reference evidence requires an actual local artifact read or load record.

Generated reference evidence requires command or workflow execution evidence, return code, log path, produced artifact evidence, and parser or loader summary.

Generated reference evidence must record author parameter fidelity. `REFERENCE_READY` is acceptable only when `fidelity_status` is `exact_match`, `runtime_only_adjusted`, or `reviewed_output_affecting_adjusted`.

A generated reference with unreviewed output-affecting parameter changes is verifier repair evidence, not an accepted `REFERENCE_READY`.

Generated GPU training references that encounter CUDA OOM must record `gpu_resource_retry_evidence`. A smaller batch size may be accepted only as a reviewed output-affecting resource adjustment when the result preserves author epochs, learning rate, seed policy, model parameters, preprocessing parameters, selected target, and result field. Reduced-epoch runs are diagnostic only and cannot satisfy `REFERENCE_READY`.

Generated reference evidence that uses copied-source compatibility patches must record `compatibility_patch_evidence`. The patch is acceptable only when it is confined to the Stage2 owned copied workdir, has diff/log evidence, preserves the selected target, author workflow input, core algorithm call, output-affecting parameters, and label alignment logic, and does not modify the reviewed author source repository.

Compatibility patches for dependency APIs, language bridges, pathing, export-only wrapping, matrix orientation, dtype conversion, sparse/dense conversion, NA/NaN handling, and randomness-control plumbing may be classified as runtime-only when the preservation checks are recorded for the affected patch class. These checks should be the minimal applicable before/after or rationale evidence needed to show that author workflow input identity, selected target, core algorithm call, output-affecting parameter values, and label alignment logic were preserved. Preprocessing code changes require explicit preprocessing parameter consistency evidence.

When a reviewed conda prefix or runtime environment is used, generated or static parser evidence must record the complete runtime invocation. A bare prefix executable failure cannot be used as final environment-failure evidence unless the complete reviewed invocation was also tested.

Generated reference evidence that depends on native author input-layout materialization must record `native_input_layout_materialization` evidence. Missing native layout files cannot support an accepted `REFERENCE_FAIL` unless lightweight materialization was attempted or the evidence records why materialization would exceed the reviewed boundary.

For long-running generated references, return code alone is insufficient when the process is externally terminated or times out. The result must include runtime monitoring evidence and a termination reason.

`REFERENCE_FAIL` requires the hard-filled `failure_evidence` block. It must include planning requirement review, target discovery attempt, static artifact attempt, native workflow attempt when required, export/parser attempt when required, retry attempts for simple local issues, and final failure boundary.

A result that has not run the native workflow/API after static artifact absence is verifier repair evidence, not an accepted `REFERENCE_FAIL`, unless complete `failure_evidence` records a preflight blocker after lightweight native input layout materialization was attempted, or records why materialization would exceed the reviewed boundary.
