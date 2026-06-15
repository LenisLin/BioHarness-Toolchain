# Method Harness Validation Outputs

## Verifier Candidate Method Result

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

## Dispatch Or Repair Status

```yaml
method_harness_validation_dispatch_status:
  method:
  dispatch_status: repair_required | blocked_external
  repair_target:
  blocking_reason:
  evidence_needed:
```

## Terminal Result Rule

The method subagent writes `method_harness_validation_candidate_result` for verifier review.

Package-level terminal method validation results consume only verifier-accepted candidate records.

`repair_required` and `blocked_external` are dispatch states. They are recorded outside package-level terminal method results.

Uppercase `REPAIR_REQUIRED` and `BLOCKED_EXTERNAL` are verifier verdicts. Method dispatch/repair records use lowercase `repair_required` and `blocked_external`.

A `candidate_workflow_status: PASS` result means the Stage3 workflow completed and the comparison judgment was written. It does not by itself mean the method was consistent; consistency is recorded in `result_comparison.judgment.conclusion`.

A `TERMINAL_FAIL` candidate may be accepted when selected Layer3 invocation evidence and actual per-surface config evidence exist, allowed non-semantic repairs were attempted where applicable, no comparison-ready harness result was produced, `reason_if_not_produced` is recorded, and the remaining failure is inside method harness validation.

A selected Layer3 chain that was not actually run is not an accepted terminal result. The verifier/package route must send the method task back to selected Layer3 execution with concrete missing invocation evidence; it must not be finalized as a method-level terminal result.
