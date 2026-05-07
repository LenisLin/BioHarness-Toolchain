# Harness Architecture

## Purpose

Describe the candidate architecture for a dependency-aware, contract-based, auditable spatial transcriptomics execution harness.

## Status

This document is a working blueprint. It does not claim that production adapters, environment capsules, validators, runtime dispatch, or backend implementations are already implemented.

## Four-Layer Architecture

BioHarness-Toolchain converts open-ended spatial transcriptomics tool use into a staged substrate: Layer 1 routes an agent to the correct task family; Layer 2 selects methods using curated evidence and decision trees; Layer 3 exposes stable execution surfaces; Layer 4 binds those surfaces to dependency-isolated backend adapters, wrappers, or rewrites.

| Layer | Main question | Agent visibility | Main artifact | Execution status |
| --- | --- | --- | --- | --- |
| Layer 1 | Which task family should be used? | Always visible at routing time | Toolbox catalog / family cards | No execution |
| Layer 2 | Which method or method class should be selected? | Visible after task-family routing | Method knowledge pack, method table, decision tree | No execution |
| Layer 3 | Which stable execution surface should be invoked? | Visible after method selection | `ExecutionSurfaceSpec` | Execution-planning, not backend internals |
| Layer 4 | How is the selected surface actually run? | Hidden by default; visible for implementation/debug/audit | `BackendAdapterSpec`, wrapper, rewrite, call graph | Concrete execution binding |

Layer 1 should not expose 140 method rows to the agent by default. The current Layer 1 method registry can be treated as a backing registry and evidence source, not necessarily the default compact Layer 1 view.

Layer 2 remains a pure documentation and knowledge layer. Layer 3 is not raw package documentation; it is a stable, machine-readable execution surface. Layer 4 maps execution surfaces to concrete backend functions and environment-bound implementations.

Layer 1/2 are agent-facing knowledge layers. Layer 3 is the first machine-readable execution-planning layer. Layer 4 is the concrete backend implementation layer.

Current Layer 3/4 planning uses `MethodExecutionPlanningRecord v0.7.1`, a small patch over v0.7. The architecture is unchanged: Layer 3 is the agent/harness-facing functional execution surface, and Layer 4 is the backend adapter, wrapper, or rewrite binding hidden by default.

## Layer 3/4 Co-design

Layer 3 and Layer 4 are distinct layers in the system. Layer 3 is the method's functional execution surface. Layer 4 is the backend function, interface, and implementation binding.

During current engineering planning, both are produced together from a `MethodExecutionPlanningRecord`. BioHarness does not ask engineers to inspect a method repository once for Layer 3 and again for Layer 4. Instead, one planning record extracts both the functional surface and the backend binding. The final artifacts remain separated: `ExecutionSurfaceSpec` for Layer 3, `BackendAdapterSpec` for Layer 4.

This avoids reading the same package twice while preserving final separation.

| Aspect | Layer 3 | Layer 4 | Co-design implication |
| --- | --- | --- | --- |
| Primary concern | Functional capabilities exposed to BioHarness | Concrete backend functions, scripts, parameters, and implementation | Extract both from the same code audit |
| Default agent visibility | Visible after Layer 2 selection | Hidden by default | Present separately despite shared audit |
| Main artifact | `ExecutionSurfaceSpec` | `BackendAdapterSpec` | Generated together, stored separately |
| Rewrite role | Preliminary wrapper/rewrite signal | Final rewrite level and implementation plan | Rewrite decision refined during audit |
| Example | `model_fit_or_inference`, `output_assignment`, `artifact_export` | backend `train()`, `predict()`, file outputs, parameter mapping | Layer 3 names stable stages; Layer 4 binds them |

Every Layer 3 functional stage must have an explicit Layer 4 binding status: `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`. No Layer 3 stage should be silently omitted from Layer 4; unresolved critical bindings block implementation readiness even when the co-design pack is structurally reviewable.

## Progressive Disclosure To The Agent

```text
Step 1: Agent sees Layer 1 toolbox catalog.
Step 2: Agent selects task family.
Step 3: Harness reveals selected Layer 2 method knowledge pack and decision tree.
Step 4: Agent selects method or method group.
Step 5: Harness reveals Layer 3 execution surfaces.
Step 6: Runtime dispatches Layer 4 backend adapter/wrapper/rewrite.
Step 7: Agent receives structured success/failure/validation summary.
Step 8: Only if needed, a limited Layer 4 debug view may be exposed.
```

## Default Brain Boundary

- The default LLM brain should normally stop at Layer 3.
- Layer 4 should not be part of default reasoning context.
- This reduces context consumption and prevents backend dependency details from leaking into routine reasoning.
- Typed failure summaries should be preferred over raw tracebacks.

## Layer 1: Task Ontology

The harness should expose curated task families, not raw package functions. Candidate high-frequency spatial transcriptomics task clusters include:

- spatial data loading and validation
- quality control
- normalization and highly variable gene selection
- dimensionality reduction and clustering
- spatial neighborhood graph construction
- neighborhood enrichment
- spatial autocorrelation
- spatially variable gene detection
- spatial domain detection
- cell type annotation
- cell type deconvolution
- ligand-receptor / spatial communication analysis
- image feature extraction
- spatial visualization
- report generation
- reproducible artifact export

These task clusters are planning targets. They do not imply that all adapters are already implemented.

## Layer 2: Method Selection

Layer 2 method knowledge packs should carry the evidence and decision logic needed to choose a method or method class inside a task family. They should include method tables, controlled fields, and decision trees.

Layer 2 should not define callable signatures, package commands, environment bindings, or adapter internals. It should produce enough evidence for Layer 3 entry review.

## Layer 3: Execution Surface

Layer 3 defines stable, machine-readable execution surfaces. An `ExecutionSurfaceSpec` should describe semantic inputs, semantic parameters, semantic outputs, environment profile, preflight checks, post-run checks, typed failure modes, artifacts, and provenance expectations.

Layer 3 allows an agent to reason about execution without reading backend package internals.

## Layer 4: Backend Adapter / Wrapper / Rewrite

Layer 4 binds a Layer 3 surface to concrete backend logic. It may include adapter code, wrapper behavior, compatibility rewrites, call graphs, parameter mappings, input conversion, output mapping, artifact capture, and typed failure translation.

Layer 4 is available for implementation, debugging, and audit. It is not part of the default agent context.

## Data Contracts

Adapters should operate on explicit input and output contracts. For spatial transcriptomics, the primary contract anchors should be AnnData and SpatialData where applicable.

Contract checks should describe:

- required object type
- required layers
- required `obs` and `var` fields
- required `obsm` keys such as spatial coordinates
- required `uns` metadata for spatial images when relevant
- expected output fields
- expected file artifacts
- downstream compatibility checks

Tool calling is not the same as reliable tool execution. A function schema alone is insufficient because successful execution depends on software environments, object structure, data contracts, filesystem side effects, statistical assumptions, and downstream compatibility.

## Environment Capsules

The project should avoid asking the agent to solve dependency conflicts at runtime. Tools should be grouped into a small number of prevalidated environment capsules based on high co-occurrence and compatibility.

Candidate capsules are described in [Environment Strategy](30_env_strategy.md). They are planning targets, not implemented environments.

## Adapter Layer

Adapters should be thin, stable wrappers around mature tools. They should translate a task-level request into concrete tool calls while hiding tool-specific parameter quirks, input formatting differences, output placement differences, and log handling from the LLM agent.

A future adapter schema should include:

- adapter name
- task category
- input contract
- output contract
- environment capsule
- primary backend tools
- parameters
- preflight checks
- execution command or function
- post-run validation
- produced artifacts
- provenance record
- typed failure modes

Adapters should not become a wholesale rewrite of mature libraries. Rewrites belong only where fragile glue, notebook fragments, or unstable wrappers cannot be made reliable through a thin adapter.

## Validation And Provenance

Validation and provenance cross-cut Layer 3 and Layer 4.

Layer 3 should define expected checks and failure semantics. Layer 4 should implement or bind those checks to backend behavior.

A task is not successful merely because no exception was raised. The harness should verify:

- required outputs exist
- object dimensions match expectations
- required fields are present
- output tables and figures are generated
- downstream steps can consume the output
- logs and errors are captured
- package versions and environment identifiers are recorded
- input/output checksums or file paths are recorded where appropriate

## Typed Failure Taxonomy

The harness should not return only raw tracebacks. It should classify failures so an LLM agent can repair efficiently.

Candidate failure categories:

- `DependencyConflict`
- `MissingDependency`
- `VersionMismatch`
- `EnvironmentUnavailable`
- `DataContractViolation`
- `MissingInputField`
- `InvalidInputFormat`
- `SpatialCoordinateMissing`
- `ImageMetadataMismatch`
- `ResourceUnavailable`
- `GPUUnavailable`
- `RuntimeToolError`
- `StatisticalAssumptionWarning`
- `EmptyResultWarning`
- `OutputContractViolation`
- `DownstreamCompatibilityError`

Example structured failure response:

```yaml
status: failed
error_type: DataContractViolation
message: "Required spatial coordinates were not found in adata.obsm['spatial']."
recoverable: true
suggested_repairs:
  - "Inspect available adata.obsm keys."
  - "Run the spatial coordinate normalization adapter."
  - "Provide a mapping from the current coordinate field to the expected spatial key."
provenance:
  adapter: build_spatial_neighbors
  environment: scverse-core
  input_object: sample.h5ad
```

Example success response:

```yaml
status: success
adapter: neighborhood_enrichment
created:
  - adata.obsp["spatial_connectivities"]
  - adata.uns["leiden_nhood_enrichment"]
artifacts:
  - outputs/figures/neighborhood_enrichment_heatmap.png
checks:
  spatial_coordinates_present: true
  cluster_key_present: true
  enrichment_matrix_shape_valid: true
provenance:
  environment: scverse-core
  package_versions:
    scanpy: "<recorded-version>"
    squidpy: "<recorded-version>"
```
