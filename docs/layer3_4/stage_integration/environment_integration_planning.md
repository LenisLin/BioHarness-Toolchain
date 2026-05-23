# Environment Integration Planning

## Purpose

This file defines the pre-Gate2 environment integration planning file for a method set within one analysis problem or feature.

Environment integration planning starts after Gate 1 parent-function / execution-surface alignment and method-to-parent Layer4 bridge planning exists. It organizes static environment evidence into Text Anchors, Method Dependency Groups, Environment Assembly Order, Split Triggers, one analysis-problem-level Environment Build Target by default, and a Gate-2-reviewable Environment Build Plan for host conda environment assembly.

It does not run conda, pip, R installation, Python imports, R loads, bridge loads, GPU checks, method workflows, author cases, data downloads, or validation runs. It does not establish executable support, runtime support, functional correctness, production readiness, or final implementation support.

Each method receives one dependency evidence organization pass. Parent-function and Layer4 bridge context is used to identify selected core paths and gated optional paths; it should not cause a full environment plan to be repeated for every execution surface or one Environment Build Target/output path to be created for every method.

## Inputs

- Environment Config Reader outputs.
- Audit-closed environment evidence from integration-readiness audit.
- Package review environment gaps.
- Method requirements surfaced by `method x parent function` Layer4 bridge planning.
- Optional path notes from code/output readers when they affect runtime dependencies.
- Storage/runtime conventions for reviewed environment build outputs.

## Core Terms

| Term | Meaning | Boundary |
| --- | --- | --- |
| Text Anchor | Author-visible environment evidence such as package names, exact pins, language requirements, GPU/CUDA notes, R/Python bridge notes, install files, CI files, or container cues. Exact package pins, Python/R/CUDA versions, and similar author-visible version statements are Source Version Anchors. They support risk ordering, compatibility review, and candidate resolution. | A Text Anchor supports risk ordering and planning only. It is not installability evidence, is not a default conda hard pin, and does not by itself justify environment splitting. |
| Method Dependency Group | The organized dependency evidence for one method or one method path, including selected core dependencies, optional/deferred dependencies, source locators, and risks. | It is not an Environment Build Target and has no `harness_environment.yaml` output path by default. |
| Environment Assembly Order | The planned order for assembling dependency groups into the analysis-problem-level environment build plan. | It guides later build execution after review; it is not execution evidence. |
| Split Trigger | A recorded risk that may require targeted repair, re-review, or a later split decision, such as version, language, GPU/CUDA, R-bridge, package-manager, or system conflicts. | It records planning risk only. It does not create an output path, final branch, or split target before reviewed build evidence or later review. |
| Environment Build Target | A path-safe human-readable output-organization key for a reviewed host conda assembly within one analysis problem. | It is the Gate-2-reviewed execution/output target for the Environment Build Plan, not a default per-method object or final environment branch split. |
| Environment Build Plan | A Gate-2-reviewable plan for host conda assembly order, checks, outputs, and failure/split response. | It is execution guidance only after Gate 2 approves the item and assigns `environment_build_execution`. |
| Conda Build Spec | The Gate-2-reviewable conda channels, dependency families, pip dependency families, candidate resolution policy, source anchors, and excluded optional dependencies for an environment build target. | It is a reviewed assembly policy, not a mechanical concatenation of every Source Version Anchor, not a solved environment claim, and not a final branch split. Actual resolved versions are recorded by environment build evidence. It does not include Docker build scope. |
| Reviewed Output State Policy | The reviewed response for pre-existing output directories, stale conda prefixes, previous failed evidence, append-vs-overwrite behavior, and evidence preservation after rebuild. | It is required before execution deletes, overwrites, archives, appends to, or mixes history in existing outputs or prefixes. Missing policy routes to targeted planning repair or Gate 2 re-review. |
| Reviewed Environment Binding Record | The minimal `harness_environment.yaml` record produced after reviewed environment build execution. | It records reviewed method / Layer3 binding scope / `environment_branch` / `conda_prefix` binding. `environment_branch` is the reviewed path-safe binding key for a successful environment output. Detailed branch naming is defined in Environment Branch Naming. Before `layer3_layer4_build` produces `build_output_result.yaml`, this scope is a reviewed parent-function / method-route binding scope, not a final callable path. |

