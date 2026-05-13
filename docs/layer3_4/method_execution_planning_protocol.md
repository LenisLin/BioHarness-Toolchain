# Layer 3/4 Method Execution Planning Protocol v0.7.1

## Status

Blueprint / protocol draft. `MethodExecutionPlanningRecord v0.7.1` is the current generic planning protocol for Layer 3/4 method engineering. v0.7.1 is a small patch over v0.7, not a conceptual redesign. It supersedes v0.5 and v0.6 planning language. Current spatial domain pilot state is summarized in [Layer 3/4 planning workspace](README.md).

## Purpose

Given a Layer 2 promoted method, this protocol guides one method engineering planning record that co-designs a Layer 3 surface and a Layer 4 backend binding while keeping final artifacts separate. The record gathers the Layer 2 handoff, callability constraints, canonical surface reference, evidence registry, code mind map, function surface map, Layer 3 draft, Layer 4 adapter draft, environment plan, rewrite decision, validation/runtime plan, risks, decisions, work plan, and acceptance gate into one traceable planning object.

The record is not a runtime API. Its downstream outputs are separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` drafts.

## Storage Policy

Generic templates, schemas, and design documents may live in the project repository. Method-specific intermediate artifacts, including method-reading notes, review packs, draft surfaces, adapter drafts, environment reports, and validation plans, must live in the NAS results workspace unless a higher-authority document explicitly promotes them.

Live method engineering packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. If a method-specific artifact is included as a project example, it must be explicitly marked synthetic or illustrative, not a live method-specific output.

```yaml
storage_policy:
  generic_template_location: project_repo_allowed
  method_specific_intermediate_location: NAS_required
  project_docs_allowed: false_for_method_specific_intermediates
  production_claim_allowed: false_unless_runtime_implementation_exists
```

## Core Principles

- Layer 3 is agent/harness readable by default after Layer 2 method selection.
- Layer 4 is hidden by default and exposed only for implementation, debugging, or trace review.
- Layer 3 and Layer 4 are co-designed from one method engineering evidence package, but final artifacts remain separated.
- Layer 3 must inherit from a canonical task-family surface or justify why no canonical surface exists.
- Layer 3 defines execution surfaces, not backend functions. The surface aligns heterogeneous method interfaces so the agent does not need to repeatedly parse method-specific APIs, notebooks, object layouts, or output conventions.
- Layer 4 records how each method satisfies the execution surface through backend calls, wrappers, input/output conversion, artifact handling, environment evidence, and typed failure translation.
- Layer 2 reasoning should not be copied wholesale into Layer 3. Hard constraints that affect callability must be preserved.
- BioHarness aggressively standardizes interfaces, contracts, validation, artifacts, and provenance, but conservatively rewrites scientific algorithms.
- Static dependency risk alone does not justify a method-level environment hold.
- Acceptance status is split across template acceptance, implementation readiness, and production readiness, and is derived from checks rather than manually assigned.
- Every required functional coverage point in the Layer3 execution surface must have an explicit Layer4 binding status.
- File-level evidence can support co-design review, but implementation-critical entrypoints and output mappings require symbol-level or line-level evidence before MVP adapter implementation.

## Current Template

The fillable template is [Method Execution Planning Record Template v0.7.1](templates/method_execution_planning_record_v0.7.1.md). The compatibility path [method_execution_planning_record_template.md](templates/method_execution_planning_record_template.md) points to the same current template.

The canonical current JSON schema path is [contracts/method_execution_planning_record_v0.7.1.schema.json](../../contracts/method_execution_planning_record_v0.7.1.schema.json). The older [contracts/method_execution_planning_record_v0.7.schema.json](../../contracts/method_execution_planning_record_v0.7.schema.json) path is retained for compatibility.

Separate v0.7.1-compatible downstream schemas are available for Layer 3 and Layer 4 drafts:

- [contracts/execution_surface_spec_v0.7.1.schema.json](../../contracts/execution_surface_spec_v0.7.1.schema.json)
- [contracts/backend_adapter_spec_v0.7.1.schema.json](../../contracts/backend_adapter_spec_v0.7.1.schema.json)

Top-level record shape:

```yaml
method_execution_planning_record:
  record_id:
  record_version: v0.7.1
  method_id:
  task_family:
  planning_status:
  authority_status:
  storage_policy:
  source_layer2_artifacts:

  layer2_to_layer3_handoff:
  hard_constraints_for_layer3:

  audit_evidence_registry:
  code_mind_map:
  function_surface_map:

  canonical_surface_reference:
  layer3_agent_surface:
  layer4_adapter_draft:

  environment_plan:
  rewrite_decision:
  validation_runtime_plan:
  static_acceptance_gate:
  runtime_acceptance_gate:
  risk_register:
  decision_log:

  subagent_work_plan:
  acceptance_gate:
  next_action_decision:
