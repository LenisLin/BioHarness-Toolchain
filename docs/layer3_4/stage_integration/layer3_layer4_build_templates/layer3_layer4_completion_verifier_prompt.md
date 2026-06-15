# Layer3 / Layer4 Completion Verifier Prompt

## Purpose

Verify whether a candidate Layer3 / Layer4 build has implementation-backed reviewed-route bindings for the requested scope.

Use this prompt with `layer3_layer4_build_workflow.md`, `layer3_layer4_build_outputs.md`, `layer3_layer4_build_audit_outputs.md`, and `layer3_layer4_anti_surrogate_audit.md`; it verifies implementation closure evidence produced by that workflow and recorded in those outputs.

The verifier is read-only. It checks completion evidence for implementation closure only. It does not define new routes, revise reviewed contracts, or evaluate biological correctness.

`FAIL_WITH_REPAIRS` is a builder repair signal. The build executor consumes it inside the implementation loop; it is not a completed phase result, fallback package status, completion-report state, or downstream-selection basis.

A verifier output with `verdict: FAIL_WITH_REPAIRS` must not be copied into final completion artifacts, completion reports, final publication matrices, or downstream-selectable package records as the invocation result. The builder must consume it as a repair input, rerun the affected method, surface, evidence class, or collation step, and then rerun the verifier. Repair packets may be recorded as transient builder evidence, but they are not completion reports and not a completed package state.

## Inputs

- Gate 2 review table.
- Layer4 bridge planning file.
- Reviewed environment binding or backend-load evidence.
- Implementation root.
- Verifier handoff from the builder.
- Method scope: `<METHOD>` or all methods.
- Subagent dispatch log when the invocation is multi-method.
- Method-subagent evidence roots.
- Shared runtime boundary check.
- Package layout record for global scope: `package_layout.yaml`.

## PASS Criteria

For multi-method invocations, a scope passes only when:

1. `subagent_dispatch_log.yaml` records one method subagent for each build-required method in scope;
2. the dispatch log records `max_active_method_subagents <= 6`;
3. every dispatch batch contains at most 6 methods;
4. every earlier dispatch batch has method iteration evidence, all repair-loop returns consumed, and final or repaired `PASS` method evidence before later batch evidence is accepted;
5. each method row points to the assigned method prompt and method evidence root;
6. method-owned implementation files are supported by method-subagent evidence;
7. shared runtime boundary check passes.

A scope passes only when every build-required row in scope has:

1. an importable Layer3 callable module path;
2. `layer3_method_config.yaml` for the method;
3. a per-row reference to the relevant execution-surface section;
4. a registered Layer3 callable that accepts or loads config;
5. a callable config projection for the execution surface, with projected config keys and the Layer4 callable/parser accepted keys recorded;
6. evidence that the projected config shape matches the method-owned Layer4 binding's `config` parser or consumer;
7. a reachable Layer3-to-Layer4 implementation path from that callable;
8. for every action binding item, an implementation file and symbol or anchor on that reachable path;
9. reachable code that executes the reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite symbol or source section recorded for that action;
10. anti-surrogate audit evidence showing that the production path does not use mock/fake backends, placeholder state, dummy, random, or synthetic strict outputs, contract-only strict-output generation, or output-affecting rewrite without preservation/equivalence evidence or prior reviewed rewrite basis;
11. the current row's reviewed strict-output contract closure through the reviewed input contract, allowed prior-surface state, or produced method state/output/artifact;
12. private-state producer/consumer closure where later rows depend on prior state;
13. method-chain action ownership evidence confirms that each output-determining native action has one owner surface and is not re-executed by later surfaces unless explicitly reviewed as non-output-determining and idempotent;
14. route-level backend-load evidence recorded separately from action-binding evidence;
15. selected bridge smoke-check evidence is present and passing for rows whose reachable Layer4 path crosses a language bridge, object-conversion boundary, backend initialization wrapper, package helper API, or runtime-only compatibility glue, or the row records `not_required` with a concrete reason;
16. for every build-required row proposed as downstream-selectable, `runtime_adapter_path_status=implemented`, with code-located evidence that the registered callable's normal runtime path enters implemented method-owned Layer4 adapter logic and is not smoke-check-only, `probe_backend`-only, deferred-only, or `NotImplementedError`;
17. for every build-required row proposed as downstream-selectable, `surface_binding_correspondence_status=pass_after_synthesis_audit`, with readable `surface_binding_correspondence_evidence` showing that the reviewed function intent for the execution surface corresponds to the actual normal Layer4 binding call path;
18. for every build-required row proposed as downstream-selectable, `reviewed_action_effect_status=pass_after_synthesis_audit`, with readable `reviewed_action_effect_reconciliation_evidence` showing that every Gate 2 bridge planning and method prompt `native_or_rewrite_actions` item has effect-bearing evidence through executed call, produced state/output, consumed prior state, reviewed equivalent, or prior reviewed rewrite basis;
19. callable import, route-level backend-load, and selected bridge smoke-check evidence use the complete reviewed invocation selected from environment build evidence;
20. for image-aware Visium/Xenium routes, `st_image_alignment_contract_status=pass_after_synthesis_audit`;
21. coordinate semantics and image pixel frame are recorded separately for image-aware Visium/Xenium routes;
22. implementation evidence applies the reviewed coordinate-to-image transform before image patch extraction for image-aware Visium/Xenium routes.

