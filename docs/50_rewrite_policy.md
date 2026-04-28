# Rewrite Policy

## Purpose

Record a working blueprint for how the substrate phase may later decide whether a tool should stay behind a thin adapter, move behind a stronger wrapper, or enter a rewrite track.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md).

## Current Working Direction

The current proposal evaluates rewrite decisions from an `agent-runtime` perspective rather than from software novelty alone. Rewriting is justified by execution reliability, validation quality, maintainability, or resource safety, not by architectural preference.

BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.

The v0.7.1 `rewrite_decision` separates `interface_standardization` from `algorithmic_rewrite`. This distinction is required because BioHarness can often normalize execution safely without changing the scientific algorithm.

## Interface Standardization

Interface standardization is encouraged and central to BioHarness:

- canonical AnnData / SpatialData / Seurat / SpatialExperiment input handling
- parameter normalization
- output mapping
- artifact layout
- logging
- typed failure translation
- provenance capture
- environment binding

These changes should make execution safer and more auditable without changing the scientific algorithm.

In a `MethodExecutionPlanningRecord`, `interface_standardization` should record the planned scope, rationale, validation required, evidence references, and confidence. Typical scope includes I/O conversion, parameter normalization, artifact export, failure translation, provenance, filesystem policy, and stable object-field assignment.

Interface standardization is expected during Layer 3/4 co-design. Agent-facing surfaces should hide low-level backend knobs while adapters standardize output names, directory layout, temporary directories, log policy, validation artifacts, and provenance.

## Algorithmic Rewriting

Algorithmic rewriting should be conservative. It includes reimplementing:

- graph construction
- model training
- loss functions
- Bayesian inference
- clustering logic
- post-processing algorithms

A convenient reimplementation is not automatically scientifically equivalent.

In a `MethodExecutionPlanningRecord`, `algorithmic_rewrite` must state whether algorithm core would be touched. If algorithm core is touched, fidelity comparison and explicit approval are required before implementation work. The planning record should name excluded algorithmic components when BioHarness intends to wrap or standardize around them rather than rewrite them.

Algorithmic rewrite requires explicit rationale and fidelity checks. It should default to hold/manual review unless scientific equivalence can be evaluated.

## Level A: Core Anchor

Mature ecosystem package. Do not rewrite.

Examples:

- AnnData
- Scanpy
- Squidpy
- SpatialData
- Seurat
- SpatialExperiment
- PyTorch

Use thin adapters, contracts, validators, and parameter templates.

## Level B: Thin Adapter

Use when a method has a stable API/CLI, clear inputs, clear outputs, and manageable dependencies.

## Level C: Strong Wrapper

Use when the method is scientifically useful but the public interface is not agent-friendly:

- notebook-only
- hard-coded paths
- unclear output names
- inconsistent logs
- manual preprocessing assumptions
- weak error semantics

Do not rewrite the algorithm; stabilize I/O, logging, artifacts, and validation.

Strong wrappers may be implementation-ready only after environment probe, minimal smoke fixture, and output schema observation. Static dependency risk alone is not enough to place a method on final environment hold.

## Level D: Compatibility Rewrite

Use when original code depends on old or conflicting packages, but the algorithmic logic can be safely migrated onto BioHarness backbone packages.

Require fidelity tests or at least documented comparison checks.

Compatibility rewrite requires comparison against original behavior before equivalence is claimed.

## Level E: Algorithmic Rewrite / Hold

Use for complex methods where rewriting risks changing scientific meaning.

Prefer:

- legacy capsule
- hold
- manual review required

Algorithmic rewrite should remain a hold/manual-review path unless scientific equivalence can be evaluated.

## Rewrite Signals

The following signals would raise rewrite priority if this blueprint is accepted:

- no stable CLI/API or no maintainable callable entry path
- severe environment fragmentation across methods in the same task family
- output cannot be validated in a reliable post-run step
- failure semantics are implicit, silent, or package-internal only
- the package exposes too much low-level detail for an agent to use safely

## Preferred Responses

| Condition | Preferred response |
| --- | --- |
| Mature package with a stable CLI/API and clear artifacts | Thin adapter plus fixed best-practice template |
| Callable path exists but parameters, outputs, or logs are inconsistent | Stronger wrapper with explicit surface contract |
| Environment fragmentation blocks reliable dispatch | Consolidate behind shared `EnvironmentProfile` definitions |
| Output cannot be validated or failure semantics remain opaque after wrapping | Candidate for rewrite or deeper internal reimplementation |

## Guardrails

- Layer 1 registry inclusion does not imply rewrite priority.
- Large, mature frameworks should not become rewrite targets by default.
- Rewrite should be justified by execution reliability, validation quality, or operator burden, not by abstract architectural preference.
- When the main pain point is interface control rather than algorithmic weakness, use a wrapper first.
- Rewrite classification can be proposed during Layer 3/4 co-design.
- Actual rewrite implementation should require an additional approval step or documented rationale.
- A compatibility rewrite should require fidelity checks or documented comparison checks.
- Any plan that touches algorithm core must trigger fidelity comparison and approval before implementation.
- A convenient reimplementation is not automatically scientifically equivalent.
- Topic-level rewrite or wrapper review should begin only after the topic completes the current Layer 2 artifact set and transition gate in [docs/90_roadmap.md](90_roadmap.md).
- The substrate phase should not interpret a convenient reimplementation as scientific improvement unless benchmark or validation evidence supports that claim.

## Deferred Questions

- Exact per-tool rewrite thresholds still depend on repository review and benchmark evidence.
- Acceleration-oriented rewrites remain in scope, but only after callable stability and validation quality are understood.
