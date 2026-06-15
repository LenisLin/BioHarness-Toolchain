# Layer3 / Layer4 Anti-Surrogate Audit Template

## Purpose

This template defines the build-stage internal audit for action-path closure in `layer3_layer4_build`.

The audit prevents a build-required row from recording `action_path_closure=pass` when the registered Layer3 callable can only satisfy the reviewed strict output through surrogate behavior rather than a reviewed production path.

## Scope

The audit covers action-path closure only. It checks whether the registered Layer3 callable reaches Layer4 code that executes reviewed implementation actions and uses their produced state, output, or artifact for the reviewed strict output.

The audit does not establish author-case success, bridge replay success, runtime support, production readiness, validation success, algorithmic equivalence, biological correctness, or scientific result quality. Those claims require later reviewed execution or validation evidence.

## Positive Rule

For a build-required row to pass action-path closure, the reachable production callable path must execute a reviewed production route basis:

- reviewed native action;
- build-time runtime-only compatibility glue that preserves the reviewed native scientific path;
- bounded equivalent implementation accepted during build with lightweight equivalence evidence;
- prior-reviewed algorithmic rewrite.

The build-stage strict-output contract must be closed through the reviewed input contract, allowed prior-surface state, or state/output/artifact created by that route basis. Actual runtime production of that strict output is recorded only when the build invocation explicitly attempts runtime execution; otherwise it remains deferred to downstream reviewed execution or validation. Supporting evidence such as source locators, import success, backend load success, selected bridge smoke checks, lifecycle prose, or deferred execution is not enough by itself.

## Compatibility And Rewrite Rule

During build, do not invent an output-affecting implementation solely to make a strict output file or object exist.

Runtime-only compatibility glue is allowed during build when it preserves the reviewed native scientific path. Examples include object conversion, language-bridge conversion, matrix orientation, dtype conversion, sparse/dense conversion, NA/NaN handling, pathing, artifact materialization, logging, and randomness-control plumbing.

A bounded equivalent implementation may be accepted during build when the method subagent records lightweight equivalence evidence. The evidence should be limited to the relevant invariant, such as matching formula, matching input identity, matching output-affecting parameters, matching observation order, matching dimensions, or matching label-alignment logic.

Algorithmic or scientific-core rewrites that cannot be justified by such bounded equivalence evidence require prior reviewed rewrite basis. If the build cannot show preservation or bounded equivalence, the row returns `FAIL_WITH_REPAIRS`, remains held, or returns to the appropriate review path.

## Hard Reject Conditions

A build-required row cannot record `action_path_closure=pass` when strict-output contract closure relies on any of the following:

- placeholder state;
- dummy, random, or synthetic strict output;
- deterministic shape-only output that is unrelated to the reviewed route computation;
- backend-unavailable synthetic state;
- mock, fake, stub, or test-double backend behavior;
- contract-only strict-output generation;
- pre-existing same-surface target output used as if it were produced by the current row;
- output-affecting rewrite without preservation evidence, bounded equivalence evidence, or prior reviewed rewrite basis;
- action evidence limited to import, backend-load, selected bridge smoke-check, source-location, lifecycle prose, or deferred-execution evidence.

## Unavailable-Path Rule

If no accepted route basis exists because the reviewed native route is unavailable, not importable, cannot be started, and no accepted runtime-only compatibility glue, bounded equivalent implementation, or prior-reviewed algorithmic rewrite can satisfy the row, the production path must fail closed.

Acceptable fail-closed outcomes are typed failure evidence, repair evidence, `FAIL_WITH_REPAIRS`, `STOP_BEFORE_IMPLEMENTATION`, or a reviewed held-row status. A row with no accepted route basis must not produce successful strict output through synthetic state, dummy/random strict output, mock/fake backend behavior, or contract-only strict-output generation.

## Long-Running Route Observation Rule

Runtime observation evidence is required only when a reviewed native route or accepted build-time equivalent route has actually started during build and has not completed because it is long-running. Do not fail it solely for elapsed time.

If runtime execution is not attempted during build, record `build_callable_path_check_status=not_run_in_build` or equivalent bounded build-check status. This is not a runtime observation state and must not be used as evidence that runtime strict output was produced.

A started long-running route can remain in repair/observation state when runtime strict output has not yet been produced.

## Evidence Shape

The audit is recorded as internal evidence for `action_path_closure`. It does not create a separate completion matrix column.

Recommended per-row evidence shape:

```yaml
anti_surrogate_audit:
  audit_template: docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md
  production_path_checked: true
  route_basis: native | runtime_only_compatibility_glue | bounded_equivalent_implementation | prior_reviewed_algorithmic_rewrite
  compatibility_glue_used: false
  bounded_equivalence_evidence:
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
  mock_or_fake_backend_used: false
  placeholder_or_dummy_state_used: false
  contract_only_strict_output_generation_used: false
  same_surface_preexisting_target_used: false
  fail_closed_when_no_accepted_route_basis: true
  code_located_action_evidence:
    implementation_file:
    implementation_symbol_or_anchor:
    reachable_layer3_to_layer4_call_path:
    executable_import_or_call_anchor:
    action_name_only_metadata_used: false
  audit_verdict: pass
  evidence_path_or_symbol:
```

`runtime_observation` is populated only when a bounded build check actually starts the route and the route is still running, stopped, or failed with observation evidence.

`audit_verdict=pass` is valid only when the evidence shows that the reachable production path uses reviewed native action, runtime-only compatibility glue with preservation evidence, bounded equivalent implementation with lightweight equivalence evidence, or prior-reviewed algorithmic rewrite, and none of the hard reject conditions apply.

`audit_verdict=pass` requires code-located executable evidence. The audit cannot pass when the reviewed route basis appears only in strings, YAML fields, comments, lifecycle prose, `MethodState`, or other metadata.
