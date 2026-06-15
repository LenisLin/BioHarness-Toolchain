# Method Validation Workflow

## Purpose

This file defines package-level orchestration for method-level validation.

Method validation runs in three gated stages. Each stage dispatches one method subagent per eligible method and records verifier acceptance before the next stage consumes its evidence.

## Stage Order

1. `validation_input_preparation`
2. `validation_reference_preparation`
3. `method_harness_validation`

## Stage 1: Validation Input Preparation

Dispatch one input-preparation subagent per included method, in batches of at most 6 methods.

Stage 1 consumes downstream-selectable build evidence for `prepare_spatial_domain_input`. The input-preparation subagent uses that public contract to prepare canonical AnnData and records a readiness check for that surface. Stage 1 does not run later execution surfaces. Missing, stale, or non-downstream-selectable first-surface build evidence is an `INPUT_REPAIR_REQUIRED` state.

Stage 1 records source-route completion before accepting input-preparation states: local check, reviewed download/localization or package route, portal artifact selection when applicable, unpack/extract when applicable, path/format/usability checks, and canonical input attempt.

A method may enter Stage 2 only when the input-preparation verifier accepts `INPUT_READY`.

Accepted Stage 1 states:

- `INPUT_READY`
- `INPUT_REPAIR_REQUIRED`
- `BLOCKED_EXTERNAL`

## Stage 2: Validation Reference Preparation

The main implementation window runs Stage 2 package orchestration. It instantiates one `validation_reference_preparation_method_prompt.md` prompt per eligible method and calls method-level subagents in batches of at most 6 methods.

```text
BEGIN VALIDATION_REFERENCE_PREPARATION_PACKAGE_ORCHESTRATION

LOAD STAGE1_PACKAGE_DISPATCH_RECORD
LOAD EACH METHOD VALIDATION_INPUT_PREPARATION_RESULT

FOR EACH METHOD
  IF PACKAGE_STAGE1_RECORD AND METHOD_STAGE1_RESULT DISAGREE
    RECORD STAGE2 DISPATCH EXCLUSION REASON
    EXCLUDE METHOD FROM STAGE2
  ELSE IF METHOD_STAGE1_RESULT ACCEPTED_STATUS IS NOT INPUT_READY
    RECORD STAGE2 DISPATCH EXCLUSION REASON
    EXCLUDE METHOD FROM STAGE2
  ELSE IF METHOD_STAGE1_RESULT CANONICAL_INPUT_STATUS IS NOT AVAILABLE
    RECORD STAGE2 DISPATCH EXCLUSION REASON
    EXCLUDE METHOD FROM STAGE2
  ELSE IF METHOD_STAGE1_RESULT CANONICAL_INPUT_RECORD.PATH DOES NOT EXIST
    RECORD STAGE2 DISPATCH EXCLUSION REASON
    EXCLUDE METHOD FROM STAGE2
  ELSE
    ADD METHOD TO ELIGIBLE_METHODS
  END IF
END FOR

FOR EACH ELIGIBLE_METHOD
  INSTANTIATE VALIDATION_REFERENCE_PREPARATION_METHOD_PROMPT FROM TEMPLATE
  FILL METHOD_OUTPUT_ROOT OWNED_PATHS READ_ONLY_STAGE1_RESULT CANONICAL_INPUT_PATH SOURCE_REPOSITORY_PATH EXECUTION_ENVIRONMENT ROUTE_CONTAMINATION_POLICY RETURN_EVIDENCE AND STOP_CONDITION
  DO NOT PREFILL SELECTED_PRIMARY_TARGET FIELD SLOT COMMAND OR EXAMPLE_SPECIFIC METHOD OUTPUT
  RECORD INSTANTIATED_METHOD_PROMPT PATH
END FOR

PARTITION ELIGIBLE_METHODS INTO BATCHES OF AT MOST 6 METHODS

FOR EACH BATCH
  CALL METHOD SUBAGENTS FOR THE CURRENT BATCH
  WAIT FOR METHOD RESULTS FOR THE CURRENT BATCH
  RUN VALIDATION_REFERENCE_PREPARATION_COMPLETION_VERIFIER FOR THE CURRENT BATCH
  UPDATE PACKAGE DISPATCH RECORD WITH METHOD RESULT PATHS VERIFIER RESULT PATHS AND ACCEPTED STATUSES
END FOR

WRITE FINAL PACKAGE DISPATCH RECORD
ROUTE ONLY REFERENCE_READY METHODS TO STAGE3
RECORD REFERENCE_FAIL METHODS AS STAGE2-COMPLETED NON-STAGE3 METHODS

END VALIDATION_REFERENCE_PREPARATION_PACKAGE_ORCHESTRATION
```

