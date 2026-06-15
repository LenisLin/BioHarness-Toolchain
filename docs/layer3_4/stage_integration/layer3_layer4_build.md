# Layer3 / Layer4 Build

## Purpose

This file defines Layer3 / Layer4 build for a Gate 2-reviewed `layer4_bridge_planning` item whose assigned step is `layer3_layer4_build`.

Layer3 / Layer4 build is a completion-directed implementation/build stage. The workflow, outputs, verifier, completion report, and build-specific acceptance checklist for this stage are defined by the `layer3_layer4_*` files in the Template Index.

## Inputs

- Gate 2 human review output with `approved_for_next_step` and `layer3_layer4_build`.
- Gate 1-reviewed parent function / execution surface.
- Method-to-parent Layer4 bridge planning file.
- Gate 1 planning-level alignment route.
- Parent-function standard contract, including canonical input, strict main output, semantic parameters, typed failures, validation expectations, and provenance expectations.
- Reviewed build-ready implementation contract for each build-required row.
- Repository-reading package, localized source files, or source locators referenced by reviewed native call sites.
- Reviewed compatibility rewrite handoff candidates when environment build or planning identifies bounded source changes for import, API, dependency, object-conversion, package-layout, or glue-code compatibility.
- Reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path when relevant.
- Storage/runtime conventions for implementation files, build outputs, import evidence, and evidence paths.

## Template Index

- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md`: build loop, implementation-start checks, lifecycle trace, closure inspection, and import boundary.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md`: action-path anti-surrogate audit rules consumed by build closure inspection and completion verification.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md`: Layer3-M config template produced during build.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md`: method-level implementation subagent prompt and handoff requirements.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md`: package layout record, dispatch log, completion matrix, per-row `build_output_result.yaml`, and downstream consumption boundary.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md`: lightweight audit output shapes for anti-surrogate evidence, method-chain lifecycle trace, publication index sanity, and per-row `build_audit.yaml`.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md`: method/global verifier prompt and verdict format.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_report.md`: completion report fields.
- `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md`: derived acceptance checklist.

## Build Boundary

Allowed build actions:

- create or modify Layer3 callable bindings;
- generate method-level `layer3_method_config.yaml`;
- create or modify Layer4 adapter, wrapper, compatibility rewrite, or algorithmic rewrite implementations within the reviewed route;
- implement config channel from Layer3 callable into method-owned Layer4 binding;
- implement object conversion, parameter mapping, output extraction, artifact handling, filesystem policy, environment binding, failure translation, validation hooks, and provenance hooks;
- record `config_consumption` evidence;
- read the reviewed repository-reading package and localized source files needed to confirm native signatures, source-observed call order, return objects, consumer patterns, mutations, private state, artifacts, and source-level behavior;
- compose reviewed native functions, classes, or script sections located in workflow-like source files, when they are used as source-confirmed call sites inside the implementation rather than executed as data-bound author workflows;
- implement runtime-only compatibility glue inside the reviewed route when preservation evidence is recorded;
- implement reviewed compatibility or algorithmic rewrite handoff candidates when they stay inside the reviewed route and preserve or explicitly review scientific-output-determining logic;
- dispatch method-level implementation subagents and collect method-level implementation evidence when the invocation assigns method subagents;
- run callable import checks, route-level backend load checks, and required selected bridge smoke checks under the reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path;
- for rows whose reachable Layer4 path crosses a language runtime, object-conversion boundary, backend initialization wrapper, package helper API, or runtime-only compatibility glue, record a selected bridge smoke check that enters the implemented Layer4 path and reaches the first selected native/glue boundary when feasible;
- prepare method-level verifier handoff records and the draft publication package for global completion verification;
- run independent read-only completion verification using `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md`.

Build scope boundary:

Layer3 / Layer4 build stays within the reviewed Gate 1 parent-function boundary, Gate 1 planning route, and Gate 2 assignment.

Build evidence uses reviewed source locators, reviewed environment evidence, implementation files, config production and consumption evidence, callable import checks, route-level backend load checks, selected bridge smoke-check evidence, and lifecycle trace evidence. Evidence class separation, lifecycle trace checks, action-path closure inspection, import boundaries, and workflow repair loops are defined in `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md`.

Source locators, environment evidence, callable import checks, backend load checks, lifecycle prose, and output observations support build confirmation; action-path closure comes from the registered Layer3 callable reaching the Layer4 implementation actions recorded for the row and passing the anti-surrogate audit defined in `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md`.

Selected bridge smoke checks are build-stage compatibility evidence. They verify that the implemented Layer4 bridge path can initialize the selected backend/API boundary under the reviewed invocation and is not immediately blocked by import-path drift, API drift, object-conversion failure, package helper API drift, or backend initialization failure. They do not establish runtime completion, strict-output production on validation data, author-case success, method-harness success, functional correctness, algorithmic equivalence, biological correctness, or production readiness.

Runtime execution evidence, author-case evidence, bridge replay evidence, validation evidence, data-localization evidence, and biological interpretation belong to their reviewed downstream phases.

Build reports state the evidence produced in this phase and reserve runtime support, functional correctness, final support status, production readiness, algorithmic equivalence, and biological correctness for later reviewed evidence.

## Completion Definition

Completion status is determined jointly by the build workflow, output contract, and completion verifier. `downstream_selectable`, publication gating, completion matrix fields, YAML records, lifecycle trace records, and completion report fields are defined in the Template Index documents.

A `layer3_layer4_build` invocation is complete only after final publication with global verifier `PASS` and publication-index sanity `pass`.

`FAIL_WITH_REPAIRS` is an internal builder repair-loop signal, not a completed invocation outcome, not a permitted fallback package status, and not a reason for the main implementation window to stop after implementation-start checks have passed. The executor must route each `FAIL_WITH_REPAIRS` packet back to the affected method subagent or final collation step, apply or assign the repair, rerun the affected implementation/check/verifier path, and continue the loop.

After implementation-start checks pass, stopping without `PASS` is allowed only for `STOP_BEFORE_IMPLEMENTATION`, unavailable method-subagent dispatch, external interruption, or a documented contradiction with the reviewed Gate1/Gate2 boundary that requires return to review.

## Non-Claims

Layer3 / Layer4 build does not establish native author-case success, BioHarness bridge replay success, runtime support, functional correctness, final support status, production readiness, algorithmic equivalence, or biological correctness. Those claims require later reviewed execution and validation evidence.
