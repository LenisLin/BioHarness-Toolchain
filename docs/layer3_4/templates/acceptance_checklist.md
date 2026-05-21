# Layer 3/4 Acceptance Checklist

## Static Design Review

- [ ] Feature container is recorded separately from callable parent-function candidates.
- [ ] Parent-function candidate has one canonical input contract.
- [ ] Parent-function candidate has one strict main output contract.
- [ ] Agent-facing surface contains no backend function names or package-private controls.
- [ ] Layer 2 method-selection logic is not copied into Layer 3.
- [ ] Layer 4 planning uses the current Gate 1 planning-route vocabulary.
- [ ] Parent-function candidate performs a real execution-layer action and is not only a check, audit, locator, or status-only report.
- [ ] Parent-function coverage records direct support, internal/no-op/not-applicable routes, and non-covered methods.
- [ ] The feature-level parent-function set covers retained methods' core functionality or explicitly routes mismatched methods out of the feature.
- [ ] Parent-function candidates are grouped by shared execution semantics before method-specific alignment routes are assigned.
- [ ] Fused or internal native stages are recorded as semantic evidence when appropriate, not automatically treated as unsupported methods.
- [ ] Method x parent-function planning-level alignment routes are recorded separately from final Layer4 support decisions.
- [ ] Planning-level alignment routes do not claim entry into implementation/build, runtime support, production readiness, or biological correctness.
- [ ] Gate 2 reviews current in-scope filled planning items from the downstream planning areas.
- [ ] Gate 2 review result is assigned to planning items, not methods or execution results.
- [ ] Each downstream planning item contains enough domain-specific fields or attached planning package references for Gate 2 to identify the reviewed target, required evidence, open question/blocker, evidence output path, evidence boundary, and repair or return target.
- [ ] Planning files raise required evidence and open planning questions; they do not approve execution/build.
- [ ] Gate 2 human review table records current in-scope reviewed planning items, assigned post-Gate2 steps, and output paths.
- [ ] Gate 2 review results use `approved_for_next_step`, `targeted_planning_repair_required`, or `return_to_gate1`.
- [ ] Gate 2 assigned steps use `environment_build_execution`, `layer3_layer4_build`, or `author_case_native_workflow_and_bridge_replay`.
- [ ] Environment build execution, Layer3/Layer4 build, and author-case/native workflow execution use Gate 2-reviewed planning items, assigned steps, output paths, and the Gate 2 human review table.
- [ ] Execution/build records are separate evidence records.
- [ ] Environment integration planning manifests do not claim installation, solve, import/load, or runtime execution.
- [ ] Environment text triage is inside environment integration planning, not a new Gate.
- [ ] Environment branch keys are path-safe and human-readable.
- [ ] `environment_branch` uses a path-safe human-readable key such as `<analysis_problem_code>_<branch_label>`.
- [ ] Analysis-specific base is recorded without hardcoding one domain's base globally.
- [ ] Native / Source Evidence Routing Table uses only `include`, `exclude`, `defer`, `compare_only`, or `out_of_scope` for `Action For This Branch`.
- [ ] Exclude-from-branch is not method exclusion from BioHarness.
- [ ] Evidence pointers include the reader artifact and source config locator when available.
- [ ] GPU, CUDA, and hardware constraints are separated as environment build uncertainty.
- [ ] No install, solve, import/load, build execution, or runtime support claim is made from text triage.
- [ ] Environment execution uses the Gate 2-reviewed filled environment integration planning record.
- [ ] Environment execution uses the assigned step, output path, and Gate 2 human review table.
- [ ] Environment integration planning includes an Environment Build Plan.
- [ ] Environment build output directory contains `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl`.
- [ ] `harness_environment.yaml` is a reviewed environment binding record, not final agent-facing UI.
- [ ] `harness_environment.yaml` uses minimal fields and BioHarness Layer3 interface paths.
- [ ] `environment_build.yaml` is pure conda YAML without default `prefix:`.
- [ ] `environment_build.jsonl` records engineering build events only.
- [ ] `runtime_environment_selection.tsv` has `analysis_problem`, `environment_branch`, `compatible_methods`, `conda_prefix`, `harness_environment_yaml`, and `compatibility_note`.
- [ ] Formal harness presentation is later than engineering implementation/review workflows.
- [ ] Environment planning files do not record actual conda execution results.
- [ ] Environment execution files do not run method workflows or claim parent-function support.
- [ ] Filled environment integration planning records belong in NAS, not repo docs.
- [ ] Functional testing planning files do not record observed outputs, runtime metrics, or observed pass/fail.
- [ ] Author-case execution files do not claim BioHarness support unless bridge replay and output-contract evidence exist.
- [ ] Validation planning manifests do not claim author-case execution or BioHarness validation evidence from static examples.
- [ ] Backend-native input/output differences are recorded as Layer4 alignment work rather than exposed in the Layer3 contract.
- [ ] Semantic output mismatches are not hidden as adapter or wrapper work.
- [ ] Environment state is planning-only unless backed by reviewed environment build output, runtime, or validation evidence.
- [ ] Evaluation plan distinguishes native-behavior comparison from biological correctness.
- [ ] Storage boundary between repo summaries and NAS full records is explicit.
- [ ] No runtime support or production readiness is claimed without implementation-backed evidence.

## Layer3 / Layer4 Build Output

- [ ] `layer3_layer4_build.md` defines the post-Gate2 workflow for `layer3_layer4_build`.
- [ ] `layer3_layer4_build` produces `build_output_result.yaml` and `build_audit.yaml`.
- [ ] `build_output_result.yaml` records `layer3_execution_surface`, `layer4_backend_binding`, `implementation_files`, `runtime_entry`, `import_experiment`, `next_evidence_needed`, and `boundary_checks`.
- [ ] `build_audit.yaml` records Gate 2 source, reviewed build scope, boundary checks, import experiment summary, non-claims, and next required evidence.
- [ ] Layer3 / Layer4 build does not use synthetic, minimal, toy, or BioHarness-created input objects.
- [ ] Layer3 / Layer4 build does not run author cases, method workflows, validation fixtures, or data downloads.
- [ ] Import experiments are bounded by reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.
- [ ] Author-case execution remains separate from Layer3 / Layer4 build.
- [ ] Build output does not claim runtime support, functional correctness, final support status, production readiness, algorithmic equivalence, or biological correctness.

- [ ] Critical backend entrypoints are identified.
- [ ] Critical parameter mappings are identified.
- [ ] Critical output mappings are identified.
- [ ] Required environment branches, Conda Build Specs, step-by-step Environment Build Plans, rollback/split responses, and reviewed build output paths are specified before environment build execution.
- [ ] Author-case functional testing plan exists, or blocked/deferred author cases are recorded with evidence.
- [ ] Synthetic or minimal BioHarness-created fixtures are not used as substitutes for blocked author cases in the current functional-testing stage.
- [ ] Output-contract observation plan exists.
- [ ] Provenance observation plan exists.
- [ ] Known blockers are explicit.

## Post-Implementation Integration Review

- [ ] Gate 3 post-implementation integration review has checked Layer4, environment, validation, output contract, provenance, and failure-handling coherence when required.
- [ ] Gate 3 acceptance, if present, is not treated as production readiness.

## Production Readiness

- [ ] Runtime implementation exists.
- [ ] Reproducible environment exists.
- [ ] Approved functional or runtime validation run has passed within stated bounds.
- [ ] Output contract has been observed.
- [ ] Provenance has been emitted.
- [ ] Native-behavior comparison is complete within stated bounds.
- [ ] Remaining non-equivalences are documented.