```

## Spatial Domain Identification Pilot Requirements

The first small-scope `spatial_domain_identification` planning pilot uses the NAS 27-tool freeze as its candidate pool, a pure random sample of 8 methods, and fixed seed `20260508`. The sampling design is a planning requirement only; this protocol text does not execute the random draw and does not create method-specific records.

This protocol currently elaborates the first two planning topics: repository/documentation evidence reading and environment configuration abstraction. Later Layer3 surface, Layer4 binding/rewrite, and bounded-equivalence topics remain the next discussion sequence. The final pilot step is a walkthrough that applies the planning flow across the sampled methods.

### Phase 1: Repository Evidence Index

Before filling method-specific Layer 3/4 fields, each sampled method should receive a repository and documentation evidence reading pass. The goal is to locate evidence that supports execution design, not to evaluate paper quality.

The core output is a unified `Repository Evidence Index`. It is the Phase 1 evidence organization used to populate evidence references in the `MethodExecutionPlanningRecord`, including the existing `audit_evidence_registry` field with a narrower execution-planning meaning. A method record should start with a compact header:

```yaml
repository_evidence_header:
  method_id:
  display_name:
  task_family: spatial_domain_identification
  primary_repository_url:
  paper_title:
```

Use tiered reading depth:

- T0 `full_repository_census`: every file enters the evidence index with relative path, file kind, language or format, size class, read depth, role hypothesis, evidence ID, and derived planning targets.
- T1 `full_textual_extraction`: README files, documentation, manifests, package descriptors, environment files, examples, scripts, notebook source cells, and tests receive complete planning summaries.
- T2 `symbol_inventory`: source files receive imports, classes, functions, signatures, exported API or CLI symbols, global configuration, and major call-relation notes.
- T3 `line_level_execution_trace`: author-recommended workflow, input conversion, parameter mapping, core algorithm calls, output assignment, artifact export, and environment-sensitive paths receive line-level or equivalent precise evidence when available.
- T4 `runtime_observed`: reserved for later runtime checks or fixture runs. The planning pilot records only future runtime-observation targets.

Each index item uses the T0 fields directly:

```yaml
repository_evidence_index:
  - relative_path:
    file_kind:
    language_or_format:
    size_class:
    read_depth:
    role_hypothesis:
    evidence_id:
    derived_planning_targets:
```

Field guide:

| Field | Fill with | Example value |
| --- | --- | --- |
| `relative_path` | Repository-relative file path or document locator. | `README.md` |
| `file_kind` | Source, documentation, manifest, package descriptor, environment file, notebook, script, test, data, generated, binary, model/checkpoint, or unknown. | `documentation` |
| `language_or_format` | Language or file format when identifiable. | `markdown` |
| `size_class` | Lightweight size bucket used to plan read depth. | `small_text` |
| `read_depth` | T0, T1, T2, T3, or T4 target level. | `T1_full_textual_extraction` |
| `role_hypothesis` | Short hypothesis for the file's role in execution planning. | `author_recommended_workflow` |
| `evidence_id` | Stable evidence identifier used by later planning phases. | `EVID-README-001` |
| `derived_planning_targets` | Later planning uses supported by this evidence item. | `environment_configuration_abstraction`, `layer3_execution_surface` |

Illustrative synthetic example:

```yaml
repository_evidence_header:
  method_id: example_spatial_domain_method
  display_name: ExampleDomain
  task_family: spatial_domain_identification
  primary_repository_url: https://github.com/example-lab/example-domain
  paper_title: "ExampleDomain: spatially informed domain identification for spatial transcriptomics"

repository_evidence_index:
  - relative_path: README.md
    file_kind: documentation
    language_or_format: markdown
    size_class: small_text
    read_depth: T1_full_textual_extraction
    role_hypothesis: author_recommended_workflow
    evidence_id: EVID-README-001
    derived_planning_targets:
      - environment_configuration_abstraction
      - layer3_execution_surface
      - layer4_binding_or_rewrite
      - bounded_equivalence_validation
