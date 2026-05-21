# Parent Functions

## Purpose

Layer 3 parent functions are stage-level execution functions extracted within a feature after same-feature multi-method evidence alignment.

A feature usually corresponds to a Layer 1 `Analysis Problem`. The feature is an analysis container, not a callable parent function.

A parent function is the interface the agent should understand for a confirmed execution stage. It is not a method-selection table, backend package API, notebook recipe, or adapter implementation.

## Construction Rule

Single-method code reading provides stage evidence; it does not define parent functions. Stage integration is the workflow that extracts parent-function candidates after methods under the same feature have completed code-stage evidence collection.

A parent-function candidate should define:

- one scientific action
- one canonical input contract
- one strict main output contract
- semantic parameters only when they are required for the action
- typed preflight failures
- typed output-contract failures
- validation and provenance expectations

Do not split parent functions by backend package, method family branch, GPU/CPU route, or optional method behavior. Those differences belong in Layer 2 selection, Layer 4 support planning, or the relevant downstream planning records.

## Coverage And Completeness Rule

A parent function does not need to be implemented by every retained method under the feature. It should be supported by a substantial cross-method subset, normally a majority of retained methods, when the shared scientific action is semantically coherent.

A retained method may support only a subset of the confirmed parent functions for the feature. This is acceptable when the unsupported parent functions are recorded as `not_applicable`, `layer4_internal`, `deferred`, `hold`, or otherwise routed with evidence.

The parent-function set for the feature should collectively cover the core functionality of retained methods that remain in the current analysis problem. A method whose core output semantics do not match the analysis problem should be routed out of the current feature rather than kept as a boundary-optional method.

## Execution Function Requirement

A parent function must perform a concrete execution-layer action, such as input preparation, structure construction, model fitting, inference, label assignment, output materialization, or another scientifically meaningful transformation.

Repository checks, readiness audits, environment build checks or reviewed environment build outputs, source locators, and validation asset discovery are not parent functions by themselves. They may appear as typed preflight failures, validation expectations, provenance requirements, or stage-integration evidence, but they should not be exposed as standalone agent-facing parent functions unless they execute a real transformation required by the analysis workflow.

## Strict Interface Policy

A parent function should reduce agent-side interpretation burden. It should not expose flexible output modes, raw backend file paths, package-private parameters, raw object-slot names, or low-level output namespaces.

For spatial transcriptomics execution-layer planning, the standard input direction is AnnData containing expression data, a spatial coordinate matrix, and optional image data. Layer 3 exposes the standard dataset semantics; Layer 4 converts those semantics to backend-specific forms.

The parent function should define one strict main output. Auxiliary method-native products may be stored as artifacts or downstream inputs, but they are not part of the parent function's public return contract unless explicitly promoted by a current design document.

Backend-native input and output differences are expected. They do not by themselves invalidate a parent function when the standard Layer 3 contract remains scientifically coherent. Layer 4 is responsible for mapping standard AnnData-centered semantics to backend-native objects, files, slots, tensors, scripts, or package APIs.

A method should be excluded, deferred, or routed to another feature when its core scientific output cannot satisfy the parent function's strict main output contract. Such semantic mismatches should not be hidden as adapter or wrapper work.

## Layer Boundary

Layer 2 decides when a method is scientifically appropriate.

Layer 3 defines stage-level parent-function candidates and confirmed parent functions within the feature.

Layer 4 records how a backend supports the parent function through adapters, wrappers, compatibility rewrites, algorithmic rewrites, or hold routes.