Stage 2 consumes the Gate-2-reviewed analysis-problem reference expectation, author workflow/data locators, canonical validation input evidence supplied by the instantiated method prompt, and reviewed output root. Stage 2 is the first stage that inspects method-specific tutorial, example, vignette, or source content to discover the concrete reference target.

Stage 2 discovers the author-defined target and acquires native/static reference evidence. It must not run the selected Layer3 callable chain, Layer4 wrapper path, bridge replay, or method harness route as reference acquisition.

A method has completed Stage 2 when the reference-preparation verifier accepts `REFERENCE_READY` or `REFERENCE_FAIL`.

Accepted Stage 2 method states:

- `REFERENCE_READY`
- `REFERENCE_FAIL`

`REFERENCE_FAIL` is an executed Stage2 failure with complete `failure_evidence`; it is not a repair-target placeholder.

## Stage 3: Method Harness Validation

Dispatch one harness-validation subagent per method accepted as `INPUT_READY` and `REFERENCE_READY`, in batches of at most 6 methods.

Stage 3 consumes Stage1 verifier-accepted canonical input, Stage2 verifier-accepted reference artifacts, per-method `layer3_method_config.yaml`, the selected Layer3 execution surface chain and contracts, reviewed build/environment evidence, and minimal `comparison_cues`. Stage2 `author_parameter_fidelity.actual_execution_parameters` remains the source evidence for recorded author/native parameter values. Stage 3 generates one `method_harness_validation_surface_config.yaml` by resolving selected Layer3-M exposed variables against Stage2 recorded parameter evidence before method harness subagent dispatch. The generated `surface_config` includes only selected Layer3 execution surfaces for the Stage3 run; empty `{}` is valid for selected surfaces with no additional Layer3-M config. Stage 3 must run only the selected Layer3 execution surface chain from canonical input before writing a verifier candidate result.

For each selected-surface Layer3-M exposed variable, Stage3 performs exposed-variable source resolution: inspect Stage2 `actual_execution_parameters`, `author_default_or_tutorial_parameters`, native command or loader-call evidence, and generation-route evidence for matching values. Apply exact-name matching and documented native-name normalization before leaving a selected exposed variable absent. For input-mapping selector variables, Stage3 may resolve values from canonical input schema only when Stage2 evidence shows that the native reference used the same input structure.

Image alignment metadata is consumed from Stage1 canonical input evidence and Layer3/4 build evidence. Stage3 config generation resolves only selected Layer3-M exposed variables such as `library_id`, `img_key`, or `img_size`. Scalefactors, physical-to-pixel transforms, and patch-frame conversion rules are not treated as ordinary Layer3-M exposed variables unless explicitly reviewed as method-facing selectors.

This source-resolution step is limited to selected Layer3-M exposed variables. It is not a full parameter audit and does not require reporting unmapped Stage2 parameters.

Stage 3 records `data_input`, `reference_input`, `execution_input`, actual selected Layer3 invocation evidence, real result observation, bounded non-semantic repair attempts when needed, and an evidence-first comparison record. A comparison judgment is written only after reference and harness outputs have both been loaded and compared.

