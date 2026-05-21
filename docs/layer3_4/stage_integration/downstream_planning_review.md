# Downstream Planning Review

## Purpose

This file defines Gate 2: the downstream planning review after Gate 1 parent-function / execution-surface alignment and after the three downstream planning files are prepared.

Gate 2 reviews current in-scope planning items from the three downstream planning areas and assigns post-Gate2 steps in a human review table. The review target is the filled planning item, not a repo instruction file, method-level inclusion decision, or execution result.

## Reviewed Planning Files

Gate 2 reviews the filled planning files prepared for the current feature or method pass. These files correspond to three planning areas:

- method-to-parent Layer4 bridge planning
- environment integration planning
- functional testing planning

The repo files in this directory define reusable instructions and review criteria. They are not the filled planning files under review. Gate 2 records the filled planning file path and the specific reviewed item, table row, or section.

## Inputs

- Gate 1 parent-function / execution-surface alignment review file.
- Layer4 bridge planning file.
- Environment integration planning file.
- Functional testing planning file.
- Completed targeted supplemental reading records when they affect a reviewed planning record.
- Integration-readiness audit and audit-closing repair records when they define the current planning input boundary.

## Review Scope

Gate 2 checks whether each reviewed planning item has enough domain-specific detail to enter its assigned post-Gate2 execution/build workflow.

The review should confirm that each planning item:

- refers to the relevant Gate 1-reviewed parent function, execution surface, and planning route when applicable;
- records the filled planning file path and reviewed item under review;
- identifies the locators, boundaries, required evidence, open questions, and evidence-to-produce fields required by its downstream planning area;
- identifies the output path for the post-Gate2 evidence or build output when the item is approved;
- routes remaining planning defects to a targeted repair record;
- routes Gate 1 boundary issues to `return_to_gate1`.

Gate 2 does not create method-level `keep`, `exclude`, or `defer` decisions. If a reviewed planning item exposes a parent-function, execution-surface, or method x surface route issue, the next step is `return_to_gate1`.

## Planning Areas

Allowed `Planning Area` values:

- `layer4_bridge_planning`
- `environment_integration_planning`
- `functional_testing_planning`

`layer4_bridge_planning` records how a Gate 1-reviewed method x parent-function route is prepared for Layer3 parent-function callable / Layer4 support build.

`environment_integration_planning` records reviewed environment branches and Layer3 interface targets for `environment_build_execution`.

`functional_testing_planning` records how an author-case/native workflow and BioHarness bridge replay path is prepared.

## Gate 2 Review Results

Gate 2 review results:

- `approved_for_next_step`
- `targeted_planning_repair_required`
- `return_to_gate1`

Use `approved_for_next_step` when the reviewed planning item has sufficient evidence and clear boundaries for the assigned post-Gate2 step.

Use `targeted_planning_repair_required` when the planning item needs a narrow repair before it can enter an assigned post-Gate2 step.

Use `return_to_gate1` when the issue affects the Gate 1 parent-function boundary, execution-surface scope, or method x surface planning route.

## Gate 2 Assigned Steps

Gate 2 assigned steps:

- `environment_build_execution`
- `layer3_layer4_build`
- `author_case_native_workflow_and_bridge_replay`

These steps are handled by:

- `environment_build_execution` -> `environment_build_execution.md`
- `layer3_layer4_build` -> `layer3_layer4_build.md`
- `author_case_native_workflow_and_bridge_replay` -> `author_case_execution.md`

## Gate 2 Human Review Table

| Planning Area | Filled Planning File Path | Reviewed Item | Method / Path | Reviewed Target | Required Evidence | Open Question / Blocker | Gate 2 Review Result | Step After Gate 2 | Output Path | Evidence Boundary | Repair / Return Target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`Output Path` points to the post-Gate2 output location. For `environment_build_execution`, Output Path points to the environment branch build output directory containing `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl`. For `layer3_layer4_build`, it points to `build_output_result.yaml` and, when used, `build_audit.yaml`. For `author_case_native_workflow_and_bridge_replay`, it points to author-case/native workflow and bridge replay evidence.

For environment rows, `Filled Planning File Path` points to the filled environment integration planning record, and `Reviewed Item` points to the specific Environment Build Plan or environment branch under review.

For environment rows, identify the reviewed `environment_branch` and Layer3 interface target(s). Native repository paths, install files, source configs, tutorials, or reader artifacts remain evidence locators; they are not Layer3 interface targets.

If `Gate 2 Review Result` is `approved_for_next_step`, `Step After Gate 2` and `Output Path` are required. If the review result is `targeted_planning_repair_required`, `Repair / Return Target` is required and execution/build does not start. If the review result is `return_to_gate1`, `Repair / Return Target` should identify the parent-function, execution-surface, or method x surface route issue.

## Targeted Planning Repair

Targeted planning repair is limited to a specific planning defect found during Gate 2 review.

| Repair ID | Planning Area | Reviewed Planning File | Reviewed Item | Repair Target | Allowed Repair Source | Required Return |
| --- | --- | --- | --- | --- | --- | --- |

Allowed repair sources are exact local source locators, official static documentation linked by the method repository, or existing NAS evidence records. Repair work should return an updated planning record for Gate 2 review.

## Boundary

Gate 2 human review output routes reviewed planning items to assigned post-Gate2 steps or repair loops. Later environment build execution, Layer3/Layer4 build, author-case/native workflow execution, BioHarness bridge replay, post-implementation validation, and Gate 3 review produce their own evidence records or build outputs.
