# Author Case Execution

## Purpose

This file defines author-case/native workflow execution and BioHarness bridge replay for a Gate 2-reviewed functional testing planning item whose assigned step is `author_case_native_workflow_and_bridge_replay`.

Author case execution observes whether a selected documented method path can run under the reviewed execution boundary and produce inspectable outputs, artifacts, and logs.

## Inputs

- Gate 2-reviewed functional testing planning item with assigned step `author_case_native_workflow_and_bridge_replay`.
- Functional testing planning file.
- Reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path referenced by the Gate 2 human review table for this author-case run.
- `build_output_result.yaml` from `layer3_layer4_build.md` when BioHarness bridge replay is planned.
- `build_audit.yaml` as boundary evidence when relevant.
- Implemented Layer3 callable / Layer4 backend binding from `build_output_result.yaml` when BioHarness bridge replay is planned.
- Original repository case, tutorial, vignette, or example locators.
- Data and artifact origin locators.
- Expected output form and output-contract expectations.
- Storage/runtime conventions for logs, outputs, and evidence records.

Author-case execution uses the reviewed environment binding/build output as an engineering input. It must not re-infer dependency boundaries, environment branch, conda prefix, or method routing. Missing or insufficient environment binding/build output routes back to the relevant environment planning/build review path.

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

## BioHarness Bridge Replay From Author Case

If a BioHarness Layer4 bridge exists or is being tested, replay the same author-provided case through the BioHarness path. Use the same data and comparable parameters when possible.

Bridge replay should use the Layer3 callable path, Layer4 backend binding, runtime entry, and implementation files recorded in `build_output_result.yaml`. The replay should not infer these values from bridge planning alone.

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

A referenced `build_output_result.yaml` supports bridge replay setup, but it does not by itself prove BioHarness support or output-contract satisfaction.

Observed native success does not prove BioHarness support.

Observed BioHarness bridge success does not prove broad algorithmic equivalence or biological correctness.

Runtime, memory, artifact, and reproducibility observations become evidence only within the executed case boundary and recorded environment build output/build boundary.

## Non-Claims

Author case execution does not prove biological correctness.

It does not prove benchmark superiority.

It does not prove algorithmic equivalence unless a separate evaluation plan defines comparison criteria and evidence.

It does not establish production readiness.

It does not establish final support status by itself.
