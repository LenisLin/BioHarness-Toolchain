# Method Harness Validation Prompt

This is a single-method subagent prompt template. It must be instantiated by the main implementation window from Stage1 INPUT_READY evidence, Stage2 REFERENCE_READY evidence, selected Layer3 surface evidence, and reviewed environment evidence. It does not perform package-level method selection, package verification, package report collation, or package-level terminal result writing.

## Prompt Fields

```yaml
analysis_problem:
method:
stage_handoff_evidence:
method_output_root:
owned_paths:
read_only_inputs:
canonical_validation_input:
reference_evidence:
comparison_cues:
build_evidence:
environment_evidence:
method_harness_surface_config:
  surface_config_path:
  load_required: true
reviewed_conda_environment:
gpu_execution_policy:
execution_environment:
selected_layer3_callable_chain:
selected_layer3_surface_contracts:
interface_preparation_policy:
bounded_nonsemantic_repair_policy:
comparison_record_requirements:
runtime_monitoring:
return_evidence:
stop_condition:
```

The candidate result must copy `stage_handoff_evidence.instantiated_method_prompt`, `stage_handoff_evidence.stage1_input_preparation_result`, `stage_handoff_evidence.canonical_input_path`, `stage_handoff_evidence.stage2_reference_preparation_result`, `stage_handoff_evidence.reference_artifact_path`, `stage_handoff_evidence.reference_artifact_source_field`, `stage_handoff_evidence.surface_config_path`, `stage_handoff_evidence.selected_layer3_surface_chain_evidence`, and `stage_handoff_evidence.reviewed_environment_evidence`.

## Status Values

```text
Candidate workflow status:
PASS
TERMINAL_FAIL

Verifier verdict:
PASS
REPAIR_REQUIRED
BLOCKED_EXTERNAL

Dispatch status:
repair_required
blocked_external
```

## Constraints

Start only from canonical validation input.

Use only the selected Layer3 callable/interface evidence exposed by the selected surface contract.

Read `method_harness_surface_config.surface_config_path`, record `execution_input.surface_config_load_result`, and use only selected-surface entries from `surface_config`; pass each selected surface config into the corresponding Layer3 callable; record the actual per-surface config values in the candidate result.

If the supplied surface config omits a selected Layer3-M exposed variable that appears resolvable from Stage2 parameter evidence, native command or loader-call evidence, generation-route evidence, or canonical input schema for input-mapping selectors, return a package repair route rather than silently relying on Layer4 defaults. This check is limited to selected Layer3-M exposed variables and does not require auditing unmapped Stage2 parameters.

You must actually run the selected Layer3 execution surface chain before writing a verifier candidate result. A filled result table without Layer3 invocation evidence is not an accepted output.

Do not write a verifier candidate result before selected Layer3 invocation evidence exists. If execution has not occurred, continue to execution or return only a verifier/package repair route that instructs execution to run the selected Layer3 chain.

Run through the reviewed conda invocation supplied for this method. Do not use bare system Python/R when a reviewed conda invocation is available.

For GPU-required methods, use the reviewed GPU execution route. Do not fallback to CPU unless the reviewed policy explicitly allows it. For GPU memory/resource failures, first try allowed resource adjustments, such as batch size, when they do not change execution surface semantics.

For simple path, loader, parser, output-root, field-alias, or serialization failures that do not change the selected execution surface semantics, attempt a bounded repair and record the attempt before returning `TERMINAL_FAIL`.

If selected Layer3 invocation evidence exists, allowed repairs were attempted, no comparison-ready harness result was produced, and the remaining failure is inside method harness validation, write a candidate `TERMINAL_FAIL` with `reason_if_not_produced` and failure evidence. Do not fabricate comparison evidence or a consistency judgment.

The comparison section must list evidence first and judgment second. The judgment must cite the loaded reference file, loaded harness file, shared cell/spot/observation-name comparison evidence when applicable, and any computed metric records.

When shared cell/spot/observation names are expected and `shared_count == 0`, treat this as an execution/file-selection check before metric computation. Recheck the canonical input, Stage2 reference artifact, harness output artifact, `id_field`, and `result_field`; repair and reload within policy when the issue is a simple artifact or field selection issue. If the check still leaves no shared names, do not compute agreement metrics; return the appropriate verifier repair route or candidate `TERMINAL_FAIL` using existing execution/failure fields.

Each metric record must state the formula or the exact library function, package, version when available, call signature, input vectors, preprocessing, value, and reason when not computed.

Write a verifier candidate result for review. Package-level terminal method results are written only after verifier acceptance.