For adapter and wrapper rows, code-located binding evidence identifies the implementation file, callable or anchor, reachable call path, reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite symbol or source section used, and produced state, output, or artifact.

A method-level `PASS` is a handoff result only. A global `PASS` verifies the draft publication package after final callable-import, route-level backend-load, selected bridge smoke-check, runtime adapter path, surface-binding semantic correspondence, reviewed action effect reconciliation, lifecycle, per-row result, and audit evidence have been collated and publication index sanity has passed for the draft completion matrix. Phase completion requires final publication artifacts only after the draft publication package is `PUBLISHABLE` and the global verifier returns `PASS`.

A global scope passes only when publication index sanity has passed for the draft completion matrix before final publication.

A global scope also requires package-level collation closure: `package_layout.yaml` exists, is readable YAML, points to the final completion matrix, dispatch log, shared-code check, publication sanity record, method folders, and per-surface row records, and records the standard final target paths for the global verifier result and completion report. Missing, unreadable, or contradictory layout pointers are `FAIL_WITH_REPAIRS` for the final collation step, not method evidence failure. The global verifier result and completion report paths are not required to exist before global verifier `PASS`.

## Hard Reject Conditions

Return `FAIL_WITH_REPAIRS` when the verifier cannot confirm method-subagent implementation evidence for a multi-method build.

Return `FAIL_WITH_REPAIRS` when a shared runtime file carries method-specific binding catalogs instead of method-agnostic helpers.

Return `FAIL_WITH_REPAIRS` when a downstream-selectable candidate lacks Layer3-M config or config consumption evidence.

Return `FAIL_WITH_REPAIRS` when a downstream-selectable candidate's Layer3-M config contains only descriptive variable schema and no callable config projection to the Layer4 callable `config` shape.

Return `FAIL_WITH_REPAIRS` when projected config keys do not match the Layer4 parser or consumer accepted keys.

Return `FAIL_WITH_REPAIRS` when a method-owned per-row `build_output_result.yaml` claims `pass_after_synthesis_audit` for config projection or independent audit status instead of providing method evidence for main-window/verifier confirmation.

Return `FAIL_WITH_REPAIRS` when the final matrix lacks `callable_config_projection_path_or_rule`, `projected_config_keys`, `layer4_accepted_config_keys_or_parser`, or `config_projection_audit_evidence` for a downstream-selectable build-required row.

Return `FAIL_WITH_REPAIRS` when the final completion matrix uses bare `pass` as an independent audit status instead of `pass_after_synthesis_audit`.

Return `FAIL_WITH_REPAIRS` when action evidence is limited to supporting evidence such as import success, backend load, selected bridge smoke check, source location, lifecycle prose, or deferred execution.

Return `FAIL_WITH_REPAIRS` when the same output-determining native action is bound to or executed by more than one sequential execution surface in the same method chain without an explicit reviewed non-output-determining and idempotent rationale.

Return `FAIL_WITH_REPAIRS` when a later surface re-runs a prior surface's fitting, training, MCMC, clustering, postprocessing, label-assignment, or other output-determining action instead of consuming the prior surface state or strict output.

Return `FAIL_WITH_REPAIRS` when a required selected bridge smoke check is missing, uses only package-level import/load evidence, bypasses the implemented Layer4 bridge path, fails without repair evidence, or claims method validation / strict-output success from the smoke check alone.

Return `FAIL_WITH_REPAIRS` when a row marked `build_required=true` and `downstream_selectable=true` has a Layer4 implementation whose selected callable path is smoke-check-only, `probe_backend`-only, unconditional deferred-runtime failure, or `NotImplementedError` for reviewed runtime execution.

Return `FAIL_WITH_REPAIRS` when selected bridge smoke-check evidence is reused as the only runtime adapter implementation evidence for a downstream-selectable row.

