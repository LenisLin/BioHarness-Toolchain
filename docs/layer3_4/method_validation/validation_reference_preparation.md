# Validation Reference Preparation

## Purpose

Prepare reference evidence for method-level output review by separating `reference_target_discovery` from `reference_acquisition`. Discovery identifies the method-specific reference target from reviewed author workflow, example, vignette, or source locators. Acquisition obtains the selected reference artifact only from native or static author routes.

Reference acquisition may come from a static author artifact read/load, an original/native author workflow run, a native package/API path matching the author workflow, or a native runtime object export. BioHarness Layer3/Layer4 callable chains, bridge replay, and method harness runs are Stage 3 comparison routes and must not be used as primary Stage 2 reference acquisition.

## Required Output

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
    provenance_class: static_author_artifact | native_author_workflow_run | native_package_api_call | native_runtime_export | failed
    static_route:
    generation_route:
    native_command_or_loader:
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
      fidelity_status: exact_match | runtime_only_adjusted | reviewed_output_affecting_adjusted | unreviewed_output_affecting_changed
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
    bioharness_surface_used: true | false
    bioharness_surface_use_scope:
    route_contamination_evidence:
    retry_attempts:
    export_only_modification:
    acquisition_status:
  reference_artifacts:
    primary:
    auxiliary:
  acquisition_evidence:
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

## Workflow

