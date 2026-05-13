# Substrate Architecture

## Purpose

This document defines the current four-layer substrate architecture used by BioHarness-Toolchain to organize spatial transcriptomics downstream execution planning.

It explains how task routing, method knowledge, execution surfaces, and backend implementation are kept separate. Agent brain visibility is defined separately in [Agent Visibility](agent_visibility.md).

## Status Boundary

This architecture is a blueprint for organizing documentation, contracts, surface manifests, method-planning records, and future implementation work. It is not, by itself, a runtime dispatcher, a production adapter set, or evidence that any execution surface is implemented.

Implementation-backed status must come from explicit runtime code, accepted implementation records, executable manifests, validation reports, or another current authority document. A pilot, example, schema, or planning record does not establish production readiness.

## Four-Layer Architecture

BioHarness separates four concerns that are often mixed together during ad hoc tool use:

| Layer | Main responsibility | Typical artifact | Execution meaning |
| --- | --- | --- | --- |
| Layer 1 | Route the analysis problem or task family. | Task catalog or problem card. | No execution claim. |
| Layer 2 | Support method selection inside the selected task family. | Method knowledge pack, feature table, decision tree. | No runtime interface claim. |
| Layer 3 | Define the stable execution surface after method selection. | `ExecutionSurfaceSpec` or equivalent surface manifest. | Execution planning, not backend internals. |
| Layer 4 | Bind the surface to concrete backend code, wrappers, capsules, or rewrites. | `BackendAdapterSpec`, adapter, wrapper, rewrite, or implementation record. | Concrete implementation layer. |

Layer 1 and Layer 2 are knowledge layers. They organize what kind of analysis is being requested and which method family or method is scientifically appropriate. They do not define commands, callable signatures, environment bindings, backend adapters, or implementation readiness.

Layer 3 is the first machine-readable execution-planning layer. It should express the stable semantic action available after method selection: expected inputs, bounded parameters, expected outputs, validation expectations, provenance expectations, and typed failure behavior.

Layer 4 is the implementation-facing layer. It records how a selected surface is actually satisfied by backend packages, scripts, adapters, wrappers, compatibility rewrites, or algorithmic rewrites. Layer 4 may contain backend functions, paths, parameter mappings, file I/O, environment evidence, and failure translation.

## Layer Responsibilities

### Layer 1

Layer 1 routes an incoming request to an `Analysis Problem` or task family. Its purpose is to keep the first routing choice compact and scientifically meaningful.

Layer 1 registry inclusion records that a method or task family exists in the current evidence base. It does not imply core candidacy, execution readiness, stable-surface status, or rewrite priority.

### Layer 2

Layer 2 answers `when to choose`. It carries method knowledge for a task family, including method comparison, selection rules, assumptions, topic-specific decision trees, and branch-local evidence.

Layer 2 should not become a command manual. It should not define parameter lists, input schemas, execution surfaces, environment bindings, adapter internals, final callable signatures, default-method claims, or runtime-support claims.

### Layer 3

Layer 3 converts a selected task or method context into an execution surface. Its role is to make heterogeneous backend methods appear as stable scientific actions where that abstraction is supported by the Layer 2 evidence and later engineering review.

Layer 3 is not raw package documentation and not a backend API. It should not encode backend function names, backend file paths, implementation call graphs, package-private parameters, temporary paths, unsafe memory flags, or low-level output namespaces.

### Layer 4

Layer 4 records the concrete binding between a Layer 3 surface and backend execution. It may include adapters, wrappers, compatibility rewrites, algorithmic rewrites, environment-specific entrypoints, parameter mappings, input conversion, output mapping, artifact handling, and typed failure translation.

Layer 4 supports implementation, debugging, and audit by recording concrete backend evidence.

## Layer 2 To Layer 3/4 Boundary

Layer 2 scientific suitability does not automatically imply Layer 3 promotion. A selected method can be appropriate for a scientific task while still lacking the repository evidence, environment evidence, input/output mapping, or validation plan needed for execution-surface planning.

Crossing into Layer 3 means the topic or method is eligible for execution-surface planning. It does not freeze a backend adapter, implementation order, environment capsule, rewrite decision, or production-ready callable signature.

Layer 3 and Layer 4 must remain separate even when they are planned from the same method evidence. Layer 3 describes the stable execution surface. Layer 4 describes backend-specific implementation evidence and binding behavior. The detailed co-design workflow belongs in `docs/layer3_4/`.

## Cross-Cutting Substrate Supports

Several substrate concerns support the four layers without becoming additional layers.

- Contracts connect layers by making input, output, surface, adapter, validation, and run-state expectations explicit. Contract schemas are blueprint artifacts unless an implementation-backed authority promotes them.
- Environment strategy constrains dependency handling and resource assumptions. Environment profiles or capsules are planning objects until backed by lockfiles, containers, import checks, fixture runs, or equivalent runtime evidence.
- Adaptation policy governs whether a backend should be connected through a thin adapter, stronger wrapper, compatibility rewrite, algorithmic rewrite, legacy capsule, or hold decision. Interface standardization can be appropriate without changing the scientific algorithm; algorithmic rewrite requires stronger evidence and validation.
- Validation and provenance define whether a run result is usable as BioHarness output. Runtime completion alone is insufficient. The substrate should distinguish preflight checks, runtime checks, post-run checks, output-contract checks, provenance capture, and manual-review triggers.
- Evaluation design measures whether the substrate improves execution reliability, repair behavior, provenance completeness, and context burden. It should not be presented as proof of biological correctness unless the evaluation design supports that claim.
