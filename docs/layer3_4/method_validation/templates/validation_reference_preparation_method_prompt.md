# Validation Reference Preparation Method Prompt

## Prompt Fields

This is a single-method subagent prompt template. It must be instantiated by the main implementation window from Stage1 method evidence. It does not perform package-level method selection, batch dispatch, package verification, or package report collation.

```yaml
analysis_problem:
method:
method_output_root:
owned_paths:
read_only_inputs:
analysis_problem_reference_expectation:
author_reference_inputs:
bioharness_context_inputs:
forbidden_primary_acquisition_routes:
author_workflow_locators:
reference_discovery_inputs:
execution_environment:
runtime_monitoring:
route_contamination_policy:
return_evidence:
stop_condition:
```

`read_only_inputs` must include the method's Stage1 `validation_input_preparation_result.yaml` and the verified canonical input path. The method result must copy the instantiated prompt path, Stage1 result path, and canonical input path into `stage_handoff_evidence`. The prompt must not predefine the method-specific selected primary target, output field, result slot, command, or parser target; those are discovered inside `reference_target_discovery`.

## Status Values

```text
REFERENCE_READY
REFERENCE_FAIL
```

## Constraints

### Reference Target Discovery

Load the planning reference requirement first, including expected result class and acceptable artifact classes. Then inspect method-specific tutorial, example, vignette, or source locators to identify the author output that satisfies both the planning requirement and author workflow evidence.

The selected target must be an algorithm output matching the analysis-problem result class.

Annotation, coordinates, input sidecars, ground truth, plots, configs, and expected paths are auxiliary or context unless author evidence explicitly defines them as the method result.

If no target can be selected after planning requirement review and author locator inspection, return `REFERENCE_FAIL` only with complete `failure_evidence`. Do not return a method result for incomplete inspection.

### Reference Acquisition Completion

Follow the all-caps `VALIDATION_REFERENCE_PREPARATION` pseudocode in `docs/layer3_4/method_validation/validation_reference_preparation.md`.

Complete target discovery before acquisition. Complete the discovered acquisition route before returning `REFERENCE_READY` or `REFERENCE_FAIL`.

For static references, check the reviewed local artifact and record read or load evidence.

For generated-in-run references, run the reviewed author workflow or reviewed command path. Here, reviewed author workflow or reviewed command path means the original repository workflow, script, vignette, example, or native package/API path matching the author workflow.

Generated-in-run references must preserve author tutorial, example, vignette, script, or package/API parameters. When author defaults or tutorial parameters are available, use them as the execution parameters. Record the reviewed parameter source, actual parameters, and all differences.

Treat training epochs, batch size, learning rate, model dimensions, preprocessing thresholds or preprocessing parameter values, cluster number, resolution, K, random seed value or seed-selection policy, and augmentation probabilities as output-affecting unless author evidence or reviewed planning evidence says otherwise. Treat workdir, output path, log name, temporary directory, cache directory, reviewed bridge invocation form, and compatibility patches for dependency APIs, language bridges, matrix orientation, dtype conversion, sparse/dense conversion, NA/NaN handling, and randomness-control plumbing as runtime-only when they preserve the author workflow input, algorithm branch, core algorithm call, selected target, result field, output-affecting parameter values, and label alignment logic.

For GPU training, fitting, or embedding-learning routes, preserve the author GPU route when reviewed GPU evidence is available. A CUDA OOM is a resource failure, not by itself a reason to switch to CPU. First retry on GPU with reviewed memory-pressure adjustments. Batch size remains output-affecting by default, but CUDA OOM may justify a reviewed resource adjustment when epochs, learning rate, seed policy, model parameters, preprocessing parameters, selected target, and result field are preserved. CPU fallback after CUDA OOM requires recorded GPU memory repair attempts or a documented reason why GPU repair is not applicable.

Do not reduce training epochs as an OOM repair for accepted reference acquisition. Reduced epochs may be used only as diagnostic or preflight evidence, not as `REFERENCE_READY`.

Stage2 may perform lightweight `native_input_layout_materialization` inside the generated-in-run route. The allowed scope is limited to small author-workflow-required sidecar or layout files, linking or copying reviewed local artifacts, downloading missing files from reviewed locators, or generating layout files that the author script reads. It must not rebuild the canonical input, change the Stage1 selected case, change the analysis-problem input definition, or use BioHarness Layer3/4 output.

Do not use `prepare_spatial_domain_input`, `construct_spatial_structure`, `fit_then_assign_domains`, `export_domain_result`, the Layer3 callable registry, bridge replay, a Layer4 wrapper path, a method harness run, or an execution-surface driver as Stage 2 primary reference acquisition.

If the current command or script invokes a BioHarness Layer3/4 surface chain, `bioharness_sdi_runtime.layer3`, the Layer3 callable registry, bridge replay, or an execution-surface driver to generate primary labels, stop that acquisition route and record diagnostic evidence. Native/static acquisition evidence is still required before accepting a method result.

BioHarness-reviewed conda prefixes may be used as compatible runtime environments for native workflows, but the complete reviewed runtime invocation must be used and recorded, including required `LD_LIBRARY_PATH`, `PYTHONPATH`, `R_LIBS`, `PATH`, CUDA variables, or other environment variables. A bare prefix executable failure is not sufficient environment-failure evidence until the complete reviewed invocation has been tested.

Record command, working directory, environment, return code, logs, produced artifacts, and loader or parser summary for native generated-in-run references.

For long-running native generated-in-run references, also record runtime monitoring evidence: PID when available, heartbeat interval, reviewed timeout, no-progress threshold, progress log or tail log, host memory/disk snapshot, CPU/RSS snapshot when available, and termination reason.

When the result exists only in a runtime object, use export-only wrapping only inside the discovered export-only scope. Record the exported field, slot, key, or object and the written artifact.

When the original author workflow itself uses a language bridge such as rpy2, first follow the author workflow. If that native author route fails at the bridge boundary, a repair route may use export-only native-runtime materialization, such as exporting a Python-produced matrix and running the author-intended R package by Rscript, only when the algorithm target and selected result field are unchanged.

Retry local path, working-directory, output-directory, lightweight loader, parser, and export-only issues while they remain inside the reviewed boundary.

Copied-source compatibility patches are allowed only inside the Stage2 owned copied workdir. They must not modify the reviewed author source repository. Record `compatibility_patch_evidence` with patch rationale, patched file paths, diff paths, retry logs, and why the patch is runtime-only. If preprocessing code is touched, keep author preprocessing parameters unchanged and record the preprocessing parameter consistency check.

A locator, documentation statement, expected path, or command string is not acquisition evidence by itself.

### Status Rules

Return `REFERENCE_READY` when planning requirement evidence, author target discovery evidence, completed native/static acquisition evidence, materialized artifacts, parser or loader summary, and files written are present.

Return `REFERENCE_FAIL` only when complete `failure_evidence` is present. Static-missing cases must run the original author tutorial, example, vignette, script, or native package/API before failing unless failure evidence shows a preflight blocker after lightweight native input layout materialization was attempted, or shows that materialization would exceed the allowed boundary, such as permission, storage, dependency, canonical-input rebuild, selected-case change, analysis-problem input change, or BioHarness Layer3/4 output use.

Do not return `REFERENCE_FAIL` when the next action is a simple local retry, output-directory fix, parser fix, export-only wrapper, or native workflow run that has not yet been attempted.

Do not return legacy unavailable, repair-required, or external-blocked reference-preparation statuses as Stage2 method results.
