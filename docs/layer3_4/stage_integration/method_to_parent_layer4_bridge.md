# Method-To-Parent Layer4 Bridge

## Purpose

This file defines how to map each method's native code paths to human-reviewed parent-function execution-surface candidates.

Bridge planning starts after Gate 1 parent-function alignment review. It uses reviewed parent-function candidates as the target boundary; it does not replace human alignment review or create final parent functions.

Bridge planning consumes Gate 1 confirmed execution surfaces and their method x surface planning-level alignment routes. It expands those route hypotheses into concrete entrypoint, input, state, parameter, output, artifact, failure, and provenance mappings.

It should not redefine the parent function to match one backend's native API.

Downstream bridge planning carries Gate 1 planning routes forward. It may identify planning-record gaps for Gate 2 downstream planning review, but it must not revise parent-function definitions or Gate 1 routes.

Only Gate 1 candidates marked `promote_to_downstream_bridge` should enter this bridge planning pass. Candidates routed to repair, supplemental reading, parent extraction, internal handling, optional support, or deferral should not be mapped as bridge targets until the required review path closes.

## Inputs

- Human-reviewed parent-function candidates from `parent_stage_alignment_review.md`.
- Integration-readiness audit outputs and completed supplemental-reading outputs when they affect bridge mapping.
- Code Function-Family Reader outputs.
- Output/Validation cues.
- Environment constraints as context only.

## Bridge Table

Use one row per `method x parent-function` mapping where possible. The table may record multiple native entry points for a method when they jointly support the same reviewed parent-function candidate.

| Method | Parent Function | Gate 1 Alignment Route | Standard Contract Element | Native Entry Points / Objects | Native Input / Output Shape | Required Mapping Work | Route Revision Needed? | Blockers | Validation Need |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

If bridge planning shows that a promoted execution-surface boundary is unstable or backend-shaped, the Gate 2 review status for the affected planning record should be `return_to_gate1` rather than silently redefining the parent function.

## Build-Ready Implementation Contract Table

For rows intended for `layer3_layer4_build`, bridge planning should record the implementation contract needed by the build executor.

Bridge planning should preserve source/control cues needed for build-time Layer3-M config generation. It does not freeze concrete Layer3-M variable names, default values, or binding targets.

| Method | Parent Function | Gate 1 Alignment Route | Native Call Sequence | Native Call Sites | Source Locators | Signature Binding | Canonical Input Or Prior-State Source | Private State Policy | Strict Output Mapping | Artifact Policy | Result Selection Policy | Method-Chain State Handoff | Compatibility Rewrite Handoff Candidate | Gate 2 Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Wrapper rows require a concrete native call sequence and call sites. Rows that select among native result rows, labels, clusters, embeddings, or fitted outputs require a result selection policy. Structure-producing rows require a private state policy and strict output mapping.

The build-ready implementation contract identifies enough native call sites and source locators for the later build executor to open the original implementation, confirm signatures, inspect return values and mutations, and bind private state/output behavior.

`Source Locators` must identify a concrete source evidence root or an explicitly named source-root field, plus repo-relative file paths and function, class, script section, or call-site anchors when available. If a filled planning artifact uses shorthand paths, it must define the base root in the same artifact. Source locators must not depend on the executor's current working directory, prompt location, or implicit path inference.

Workflow-like source files, scripts, or notebook-exported files may be source locators when they contain reviewed native call sites. Recording such files as source locators authorizes source reading and wrapper composition of reviewed native functions, classes, or call-site logic; it does not authorize running data-bound author workflows during Layer3/Layer4 build.

A wrapper row names the native calls that perform the current parent-function action, along with the prior-surface state consumed and the strict output produced.

For methods with multi-surface execution, bridge planning records native action ownership across the method chain. A scientific-output-determining native action should have one owner surface in the reviewed chain. Later surfaces may consume the owner surface's private state or public strict output, but should not re-execute the same output-determining native action unless the planning record explicitly documents that the repeated call is non-output-determining, idempotent, and required by the native API boundary.

If the same fitting, training, MCMC, clustering, postprocessing, label-assignment, or other output-determining native action appears necessary in more than one surface, the row should return to planning repair rather than entering `layer3_layer4_build` as ready.

A structure-producing row records private state policy and strict output mapping. A result-producing row records result selection policy. A method with multi-surface execution records method-chain state handoff across rows.

Private state policy must identify the reviewed source or prior-surface handoff for private state required to produce the strict output. If bridge planning cannot identify a reviewed source for private or prior state that appears scientific-output-determining, the row should return to the relevant review/planning repair path rather than entering `layer3_layer4_build` as ready.

When a method requires an optional spatial image payload for scientific-output-determining behavior, the build-ready implementation contract records the ST image alignment contract. Valid image sources are canonical image-aware AnnData fields, external morphology image records with reviewed provenance, or reviewed prior-surface state.

For image-aware routes, the ST image alignment contract records:

- `platform_family`: `Visium | Xenium | other | unknown`;
- `spatial_coordinate_semantics`: spot, cell, bin, array, physical, image-pixel, or unknown;
- `coordinate_source`: AnnData field or reviewed prior state;
- `image_source`: AnnData spatial image, external morphology image, or reviewed prior state;
- `image_key_or_resolution`: `fullres | hires | lowres | morphology_pyramid_level | other`;
- `image_shape`;
- `coordinate_to_image_transform_evidence`;
- `patch_or_image_state_handoff`.

For Visium image-aware routes, if the route uses `hires` or `lowres` images and the coordinates are in the full-resolution pixel frame, Layer 4 must scale coordinates with the matching `tissue_hires_scalef` or `tissue_lowres_scalef`. `array_row` and `array_col` must not be used as image crop coordinates unless reviewed mapping evidence exists.

For Xenium image-aware routes, the contract must not assume Visium scalefactor semantics. When morphology image patches are output-determining, the contract requires Xenium morphology image coordinate or physical-to-pixel transform evidence.

For other platforms, the contract records coordinate semantics. Missing H&E or morphology alignment evidence is not by itself a blocker unless the reviewed route selects an image payload as scientific-output-determining behavior.

A compatibility rewrite handoff candidate states the non-core compatibility issue handed to build, such as import path drift, API drift, dependency compatibility, object conversion, package layout, or integration glue. Source changes that affect scientific-output-determining logic are represented through reviewed `algorithmic_rewrite` scope.

## Bridge Planning Output

This file produces pre-Gate2 `layer4_bridge_planning` evidence. It identifies the required mapping work, route issues, blockers, and validation needs for each reviewed `method x parent-function` route.

Bridge planning records reviewed instance facts for later build: method x surface route, native call evidence, source locators, source/control cues for build-time Layer3-M config generation, required mapping work, private-state policy, strict output mapping, artifact policy, result selection policy, method-chain handoff, compatibility rewrite handoff candidates, reviewed output roots, and build-required or held status. It does not define Layer3/Layer4 build completion, verifier cadence, publication gating, completion matrix schema, per-row YAML schema, or downstream selectability rules; those are defined by `layer3_layer4_build.md` and the completion verifier prompt.

Bridge planning does not produce Layer3 / Layer4 build output. If Gate 2 assigns `layer3_layer4_build` to a reviewed bridge planning item, the post-Gate2 build workflow in `layer3_layer4_build.md` produces root `layer3_layer4_build_completion_matrix.tsv`, per-row `build_output_result.yaml`, per-row `build_audit.yaml`, callable import evidence, route-level backend load evidence, and verifier-confirmed action-path closure evidence under the current `layer3_layer4_build.md` workflow.

Bridge planning should make clear whether the later build needs object conversion, parameter mapping, output extraction, artifact handling, filesystem policy, environment binding, failure translation, validation hooks, or provenance hooks.

## Planning Route Language

Allowed Gate 1 planning routes:

- `adapter`
- `wrapper`
- `compatibility_rewrite`
- `algorithmic_rewrite`
- `hold`

These are planning routes only. They are not final support decisions.

A Gate 1 alignment route is the starting hypothesis for bridge planning. Bridge planning may identify that a Gate 1 route or surface needs re-review, but it must record that as a Gate 2 review need rather than revising the route in place.

Do not treat a Gate 1 route as final support. Final support decisions require later implementation-facing evidence and review.

Input/output standardization is normal Layer 4 mapping work under the Gate 1-confirmed planning route. Bridge planning should describe the required mapping work, orchestration, state management, output extraction, artifact handling, and failure translation for that inherited route. It must not select a different planning route in place.

Dependency or platform incompatibility should be recorded as bridge or environment planning evidence under the inherited Gate 1 route. If that evidence suggests that `compatibility_rewrite`, `algorithmic_rewrite`, `hold`, or another route change is needed, route the affected planning record back to Gate 1 review rather than revising the route inside bridge planning.

A semantic output mismatch should not be converted into an adapter, wrapper, or rewrite hypothesis. It should route back to Gate 1, `hold`, or removal from the current feature.

## Bridge-Triggered Source Gaps

If bridge planning depends on unresolved source behavior, record a supplemental reading request through `supplemental_reading.md` before forming a stronger support hypothesis.

Do not use unresolved source behavior to justify a stronger adapter, wrapper, rewrite, or hold route.

After Gate 2 approval, source reading continues inside `layer3_layer4_build` for implementation details inside the reviewed route. Bridge planning leaves enough call-site and source-locator evidence for build execution to continue from the reviewed method path.

Environment constraints are context for bridge planning. They are not support proof and do not by themselves establish that a method can execute through the proposed bridge.

## Boundary

Layer4 bridge planning must not redefine parent functions. If a bridge exposes that a parent function is not implementable across methods without backend leakage, return that issue to parent-function alignment review.

A planning route is not a final support decision. Final support requires post-Gate2 build output, reviewed environment build output when relevant, author-case/bridge-replay evidence when relevant, and later validation/review.
