# Layer3 / Layer4 Build Outputs Template

## Purpose

This file defines the output contract for a completed `layer3_layer4_build` invocation indexed by `docs/layer3_4/stage_integration/layer3_layer4_build.md`.

It covers the package layout record, dispatch log, completion matrix, per-row build result, and downstream consumption boundary. Lightweight audit output shapes are defined in `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md`. Verifier verdict structure is defined in `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md`.

## Method Subagent Dispatch Log

`subagent_dispatch_log.yaml` records method-level implementation dispatch for invocations that assign method subagents.

```yaml
subagent_dispatch_log:
  invocation_id:
  subagent_prompt_template: docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md
  max_active_method_subagents: 6
  dispatch_batches:
    - batch_id:
      methods:
        - <method>
      batch_status: pass
  methods:
    - method:
      dispatch_batch_id:
      subagent_id:
      method_prompt_path:
      owned_paths:
      read_only_inputs:
      dispatch_status: pass
      method_evidence_root:
      method_verifier_status:
      returned_files:
      unresolved_repairs:
      repair_loop_iterations:
        - iteration_id:
          method:
          input_status: FAIL_WITH_REPAIRS
          repair_packet:
            execution_surface:
            evidence_class:
            observed_code_path:
            repair_target:
          repair_assignment:
            assigned_to_subagent_id:
            assigned_at:
          repaired_iteration_status: PASS | FAIL_WITH_REPAIRS | STOP_BEFORE_IMPLEMENTATION
          repaired_evidence_root:
  dispatch_verdict: pass
```

When method subagents are required by the invocation, final registry, completion matrix, per-row YAML records, and downstream-selectable publication are not publishable until `subagent_dispatch_log.yaml` exists, every dispatch batch has at most 6 methods, and each build-required method has method evidence with method-level verifier `PASS`.

A dispatch log with unresolved `FAIL_WITH_REPAIRS` packets is not publishable. For a completed invocation, every repair packet must either have a later repaired `PASS` iteration or a documented allowed stop condition outside final publication.

Repair-loop history may remain in a final published package as consumed audit trail only. It must not record unresolved `FAIL_WITH_REPAIRS` as the completed invocation status, final method status, final package status, or basis for `downstream_selectable=true`.

## Package Layout

`package_layout.yaml` records the directory layout of the current Layer3 / Layer4 build package. It is a layout and navigation record only. It helps readers locate the package root, standard folders, root-level records, method folders, method code files, and per-surface row records.

`package_layout.yaml` does not record pass/fail status and does not replace the completion matrix, per-row build result, per-row audit, verifier result, publication index sanity record, or downstream-selectable decision.

The `methods[]` and nested `surfaces[]` entries are derived from the reviewed denominator and final completion matrix. They must list only current in-scope methods and reviewed denominator surfaces, without hardcoded method or surface names in common templates.

`records.global_verifier` and `records.completion_report` record standard final target paths. During draft global verification, those paths may be expected final paths rather than already-written files because the global verifier result and completion report are produced at the end of publication.

Use `method` for the reviewed method display name and `method_slug` for filesystem and Python import paths. `method_slug` is lowercase ASCII with non-alphanumeric runs collapsed to underscores.

The expected shape is:

