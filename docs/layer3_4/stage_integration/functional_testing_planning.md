# Functional Testing Planning

## Purpose

This file defines the pre-Gate2 functional testing planning file for method-centered result testing using author-provided case, tutorial, vignette, or example workflows from the original repository.

Functional testing planning prepares author-case and validation candidates. It does not define terminal method validation status. Post-build method validation is defined in `docs/layer3_4/method_validation/`.

Functional testing planning selects candidate author cases, records source/data/result locators, identifies expected output forms, and prepares execution targets for later author-case/native workflow execution and BioHarness bridge replay. It does not execute notebooks/scripts, download data, record observed outputs, record runtime metrics, or claim BioHarness validation evidence.

Validation planning is organized once per method. Cases may record which reviewed parent functions or execution surfaces they cover, but the plan should not duplicate a complete method validation package for every execution surface.

Gate 2 downstream planning review for functional testing planning checks whether static evidence identifies an author-case candidate, code/data/result locators, expected output form, required environment build output, required Layer3/Layer4 build output when bridge replay is planned, an evidence output path, and evidence to produce.

## Inputs

- Parent-function / execution-surface candidates.
- Method-to-parent Layer4 bridge hypotheses.
- Environment integration planning outputs, including the analysis-problem-level planned Environment Build Target.
- Reviewed environment binding record (`harness_environment.yaml`) or required reviewed environment build output path when already available from an earlier reviewed pass. Pre-Gate2 functional planning should reference the planned analysis-problem-level environment build target from environment integration planning.
- Docs/Workflow reader outputs listing original repository cases/tutorials/vignettes/examples.
- Author Case Asset Locator Table from Output/Validation Reader.
- Output/Validation runtime-observation needs.
- Package review gaps affecting case eligibility.

## Case / Tutorial / Vignette Selection

Use original repository cases first. Candidate cases come from the Author Case Asset Locator Table and may point to README quickstarts, tutorials, notebooks, vignettes, example scripts, and author-provided test data. Functional testing planning should not rediscover basic case assets after audit closure.

The first functional testing question is which author-provided case is eligible as the primary runnable case and what artifact origins the case depends on.

Select a primary runnable case when data, instructions, dependencies, and expected outputs are sufficiently documented by the locator table and related evidence. If a case depends on unavailable external data or insufficient instructions, record it as blocked or deferred rather than replacing it with synthetic data.

Repository-provided fixtures or test data may be used when they are part of the upstream method repository or official documentation. Synthetic, minimal, or BioHarness-created fixtures are out of scope for this functional-testing stage unless a later design document explicitly promotes a separate runtime-result validation task.

Case code follows a locator-only policy in planning documents: record locators and commands, but do not copy author case code into repo docs. Data download and execution occur only in the author-case execution workflow when Gate 2 assigns `author_case_native_workflow_and_bridge_replay` to the reviewed functional testing planning item. Author case reproduction occurs only after parent functions, reviewed environment build output, and the Layer3/Layer4 build output are defined enough to make the run interpretable.

| Method | Case / Tutorial / Vignette | Source Locator | Covered Parent Function(s) | Data Availability | Artifact Origin | Execution Form | Expected Author Outputs | Resource / Optional Dependency Notes | Eligibility |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allowed artifact-origin values:

- `bundled_data`
- `generated_intermediate`
- `pretrained_model`
- `notebook_output`
- `external_download`
- `unclear`

Allowed eligibility values:

- `selected_primary_case`
- `candidate_case`
- `blocked_by_data`
- `blocked_by_environment`
- `blocked_by_missing_instructions`
- `deferred_heavy_case`
- `deferred_optional_path`

## Execution Target Planning

| Method | Case / Tutorial / Vignette | Execution Target | Required Environment Build Output | Required Layer3/Layer4 Build Output | Expected Output For Contract Check | Evidence Output Path | Evidence To Produce | Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allowed execution targets:

- `candidate_native_author_case_execution`
- `candidate_bioharness_bridge_replay_from_author_case`
- `requires_environment_build_output`
- `requires_layer3_layer4_build_evidence`
- `requires_data_or_instruction_resolution`

