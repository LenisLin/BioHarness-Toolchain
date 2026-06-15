# Layer 3/4 Rearchitecture Notes

## Current Decision State

`docs/layer3_4` represents the concrete execution-scheme layer for BioHarness. It is not a Layer 2 method-comparison extension and not a random-method planning exercise.

The core role is to translate a Layer 1 `Analysis Problem` or task family, after Layer 2 output, into feature-scoped stage-level parent-function candidates and Layer 4 support plans.

## Confirmed Direction

- A feature usually corresponds to a Layer 1 `Analysis Problem`, but the feature is not a callable parent function.
- Parent functions are extracted as stage-level execution functions after same-feature multi-method evidence alignment.
- A parent-function candidate exposes a strict agent-facing interface when promoted for that stage.
- A parent-function candidate uses one unified input type.
- A parent-function candidate uses one strict main output type.
- Method-specific variation belongs in Layer 4 bindings, environment plans, adaptation decisions, validation plans, and non-agent-facing artifacts.
- Flexible output modes should not be exposed at Layer 3 because they would push method-specific interpretation back onto the agent.
- Full method-specific evidence and records remain NAS artifacts; repo docs may contain reusable planning and review instructions.

## Parent Function Principle

Layer 3 parent functions are abstracted scientific actions at stage level. For example, `spatial_domain_identification` is the feature container for same-feature methods and later stage extraction, not itself the callable parent function.

Layer 2 remains responsible for scientific method selection. Stage integration extracts parent-function candidates from code-stage evidence. Layer 4 is responsible for satisfying confirmed or candidate stages through backend-specific support.

## Strict Input Direction

For spatial transcriptomics execution-layer planning, the standard input direction is AnnData with expression data, aligned observation/feature metadata, and spatial coordinates such as `adata.obsm["spatial"]`.

- Layer 3 exposes standard AnnData semantics, not backend-specific object slots.
- Optional image payloads may be carried in AnnData spatial records or platform-specific morphology image records with image provenance and scale/transform metadata.
- For image-aware routes, Layer 4 must distinguish spatial coordinate semantics from image pixel frame and must use reviewed transform evidence when converting coordinates to image patches.
- Layer 4 maps standard AnnData semantics to backend-specific AnnData, Seurat, SpatialExperiment, matrix/coordinate/image files, tensors, or other required forms.
- Method-required optional fields are handled by method eligibility checks, reviewed prepare-surface validation, or typed preflight failures.

Detailed contract design is deferred until the Layer 3/4 architecture is stabilized.

## Strict Output Direction

Each parent-function candidate should define one strict main output contract.

For `spatial_domain_identification`, the likely main output is domain-label assignment aligned to observations, spots, or cells. Methods whose primary output is topic programs, continuous gradients, semantic annotations, or reference-guided interpretations should not be silently folded into this parent output unless they directly satisfy the strict output contract. Such methods may require separate downstream functions, separate analysis problems, or `hold`.

Auxiliary artifacts may be recorded for audit, debugging, provenance, or downstream optional functions, but they are not part of the agent-facing parent function output.

## Core Document Responsibilities

`docs/layer3_4` should cover:

1. Parent-function and Layer 3 surface design through same-feature stage integration.
2. Environment configuration and reviewed build-output integration.
3. Layer 4 support through adapters, wrappers, rewrites, or hold routes.
4. Evaluation of BioHarness-supported execution against native method behavior using bounded author-provided cases first, with later validation fixtures only when explicitly approved, and with stated versions, seeds, metrics, and tolerances.
5. Operational notes for NAS result locations, conda/environment roots, artifact layout, and storage boundaries.
6. README navigation.
7. Supporting design documents, templates, checklists, and downstream planning/review formats.

## Cleanup Direction

Existing broad or draft-heavy Layer 3/4 files have been removed from the current working tree before rebuilding the directory. Use Git history when older pre-rearchitecture material is needed for reference.

Current Gate 1 planning language should use these route values:

- `adapter`
- `wrapper`
- `compatibility_rewrite`
- `algorithmic_rewrite`
- `hold`

Historical terms such as `adapter_candidate_status`, `candidate_status`, `environment_candidate`, `rewrite_policy: wrapper_before_rewrite`, `interface_rewrite_needed`, and `algorithmic_rewrite_needed` should not remain current design language.

## Open Next Step

Before method-specific design resumes, stabilize the compact Layer 3/4 document set around parent functions, stage integration, environment planning, Layer 4 support, evaluation, storage/runtime conventions, downstream planning records, and Gate 2 human review tables.