```yaml
package_layout:
  version: 1
  analysis_problem: <analysis_problem>
  workflow_phase: layer3_layer4_build

  package:
    root: <reviewed_output_package_root>
    scope_id: <stable_scope_id>
    label: <human_readable_label>
    methods_in_scope:
      - <METHOD>
    methods_out_of_scope:
      - <METHOD>
    scope_record: <package_root>/inputs/scope_record.yaml

  folders:
    inputs: <package_root>/inputs
    method_prompts: <package_root>/method_prompts
    methods: <package_root>/methods
    code: <package_root>/<analysis_problem>
    logs: <package_root>/logs
    work: <package_root>/work
    outputs: <package_root>/outputs
    reports: <package_root>/reports
    verifier: <package_root>/verifier

  records:
    completion_matrix: <package_root>/layer3_layer4_build_completion_matrix.tsv
    dispatch_log: <package_root>/subagent_dispatch_log.yaml
    shared_code_check: <package_root>/shared_runtime_boundary_check.yaml
    publication_index_sanity: <package_root>/publication_index_sanity.yaml
    global_verifier: <package_root>/verifier/global_verifier_result.yaml
    completion_report: <package_root>/reports/layer3_layer4_completion_report.md

  code:
    python_path: <package_root>
    package: <analysis_problem>
    registry: <analysis_problem>.registry
    method_file_pattern: <package_root>/<analysis_problem>/<method_slug>/layer4.py
    shared_code_check: <package_root>/shared_runtime_boundary_check.yaml

  methods:
    - method: <METHOD>
      method_slug: <method_slug>
      method_prompt: <package_root>/method_prompts/<METHOD>_layer3_layer4_method_prompt.md
      method_folder: <package_root>/methods/<METHOD>
      method_code_file: <package_root>/<analysis_problem>/<method_slug>/layer4.py
      method_module: <analysis_problem>.<method_slug>.layer4
      config: <package_root>/methods/<METHOD>/layer3_method_config.yaml
      lifecycle_trace: <package_root>/methods/<METHOD>/method_chain_lifecycle_trace.yaml
      method_verifier: <package_root>/methods/<METHOD>/verifier/method_verifier_result.yaml
      surfaces:
        - surface: <execution_surface>
          surface_folder: <package_root>/methods/<METHOD>/<execution_surface>
          build_result: <package_root>/methods/<METHOD>/<execution_surface>/build_output_result.yaml
          build_audit: <package_root>/methods/<METHOD>/<execution_surface>/build_audit.yaml
          smoke_check: <package_root>/methods/<METHOD>/<execution_surface>/selected_bridge_smoke_check.yaml
          logs: <package_root>/logs/<METHOD>_<execution_surface>_*.log
```

## Completion Matrix

`layer3_layer4_build_completion_matrix.tsv` covers the full reviewed `execution surface x method` denominator. It must include enough columns to identify the reviewed row, implementation binding, runtime adapter path status, import checks, selected bridge smoke-check status, surface-binding semantic correspondence, reviewed action effect reconciliation, action-path closure, strict-output contract closure, build callable-path or bounded-adapter check status, per-row output files, and downstream selectability.

For build-required rows, the matrix records `route_type`, `source_confirmation_status`, `own_output_preexisting_input_used`, `method_chain_id`, `prior_surface_dependency`, `state_handoff_policy`, `proposed_downstream_selectable`, and final `downstream_selectable`.

For build-required rows in multi-method invocations, the matrix records `method_subagent_id`, `method_prompt_path`, `method_evidence_root`, and `shared_runtime_boundary_check`.

For build-required rows, the matrix records:

- `layer3_method_config_path`
- `layer3_method_config_consumption_status`
- `callable_config_projection_path_or_rule`
- `projected_config_keys`
- `layer4_accepted_config_keys_or_parser`
- `config_projection_audit_evidence`

`layer3_method_config_consumption_status` allowed values are `pass_after_synthesis_audit`, `repair_required`, `held_with_reason`, or `not_applicable`. For `build_required=true` and `downstream_selectable=true`, `pass_after_synthesis_audit` requires a Layer3-M artifact, an execution-surface section, an explicit callable config projection, projected config keys, and evidence that the projected shape matches the Layer4 callable `config` parser or consumer accepted keys.

`callable_config_projection_path_or_rule`, `projected_config_keys`, and `layer4_accepted_config_keys_or_parser` are method evidence. `layer3_method_config_consumption_status=pass_after_synthesis_audit` is main-window/verifier confirmation over that evidence.

