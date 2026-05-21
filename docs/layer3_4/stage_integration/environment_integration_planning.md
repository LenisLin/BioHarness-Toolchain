# Environment Integration Planning

## Purpose

This file defines the pre-Gate2 environment integration planning file for a method set within one analysis problem or feature.

Environment integration planning starts after Gate 1 parent-function / execution-surface alignment and method-to-parent Layer4 bridge planning exists. It organizes static environment evidence into Text Anchors, environment branches, selected dependency boundaries, and a Gate-2-reviewable Environment Build Plan for host conda environment assembly.

It does not run conda, pip, R installation, Python imports, R loads, bridge loads, GPU checks, method workflows, author cases, data downloads, or validation runs. It does not establish executable support, runtime support, functional correctness, production readiness, or final implementation support.

Each method receives one environment organization pass. Parent-function and Layer4 bridge context is used to identify selected core paths and gated optional paths; it should not cause a full environment plan to be repeated for every execution surface.

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
| Text Anchor | Author-visible environment evidence such as package names, exact pins, language requirements, GPU/CUDA notes, R/Python bridge notes, install files, CI files, or container cues. | A Text Anchor supports risk ordering and planning only. It is not installability evidence and does not by itself justify environment splitting. |
| Environment Branch | A path-safe human-readable key for a planned host conda environment grouping within one analysis problem. | It is a planning branch until Gate 2 approves `environment_build_execution` and reviewed build output exists. |
| Environment Build Plan | A Gate-2-reviewable plan for creating, updating, checking, and recording one environment branch. | It is execution guidance only after Gate 2 approves the item and assigns `environment_build_execution`. |
| Conda Build Spec | The reviewed conda channels, dependencies, pip dependencies, and excluded optional dependencies for an environment branch. | It is not a solved environment claim before execution and does not include Docker build scope. |
| Reviewed Environment Binding Record | The minimal `harness_environment.yaml` record produced after reviewed environment build execution. | It records reviewed method / Layer3 interface path / `environment_branch` / `conda_prefix` binding. It is not a formal harness UI, prompt contract, or method workflow success claim. |

## Method-Centered Boundary

Environment integration planning starts from method-level environment evidence. For each method, identify the dependency sources, author-stated constraints, required runtime ecosystem, Text Anchors, optional paths, selected core paths, and planned environment branch needs once.

Use parent-function and Layer4 bridge hypotheses only to mark which method paths are core for the selected integration plan and which paths are optional, deferred, or out of scope. Do not create duplicate full environment plans for every execution surface unless the method genuinely requires separate runtime stacks for distinct selected paths.

Environment integration planning consumes audit-closed repository evidence. It may organize text conflicts, core/optional boundaries, environment branch hypotheses, and host conda build plans. It does not reopen environment repository reading or use static evidence as installability proof.

Gate 2 downstream planning review assigns review results to environment integration planning items after checking whether static evidence identifies the method's environment planning status, selected core dependency boundary, gated optional dependency boundary, Environment Build Plan, output path, failure response, and required build outputs.

## Text Compatibility Triage

Text compatibility triage is the first substep inside environment integration planning. It is not a new gate, a separate top-level workflow stage, or an execution action. It turns static environment evidence into a review-ready text/source evidence section inside the filled environment integration planning record.

Read author-visible environment evidence before planning local assembly. Use README and install documentation, `pyproject.toml`, `setup.py`, `requirements.txt`, `environment.yml`, lockfiles, Dockerfiles, CI files, optional dependency notes, resource notes, and environment-reader locators when present.

This substep uses Environment Config Reader outputs, Gate 1 scope, downstream bridge-planning context, environment integration inputs, and evidence records. Gate 2 human review output should record the filled planning file path, reviewed item, review result, assigned step, output path, and evidence boundary for environment planning items that enter environment build execution. Evidence records should identify both the reader output and the source config locator when available.

