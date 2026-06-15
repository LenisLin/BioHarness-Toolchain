# Environment Build Execution

## Purpose

This file defines the post-Gate2 execution workflow for a Gate 2-reviewed environment integration planning item whose assigned step is `environment_build_execution`.

Environment build execution assembles or updates a host conda environment from a Gate-2-reviewed Environment Build Plan for a planned environment build target. It produces reviewed environment build output, including a reviewed environment binding record, for later Layer3/Layer4 build, author-case execution, bridge replay, and validation planning. It does not build Docker images.

The execution plan comes from the Gate 2 human review table pointing to a filled environment integration planning record. This repo instruction file defines the reusable workflow; it is not itself the execution plan.

Invocation prompts are thin dispatch records for opening a focused execution window. They are not execution-policy authority and must not restate or override this phase workflow.

## Inputs

The Gate 2 row must include:

- `Planning Area = environment_integration_planning`
- `Gate 2 Review Result = approved_for_next_step`
- `Step After Gate 2 = environment_build_execution`
- `Filled Planning File Path`
- `Reviewed Item`
- `Output Path`

Execution reads the reviewed `Environment Build Plan` section from the filled planning record identified by `Filled Planning File Path`. `Reviewed Item` should identify the specific Environment Build Plan or environment build target under review. `Output Path` points to the environment build output directory.

Execution may consult only the source and config references explicitly listed in the reviewed planning record when those references are needed to execute the plan. It must not broad reread repositories, expand dependency scope, add a new split target or environment binding outside the reviewed plan, or add a new Layer3 binding scope/interface target. Execution produces evidence only within the reviewed scope recorded before invocation.

Execution authority comes from the Gate 2 row, the filled environment integration planning record, any reviewed repair addendum, this phase workflow document, and storage/runtime conventions. If an invocation prompt conflicts with reviewed workflow or planning records, it must not expand dependency scope, branch scope, output scope, or rewrite authority.

## Execution Boundary

Environment build execution is plan-led. Follow the reviewed plan step order for host conda environment create, update, and check actions; perform only the planned load checks; and write the required output files.

Allowed execution controls are limited to:

- stop on an unhandled failure and record the failure event;
- apply only the rollback, split, or repair response already specified in the reviewed plan;
- resolve package versions within the reviewed Flexible Resolution Policy and record actual resolved versions;
- create branch outputs under the reviewed branch policy when execution evidence identifies a compatible method scope for a base, single-method, or reviewed method-set environment branch;
- record compatibility rewrite candidates as handoff evidence without editing code;
- stop when required input is missing or an unreviewed dependency boundary, branch scope, output path, conda prefix rule, or Layer3 binding scope would be needed.

Environment build execution must not mechanically convert all Source Version Anchors into simultaneous hard solver constraints.

### PyTorch / PyG ABI Bundle Constraint

When a reviewed environment build target includes PyTorch, torchvision, PyTorch Geometric, or PyG extension packages, execution must treat the host CUDA or CPU runtime, Python version, PyTorch version, torchvision version, PyG version, and PyG extension package variants as one ABI bundle.

The candidate install spec for that bundle must be derived from the official PyTorch previous-version installation matrix and the official PyTorch Geometric installation instructions:

- `https://pytorch.org/get-started/previous-versions/`
- `https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html`

Execution must not allow the generic conda or pip solver to independently mix CPU and CUDA variants, PyTorch minor versions, torchvision builds, PyG builds, or extension package builds. Examples of disallowed execution outputs include a CUDA PyTorch build with a CPU torchvision build, PyG extension wheels built for a different PyTorch or CUDA variant, or any package set that does not correspond to one official PyTorch/PyG install recipe.

Before creating or updating the conda prefix, execution must record the chosen PyTorch/PyG ABI bundle in `environment_build.jsonl`, including:

- host runtime choice: CPU-only or the observed CUDA runtime family used for package selection;
- Python version;
- PyTorch version;
- torchvision version when required by the reviewed dependency boundary;
- PyG version or PyG install route;
- PyG extension package install route and variant when extension packages such as `torch_scatter`, `torch_sparse`, `torch_cluster`, `torch_spline_conv`, or `pyg_lib` are required.

