# Layer3 / Layer4 Build Acceptance Checklist

## Purpose

This is the derived acceptance checklist indexed by `docs/layer3_4/stage_integration/layer3_layer4_build.md`. Checks should align with `layer3_layer4_build_outputs.md`, `layer3_layer4_build_audit_outputs.md`, `layer3_layer4_completion_verifier_prompt.md`, and `layer3_layer4_anti_surrogate_audit.md`.

## Build Output Acceptance

- [ ] Method-subagent dispatch evidence exists for every build-required method in multi-method invocations.
- [ ] Method-subagent dispatch uses batches of at most 6 active methods.
- [ ] Method-owned Layer3 / Layer4 implementation evidence comes from the assigned method subagent.
- [ ] Layer3-M config exists for every build-required method with downstream-selectable rows.
- [ ] Each build-required row records config path/section reference.
- [ ] Layer3-M config includes callable projection for every downstream-selectable surface.
- [ ] Callable config projection records projected keys and Layer4 callable/parser accepted keys.
- [ ] Projection is checked against the Layer4 config parser/consumer after synthesis.
- [ ] Config consumption evidence is present and `layer3_method_config_consumption_status=pass_after_synthesis_audit` for downstream-selectable rows.
- [ ] Each build-required row has reachable Layer3-to-Layer4 action-path closure, required selected bridge smoke-check evidence, anti-surrogate audit evidence, and reviewed strict-output contract closure.
- [ ] Each build-required downstream-selectable row records `runtime_adapter_path_status=implemented`.
- [ ] Runtime adapter path evidence is checked separately from selected bridge smoke-check evidence.
- [ ] Each build-required downstream-selectable row has `surface_binding_correspondence_status=pass_after_synthesis_audit`.
- [ ] Each build-required downstream-selectable row has readable `surface_binding_correspondence_evidence`.
- [ ] Each build-required downstream-selectable row has `reviewed_action_effect_status=pass_after_synthesis_audit`.
- [ ] Each build-required downstream-selectable row has readable `reviewed_action_effect_reconciliation_evidence`.
- [ ] Independent audit statuses use `pass_after_synthesis_audit`, including action-path closure, strict-output contract closure, surface lifecycle trace, method-chain lifecycle, and applicable ST image alignment.
- [ ] Surface-binding correspondence records reviewed surface intent, reviewed strict output or state, implemented binding actual calls, actual call classification, and reviewed ownership change when needed.
- [ ] Reviewed action effect reconciliation preserves Gate2 bridge planning and `native_or_rewrite_actions` action names, or records reviewed bounded-equivalence/rewrite basis for any renamed or summarized action.
- [ ] Reviewed action effect reconciliation records expected effect versus actual effect, produced state/output or consumed prior state, and consumed-by-surface evidence when applicable.
- [ ] Probe-only, smoke-only, deferred-only, or `NotImplementedError` Layer4 paths are marked `repair_required` or `downstream_selectable=false`.
- [ ] Method-chain lifecycle evidence records action ownership and confirms no duplicate execution of output-determining native actions across sequential surfaces.
- [ ] Lifecycle/state handoff evidence is limited to surface order, private state producer/consumer, state shape, action ownership, and duplicate output-determining action checks; it does not replace surface-binding correspondence or action-effect evidence.
- [ ] Build callable-path or bounded-adapter check status is recorded without treating deferred runtime execution as produced runtime output.
- [ ] Shared runtime boundary check confirms method-agnostic shared helpers.
- [ ] Method-level and global verifier statuses are `PASS`.
- [ ] Image-aware Visium/Xenium rows record `st_image_alignment_contract_status=pass_after_synthesis_audit`.
- [ ] Rows that are not image-aware record `st_image_alignment_contract_status=not_applicable`.
- [ ] Image-aware downstream-selectable rows have transform evidence and bounded alignment check evidence.
- [ ] Final publication occurs only after all dispatch batches have method iteration evidence, all repair-loop redispatches are resolved, and every build-required method has final or repaired `PASS` evidence.
- [ ] Every `FAIL_WITH_REPAIRS` packet has a repair-loop iteration record showing redispatch/resume, repaired evidence, and final repaired `PASS`, unless the workflow stopped before implementation or returned to review.
- [ ] Every repair-loop iteration record names the affected execution surface, evidence class, observed code path, repair target, repair assignment, repaired evidence root, and repaired iteration status.
- [ ] No method-owned Layer4 binding that only records reviewed action names in metadata, YAML, comments, lifecycle prose, dictionaries, or state containers is accepted as action-path closure.
- [ ] No skeleton-only or metadata-only Layer4 binding is accepted as final repaired `PASS` evidence.
- [ ] Completion matrix publication index sanity check passes before global verifier `PASS`.
- [ ] Publication sanity only confirms required columns, required pointers, readable evidence files, independent audit verdicts present and post-synthesis-audit confirmed, and matrix/per-row non-contradiction.
- [ ] No final completion artifact records `FAIL_WITH_REPAIRS` as the completed invocation status, fallback package status, final matrix status, or downstream-selectable basis; every repair signal has a corresponding repair-loop re-dispatch, final-collation repair, or documented `STOP_BEFORE_IMPLEMENTATION` / review-boundary return.
- [ ] Rows marked `build_required=true` and `downstream_selectable=true` have non-empty key status fields, callable/binding/config pointers, lifecycle evidence, verifier evidence, and per-row result/audit pointers.
- [ ] Core matrix file pointers are readable and do not contradict per-row method, execution surface, or downstream-selectable status.
- [ ] `package_layout.yaml` exists and points to the final package folders, method folders, per-surface records, completion matrix, dispatch log, verifier result, publication sanity record, and completion report.
- [ ] Final registry, completion matrix, package layout, per-row result, and audit are published only after Layer3-M config production, callable projection consumption evidence, action-path closure, strict-output contract closure, final evidence collation into the draft publication package, draft package publishability checks, and global verifier pass on the draft publication package.
- [ ] Held rows remain in the denominator and are not downstream-selectable.
- [ ] Rows marked `downstream_selectable=true` are exactly verifier-confirmed build-required rows.
- [ ] Any independent audit fail, including surface-binding correspondence, reviewed action effect reconciliation, lifecycle/state handoff, anti-surrogate audit, strict-output contract closure, verifier, or publication index sanity, prevents `downstream_selectable=true`.
- [ ] No build matrix field uses method-validation or Stage3 wording to claim runtime result success from the Layer3/Layer4 build phase.

