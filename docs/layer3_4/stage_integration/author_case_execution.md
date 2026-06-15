# Author Case Execution

## Purpose

This file defines author-case/native workflow execution and BioHarness bridge replay for a Gate 2-reviewed functional testing planning item whose assigned step is `author_case_native_workflow_and_bridge_replay`.

Author case execution observes whether a selected documented method path can run under the reviewed execution boundary and produce inspectable outputs, artifacts, and logs.

## Inputs

- Gate 2-reviewed functional testing planning item with assigned step `author_case_native_workflow_and_bridge_replay`.
- Functional testing planning file.
- Reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path referenced by the Gate 2 human review table for this author-case run.
- Root-level `layer3_layer4_build_completion_matrix.tsv` from `layer3_layer4_build.md` when BioHarness bridge replay is planned.
- `build_output_result.yaml` from `layer3_layer4_build.md` only for rows whose completion matrix entry has `downstream_selectable=true`.
- `build_audit.yaml` as boundary evidence for the same downstream-selectable row when relevant.
- Implemented Layer3 callable / Layer4 backend binding from downstream-selectable Layer3 / Layer4 build evidence when BioHarness bridge replay is planned.
- Original repository case, tutorial, vignette, or example locators.
- Data and artifact origin locators.
- Expected output form and output-contract expectations.
- Storage/runtime conventions for logs, outputs, and evidence records.

Author-case execution uses the reviewed environment binding/build output as an engineering input. It must not re-infer dependency boundaries, environment branch, conda prefix, method routing, or Layer3 / Layer4 build selectability. Missing or insufficient environment binding/build output routes back to the relevant environment planning/build review path.

## Template Index

Method validation templates live under `docs/layer3_4/method_validation/templates/`. This file records author-case and reference execution context used by method validation.

## Execution Orchestration

Author-case/native workflow execution is organized by method. The main executor reads the reviewed validation-scope table and prepares one `method_handoff` for each included method.

Use this handoff template:

```yaml
method_handoff:
  method:
  selected_surfaces:
  build_evidence:
  environment_evidence:
  execution_environment:
    conda_prefix:
    python_invocation: conda run -p <conda_prefix> python
    r_invocation: conda run -p <conda_prefix> Rscript
    embedded_r_required: yes | no
    expected_r_home: <conda_prefix>/lib/R
  case_data:
    local_locator:
    remote_locator:
    remote_locator_type: direct_download | portal_or_index | package_data_route | not_applicable
    required_payload:
    helper_packages_for_data_access:
    data_target_dir:
    localization_status: pending | available | unavailable
    format_check:
    usability_check:
  author_workflow:
    local_locator:
    remote_locator:
    local_saved_path:
    workflow_usability_check:
    allowed_adjustment_scope: path | workdir | input_path | output_path | cache_path
    core_workflow_status: original_workflow_preserved
  reference_discovery_seed:
    analysis_problem_reference_expectation:
    candidate_author_locators:
    reference_output_root:
    reference_environment_mode: bioharness_build_environment | temporary_method_environment
  execution_surface_entrypoints:
  output_root:
  workdir:
  data_target_dir:
  parameter_policy: follow_author_tutorial_else_default
  seed_policy: use_619_when_seed_is_exposed
  runtime_monitoring:
    required: yes | no
    progress_unit: epoch | iteration | step | command_phase | not_applicable
    heartbeat_interval:
    reviewed_timeout:
    no_progress_threshold:
```

The handoff fixes execution boundary and discovery inputs, not the concrete method-specific reference target. The method executor uses the execution environment, case data record, author workflow record, reference discovery seed, output root, workdir, and data target recorded in the handoff for Stage 2 target discovery and native/static acquisition.

`selected_surfaces`, `build_evidence`, and `execution_surface_entrypoints` are Stage 3 or bridge replay context. The Stage 2 executor must not consume `execution_surface_entrypoints` to produce the primary reference.

`reference_discovery_seed` is reviewed by Gate 2 as an execution seed only. It records expected reference mode and locator classes for Stage 2 target discovery and native/static acquisition, not concrete method-specific targets.

`case_data.local_locator` records a local source path or reviewed local target. Case data are executable only after `localization_status`, path existence, format check, and usability check are recorded as available for the selected method input.

### Case Data Localization Workflow Template

Use this template to record case data localization evidence:

```yaml
case_data_localization_evidence:
  method:
  required_payload:
  reviewed_local_target:
  initial_local_status: available | pending | unavailable
  remote_locator:
  remote_locator_type: direct_download | portal_or_index | package_data_route | not_applicable
  resolved_artifacts:
  helper_packages_for_data_access:
  localization_action:
  localized_path:
  path_existence_check: pass | fail
  format_check: pass | fail
  usability_check: pass | fail
  final_localization_status: available | unavailable
  evidence_files:
  notes:
```

Case data localization proceeds in this order:

1. Confirm `case_data` fields: required payload, reviewed local target, remote locator, remote locator type, data target, and helper package field when applicable.
2. Check the reviewed local target and record `initial_local_status`.
3. When the local target is not available and `remote_locator_type` is not `not_applicable`, perform remote localization from the reviewed locator.
4. For `direct_download`, download or locate the reviewed file or archive.
5. For `portal_or_index`, resolve the reviewed page to method-required downloadable artifacts.
6. For `package_data_route`, use the named helper package for data access.
7. Write localized artifacts under the reviewed method `data_target_dir` or link them there.
8. Apply path existence, format, and usability checks to the localized artifacts.
9. Record `final_localization_status: available` only after all three checks pass.

The execution environment records the reviewed conda prefix and the command form used to enter that prefix. Python commands should use `conda run -p <conda_prefix> python` or an equivalent reviewed invocation that resolves the same prefix. R commands should use `conda run -p <conda_prefix> Rscript` or an equivalent reviewed invocation that resolves the same prefix.

For adapter and wrapper routes, the reviewed BioHarness build environment may be reused only as a runtime environment for a compatible native author workflow.

Environment reuse does not authorize BioHarness Layer3/Layer4 callable chains as reference generation.

The native reference command must point to an original repository workflow, script, vignette, example, or native package/API path matching the author workflow.

For algorithmic rewrite routes, native reference generation may use one method-scoped temporary conda environment. The temporary environment is used only to run the original tutorial or workflow and generate the native reference output. The generated reference output, logs, and environment summary are retained under the reviewed output root. The temporary environment is deleted after reference capture and is not recorded as a BioHarness runtime environment.

Author-case preparation proceeds in this order:

1. Resolve and localize case data using the Case Data Localization Workflow Template.
2. Check and localize the author workflow reference when a local workflow is not already available.
3. Inspect workflow, example, vignette, or source evidence to discover the primary reference target and acquisition route.
4. Acquire static reference if available, otherwise generate from the native author workflow when required.
5. Record command, environment, log, artifact, parser evidence, and provenance class.
6. Complete native/static reference acquisition before bridge replay.
7. Treat bridge replay output as the comparison target, not as the Stage 2 reference.
8. Hand canonical input and reference-preparation evidence to `docs/layer3_4/method_validation/method_harness_validation.md`.

Author-case preparation records preparation and native-observation evidence. It does not write terminal method validation results.

Terminal method validation results are defined by `docs/layer3_4/method_validation/method_harness_validation.md` and are written only after method-harness-validation verifier acceptance.

Input-preparation gaps record repair states under the input-preparation workflow. Stage2 reference-preparation gaps must continue execution or verifier repair until they produce `REFERENCE_READY` or `REFERENCE_FAIL` with complete `failure_evidence`.

Method harness validation records terminal failure classes only inside `docs/layer3_4/method_validation/method_harness_validation.md`.

Environment preflight consumes reviewed environment evidence. Environment package repair, package-level isolation, dependency-family diagnosis, and new backend-load-target selection belong to environment build or repair workflows.

For Python execution surfaces that enter R through `rpy2`, the execution preflight records the embedded-R startup result under the reviewed invocation. The preflight should confirm the observed `R_HOME`, observed R version, `import rpy2.robjects`, base package loading for `utils` and `stats`, and method package loading when the method uses an R package through the Python bridge.

For R-backed Python surfaces, the method execution record captures bridge API compatibility observed along the selected source call path when rpy2 conversion, object conversion, or R package helper APIs are used.

Use this preflight template when `embedded_r_required: yes`:

```yaml
embedded_r_preflight:
  invocation:
  expected_r_home:
  observed_r_home:
  observed_r_version:
  import_rpy2_robjects: pass | fail
  load_base_packages: pass | fail
  method_package_load: pass | fail | not_applicable
  status: pass | fail
```

A failed embedded-R preflight is recorded as `environment_failure` and routed to environment repair.

When native reference output differs from the selected or discovered reference target or expected result class, record the observed difference as diagnostic or failure evidence. Treat it as reference evidence only after explicit re-review confirms that the observed output is the correct target for the planning requirement.

## Native Author Case Execution

Native author case execution runs the original documented workflow as closely as possible under the reviewed execution boundary and reviewed environment build output. It records observed outputs, logs, warnings/errors, runtime, memory, and artifacts.

This is native method evidence. It is not BioHarness parent-function support unless the BioHarness bridge path is also tested.

| Method | Case / Tutorial / Vignette | Execution Mode | Covered Parent Function(s) | Data Source | Artifact Origin | Author Commands / Workflow | Expected Author Outputs | Observed Outputs | Runtime Metrics | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allowed execution modes:

- `native_author_case_execution`
- `bioharness_bridge_replay_from_author_case`

Both execution modes must use original repository cases or direct tutorial, vignette, or example material.

Allowed status values:

- `planned`
- `blocked_by_data`
- `blocked_by_environment`
- `blocked_by_missing_instructions`
- `ready_for_execution`
- `observed_pass`
- `observed_fail`
- `deferred_optional`

These table values are row-level native-execution observation states only. Terminal method validation status is recorded only by method harness validation after verifier acceptance.

## BioHarness Bridge Replay From Author Case

