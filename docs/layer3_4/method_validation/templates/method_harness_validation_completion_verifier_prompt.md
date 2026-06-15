# Method Harness Validation Completion Verifier Prompt

## Purpose

Read-only verifier for method harness validation evidence.

## Acceptance Rules

Accept workflow `PASS` only when `candidate_workflow_status: PASS` and the candidate result records data_input, reference_input, and execution_input consumability, a readable `surface_config_path`, `surface_config_load_result`, actual selected Layer3 execution evidence, actual config used for each selected surface invocation, real-result observation, loaded reference and harness comparison evidence, metric records or documented non-use, and an evidence-first comparison judgment.

Return `REPAIR_REQUIRED` when canonical input, Stage2 reference artifact, comparison_cues when supplied, environment evidence, build evidence, output-root evidence, selected Layer3 invocation evidence, or required validation evidence is incomplete.

Accept a candidate result only when `stage_handoff_evidence` records the instantiated Stage3 method prompt path, Stage1 result path, canonical input path, Stage2 result path, reference artifact path, reference artifact source field, surface config path, selected Layer3 surface evidence, and reviewed environment evidence supplied by the main implementation window.

Return `REPAIR_REQUIRED` when selected Layer3 invocation evidence is absent, with a repair instruction that routes the method task back to actual selected Layer3 execution. Do not accept a terminal method result for a non-executed selected chain.

Return `REPAIR_REQUIRED` when the method did not use the reviewed conda invocation while one was provided.

Return `REPAIR_REQUIRED` when a GPU-required method falls back to CPU before applying reviewed resource adjustments allowed by the surface contract, unless CPU fallback is explicitly reviewed.

Return `REPAIR_REQUIRED` when a simple non-semantic path, loader, parser, output-root, field-alias, or serialization repair is available but was not attempted.

Return `REPAIR_REQUIRED` when shared cell/spot/observation names are expected, `shared_count == 0`, and the candidate proceeds to agreement metrics or a consistency judgment without first resolving the execution/file-selection issue through reload, repair route, or candidate `TERMINAL_FAIL`.

Accept `TERMINAL_FAIL` only when all required data/build/environment evidence is available, `surface_config_path` is readable, `surface_config_load_result` is recorded, actual config used for each selected surface invocation is recorded, the selected Layer3 chain was actually run, allowed non-semantic repairs were attempted where applicable, and the remaining failure is inside method harness validation.

Accept a no-comparison-output `TERMINAL_FAIL` only when selected Layer3 invocation evidence exists, `real_result_observation.produced: false` or no comparison-ready harness artifact is documented, `reason_if_not_produced` is present, allowed repairs were attempted where applicable, and no comparison judgment is fabricated.

Return `BLOCKED_EXTERNAL` when the next action requires network, permission, storage, credentials, unavailable hardware, or another external action.

Do not accept a comparison judgment unless it first lists the reference file evidence, harness file evidence, shared cell/spot/observation-name comparison evidence when applicable, metric computation records when applicable, and then the consistent/inconsistent judgment with reason.

Do not re-evaluate Stage2 reference acquisition. The verifier does not audit full Stage2-to-Layer3-M parameter mapping correctness; it checks Stage3 config handoff presence, readability, and recorded use, plus Stage3 evidence completeness and workflow compliance. If candidate evidence itself shows that a selected Layer3-M exposed variable was omitted despite an available Stage2 or canonical-input source, return `REPAIR_REQUIRED`; otherwise do not require reporting unmapped Stage2 parameters.

## Output

```yaml
verifier_result:
  scope: method | package
  verifier_verdict: PASS | REPAIR_REQUIRED | BLOCKED_EXTERNAL
  method_acceptance:
    - method:
      method_workflow_terminal_status: PASS | TERMINAL_FAIL
      candidate_result_path:
      terminal_result_path:
  required_repairs:
    - method:
      stage:
      repair_instruction:
      evidence_needed:
```
