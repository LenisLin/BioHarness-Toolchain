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

## Bridge Planning Output

This file produces pre-Gate2 `layer4_bridge_planning` evidence. It identifies the required mapping work, route issues, blockers, and validation needs for each reviewed `method x parent-function` route.

Bridge planning does not produce Layer3 / Layer4 build output. If Gate 2 assigns `layer3_layer4_build` to a reviewed bridge planning item, the post-Gate2 build workflow in `layer3_layer4_build.md` produces `build_output_result.yaml` and `build_audit.yaml`.

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

Environment constraints are context for bridge planning. They are not support proof and do not by themselves establish that a method can execute through the proposed bridge.

## Boundary

Layer4 bridge planning must not redefine parent functions. If a bridge exposes that a parent function is not implementable across methods without backend leakage, return that issue to parent-function alignment review.

A planning route is not a final support decision. Final support requires post-Gate2 build output, reviewed environment build output when relevant, author-case/bridge-replay evidence when relevant, and later validation/review.