The goal is to route methods and source evidence into readable environment branches, handled-elsewhere records, deferred records, comparison-only records, or out-of-scope records before any local conda solve, install, import/load check, GPU check, R load, author-case run, data download, or method run is planned. Absence of a visible text conflict should be recorded as build-time uncertainty, not as installability evidence.

Use positive routing language. Prefer `defer`, `handled elsewhere`, `compare_only`, or `out_of_scope` over describing a method as infeasible unless reviewed build output or an impossible documented constraint justifies that conclusion.

Environment branches should use path-safe human-readable keys for one analysis problem. Prefer `<analysis_problem_code>_<branch_label>`, such as `SDI_base` for a spatial-domain-identification base branch. Natural-language role descriptions belong in `Branch Role` or `compatibility_note`, not in the path key. Do not hardcode Python AnnData/Scanpy as the global default base for all analysis problems.

Hardware, GPU, CUDA, and driver constraints should be recorded separately as build-time uncertainty. Author-visible CUDA version differences do not become text-stage incompatibilities by themselves; they identify planned checks inside an Environment Build Plan. Exact pins are Text Anchors. They indicate where risk should be reviewed first, but they do not directly force branch splitting. Solve results, import/load results, GPU results, R load results, and author-case behavior can only come from execution evidence, not from text triage.

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
- Define path-safe human-readable environment branch keys appropriate to the current analysis problem.
- Route each method/source evidence scope to include, exclude, defer, compare_only, or out_of_scope for each relevant environment branch.
- Separate author-visible package/runtime constraints from planned build checks.
- Record GPU/CUDA/hardware/R bridge uncertainty as Environment Build Plan checks, not as text-stage installability or incompatibility proof.
- Prepare a Gate-2-reviewable Environment Build Plan for host conda environment assembly.

Boundary:
- Do not run conda solve, install, import/load checks, GPU checks, R loads, data downloads, method runs, or author cases.
- Do not reopen Gate 1 or Gate 2.
- This planning step does not assign a Gate 2 review result and does not approve execution/build. It prepares Text Anchors, environment branches, selected dependency boundaries, Conda Build Specs, step-by-step build instructions, rollback/split responses, and required build outputs for Gate 2 review.
- Do not copy filled method-specific evidence into repo docs; filled planning files belong in the NAS results workspace.

