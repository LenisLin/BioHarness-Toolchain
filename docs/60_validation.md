# Validation

## Purpose

Record a working blueprint for the quality gates that future execution surfaces may need before BioHarness can treat a run as trustworthy.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md).

## Current Working Direction

The current blueprint treats substrate validation as a three-stage gate rather than a single success flag. Every bounded task should be able to explain what was checked before execution, during execution, and after artifacts are produced.

Validation is substrate-level quality control. It does not replace scientific review or prove that a biological interpretation is correct.

## `validation_runtime_plan` In Method Planning

`MethodExecutionPlanningRecord v0.7.1` uses `validation_runtime_plan` to separate callability, preflight checks, postrun checks, contract tests, visual sanity, reproducibility, rewrite comparison, output schema observation, provenance observation, and runtime cost evidence. It also includes static/runtime acceptance gates and split `acceptance_gate` statuses that derive review, implementation, and production readiness from explicit checks rather than manual labels.

The `callability_check` has three layers:

- `installable`: dependencies can be installed or resolved in the proposed environment.
- `runnable_example`: an example, fixture, or minimal invocation can execute.
- `observable_io`: the run produces inspectable inputs, outputs, artifacts, logs, or object fields that BioHarness can validate.

Visual sanity is sanity only. It can catch blank plots, missing labels, missing spatial alignment, or obvious artifact failures, but it is not biological correctness and not algorithmic equivalence.

```yaml
visual_checks:
  purpose: sanity_only
  known_limitations:
    - visual plausibility is not biological correctness
    - visual similarity does not prove algorithmic equivalence
```

Reproducibility checks should cover random seed policy, determinism expectations, repeated runs, label permutation awareness, and stochastic components.

Rewrite comparison, when required, should cover schema equivalence, domain count, no empty domain, label permutation handling, ARI/NMI/AMI where meaningful, spatial pattern sanity, and runtime/memory delta.

Runtime cost records should include wall time, peak memory, device used, and fixture size.

Runtime measurement cannot be faked or inferred from static docs. It must come from an actual execution check, fixture run, or observed runtime execution.

Static acceptance and runtime acceptance must stay separate:

```yaml
static_acceptance_gate:
  required_files_exist:
  yaml_valid:
  layer3_layer4_separation_valid:
  evidence_authority_present:
  required_sections_present:
  no_production_claims:
  status:

runtime_acceptance_gate:
  environment_import_check:
  minimal_fixture_smoke_run:
  runtime_measurement:
  output_schema_observed:
  provenance_observed:
  status:
```

A Layer3/4 review pack can pass static acceptance. Runtime acceptance remains blocked until execution checks and fixtures run. Production support requires runtime acceptance.

## Validation Stages

### Layer 3 validation

Layer 3 validation checks contract completeness before runtime binding:

- semantic input and output contracts are defined
- semantic parameters are bounded enough for execution planning
- environment profile is declared
- preflight checks are named
- post-run expectations are named
- typed failure modes are documented
- provenance expectations are explicit

### Layer 4 validation

Layer 4 validation checks backend binding quality:

- backend call graph is testable
- parameter mapping is sane
- input conversion is explicit
- output extraction is explicit
- artifact capture is explicit
- failure translation is mapped to typed failures
- smoke or fidelity checks are defined when feasible
- every Layer3 functional surface has a Layer4 binding status
- critical backend entrypoints and output mappings reach symbol-level or line-level evidence before implementation starts
- unresolved backend symbols are marked as implementation blockers

### Fidelity Checks

Strong wrappers may need smoke tests that verify the backend can run, produce expected files or object fields, and return typed failures for common setup problems.

Compatibility rewrites require fidelity checks or documented comparison checks against the original implementation. A compatibility rewrite should not be treated as equivalent only because it uses similar inputs and outputs.

Algorithmic rewrites should be hold/manual-review by default unless scientific equivalence can be evaluated with appropriate evidence.

For spatial domain identification, fidelity may include:

- output shape checks
- domain label count checks
- no empty domains
- stable output schema
- agreement with original implementation on a small fixture where possible
- awareness that label permutations are possible
- visual/artifact sanity checks
- provenance and random seed capture
- repeated-run policy
- output schema observation
- contract vs fidelity vs smoke-test separation

Simple smoke tests do not establish exact biological equivalence.

## Bounded Equivalence For Spatial Domain Identification

Spatial domain identification validation should use bounded equivalence rather than byte-level identity. Many relevant methods include stochastic clustering, representation learning, resolution search, GPU/CPU numerical differences, label permutation, and package-version drift. A validation claim is therefore valid only inside the stated fixture, seed, version, metric, and tolerance boundaries.

For wrapper-only paths, validation should confirm that the algorithm core is not touched and that the standardized interface preserves the original method's functional behavior within the declared scope:

- input and output schemas match the Layer 3/4 contract
- labels align one-to-one with observations or the declared output table
- domain count or granularity is reported with the correct guarantee status
- no empty or degenerate domains appear when the method contract forbids them
- declared artifacts, validation report, and provenance record are present
- random-seed behavior and repeated-run policy are recorded

For compatibility rewrites, validation must compare the original implementation and the BioHarness-compatible path on the same fixture where feasible. Comparison should account for label permutation and stochastic variation, and may use ARI, NMI, adjusted mutual information, domain-count agreement, no-empty-domain checks, spatial-pattern sanity, output-schema agreement, and runtime or memory deltas.

For algorithmic rewrites, bounded-equivalence evaluation is not enough by itself to authorize implementation. Any plan that touches graph construction, model training, loss functions, Bayesian inference, clustering logic, or other scientific algorithm core should remain hold or manual-review until the equivalence scope, fixture design, and approval requirement are explicit.

Visual plausibility remains a sanity check only. A nonblank spatial plot, visually coherent domains, or successful runtime completion does not prove biological correctness or algorithmic equivalence.

### `preflight`

`preflight` checks happen before any surface starts running.

They include:

- input data presence and schema checks
- parameter-shape validation against the chosen surface
- environment-profile resolution
- detection of actions that require explicit approval before execution

### `runtime`

`runtime` checks govern what the harness is allowed to do while execution is live.

They include:

- approval gates for sensitive or expensive actions
- guardrails around filesystem, network, and secret access
- run-state capture into `RunRecord`
- interruption or escalation when a blocked action appears

### `post-run`

`post-run` checks happen after artifacts are emitted.

They include:

- artifact presence and shape checks
- domain-level sanity checks such as label coverage or output completeness
- comparison against the promised output contract
- release, block, or manual-review decisions recorded in `ValidationReport`

## Default Manual Approval Triggers

The following actions require explicit human approval unless a later policy says otherwise:

- writing to an `authoritative CSV`
- writing to a `NAS report`
- accessing an `external resource` that depends on secrets
- launching a `high-cost GPU` execution path
- executing a change that mutates the `baseline registry`

## Validation Artifacts

- `RunRecord` preserves structured execution state for resume and compaction.
- `ValidationReport` records `preflight` and `post-run` outcomes plus final release status.
- Golden scenarios under [evals](../evals) act as regression anchors for approval rules and resume behavior.

Future validation reports should also record typed failures and provenance fields such as adapter name, environment profile or capsule, input artifact identifiers, output artifact identifiers, package versions, and relevant checksums or file paths where appropriate.

## Typed Failure Handling

The harness should classify common failures rather than return only raw tracebacks. Candidate categories are defined in [docs/25_harness_architecture.md](25_harness_architecture.md), including dependency, environment, data-contract, resource, runtime-tool, statistical-warning, output-contract, and downstream-compatibility failures.

Typed failures should help the LLM agent decide whether to inspect object fields, switch environment profile, request human approval, repair an input mapping, or stop for manual review.

Spatial transcriptomics-specific categories should include:

- `CoordinateSystemMismatch`
- `SpatialKeyMissing`
- `LibraryIDMismatch`
- `HistologyImageMissing`
- `HistologyScaleFactorMissing`
- `SpotBarcodeMismatch`
- `ReferenceModalityMismatch`
- `ReferenceSpeciesMismatch`
- `ClusterKeyNotCategorical`
- `InsufficientReplicates`
- `SparseMatrixDensificationRisk`
- `OutputSchemaDrift`
- `PackageAPIChanged`
- `EmptyNeighborhoodGraph`
- `DisconnectedSpatialGraph`

Key examples:

- `CoordinateSystemMismatch`: pixel, array row/col, micron, and aligned coordinate systems may differ.
- `ReferenceModalityMismatch`: deconvolution or annotation can fail when scRNA, snRNA, and spatial references are mismatched.
- `SparseMatrixDensificationRisk`: resource safety risk, not just a runtime exception.
- `OutputSchemaDrift`: package update changes field names or output layout while execution appears successful.

## Acceptance Standard

A future execution surface should not be considered BioHarness-ready unless it can:

- identify its required validation hooks before dispatch
- produce enough structured state to resume after compaction
- explain when manual review is required instead of implying success
- classify common recoverable failures in a way the agent can act on
- record enough provenance for replay or manual inspection

The topic that surface belongs to should also have completed the current Layer 2 artifact set and transition gate in [docs/90_roadmap.md](90_roadmap.md) before the surface is treated as ready for Layer 3 work.

## Non-Goals

- This phase does not define a full benchmark harness or runtime implementation.
- This phase does not replace scientific review; it sketches substrate-level gates that would need to happen before scientific interpretation.