## Method-Centered Boundary

Environment integration planning starts from method-level environment evidence. For each method, identify the dependency sources, author-stated constraints, required runtime ecosystem, Text Anchors, optional paths, selected core paths, and Method Dependency Group once.

Use parent-function and Layer4 bridge hypotheses only to mark which method paths are core for the selected integration plan and which paths are optional, deferred, or out of scope. Do not create duplicate full environment plans for every execution surface unless the method genuinely requires separate runtime stacks for distinct selected paths.

Method Dependency Groups are evidence organization records. They do not imply one Environment Build Target per method, do not receive per-method environment output directories, and do not have `harness_environment.yaml` output paths unless later reviewed build evidence or review creates a separate target.

Environment integration planning consumes audit-closed repository evidence. It may organize text conflicts, core/optional boundaries, Method Dependency Groups, an Environment Assembly Order, Split Triggers, and host conda build plans. It does not reopen environment repository reading or use static evidence as installability proof.

Gate 2 downstream planning review assigns review results to environment integration planning items after checking whether static evidence identifies the analysis-problem Environment Build Plan or initial Environment Build Target, selected core dependency boundary, gated optional dependency boundary, Split Triggers, output path, failure response, and required build outputs.

## Text Compatibility Triage

Text compatibility triage is the first substep inside environment integration planning. It is not a new gate, a separate top-level workflow stage, or an execution action. It turns static environment evidence into a review-ready text/source evidence section inside the filled environment integration planning record.

Read author-visible environment evidence before planning local assembly. Use README and install documentation, `pyproject.toml`, `setup.py`, `requirements.txt`, `environment.yml`, lockfiles, Dockerfiles, CI files, optional dependency notes, resource notes, and environment-reader locators when present.

This substep uses Environment Config Reader outputs, Gate 1 scope, downstream bridge-planning context, environment integration inputs, and evidence records. Gate 2 human review output should record the filled planning file path, reviewed item, review result, assigned step, output path, and evidence boundary for environment planning items that enter environment build execution. Evidence records should identify both the reader output and the source config locator when available.

The goal is to organize methods and source evidence into review-ready Method Dependency Groups, Environment Assembly Order, Split Triggers, and one initial analysis-problem Environment Build Target by default, with handled-elsewhere records, deferred records, comparison-only records, or out-of-scope records where needed, before any local conda solve, install, import/load check, GPU check, R load, author-case run, data download, or method run is planned. Absence of a visible text conflict should be recorded as build-time uncertainty, not as installability evidence.

Use positive routing language. Prefer `defer`, `handled elsewhere`, `compare_only`, or `out_of_scope` over describing a method as infeasible unless reviewed build output or an impossible documented constraint justifies that conclusion.

The initial Environment Build Target should use a path-safe human-readable key for one analysis problem. Prefer `<analysis_problem_code>_<build_target_label>`, such as `SDI_environment_build_plan` for a spatial-domain-identification build plan. Natural-language role descriptions belong in `Build Target Role` or `compatibility_note`, not in the path key. Do not hardcode Python AnnData/Scanpy as the global default base for all analysis problems.

Hardware, GPU, CUDA, and driver constraints should be recorded separately as build-time uncertainty. Author-visible CUDA version differences do not become text-stage incompatibilities by themselves; they identify planned checks inside an Environment Build Plan. Exact pins are Text Anchors. They indicate where risk should be reviewed first, but they do not determine split decisions. Solve results, import/load results, GPU results, R load results, and author-case behavior can only come from execution evidence, not from text triage.

### Dependency Constraint Interpretation

Author-visible version pins are Source Version Anchors unless the reviewed plan records a narrower compatibility boundary from package metadata, source API use, ABI needs, or execution evidence. Environment planning must separate source anchors from solver constraints.

