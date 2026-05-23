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

For `environment_build_execution`, Gate 2 should confirm that the filled plan records branch naming rules, load-check attribution units, branch output path rules, conda prefix rules, and successful-branch selection-index handoff.

## Human-In-The-Loop Discussion Protocol

Gate 2 discussion is a human-in-the-loop planning confirmation loop before the formal Gate 2 human review table is written. The discussion should help human reviewers find planning ambiguities, missing fields, execution-boundary gaps, and reviewability blockers, then route confirmed issues to targeted static reading or targeted planning repair.

This discussion is not post-Gate2 execution and is not itself the formal Gate 2 human review table.

### Discussion Boundary

- Work read-only until a human explicitly authorizes planning-record repair.
- Do not execute environment builds, dependency installs, imports, R library loads, GPU checks, method workflows, author cases, bridge replay, validation, or post-Gate2 build workflows.
- Do not generate new aggregation or index artifacts unless the human explicitly requests them.
- Do not make Gate 2 decisions on behalf of the human reviewer.
- Do not perform broad terminology or language audits.
- Raise wording issues only when they affect workflow correctness, Gate 2 reviewability, execution boundary, or downstream artifact usability.
- Treat runtime-only unknowns as runtime observation needs unless the planning record incorrectly depends on them before execution.

### Required File Check

Before discussion begins, check that all three filled planning files exist:

1. `environment_integration_planning`
2. `layer4_bridge_planning` / method-to-parent Layer4 bridge planning
3. `functional_testing_planning` / function-validation planning

If any required planning file is missing, stop and report the missing file. Do not infer, recreate, or substitute the missing planning record.

### Serial Review Order

Review the three planning files strictly in this order:

1. `environment_integration_planning`
2. `layer4_bridge_planning` / execution-surface planning
3. `functional_testing_planning` / function-validation planning

Do not start reviewing the next planning file until the human has confirmed the current file's ambiguity/blocker table and any required repair direction.

### Per-Plan Discussion Loop

For each planning file:

1. Read the planning file and the relevant Gate 2 workflow instructions.
2. Identify only issues that may block or confuse downstream execution, build, or review.
3. Summarize candidate issues in the ambiguity/blocker review table.
4. Ask the human to confirm whether each candidate issue is real and whether the intended interpretation is correct.
5. For human-confirmed issues, perform only the targeted static reading or planning-record repair that the human authorizes.
6. Re-review the repaired planning file.
7. Repeat until the human confirms that no blocking ambiguity remains for that planning file.
8. Only then proceed to the next planning file.

### Ambiguity / Blocker Review Table

Use this table for human review before any repair:

| Issue ID | Planning File | Location | Brief Explanation For Human Reviewer | Potential Blocker / Ambiguity | Why It May Affect Downstream Execution Or Review | Evidence Already Present | Missing Or Unclear Part | Proposed Handling | Human Confirmation Needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Field guidance:

- `Issue ID`: Stable short ID for discussion, such as `ENV-Q1`, `SURFACE-Q1`, or `VALIDATION-Q1`.
- `Planning File`: One of the three filled planning files under review.
- `Location`: Section, row, heading, or line reference when available.
- `Brief Explanation For Human Reviewer`: Short plain-language explanation so the human can judge the issue without reconstructing the whole context.
- `Potential Blocker / Ambiguity`: The concrete planning problem being raised.
- `Why It May Affect Downstream Execution Or Review`: The practical failure mode if the issue is left unresolved.
- `Evidence Already Present`: Existing planning-file or source-evidence anchors.
- `Missing Or Unclear Part`: The specific information, policy, path, boundary, or locator that is absent or ambiguous.
- `Proposed Handling`: Use one of the discussion-stage handling labels below.
- `Human Confirmation Needed`: The exact yes/no or short decision the human must make before repair or progression.

Allowed discussion-stage handling labels:

- `no_issue`
- `acceptable_runtime_uncertainty`
- `needs_more_static_reading`
- `targeted_planning_repair_candidate`
- `possible_return_to_gate1_candidate`

These labels are for discussion only. The formal Gate 2 human review output must still use only `approved_for_next_step`, `targeted_planning_repair_required`, or `return_to_gate1`.

### Human Confirmation Rules

Do not repair or advance to the next planning file until the human confirms the current table.

For each candidate issue, the human should confirm one of:

- The issue is real and should enter targeted planning repair.
- The issue is real but needs more static reading first.
- The issue is acceptable runtime uncertainty and should not be repaired now.
- The issue is not a real blocker.
- The issue may affect a Gate 1 boundary or method x surface route and needs possible `return_to_gate1` discussion.

If the human does not confirm the issue, do not treat it as a Gate 2 blocker.

### Targeted Repair Return Table

After an authorized repair or static rereading pass, return with:

| Repair ID | Original Issue ID | Planning File | What Was Checked Or Changed | Why This Resolves The Blocker | Remaining Ambiguity | Human Recheck Needed |
| --- | --- | --- | --- | --- | --- | --- |