```

The repository census should distinguish source code, documentation, examples, notebooks, tests, configuration, install manifests, data files, generated files, binary files, model/checkpoint files, notebook outputs, and unknown roles. Data, binary, generated, and large notebook-output files may be recorded as metadata-only unless their content is required to understand callability or output contracts.

The evidence index should cover repository URL, version or commit, license, install-file locations, README/tutorial/notebook locations, package structure, main entrypoints, input objects or files, spatial-coordinate conventions, histology-image requirements, multi-sample or batch support, output-label location, visualization or export paths, example datasets, algorithm-core boundary, and documentation evidence level.

The reading pass should also identify method-internal source structure. Use the following shared function-family vocabulary when classifying source symbols, scripts, notebooks, and workflow glue:

- `package_setup`
- `data_loading`
- `input_validation`
- `object_conversion`
- `method_preprocessing`
- `spatial_structure_building`
- `image_feature_extraction`
- `model_fit_or_inference`
- `clustering_or_domain_assignment`
- `postprocessing`
- `output_writeback`
- `artifact_export`
- `visualization`
- `cli_or_notebook_glue`
- `configuration`
- `tests_or_fixtures`
- `utility_unclassified`

The execution path trace should connect the author-recommended workflow to source symbols and files, then to input object requirements, coordinate handling, image or reference use, semantic parameters, intermediate objects, algorithm-core calls, output label writeback, artifacts, logging, provenance hooks, and unresolved symbols. The trace should make later Layer3/4 discussion evidence-based rather than README-only.

### Phase 2: Environment Configuration Abstraction

Phase 2 uses install, dependency, runtime, and automation evidence from the `Repository Evidence Index` to form environment planning fields. It does not claim runtime support, capsule availability, or final environment hold.

```yaml
environment_configuration_abstraction:
  method_level_summary:
    documented_primary_runtime:
    author_recommended_install_route:
    explicit_gpu_cuda_note:
    explicit_r_python_cross_runtime_note:
    automation_material_visible:
    author_environment_notes:

  key_path_references:
    - path_ref:
      source_type:
      author_reported_install_or_runtime_content:
      package_or_command_mentions:
      explicit_version_constraints:
      package_manager_or_installer:
      documented_role:
      explicit_gpu_cuda_signal:
      version_or_runtime_attention_note:

  later_comparison_and_check_targets:
    shared_capsule_candidates:
    dedicated_capsule_risks:
    conflict_candidates:
    future_minimal_check_targets:
```

These fields preserve author-visible runtime and install information while keeping environment decisions at planning level. More complete dependency extraction uses the environment strategy fields `path`, `source_type`, `package_manager`, `declared_dependencies`, `version_constraints`, `channel_or_source`, `optional_or_core`, `extras`, `system_libraries`, `gpu_cuda_constraints`, `python_r_bridge`, `conflict_candidates`, and `future_check_target`.

Field guide:

| Field | Fill with |
| --- | --- |
| `documented_primary_runtime` | Main runtime shape presented by author documentation, such as Python, R, mixed R/Python, CLI/script, container-only, or unclear. |
| `author_recommended_install_route` | Most direct author-recommended installation entrypoint visible in the evidence index, such as pip, conda, R install, Bioconductor, GitHub source, Docker, manual, mixed, or unclear. |
| `explicit_gpu_cuda_note` | Author-visible GPU/CUDA note at method level. A torch or tensorflow mention alone is not enough. |
| `explicit_r_python_cross_runtime_note` | Author-visible cross-runtime boundary, such as `rpy2`, `reticulate`, `Rscript`, or Python workflow use of an R package. Pure R usage is recorded as runtime shape, not as a cross-runtime boundary. |
| `automation_material_visible` | Author-visible Docker, CI, Makefile, shell script, notebook install cell, benchmark script, or comparable automation material. |
| `author_environment_notes` | Author-emphasized version, installation-order, compatibility, operating-system, branch, or source-install notes. |
| `path_ref` | Evidence-index path or locator used by the environment abstraction. |
| `source_type` | Type of evidence source, such as README install section, docs page, requirements file, environment file, package descriptor, R DESCRIPTION, Dockerfile, CI workflow, shell script, notebook install cell, usage note, or other text. |
| `author_reported_install_or_runtime_content` | Short paraphrase of the author-visible install, version, environment, or runtime content. |
| `package_or_command_mentions` | Packages, install commands, source installs, system packages, R packages, or Bioconductor packages explicitly mentioned in the evidence source. |
| `explicit_version_constraints` | Explicit pins, ranges, minimum versions, source tags, source branches, source commits, or old-version requirements visible in the evidence source. |
| `package_manager_or_installer` | Installer or mechanism used or implied by the evidence source. |
| `documented_role` | Role of the evidence source in author documentation, such as main install, quick start, tutorial/demo, paper reproduction, benchmark, test/CI, container build, developer setup, optional feature, or unclear. |
| `explicit_gpu_cuda_signal` | GPU/CUDA signal visible in that specific evidence source. |
| `version_or_runtime_attention_note` | Lightweight note for later environment comparison, such as fixed old versions, R package requirements, CUDA mentions, or inconsistent README and Docker routes. |
| `shared_capsule_candidates` | Evidence-derived hints that a method may fit a shared environment after comparison across sampled methods. |
| `dedicated_capsule_risks` | Evidence-derived hints that a method may require an isolated environment path. |
| `conflict_candidates` | Dependency-version, package-manager, GPU/CUDA, system-library, or R/Python boundary risks to compare later. |
| `future_minimal_check_targets` | Later import, fixture, GPU, optional-path, or R/Python bridge checks suggested by repository evidence. |

## Subsequent Planning Topics

The following topics remain the next discussion sequence after the repository evidence and environment abstraction guidance above.

### Phase 3: Layer3 Execution Surface Unification

This discussion will define how the `spatial_domain_identification` canonical surface represents the shared scientific action across methods. It should cover semantic inputs, semantic parameters, outputs, artifacts, failure and provenance policy, AnnData versus separated matrix/coordinate/image inputs, coordinate source modes, image use, batch or multi-sample policy, target-domain granularity, agent-visible parameters, and adapter-controlled parameters.

### Phase 4: Layer4 Binding / Wrapper / Rewrite Decision

This discussion will map each functional coverage point to backend-bound behavior, wrapper responsibility, `not_applicable`, or `requires_followup` status. It should use the Phase 1 function-family map and execution trace to decide input conversion, method-local preprocessing, structure construction, model fitting or inference, output assignment, artifact export, validation hooks, visualization, filesystem policy, failure translation, and whether algorithm-core behavior is touched.

### Phase 5: Bounded-Equivalence Validation Plan

This discussion will define validation plans within stated fixture, seed, version, metric, and tolerance boundaries. Wrapper checks should cover schema, label alignment, artifacts, and provenance. Rewrite checks should compare original and BioHarness-compatible paths where feasible. Stochastic, deep, or clustering methods should account for label permutation, ARI/NMI/AMI, domain count, no empty domain, and spatial sanity. Visual plausibility remains a sanity signal rather than biological correctness.

### Phase 6: 8-Method Planning Pilot Walkthrough

The pilot walkthrough applies the preceding planning flow across the sampled methods. It should check method work packages, review gates, record-filling rules, allowed `requires_followup` states, implementation-readiness blockers, and the current pilot-state context summarized in [Layer 3/4 planning workspace](README.md).

The current pilot target is planning and documentation readiness. It does not require package imports, minimal fixture runs, output-schema observation from runtime, runtime or memory measurement, provenance emission from runtime, or production support.

## Layer 2 Handoff

Use the full handoff to retain selection context without copying the whole Layer 2 method-comparison artifact into the Layer 3 agent card:

```yaml
layer2_to_layer3_handoff:
  full_handoff:
    layer2_branch:
    method_role:
    selection_context:
    caveats:
    evidence_summary:
    hardware_resource_tag:
    applicability_notes:

hard_constraints_for_layer3:
  required_modalities:
  forbidden_modalities:
  required_input_object:
  required_spatial_information:
  histology_requirement:
  reference_requirement:
  gpu_requirement:
  multi_sample_policy:
  minimum_dataset_assumptions:
```

## Layer 3 Rules

Layer 3 describes semantic execution surfaces. It must not expose raw backend function names, backend file paths, package-private parameters, implementation call graphs, unsafe memory flags, temporary filenames, or raw backend coordinate tuple/key details.

For spatial domain identification, the canonical execution surface must account for this functional coverage vocabulary:

```yaml
functional_surfaces:
  - input_check
  - method_preprocessing
  - core_structure_building
  - model_fit_or_inference
  - output_assignment
  - artifact_export
  - final_validation
  - visualization
```

This vocabulary is a coverage checklist inside the execution surface, not a new conceptual layer and not a backend function list. Use `method_preprocessing` for method-local preprocessing.

Layer 3 keeps the agent-facing interface stable even when methods differ internally. A method that accepts AnnData directly, a method that requires expression/coordinate/image components to be split, a method that does not use images, and a method without explicit preprocessing should still be represented through the same canonical execution surface where scientifically appropriate. The method-specific differences belong in semantic constraints at Layer 3 and in wrappers or bindings at Layer 4.

Layer 3 coordinate handling uses semantic source modes only:

```yaml
spatial_coordinate_source:
  allowed_modes:
    - obsm_spatial
    - obs_x_y_columns
    - adapter_validated_custom_mapping
