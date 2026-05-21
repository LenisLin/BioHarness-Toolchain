# Layer3 / Layer4 Build

## Purpose

This file defines Layer3 / Layer4 build for a Gate 2-reviewed `layer4_bridge_planning` item whose assigned step is `layer3_layer4_build`.

Layer3 / Layer4 build may create or modify implementation files. Its main output is a harness-usable build output that describes the Layer3 execution surface, Layer4 backend binding, implementation files, runtime entry, and import experiment for the reviewed method path.

This workflow produces `build_output_result.yaml` as the main output and `build_audit.yaml` as a small boundary audit. It does not run author cases, produce functional validation evidence, or establish final support status.

## Inputs

- Gate 2 human review output with `approved_for_next_step` and `layer3_layer4_build`.
- Gate 1-reviewed parent function / execution surface.
- Method-to-parent Layer4 bridge planning file.
- Gate 1 planning-level alignment route.
- Parent-function standard contract, including canonical input, strict main output, semantic parameters, typed preflight failures, typed output-contract failures, validation expectations, and provenance expectations.
- Backend entrypoints, native input/output shape, mapping notes, and blockers from repository-reading and bridge planning.
- Reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path when relevant.
- Storage/runtime conventions for implementation files, build outputs, import evidence, and evidence paths.

## Build Boundary

Allowed build actions:

- create or modify Layer3 callable binding;
- create or modify Layer4 adapter, wrapper, compatibility rewrite, or algorithmic rewrite implementation within the reviewed route;
- implement object conversion, parameter mapping, output extraction, artifact handling, filesystem policy, environment binding, failure translation, validation hooks, and provenance hooks;
- run bounded import experiments under the reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.

Forbidden build actions:

- change the Gate 1 parent-function boundary;
- change the Gate 1 planning-level alignment route;
- use synthetic, minimal, toy, or BioHarness-created input objects;
- run author cases, tutorials, vignettes, examples, repository fixtures, or validation fixtures;
- download case data, model assets, or validation data;
- run backend method workflows;
- interpret biological outputs;
- claim runtime support, functional correctness, final support status, production readiness, algorithmic equivalence, or biological correctness.

## Output 1: build_output_result.yaml

`build_output_result.yaml` is the main build output. It records the harness-usable result of the Layer3 / Layer4 build.

Use this YAML shape:

```yaml
build_output_result:
  analysis_problem:
  method:
  parent_function:
  gate1_planning_route:

  layer3_execution_surface:
    surface_api:
      name:
      file:
      callable_path:
    input_contract:
    main_output:
    semantic_parameters:
    preflight_failures:
    output_failures:
    validation_expectations:
    provenance_expectations:
    agent_visibility:

  layer4_backend_binding:
    binding_name:
    backend_binding_file:
    backend_entrypoints:
    native_input_output_shape:
    input_conversion:
    parameter_mapping:
    output_extraction:
    artifact_handling:
    filesystem_policy:
    environment_binding:
    failure_translation:
    validation_hooks:
    provenance_hooks:

  implementation_files:
    repo_files:
    changed_files:
    notes:

  runtime_entry:
    environment_ref:
    registration_file:
    import_path:
    runtime_requirements:

  import_experiment:
    run:
    environment_ref:
    result:
    evidence_path:
    failure_route:

  next_evidence_needed:
    environment_build_output:
    author_case_execution:
    bridge_replay:
    validation:

  boundary_checks:
    synthetic_or_minimal_inputs_used: false
    author_case_execution_run: false
    method_workflow_run: false
    data_download_run: false
```

`surface_api` is the built or declared Layer3 callable API for the reviewed parent function. It is not a backend API and must not expose backend-private controls.

`surface_api.file` may point to a NAS draft surface file or to a repo surface file only if a current authority has promoted that file into repo state.

`layer4_backend_binding.backend_binding_file` may point to a BackendAdapterSpec, adapter binding record, or equivalent implementation-facing file.

`runtime_entry.environment_ref` should preferentially point to a reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path. It should not imply that an agent directly reads YAML to decide the environment.

`import_experiment.evidence_path` should point to the NAS evidence path for the import experiment.

## Output 2: build_audit.yaml

`build_audit.yaml` is a small boundary audit. It is not the main build output.

Use this YAML shape:

```yaml
build_audit:
  gate2_review:
  bridge_plan:
  gate1_surface:
  environment_ref:

  reviewed_build_scope:
    method:
    parent_function:
    gate1_planning_route:

  boundary_checks:
    gate1_parent_function_changed: false
    gate1_planning_route_changed: false
    synthetic_or_minimal_inputs_used: false
    author_case_execution_run: false
    method_workflow_run: false
    data_download_run: false

  import_experiment:
    run:
    result:
    evidence_path:
    failure_route:

  build_output_result:
  implementation_files:
  non_claims:
  next_evidence_needed:
```

## Import Experiment Boundary

Import experiments are allowed only under the reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.

Allowed import experiments may import the BioHarness implementation module, callable registration path, adapter or wrapper registration path, or backend import through the adapter.

Import experiments must not construct input objects, run backend method workflows, run author cases, download data, replace reviewed environment build execution/output, or establish functional correctness.

If import fails because of dependency, runtime, or package-load behavior, route the issue to reviewed environment build output review or environment planning repair.

If import fails because of adapter module path, registration, or BioHarness wrapper code, route the issue to build repair.

If import failure exposes a parent-function boundary or Gate 1 planning-route issue, route the issue to `return_to_gate1`.

## Evidence Boundary

Layer3 / Layer4 build output can support later harness or runtime loading and later BioHarness bridge replay.

Layer3 / Layer4 build output does not establish native author-case success, BioHarness bridge replay success, runtime support, functional correctness, final support status, production readiness, algorithmic equivalence, or biological correctness.

## Non-Claims

Layer3 / Layer4 build does not replace reviewed environment build execution or reviewed environment build output.

Layer3 / Layer4 build does not replace author-case/native workflow execution.

Layer3 / Layer4 build does not replace post-implementation validation.

`build_audit.yaml` is a small boundary audit. It is not the main build output.