```text
BEGIN METHOD_HARNESS_VALIDATION_PACKAGE_ORCHESTRATION

LOAD STAGE1_PACKAGE_DISPATCH_RECORD
LOAD STAGE2_PACKAGE_DISPATCH_RECORD
LOAD EACH METHOD VALIDATION_INPUT_PREPARATION_RESULT
LOAD EACH METHOD VALIDATION_REFERENCE_PREPARATION_RESULT
LOAD SELECTED LAYER3 SURFACE, BUILD, AND ENVIRONMENT EVIDENCE
LOAD EACH METHOD LAYER3_METHOD_CONFIG

FOR EACH STAGE2 REFERENCE_READY METHOD
  SET REFERENCE_ARTIFACT_PATH FROM reference_artifacts.primary.standardized_artifact WHEN PRESENT
  ELSE SET REFERENCE_ARTIFACT_PATH FROM reference_artifacts.primary.raw_artifact WHEN PRESENT
  RECORD reference_artifact_source_field
END FOR

FOR EACH METHOD
  IF STAGE1 RESULT IS NOT INPUT_READY
    SET stage3_dispatch_decision TO excluded
    SET dispatch_reason TO Stage1 result is not INPUT_READY
    EXCLUDE METHOD FROM STAGE3
  ELSE IF STAGE2 RESULT IS NOT REFERENCE_READY
    SET stage3_dispatch_decision TO excluded
    SET dispatch_reason TO Stage2 result is not REFERENCE_READY
    EXCLUDE METHOD FROM STAGE3
  ELSE IF CANONICAL_INPUT_PATH DOES NOT EXIST
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO canonical input path does not exist after Stage1 handoff
    EXCLUDE METHOD FROM STAGE3
  ELSE IF REFERENCE_ARTIFACT_PATH DOES NOT EXIST
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO extracted Stage2 reference_artifact_path does not exist
    EXCLUDE METHOD FROM STAGE3
  ELSE IF SELECTED LAYER3 SURFACE OR REVIEWED ENVIRONMENT EVIDENCE IS MISSING
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO missing selected Layer3 or reviewed environment evidence
    EXCLUDE METHOD FROM CURRENT DISPATCH
  ELSE IF LAYER3_METHOD_CONFIG IS MISSING OR UNREADABLE
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO layer3_method_config.yaml is missing or unreadable
    EXCLUDE METHOD FROM CURRENT DISPATCH
  ELSE
    SET stage3_dispatch_decision TO eligible
    SET dispatch_reason TO Stage1 input, Stage2 reference artifact, selected Layer3 surface, Layer3-M config, and reviewed environment evidence are available
    ADD METHOD TO ELIGIBLE_METHODS
  END IF
END FOR

FOR EACH ELIGIBLE_METHOD
  FOR EACH SELECTED SURFACE IN SELECTED_LAYER3_CALLABLE_CHAIN
    FOR EACH EXPOSED VARIABLE IN LAYER3_METHOD_CONFIG.execution_surfaces[SELECTED SURFACE].variables
      RESOLVE VALUE FROM Stage2 actual parameters, author/tutorial parameters, native command or loader-call evidence, or generation-route evidence
      APPLY EXACT-NAME AND DOCUMENTED NATIVE-NAME NORMALIZATION BEFORE LEAVING THE VARIABLE ABSENT
      IF VARIABLE IS AN INPUT-MAPPING SELECTOR
        RESOLVE FROM CANONICAL INPUT SCHEMA ONLY WHEN STAGE2 EVIDENCE SUPPORTS THE SAME INPUT STRUCTURE
      END IF
      WRITE RESOLVED VALUE INTO surface_config[SELECTED SURFACE] WHEN RESOLVED
    END FOR
  END FOR
  GENERATE method_harness_validation_surface_config.yaml FROM THE RESOLVED SELECTED-SURFACE CONFIG
  IF METHOD_HARNESS_VALIDATION_SURFACE_CONFIG CANNOT BE GENERATED
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO method_harness_validation_surface_config.yaml generation failed before method harness dispatch
    SET surface_config_status TO generation_failed
    EXCLUDE METHOD FROM CURRENT DISPATCH
    CONTINUE TO NEXT METHOD
  END IF
  SET SURFACE_CONFIG_PATH TO generated method_harness_validation_surface_config.yaml path
  IF SURFACE_CONFIG_PATH DOES NOT EXIST
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO generated method_harness_validation_surface_config.yaml is missing
    SET surface_config_status TO missing
    EXCLUDE METHOD FROM CURRENT DISPATCH
    CONTINUE TO NEXT METHOD
  ELSE IF SURFACE_CONFIG_PATH IS NOT READABLE
    SET stage3_dispatch_decision TO repair_route
    SET dispatch_reason TO generated method_harness_validation_surface_config.yaml is unreadable
    SET surface_config_status TO unreadable
    EXCLUDE METHOD FROM CURRENT DISPATCH
    CONTINUE TO NEXT METHOD
  ELSE
    SET surface_config_status TO generated
  END IF
  INSTANTIATE METHOD_HARNESS_VALIDATION_PROMPT FROM TEMPLATE
  FILL METHOD_OUTPUT_ROOT, OWNED_PATHS, READ_ONLY_INPUTS, STAGE_HANDOFF_EVIDENCE.surface_config_path, CANONICAL_VALIDATION_INPUT, REFERENCE_EVIDENCE, COMPARISON_CUES, BUILD_EVIDENCE, REVIEWED_CONDA_ENVIRONMENT, SELECTED_LAYER3_CALLABLE_CHAIN, SELECTED_LAYER3_SURFACE_CONTRACTS, METHOD_HARNESS_SURFACE_CONFIG, RETURN_EVIDENCE, AND STOP_CONDITION
  RECORD INSTANTIATED_METHOD_PROMPT PATH
END FOR

PARTITION ELIGIBLE_METHODS INTO BATCHES OF AT MOST 6 METHODS

FOR EACH BATCH
  CALL METHOD SUBAGENTS FOR THE CURRENT BATCH
  WAIT FOR CANDIDATE RESULTS FOR THE CURRENT BATCH
  RUN METHOD_HARNESS_VALIDATION_COMPLETION_VERIFIER FOR THE CURRENT BATCH
  UPDATE PACKAGE DISPATCH RECORD WITH CANDIDATE_RESULT_PATHS, VERIFIER_RESULT_PATHS, VERIFIER_VERDICT, METHOD_WORKFLOW_TERMINAL_STATUS, DISPATCH_STATUS, TERMINAL_RESULT_PATHS, AND REPAIR_TARGETS
END FOR

WRITE PACKAGE TERMINAL RESULTS ONLY FROM VERIFIER-ACCEPTED CANDIDATE RESULTS
END METHOD_HARNESS_VALIDATION_PACKAGE_ORCHESTRATION
```

