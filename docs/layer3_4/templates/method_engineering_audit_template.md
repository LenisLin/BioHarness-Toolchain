# MethodEngineeringAudit Template

This is a lightweight engineering audit template. It is not an implementation claim, not a runtime layer, and not agent-facing by default.

For current full Layer 3/4 method planning, prefer `method_execution_planning_record_template.md`, which points to `MethodExecutionPlanningRecord v0.7.1`. This file remains a compact inspection note template.

Fill it after Layer 2 method selection for a promoted method. A completed audit should produce separate Layer 3 and Layer 4 artifacts: an `ExecutionSurfaceSpec` for the functional surface and a `BackendAdapterSpec` for the backend binding. It may also record a `RewriteDecision`, `EnvironmentProfile` assignment, and validation/fidelity requirements.

```yaml
method_id:
task_family:
layer2_role:
  -
repository:
  url:
  commit_or_release:
  code_available:
  license:
  last_checked:
engineering_audit:
  evidence_resolution:
    level: file_level | symbol_level | line_level | runtime_observed
    implementation_ready: true | false
  install_files:
    -
  environment_files:
    -
  example_entrypoints:
    - notebook
    - script
    - python_api
    - r_function
    - cli
  main_modules:
    -
  main_functions:
    -
  input_objects:
    - AnnData
    - SpatialData
    - Seurat
    - SpatialExperiment
    - matrix
    - coordinates
    - image
  output_objects:
    - labels
    - embeddings
    - plots
    - intermediate_files
layer3_surface_draft:
  functional_surfaces:
    - input_check
    - method_preprocessing
    - core_structure_building
    - model_fit_or_inference
    - output_assignment
    - artifact_export
    - final_validation
    - visualization
  semantic_inputs:
    -
  semantic_parameters:
    -
  semantic_outputs:
    -
  preflight_checks:
    -
  postrun_checks:
    -
  failure_modes:
    -
layer4_binding_draft:
  entrypoint:
  evidence_resolution:
    level: file_level | symbol_level | line_level | runtime_observed
    implementation_ready: true | false
  function_surface_bindings:
    - layer3_stage:
      binding_status: backend_bound | wrapper_added | not_applicable | requires_followup
      backend_files_or_functions:
      adapter_responsibility:
      evidence_refs:
      implementation_blocker:
  function_bindings:
  parameter_mapping:
  input_conversion:
  output_mapping:
  artifact_mapping:
  failure_translation:
environment:
  expected_capsule:
  dependency_risk:
  gpu_policy:
  cpu_fallback_policy:
rewrite_decision:
  class:
  rationale:
  interface_rewrite_needed:
  algorithmic_rewrite_needed:
  blocking_issues:
  fidelity_check_needed:
promotion_status:
  - enter_layer3_surface
  - enter_layer4_adapter_design
  - hold
notes:
```