A reviewed Environment Build Plan may define a Flexible Resolution Policy. Under that policy, execution may allow conda/mamba to resolve compatible package versions within the reviewed dependency family and source/config boundary. This is not dependency broadening when it remains inside reviewed method dependency groups and source references.

For R-dependent method groups, `R >=3.6` is a minimum execution-time runtime floor. It is not a default hard pin and does not override stricter reviewed source/package requirements such as `R >=4.0.0` or `R >=4.0.3`.

### Reusable Prompt

Use this prompt pattern to generate the review-ready filled environment integration planning record:

```text
Inputs:
- Environment Config Reader outputs, including reader artifact paths and source config locators.
- Gate 1 closure and current downstream integration scope.
- Method-to-parent Layer4 bridge planning context.
- Current-pass method/path scope available before Gate 2.
- Environment integration inputs, including selected core paths, optional paths, and evidence records.

Work:
- Define one analysis-problem-level initial Environment Build Target for the current analysis problem.
- Record method-level Text Anchors.
- Record Method Dependency Groups for method-specific dependency evidence.
- Record Environment Assembly Order across dependency groups.
- Record Split Triggers for version, language, GPU/CUDA, R-bridge, package-manager, or system conflicts found from text evidence.
- Separate author-visible package/runtime constraints from planned build checks.
- Record GPU/CUDA/hardware/R bridge uncertainty as Environment Build Plan checks, not as text-stage installability or incompatibility proof.
- Prepare one Gate-2-reviewable Environment Build Plan for host conda environment assembly unless a later reviewed result creates a separate target.

Boundary:
- Do not run conda solve, install, import/load checks, GPU checks, R loads, data downloads, method runs, or author cases.
- Do not reopen Gate 1 or Gate 2.
- This planning step does not assign a Gate 2 review result and does not approve execution/build. It prepares Text Anchors, Method Dependency Groups, Environment Assembly Order, Split Triggers, an initial Environment Build Target, selected dependency boundaries, Conda Build Specs, step-by-step build instructions, rollback/split responses, and required build outputs for Gate 2 review.
- Do not create method-specific environment output paths or `harness_environment.yaml` paths from pre-Gate2 text evidence.
- Do not copy filled method-specific evidence into repo docs; filled planning files belong in the NAS results workspace.

Output:
- A review-ready filled environment integration planning record containing Evidence Roots, Text Anchor Table, Method Dependency Group Table, Environment Assembly Order Table, Split Trigger Table, Environment Build Target Summary, Conda Build Spec for the initial build target, Step-By-Step Build Instructions, Load Check Attribution Plan, Reviewed Output State Policy, Required Environment Build Outputs, Selection Index Handoff, and Non-Claims.
```

### Text Anchor Table

Use `Method` for text/source evidence. Do not use Layer3 binding-scope or interface-target columns in this table.

| Method | Text Anchor Type | Text Anchor | Source Locator | Planning Implication | Non-Claim |
| --- | --- | --- | --- | --- | --- |

### Method Dependency Group Table

Use `Method Dependency Group` for method-specific dependency evidence. Do not use group labels as output directories unless later reviewed build evidence or review creates a separate Environment Build Target.

| Method Dependency Group | Method | Selected Core Dependency Boundary | Optional / Deferred / Handled Elsewhere | Source Evidence / Locator | Planned Assembly Role | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- |

### Environment Assembly Order Table

| Assembly Order | Method Dependency Group(s) | Assembly Purpose | Planned Checks After Review | Dependency Boundary | Failure / Repair Routing |
| --- | --- | --- | --- | --- | --- |

Environment Assembly Order may be risk-first. A reviewed plan may start from the most constrained or highest-risk dependency group, add groups progressively, and require evidence after each solve or load check. This ordering is planning and execution-control guidance only; it is not a runtime success claim, workflow success claim, or installability claim before execution evidence exists.

### Split Trigger Table

| Split Trigger | Affected Method Dependency Group(s) | Evidence Anchor / Source Locator | Risk Type | Planning Response | Split Decision Boundary |
| --- | --- | --- | --- | --- | --- |