Return `FAIL_WITH_REPAIRS` when surface-binding correspondence evidence is missing, unreadable, or records a non-pass verdict for a downstream-selectable build-required row.

Return `FAIL_WITH_REPAIRS` when an actual binding call belongs to a different reviewed surface than the current row and no reviewed ownership change, reviewed equivalent, or reviewed rewrite basis is recorded.

Return `FAIL_WITH_REPAIRS` when symbol lookup, import-only evidence, DLL routine presence, metadata, state-string labels, lifecycle prose, or bridge-smoke boundary-only evidence is treated as reviewed action effect.

Return `FAIL_WITH_REPAIRS` when the strict output or private state consumed by the current surface is not produced by the corresponding binding action, produced by reviewed prior surface state, or covered by reviewed equivalence/rewrite evidence.

Return `FAIL_WITH_REPAIRS` when a downstream-selectable row omits a reviewed action from Gate2 bridge planning unless the omission has reviewed held/rewrite/equivalence basis.

Return `FAIL_WITH_REPAIRS` when a reviewed action is renamed as handoff, adapter, policy, provenance, or summary evidence without exact mapping to the reviewed action and reviewed bounded-equivalence/rewrite evidence.

Return `FAIL_WITH_REPAIRS` when action execution evidence points only to selected bridge smoke-check commands, source locators, lifecycle prose, or metadata, without confirming the normal registered callable path.

Return `FAIL_WITH_REPAIRS` when a later surface consumes native state that the reviewed source requires but no earlier surface produces it on the normal callable path.

Return `FAIL_WITH_REPAIRS` when build callable-path or bounded-adapter check status is used to hide a missing runtime adapter path.

Return `FAIL_WITH_REPAIRS` when a build-stage callable-path or bounded-adapter check is used to claim method validation success, author-case execution success, comparison-ready runtime output, or scientific result success.

Return `FAIL_WITH_REPAIRS` when reviewed action names are present only in strings, YAML fields, comments, lifecycle prose, state metadata, or method config, without executable import/call/start/fail-closed boundary evidence in the reachable Layer3-to-Layer4 path.

Return `FAIL_WITH_REPAIRS` when selected bridge smoke-check `pass` evidence lacks command output, exit code, invoked Layer4 entrypoint evidence, or first native/glue boundary observation.

Return `FAIL_WITH_REPAIRS` when an image-aware Visium/Xenium row directly crops the selected image using unmapped `adata.obsm["spatial"]` values.

Return `FAIL_WITH_REPAIRS` when a Visium `hires` or `lowres` image route omits the corresponding scalefactor when coordinates are full-resolution pixel coordinates.

Return `FAIL_WITH_REPAIRS` when a Xenium image-aware route assumes Visium scalefactor semantics.

Return `FAIL_WITH_REPAIRS` when the only smoke evidence uses synthetic identity-scale coordinates while the reviewed route requires nontrivial coordinate-to-image mapping.

Return `FAIL_WITH_REPAIRS` when a candidate row creates strict output through mock/fake backend behavior, placeholder state, dummy, random, synthetic, or deterministic shape-only strict-output generation, backend-unavailable synthetic state, contract-only strict-output generation, or same-surface pre-existing target output.

Return `FAIL_WITH_REPAIRS` when a candidate row uses output-affecting implementation changes without preservation evidence, bounded equivalence evidence, or prior reviewed rewrite basis.

Return `FAIL_WITH_REPAIRS` when rows with no accepted route basis produce successful strict output instead of failing closed, returning repair evidence, or staying held.

Return `FAIL_WITH_REPAIRS` when a long-running route is claimed as still executing but lacks runtime observation evidence, such as command/call evidence, progress or tail log, heartbeat or reviewed no-progress threshold, and termination reason when externally stopped or timed out.

Return `FAIL_WITH_REPAIRS` when a row claims runtime strict output was produced during build but records no bounded build-check status or execution evidence.

Return `FAIL_WITH_REPAIRS` when published per-row records still contain unresolved verifier placeholders such as `pending`, `TODO`, or missing final global verifier evidence paths.

Return `FAIL_WITH_REPAIRS` when the completion matrix is missing required columns from the current build output template.

Return `FAIL_WITH_REPAIRS` when any row marked `build_required=true` and `downstream_selectable=true` has missing, blank, or invalid key publication-index fields for callable path, Layer4 binding, config path/consumption, import/backend/smoke status, action-path closure, strict-output closure, lifecycle status, verifier status, evidence pointers, or per-row result/audit pointers.

