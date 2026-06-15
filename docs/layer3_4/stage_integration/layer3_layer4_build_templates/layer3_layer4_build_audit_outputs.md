# Layer3 / Layer4 Build Audit Outputs Template

## Purpose

Defines lightweight audit evidence shapes for Layer3/4 build. This file records audit outputs only. It does not redefine build workflow, verifier criteria, or anti-surrogate rules.

## Per-Row Anti-Surrogate Evidence

Compact evidence shape for action-path closure evidence; rules remain in `layer3_layer4_anti_surrogate_audit.md`. Per-row audit evidence may record local `pass`, but the final completion matrix records independent audit status as `pass_after_synthesis_audit` only after main-window or verifier inspection.

```yaml
anti_surrogate_audit:
  audit_template: docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md
  production_path_checked:
  route_basis:
  compatibility_glue_used:
  bounded_equivalence_evidence:
  mock_or_fake_backend_used:
  placeholder_or_dummy_state_used:
  contract_only_strict_output_generation_used:
  same_surface_preexisting_target_used:
  fail_closed_when_no_accepted_route_basis:
  build_callable_path_check:
    attempted_in_build:
    status: not_run_in_build | bounded_check_pass | bounded_check_failed | observation_recorded | not_applicable
    evidence_path_or_summary:
  runtime_observation:
    required:
    started:
    invocation_evidence:
    start_time:
    pid:
    heartbeat_interval:
    reviewed_timeout:
    no_progress_threshold:
    progress_log:
    host_snapshots:
    intermediate_artifacts:
    observation_summary_or_log:
    termination_reason:
  audit_verdict: pass | repair_required
  evidence_path_or_symbol:
```

## Method-Chain Lifecycle Trace

Each method directory contains `method_chain_lifecycle_trace.yaml` when the method has build-required rows.

```yaml
method_chain_lifecycle_trace:
  method:
  method_chain_id:
  method_subagent_id:
  method_subagent_prompt_path:
  method_evidence_root:
  shared_runtime_boundary_check:
  surface_order:
  agent_visible_contract:
  private_state_inventory:
  producer_consumer_map:
  private_state_shape_flow:
  action_ownership_map:
    - native_action:
      output_determining: true | false
      owner_surface:
      consumer_surfaces:
      repeated_in_surfaces:
      repeated_call_review_status: not_repeated | reviewed_non_output_determining_idempotent | repair_required
      repair_reason:
  duplicate_output_determining_action_check:
    status: pass | repair_required
    duplicate_actions:
      - native_action:
        surfaces:
        reason:
  native_call_flow_summary:
  binding_call_flow_summary:
  strict_output_progression:
  new_agent_walkthrough:
  chain_closure_verdict: pass
  matrix_status_after_synthesis_audit: pass_after_synthesis_audit | repair_required
```

`action_ownership_map` records the single owner surface for each output-determining native action in the method chain. `duplicate_output_determining_action_check` fails when the same fitting, training, MCMC, clustering, postprocessing, label-assignment, or other output-determining native action is executed by more than one sequential surface without an explicit reviewed non-output-determining/idempotent rationale.

`private_state_shape_flow` records the source-observed shape or container form of private state that crosses surface boundaries. `native_call_flow_summary` records the method-level source-observed call order used by adapter and wrapper rows as lifecycle context. `binding_call_flow_summary` records the implemented Layer4 binding order as lifecycle context.

Lifecycle trace fields are implementation guidance for method-chain state handoff. The lifecycle record covers surface order, private state producer/consumer, state shape, action ownership, and duplicate output-determining action checks. It does not replace surface-binding semantic correspondence, reviewed action effect reconciliation, anti-surrogate audit, strict-output contract closure, or verifier review.

## Per-Row Surface-Binding Semantic Correspondence

Each build-required row proposed as downstream-selectable records surface-binding semantic correspondence evidence. This audit asks whether the reviewed function intent for `<EXECUTION_SURFACE>` corresponds to the real function reached by the normal Layer4 callable binding. It does not decide whether each reviewed action has produced an effect-bearing state or output; that is recorded separately in `reviewed_action_effect_reconciliation`.

