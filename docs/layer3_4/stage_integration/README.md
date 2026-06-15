# Stage Integration

## Purpose

Stage integration is the post-code-reading, same-feature workflow for auditing method packages, routing targeted supplemental reading, extracting stage-level parent-function candidates, and preparing downstream integration after human review.

## Scope

This package starts after method-specific repository-reading packages have produced first-round evidence packages. It covers feature-level integration-readiness audit, targeted supplemental reading, parent-function extraction, human alignment review, three downstream planning files, Gate 2 downstream planning review, Gate 2 human review table, and post-Gate2 execution/build workflows and build outputs.

The current workflow is:

```text
Per-method repository localization and repository-reading
  -> produce per-method repository-reading evidence packages

Feature-level stage integration consumes the evidence packages
  -> integration-readiness audit
  -> audit-closing remediation loop when needed
  -> agent parent-function extraction
  -> human parent-function / execution-surface alignment review (Gate 1)
  -> Gate 1 remediation loop when surface or route evidence requires repair
  -> agent downstream execution planning
       -> method-to-parent Layer4 bridge planning
       -> environment integration planning
            -> Environment Text Compatibility Triage
            -> Method Dependency Groups
            -> Environment Assembly Order and Split Triggers
            -> analysis-problem-level environment build planning by default
            -> Environment Build Plan
       -> functional testing planning
  -> Gate 2 downstream planning review
  -> targeted planning repair or return-to-Gate-1 loop when a reviewed planning item requires revision
  -> Gate 2 human review table for current in-scope planning items
  -> post-Gate2 execution/build according to Gate 2 assigned steps
       -> environment build execution
            -> harness_environment.yaml
            -> environment_build.yaml
            -> environment_build.jsonl
       -> Layer3 / Layer4 build
            -> layer3_layer4_build_completion_matrix.tsv
            -> build_output_result.yaml
            -> build_audit.yaml
            -> layer3_method_config.yaml
            -> callable import evidence, route-level backend load evidence, and selected bridge smoke-check evidence when required
       -> author-case/native workflow execution with BioHarness bridge replay
  -> post-implementation validation
  -> production-readiness review
```

Each downstream planning file should provide enough domain-specific planning detail for Gate 2 to review whether the item can enter its post-Gate2 execution/build workflow. These planning details belong in the relevant planning files or attached planning packages, not in a separate post-planning aggregation artifact.

Gate 2 human review output records which current in-scope planning items enter post-Gate2 steps. Execution/build actions use the Gate 2-reviewed planning item, the assigned step, the output path, and the Gate 2 human review table.

Environment and validation locator gaps should be closed before downstream execution planning. Parent-function and Layer4 code-centric questions may still trigger targeted supplemental reading after audit when they are tied to a specific stage or bridge planning record. Runtime, download, environment build/check, and author-case actions remain outside repository reading and use the next steps assigned by Gate 2 downstream planning review.

Gate 1 execution surfaces are the human-reviewed analysis-problem-scale surface set; downstream planning integrates that result.

Environment integration planning occurs during downstream execution planning before Gate 2. It includes Environment Text Compatibility Triage, Method Dependency Groups, selected dependency boundaries, Environment Assembly Order, Split Triggers, and one analysis-problem-level Environment Build Plan by default. Gate 2 reviews filled environment integration planning records and records the review result plus assigned step through the Gate 2 human review table. Environment build execution occurs when a reviewed environment integration planning item has `approved_for_next_step` and Gate 2 assigns `environment_build_execution`. The reviewed build output directory must contain the core outputs `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl`.

`harness_environment.yaml` is the reviewed environment binding record, `environment_build.yaml` is the pure conda YAML for reproducibility, and `environment_build.jsonl` records actual environment build events in reviewed plan step order.

Layer3 / Layer4 build occurs after Gate 2 assigns `layer3_layer4_build` to a reviewed Layer4 bridge planning item. The build workflow is defined in `layer3_layer4_build.md`. A completed build follows the control-flow specification in `layer3_layer4_build.md`: build-required rows become downstream-selectable only after reachable Layer3-to-Layer4 action-path closure, strict-output contract closure, final callable-import, route-level backend-load, selected bridge smoke-check, lifecycle, per-row result, and audit evidence collation, publication index sanity pass on the draft completion matrix, global verifier pass on the draft publication package, and final publication. Reviewed held rows remain held. Completed outputs include the root `layer3_layer4_build_completion_matrix.tsv`, per-row `build_output_result.yaml`, per-row `build_audit.yaml`, method-level `layer3_method_config.yaml`, config consumption evidence, callable import evidence, route-level backend-load evidence, selected bridge smoke-check evidence when required, lifecycle evidence, and publication index sanity evidence. Later execution and replay consume downstream-selectable rows only when the referenced environment evidence includes route-level backend load evidence for the selected Layer4 route. The build output does not establish runtime support, functional correctness, final support status, algorithmic equivalence, or biological correctness.

Author-case and validation preparation occur after the reviewed functional-testing planning item and required build/environment evidence are available. Preparation records case-data localization, canonical validation input, and reference evidence.

