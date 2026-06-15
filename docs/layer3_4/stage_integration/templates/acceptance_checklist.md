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
- [ ] Pre-Gate2 default environment planning is analysis-problem-level, not one build target per method.
- [ ] Pre-build environment planning records reviewed Layer3 parent-function / method-route binding scope, not final callable paths.
- [ ] Final Layer3 callable paths are produced later by `layer3_layer4_build` in `build_output_result.yaml`.
- [ ] Method Dependency Groups organize method evidence and are not treated as Environment Build Targets.
- [ ] Method Dependency Groups do not receive `harness_environment.yaml` output paths before reviewed build evidence or later review creates a separate target.
- [ ] Environment build target keys are path-safe and human-readable.
- [ ] Pre-Gate2 environment build targets are not described as reviewed until Gate 2 approves the planning item.
- [ ] `environment_branch` records the reviewed path-safe environment binding key after build execution.
- [ ] Environment branch names describe compatible method scope using `<analysis_problem_code>_base`, `<analysis_problem_code>_<METHOD>`, or a reviewed method-set key.
- [ ] Analysis-specific build target naming is recorded without hardcoding one domain's base globally.
- [ ] Method Dependency Group and assembly-order rows preserve include, defer, compare-only, handled-elsewhere, optional, and out-of-scope boundaries without treating them as BioHarness method exclusion.
- [ ] Evidence pointers include the reader artifact and source config locator when available.
- [ ] Environment planning records a Manifest Cross-Check Table for methods with README/install docs, package metadata, or dependency manifest sources.
- [ ] Manifest cross-check hits that affect the selected execution path are reflected in the Conda Build Spec or Load Check Attribution Plan.
- [ ] Manifest versions are treated as Source Version Anchors unless the reviewed compatibility boundary records a hard constraint.
- [ ] GPU, CUDA, and hardware constraints are separated as environment build uncertainty.
- [ ] Selected PyTorch/PyG training, fitting, or embedding-learning paths record a CUDA runtime target when host GPU evidence is available.
- [ ] PyTorch/PyG CUDA checks record host GPU evidence, PyTorch CUDA build, PyG extension package variants, and `torch.cuda.is_available()`.
- [ ] Seurat-backed methods record Seurat version, SeuratObject version, and selected source API family.
- [ ] Seurat V4-style and V5-style API paths are handled as separate compatibility families unless reviewed source compatibility evidence covers the selected path.
- [ ] No install, solve, import/load, build execution, or runtime support claim is made from text triage.
- [ ] Text evidence does not determine environment branch splits.
- [ ] Split triggers do not create output paths before reviewed build evidence or later review.
- [ ] Environment build planning records assembly order and split response.
- [ ] Environment build planning records package-manager/source-build policy for high-risk dependency families.
- [ ] Environment build plans include load-check attribution units before execution.
- [ ] Route-level backend load targets are bounded package/module/library/source-package/component checks, not workflow execution.
- [ ] Package-level isolation checks are required when a check unit fails.
- [ ] Environment build failures follow repair-first handling before held-out evidence.
- [ ] Clean environment branch retry is used when covered by reviewed branch policy and base scope cannot support the relevant method scope.
- [ ] API drift, import-path drift, package-layout, object-conversion, file/cache-layout, and glue-code failures are routed to compatibility-rewrite handoff when the scientific core is unchanged.
- [ ] Evidence recording supports repair, branch selection, rewrite handoff, or held-out decisions; it is not treated as the environment build goal.
- [ ] Branch split requires reviewed build evidence, impossible documented constraints, or re-review.
- [ ] Environment execution uses the Gate 2-reviewed filled environment integration planning record.
- [ ] Environment execution uses the assigned step, output path, and Gate 2 human review table.
- [ ] Environment build execution has a reviewed Output State Policy before existing outputs/prefixes are deleted, overwritten, archived, or appended.
- [ ] Environment integration planning includes an Environment Build Plan.
- [ ] Environment build output directory contains `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl`.
- [ ] `harness_environment.yaml` is a reviewed environment binding record, not final agent-facing UI.
- [ ] `compatible_methods` contains only methods with route-level backend load evidence for the selected Layer4 route.
- [ ] `consumable_surface_scope` uses exact BioHarness execution surface names only.
- [ ] Held or conditional surfaces are recorded under `held_surfaces`, not inside consumable surface strings.
- [ ] Dependency-family load evidence and source locator evidence are not used as method compatibility evidence by themselves.
- [ ] `environment_build.yaml` is pure conda YAML without default `prefix:`.
- [ ] `environment_build.jsonl` records engineering build events only.
- [ ] `runtime_environment_selection.tsv` has `analysis_problem`, `environment_branch`, `compatible_methods`, `conda_prefix`, `harness_environment_yaml`, and `compatibility_note`.
- [ ] Successful environment branches are reflected in `runtime_environment_selection.tsv`.
- [ ] Successful environment outputs use the same branch key in output path, conda prefix, `harness_environment.yaml`, and `runtime_environment_selection.tsv`.
- [ ] Rerun prompts name stale environment/build/implementation artifacts and state whether each root is deleted, archived, reused as input evidence, or left untouched.
- [ ] Invocation prompts remain thin and do not define phase execution policy.
- [ ] Bridge planning, Gate 2 review tables, functional testing planning, and invocation prompts record instance facts and reviewed input boundaries without defining Layer3/Layer4 build completion, verifier cadence, publication gating, output schemas, or `downstream_selectable` rules.
- [ ] Formal harness presentation is later than engineering implementation/review workflows.
- [ ] Environment planning files do not record actual conda execution results.
- [ ] Environment execution files do not run method workflows or claim parent-function support.
- [ ] Filled environment integration planning records belong in NAS, not repo docs.
- [ ] Functional testing planning files do not record observed outputs, runtime metrics, or observed pass/fail.
- [ ] Author-case execution files record preparation, reference, and native-observation evidence.
- [ ] Method validation files record BioHarness harness results after prepared canonical input, `REFERENCE_READY` evidence, reviewed environment evidence, downstream-selectable Layer3/4 rows, output-contract evidence, and verifier acceptance are available.
- [ ] Validation planning manifests do not claim author-case execution or BioHarness validation evidence from static examples.
- [ ] Backend-native input/output differences are recorded as Layer4 alignment work rather than exposed in the Layer3 contract.
- [ ] Semantic output mismatches are not hidden as adapter or wrapper work.
- [ ] Environment state is planning-only unless backed by reviewed environment build output, runtime, or validation evidence.
- [ ] Evaluation plan distinguishes native-behavior comparison from biological correctness.
- [ ] Storage boundary between repo summaries and NAS full records is explicit.
- [ ] No runtime support or production readiness is claimed without implementation-backed evidence.