```yaml
surface_binding_semantic_correspondence:
  inventory_source:
  reviewed_surface_intent:
  reviewed_strict_output_or_state:
  reviewed_native_or_rewrite_actions:
    - <REVIEWED_ACTION>
  implemented_binding:
    layer3_callable_path:
    layer4_binding_path:
    normal_callable_path_anchor:
    actual_calls:
      - call_target:
        call_type: executed_call | symbol_lookup | import_only | dll_routine_presence | metadata_only | prior_state_consume | reviewed_equivalent
        source_anchor:
        reviewed_ownership_change:
        notes:
  correspondence_checks:
    surface_intent_matches_binding: true | false
    strict_output_or_state_target_matches: true | false
    actual_calls_belong_to_reviewed_surface: true | false
    ownership_change_reviewed_when_needed: true | false
    smoke_or_probe_only: true | false
  verdict: pass | repair_required
```

For `build_required=true` and `downstream_selectable=true`, `verdict` must be `pass`. A binding whose actual call belongs to a different reviewed surface, or whose binding is only a symbol lookup, import, DLL routine presence check, metadata record, or smoke/probe-only path without reviewed ownership change, is `repair_required`.

## Per-Row Reviewed Action Effect Reconciliation

Each build-required row proposed as downstream-selectable records reviewed action effect reconciliation evidence. This audit asks whether each `<REVIEWED_ACTION>` has effect-bearing evidence on the normal callable path, or is covered by produced prior state, reviewed equivalence, or reviewed rewrite. It is distinct from surface-binding semantic correspondence and from bridge smoke evidence.

```yaml
reviewed_action_effect_reconciliation:
  inventory_source:
  reviewed_actions:
    - reviewed_action: <REVIEWED_ACTION>
      source_surface: <EXECUTION_SURFACE>
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
```

For `build_required=true` and `downstream_selectable=true`, every reviewed action from the inventory must have `status: pass`, `smoke_check_only: false`, `symbol_or_metadata_only: false`, and either direct effect evidence or reviewed prior-state/equivalence/rewrite evidence. `boundary_only_allowed` defaults to `false`; it may be `true` only when the reviewed row explicitly defines that action as boundary-only, bridge-only, or fail-closed boundary evidence. Import success, symbol lookup, DLL routine presence, metadata fields, state-string labels, lifecycle prose, or boundary-only bridge smoke evidence do not by themselves establish reviewed action effect. If a row has only boundary evidence without reviewed boundary-only basis, record `boundary_only_allowed: false` and `status: repair_required` for reviewed action effect reconciliation while retaining the boundary evidence under bridge/smoke or fail-closed evidence.

## Publication Index Sanity

Defines the lightweight completion-matrix index sanity check required before final publication.

The check confirms:

- required matrix columns exist;
- required pointers are present;
- readable evidence files exist for pointer fields;
- independent audit verdict fields are present and use the allowed post-synthesis status values required by the build output template for draft rows proposed as downstream-selectable and final rows marked downstream-selectable;
- matrix rows and per-row records do not contradict one another.

Publication index sanity is an index and consistency check. It does not perform or replace surface-binding semantic correspondence, reviewed action effect reconciliation, lifecycle/state handoff review, anti-surrogate review, strict-output contract review, or verifier review.

Required columns include row identity, `method`, `execution_surface`, `build_required`, `proposed_downstream_selectable`, final `downstream_selectable`, `layer3_callable_path`, Layer4 binding pointer, `layer3_method_config_path`, `layer3_method_config_consumption_status`, `callable_config_projection_path_or_rule`, `projected_config_keys`, `layer4_accepted_config_keys_or_parser`, `config_projection_audit_evidence`, callable import status, route-level backend-load status, selected bridge smoke-check status, runtime adapter path status, runtime adapter path evidence pointer, build callable-path or bounded-adapter check status, `surface_binding_correspondence_status`, `surface_binding_correspondence_evidence`, `reviewed_action_effect_status`, `reviewed_action_effect_reconciliation_evidence`, action-path closure status, strict-output contract closure status, lifecycle status, method/global verifier status, evidence pointers, `build_output_result`, and `build_audit`.