Method validation occurs under `docs/layer3_4/method_validation/`. It consumes prepared inputs, reference evidence, reviewed environment evidence, and downstream-selectable Layer3/4 rows to run method-level BioHarness harness tests.

Terminal method validation failures are recorded only for method harness validation attempts. Input-preparation gaps may remain repair states under the input-preparation workflow. Stage2 reference-preparation gaps are verifier repair evidence until the method result is accepted as `REFERENCE_READY` or `REFERENCE_FAIL` with complete `failure_evidence`. Runtime work uses the workspace conventions in `storage_and_runtime.md`. Output consistency review reports case-level agreement or reviewed difference for the selected author case.

## Inputs

- Method-specific repository-reading package roots.
- Repository localization outputs and local source-root provenance.
- Integration-readiness audit outputs.
- Completed supplemental-reading outputs when routed by the audit or later stage-integration steps.
- Code Planner stage-inform groups.
- Code Function-Family Reader outputs.
- Output/Validation cues when needed for result-assignment or artifact interpretation.
- Environment Config Reader outputs for environment integration.
- Package review gaps when they affect extraction, bridging, or testing.

## Non-Inputs

- Layer 2 method-selection comparisons.
- Filled method-specific evidence copied into repo docs.
- Runtime evidence unless a later reviewed execution pass imports it.
- Production-readiness claims.

## Reading Order

1. `integration_readiness_audit.md`
2. `supplemental_reading.md`
3. `parent_function_extraction.md`
4. `parent_stage_alignment_review.md`
5. `method_to_parent_layer4_bridge.md`
6. `environment_integration_planning.md`
7. `functional_testing_planning.md`
8. `downstream_planning_review.md`
9. `environment_build_execution.md`
10. `layer3_layer4_build.md`
11. `author_case_execution.md`

Phase-local templates live beside their owning stage under `*_templates/` directories. Cross-stage invocation and acceptance templates live under `docs/layer3_4/stage_integration/templates/`.

## Human Gates

Gate 1 is `parent_stage_alignment_review.md`. It reviews rough stage-level parent-function candidates as execution-surface candidates. Gate 1 confirms the semantic boundary, checks cross-method coverage, reviews method x surface planning-level alignment routes, and either promotes candidates to downstream bridge planning, routes them to repair, returns them to extraction, marks them internal or optional, or defers them.

Gate 1 may confirm planning-level alignment routes: `adapter`, `wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, or `hold`. These routes are not final Layer4 support decisions and do not permit implementation or runtime execution.

Gate 2 is `downstream_planning_review.md`. It reviews current in-scope planning items from three downstream planning areas: method-to-parent Layer4 bridge planning, environment integration planning, and functional testing planning. Planning items that require revision are routed to targeted planning repair or returned to Gate 1 when the issue affects parent-function, execution-surface, or method x surface route boundaries. Gate 2 human review output assigns post-Gate2 steps for planning items that have sufficient evidence and clear boundaries.

Gate 2 assigned steps are `environment_build_execution`, `layer3_layer4_build`, and `author_case_native_workflow_and_bridge_replay`. These steps are handled by `environment_build_execution.md`, `layer3_layer4_build.md`, and `author_case_execution.md`, respectively. Gate 2 repair routing values are `targeted_planning_repair` and `return_to_gate1`.

Post-implementation coherence review may be recorded as ordinary review evidence when required; it is not a named gate in this workflow.

Gate decisions and review status values are routing, alignment, or downstream planning review records. Later execution/build stages and validation stages produce their own evidence records.

## Supplemental Reading Loop

Stage integration may identify decision-relevant source gaps after the initial method repository-reading package is complete.

Supplemental reading is an integration-triggered second pass defined in `supplemental_reading.md`. It should be targeted and should answer a specific integration question, such as parent-function candidate classification, Layer4 mapping, output normalization, failure translation, or functional-test questions tied to an already recorded author-case locator. After audit closure, supplemental reading should not rediscover basic validation assets such as case files, small-case code, data locators, or author-result locators. It should not restart full repository reading, run the method, install dependencies, or claim runtime support.

Gate 1 remediation repairs surface-level or route-level static evidence gaps. It may support re-review of affected parent-function boundaries, execution-surface scope, or method x surface planning routes. It does not implement adapters or wrappers, run methods, perform environment build execution, or observe runtime outputs.

Targeted planning repair after Gate 2 addresses narrow defects in reviewed planning records. Allowed domains are `layer4_bridge_planning`, `environment_integration_planning`, and `functional_testing_planning`. Repaired planning records return to Gate 2 downstream planning review for review result and assigned step.

Supplemental reading outputs remain method-specific evidence and should be stored in NAS with the feature-level integration package.

## Storage Boundary

Repository files in this directory are reusable instructions and templates. Filled method-specific and feature-level integration evidence belongs in the NAS results workspace.

## Non-Claims

Stage integration instructions do not by themselves select final implementation support states, claim runtime support, establish production readiness, or validate biological correctness. Build/execution actions named in this workflow remain bounded evidence-producing actions until later validation and review support stronger claims. Layer3 / Layer4 build output supports later harness/runtime loading and bridge replay only through completion matrix rows marked `downstream_selectable=true` and backed by referenced environment evidence with route-level backend load evidence for the selected Layer4 route.