Split Triggers can record version, language, GPU/CUDA, R-bridge, package-manager, system, or optional-path conflicts. They do not create output paths before reviewed environment build evidence or later review.

A reviewed Environment Build Plan may include a Reviewed Branch Policy. If Gate 2 approves that policy, execution may create branch outputs only after explicit execution-stage evidence, using the reviewed `environment_branch` and output path rules. The policy is reviewed; future concrete branch names are produced during execution from compatible method scope.

## Environment Build Plan

The Environment Build Plan replaces old target-list planning as the reviewable environment execution plan. It must give Gate 2 and later execution enough detail to assemble or update the planned host conda environment build target after review, run planned load checks, write the three required output files, and respond to failure without broad rereading.

### Environment Build Target Summary

Use `Reviewed Layer3 Binding Scope` for build/harness routing. In pre-build environment planning, this records the reviewed Layer3 parent-function / method-route binding scope that the environment is intended to support. It is not a final `callable_path`; final callable paths are produced later by `layer3_layer4_build` in `build_output_result.yaml`. The reviewed scope must use BioHarness Layer3 planning language, not original repository paths, tutorials, native module paths, source config locators, or reader artifacts.

| Environment Build Target | Analysis Problem | Reviewed Layer3 Binding Scope | Compatible Methods Planned | Output Path | Scope Boundary |
| --- | --- | --- | --- | --- | --- |

Required Environment Build Outputs attach to this reviewed build target and output path. They do not attach to every Method Dependency Group.

### Conda Build Spec

The Conda Build Spec records the Gate-2-reviewable host conda environment build target specification. It records reviewed dependency families, source anchors, candidate resolution policy, and excluded optional paths. It is a planned assembly spec before Gate 2 review, not a solved environment, hard-pinned concatenation of all Source Version Anchors, or branch split. The current stage integration workflow supports host conda environment build, update, and check only; Docker build is out of scope.

| Environment Build Target | Conda Environment Name Or Prefix Policy | Channels | Dependencies | Pip Dependencies | Explicitly Excluded Optional Dependencies | Source / Config References |
| --- | --- | --- | --- | --- | --- | --- |

`Source / Config References` lists the exact reviewed references that execution may consult if needed. Execution may not broad reread the repository or expand dependency scope from unreviewed files.

### Step-By-Step Build Instructions

| Step Order | Environment Build Target | Planned Action | Command Intent | Planned Load Check | Expected Output File Update | Failure Response |
| --- | --- | --- | --- | --- | --- | --- |

The step list should allow execution to proceed in order through:

- conda environment create or update for the Gate-2-reviewed build target;
- planned package, Python import, R library, bridge, GPU, or hardware visibility checks when included in the plan;
- writing `environment_build.yaml` as a pure conda YAML with no default `prefix:`;
- writing `harness_environment.yaml` as the reviewed environment binding record;
- appending actual events to `environment_build.jsonl` in reviewed step order.

Each step should specify the failure response. Reviewed responses should describe how execution records evidence inside the reviewed boundary, including primary output evidence, covered branch evidence, rollback to a reviewed spec, package-level isolation evidence, and compatibility rewrite handoff evidence.

When the planned dependency boundary includes ABI-sensitive dependency families such as PyTorch, torchvision, PyTorch Geometric, PyG extension packages, R/Rcpp stacks, Python/R bridge packages, native image libraries, or other compiled dependency families, the Step-By-Step Build Instructions must record a risk-ordered assembly strategy. The strategy must identify which dependency family is installed first, which invariant checks are run after that family, and which invariant checks are repeated after later high-risk updates.

For PyTorch/PyG targets, the plan must require an official PyTorch/PyG ABI bundle check before later dependency-family updates and another ABI bundle check after those updates when the same prefix is retained.

### Environment Branch Naming

Environment branch names describe the compatible method scope supported by the successful environment output. The filled plan must record the analysis problem code used for branch names, the base branch name, and the method or reviewed method-set naming rule for branch outputs created after execution evidence.

### Load Check Attribution Plan

