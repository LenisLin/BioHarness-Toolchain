# Layer3 / Layer4 Method Subagent Prompt Template

## Purpose

Use this template when the main implementation window dispatches one method-level implementation subagent during `layer3_layer4_build`.

The method subagent implements only one method's reviewed Layer3 / Layer4 execution surfaces. It does not define new routes, publish the root completion matrix, edit other method directories, or expose native method functions as public BioHarness API.

The method assignment is derived from the reviewed analysis-problem-level execution surface denominator and Gate1/Gate2 reviewed route. The method subagent must not define, expand, narrow, or reinterpret that denominator.

## Prompt Fields

```yaml
analysis_problem:
workflow_phase: layer3_layer4_build
method:
repo_root:
results_root:
current_artifact_root:
implementation_root:
method_build_output_root:
owned_paths:
read_only_inputs:
minimum_reference_documents:
reference_documents:
execution_environment:
reviewed_rows:
surface_order:
strict_outputs:
native_or_rewrite_actions:
private_state_policy:
held_rows:
method_verifier:
return_evidence:
stop_condition:
```

`native_or_rewrite_actions` is retained as a compatibility field name. In this template it also covers accepted runtime-only compatibility glue and bounded equivalent implementations when they are recorded with preservation or equivalence evidence.

## Prompt Skeleton

