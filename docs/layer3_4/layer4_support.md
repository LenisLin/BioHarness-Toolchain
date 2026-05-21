# Layer 4 Support

## Purpose

Layer 4 records how a concrete backend satisfies a strict Layer 3 parent function.

Layer 4 is implementation-facing. It may include backend entrypoints, object conversion, parameter mapping, output extraction, artifact handling, filesystem policy, environment binding, failure translation, and validation hooks. It should not be exposed to the default agent context.

## Gate 1 Planning Routes

Gate 1 records planning-level alignment routes for each `method x parent function` pair. These routes explain the expected bridge-planning posture. They are not final Layer 4 support decisions and do not claim entry into Layer4 build, runtime support, production readiness, or biological correctness.

- `adapter`
- `wrapper`
- `compatibility_rewrite`
- `algorithmic_rewrite`
- `hold`

If a route is not established after evidence review, use `hold` with a concrete reason. Do not preserve unknown route states after Gate 1 closure.

## Planning Route Versus Implementation Status

A planning route is not an implementation status.

`adapter`, `wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, and `hold` describe the expected bridge-planning posture for a `method x parent function` pair. They do not indicate that an adapter, wrapper, callable parent function, reviewed environment build output, runtime path, or tested support path exists.

Downstream planning records should preserve this distinction by recording:

- `support_decision_status: planning_hypothesis`
- `planning_route: adapter | wrapper | compatibility_rewrite | algorithmic_rewrite | hold`
- `implementation_status: not_implemented`

Actual Layer 4 build begins only after Gate 2 downstream planning review assigns `approved_for_next_step` to the relevant `layer4_bridge_planning` record with `layer3_layer4_build` as a named next step. That review should use the Layer4 bridge planning record, environment integration planning record when relevant, validation/native-output planning record when relevant, and output-contract expectations.

Gate 2 downstream planning review routes reviewed planning records to their next steps. Final Layer 4 support still requires implementation evidence, reviewed environment build output, validation evidence, and output-contract observation.

## Layer3 / Layer4 Co-Design Boundary

Layer 3 defines the standard semantic contract. Layer 4 defines how a concrete backend satisfies that contract.

Backend-specific objects, slots, package functions, scripts, tensors, file layouts, and parameter names belong in Layer 4. Their presence is expected and should not widen the parent-function interface.

Layer4 support planning should distinguish three cases:

- native input/output shape differs from the standard contract but can be mapped without changing the scientific meaning;
- execution compatibility or dependency issues require wrapper or bounded rewrite planning;
- core scientific output semantics do not satisfy the parent function and should be routed to hold, exclusion, or another feature.

## Planning-Level Alignment Routes

Parent-function extraction and Gate 1 may record planning-level alignment routes for each `method x parent function` pair. These routes explain how the method is expected to connect to the execution surface during downstream bridge planning.

Use the current Gate 1 planning-route vocabulary: `adapter`, `wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, or `hold`.

A planning-level alignment route is not a final Layer4 support decision. It does not claim entry into Layer4 build, runtime support, production readiness, or biological correctness.

Semantic fit should be assessed before route selection. A method with a fused native stage may still fit a parent-function surface when the scientific execution role is shared. The downstream bridge then determines the concrete mapping.

## Functional Coverage

For downstream planning review, every required parent-function stage in a selected method path must have an explicit planned Layer 4 handling status. During Gate 1 and Gate 2 this may still be a planning route or held/deferred item; it is not implementation evidence. Typical stages include:

- input check
- method-local preprocessing
- core structure construction
- model fit or inference
- output assignment
- artifact export
- final validation
- visualization or report generation when required

A method does not need to support every confirmed parent function. Unsupported stages should be explicitly marked as not applicable, internal, deferred, held, or excluded with rationale. Required stages for a selected method path must not be silently omitted.

No required stage should be silently omitted. Critical unresolved backend entrypoints, output mappings, or parameter mappings should trigger planning repair or block entry into the corresponding Layer4 build named next step.

## Rewrite Boundary

Interface standardization is expected. It may include input conversion, parameter normalization, output mapping, logging, artifact handling, provenance capture, and typed failure translation.

Compatibility rewrites target non-core execution or integration code. Algorithmic rewrites touch scientific-output-determining logic and require explicit scope, comparison targets, validation plans, and review before implementation.
