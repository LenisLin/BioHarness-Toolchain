# Method Harness Validation

## Purpose

Run the reviewed BioHarness Layer3 callable chain for one method and check whether the observed result satisfies the selected parent-function contract.

## Preconditions

- Canonical validation input is available.
- Stage2 verifier-accepted reference artifact is available.
- Minimal comparison cues are available when already reviewed or planned; absence of optional cues must not prevent running the selected Layer3 surface when required data, reference, execution, and environment inputs are available.
- Reviewed environment evidence is available.
- Selected Layer3 execution surface rows are downstream-selectable.
- A generated `method_harness_validation_surface_config.yaml` is available for the selected surface chain.
- The reviewed invocation is recorded.

## Required Output

Verifier candidate result:

```yaml
method_harness_validation_candidate_result:
  method:
  stage_handoff_evidence:
    instantiated_method_prompt:
    stage1_input_preparation_result:
    canonical_input_path:
    stage2_reference_preparation_result:
    reference_artifact_path:
    reference_artifact_source_field:
    surface_config_path:
    selected_layer3_surface_chain_evidence:
    reviewed_environment_evidence:
  candidate_workflow_status: PASS | TERMINAL_FAIL
  data_input:
    canonical_input_path:
    load_result:
    required_fields:
  reference_input:
    reference_artifact_path:
    reference_artifact_source_field:
    reference_type: subset | static | native_rerun | native_rerun_with_patch | generated_native
    load_result:
    id_field:
    result_field:
  execution_input:
    selected_layer3_surface_chain:
    selected_layer3_contracts:
    reviewed_build_evidence:
    reviewed_environment_evidence:
    conda_invocation:
    gpu_execution_policy:
    surface_config_path:
    surface_config_load_result:
    comparison_cues:
  harness_execution:
    interface_preparation:
      status: pass | repaired | failed
      attempts:
    surface_invocations:
      - surface:
        callable_or_command:
        config:
        status: pass | failed | skipped
        output_artifact:
        reason:
        environment:
        workdir:
        logs:
        return_code:
    real_result_observation:
      produced: true | false
      reason_if_not_produced:
      attempted_repairs:
      raw_artifact:
      comparison_ready_artifact:
      id_field:
      result_field:
      output_level:
      row_count:
      missing_result_count:
  result_comparison:
    required_when: candidate_workflow_status == PASS
    not_applicable_reason:
    evidence:
      reference_file:
      reference_load_result:
      harness_file:
      harness_load_result:
      shared_name_comparison:
        shared_id_field:
        reference_count:
        harness_count:
        shared_count:
        reference_only_count:
        harness_only_count:
      metric_records:
        - formula_or_function:
          package:
          version:
          call_signature:
          input_vectors:
          preprocessing:
          value:
          reason_when_not_computed:
    judgment:
      conclusion: consistent | inconsistent
      reason:
      uncertainty_or_limits:
  failure_class:
  failure_stage:
  reason:
  runtime_monitoring_summary:
  files_written:
```

Dispatch or repair status:

```yaml
method_harness_validation_dispatch_status:
  method:
  dispatch_status: repair_required | blocked_external
  repair_target:
  blocking_reason:
  evidence_needed:
```

## Workflow

```text
BEGIN METHOD_HARNESS_VALIDATION

LOAD data_input, reference_input, execution_input, comparison_cues, and method_harness_surface_config.

VERIFY canonical input and Stage2 reference artifact are readable.
VERIFY selected Layer3 chain, reviewed build evidence, and reviewed conda environment are available.
READ the generated surface config YAML from `method_harness_surface_config.surface_config_path` and confirm it matches `stage_handoff_evidence.surface_config_path` and `execution_input.surface_config_path`.
RECORD `execution_input.surface_config_load_result`.
VERIFY `execution_input.surface_config_load_result` is readable before invocation.

RUN only the selected Layer3 execution surface chain from canonical input.
For each selected surface, pass `surface_config.<surface>` as the callable `config`.
Record the actual config used in `surface_invocations`.
Use the reviewed conda invocation.
For GPU-required methods, use the reviewed GPU route. Do not switch to CPU as first recovery. If resource failure occurs, first apply allowed resource adjustments recorded by the surface contract, such as batch size, and record evidence.

Do not write a terminal method result unless selected Layer3 invocation evidence exists.
If no invocation evidence exists, the verifier/package route returns the task to execution.

If a simple path, loader, parser, output-root, field-alias, or serialization failure occurs and does not change execution surface semantics, repair once within policy and record the attempt.

IF selected Layer3 invocation evidence exists, allowed repairs were attempted, no comparison-ready harness result was produced, and the remaining failure is inside method harness validation:
  WRITE evidence-first candidate terminal_fail with reason_if_not_produced and failure evidence.
  SET result_comparison.not_applicable_reason because no comparison-ready harness result exists.
  SKIP comparison judgment.
  RETURN candidate for verifier review.

LOAD reference and harness outputs.
COMPARE records by shared cell/spot/observation names when such names are the comparable unit.

IF shared cell/spot/observation names are expected and shared_count == 0:
  TREAT this as an execution/file-selection check before metric computation.
  RECHECK canonical input, Stage2 reference artifact, harness output artifact, id_field, and result_field.
  IF a simple artifact or field selection issue is found:
    REPAIR within policy and reload.
  ELSE:
    DO NOT compute agreement metrics.
    RETURN the appropriate verifier repair route or candidate TERMINAL_FAIL using existing execution/failure fields.
  END IF
END IF

WRITE evidence first: reference file, harness file, shared-name counts, metric records.
WRITE judgment second: consistent or inconsistent, with reason.
WRITE candidate result for verifier review.

END METHOD_HARNESS_VALIDATION
```