## Layer3 / Layer4 Build Output

- [ ] Layer3/Layer4 build review uses `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md`.
- [ ] The reviewed build package follows `layer3_layer4_build.md` and the referenced `layer3_layer4_*` templates.
- [ ] Layer3/Layer4 build review includes anti-surrogate audit through action-path closure, not as a separate downstream validation claim.

## Cross-Phase Planning Preconditions

- [ ] Critical backend entrypoints are identified.
- [ ] Critical parameter mappings are identified.
- [ ] Critical output mappings are identified.
- [ ] The required initial Environment Build Target, Conda Build Spec, step-by-step Environment Build Plan, rollback/split responses, and reviewed build output path are specified before environment build execution; additional split targets are specified only after reviewed build evidence or later review creates them.
- [ ] Author-case functional testing plan exists, or blocked/deferred author cases are recorded with evidence.
- [ ] Synthetic or minimal BioHarness-created fixtures are not used as substitutes for blocked author cases in the current functional-testing stage.
- [ ] Output-contract observation plan exists.
- [ ] Provenance observation plan exists.
- [ ] Remaining review-return conditions are explicit before author-case preparation or method validation.

## Method Validation

- [ ] Validation scope names included and excluded methods.
- [ ] Each included method has input-preparation evidence; methods with `REFERENCE_READY` have harness-validation evidence when dispatched to Stage3, and methods with `REFERENCE_FAIL` have complete Stage2 `failure_evidence` instead of harness-validation evidence.
- [ ] Canonical validation input exists before method harness validation starts.
- [ ] Method validation input preparation records data acquisition, canonical AnnData preparation, and `prepare_spatial_domain_input` readiness before Stage 2.
- [ ] Reference preparation records `REFERENCE_READY` with artifacts or `REFERENCE_FAIL` with complete `failure_evidence`.
- [ ] Method harness validation consumes reviewed environment evidence and downstream-selectable Layer3/4 build rows.
- [ ] Terminal method results are written only from verifier-accepted harness validation attempts.
- [ ] Reference-preparation gaps are verifier repair evidence until they produce `REFERENCE_READY` or `REFERENCE_FAIL`.
- [ ] Method validation uses stage-gated orchestration from `docs/layer3_4/method_validation/method_validation_workflow.md`.
- [ ] Input preparation, reference preparation, and harness validation each have verifier acceptance.
- [ ] Each stage dispatches method subagents in batches of at most 6 active methods.
- [ ] Only methods accepted as `INPUT_READY` enter reference preparation.
- [ ] Only methods accepted as `INPUT_READY` and `REFERENCE_READY` enter method harness validation.

## Post-Implementation Coherence Review

- [ ] Any post-implementation coherence review is recorded as ordinary evidence, not as a named gate or production-readiness decision.
- [ ] Production readiness remains separate from build, validation, and coherence-review evidence.

## Production Readiness

- [ ] Runtime implementation exists.
- [ ] Reproducible environment exists.
- [ ] Approved functional or runtime validation run has passed within stated bounds.
- [ ] Output contract has been observed.
- [ ] Provenance has been emitted.
- [ ] Native-behavior comparison is complete within stated bounds.
- [ ] Remaining non-equivalences are documented.
