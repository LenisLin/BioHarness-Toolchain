# Environment Strategy

## Purpose

Record a working blueprint for substrate-phase environment design without locking the repository into a single execution provider.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries stated in [docs/15_layer1_method_registry_and_substrate_transition.md](15_layer1_method_registry_and_substrate_transition.md).

## Current Working Direction

The substrate phase treats environment handling as a first-class architecture concern rather than as a later implementation detail. The operative design is provider-neutral and uses the same separation that recent agent runtimes emphasize: the orchestration harness stays lightweight and stateful, while compute remains isolated and disposable.

For spatial transcriptomics, the working target is a small number of prevalidated environment capsules rather than ad hoc dependency solving by an LLM agent at run time.

Unified backbone packages do not imply one global super-environment. BioHarness should use a small number of prevalidated environment capsules.

## Harness vs Compute

### Harness responsibilities

- decompose the user task into a bounded analysis action
- resolve the right skill and default execution surface
- check approval requirements before expensive or sensitive actions
- maintain structured state summaries for resume and compaction
- evaluate outputs and decide whether post-run validation is sufficient

### Compute responsibilities

- execute the chosen surface inside an isolated runtime
- provide the required dependency stack and resource class
- enforce filesystem, network, and secret boundaries
- emit logs, artifacts, and failure signals in a predictable shape
- avoid leaking package-internal complexity back to the harness

This split keeps BioHarness aligned with current agent-runtime practice while avoiding a hard dependency on any one provider. Modal is a useful reference for the separation itself, not a required execution backend.

## `EnvironmentProfile`

`EnvironmentProfile` is the candidate public abstraction for environment selection in the current working blueprint. It is designed to be serializable, reviewable, and reusable across providers if later accepted.

| Field | Meaning |
| --- | --- |
| `profile_id` | Stable identifier for the profile. |
| `isolation_mode` | Isolation boundary such as container, sandbox, or remote worker. |
| `base_stack` | Named dependency stack or pinned package family. |
| `resource_class` | Coarse resource tier such as CPU, GPU, or high-memory GPU. |
| `storage_policy` | Artifact, cache, and mount behavior. |
| `secrets_policy` | Whether external credentials are disallowed, inherited, or explicitly mounted. |
| `provider` | Execution provider or provider-neutral placeholder. |

The repository blueprint may also carry optional operational fields such as `approval_required`, `network_policy`, and `retention_policy`, but those do not replace the required core fields above.

## `environment_plan` In Layer 3/4 Method Planning

`environment_plan` is an independent artifact inside the `MethodExecutionPlanningRecord v0.7.1`. It is separate from `rewrite_decision`: an environment conflict does not automatically imply a rewrite, and a rewrite proposal does not remove the need to document environment evidence.

For promoted methods, the plan should record:

- `environment_profile_candidate`
- `expected_capsule`
- `native_package_manager`
- `install_files`
- `lock_or_container_available`
- `dependency_conflict_risk`
- `known_dependency_risks`
- `gpu_policy`
- `cuda_policy`
- `cpu_fallback_policy`
- `shared_environment_feasibility`
- `isolation_strategy`
- `environment_decision`
- `environment_hold_status`
- `environment_subagent_report`
- `future_check_targets`

Preferred pre-check planning decisions include `environment_check_required`, `shared_capsule_unknown`, `dedicated_capsule_may_be_required`, and `wrapper_boundary_required`.

Static dependency risk does not justify final environment hold. `hold_due_to_environment` must not be used as a final decision unless an environment subagent report cites a failed execution check or impossible dependency constraint. If no environment check has run, `environment_hold_status` must be `not_justified_yet` or `unknown`, not `justified`.

Environment risk may trigger a future execution check, a dedicated capsule, a wrapper boundary, or an optional-path exclusion. It should not automatically trigger method hold. Optional runtime paths, such as R/rpy2/mclust or method-specific GPU extras, should be separated from the core path and kept unavailable to the agent until verified.

These are planning decisions only. They do not claim that a capsule, wrapper, or compatibility rewrite exists.

## Dependency Evidence Extraction For Method Planning

For spatial domain identification, Phase 1 `Repository Evidence Index` provides install, dependency, runtime, and automation evidence references. Phase 2 `Environment Configuration Abstraction` uses those references to form environment planning fields without local installation or execution checks. The fuller extraction fields below serve Phase 2 environment planning and concrete method-to-surface binding work.

For Layer 3/4 method planning, `install_files` must refer to concrete evidence paths rather than a generic statement that installation material exists. A method planning record should preserve enough dependency evidence to support later conflict analysis and capsule grouping without claiming that an environment has already been solved.