Planned load checks must be attributable to a method dependency group or reviewed method scope. A combined check may be used only after the individual check units have passed. When a check unit fails, execution records package-level isolation results before deciding compatible method scope for any branch output.

When a check unit fails, the filled plan must require package-level or library-level isolation before branch assignment. The isolation result should determine whether execution first attempts a package-level or dependency-family repair in the base environment, creates a reviewed branch, records a compatibility rewrite handoff candidate, or records failed or held-out evidence. A first failed solve, import, or load result should not be treated as direct branch evidence without this attribution step.

| Check Unit | Method Dependency Group(s) | Method Scope | Packages / Libraries To Check | Package-Level Isolation Required | Evidence Recorded In |
| --- | --- | --- | --- | --- | --- |

### Reviewed Output State Policy

The Reviewed Output State Policy controls pre-existing output directories, stale conda prefixes, previous failed evidence, append-vs-overwrite behavior, and whether old evidence remains durable after rebuild. It must be reviewed before `environment_build_execution` deletes, overwrites, archives, appends to, or mixes history in any existing output path, branch output path, or `conda_prefix`.

| Existing State | Applies To | Reviewed Response | Evidence Preservation Rule | Allowed Mutation Boundary | Covered State Handling |
| --- | --- | --- | --- | --- | --- |
| `<no prior output / existing output directory / existing branch directory / stale conda_prefix / previous failed evidence / existing selection-index row>` | `<primary output path, branch output path, conda_prefix, environment_build.jsonl, runtime_environment_selection.tsv row>` | `<stop / overwrite / append / archive then rebuild / reuse after check / remove stale prefix / other reviewed response>` | `<which prior files, logs, failed evidence, or old rows remain durable and where>` | `<exact path, prefix, row, or file set that may be mutated>` | `<covered action for this observed state; leave uncovered states out of execution approval>` |

Execution approval covers only observed states listed in this policy. The filled plan should cover any output directory, branch output path, `conda_prefix`, failed evidence, or selection-index row expected at invocation time.

### Reviewed Branch Policy

The branch policy maps execution evidence to compatible method scope and environment branch names. The broad successful environment uses `<analysis_problem_code>_base`. A single-method successful branch uses `<analysis_problem_code>_<METHOD>`. A method-set branch requires an explicit reviewed method-set name in the filled plan.

| Branch Condition | Evidence Required | Compatible Method Scope | Environment Branch Name Rule | Output Path Rule | Conda Prefix Rule | Remaining Check Policy |
| --- | --- | --- | --- | --- | --- | --- |

### Rollback And Split Response

| Trigger | Reviewed Response | Split Response Allowed | Reviewed Evidence Handling | Notes |
| --- | --- | --- | --- | --- |

Rollback and split responses stay inside the reviewed dependency boundary. The filled plan records the branch evidence, rollback evidence, or compatibility handoff evidence that execution writes for each covered response.

Text evidence records risk ordering only. Execution-stage build evidence determines whether a reviewed branch output is produced.

If the reviewed Environment Build Plan includes a Reviewed Branch Policy, execution creates branch output after execution evidence identifies a compatible method scope for a base, single-method, or reviewed method-set environment branch. A branch must not introduce an unreviewed dependency family, source/config reference, method, optional path, Layer3 binding scope, or interface target.

Rollback and split response planning must use this escalation order for covered failures:

1. package-level or dependency-family attempt inside the reviewed dependency boundary;
2. reviewed branch creation only after evidence shows the base cannot support the relevant compatible method scope;
3. compatibility rewrite handoff candidate when the remaining issue is a code compatibility concern rather than an environment solve concern;
4. failed or held-out evidence when success would require unreviewed dependency scope, source references, methods, optional paths, data download, downstream execution, code rewrite, algorithmic rewrite, or Layer3 binding scope.

The filled plan should distinguish clean-prefix retry, package-level isolation, branch evidence, compatibility rewrite handoff, and held-out failure evidence as separate response types.

### Compatibility Rewrite Handoff

