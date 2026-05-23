# Environment Integration Planning Template

## Purpose

This template records a complete filled environment integration planning record for `<analysis problem or feature>`.

It organizes author-visible environment evidence into Text Anchors, Method Dependency Groups, Environment Assembly Order, Split Triggers, one analysis-problem-level initial Environment Build Target by default, and a Gate-2-reviewable Environment Build Plan for host conda environment assembly. It is a planning artifact only and does not determine final environment branch splits.

Filled records belong in the NAS results workspace. Do not copy filled method-specific evidence into repo templates or generic repo docs.

## Evidence Roots

| Evidence Root | Artifact / Locator | Scope Used | Notes |
| --- | --- | --- | --- |
| Environment Config Reader output | `<reader artifact path>` | `<method/config scope>` | `<notes>` |
| Source config locator | `<source config path or locator>` | `<config file or source location>` | `<notes>` |
| Gate 1 closure / downstream integration scope | `<Gate 1 artifact or downstream scope path>` | `<promoted/deferred/out-of-scope boundary>` | `<notes>` |
| Method-to-parent Layer4 bridge planning context | `<bridge planning artifact path>` | `<selected core and optional path boundary>` | `<notes>` |
| Storage/runtime convention | `<storage/runtime path or policy>` | `<planned output location>` | `<notes>` |

## Text Compatibility Triage

Text compatibility triage is a substep inside environment integration planning. It records source evidence, Method Dependency Groups, assembly order, and split triggers before any conda solve, environment create/update, package install, import/load check, method workflow, author case, data download, or validation run.

### Text Anchor Table

| Method | Text Anchor Type | Text Anchor | Source Locator | Planning Implication | Non-Claim |
| --- | --- | --- | --- | --- | --- |
| `<method A>` | `<package/version/language/GPU/CUDA/R bridge/system/optional>` | `<author-visible text>` | `<reader artifact and source config locator>` | `<assembly-order, risk-order, planned-check, or dependency-boundary implication>` | `<what this anchor does not prove>` |
| `<method B>` | `<package/version/language/GPU/CUDA/R bridge/system/optional>` | `<author-visible text>` | `<reader artifact and source config locator>` | `<assembly-order, risk-order, planned-check, or dependency-boundary implication>` | `<what this anchor does not prove>` |

### Method Dependency Group Table

Method Dependency Groups organize method-specific evidence. They are not Environment Build Targets and do not have `harness_environment.yaml` output paths unless later reviewed build evidence or review creates a separate target.

| Method Dependency Group | Method | Selected Core Dependency Boundary | Optional / Deferred / Handled Elsewhere | Source Evidence / Locator | Planned Assembly Role | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- |
| `<method_a_dependency_group>` | `<method A>` | `<selected core packages/language/runtime boundary>` | `<optional/deferred/handled-elsewhere paths>` | `<reader artifact and source config locator>` | `<base/early/mid/late/risk-isolated assembly role>` | `<planning boundary and non-claim>` |
| `<method_b_dependency_group>` | `<method B>` | `<selected core packages/language/runtime boundary>` | `<optional/deferred/handled-elsewhere paths>` | `<reader artifact and source config locator>` | `<base/early/mid/late/risk-isolated assembly role>` | `<planning boundary and non-claim>` |

### Dependency Constraint Interpretation

| Method Dependency Group | Source Version Anchor(s) | Flexible Resolution Policy | Compatibility Boundary | Resolution Evidence Required |
| --- | --- | --- | --- | --- |
| `<method_a_dependency_group>` | `<author-visible exact package/language/CUDA/R version text>` | `<resolver latitude within reviewed dependency family and source/config boundary>` | `<package metadata/API/ABI/source-use boundary, or unknown until execution evidence>` | `<environment_build.yaml resolved versions and environment_build.jsonl solve/load event>` |
| `<method_b_dependency_group>` | `<author-visible exact package/language/CUDA/R version text>` | `<resolver latitude within reviewed dependency family and source/config boundary>` | `<package metadata/API/ABI/source-use boundary, or unknown until execution evidence>` | `<environment_build.yaml resolved versions and environment_build.jsonl solve/load event>` |

### Environment Assembly Order Table

| Assembly Order | Method Dependency Group(s) | Assembly Purpose | Planned Checks After Review | Dependency Boundary | Failure / Repair Routing |
| --- | --- | --- | --- | --- | --- |
| `1` | `<method dependency group(s)>` | `<establish shared base or first dependency family>` | `<checks after Gate 2 only>` | `<dependencies included at this step>` | `<record evidence / continue covered branch checks / produce covered branch evidence>` |
| `2` | `<method dependency group(s)>` | `<add next dependency family or language bridge>` | `<checks after Gate 2 only>` | `<dependencies included at this step>` | `<record evidence / continue covered branch checks / produce covered branch evidence>` |