```text
BEGIN VALIDATION_REFERENCE_PREPARATION

LOAD PLANNING_REFERENCE_REQUIREMENT
LOAD CANONICAL_INPUT_EVIDENCE
LOAD AUTHOR_WORKFLOW_LOCATORS
LOAD REVIEWED_OUTPUT_ROOT
LOAD FORBIDDEN_PRIMARY_ACQUISITION_ROUTES

VERIFY PLANNING_REFERENCE_REQUIREMENT DEFINES EXPECTED RESULT CLASS
VERIFY PLANNING_REFERENCE_REQUIREMENT DEFINES ACCEPTABLE ARTIFACT CLASSES
VERIFY CANONICAL_INPUT_EVIDENCE WAS SUPPLIED BY THE INSTANTIATED METHOD PROMPT
VERIFY CANONICAL_INPUT_EVIDENCE REFERENCES THE METHOD STAGE1 VALIDATION_INPUT_PREPARATION_RESULT
VERIFY CANONICAL_INPUT_PATH EXISTS
RECORD STAGE_HANDOFF_EVIDENCE WITH INSTANTIATED_METHOD_PROMPT STAGE1_INPUT_PREPARATION_RESULT AND CANONICAL_INPUT_PATH

INSPECT AUTHOR_WORKFLOW_LOCATORS
IDENTIFY AUTHOR_OUTPUT_CANDIDATES FROM TUTORIAL EXAMPLE VIGNETTE SOURCE
FILTER AUTHOR_OUTPUT_CANDIDATES BY PLANNING_REFERENCE_REQUIREMENT
REJECT ANNOTATION COORDINATE INPUT_SIDECAR GROUND_TRUTH PLOT CONFIG EXPECTED_PATH_ONLY CANDIDATES
SELECT PRIMARY_REFERENCE_TARGET ONLY IF AUTHOR_EVIDENCE AND PLANNING_REQUIREMENT BOTH SUPPORT IT

IF NO PRIMARY_REFERENCE_TARGET IS SELECTED
  RECORD FAILURE_EVIDENCE WITH PLANNING_REQUIREMENT_CHECKED INSPECTED_LOCATORS AUTHOR_OUTPUT_CANDIDATES REJECTED_CANDIDATES AND FAILURE_REASON
  RETURN REFERENCE_FAIL
END IF

SEARCH REVIEWED LOCAL AUTHOR_RESULT_ARTIFACTS FOR PRIMARY_REFERENCE_TARGET

IF LOCAL STATIC AUTHOR_RESULT_ARTIFACT EXISTS
  LOAD COMPLETE REVIEWED_RUNTIME_INVOCATION WHEN A REVIEWED PREFIX OR RUNTIME ENVIRONMENT IS USED FOR STATIC PARSING
  READ OR LOAD LOCAL STATIC AUTHOR_RESULT_ARTIFACT
  PARSE PRIMARY_REFERENCE_TARGET FIELD
  RECORD ENVIRONMENT_INVOCATION WHEN STATIC PARSER USES A REVIEWED PREFIX OR RUNTIME ENVIRONMENT
  STANDARDIZE REFERENCE LABELS TO REQUIRED OUTPUT ARTIFACT
  RECORD LOADER PARSER SUMMARY
  RECORD FILES_WRITTEN
  RETURN REFERENCE_READY
END IF

PREPARE NATIVE_AUTHOR_WORKFLOW_EXECUTION
LOAD COMPLETE REVIEWED_RUNTIME_INVOCATION WHEN A REVIEWED PREFIX OR RUNTIME ENVIRONMENT IS USED
VERIFY WORKDIR FULL_RUNTIME_INVOCATION OUTPUT_DIR

LOAD REVIEWED_AUTHOR_PARAMETER_SOURCES
RESOLVE AUTHOR_DEFAULT_OR_TUTORIAL_PARAMETERS
PLAN ACTUAL_EXECUTION_PARAMETERS
CLASSIFY PARAMETER_DIFFERENCES AS OUTPUT_AFFECTING OR RUNTIME_ONLY
RETRY WITH AUTHOR_DEFAULT_OR_TUTORIAL_PARAMETERS WHEN OUTPUT_AFFECTING PARAMETER DIFFERENCES ARE NOT REVIEWED
IF OUTPUT_AFFECTING PARAMETER DIFFERENCES REMAIN UNREVIEWED
  RECORD FAILURE_EVIDENCE WITH AUTHOR_PARAMETER_FIDELITY AND FINAL_FAILURE_BOUNDARY
  RETURN REFERENCE_FAIL
END IF

IF COMPATIBILITY_PATCH_IS_NEEDED
  APPLY PATCH ONLY TO STAGE2_OWNED_COPIED_WORKDIR
  ALLOW DEPENDENCY_API LANGUAGE_BRIDGE PATH EXPORT_ONLY MATRIX_ORIENTATION DTYPE SPARSE_DENSE NA_NAN RANDOMNESS_CONTROL COMPATIBILITY PATCHES
  VERIFY PATCH DOES NOT CHANGE SELECTED_PRIMARY_TARGET AUTHOR_WORKFLOW_INPUT ALGORITHM_BRANCH CORE_ALGORITHM_CALL OUTPUT_AFFECTING_PARAMETERS OR LABEL_ALIGNMENT_LOGIC
  VERIFY PREPROCESSING PARAMETERS MATCH AUTHOR_DEFAULT_OR_TUTORIAL_PARAMETERS WHEN PREPROCESSING CODE IS TOUCHED
  RECORD COMPATIBILITY_PATCH_EVIDENCE WITH APPLIED PATCH_SCOPE ALLOWED_PATCH_CLASSES PATCHED_FILES DIFF_PATHS RATIONALE AUTHOR_REPO_MODIFIED_FALSE PREPROCESSING_PARAMETER_CONSISTENCY OUTPUT_AFFECTING_PARAMETER_CHANGED RETRY_LOGS REVIEWED_ACCEPTANCE
  RECORD RUNTIME_ONLY_PRESERVATION_CHECKS FOR SELECTED_PRIMARY_TARGET AUTHOR_WORKFLOW_INPUT ALGORITHM_BRANCH CORE_ALGORITHM_CALL OUTPUT_AFFECTING_PARAMETERS AND LABEL_ALIGNMENT_LOGIC
END IF

CHECK AUTHOR_WORKFLOW_NATIVE_INPUT_LAYOUT AGAINST CANONICAL_INPUT_EVIDENCE AND REVIEWED LOCATORS

IF NATIVE_AUTHOR_WORKFLOW_INPUT_LAYOUT IS INCOMPLETE
  MATERIALIZE ONLY LIGHTWEIGHT AUTHOR_WORKFLOW_REQUIRED INPUT_LAYOUT FILES FROM REVIEWED LOCAL ARTIFACTS OR REVIEWED DOWNLOAD LOCATORS
  RECORD NATIVE_INPUT_LAYOUT_MATERIALIZATION SOURCE_ARTIFACTS ACTIONS MATERIALIZED_PATHS PATH_FORMAT_USABILITY_CHECKS AND CANONICAL_INPUT_CHANGED_FALSE
END IF

IF MATERIALIZATION WOULD REBUILD CANONICAL_INPUT CHANGE SELECTED_CASE CHANGE ANALYSIS_PROBLEM_INPUT OR USE BIOHARNESS_LAYER3_LAYER4_OUTPUT
  RECORD FAILURE_EVIDENCE WITH NATIVE_WORKFLOW_ATTEMPT REQUIRED_TRUE STARTED_FALSE AND FINAL_FAILURE_BOUNDARY
  RETURN REFERENCE_FAIL
END IF

VERIFY NATIVE_INPUT_LAYOUT WORKDIR FULL_RUNTIME_INVOCATION OUTPUT_DIR
RETRY LOCAL PATH WORKDIR OUTPUT_DIR INPUT_LAYOUT PARSER LOADER EXPORT_ONLY ISSUES WITHIN REVIEWED BOUNDARY

RUN ORIGINAL AUTHOR TUTORIAL EXAMPLE VIGNETTE SCRIPT OR NATIVE PACKAGE_API
RECORD ENVIRONMENT_INVOCATION AUTHOR_PARAMETER_FIDELITY COMMAND WORKDIR ENVIRONMENT RETURN_CODE LOGS PRODUCED_ARTIFACTS

IF GPU_TRAINING_RUN_FAILS_WITH_CUDA_OOM
  RECORD GPU_RESOURCE_RETRY_EVIDENCE WITH REQUIRED_TRUE AUTHOR_DEVICE AUTHOR_BATCH_SIZE AUTHOR_EPOCHS OOM_LOG_PATHS GPU_MEMORY_SNAPSHOTS
  DO NOT FALL BACK TO CPU BEFORE GPU_MEMORY_REPAIR_ATTEMPTS WHEN REVIEWED_GPU_IS_AVAILABLE
  PLAN GPU_BATCH_SIZE_RETRY_CANDIDATES FROM AUTHOR_BATCH_SIZE TOWARD SMALLER VALUES
  TRY LARGER_FEASIBLE_GPU_BATCH_SIZE BEFORE SMALLER_GPU_BATCH_SIZE WHEN RESOURCE_EVIDENCE SUPPORTS IT
  RERUN NATIVE_AUTHOR_WORKFLOW_ON_GPU WITH SAME AUTHOR EPOCHS LEARNING_RATE SEED_POLICY MODEL_PARAMETERS PREPROCESSING_PARAMETERS SELECTED_TARGET AND RESULT_FIELD
  RECORD GPU_RESOURCE_RETRY_EVIDENCE WITH RETRY_CANDIDATES RETRY_RESULTS SELECTED_DEVICE SELECTED_BATCH_SIZE SELECTED_BATCH_SIZE_RATIONALE PRESERVED_AUTHOR_PARAMETERS CPU_FALLBACK_ATTEMPTED CPU_FALLBACK_RATIONALE FINAL_GPU_MEMORY_SNAPSHOT STATUS
  IF SELECTED_BATCH_SIZE DIFFERS FROM AUTHOR_BATCH_SIZE
    UPDATE AUTHOR_PARAMETER_FIDELITY ACTUAL_EXECUTION_PARAMETERS PARAMETER_DIFFERENCES OUTPUT_AFFECTING_PARAMETER_CHANGES REVIEWED_ACCEPTANCE_FOR_DIFFERENCES AND FIDELITY_STATUS_REVIEWED_OUTPUT_AFFECTING_ADJUSTED
  END IF
END IF

IF NATIVE_RUN_FAILS DUE TO DEPENDENCY_API LANGUAGE_BRIDGE PATH EXPORT_ONLY MATRIX_ORIENTATION DTYPE SPARSE_DENSE NA_NAN OR RANDOMNESS_CONTROL COMPATIBILITY ISSUE
  CLASSIFY ISSUE AS COMPATIBILITY_PATCH_CANDIDATE
  APPLY PATCH ONLY TO STAGE2_OWNED_COPIED_WORKDIR
  RECORD PRE_PATCH_FAILURE_LOG PATCH_DIFF AND POST_PATCH_RETRY_LOG
  RERUN ORIGINAL AUTHOR TUTORIAL EXAMPLE VIGNETTE SCRIPT OR NATIVE PACKAGE_API WITH SAME AUTHOR OUTPUT_AFFECTING PARAMETERS
END IF

IF RUN IS LONG_RUNNING
  RECORD PID HEARTBEAT REVIEWED_TIMEOUT NO_PROGRESS_THRESHOLD PROGRESS_LOG HOST_RESOURCE_SNAPSHOT TERMINATION_REASON
END IF

IF PRIMARY_REFERENCE_TARGET EXISTS IN GENERATED FILE
  READ OR LOAD GENERATED FILE
  PARSE PRIMARY_REFERENCE_TARGET FIELD
  STANDARDIZE REFERENCE LABELS TO REQUIRED OUTPUT ARTIFACT
  RECORD LOADER PARSER SUMMARY
  RECORD FILES_WRITTEN
  RETURN REFERENCE_READY
END IF

IF PRIMARY_REFERENCE_TARGET EXISTS ONLY IN NATIVE_RUNTIME_OBJECT
  APPLY EXPORT_ONLY WRAPPING INSIDE DISCOVERED EXPORT_ONLY_SCOPE
  RECORD EXPORTED FIELD SLOT KEY OR OBJECT
  STANDARDIZE REFERENCE LABELS TO REQUIRED OUTPUT ARTIFACT
  RECORD LOADER PARSER SUMMARY
  RECORD FILES_WRITTEN
  RETURN REFERENCE_READY
END IF

RETRY SIMPLE LOCAL EXPORT PARSER OUTPUT_PATH ISSUES WITHIN REVIEWED BOUNDARY

IF REFERENCE_READY HAS NOT BEEN PRODUCED
  RECORD FAILURE_EVIDENCE USING REQUIRED FAILURE_EVIDENCE TEMPLATE
  RETURN REFERENCE_FAIL
END IF

END VALIDATION_REFERENCE_PREPARATION
```