For every install, dependency, or runtime-configuration evidence item, record at planning level:

- `path`: repository-relative path or URL section for the evidence
- `source_type`: setup file, package descriptor, environment file, lockfile, container file, CI file, README install section, notebook install cell, script header, optional-runtime note, or inferred import clue
- `package_manager`: pip, conda, mamba, poetry, uv, R, Bioconductor, GitHub source install, system package manager, container, or mixed
- `declared_dependencies`: package names or install commands as declared by the source
- `version_constraints`: exact pins, ranges, unconstrained versions, or implicit latest-source installs
- `channel_or_source`: conda channel, PyPI, Bioconductor, GitHub repository, local path, system package source, or unknown
- `optional_or_core`: whether the dependency path is required for the core workflow or only for optional clustering, plotting, image, GPU, R/Python bridge, or reporting behavior
- `extras`: extras, optional groups, feature flags, or documented alternate install paths
- `system_libraries`: compiler, OS library, BLAS/LAPACK, image library, geospatial library, Java, or other non-Python/R dependency hints
- `gpu_cuda_constraints`: GPU requirement, CUDA version, torch/tensorflow build, CPU fallback, or unknown status
- `python_r_bridge`: rpy2, reticulate, Rscript boundary, mclust, Seurat, Bioconductor, or other cross-language dependency
- `conflict_candidates`: dependency-version or runtime-boundary risks that should be checked later
- `future_check_target`: import check, optional-path check, minimal fixture run, GPU check, R bridge check, or no immediate check identified

Static dependency evidence may justify planning decisions such as `environment_check_required`, `shared_capsule_unknown`, `dedicated_capsule_may_be_required`, `wrapper_boundary_required`, or optional-path exclusion. It must not be used by itself to claim that an environment capsule is available, that runtime support exists, or that a method should receive a final environment hold.

## Candidate Environment Capsules

The following capsule names are planning targets, not implemented environments:

| Capsule | Intended use |
| --- | --- |
| `scverse-core` | AnnData, Scanpy, Squidpy, SpatialData, numpy, scipy, pandas, scikit-learn, igraph/leidenalg, and matplotlib. |
| `image-spatial` | OpenCV, scikit-image, Squidpy image utilities, napari, or spatial image tooling where relevant. |
| `deep-spatial-cpu` | PyTorch and graph/deep spatial packages where CPU execution is supported. |
| `deep-spatial-cu*` | Conceptual CUDA-specific variants for GPU-bound deep spatial methods. Exact CUDA versions are not pinned in this blueprint. |
| `r-seurat-core` | Seurat object workflows, Visium/HD workflows, reference mapping, and Seurat-native visualization. |
| `r-bioc-spatial` | SpatialExperiment, SingleCellExperiment, SummarizedExperiment, and Bioconductor-style spatial workflows. |
| `r-spatial-communication` | CellChat, NicheNet, COMMOT, spacexr, or related communication and deconvolution tools where relevant. |
| `reporting` | matplotlib, plotly, nbconvert, quarto, or equivalent report-generation utilities. |

These capsules should eventually group tools by dependency compatibility and task co-occurrence. They should not be treated as available runtime targets until they have lockfiles, container metadata, or equivalent implementation evidence.

Deep learning and CUDA methods should be isolated by resource and torch/CUDA build profile. CPU fallback behavior should be explicit: unsupported, slow path, or reselect method. Do not force all methods into one environment.

## Operating Rules

- The harness should not infer package-level install steps at run time when an `EnvironmentProfile` already exists.
- A surface that requires `high-cost GPU` execution should resolve to a named profile instead of ad hoc flags.
- Access to an `external resource` with secrets should be routed through explicit approval and a documented `secrets_policy`.
- Environment definitions are planning artifacts for this phase; they do not yet imply a committed runtime implementation under `src/`.
- Topic-level environment design should begin only after the topic completes the current Layer 2 artifact set and transition gate in [docs/90_roadmap.md](90_roadmap.md).
- The agent should not infer package-level installation or version repair when a task can be routed through a declared profile or future capsule.

## Repository Blueprint Mapping

- Human-readable policy stays in this document and [docs/35_agent_runtime_reference.md](35_agent_runtime_reference.md).
- Machine-readable contract shape lives in [contracts/environment_profile.schema.json](../contracts/environment_profile.schema.json).
- Example profiles live under [contracts/examples](../contracts/examples).

## Non-Goals

- This phase does not commit BioHarness to Modal, OpenAI sandboxes, Kubernetes, or any other single execution target.
- This phase does not define per-tool Dockerfiles, cluster topology, or deployment automation.