Output:
- A review-ready filled environment integration planning record containing Evidence Roots, Text Compatibility Triage, Environment Build Plan, and Non-Claims.
```

### Text Anchor Table

Use `Method` for text/source evidence. Do not use Layer3 interface target columns in this table.

| Method | Text Anchor Type | Text Anchor | Source Locator | Planning Implication | Non-Claim |
| --- | --- | --- | --- | --- | --- |

### Environment Branch Table

| Environment Branch | Branch Role | Candidate Methods | Selected Dependency Boundary | Deferred Or Handled Elsewhere | Evidence Status |
| --- | --- | --- | --- | --- | --- |

- `Environment Branch` is a path-safe human-readable branch key, preferably `<analysis_problem_code>_<branch_label>`; for example, `SDI_base`.
- `Branch Role` states the planning role of the branch for this analysis problem.
- `Candidate Methods` records methods planned for this branch.
- `Deferred Or Handled Elsewhere` records methods, paths, or dependency families routed to another branch, deferred handling, comparison-only review, or out-of-scope handling.
- `Evidence Status` records whether the grouping is based on text evidence only, reviewed build output, or unresolved evidence.

### Native / Source Evidence Routing Table

Use `Method` and `Native / Source Evidence Scope` for source-stage routing. Do not use native repository paths as Layer3 interface targets.

| Method | Native / Source Evidence Scope | Environment Branch | Action For This Branch | Reason | Evidence Record / Source Locator | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- |

Allowed values for `Action For This Branch` are:

- `include`
- `exclude`
- `defer`
- `compare_only`
- `out_of_scope`

`exclude` means exclude from this environment branch. It does not mean exclude from BioHarness, exclude from the current method registry, or reject the method as scientifically invalid.

## Environment Build Plan

The Environment Build Plan replaces old target-list planning as the reviewable environment execution plan. It must give Gate 2 and later execution enough detail to assemble or update the reviewed host conda environment branch, run planned load checks, write the three required output files, and respond to failure without broad rereading.

### Environment Branch Summary

Use `Layer3 Interface Target(s)` for build/harness routing. These are BioHarness Layer3 interface paths after Layer3/4 restructuring, not original repository paths, tutorials, native module paths, or source config locators.

| Environment Branch | Analysis Problem | Layer3 Interface Target(s) | Compatible Methods Planned | Output Path | Scope Boundary |
| --- | --- | --- | --- | --- | --- |

### Conda Build Spec

The Conda Build Spec records the reviewed host conda environment branch specification. The current stage integration workflow supports host conda environment build, update, and check only; Docker build is out of scope.

| Environment Branch | Conda Environment Name Or Prefix Policy | Channels | Dependencies | Pip Dependencies | Explicitly Excluded Optional Dependencies | Source / Config References |
| --- | --- | --- | --- | --- | --- | --- |

`Source / Config References` lists the exact reviewed references that execution may consult if needed. Execution may not broad reread the repository or expand dependency scope from unreviewed files.

### Step-By-Step Build Instructions

| Step Order | Environment Branch | Planned Action | Command Intent | Planned Load Check | Expected Output File Update | Failure Response |
| --- | --- | --- | --- | --- | --- | --- |

The step list should allow execution to proceed in order through:

- conda environment create or update for the reviewed branch;
- planned package, Python import, R library, bridge, GPU, or hardware visibility checks when included in the plan;
- writing `environment_build.yaml` as a pure conda YAML with no default `prefix:`;
- writing `harness_environment.yaml` as the reviewed environment binding record;
- appending actual events to `environment_build.jsonl` in reviewed step order.

Each step should specify the failure response. Typical reviewed responses include stop and record failure, rollback to the prior reviewed spec, split only when the plan already defines the branch split boundary, targeted planning repair, or Gate 2 re-review.

### Rollback And Split Response

| Trigger | Reviewed Response | Branch Split Allowed | Repair Or Re-Review Needed | Notes |
| --- | --- | --- | --- | --- |

Rollback and split responses must stay inside the reviewed dependency boundary. If the response requires a new dependency scope, environment branch, Layer3 interface target, or source/config reference, execution stops and routes to targeted planning repair or Gate 2 re-review.

### Required Environment Build Outputs

The reviewed output path for each environment branch must contain:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

| Output File | Required Content | Boundary |
| --- | --- | --- |
| `harness_environment.yaml` | Reviewed environment binding record with `analysis_problem`, `environment_branch`, `conda_prefix`, `compatible_methods`, and `compatibility_note`. | Uses BioHarness Layer3 interface paths and does not include status, build ID, provider, log, reproducibility, Gate 2, or non-claim fields. |
| `environment_build.yaml` | Pure conda YAML for the reviewed branch. | Defaults to no `prefix:`. |
| `environment_build.jsonl` | Actual execution events in the same order as the reviewed plan steps. | Records environment build events only. |

## Execution Scope After Gate 2

When Gate 2 approves an environment planning item for `environment_build_execution`, execution follows the reviewed Environment Build Plan in the filled planning record. Execution may inspect only the source/config references listed in the reviewed plan. It may not extend dependency scope, add environment branches, add Layer3 interface targets, or reinterpret method routing. Required expansion goes through targeted planning repair or re-review.

## Core Path And Optional Path Handling

Core path dependencies are dependencies required by the selected Layer4 bridge path. They should be evaluated for the environment branch that would run the selected execution surface.

Optional paths are gated. Examples include non-selected clustering alternatives, GPU extras, plotting extras, image/reporting utilities, and acceleration paths. Optional paths should be excluded from shared core branches unless explicitly selected by Layer4 bridge planning. Optional paths may have separate branch plans when Gate 2 reviews them.

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