```text
You are Codex working in <repo_root>.

Current analysis_problem:
<analysis_problem>

Current workflow_phase:
layer3_layer4_build

Method assignment:
<method>

Task:
Implement this method's reviewed Layer3 / Layer4 execution surfaces inside the owned paths only. For every build-required row assigned to this method, the registered Layer3 callable must reach method-owned Layer4 code for the reviewed surface. Selected bridge smoke checks may import, call, start, or fail-closed reach the reviewed native/glue boundary as bounded build evidence. For a row intended to become downstream-selectable, the callable's normal runtime path must also implement the intended runtime adapter path from canonical input or prior method state toward the reviewed strict output/state/artifact boundary, and use the produced state, output, or artifact to close the reviewed strict-output contract. Do not satisfy strict-output contracts with mock/fake backend behavior, placeholder state, dummy, random, or synthetic strict output, contract-only strict-output generation, or output-affecting rewrite without preservation/equivalence evidence. Do not return `PASS` for a downstream-selectable row whose Layer4 implementation is only `probe_backend`, selected bridge smoke-check code, unconditional deferred-runtime exception, or `NotImplementedError`.

A skeleton implementation is not sufficient. A method-owned Layer4 module that only records reviewed action names in dictionaries, YAML, comments, lifecycle prose, metadata, `MethodState`, or other non-executable records, or that raises before importing/calling/starting/fail-closed reaching the reviewed native/glue/equivalence/rewrite boundary, must not be returned as `PASS`. If such a gap is found inside the reviewed route, continue implementing real Layer4 binding evidence in this iteration when possible; return `FAIL_WITH_REPAIRS` only as a repair packet when the current iteration cannot complete the repair without main-window reassignment or reviewed-boundary resolution.

Owned paths:
<owned_paths>

Read-only inputs:
<read_only_inputs>

Read these reference documents first:
docs/layer3_4/stage_integration/layer3_layer4_build.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md
docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md
docs/layer3_4/storage_and_runtime.md

Then read method-specific reviewed inputs:
<read_only_inputs>

Execution environment:
<execution_environment>

Reviewed rows:
<reviewed_rows>

Reviewed surface order:
<surface_order>

Strict outputs:
<strict_outputs>

Reviewed native or rewrite actions:
<native_or_rewrite_actions>

Reviewed action inventory source:
Gate 2 bridge planning plus the reviewed rows and `native_or_rewrite_actions` in this prompt. Preserve reviewed action names in surface-binding semantic correspondence and reviewed action effect reconciliation records. Do not replace reviewed action names with handoff, adapter, policy, provenance, or summary labels unless explicit reviewed bounded-equivalence or rewrite basis is recorded.

Private-state and handoff policy:
<private_state_policy>

Held rows:
<held_rows>

Implementation workflow:
1. Confirm owned paths, reviewed rows, source roots, strict outputs, and the complete execution environment, including command-level environment variables and invocation prefix when recorded.
2. Read the method source package and reviewed native call sites; identify any runtime-only compatibility glue, object-conversion boundary, backend initialization wrapper, package helper API, or bounded equivalent implementation needed to preserve the reviewed route.
3. If the reviewed route is image-aware, identify platform family, spatial coordinate semantics, image source, image key or resolution, image shape, and coordinate-to-image transform evidence before implementing patch or image extraction.
4. Identify method-local controllable variables, binding targets, and the per-surface callable config projection from the reviewed source path.
5. Write `<method_build_output_root>/layer3_method_config.yaml`.
6. Implement Layer3 callable config channel. `layer3_method_config.yaml` must not be only a variable description; every downstream-selectable surface must record method evidence for how its variables project into the Layer4 callable `config` key/value shape.
7. Derive reviewed action inventory exactly from reviewed rows and `native_or_rewrite_actions`. Preserve reviewed action names in the surface-binding semantic correspondence and reviewed action effect reconciliation records. Do not replace reviewed action names with handoff/adapter/provenance summaries unless an explicit reviewed bounded-equivalence or rewrite basis is recorded.
8. Implement method-owned Layer4 binding and downstream runtime adapter path for each reviewed action. The binding must contain reachable executable import/call/start/fail-closed boundary evidence, and downstream-selectable rows must also contain a normal runtime adapter path distinct from smoke/probe-only code. Pass projected config values into the method-owned Layer4 binding and record `callable_config_projection`, `projected_config_keys`, `layer4_accepted_config_keys_or_parser`, and a method evidence path or symbol. Reviewed action names in YAML, dictionaries, metadata, comments, lifecycle prose, or `MethodState` are not implementation unless the reachable Layer4 path also contains that executable boundary evidence.
9. Register method-owned Layer3 callable for each reviewed surface.
10. Run selected bridge smoke checks for surfaces that cross language runtimes, object-conversion boundaries, backend initialization wrappers, package helper APIs, or runtime-only compatibility glue; record `pass`, `not_required`, or `repair_required` for build-required rows, and record `held_with_reason` only for reviewed held or non-build-required rows, without claiming strict-output production or method validation success. Selected bridge smoke-check pass does not establish runtime adapter implementation.
11. Record `runtime_adapter_path_status`, close the reviewed strict-output contract through produced method state, output, or artifact evidence, and record build callable-path or bounded-adapter check status as `not_run_in_build`, `bounded_check_pass`, `bounded_check_failed`, `observation_recorded`, or `not_applicable`. This build check status must not replace `runtime_adapter_path_status=implemented`.
12. Record surface-binding semantic correspondence for each build-required row proposed as downstream-selectable, including `reviewed_surface_intent`, `reviewed_strict_output_or_state`, `reviewed_native_or_rewrite_actions`, `implemented_binding.actual_calls`, actual call classification, surface ownership check, and `verdict`.
13. Record reviewed action effect reconciliation for each build-required row proposed as downstream-selectable, including exact reviewed-action names, expected effect versus actual effect, effect basis, state/output producer check, consumed-by-surface evidence when applicable, and explicit status for actions covered by prior surface state, runtime-only compatibility glue, bounded equivalence, or reviewed rewrite.
14. Distinguish bridge/smoke evidence from action-effect evidence. Bridge/smoke evidence may show import, start, or fail-closed boundary readiness. Action-effect evidence requires executed call, produced state/output, consumed prior state, reviewed equivalent, or reviewed rewrite evidence.
15. Apply the anti-surrogate audit to the reachable production path and record the audit evidence inside per-row action-path evidence.
16. For reviewed routes started during build and still long-running, record runtime observation evidence instead of failing solely for elapsed time.
17. Record method-chain lifecycle trace, per-row action binding evidence, action ownership map, duplicate output-determining action check, and `config_consumption` method evidence, including callable config projection evidence. Do not assign final matrix `layer3_method_config_consumption_status=pass_after_synthesis_audit`, `surface_binding_correspondence_status=pass_after_synthesis_audit`, or `reviewed_action_effect_status=pass_after_synthesis_audit`.
18. Run method verifier handoff.
19. Return `PASS` only with method evidence root and method verifier pass. Return `FAIL_WITH_REPAIRS` only as a repair packet naming the first affected surface, evidence class, observed code path, and repair target. A `FAIL_WITH_REPAIRS` return does not complete the method assignment; the main implementation window must re-dispatch the affected method/surface after assigning or applying the repair unless the issue is `STOP_BEFORE_IMPLEMENTATION` or a reviewed-boundary contradiction. When re-dispatched with a repair packet, begin from the affected surface/evidence class and either repair it to method verifier `PASS` or return a narrower repair packet. Do not repeat the same skeleton-only state, metadata-only binding, or non-executable action-name record as a new method iteration.

Shared runtime edits are limited to method-agnostic helpers.

Required method evidence:
- method-owned Layer3 callable files;
- method-owned Layer4 implementation files;
- `layer3_method_config.yaml`;
- per-row `layer3_method_config` reference;
- `callable_config_projection` evidence;
- `projected_config_keys`;
- `layer4_accepted_config_keys_or_parser`;
- method evidence path or symbol for config projection and consumption;
- per-row action binding list with reachable Layer3-to-Layer4 call path;
- surface-binding semantic correspondence evidence for each build-required row proposed as downstream-selectable;
- reviewed action effect reconciliation evidence for each build-required row proposed as downstream-selectable;
- exact reviewed-action-to-code-anchor mapping;
- explicit status for actions covered by prior state, compatibility glue, bounded equivalence, or reviewed rewrite;
- actual call classification as `executed_call`, `symbol_lookup`, `import_only`, `dll_routine_presence`, `metadata_only`, `prior_state_consume`, or `reviewed_equivalent`;
- expected effect versus actual effect for each reviewed action;
- surface ownership check confirming actual calls belong to the current reviewed surface or have reviewed ownership change;
- state/output producer check naming produced state/output or consumed prior state when used as action-effect evidence;
- confirmation that selected bridge smoke-check evidence is not the only action execution evidence;
- code-located executable action evidence showing that the reachable Layer3-to-Layer4 path imports, calls, starts, or fail-closed reaches the reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite boundary;
- native/rewrite action names recorded only in YAML, lifecycle prose, comments, lists, dictionaries, `MethodState`, or other metadata are not action-binding evidence unless the reachable Layer4 implementation also contains executable import/call/start/fail-closed boundary evidence for that action;
- callable import, route-level backend-load, and selected bridge smoke-check logs recording the exact invocation used;
- selected bridge smoke-check evidence for every surface whose reachable Layer4 path crosses a language bridge, object-conversion boundary, backend initialization wrapper, package helper API, or runtime-only compatibility glue, including status, failure class, and first failed bridge boundary when the check fails;
- `runtime_adapter_path_status` for each build-required row;
- evidence that the registered Layer3 callable's normal runtime path reaches method-owned Layer4 adapter logic separately from smoke/probe-only code;
- evidence that the normal runtime path is not an unconditional deferred-runtime exception and does not raise `NotImplementedError` for reviewed runtime execution;
- evidence naming the required canonical input or prior method state and the reviewed strict output, method state, or artifact target produced or advanced by the adapter path;
- evidence that each reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite action is executed on that reachable path;
- evidence that symbol lookup, import-only evidence, DLL routine presence, metadata-only records, state-string-only records, lifecycle prose, or bridge/smoke boundary-only evidence are not used as reviewed action effect pass;
- method-chain action ownership evidence showing the owner surface for each output-determining native action and confirming that later surfaces consume prior state rather than re-executing the same output-determining action;
- duplicate output-determining action check evidence, with `repair_required` when the same fitting, training, MCMC, clustering, postprocessing, label-assignment, or other output-determining action appears in more than one surface without reviewed non-output-determining/idempotent rationale;
- `st_image_alignment_contract` evidence for image-aware Visium/Xenium routes;
- evidence that Layer4 applies the reviewed coordinate-to-image transform internally rather than exposing scalefactors as Layer3-M defaults;
- bounded alignment check evidence when the implementation extracts image patches;
- evidence that produced state/output/artifact closes the reviewed strict-output contract;
- build callable-path or bounded-adapter check status for each row;
- anti-surrogate audit evidence showing no mock/fake backend, placeholder state, dummy, random, or synthetic strict output, contract-only strict-output generation, same-surface target-output shortcut, or output-affecting rewrite without preservation/equivalence evidence was used;
- fail-closed evidence when no accepted route basis exists for the reviewed row;
- runtime observation evidence only when a reviewed route was started during build and is still running, stopped, or failed with observation evidence;
- method-chain lifecycle trace;
- method-level verifier handoff and verdict;
- boundary checks confirming no author-case, bridge replay, validation, data download, or native-result shortcut was used.
- evidence verdicts for independent audits, without writing final matrix independent audit statuses as bare `pass`; post-synthesis audit confirmation belongs to the main implementation window or verifier.

Method verifier:
<method_verifier>

Return evidence:
<return_evidence>

Stop condition:
Stop only when the method reaches method-level verifier `PASS`, or when a phase-start required input is missing, a reviewed source locator contradicts the Gate1/Gate2 boundary, or the reviewed route is impossible without returning to the appropriate review path.

A route that would require mock/fake backend behavior or contract-only surrogate output to pass must return `FAIL_WITH_REPAIRS` or `STOP_BEFORE_IMPLEMENTATION`, not `PASS`.

A route whose only implemented Layer4 behavior is backend probing, selected bridge smoke-checking, deferred execution stubbing, or `NotImplementedError` must return `FAIL_WITH_REPAIRS` or remain non-selectable; it must not be returned as downstream-selectable `PASS`.

A route that has started the reviewed native action but has not completed because it is long-running should return runtime observation evidence or repair evidence, not a surrogate success output and not a failure based only on elapsed time.

Final response:
Report method status, files changed, evidence paths, verifier result, first unresolved repair if any, and any shared utility edits.
```