When BioHarness bridge replay is selected, replay the same author-provided case through downstream-selectable Layer3/Layer4 build rows. Use the same data and comparable parameters when possible.

Bridge replay starts from a resolved BioHarness handoff.

For method-level execution, use `method_handoff` as the dispatch record. A bridge-specific handoff may be included inside the method handoff when bridge replay needs additional row-level evidence.

```yaml
bridge_replay_handoff:
  method:
  ordered_surfaces:
  completion_matrix_rows:
  build_output_result_files:
  build_audit_files:
  environment_ref:
  route_level_backend_load_evidence:
  input_preparation_boundary:
  required_input_payload:
  output_root:
```

A bridge replay handoff is complete when every selected row is `downstream_selectable=true`, the reviewed environment evidence includes the selected backend load path, and the selected input provides the payload required by the reviewed method route.

Bridge replay interpretation follows the lifecycle evidence recorded in the consumed build rows. Output-contract observation is recorded from the bridge replay run, not used as a build-evidence substitute.

After the handoff is resolved, bridge replay should use the Layer3 callable path, Layer4 backend binding, runtime entry, and implementation files recorded in the corresponding `build_output_result.yaml`. The replay should not infer these values from bridge planning alone.

Bridge replay must execute the reviewed BioHarness Layer3 callable path from the selected author-case input after any required reviewed input preparation. It must not start from a native-result-enriched object merely to extract structures, labels, exports, or plots.

If the author case starts from raw files, locators, or another non-canonical object, bridge replay may use only a reviewed input-preparation boundary to create the canonical input for the first selected BioHarness surface. This preparation evidence does not widen the Layer3 callable contract unless Gate1/Gate2 explicitly reviewed that widened input.

Native author-case outputs are comparison references and output-contract observation targets. Intermediate artifacts and static author results are recorded as observations or comparison references. The execution-surface output contract is assessed during bridge replay from the completed selected BioHarness surface chain and observed reviewed strict outputs.

Check whether BioHarness outputs satisfy the parent-function output expectations for the selected case. Do not use bridge replay to claim algorithmic equivalence unless a separate evaluation plan defines comparison criteria.

| Method | Author Case | Parent Function(s) Tested | Build Output / Bridge Path | Expected BioHarness Output | Native Output Reference | Observed Difference / Gap | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Output And Runtime Observation

Record only observed evidence from reviewed executions. Runtime-observation needs remain pending until execution occurs under the reviewed environment build output and Layer3/Layer4 build boundary.

Result consistency can be assessed only from observed execution evidence. Notebook outputs, screenshots, saved figures, or author text descriptions are static expected-output locators until execution produces comparable observed outputs.

| Method | Case | Output Objects | Artifact Files | Logs / Warnings / Errors | Runtime / Memory | Provenance Captured | Evidence Pointer |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Result Consistency Review

| Method | Case / Tutorial / Vignette / Example Data | Input Data Path Or Link | Native Workflow / Interface | Execution Surface Interface | Native Output Path | Execution-Surface Output Path | Native Result Summary | Execution-Surface Result Summary | Agent Consistency Judgment | Primary Human Consistency Judgment | Secondary Human Consistency Judgment | Evidence Pointer | Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allowed consistency judgment values:

- `consistent`
- `partially_consistent`
- `inconsistent`
- `not_assessable`
- `pending`

`Input Data Path Or Link` records the data location actually used for the reviewed execution. It may be a localized source path, a post-Gate2 downloaded local path, an online link, or `unavailable` when the run is blocked.

`Native Output Path` records the observed or referenced output from the original workflow/interface.

`Execution-Surface Output Path` records the output produced through the reviewed Layer3 execution surface / BioHarness bridge path.

`Native Result Summary` and `Execution-Surface Result Summary` should briefly describe the comparable result content without upgrading the observation into a final support claim.

The three consistency judgment columns record case-bound reviewer judgments only. They do not automatically combine into final support, algorithmic equivalence, biological correctness, production readiness, or final support status.

## Evidence Boundary

Native author-case execution shows native method behavior for the selected case only.

BioHarness bridge replay tests bridge behavior for the selected case only.

A referenced `build_output_result.yaml` supports bridge replay setup only when the corresponding completion matrix row has `downstream_selectable=true`. A per-row YAML file by itself is not sufficient bridge replay input and does not prove BioHarness support or output-contract satisfaction.

Declaration-only, no-registration, no-import, or incomplete Layer3 / Layer4 build rows must not be consumed by author-case/native workflow execution or BioHarness bridge replay.

Observed native success does not prove BioHarness support.

Observed BioHarness bridge success does not prove broad algorithmic equivalence or biological correctness.

Runtime, memory, artifact, and reproducibility observations become evidence only within the executed case boundary and recorded environment build output/build boundary.

## Non-Claims

Author case execution does not prove biological correctness.

It does not prove benchmark superiority.

It does not prove algorithmic equivalence unless a separate evaluation plan defines comparison criteria and evidence.

It does not establish production readiness.

It does not establish final support status by itself.