Execution target planning records the planned author-case/native workflow or bridge-replay target for Gate 2 downstream planning review. Observed outputs, runtime metrics, pass/fail status, and BioHarness validation evidence belong in the later author-case/native workflow execution and bridge replay records.

Functional testing planning items should identify the method, author case or tutorial target, covered parent function(s), reviewed environment binding record (`harness_environment.yaml`) or required reviewed environment build output path, required Layer3/Layer4 build output when BioHarness bridge replay is planned, expected output for contract check, open planning question if any, evidence output path, and evidence boundary.

The required environment output should identify the planned environment build target for the analysis problem, or the reviewed environment build output path when it already exists.

Pre-Gate2 functional testing planning must not infer method-specific environment bindings, `environment_branch` values, or method-specific `harness_environment.yaml` paths from text evidence. Method-specific environment bindings can be referenced only after reviewed environment build output exists or later review creates a separate target.

Required Layer3/Layer4 build output for bridge replay is recorded as a dependency on completed downstream-selectable build rows under the current `layer3_layer4_build.md` workflow. Functional testing planning records which surfaces will be consumed and where the future build evidence is expected; it does not define build completion, verifier, publication, or downstream-selectable rules.

Functional validation planning records an explicit validation scope before execution.

At planning time, method-specific repository vignette/example/source code is not inspected to select concrete result keys, object slots, output paths, or command outputs. Functional testing planning records only the analysis-problem-level expected reference mode: expected result class, acceptable artifact classes, auxiliary/context-only artifacts, candidate locator classes, and evidence to produce. Concrete per-method reference targets are discovered later during `validation_reference_preparation`.

```md
| Method | Surface Rows Consumed | Completion Matrix Evidence | Environment Evidence | Required Case Data | Author Workflow Locator | Expected Result Reference | Required Canonical Validation Input | Reviewed Output Root | Current Validation Decision | Required Repair Before Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <method> | <ordered selected surfaces> | <downstream-selectable rows and per-row YAMLs> | <environment branch with route-level backend load evidence> | <case data locator or reviewed data target> | <tutorial/example/script/workflow locator> | <analysis-problem result class; expected reference modes such as static artifact / generated-in-run / unavailable; acceptable artifact classes; auxiliary/context-only artifacts; Stage2 target-discovery requirement> | <canonical input payload requirement> | <reviewed execution evidence root> | prepare_input / prepare_reference / ready_for_method_validation / repair_input_first / repair_reference_first / held_by_review | <short repair target or none> |
```

Rows selected as `ready_for_method_validation` have post-Stage1 canonical validation input evidence, post-Stage2 verifier-accepted reference artifact evidence, downstream-selectable build evidence, route-level backend load evidence, and reviewed output root needed for method harness validation.

`Expected Result Reference` records the analysis-problem-level result expectation and Stage2 discovery boundary. It should identify the expected result class, acceptable artifact classes, auxiliary/context-only artifacts, and evidence to produce. It must not freeze per-method result keys, object slots, paths, or command outputs before Stage2 inspects method-specific author workflow evidence.

The field is planning evidence only. It must not record observed outputs, runtime metrics, validation conclusions, or locally acquired artifacts before the reviewed execution step.

Bridge replay prerequisites are implementation-backed rows with verifier-confirmed action-path closure evidence, route-level backend load evidence, and ordered method-chain state handoff when the selected surface consumes prior-surface state. Bridge replay must not start from bridge planning alone. Bridge replay must not consume declaration-only, no-registration, no-import, or incomplete build rows.

Bridge replay starts from the reviewed canonical input for the first selected surface, not from a native-result-enriched object created only to extract structures, labels, or plots.

## Validation Planning Seed