Environment planning may record compatibility rewrite candidates when dependency or version evidence suggests old APIs, glue code, file layout, object conversion, artifact export, logging, visualization, or dependency migration issues.

Environment build execution must not implement code rewrites. Compatibility rewrite candidates are handed off to `layer4_bridge_planning` or `layer3_layer4_build`. If the candidate affects graph construction, model fitting, loss functions, inference, clustering, post-processing, stochastic behavior, or GPU/CPU numerical path, it requires stronger review as possible `algorithmic_rewrite`.

### Required Environment Build Outputs

The Gate-2-reviewed output path for the reviewed Environment Build Target must contain:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

| Output File | Required Content | Boundary |
| --- | --- | --- |
| `harness_environment.yaml` | Reviewed environment binding record with `analysis_problem`, `environment_branch`, `conda_prefix`, `compatible_methods`, and `compatibility_note`. `environment_branch` uses the reviewed branch name rule from the Environment Build Plan. `compatible_methods` comes only from the compatible method scope of the successful final event for that environment branch. If `layer3_interface_paths` is retained inside `compatible_methods`, it may refer to the reviewed Layer3 binding scope before final callable paths exist. | Uses BioHarness Layer3 planning/interface language only; `layer3_interface_paths` must not be native repository paths, source config locators, tutorials, reader artifacts, or final `callable_path` claims before `build_output_result.yaml` exists. Does not include status, build ID, provider, log, reproducibility, Gate 2, or non-claim fields. |
| `environment_build.yaml` | Pure conda YAML for the Gate-2-reviewed build target. | Defaults to no `prefix:`. |
| `environment_build.jsonl` | Actual execution events in the same order as the reviewed plan steps. | Records environment build events only. |

### Selection Index Handoff

Core branch outputs remain `harness_environment.yaml`, `environment_build.yaml`, and `environment_build.jsonl` in each successful environment build output directory.

Successful primary or branch outputs must be eligible for `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/runtime_environment_selection.tsv` indexing after execution. Failed outputs are evidence only and are not downstream-selectable.

The selection index handoff should identify the expected `analysis_problem`, `environment_branch`, `compatible_methods`, `conda_prefix`, `harness_environment_yaml`, and `compatibility_note` values to be derived from successful reviewed build outputs. The selection TSV records only successful `environment_branch` values. Row replacement or removal for an existing `environment_branch` must follow the Reviewed Output State Policy.

## Execution Scope After Gate 2

When Gate 2 approves an environment planning item for `environment_build_execution`, execution follows the reviewed Environment Build Plan in the filled planning record. Execution may inspect only the source/config references listed in the reviewed plan. It may not extend dependency scope, add split targets, add Layer3 binding scopes or interface targets, or reinterpret method routing. Execution produces evidence only for reviewed dependency scope, branch scope, output paths, prefix rules, source/config references, and Layer3 binding scope.

## Core Path And Optional Path Handling

Core path dependencies are dependencies required by the selected Layer4 bridge path. They should be evaluated for the environment build target that would run the selected execution surface.

Optional paths are gated. Examples include non-selected clustering alternatives, GPU extras, plotting extras, image/reporting utilities, and acceleration paths. Optional paths should be excluded from shared core build targets unless explicitly selected by Layer4 bridge planning. Optional paths may have separate build target plans when Gate 2 reviews them.

| Method | Dependency Path | Dependency Shape | Selected-Path Role | Default Inclusion | Planned Build Check Required | Boundary |
| --- | --- | --- | --- | --- | --- | --- |

Do not use optional dependency conflicts to reject a core path unless the optional path is required by the selected bridge path.

If the selected native path requires an R/Python bridge or an R-side dependency such as `mclust`, that dependency is part of the selected core dependency boundary for environment build planning. It should not be treated as optional merely because it lives in another language ecosystem.

## Non-Claims

Environment integration planning makes no installability claim.

It makes no runtime support claim.

It makes no production readiness claim.

It makes no final implementation support decision.

It makes no method workflow success claim.

It makes no author-case success claim.

It makes no biological correctness validation.