For selected PyTorch/PyG methods whose reviewed path includes training, fitting, or embedding learning, execution builds and checks the reviewed CUDA PyTorch/PyG target when host GPU evidence is available. The evidence records the observed GPU, driver/CUDA runtime family, PyTorch CUDA build, PyG extension package variants, and `torch.cuda.is_available()`.

If a valid official PyTorch/PyG bundle cannot be selected before prefix creation, execution must stop before creating or updating any base or branch conda prefix. It must not create base or branch evidence from a mismatched PyTorch/PyG environment, and it must not use later single-method branch creation to bypass an invalid base ABI bundle.

After installing the selected PyTorch/PyG ABI bundle, execution must run and record an ABI bundle load check before installing or updating other high-risk dependency families. When later conda, mamba, or pip operations install R stacks, native libraries, image libraries, TensorFlow-family packages, compiled extensions, or other large dependency families into the same prefix, execution must re-run and record the PyTorch/PyG ABI bundle load check after that update.

The ABI recheck must verify that the resolved PyTorch, torchvision when required, PyG route, and required PyG extension packages still match the recorded official bundle. A later successful method load check must not substitute for this bundle-level invariant check.

### R Runtime Version Constraint

When a reviewed environment build target includes R, Rcpp, R-side packages, or Python/R bridge packages such as `rpy2`, execution must select an R runtime version greater than or equal to 3.6 before creating or updating any base or branch conda prefix.

This is a minimum runtime floor, not a method-specific hard pin. If the reviewed planning record, source package metadata, DESCRIPTION file, package repository metadata, or Source Version Anchor requires a narrower or higher R version, the narrower or higher reviewed requirement takes precedence.

Execution must not allow the generic conda or mamba solver to choose `r-base <3.6` for any branch that claims compatibility with an R, Rcpp, or Python/R bridge dependency group.

Before creating or updating the conda prefix, execution must record the chosen R runtime in `environment_build.jsonl`, including:

- R runtime version;
- `r-base` package version/build when available;
- R package manager route used by the reviewed plan, such as conda R packages, Bioconductor packages, or reviewed source/remotes;
- any method-specific R version requirement that is stricter than `R >=3.6`.

If a valid `R >=3.6` runtime cannot be selected before prefix creation for an R-dependent branch, execution must stop before creating or updating that branch prefix. It must not create base or branch evidence that claims compatibility with R-dependent methods from an `R <3.6` environment.

### Seurat API Compatibility Check

For Seurat-backed methods, execution records the resolved Seurat and SeuratObject versions and runs the reviewed API-family check for the selected method path.

The check covers the selected V4-style `slot` path, V5-style `layer` path, or reviewed method compatibility helper.

### Clean Base Assembly And Failure Escalation

Environment build execution is repair-first. It must treat base environment assembly as the first reviewed target when the Environment Build Plan defines a base branch. A first solve, install, import, library-load, bridge-load, or compiled-component failure is not a terminal result and is not by itself evidence that methods are incompatible.

When a failed or partial prefix is covered by the Reviewed Output State Policy for delete, overwrite, or rebuild, execution must not continue iterative package experiments inside that failed prefix. It must create the next attempt from a clean prefix and record only the evidence needed to support the next repair, branch, rewrite-handoff, or held-out decision.

Before writing held-out evidence or final branch evidence from a failed base attempt, execution must first attempt repair inside the reviewed dependency boundary. Repair attempts may include package-manager route changes, install-order changes, relaxing an incorrect hard pin into a reviewed lower bound or range, ABI bundle reselection, explicitly resolving native/system libraries exposed by the solver, package-level isolation, or dependency-family repair.

The escalation order for covered failures is:

1. repair the base environment inside the reviewed dependency boundary when a concrete package-level or dependency-family repair is available;
2. create a reviewed clean environment branch when execution evidence shows the base cannot support the relevant compatible method scope, then retry installation and load checks inside that branch;
3. continue package-manager, pin, ABI, install-order, or dependency-family repair inside the reviewed branch while the remaining failure is still an environment configuration problem;
4. record a `compatibility_rewrite` handoff candidate when the remaining failure is API drift, import-path drift, package layout, object conversion, file/cache layout, or integration glue and the reviewed scientific path is unchanged;
5. route to possible `algorithmic_rewrite` when the remaining fix may touch scientific-output-determining logic;
6. write failed or held-out evidence only when success would require unreviewed dependency scope, source references, methods, optional paths, data download, workflow execution, code changes during environment build, algorithmic rewrite, or Layer3 binding-scope expansion.

Environment build execution must not use branch creation to bypass a solvable package-level or dependency-family conflict in the base environment. Branch creation is a repair mechanism for reviewed compatible method scope, not an audit goal. Compatibility rewrite candidates are handoff evidence only and must not be implemented during environment build execution.

Environment build execution must not implement adapters, wrappers, compatibility rewrites, or algorithmic rewrites.

A failed environment branch is evidence only. Later Layer3/Layer4 build, author-case execution, bridge replay, or validation may consume only a branch whose `environment_build.jsonl` records successful completion, whose `conda_prefix` exists, and whose `harness_environment.yaml` binds the relevant compatible methods.

This workflow does not run method workflows, author cases, bridge replay, data downloads, validation fixtures, biological interpretation, or Docker builds.

## Pre-existing Output Handling

If `Output Path`, any branch output path, or `conda_prefix` already exists, execution must follow the reviewed Output State Policy from the filled planning record or reviewed repair addendum.

Before any output or prefix mutation, execution verifies that the observed state is covered by the reviewed Output State Policy. Covered states are handled exactly as recorded in that policy.

Execution must not independently choose overwrite, delete, archive, append, or mixed-history behavior for pre-existing directories, stale conda prefixes, previous failed evidence, or prior branch records.

## Load Check Attribution

Execute planned load checks by check unit. A check unit is tied to one method dependency group, one method, or one reviewed method set. Record each check unit as a separate event in `environment_build.jsonl`.

If a check unit fails, run package- or library-level isolation checks for the reviewed packages in that unit and record the result before writing branch evidence.

Package- or library-level isolation results must be used first to decide whether a package-level or dependency-family attempt can repair the current base or branch environment inside the reviewed boundary. A failed check unit may support branch evidence only after clean-prefix retry and package-level or dependency-family attempts have been recorded, unless the reviewed plan explicitly identifies the failure as outside the base dependency boundary.

Combined import/load checks are summary checks after attributable check units, not the evidence source for branch assignment.

### Native Backend Load Evidence

For an `adapter` or `wrapper` route, the method check unit must include the selected native backend entry required by the reviewed Layer4 binding.

For adapter and wrapper routes, route-level backend load checks verify that the selected backend package, module, R library, reviewed source-package component, or compiled component can be loaded as an environment dependency.

The selected load target must be bounded and import-safe. Prefer package imports, module imports, R library loads, package metadata checks, compiled-component checks, or syntax/bytecode parsing for script locators that are source evidence only.

Workflow drivers, author-case scripts, tutorial commands, data-loading scripts, training commands, and whole-method orchestration scripts are not default backend load targets. If such a script contains top-level execution behavior, record it as source evidence and defer callable extraction, guarding, or rewrite to Layer3/Layer4 build.

Use these route-level check requirements:

| Layer4 route family | Required environment check for method compatibility |
| --- | --- |
| `adapter` / `wrapper` | Import or load the selected bounded backend package, module, R library, reviewed source-package component, or compiled component used by the Layer4 binding. For R/Rcpp backends, include `library(<package>)` or a reviewed source-package build/load equivalent, plus compiled-code load evidence when compiled code is part of the selected path. |
| `compatibility_rewrite` / `algorithmic_rewrite` | If a reviewed rewrite implementation already exists in the approved build scope, import or load the rewritten callable/module and retained native components. If no reviewed rewrite implementation exists yet, environment build records the retained dependency load evidence and rewrite handoff boundary, then stops before code modification or compatibility claim. |

A planned rewrite route does not require environment build execution to invent or import a callable that has not yet been implemented by a reviewed Layer3/Layer4 build.