## Status Rules

`REFERENCE_READY` requires planning requirement evidence, author target discovery evidence, selected primary target, completed native/static acquisition evidence, materialized reference artifacts, parser or loader summary, and written output records. The primary acquisition provenance must be native/static and `bioharness_surface_used` must be `false`.

`REFERENCE_FAIL` requires complete `failure_evidence`. It is valid only after planning requirement review, author locator inspection, static artifact search/read attempt when applicable, native workflow/API execution attempt or documented preflight failure after allowed lightweight native input layout materialization when static artifacts are absent, export/parser attempt when applicable, and retry evidence for simple local path, output directory, parser, loader, or export-only issues.

When no author-supported primary target can be selected, native/static acquisition is not applicable; `REFERENCE_FAIL` is acceptable only if `failure_evidence.target_discovery_attempt` records inspected locators, author output candidates, rejected candidates, and why none satisfies both the planning requirement and author evidence, with `native_workflow_attempt.required: false`.

`REFERENCE_FAIL` must not mean "native workflow still needs to be run." A method result that stops after target discovery, expected path discovery, command discovery, or repair-target writing is incomplete Stage2 execution and must be rejected by the verifier. Missing small author workflow sidecar or layout files cannot directly justify `REFERENCE_FAIL`; first perform lightweight materialization from reviewed locators or local artifacts, or record why materialization would cross the allowed boundary.

If the observed acquisition route used a BioHarness Layer3/4 callable chain, bridge replay, method harness run, or execution-surface driver to generate primary labels, the result is not `REFERENCE_READY`. Record diagnostic evidence and require native/static acquisition evidence before accepting a method result.
