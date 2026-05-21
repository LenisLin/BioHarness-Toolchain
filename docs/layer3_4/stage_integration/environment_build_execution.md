# Environment Build Execution

## Purpose

This file defines the post-Gate2 execution workflow for a Gate 2-reviewed environment integration planning item whose assigned step is `environment_build_execution`.

Environment build execution assembles or updates a host conda environment branch from a reviewed Environment Build Plan. It produces reviewed environment build output, including a reviewed environment binding record, for later Layer3/Layer4 build, author-case execution, bridge replay, and validation planning. It does not build Docker images.

The execution plan comes from the Gate 2 human review table pointing to a filled environment integration planning record. This repo instruction file defines the reusable workflow; it is not itself the execution plan.

## Inputs

The Gate 2 row must include:

- `Planning Area = environment_integration_planning`
- `Gate 2 Review Result = approved_for_next_step`
- `Step After Gate 2 = environment_build_execution`
- `Filled Planning File Path`
- `Reviewed Item`
- `Output Path`

Execution reads the reviewed `Environment Build Plan` section from the filled planning record identified by `Filled Planning File Path`. `Reviewed Item` should identify the specific Environment Build Plan or environment branch under review. `Output Path` points to the environment branch build output directory.

Execution may consult only the source and config references explicitly listed in the reviewed planning record when those references are needed to execute the plan. It must not broad reread repositories, expand dependency scope, add a new environment branch, or add a new Layer3 interface target. Scope expansion requires targeted planning repair or Gate 2 re-review.

## Execution Boundary

Environment build execution is plan-led. Follow the reviewed plan step order for host conda environment create, update, and check actions; perform only the planned load checks; and write the required output files.

Allowed execution controls are limited to:

- stop on an unhandled failure and record the failure event;
- apply only the rollback, split, or repair response already specified in the reviewed plan;
- request targeted planning repair or re-review when the plan lacks a necessary dependency boundary, branch decision, failure response, or Layer3 interface target.

This workflow does not run method workflows, author cases, bridge replay, data downloads, validation fixtures, biological interpretation, or Docker builds.

## Required Outputs

The `Output Path` directory must contain the core environment branch build outputs below:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

### harness_environment.yaml

`harness_environment.yaml` is the reviewed environment binding record. It records the reviewed method / Layer3 interface path / `environment_branch` / `conda_prefix` binding for the reviewed environment branch.

It is not the formal harness UI, a prompt contract, or an agent-interpreted environment selection entry. It should not contain status, build ID, provider, log, reproducibility, Gate 2, non-claim, or execution-event fields.

Use this minimal shape:

```yaml
analysis_problem:
environment_branch:
conda_prefix:
compatible_methods:
  - method:
    layer3_interface_paths:
compatibility_note:
```

`layer3_interface_paths` identifies BioHarness Layer3 interface paths after Layer3/4 restructuring. It is not the original repository path, tutorial path, source config path, or native method path.

### environment_build.yaml

`environment_build.yaml` is a pure conda YAML for reproducibility of the reviewed environment branch. By default, do not write `prefix:`. If a prefix is required by a reviewed local execution policy, record that decision outside the conda YAML or in the event log rather than making it the default template behavior.

### environment_build.jsonl

`environment_build.jsonl` records the actual environment build events in the same order as the reviewed plan steps. Each line should be a single JSON object with enough detail to audit the step, command intent, result, failure response, and evidence pointer when applicable.

Example event fields:

```json
{"step_index":1,"planned_step":"conda_env_create","result":"passed","note":"created reviewed branch environment"}
```

## Evidence Boundary

Reviewed environment build output may support later `layer3_layer4_build`, author-case execution, bridge replay, and validation planning by giving those workflows a reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.

The output records host conda environment assembly/update/check behavior for the reviewed environment branch only. Install and load checks inside the plan are environment build checks, not workflow success evidence.

## Non-Claims

Environment build output does not establish method workflow success.

It does not establish author-case success.

It does not establish functional correctness.

It does not establish production readiness.

It does not establish algorithmic equivalence.

It does not establish biological correctness.