Terminal package results consume only verifier-accepted harness validation results.

Stage 3 state fields:

- `verifier_verdict`: `PASS | REPAIR_REQUIRED | BLOCKED_EXTERNAL`
- `method_workflow_terminal_status`: `PASS | TERMINAL_FAIL`
- `dispatch_status`: `repair_required | blocked_external`

`dispatch_status` uses lowercase values because it is a method dispatch/repair record, not a verifier verdict.

Consistency or inconsistency is recorded only in `result_comparison.judgment.conclusion`; no `PASS` field represents the comparison conclusion.

## Package Dispatch Record

```yaml
method_validation_dispatch_log:
  invocation_id:
  stages:
    - stage: validation_input_preparation
      subagent_prompt_template: docs/layer3_4/method_validation/templates/validation_input_preparation_method_prompt.md
      verifier_prompt_template: docs/layer3_4/method_validation/templates/validation_input_preparation_completion_verifier_prompt.md
      max_active_method_subagents: 6
      methods:
        - method:
          method_output_root:
          subagent_status:
          verifier_status:
          accepted_status:
          input_preparation_result:
          first_execution_surface_evidence:
          first_execution_surface_status:
          repair_target:
    - stage: validation_reference_preparation
      subagent_prompt_template: docs/layer3_4/method_validation/templates/validation_reference_preparation_method_prompt.md
      verifier_prompt_template: docs/layer3_4/method_validation/templates/validation_reference_preparation_completion_verifier_prompt.md
      max_active_method_subagents: 6
      methods:
        - method:
          method_output_root:
          instantiated_method_prompt:
          stage1_input_preparation_result:
          canonical_input_path:
          validation_reference_preparation_result:
          verifier_result:
          subagent_status:
          verifier_status:
          accepted_status:
    - stage: method_harness_validation
      subagent_prompt_template: docs/layer3_4/method_validation/templates/method_harness_validation_prompt.md
      verifier_prompt_template: docs/layer3_4/method_validation/templates/method_harness_validation_completion_verifier_prompt.md
      max_active_method_subagents: 6
      methods:
        - method:
          method_output_root:
          stage3_dispatch_decision: eligible | excluded | repair_route | blocked_external
          dispatch_reason:
          instantiated_method_prompt:
          stage1_input_preparation_result:
          canonical_input_path:
          stage2_reference_preparation_result:
          reference_artifact_path:
          reference_artifact_source_field:
          layer3_method_config:
          surface_config_path:
          surface_config_status: generated | missing | unreadable | generation_failed
          selected_layer3_surface_chain_evidence:
          reviewed_environment_evidence:
          comparison_cues:
          candidate_result_path:
          verifier_result:
          subagent_status:
          verifier_verdict:
          method_workflow_terminal_status:
          dispatch_status:
          terminal_result_path:
          repair_target:
  package_terminal_results_written: true | false
```

## Package Completion Rule

Package-level terminal method results are written after Stage 3 verifier acceptance.

Incomplete Stage 2 preparation remains verifier repair evidence and is not an accepted method result. Accepted Stage 2 method results are only `REFERENCE_READY` or `REFERENCE_FAIL`.
