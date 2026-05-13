# Layer 3 And Layer 4 Design

## Purpose

Explain how Layer 3 and Layer 4 bridge method selection to reliable execution.

## Status

This document is a working blueprint. Examples are illustrative; implementation-backed status belongs in explicit runtime artifacts or accepted implementation records.

Layer 3 and Layer 4 remain separate presentation and runtime layers. During method onboarding, they may be co-designed through the same `MethodExecutionPlanningRecord` as described in [Layer 3/4 Co-design](codesign.md).

## Spatial Domain Identification Scientific Goal

For the first Layer 3/4 scientific planning case, the goal is to build a traceable planning path for identifying spatially coherent tissue regions or structural domains, from method-repository evidence through Layer 3/4 execution-substrate design.

The current planning case is `spatial_domain_identification`. It uses:

- candidate pool: the NAS `spatial_domain_identification` 27-tool freeze
- sampling design: pure random sample of 8 methods
- sampling seed: `20260508`
- record format: one `MethodExecutionPlanningRecord v0.7.1` per sampled method

The full current workflow, six-phase planning sequence, and pilot state are summarized in [Layer 3/4 planning workspace](README.md). This design document focuses on the architectural relationship between the Layer 3 execution surface and the Layer 4 backend binding.

The canonical `spatial_domain_identification` execution surface may be abstracted before an environment exists for every method. Concrete method-to-surface binding is a later step: before a method-specific Layer 4 binding, wrapper, or rewrite moves toward implementation readiness, it should have at least a minimal environment configuration or future check path.

## Layer 3: Execution Surface Registry

Layer 3 contains stable, machine-readable execution surfaces. It is agent-readable after Layer 2 method selection.

Layer 3 is not raw backend function documentation and is not a full implementation. It is a contract describing semantic inputs, semantic parameters, outputs, environment profile, preflight checks, post-run checks, artifacts, failure modes, and provenance expectations.

An execution surface is the alignment layer between Layer 2 method selection and Layer 4 backend execution. It should make heterogeneous methods look like a small number of stable scientific actions to the agent, even when the backend methods require different object layouts, preprocessing conventions, coordinate formats, image inputs, clustering controls, or output locations.

For example, one spatial domain method may accept an AnnData object directly, another may require expression, coordinates, and histology image to be split and passed separately, a third may not use images at all, and a fourth may not have a distinct preprocessing step. Layer 3 keeps the agent-facing surface stable; Layer 4 records whether each method is directly backend-bound, wrapper-normalized, not applicable, or still unresolved.

A method-specific Layer 3 surface is a realization of a canonical task-family surface. It should carry `inherits_from`, such as `spatial_domain_identification.canonical.v1`, and only add method-specific semantic constraints, parameters, outputs, artifacts, and validation hooks.

Layer 3 planning may use a shared functional coverage vocabulary such as `input_check`, `method_preprocessing`, `core_structure_building`, `model_fit_or_inference`, `output_assignment`, `artifact_export`, `final_validation`, and `visualization`. This vocabulary is a coverage checklist inside an execution surface, not a new conceptual layer and not a list of backend functions. `method_preprocessing` means method-local preprocessing, not global Scanpy/ST preprocessing.

Layer 3 is agent-visible by default. It should not expose backend function names, backend file paths, internal call graphs, or package-private parameters.

Layer 3 parameter policy should expose only semantic, constrained controls. Low-level output namespaces, directory layouts, temporary paths, backend output prefixes, unsafe memory flags, internal object keys, and backend optimization knobs should remain adapter-controlled or forbidden for agent use.

Illustrative `ExecutionSurfaceSpec`:

```yaml
surface_id: spatial_domain_detection.spagcn.v1
task_family: spatial_domain_identification
method: SpaGCN
inherits_from: spatial_domain_identification.canonical.v1
environment_profile: deep-spatial
visibility: agent_readable
functional_surfaces:
  - input_check
  - method_preprocessing
  - core_structure_building
  - model_fit_or_inference
  - output_assignment
  - artifact_export
  - final_validation
  - visualization
semantic_inputs:
  - spatial_anndata
  - optional_histology_image
semantic_parameters:
  - target_domain_count_or_granularity
  - spatial_coordinate_source
  - image_policy
  - random_seed
  - output_label_key_alias_optional
target_domain_count_policy:
  status: method_dependent
  note: Some backends expose resolution or granularity controls rather than exact domain-count guarantees.
semantic_outputs:
  - domain_labels
  - domain_plot
  - run_summary
preflight_checks:
  - has_expression_matrix
  - has_spatial_coordinates
  - histology_available_if_required
postrun_checks:
  - domain_key_written
  - number_of_domains_valid
  - no_empty_domain
  - artifacts_exist
failure_modes:
  - SpatialCoordinateMissing
  - HistologyImageMissing
  - GPUUnavailable
  - OutputContractViolation
```