### Split Trigger Table

| Split Trigger | Affected Method Dependency Group(s) | Evidence Anchor / Source Locator | Risk Type | Planning Response | Split Decision Boundary |
| --- | --- | --- | --- | --- | --- |
| `<trigger key>` | `<method dependency group(s)>` | `<text anchor and source locator>` | `<version/language/GPU/R bridge/system/package-manager/optional>` | `<planned check and reviewed evidence response>` | `No output path or split target before reviewed build evidence or later review.` |

## Environment Build Plan

This section is the Gate-2-reviewable plan for `environment_build_execution`. It must be specific enough for execution to follow step by step without broad rereading or expanding dependency scope.

### Environment Build Target Summary

This summary records the reviewed Layer3 parent-function / method-route binding scope that the environment is intended to support. It does not require final callable paths before build; final `callable_path` values are produced later by `layer3_layer4_build` in `build_output_result.yaml`.

| Environment Build Target | Analysis Problem | Reviewed Layer3 Binding Scope | Compatible Methods Planned | Output Path | Scope Boundary |
| --- | --- | --- | --- | --- | --- |
| `<initial build target, e.g. SDI_environment_build_plan>` | `<analysis problem>` | `<reviewed Layer3 parent-function / method-route scope; not native repo paths or final callable paths>` | `<methods covered by the initial plan>` | `<environment build output directory for the initial target>` | `<what is in and out of build target scope>` |

### Conda Build Spec

The Conda Build Spec records reviewed dependency families, source anchors, candidate resolution policy, and excluded optional paths. Do not mechanically copy all Source Version Anchors into one hard-pinned dependency list.

| Environment Build Target | Conda Environment Name Or Prefix Policy | Channels | Dependencies | Pip Dependencies | Explicitly Excluded Optional Dependencies | Source / Config References |
| --- | --- | --- | --- | --- | --- | --- |
| `<initial build target>` | `<name or reviewed prefix policy>` | `<channels>` | `<conda deps organized by assembly group>` | `<pip deps or none, organized by assembly group when useful>` | `<excluded optional deps>` | `<references execution may consult>` |

### Step-By-Step Build Instructions

| Step Order | Environment Build Target | Planned Action | Command Intent | Planned Load Check | Expected Output File Update | Failure Response |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `<initial build target>` | `<conda env create/update/check/write file>` | `<command intent, not necessarily literal shell>` | `<import/library/GPU/R bridge check or none>` | `<harness_environment.yaml / environment_build.yaml / environment_build.jsonl>` | `<record event / rollback to reviewed spec / produce covered branch evidence / write handoff evidence>` |

Steps should cover conda environment create or update, planned package/load checks, writing `environment_build.yaml`, writing `harness_environment.yaml`, and appending execution events to `environment_build.jsonl`.

### Load Check Attribution Plan

| Check Unit | Method Dependency Group(s) | Method Scope | Packages / Libraries To Check | Package-Level Isolation Required | Evidence Recorded In |
| --- | --- | --- | --- | --- | --- |
| `<method_or_group_check>` | `<dependency groups>` | `<base / METHOD / reviewed method set>` | `<packages/libraries>` | `<yes; list package-level checks>` | `environment_build.jsonl` |

### Reviewed Output State Policy

This policy controls pre-existing output directories, stale conda prefixes, previous failed evidence, append-vs-overwrite behavior, and whether old evidence remains durable after rebuild. If execution observes an existing output path, branch output path, `conda_prefix`, failed evidence, or selection-index row not covered here, execution stops for targeted planning repair or Gate 2 re-review.

| Existing State | Applies To | Reviewed Response | Evidence Preservation Rule | Allowed Mutation Boundary | Covered State Handling |
| --- | --- | --- | --- | --- | --- |
| `<no prior output / existing output directory / existing branch directory / stale conda_prefix / previous failed evidence / existing selection-index row>` | `<primary output path, branch output path, conda_prefix, environment_build.jsonl, runtime_environment_selection.tsv row>` | `<stop / overwrite / append / archive then rebuild / reuse after check / remove stale prefix / other reviewed response>` | `<which prior files, logs, failed evidence, or old rows remain durable and where>` | `<exact path, prefix, row, or file set that may be mutated>` | `<covered action for this observed state; leave uncovered states out of execution approval>` |