| Method | Case / Tutorial / Vignette / Example Data | Original Data Description | Original Data Path Or Link | Original Result Description | Original Result Path Or Link | Original Method Interface / Workflow | Execution Surface Interface | Native Input Type | Execution-Surface Input Type | Native Output Type | Execution-Surface Output Type | Required Environment Build Output | Required Layer3/Layer4 Build Output | Planned Local Evidence Output Path | Planned Comparison Cue | Consistency Review Roles | Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`Original Data Path Or Link` and `Original Result Path Or Link` should contain a local path, an online link, or `unavailable`.

`Original Method Interface / Workflow` records the original repository function, script, notebook, tutorial workflow, or command locator used by the author case.

`Execution Surface Interface` records the reviewed Layer3 execution surface or parent-function callable target.

`Planned Local Evidence Output Path` records the post-Gate2 evidence output location for data acquisition, native execution, BioHarness bridge replay, and comparison records. It is a planned evidence location, not observed execution evidence.

`Planned Comparison Cue` records only minimal planning hints for later method harness validation, such as expected result class, comparable output level, shared cell/spot/observation-name key when known, and candidate metrics or descriptive checks when already reviewed. It must not record observed metric values, thresholds, consistency judgments, final comparison direction, language-boundary statements, or locally acquired artifacts.

`Consistency Review Roles` should use stable role names such as `agent`, `primary_human`, and `secondary_human`.

This table is a pre-Gate2 planning record. It does not record observed outputs, runtime metrics, consistency judgments, BioHarness validation evidence, runtime support, production readiness, or final support status.

Pre-Gate2 rows should not infer method-specific environment branches from text evidence.

## Blocked Case Handling

If an author case is not runnable because data are unavailable, instructions are incomplete, or reviewed environment build output is missing, record the blocker. Do not replace the case with synthetic data in this stage. Synthetic/minimal fixtures are out of scope for this stage.

Artificial negative case construction is out of scope unless the original repository case naturally exposes the failure. If the blocker is source-understanding related for an existing locator, route it to supplemental reading within the boundary above. If the blocker is environment-related, record the required environment build output and point to the relevant environment integration planning item, or request targeted environment planning repair. If the blocker requires execution, keep it as a runtime-observation need.

| Method | Case | Blocker Type | Evidence Basis | Routed To | Next Action |
| --- | --- | --- | --- | --- | --- |

Allowed blocker types:

- `data_unavailable`
- `instructions_incomplete`
- `environment_unresolved`
- `optional_dependency_unavailable`
- `source_gap`
- `runtime_failure`
- `resource_limit`

## Source Gaps Versus Runtime Observations

After integration-readiness audit closure, functional testing planning should not rediscover basic author-case assets. Basic case files, small-case code locators, data locators, author-result locators, and expected-output locators should come from the Author Case Asset Locator Table or audit-routed supplemental reading completed before closure.

Targeted supplemental reading during functional testing planning is allowed only when it starts from an existing locator and answers a stage-specific, bridge-specific, or expected-behavior question needed to select or interpret an author case. If the missing information is a basic asset locator, route it back to audit closure rather than treating it as downstream functional-test planning.

If a case is blocked by missing environment support, record the required reviewed environment binding record (`harness_environment.yaml`) or the planned/reviewed analysis-problem-level environment build output path and point to the relevant environment integration planning item, or request targeted environment planning repair. Environment build execution is entered through the Gate 2 human review table for the environment integration planning item.

When the reviewed environment binding/build output is missing, functional testing planning records the blocker only. It must not execute conda, author cases, or method workflows.

Conda solves, package installs, and import/load checks remain environment build checks handled through reviewed environment build execution. Author-case/native workflow execution uses the reviewed environment binding/build output and does not reclassify environment build checks as functional testing actions.

If the question requires execution, keep it as a runtime-observation need. Runtime-observation needs become evidence only after the method is run from a Gate 2-reviewed functional testing planning item using an original repository case, tutorial, vignette, or example workflow.

## Boundary

Functional testing planning uses original repository cases only.

Functional testing planning is method-specific.

Functional testing planning does not record observed outputs, observed pass/fail, runtime metrics, BioHarness bridge replay results, runtime support, production readiness, or final support status.