```

Layer 3 must include normalized policies for:

- `multi_sample_policy`
- `target_domain_count_policy`
- `parameter_policy`
- `clustering_backend_policy` where a method exposes or depends on optional clustering runtimes
- `layer4_reference_policy`
- `validation_contract`
- `failure_policy`
- `provenance_policy`

Agent-visible parameters must be semantic and constrained. Low-level backend knobs, raw file paths, temporary filenames, internal object keys, unsafe memory flags, backend optimization parameters, low-level output namespaces, directory layouts, and backend output prefixes should be forbidden for agent control. If user naming control is needed, expose a safe semantic alias such as `output_label_key_alias_optional`; the adapter controls output field prefixes, directory layout, temporary directories, and log-file policy.

## Layer 4 Rules

Layer 4 binds the execution surface to concrete backend implementation details. It may contain backend functions, scripts, notebooks, file paths, parameter mappings, call graphs, filesystem policy, environment binding, and failure translation. Every major backend claim must cite repository evidence references.

Layer 4 adapter drafts must include at least the fields listed in the v0.7.1 template's Layer4 completeness contract. `implementation_status` remains `not_implemented` unless actual runtime code exists. `authority_status` remains `blueprint` unless formally promoted.

Every required functional coverage point in the Layer3 execution surface must be represented by `function_surface_bindings` with one of `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`. No required part of the execution surface may be silently omitted from Layer4. Missing binding coverage can still pass static template review if explicit, but critical unresolved bindings block implementation readiness.

The draft-only sentinel `source_symbol_not_resolved_in_current_inventory` is allowed only when paired with `implementation_blocker: true` and `resolution_required_before: MVP_adapter_implementation`. It is not allowed in implementation-ready adapter specs. If it appears for model fitting, inference, output assignment, or parameter mapping, implementation readiness must be `fail`.

Evidence resolution must be recorded as `file_level`, `symbol_level`, `line_level`, or `runtime_observed`. A Layer4 draft may be accepted for planning with file-level evidence, but implementation cannot start until critical backend entrypoints and output mappings reach symbol-level or line-level evidence. Runtime-observed evidence is required before runtime support can be claimed.

## Environment Rules

Environment planning is independent from rewrite planning. Use `environment_plan` as the top-level holder for installability, dependency, GPU/CUDA, shared-capsule, isolation, optional-path, and future check requirements.

Layer 3 may declare an environment profile candidate or resource expectation, but compatibility is a Layer4 evidence and execution-check question. Without an import check or fixture run, the record must not claim that a shared capsule is usable.

Static dependency risk does not justify final environment hold. `hold_due_to_environment` must not be used as a final decision unless an environment subagent report cites a failed execution check or impossible dependency constraint. Preferred pre-check state:

```yaml
environment_decision:
  - environment_check_required
  - shared_capsule_unknown
  - dedicated_capsule_may_be_required
  - wrapper_boundary_required
environment_hold_status: not_justified_yet
```

Optional backend paths, such as mclust/rpy2, should be separated from the core path.

Environment risk may trigger a future execution check, a dedicated capsule, a wrapper boundary, or an optional-path exclusion. It should not automatically trigger method hold.

## Validation And Acceptance

The validation plan must separate callability checks, preflight checks, postrun checks, contract tests, visual sanity checks, reproducibility checks, runtime-cost records, output schema observation, provenance observation, and rewrite comparison. Visual plausibility is not biological correctness, and visual similarity does not prove algorithmic equivalence. Runtime measurement cannot be faked or inferred from static docs.

Static acceptance and runtime acceptance are separate. A Layer3/4 review pack can pass static acceptance with valid YAML, separated Layer3/Layer4 artifacts, evidence authority, required sections, and no production claims. Runtime acceptance remains blocked until environment import checks, minimal fixture smoke runs, runtime measurement, output schema observation, and provenance observation exist.

The acceptance gate derives three statuses:

- `template_acceptance_status` checks structural review validity.
- `implementation_readiness_status` checks whether MVP adapter implementation can start.
- `production_readiness_status` checks whether runtime support can be claimed.

A method can pass template acceptance while failing implementation readiness. Missing environment check, fixture, runtime measurement, output schema freeze, or symbol-level bindings should block implementation readiness but not necessarily template acceptance. Production readiness must remain `fail` unless actual runtime implementation, validation, and provenance are complete. `ready_for_review` is not a manual label; it requires `template_acceptance_status: pass` or `overall_status: partial_with_known_blockers` with explicit blockers. Invalid YAML, missing required Layer4 sections, broken critical links, unnormalized coordinate/multi-sample/domain-count fields, or production-support claims must block review readiness.