For build-required rows, the matrix records `selected_bridge_smoke_check_status` as `pass`, `not_required`, or `repair_required`. `held_with_reason` is reserved for reviewed held or non-build-required denominator rows and always corresponds to `downstream_selectable=false`.

For build-required rows, the matrix records `runtime_adapter_path_status` as `implemented`, `repair_required`, `held_with_reason`, or `not_applicable`. `implemented` is required for `downstream_selectable=true`. `held_with_reason` is reserved for reviewed held or non-build-required denominator rows. `not_applicable` must not be used for ordinary build-required execution surfaces that are intended for downstream execution.

For build-required rows, the matrix records `surface_binding_correspondence_status` as `pass_after_synthesis_audit`, `repair_required`, `held_with_reason`, or `not_applicable`, and records `surface_binding_correspondence_evidence` as a readable pointer to the per-row surface-binding semantic correspondence audit. For `build_required=true` and `downstream_selectable=true`, `surface_binding_correspondence_status` must be `pass_after_synthesis_audit`.

For build-required rows, the matrix records `reviewed_action_effect_status` as `pass_after_synthesis_audit`, `repair_required`, `held_with_reason`, or `not_applicable`, and records `reviewed_action_effect_reconciliation_evidence` as a readable pointer to the per-row reviewed action effect reconciliation audit. For `build_required=true` and `downstream_selectable=true`, `reviewed_action_effect_status` must be `pass_after_synthesis_audit`.

The legacy `reviewed_action_reconciliation` name may appear in older per-row records as an alias, but new completion records use `surface_binding_semantic_correspondence` and `reviewed_action_effect_reconciliation` as the primary semantic fields. New completion matrices must not use legacy `reviewed_action_reconciliation` fields as publication-gating fields.

For build-required rows, the matrix records `action_path_closure_status`, `strict_output_contract_closure_status`, `surface_lifecycle_trace_status`, `method_chain_lifecycle_status`, and applicable `st_image_alignment_contract_status` as `pass_after_synthesis_audit`, `not_applicable`, `repair_required`, or `held_with_reason`. `held_with_reason` is reserved for reviewed held or non-build-required denominator rows and always corresponds to `downstream_selectable=false`.

The final completion matrix must not use bare `pass` for independent audit status fields. Bare `pass` remains valid for non-audit execution checks such as callable import, route-level backend load, and selected bridge smoke check, and verifier verdicts continue to use `PASS`.

For build-required rows, the matrix records `build_callable_path_check_status` or `build_bounded_adapter_check_status` as `not_run_in_build`, `bounded_check_pass`, `bounded_check_failed`, `observation_recorded`, or `not_applicable`. These fields describe bounded build checks only. They do not represent method validation, author-case execution, comparison-ready runtime output, or scientific result success.

After draft collation and post-synthesis audit normalization, a build-required row may record `proposed_downstream_selectable=true` only when non-audit execution checks use their allowed pass values, independent audit gates use `pass_after_synthesis_audit` or allowed `not_applicable` / `not_required`, `runtime_adapter_path_status=implemented`, and `layer3_method_config_consumption_status=pass_after_synthesis_audit`. The final `downstream_selectable=true` value is assigned only after publication index sanity also passes. This avoids using publication index sanity as both a prerequisite for, and a check over, the same draft truth value.

A build-required row is finally downstream-selectable only when all of the following pass or are post-synthesis-audit confirmed as applicable: runtime adapter path implemented, surface-binding correspondence, reviewed action effect reconciliation, lifecycle/state handoff, anti-surrogate audit, strict-output contract closure, verifier, and publication index sanity. It also requires method evidence, config production and callable projection consumption, shared runtime boundary check, and applicable `st_image_alignment_contract_status` of `pass_after_synthesis_audit` or `not_applicable`. `downstream_selectable=true` means the row is eligible for downstream reviewed execution or validation; it does not by itself prove author-case success, runtime completion on real data, method validation success, or scientific result quality. Build callable-path or bounded-adapter check status does not replace runtime adapter path implementation evidence.