Dependency-family load checks support environment assembly. Method compatibility requires route-level backend load evidence for the selected Layer4 route.

## Required Outputs

The `Output Path` directory must contain the core environment build outputs below. Any branch output created under a Reviewed Branch Policy must contain the same three files in its branch output directory:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

### harness_environment.yaml

`harness_environment.yaml` is the reviewed environment binding record. It records the reviewed method / Layer3 binding scope / `environment_branch` / `conda_prefix` binding produced by environment build execution. The `environment_branch` value is the reviewed binding key recorded after build output exists; it is not inferred directly from pre-Gate2 text comparison. Before `layer3_layer4_build` produces `build_output_result.yaml`, this Layer3 binding is a reviewed parent-function / method-route scope, not a final `callable_path`.

It is not the formal harness UI, a prompt contract, or an agent-interpreted environment selection entry. It should not contain status, build ID, provider, log, reproducibility, Gate 2, non-claim, or execution-event fields.

Use this minimal shape:

```yaml
analysis_problem:
environment_branch:
conda_prefix:
compatible_methods:
  - method:
    consumable_surface_scope:
      - <execution surface name>
    route_level_backend_load_evidence:
      route_family: adapter | wrapper | compatibility_rewrite | algorithmic_rewrite
      selected_backend_entry:
      load_or_import_check:
      compiled_component_check:
      evidence_path:
    held_surfaces:
      - surface:
        reason:
compatibility_note:
```

`consumable_surface_scope` lists only BioHarness execution surfaces that the environment branch can support for downstream build, replay, or validation. It uses exact surface names only.

`route_level_backend_load_evidence` records the native backend package, module, source-package, or rewrite callable load evidence used to decide method compatibility.

`held_surfaces` records reviewed surfaces retained in the denominator but not consumable from this environment branch.

`compatible_methods` lists the method scope supported by the successful final event for that environment branch. A method enters this scope only when its reviewed route-level backend load check has passed for the selected Layer4 route. Dependency-family load success and source locator availability may be recorded as evidence, but method compatibility is derived from route-level backend load evidence.

### environment_build.yaml

`environment_build.yaml` is a pure conda YAML for reproducibility of the reviewed environment build output. By default, do not write `prefix:`. If a prefix is required by a reviewed local execution policy, record that decision outside the conda YAML or in the event log rather than making it the default template behavior.

### environment_build.jsonl

`environment_build.jsonl` records the actual environment build events in the same order as the reviewed plan steps. Each line should be a single JSON object with enough detail to audit the step, command intent, result, failure response, and evidence pointer when applicable.

Example event fields:

```json
{"step_index":1,"planned_step":"conda_env_create","result":"passed","note":"created reviewed environment build output"}
```

## Selection Index Update

After a successful primary or branch environment build, update or create:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/runtime_environment_selection.tsv
```

Use these columns:

```text
analysis_problem
environment_branch
compatible_methods
conda_prefix
harness_environment_yaml
compatibility_note
```

The TSV is a selection index, not a build manifest or event log. Failed branches must not be added as downstream-selectable rows. `harness_environment.yaml` remains the authoritative per-branch binding record.

## Evidence Boundary

Reviewed environment build output may support later `layer3_layer4_build`, author-case execution, bridge replay, and validation planning by giving those workflows a reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.

The output records host conda environment assembly/update/check behavior for the reviewed environment build output only. Install and load checks inside the plan are environment build checks, not workflow success evidence.

## Non-Claims

Environment build output does not establish method workflow success.

It does not establish author-case success.

It does not establish functional correctness.

It does not establish production readiness.

It does not establish algorithmic equivalence.

It does not establish biological correctness.

## Completion Report

The completion report must include:

- attempted primary output path;
- branch output paths created;
- successful `environment_branch` values;
- load-check attribution summary;
- environment_branch values produced using base/method/method-set naming;
- compatible methods per successful branch;
- `conda_prefix` existence;
- core output file status;
- `runtime_environment_selection.tsv` update status;
- failed branch evidence and covered boundary outcome;
- package-level isolation summary for failed check units;
- compatibility rewrite handoff candidates;
- explicit non-claims.
