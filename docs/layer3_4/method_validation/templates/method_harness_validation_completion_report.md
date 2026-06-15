# Method Harness Validation Completion Report

## Required Summary

- included methods
- excluded methods and reason
- consumed canonical validation input evidence
- consumed Stage2 verifier-accepted reference artifact
- consumed surface config path
- surface config load status
- consumed build rows and evidence paths
- consumed environment evidence
- surface invocation status summary
- harness workflow status
- comparison conclusion
- Stage3 stage_handoff_evidence completeness
- selected Layer3 execution evidence status
- real harness result status
- evidence-first comparison judgment
- failures, blockers, and repair routes
- data_input, reference_input, and execution_input consumability
- reviewed conda invocation and GPU resource adjustment evidence when applicable
- shared cell/spot/observation-name comparison evidence when applicable
- verifier candidate result path and package terminal result path when accepted

## Method Result Table

```yaml
method_results:
  - method:
    verifier_verdict:
    method_workflow_terminal_status:
    stage_handoff_evidence:
    stage3_dispatch_decision:
    dispatch_reason:
    dispatch_status:
    surface_config_path:
    surface_config_status:
    surface_invocations:
    candidate_result_path:
    terminal_result_path:
    data_input:
    reference_artifact_source_field:
    reference_input:
    execution_input:
    selected_layer3_surface_chain:
    reviewed_conda_invocation:
    layer3_invocation_evidence:
    gpu_resource_adjustment:
    real_result_observation:
    result_comparison:
      reference_file:
      harness_file:
      shared_name_comparison:
      metric_records:
      judgment:
    failure_class:
    failure_stage:
    reason:
    repair_route:
    files_written:
```
