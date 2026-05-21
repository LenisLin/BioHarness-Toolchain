# Environment Integration Planning Template

## Purpose

This template records a complete filled environment integration planning record for `<analysis problem or feature>`.

It organizes author-visible environment evidence into Text Anchors, environment branches, selected dependency boundaries, and a Gate-2-reviewable Environment Build Plan for host conda environment assembly. It is a planning artifact only.

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

Text compatibility triage is a substep inside environment integration planning. It records source evidence and routing decisions before any conda solve, environment create/update, package install, import/load check, method workflow, author case, data download, or validation run.

### Text Anchor Table

| Method | Text Anchor Type | Text Anchor | Source Locator | Planning Implication | Non-Claim |
| --- | --- | --- | --- | --- | --- |
| `<method>` | `<package/version/language/GPU/CUDA/R bridge/system/optional>` | `<author-visible text>` | `<reader artifact and source config locator>` | `<branch or dependency-boundary implication>` | `<what this anchor does not prove>` |

### Environment Branch Table

| Environment Branch | Branch Role | Candidate Methods | Selected Dependency Boundary | Deferred Or Handled Elsewhere | Evidence Status |
| --- | --- | --- | --- | --- | --- |
| `<path-safe branch key, e.g. SDI_base>` | `<role for this analysis problem>` | `<methods planned for this branch>` | `<core packages/language/runtime boundary>` | `<deferred, compare_only, out_of_scope, or other branch>` | `<text evidence only / reviewed build output / unresolved>` |

### Native / Source Evidence Routing Table

| Method | Native / Source Evidence Scope | Environment Branch | Action For This Branch | Reason | Evidence Pointer | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- |
| `<method>` | `<source config, install doc, CI, Dockerfile, README, or optional path>` | `<branch>` | `<include / exclude / defer / compare_only / out_of_scope>` | `<author-visible reason>` | `<reader artifact and source config locator>` | `<planning boundary and non-claim>` |

Allowed values for `Action For This Branch` are:

- `include`
- `exclude`
- `defer`
- `compare_only`
- `out_of_scope`

`exclude` means exclude from this environment branch. It does not mean exclude from BioHarness, exclude from the method registry, or reject the method.

## Environment Build Plan

This section is the Gate-2-reviewable plan for `environment_build_execution`. It must be specific enough for execution to follow step by step without broad rereading or expanding dependency scope.

### Environment Branch Summary

| Environment Branch | Analysis Problem | Layer3 Interface Target(s) | Compatible Methods Planned | Output Path | Scope Boundary |
| --- | --- | --- | --- | --- | --- |
| `<branch>` | `<analysis problem>` | `<BioHarness Layer3 interface path(s)>` | `<methods>` | `<environment branch output directory>` | `<what is in and out of branch scope>` |

### Conda Build Spec

| Environment Branch | Conda Environment Name Or Prefix Policy | Channels | Dependencies | Pip Dependencies | Explicitly Excluded Optional Dependencies | Source / Config References |
| --- | --- | --- | --- | --- | --- | --- |
| `<branch>` | `<name or reviewed prefix policy>` | `<channels>` | `<conda deps>` | `<pip deps or none>` | `<excluded optional deps>` | `<references execution may consult>` |

### Step-By-Step Build Instructions

| Step Order | Environment Branch | Planned Action | Command Intent | Planned Load Check | Expected Output File Update | Failure Response |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `<branch>` | `<conda env create/update/check/write file>` | `<command intent, not necessarily literal shell>` | `<import/library/GPU/R bridge check or none>` | `<harness_environment.yaml / environment_build.yaml / environment_build.jsonl>` | `<stop, rollback, split response, targeted repair, or re-review>` |

Steps should cover conda environment create or update, planned package/load checks, writing `environment_build.yaml`, writing `harness_environment.yaml`, and appending execution events to `environment_build.jsonl`.

### Rollback And Split Response

| Trigger | Reviewed Response | Branch Split Allowed | Repair Or Re-Review Needed | Notes |
| --- | --- | --- | --- | --- |
| `<solver conflict / missing package / failed load check / system requirement>` | `<rollback, pin adjustment, branch split, targeted planning repair, or re-review>` | `<yes/no and boundary>` | `<repair target or none>` | `<notes>` |

### Required Environment Build Outputs

The reviewed output path for each environment branch must contain:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

| Output File | Required Content | Boundary |
| --- | --- | --- |
| `harness_environment.yaml` | Reviewed environment binding record with `analysis_problem`, `environment_branch`, `conda_prefix`, `compatible_methods`, and `compatibility_note`. | Uses BioHarness Layer3 interface paths; does not include status/build/log/repro/Gate2/non-claim fields. |
| `environment_build.yaml` | Pure conda YAML for the branch. | Defaults to no `prefix:`. |
| `environment_build.jsonl` | Actual execution events in reviewed step order. | Records environment build events only. |

## Non-Claims

This planning file does not approve execution/build.

It does not record actual conda execution results.

It does not claim installability, solved environment reproducibility, import/load success, runtime support, method workflow success, author-case success, production readiness, final implementation support, algorithmic equivalence, or biological correctness.