Publication index sanity for the completion matrix is defined in `layer3_layer4_build_audit_outputs.md` and is required before final publication.

For build-required rows, the matrix also records `surface_lifecycle_trace_status`, `method_chain_lifecycle_status`, `lifecycle_trace_evidence`, `method_level_verifier_status`, `global_verifier_status`, and verifier evidence paths when the invocation assigns method subagents.

For every `build_required=true` and `downstream_selectable=true` row in a completed publication matrix:

- callable import, route-level backend load, required selected bridge smoke check, and interface alignment are pass/true or explicitly `not_required`;
- independent audit fields, including action-path closure and strict-output contract closure, use `pass_after_synthesis_audit` or explicitly allowed `not_applicable` / `not_required`;
- `runtime_adapter_path_status=implemented`;
- runtime adapter path evidence is present and points to the selected callable's normal Layer3-to-Layer4 path;
- `surface_binding_correspondence_status=pass_after_synthesis_audit`;
- `surface_binding_correspondence_evidence` is present and readable;
- `reviewed_action_effect_status=pass_after_synthesis_audit`;
- `reviewed_action_effect_reconciliation_evidence` is present and readable;
- build callable-path or bounded-adapter check status is recorded as `not_run_in_build`, `bounded_check_pass`, `bounded_check_failed`, `observation_recorded`, or `not_applicable`;
- Layer3-M config production and callable projection consumption are present;
- `layer3_method_config_path` is present;
- `layer3_method_config_consumption_status=pass_after_synthesis_audit`;
- `st_image_alignment_contract_status` is `pass_after_synthesis_audit` or `not_applicable`;
- method-level and global verifier statuses are `PASS`;
- `own_output_preexisting_input_used=false`;
- `downstream_selectable=true`;
- `build_output_result` and `build_audit` point to the successful per-row records.

Reviewed held rows remain in the denominator with a reviewed hold reason and `downstream_selectable=false`.

## Verifier Result Handoff

Verifier handoff records use the structure defined by `layer3_layer4_completion_verifier_prompt.md`:

```yaml
verifier_result:
  scope: method | global
  scope_id:
  verdict: PASS | FAIL_WITH_REPAIRS
  repair_loop_required: true | false
  terminal_completion_allowed: true | false
  required_repairs:
    - method:
      execution_surface:
      failure_class:
      reviewed_action:
      observed_code_path:
      repair_instruction:
      anti_surrogate_failure:
  pass_summary:
    completed_build_required_rows:
    held_rows_confirmed:
    native_or_rewrite_actions_checked:
```

For `verdict: PASS`, set `repair_loop_required: false` and `terminal_completion_allowed: true`. For `verdict: FAIL_WITH_REPAIRS`, set `repair_loop_required: true` and `terminal_completion_allowed: false`. A `FAIL_WITH_REPAIRS` verifier result is repair-loop input; it is not a publishable final package status.

## Per-Row Build Output Result

`build_output_result.yaml` records one successful build-required row. It contains:

- reviewed Gate 1 / Gate 2 row identity;
- implemented Layer3 callable path and public contract;
- Layer4 backend binding;
- implementation files and registration file;
- runtime environment reference;
- callable import evidence;
- route-level backend load evidence;
- selected bridge smoke-check evidence;
- method-level verifier pass summary;
- global verifier pass summary;
- layer3_method_config:
    config_path:
    method:
    execution_surface:
    variable_keys:
    binding_target_names:
    config_consumption:
      layer3_callable_accepts_or_loads_config: true
      config_values_passed_to_layer4: true
      callable_config_projection_path_or_rule:
      projected_config_keys:
        - <layer4_config_key>
      layer4_accepted_config_keys_or_parser:
      method_evidence_path_or_symbol:
- method_subagent_evidence:
    subagent_id:
    method_prompt_path:
    method_evidence_root:
    method_verifier_status:
- shared_runtime_boundary_check:
    shared_files_reviewed:
    method_agnostic_helpers_only: true
    method_specific_binding_location: method_owned_layer4
- st_image_alignment_contract:
    required: true | false
    platform_family: Visium | Xenium | other | unknown
    spatial_coordinate_semantics:
    coordinate_source:
    image_source:
    image_key_or_resolution:
    image_shape:
    coordinate_to_image_transform_evidence:
    transform_applied_by_layer4: true | false | not_applicable
    bounded_alignment_check:
      required:
      invocation_or_fixture:
      nontrivial_transform_exercised:
      patch_bounds_or_image_access_check:
      status: pass | repair_required | not_applicable
    failure_or_repair_target:
```

The final completion matrix records post-synthesis config projection audit status separately from method-owned per-row evidence:

```yaml
config_projection_audit:
  config_projection_audit_evidence:
  layer3_method_config_consumption_status: pass_after_synthesis_audit | repair_required | held_with_reason | not_applicable
```

`build_output_result.yaml` also contains:

```yaml
- implementation evidence:
  - native_call_sequence;
  - native_call_sites;
  - signature_binding;
  - canonical_input_or_prior_state_source;
  - private_state_policy;
  - strict_output_mapping;
  - artifact_policy;
  - result_selection_policy;
  - source_confirmation_status;
  - method_chain_id;
  - surface_order;
  - prior_surface_dependency;
  - state_handoff_policy;
  - surface_lifecycle_trace:
      agent_visible_inputs:
      source_observed_call_flow:
      implemented_binding_call_flow:
      reviewed_native_call_sites_covered:
      selected_bridge_smoke_check:
        required:
        reason:
        command:
        invocation:
        command_workdir:
        exit_code:
        stdout_path:
        stderr_path:
        layer4_bridge_entrypoint:
        layer4_entrypoint_invoked: true | false
        evidence_mode_used: true | false
        evidence_mode_bypassed_native_boundary: true | false
        first_selected_native_or_glue_boundary:
        native_boundary_observation:
          boundary_symbol_or_source_section:
          observation_type: imported | called | started | fail_closed_at_boundary
          observation_evidence:
        minimal_boundary_reached:
        status:
        failure_class:
        first_failed_bridge_boundary:
        evidence_path_or_summary:
      native_return_objects:
      native_consumer_patterns:
      prior_surface_state_consumed:
      private_state_shape:
  - surface_binding_semantic_correspondence:
      inventory_source:
      reviewed_surface_intent:
      reviewed_strict_output_or_state:
      reviewed_native_or_rewrite_actions:
        - reviewed_action:
      implemented_binding:
        layer3_callable_path:
        layer4_binding_path:
        normal_callable_path_anchor:
        actual_calls:
          - call_target:
            call_type: executed_call | symbol_lookup | import_only | dll_routine_presence | metadata_only | prior_state_consume | reviewed_equivalent
            source_anchor:
            reviewed_ownership_change:
      correspondence_checks:
        surface_intent_matches_binding: true | false
        strict_output_or_state_target_matches: true | false
        actual_calls_belong_to_reviewed_surface: true | false
        ownership_change_reviewed_when_needed: true | false
        smoke_or_probe_only: true | false
      verdict: pass | repair_required
  - reviewed_action_effect_reconciliation:
      inventory_source:
      reviewed_actions:
        - reviewed_action:
          source_surface:
          expected_effect:
          effect_basis: executed_call | produced_state_or_output | consumed_prior_state | reviewed_equivalent | reviewed_rewrite
          implemented_binding_actual_call:
          call_type: executed_call | symbol_lookup | import_only | dll_routine_presence | metadata_only | prior_state_consume | reviewed_equivalent
          implementation_anchor:
          boundary_only_allowed: true | false
          symbol_or_metadata_only: true | false
          smoke_check_only: true | false
          produced_state_or_output:
          consumed_by_surface:
          exact_name_preserved: true | false
          renamed_or_summarized: true | false
          equivalence_or_rewrite_evidence:
          status: pass | repair_required
  - reviewed_action_reconciliation:
      legacy_alias_for: reviewed_action_effect_reconciliation
      use_as_primary_semantic_field: false
  - action_binding_list:
      - reviewed_action:
        source_or_review_evidence:
        layer4_binding_action:
        implementation_file:
        implementation_symbol_or_anchor:
        reachable_layer3_to_layer4_call_path:
        native_or_rewrite_symbol_or_source_section:
        executable_evidence:
          code_anchor:
          import_or_call_statement:
          call_context:
          produced_state_output_or_artifact:
          fail_closed_boundary_when_not_completed:
        required_input_or_prior_state:
        private_state_created_or_updated:
        strict_output_or_artifact_produced:
  - anti_surrogate_audit:
      evidence_path_or_symbol:
      audit_verdict:
  - lifecycle_audit:
      evidence_path_or_symbol:
      lifecycle_verdict:
  - publication_index_sanity:
      status: pass | repair_required | not_applicable
      evidence_path_or_summary:
  - canonical_fields_created_or_updated:
  - strict_output_contract_closure:
      status:
      output_mapping:
      produced_by_reachable_binding:
  - runtime_adapter_path:
      status: implemented | repair_required | held_with_reason | not_applicable
      callable_default_path_summary:
      smoke_probe_separate: true | false
      probe_only: true | false
      deferred_only: true | false
      not_implemented_runtime_path: true | false
      required_input_or_prior_state:
      produced_state_output_artifact_target:
      evidence_path_or_symbol:
  - build_callable_path_check:
      status: not_run_in_build | bounded_check_pass | bounded_check_failed | observation_recorded | not_applicable
      evidence_path_or_summary:
  - downstream_state_obligations:
  - lifecycle_verdict: pass_after_synthesis_audit
  - evidence_basis:
  - compatibility_rewrite_handoff_status;
  - core_chain_complete;