A repair is complete only after the human confirms that the original blocker has been resolved or reclassified.

### Cross-Plan Review

After all three planning files have been individually confirmed, perform one cross-plan consistency review before writing the formal Gate 2 human review table.

Use this table:

| Cross-Plan Check ID | Brief Explanation For Human Reviewer | Plans Compared | Potential Cross-Plan Issue | Evidence Already Present | Missing Or Unclear Part | Proposed Handling | Human Confirmation Needed |
| --- | --- | --- | --- | --- | --- | --- | --- |

Required cross-plan checks:

- Environment build output paths required by Layer3/Layer4 build and function-validation planning are present and consistent.
- Execution-surface build granularity is consistent with function-validation prerequisites.
- Function-validation planning depends only on reviewed or planned environment/build outputs.
- Remaining targeted repairs are either resolved or explicitly routed before execution.
- No planning record claims runtime support, import success, workflow success, validation success, production readiness, algorithmic equivalence, or biological correctness before execution evidence exists.

### Formal Gate 2 Output Boundary

Only after the human confirms that all three planning files have no unresolved blocking ambiguity and the cross-plan review has no unresolved blocker, write the formal Gate 2 human review table.

The formal output must use the approved Gate 2 review result vocabulary:

- `approved_for_next_step`
- `targeted_planning_repair_required`
- `return_to_gate1`

The formal output must use the approved Gate 2 assigned-step vocabulary:

- `environment_build_execution`
- `layer3_layer4_build`
- `author_case_native_workflow_and_bridge_replay`

## Planning Areas

Allowed `Planning Area` values:

- `layer4_bridge_planning`
- `environment_integration_planning`
- `functional_testing_planning`

`layer4_bridge_planning` records how a Gate 1-reviewed method x parent-function route is prepared for Layer3 parent-function callable / Layer4 support build.

`environment_integration_planning` records the Environment Build Plan or initial Environment Build Target and reviewed Layer3 parent-function / method-route binding scope for Gate 2 review before `environment_build_execution`. It does not require final callable paths before `layer3_layer4_build` produces `build_output_result.yaml`.

`functional_testing_planning` records how an author-case/native workflow and BioHarness bridge replay path is prepared.

## Gate 2 Review Results

Gate 2 review results:

- `approved_for_next_step`
- `targeted_planning_repair_required`
- `return_to_gate1`

Use `approved_for_next_step` when the reviewed planning item has sufficient evidence and clear boundaries for the assigned post-Gate2 step.

Use `approved_for_next_step` for an environment build item only when the reviewed plan can produce base, single-method, or reviewed method-set environment evidence without inventing branch names or load-check attribution during execution.

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

`Output Path` points to the post-Gate2 output location. For `environment_build_execution`, Output Path points to the reviewed initial environment build output directory containing `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl`, unless a later reviewed decision creates another target. For `layer3_layer4_build`, it points to `build_output_result.yaml` and, when used, `build_audit.yaml`. For `author_case_native_workflow_and_bridge_replay`, it points to author-case/native workflow and bridge replay evidence.

For environment rows, `Filled Planning File Path` points to the filled environment integration planning record, and `Reviewed Item` points to the Environment Build Plan or initial Environment Build Target under review.

For environment rows, identify the planned environment build target and reviewed Layer3 binding scope. The pre-build scope is a reviewed parent-function / method-route binding scope, not a final `callable_path`; final callable paths are produced later by `layer3_layer4_build` in `build_output_result.yaml`. The reviewed `environment_branch` binding is recorded later in `harness_environment.yaml` after environment build execution. Native repository paths, install files, source configs, tutorials, or reader artifacts remain evidence locators; they are not Layer3 binding scopes or interface targets.

Split Triggers are reviewed as planning risks, repair triggers, or later review targets. They are not default output paths and do not create split targets before reviewed environment build evidence or later review.

If `Gate 2 Review Result` is `approved_for_next_step`, `Step After Gate 2` and `Output Path` are required. If the review result is `targeted_planning_repair_required`, `Repair / Return Target` is required and execution/build does not start. If the review result is `return_to_gate1`, `Repair / Return Target` should identify the parent-function, execution-surface, or method x surface route issue.

## Targeted Planning Repair

Targeted planning repair is limited to a specific planning defect found during Gate 2 review.

| Repair ID | Planning Area | Reviewed Planning File | Reviewed Item | Repair Target | Allowed Repair Source | Required Return |
| --- | --- | --- | --- | --- | --- | --- |

Allowed repair sources are exact local source locators, official static documentation linked by the method repository, or existing NAS evidence records. Repair work should return an updated planning record for Gate 2 review.

## Boundary

Gate 2 human review output routes reviewed planning items to assigned post-Gate2 steps or repair loops. Later environment build execution, Layer3/Layer4 build, author-case/native workflow execution, BioHarness bridge replay, post-implementation validation, and Gate 3 review produce their own evidence records or build outputs.