### Reviewed Branch Policy

| Branch Condition | Evidence Required | Compatible Method Scope | Environment Branch | Output Path | Conda Prefix | Remaining Check Policy |
| --- | --- | --- | --- | --- | --- | --- |
| `<base success>` | `<all base check units pass>` | `<reviewed base method scope>` | `<ANALYSIS_CODE>_base` | `<environment_builds>/<environment_branch>/` | `<conda_prefixes>/<environment_branch>` | `<continue/finalize>` |
| `<single-method branch>` | `<method check unit passes>` | `<METHOD>` | `<ANALYSIS_CODE>_<METHOD>` | `<environment_builds>/<environment_branch>/` | `<conda_prefixes>/<environment_branch>` | `<continue remaining method checks>` |
| `<reviewed method-set branch>` | `<all method-set check units pass>` | `<reviewed method set>` | `<ANALYSIS_CODE>_<METHOD_SET>` | `<environment_builds>/<environment_branch>/` | `<conda_prefixes>/<environment_branch>` | `<continue remaining method checks>` |

### Rollback And Split Response

| Trigger | Reviewed Response | Split Response Allowed | Reviewed Evidence Handling | Notes |
| --- | --- | --- | --- | --- |
| `<solver conflict / missing package / failed load check / system requirement>` | `<rollback to reviewed spec / pin adjustment inside reviewed policy / produce covered branch evidence / write handoff evidence>` | `<yes when this trigger is covered by Reviewed Branch Policy / no when this trigger only records failure evidence>` | `<record failure evidence / branch evidence / rollback evidence / handoff evidence>` | `<notes>` |

Split response is triggered by execution-stage evidence or re-review, not text comparison alone. Text evidence records risk order, assembly order, and planned checks.

### Compatibility Rewrite Handoff Candidates

| Method Dependency Group | Compatibility Issue | Candidate Adaptation Level | Scientific Core Touched | Handoff Target | Validation Need |
| --- | --- | --- | --- | --- | --- |
| `<method_a_dependency_group>` | `<old API / glue code / file layout / object conversion / export / logging / visualization / dependency migration issue>` | `<adapter / wrapper / compatibility_rewrite / possible_algorithmic_rewrite>` | `<no / unknown / yes>` | `<layer4_bridge_planning or layer3_layer4_build>` | `<load check / bridge replay / output-contract check / stronger algorithmic review>` |

### Required Environment Build Outputs

The reviewed output path for the initial Environment Build Target must contain:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

| Output File | Required Content | Boundary |
| --- | --- | --- |
| `harness_environment.yaml` | Reviewed environment binding record with `analysis_problem`, `environment_branch`, `conda_prefix`, `compatible_methods`, and `compatibility_note`. `environment_branch` uses the reviewed base, method, or method-set branch name. `compatible_methods` comes only from the compatible method scope of the successful final event for that branch. If `layer3_interface_paths` is retained inside `compatible_methods`, it may refer to reviewed Layer3 binding scope before final callable paths exist. | Uses BioHarness Layer3 planning/interface language only; `layer3_interface_paths` must not be native repo paths, source config locators, tutorials, reader artifacts, or final `callable_path` claims before `build_output_result.yaml` exists. Does not include status/build/log/repro/Gate2/non-claim fields. |
| `environment_build.yaml` | Pure conda YAML for the build target. | Defaults to no `prefix:`. |
| `environment_build.jsonl` | Actual execution events in reviewed step order. | Records environment build events only. |

### Selection Index Handoff

Successful primary or branch outputs must be eligible for `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/runtime_environment_selection.tsv` indexing after execution. Failed outputs are evidence only and are not downstream-selectable.

Core branch outputs remain:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

Do not add `runtime_environment_selection.tsv` as a fourth core file inside each branch directory.

| Successful Output Scope | Selection Index Row Source | Downstream Selectable Condition | Existing Row Handling |
| --- | --- | --- | --- |
| `<primary or branch output path>` | `<analysis_problem, environment_branch, compatible_methods, conda_prefix, harness_environment_yaml, compatibility_note from successful build output>` | `<environment_build.jsonl records successful completion, conda_prefix exists, harness_environment.yaml binds compatible methods>` | `<follow Reviewed Output State Policy for row replacement or removal; successful environment_branch rows only>` |

## Non-Claims

This planning file does not approve execution/build.

It does not record actual conda execution results.

It does not claim installability, solved environment reproducibility, import/load success, runtime support, method workflow success, author-case success, production readiness, final implementation support, algorithmic equivalence, or biological correctness.