This example is illustrative.

## Layer 4: Backend Adapter / Wrapper / Rewrite

Layer 4 is the concrete backend binding. It captures parameter mapping, input conversion, output mapping, artifact capture, call graph, environment-bound runtime entrypoint, typed failure translation, and smoke/fidelity tests when available.

Layer 4 must record `integration_mode` and `filesystem_policy` so the planning record can distinguish thin API adapters, wrappers, legacy capsules, CLI/script boundaries, and rewrite candidates. It also carries evidence traceability for backend files, functions, entrypoints, parameters, I/O behavior, and failure translation.

Layer 4 is the method-specific binding map for a Layer 3 execution surface. It records which backend functions, scripts, or wrappers satisfy the surface, and which parts remain unresolved. The required `function_surface_bindings` table is the bridge between the semantic surface and method-specific implementation evidence.

A binding can be `backend_bound` when the backend directly supports the required behavior, `wrapper_added` when BioHarness must normalize I/O, artifacts, logs, or failures, `not_applicable` when the method genuinely lacks that functional coverage point, or `requires_followup` when evidence is insufficient. Critical unresolved bindings block implementation readiness.

Illustrative `BackendAdapterSpec`:

```yaml
adapter_id: backend.spatial_domain_identification.spagcn.v1
surface_id: spatial_domain_detection.spagcn.v1
runtime_language: python
environment_profile: deep-spatial
integration_mode: strong_wrapper
filesystem_policy:
  working_directory: run_scoped
  input_mounts:
    - spatial_input
  output_directory: bioharness_outputs
  temp_storage: isolated_temp
  cache_policy: explicit_only
  cleanup_policy: retain_declared_artifacts
entrypoint: bioharness_adapters.spatial_domain.spagcn.run
call_graph:
  - validate_input_contract
  - convert_anndata_to_backend_input
  - run_backend_training_or_inference
  - extract_domain_labels
  - write_domain_labels_to_adata_obs
  - generate_standard_plots
  - emit_validation_report
function_surface_bindings:
  - layer3_stage: model_fit_or_inference
    binding_status: requires_followup
    backend_files_or_functions:
      - source_symbol_not_resolved_in_current_inventory
    adapter_responsibility: "Resolve exact backend entrypoint before implementation."
    implementation_blocker: true
parameter_mapping:
  n_domains: backend.cluster_count
  spatial_key: backend.coordinate_key
  random_seed: backend.seed
output_mapping:
  domain_labels: adata.obs["bioharness_domain"]
  summary: outputs/summary.json
  plot: outputs/figures/domain_plot.png
failure_translation:
  missing_spatial_key: SpatialCoordinateMissing
  cuda_not_available: GPUUnavailable
rewrite_level: strong_wrapper
visibility: implementation_debug_audit_only
```

This example is illustrative and does not indicate that the adapter entrypoint exists.

## Layer 3 Entry Review

Layer 2 scientific suitability does not automatically imply Layer 3 promotion. Layer 3 entry requires execution readiness review. Layer 3 promotion does not freeze Layer 4 implementation.

For promoted methods, the execution readiness review should usually become a Layer 3/4 `MethodExecutionPlanningRecord`. The planning pass reads the method repository once and separates findings into a Layer 3 `ExecutionSurfaceSpec`, a Layer 4 `BackendAdapterSpec`, a rewrite decision, environment assignment, and validation requirements.

v0.7.1 distinguishes static template acceptance from implementation and production readiness. A method can be structurally reviewable while still failing implementation readiness because environment checks, minimal fixtures, runtime measurement, output schema observation, provenance observation, or symbol-level bindings are missing. Production readiness remains `fail` until runtime implementation, validation, and provenance exist.

Illustrative entry review:

```yaml
method_id: spagcn
task_family: spatial_domain_identification
layer2_decision_role:
  - histology-aware candidate
  - graph neural network candidate
native_ecosystem: python
expected_capsule: deep-spatial
callable_surface_type: script_or_api
input_contract_candidate: SpatialAnnDataContract
output_contract_candidate: DomainLabelsContract
adapter_candidate_status: strong_wrapper
rewrite_policy: wrapper_before_rewrite
blocking_issues:
  - confirm maintained API
  - define histology fallback
  - define deterministic smoke test
promotion_decision: enter_layer3_planning
```

## Visibility Rule

The default reasoning brain should normally stop at Layer 3. Layer 4 can be inspected by a runtime, adapter developer, debugging agent, or audit tool.