## Method Subagent Self-Check

- Does the prompt name exactly one method?
- Are owned paths disjoint from other method subagents?
- Are read-only inputs concrete paths?
- Are `layer3_layer4_build.md`, `layer3_layer4_build_workflow.md`, `layer3_layer4_anti_surrogate_audit.md`, `layer3_layer4_build_outputs.md`, `layer3_layer4_build_audit_outputs.md`, and `layer3_layer4_completion_verifier_prompt.md` included as references?
- Does the prompt include the method's reviewed rows, surface order, strict outputs, native/rewrite actions, and private-state policy?
- Does the prompt require strict-output contract closure from method-produced state, output, or artifact, and bounded build-check status when applicable?
- Does the prompt reference `layer3_layer4_anti_surrogate_audit.md`?
- Does the prompt forbid mock/fake backend behavior and contract-only surrogate outputs for build-required PASS?
- Does it require fail-closed behavior instead of successful strict output when no accepted route basis exists?
- Does the prompt limit shared runtime edits to method-agnostic helpers?
- Does the prompt require method-level evidence before returning `PASS`?
- Does the prompt explicitly forbid skeleton-only Layer4 bindings as `PASS` evidence?
- Does the prompt require redispatched repair packets to be implemented or narrowed, not merely re-reported?
- Does the prompt include the complete reviewed invocation, including command-level environment variables when required?
- Does the prompt require per-surface callable config projection for downstream-selectable rows?
- Does the prompt require projected config keys to be checked against the Layer4 config parser or consumer?
- Does the prompt require selected bridge smoke checks for R/Python bridges, object conversion, backend initialization wrappers, package helper APIs, and runtime-only compatibility glue?
- Does the prompt require downstream runtime adapter path evidence separately from selected bridge smoke-check evidence?
- Does the prompt reject smoke-only, probe-only, deferred-only, or `NotImplementedError` Layer4 paths as downstream-selectable implementation evidence?
- Does the method prompt require exact reviewed action effect reconciliation?
- Does it reject renamed/summarized handoff actions without reviewed equivalence or rewrite basis?
- Does it require normal callable path anchors for reviewed action coverage?
- Does it require surface-binding semantic correspondence evidence?
- Does it require reviewed action effect reconciliation evidence separately from bridge/smoke, runtime adapter, lifecycle, anti-surrogate, and publication sanity evidence?
- Does it require actual call classification?
- Does it distinguish symbol lookup, import, and DLL routine presence from action execution or effect?
- Does it prohibit metadata-only or state-string-only evidence as action-effect pass?