For each draft row with `build_required=true` and `proposed_downstream_selectable=true`, and for each final row with `build_required=true` and `downstream_selectable=true`, key status fields must use allowed pass values or explicit `not_required` / `not_applicable` values where the build output template permits them. Independent audit verdict fields must be present and use `pass_after_synthesis_audit`, including Layer3-M config callable consumption, surface-binding correspondence, reviewed action effect reconciliation, action-path closure, strict-output contract closure, surface lifecycle trace, method-chain lifecycle, and applicable ST image alignment. Core pointers include callable path, Layer4 binding, config path, config projection and consumption evidence, runtime adapter path evidence, surface-binding correspondence evidence, reviewed action effect reconciliation evidence, lifecycle evidence, verifier evidence, per-row `build_output_result`, and per-row `build_audit`.

```yaml
publication_index_sanity:
  matrix_path:
  required_columns_status: pass | repair_required
  key_status_fields_status: pass | repair_required | not_applicable
  core_pointer_fields_status: pass | repair_required | not_applicable
  readable_core_file_pointers_status: pass | repair_required | not_applicable
  independent_audit_verdicts_present_status: pass | repair_required | not_applicable
  per_row_non_contradiction_status: pass | repair_required | not_applicable
  checked_rows:
    - method:
      execution_surface:
      build_required: true | false
      proposed_downstream_selectable: true | false
      downstream_selectable: true | false
      build_output_result:
      build_audit:
      surface_binding_correspondence_status:
      surface_binding_correspondence_evidence:
      reviewed_action_effect_status:
      reviewed_action_effect_reconciliation_evidence:
      layer3_method_config_consumption_status:
      callable_config_projection_path_or_rule:
      projected_config_keys:
      layer4_accepted_config_keys_or_parser:
      action_path_closure_status:
      strict_output_contract_closure_status:
      surface_lifecycle_trace_status:
      method_chain_lifecycle_status:
      st_image_alignment_contract_status:
      build_callable_path_check_status:
      lifecycle_trace_evidence:
      anti_surrogate_evidence:
      method_level_verifier_evidence:
      global_verifier_evidence:
      row_status: pass | repair_required | held_with_reason
      finding:
  sanity_verdict: pass | repair_required
```

Publication index sanity must not promote a row by reinterpreting evidence. It only confirms required columns, required pointers, readable evidence files, presence and allowed post-synthesis pass values for independent audit verdicts, and matrix/per-row non-contradiction. Any final package or completion matrix that records `FAIL_WITH_REPAIRS` for a build-required row is not publication-sane. Any final matrix that records bare `pass` for an independent audit field is not publication-sane.

## Per-Row Build Audit

`build_audit.yaml` is a compact link record covering Gate2 source, bridge plan source, build scope, verifier evidence, import/backend/smoke evidence, lifecycle evidence, anti-surrogate evidence, publication index sanity status, and non-claims. For build-required rows in a completed invocation, the audit corresponds to `downstream_selectable=true`.

```yaml
build_audit:
  method:
  execution_surface:
  gate2_source:
  bridge_plan_source:
  reviewed_build_scope:
  build_required: true
  downstream_selectable: true
  callable_import_evidence:
  route_level_backend_load_evidence:
  selected_bridge_smoke_check_evidence:
  runtime_adapter_path_evidence:
  build_callable_path_check_evidence:
  surface_binding_correspondence_evidence:
  reviewed_action_effect_reconciliation_evidence:
  method_level_verifier_evidence:
  global_verifier_evidence:
  lifecycle_trace_evidence:
  anti_surrogate_evidence:
  publication_index_sanity:
    status: pass | repair_required | not_applicable
    evidence_path_or_summary:
  build_output_result:
  non_claims:
    author_case_success: not_claimed
    bridge_replay_success: not_claimed
    method_validation_success: not_claimed
    biological_correctness: not_claimed
```
