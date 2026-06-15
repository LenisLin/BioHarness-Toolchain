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

For spatial transcriptomics execution-layer planning, the standard input direction is AnnData containing expression data, aligned observation/feature metadata, and a spatial coordinate matrix such as `adata.obsm["spatial"]`. The spatial coordinate matrix is not assumed to be in the pixel frame of any selected image resolution. The AnnData may also carry optional spatial image payloads using Scanpy/Visium-style fields such as `adata.uns["spatial"][library_id]["images"][img_key]`, platform-specific morphology image records, and associated scale or transform metadata. Layer 3 exposes these standard dataset semantics; Layer 4 converts them to backend-specific objects, files, tensors, image patches, or package APIs.

For image-aware routes, the reviewed contract must record coordinate semantics separately from image pixel frame. For Visium and Xenium image-aware routes, the reviewed evidence must record image source, image frame, and coordinate-to-image transform evidence before the row can be published as downstream-selectable. Layer 4 is responsible for applying the reviewed transform from standard AnnData semantics, canonical input evidence, or reviewed prior state to backend-specific image, patch, or tensor inputs. Raw spatial coordinates must not be treated as pixel coordinates in the selected image resolution unless reviewed evidence explicitly supports that mapping.

Input-format compatibility before the first reviewed parent function is a separate ingestion or data-localization boundary unless the current Gate1 closure explicitly includes it. A Layer3/Layer4 build must not silently widen the public callable input contract to raw file locators or backend-private loader controls.

The parent function should define one strict main output. Auxiliary method-native products may be stored as artifacts or downstream inputs, but they are not part of the parent function's public return contract unless explicitly promoted by a current design document.

A strict main output is the product of the current parent function. It must not be required as a pre-existing input for that same parent function. It may become valid state for a later parent function in the reviewed execution-surface chain.

Backend-native input and output differences are expected. They do not by themselves invalidate a parent function when the standard Layer 3 contract remains scientifically coherent. Layer 4 is responsible for mapping standard AnnData-centered semantics to backend-native objects, files, slots, tensors, scripts, or package APIs.

A method should be excluded, deferred, or routed to another feature when its core scientific output cannot satisfy the parent function's strict main output contract. Such semantic mismatches should not be hidden as adapter or wrapper work.

## Layer Boundary

Layer 2 decides when a method is scientifically appropriate.

Layer 3 defines stage-level parent-function candidates and confirmed parent functions within the feature.

Layer 4 records how a backend supports the parent function through adapters, wrappers, compatibility rewrites, algorithmic rewrites, or hold routes.