- boundary checks confirming no author case, bridge replay, validation, or data download occurred during build.

`implemented_binding_call_flow` summarizes the Layer4 binding for the current surface. `action_binding_list` records per-action closure from reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite action to a Layer4 binding action on the reachable Layer3-to-Layer4 implementation path. `reviewed_native_call_sites_covered` records the reviewed native call sites, accepted glue/equivalence path, or prior-reviewed algorithmic rewrite path executed by those binding actions.

Legacy field names containing `native_or_rewrite` are retained for schema stability. In this template they also cover accepted runtime-only compatibility glue and bounded equivalent implementations when preservation or equivalence evidence is recorded.

`selected_bridge_smoke_check_status=pass` is invalid when the only evidence is `py_compile`, package import, callable import, source locator evidence, lifecycle prose, or an `evidence_mode` path that bypasses the first reviewed native/glue boundary. When a bounded smoke cannot complete the native action, it may still pass only if it enters the method-owned Layer4 entrypoint and records a fail-closed first native/glue boundary with command output evidence.

Selected bridge smoke-check evidence may support bridge readiness, but it is not runtime adapter path evidence unless the same reachable normal path also implements the downstream runtime adapter behavior and is not smoke-only, probe-only, deferred-only, or `NotImplementedError`.

`executable_evidence` must identify code-located import/call/start/fail-closed boundary evidence. A reviewed action name appearing only as a string value is insufficient.

`config_consumption` proves the parse/pass channel and callable config projection only. Native or rewrite action execution remains in `action_binding_list`.

## Downstream Consumption Boundary

Downstream phases consume only rows marked `downstream_selectable=true` in a completed `layer3_layer4_build_completion_matrix.tsv`.