Return `FAIL_WITH_REPAIRS` when any row marked `build_required=true` and `downstream_selectable=true` has `surface_binding_correspondence_status` other than `pass_after_synthesis_audit`, missing or unreadable `surface_binding_correspondence_evidence`, `reviewed_action_effect_status` other than `pass_after_synthesis_audit`, or missing or unreadable `reviewed_action_effect_reconciliation_evidence`.

Return `FAIL_WITH_REPAIRS` when publication index sanity attempts to substitute for independent surface-binding semantic correspondence, reviewed action effect reconciliation, lifecycle/state handoff review, anti-surrogate review, strict-output contract review, or verifier review.

Return `FAIL_WITH_REPAIRS` when a core matrix pointer for `build_output_result`, `build_audit`, `lifecycle_trace_evidence`, `method_level_verifier_evidence`, or `global_verifier_evidence` is missing, unreadable, or points to a row whose method or execution surface contradicts the matrix row.

Return `FAIL_WITH_REPAIRS` when a per-row `build_output_result` or `build_audit` contradicts the matrix `downstream_selectable` value for the same method and execution surface.

Return `FAIL_WITH_REPAIRS` for final collation when `package_layout.yaml` is missing, unreadable as YAML, omits required package pointers or expected final verifier/report target paths, points to non-existing standard package locations for already-produced records, or contradicts the final completion matrix for current in-scope methods, reviewed denominator surfaces, method folders, or per-surface row records.

## Verification Steps

1. Enumerate build-required and held rows from Gate 2 and bridge planning.
2. For multi-method scope, check subagent dispatch log, dispatch batch size, terminal batch status, and method evidence roots.
3. Check shared runtime boundary evidence.
4. Read Layer3-M config, check config existence, execution-surface section reference, registered Layer3 callable config acceptance/loading, callable config projection, projected config keys, Layer4 callable/parser accepted keys, and config pass-through into method-owned Layer4 binding.
5. Trace each registered Layer3 callable to method-owned Layer4 implementation.
6. Apply `layer3_layer4_anti_surrogate_audit.md` to the reachable production path.
7. Check selected bridge smoke-check evidence for required rows and verify that it uses the complete reviewed invocation and enters the implemented Layer4 bridge path.
8. Check downstream runtime adapter path readiness for every downstream-selectable build-required row, separately from selected bridge smoke-check evidence.
9. Check ST image alignment contract evidence for image-aware Visium/Xenium routes, including separate coordinate semantics and image pixel frame, reviewed transform evidence, and bounded alignment check evidence when image patches are extracted.
10. Confirm surface-binding semantic correspondence for every downstream-selectable build-required row, including reviewed surface intent, reviewed strict output or state, implemented binding actual calls, actual call classification, and reviewed ownership change when the binding call belongs to another surface.
11. Confirm reviewed action effect reconciliation for every downstream-selectable build-required row, including exact reviewed action names or reviewed equivalence/rewrite basis, expected effect versus actual effect, state/output producer evidence, consumed prior-state evidence where applicable, and rejection of symbol/import/DLL/metadata-only action-effect claims.
12. Confirm reviewed native action execution, accepted compatibility/equivalence evidence where used, runtime observation evidence for started long-running routes where applicable, strict-output contract closure when the row is claimed build-complete, and runtime execution evidence when the row claims runtime strict output was produced during build.
13. Check method-chain action ownership and duplicate output-determining action evidence across the reviewed surface order.
14. Check private-state producer/consumer closure.
15. Confirm held rows are not selectable.
16. Confirm final matrix independent audit statuses were written or confirmed after synthesis by the main window or verifier, not copied as bare `pass` from method-subagent synthesis text.
17. Check publication index sanity for the completion matrix as an index-only check: required columns, key status values including `surface_binding_correspondence_status` and `reviewed_action_effect_status`, core pointer fields including config projection evidence, `surface_binding_correspondence_evidence`, and `reviewed_action_effect_reconciliation_evidence`, readable core evidence files, independent audit verdicts present with `pass_after_synthesis_audit` where required, and method/surface/downstream-selectable non-contradiction between matrix rows and per-row records.
18. Check package-level collation: `package_layout.yaml` exists, is readable YAML, points to the final completion matrix, dispatch log, shared-code check, publication sanity record, method folders, and per-surface row records, and records standard final target paths for the global verifier result and completion report without contradicting the final completion matrix.
19. Return structured verdict.

The verifier does not require per-variable native final-value proof.

## Output

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

For `verdict: PASS`, set `repair_loop_required: false` and `terminal_completion_allowed: true`. For `verdict: FAIL_WITH_REPAIRS`, set `repair_loop_required: true` and `terminal_completion_allowed: false`; the builder must route the first repair target back to the affected method subagent or final collation step and rerun the affected checks before any completion report or publication.