## Boundary Acceptance

- [ ] Callable import evidence, route-level backend-load evidence, selected bridge smoke-check evidence, runtime adapter evidence, surface-binding correspondence evidence, reviewed action effect evidence, lifecycle evidence, anti-surrogate evidence, publication sanity evidence, source locator evidence, and action-binding evidence are recorded as separate evidence classes.
- [ ] Required selected bridge smoke checks use the complete reviewed invocation and enter the implemented Layer4 bridge path rather than only loading the package/module/library.
- [ ] For each selected bridge smoke-check `pass`, command output, exit code, invoked Layer4 entrypoint evidence, and first native/glue boundary observation are recorded.
- [ ] Selected bridge smoke checks do not claim method-harness success, author-case success, strict-output production on validation data, functional correctness, or scientific correctness.
- [ ] Selected bridge smoke checks are retained as bridge readiness evidence but are not accepted as the only implementation evidence for downstream-selectable rows.
- [ ] Smoke-check commands, source locators, lifecycle prose, metadata, handoff summaries, adapter names, policy names, and provenance labels are not accepted as the only reviewed action execution evidence.
- [ ] Symbol lookup, import-only evidence, DLL routine presence, metadata-only records, state-string-only records, lifecycle prose, and bridge/smoke boundary-only records are not accepted as reviewed action effect pass.
- [ ] Normal callable path anchors are recorded for each reviewed action, or the row records explicit prior-state, compatibility glue, bounded-equivalence, or reviewed rewrite basis.
- [ ] Required native state consumed by later surfaces is produced by an earlier surface on the normal callable path.
- [ ] Callable import and route-level backend-load checks use the complete reviewed invocation selected from environment build evidence.
- [ ] Public callable parameters preserve the reviewed Gate1/Gate2 contract.
- [ ] Layer3-M config does not define default values.
- [ ] Layer3-M config is not only a descriptive variable schema for downstream-selectable rows; it includes the callable projection consumed by Layer4.
- [ ] Layer3-M does not expose scalefactors or image transform internals as public/default variables unless they are reviewed method-facing selectors.
- [ ] Layer4 applies image-coordinate transforms internally from canonical input metadata or reviewed prior state.
- [ ] Layer4 default resolution remains implementation-facing; run-time effective parameter recording is downstream evidence, not build-side default policy.
- [ ] Import checks are bounded by reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.
- [ ] Action-path closure does not rely on mock/fake backend behavior, placeholder state, dummy outputs, contract-only strict-output generation, or same-surface pre-existing target output.
- [ ] For each action-path closure pass, reviewed action names appear in executable import/call/start/fail-closed boundary evidence on the reachable Layer3-to-Layer4 path, not only in strings, YAML, comments, lifecycle prose, state metadata, or Layer3-M config.
- [ ] Later surfaces consume prior-surface state or strict output rather than re-running prior output-determining fitting, training, MCMC, clustering, postprocessing, or label-assignment actions.
- [ ] Output-affecting implementation changes have preservation evidence, bounded equivalence evidence, or prior reviewed rewrite basis.
- [ ] Rows with no accepted route basis fail closed rather than producing successful strict output.
- [ ] Reviewed routes started during build and still long-running record runtime observation evidence and are not failed solely for elapsed time.
- [ ] Build output claims are limited to implementation closure, importability, backend loadability, and verifier-confirmed completion for this phase.
- [ ] Build output claims do not assert author-case success, method validation success, comparison-ready runtime output, or scientific result quality.
