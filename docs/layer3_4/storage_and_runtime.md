# Storage And Runtime

## Purpose

This document records operational conventions for Layer 3/4 artifacts, NAS storage, runtime environments, logs, and evidence boundaries.

## Storage Boundary

The repository stores current design documents, schemas, templates, summaries, and illustrative examples.

Full method-specific evidence, audit packs, review packs, surface drafts, adapter drafts, environment reports, validation plans, logs, and runtime outputs should remain in the NAS results workspace unless a higher-authority project document explicitly promotes a subset into repo state.

Repo-level planning and review documents may point to NAS records, but they should not duplicate full evidence packs.

## NAS Layout

Current spatial domain Layer 3/4 work uses:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/
```

Method-specific Layer 3/4 work should separate localized source evidence, reading packages, integration outputs, and runtime artifacts:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/<method_id>/source_repository/
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/<method_id>/repository_reading/
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/<method_id>/stage_integration/
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/<method_id>/runtime_artifacts/
```

Method-specific packs should keep evidence, surfaces, adapter drafts, environment notes, checks, and manifests separated so review and replay are auditable.

`source_repository/` may contain a cloned source tree after `.git/` history removal. Retain `.github/` and `.git*` metadata files such as `.gitattributes`, `.gitmodules`, and `.gitignore` when present because they are source evidence.

External data download is not part of source repository localization. External case data, model assets, URL checks, and author-case downloads belong to separately scoped validation/testing workflows and require an explicit reviewed boundary.

Current stage integration uses a three-layer storage model for environment planning and reviewed build output:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/runtime_environment_selection.tsv
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/stage_integration/
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/runtime_artifacts/environment_builds/<environment_build_output_key>/
```

`runtime_environment_selection.tsv` is a lightweight engineering selection index, not a build manifest. It is updated only from successful reviewed environment build outputs. Failed branches are evidence only and are excluded from downstream-selectable rows. It should contain these columns:

```text
analysis_problem
environment_branch
compatible_methods
conda_prefix
harness_environment_yaml
compatibility_note
```

It does not record status, build history, event logs, rollback events, or rollback history.

Row replacement or removal for existing `environment_branch` values must follow the Reviewed Output State Policy in the filled environment integration planning record or reviewed addendum.

For successful environment outputs, prefer using the reviewed `environment_branch` value as `<environment_build_output_key>`, such as `SDI_base` or `SDI_BANKSY`. The same key should appear in `harness_environment.yaml.environment_branch`, the conda prefix path, and `runtime_environment_selection.tsv`.

The environment build output directory contains:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

Method-specific records may reference an analysis-problem-level environment build output path. They should not copy a shared environment build output into every method-specific pack.

## Semantic Environment Planning Packages

Environment planning packages should use semantic names rather than numbered reader-style filenames when they are created for Gate 2 review or after reviewed environment build execution. For example:

```text
environment_integration_planning_<date>/
```

Such packages may contain Text Anchors, environment build targets, selected dependency boundaries, Conda Build Specs, step-by-step Environment Build Plans, rollback/split responses, and pointers to reviewed environment build outputs. They are planning or reviewed build records, not runtime support claims.

## Runtime Layout

Runtime environment paths, conda roots, container images, cache locations, and artifact directories should be recorded explicitly before implementation support is claimed.

Until such runtime artifacts exist and have been checked, environment and runtime paths remain planning conventions.

## Execution Workspace Layout

Layer3/4 phases that execute commands should use the reviewed output root as the execution workspace boundary.

Use this phase-level layout when a workflow writes runtime artifacts:

```text
<reviewed_output_root>/
  inputs/
  work/
  data/
  outputs/
  logs/
  reports/
```

Use this method-level layout when a workflow runs one method at a time:

```text
<reviewed_output_root>/methods/<method_id>/
  work/
  data/
  outputs/
  logs/
```

`inputs/` records the selected input pointers or lightweight input notes for the phase. `work/` is the command working directory for runtime steps that write intermediate files. `data/` stores or links localized case data. `outputs/` stores method or phase outputs. `logs/` stores stdout, stderr, and runtime notes. `reports/` stores summary tables and reports.

Source repositories are source evidence roots. Runtime commands that write files should run from the reviewed `work/` directory or a method-level `work/` directory. Final evidence files should be written or copied back under the reviewed output root.

## Execution Environment Invocation

Layer3/4 phases that execute commands should record the reviewed runtime invocation before running method commands.

Use this template when a phase executes inside a conda prefix:

```yaml
execution_environment:
  conda_prefix:
  command_env:
    LD_LIBRARY_PATH: <conda_prefix>/lib
    LD_PRELOAD: <when required by reviewed native-library evidence>
  python_invocation: env LD_LIBRARY_PATH=<conda_prefix>/lib conda run -p <conda_prefix> python
  r_invocation: env LD_LIBRARY_PATH=<conda_prefix>/lib conda run -p <conda_prefix> Rscript
  method_runtime_boundary:
    required_package_family:
    language_bridge:
    native_library_policy:
    backend_smoke_path:
  command_workdir:
  environment_check_output:
```

`command_env` records command-level environment variables only when the environment build evidence shows they are required for the selected route-level backend-load checks. Leave it empty when no command-level variables are required.

`command_env` may record method-critical native runtime settings such as `LD_PRELOAD` when reviewed evidence shows that the selected backend route requires a specific library ordering.

Layer3/4 execution uses the same invocation form that produced the reviewed route-level backend-load `PASS` evidence, including command-level environment variables recorded in `environment_build.jsonl` or the reviewed environment handoff.

The invocation records how the process enters the reviewed prefix. Directly naming a binary inside the prefix is sufficient only when the process environment resolves the same prefix at runtime.

For Python surfaces that start R through `rpy2`, record an embedded-R preflight under the same invocation used for method execution. The preflight should cover the selected backend smoke path under the reviewed Python import order. Startup checks such as `import rpy2` and `library(<method package>)` are necessary but not sufficient when the backend route depends on additional native libraries:

```yaml
embedded_r_preflight:
  invocation:
  expected_r_home:
  observed_r_home:
  observed_r_version:
  python_import_order:
  import_rpy2_robjects: pass | fail
  load_base_packages: pass | fail
  method_package_load: pass | fail | not_applicable
  backend_smoke_path:
    description:
    status: pass | fail | not_applicable
  status: pass | fail
```

Runtime commands should use the reviewed workdir and the complete reviewed invocation together. Final logs and preflight outputs should be written under the reviewed output root.

## Validation Data Localization

Author-case and functional-validation execution should localize case data inside the reviewed output boundary.

Use this data-localization sequence:

1. Confirm the required case data from the reviewed planning record.
2. Use an existing local or NAS path when it is available.
3. When only a reviewed remote locator is available, download or locate the data from that locator.
4. Check the data format and usability for the selected workflow.
5. Move or link the usable data into the reviewed NAS data target.

Record data localization with this template:

```yaml
data_localization_record:
  data_item:
  source_locator:
  local_or_nas_path:
  format_check:
  usability_check:
  status_or_failure_reason:
```

## Validation Workflow Reference Localization

Author-case and functional-validation execution may localize remote author workflow, tutorial, vignette, or example references when the reviewed planning record names the remote locator and no local copy is available.

Save localized workflow references under:

```text
<reviewed_output_root>/inputs/workflow_references/<method_id>/
```

Record workflow reference localization with this template:

```yaml
workflow_reference_localization_record:
  method:
  source_locator:
  local_saved_path:
  workflow_usability_check:
  allowed_adjustment_scope: path | workdir | input_path | output_path | cache_path
  core_workflow_status: original_workflow_preserved
  status_or_failure_reason:
```

Runtime commands should run from the reviewed `work/` directory or method-level `work/` directory. Localized workflow references are input evidence for the run. Generated native reference outputs belong under the method `outputs/` directory.

## Rerun Artifact State

A rerun must define the state of prior artifacts before execution. The reviewed policy for each prior root is one of:

- `delete_before_rebuild`
- `archive_then_rebuild`
- `reuse_as_input`
- `do_not_touch`

Artifacts marked `delete_before_rebuild` or `archive_then_rebuild` are not downstream-consumable after the rerun starts. Artifacts marked `reuse_as_input` must be named explicitly in the invocation prompt and remain within the reviewed evidence boundary.

For Layer3/Layer4 implementation package reruns, prefer `delete_before_rebuild` or a fresh reviewed output root. Do not create history archives inside the active output package root; if an archive is explicitly required, place it under a separately reviewed archive root outside the active package.

## Reviewed Output Roots

Reviewed output roots are part of the evidence boundary for a workflow phase. Filled records, build evidence, import evidence, logs, and runtime artifacts should be written under the reviewed output root recorded by the phase planning or Gate review.

If a reviewed output root is unavailable because of filesystem permissions, sandbox restrictions, missing mounts, or storage errors, the execution should request the required permission or stop and report the issue. It should not silently redirect final evidence outputs to `/tmp`, repo-local paths, user home directories, or other unreviewed roots.

This does not forbid temporary scratch space when a phase explicitly permits it, but final evidence artifacts used for review or downstream selection must land under the reviewed output root.
