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
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/runtime_artifacts/environment_builds/<environment_branch>/
```

`runtime_environment_selection.tsv` is a lightweight engineering selection index, not a build manifest. It should contain these columns:

```text
analysis_problem
environment_branch
compatible_methods
conda_prefix
harness_environment_yaml
compatibility_note
```

It does not record status, build history, event logs, or rollback history.

`<environment_branch>/` uses the path-safe human-readable branch key for the analysis problem, such as `SDI_base`.

The environment branch output directory contains:

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

Such packages may contain Text Anchors, environment branches, selected dependency boundaries, Conda Build Specs, step-by-step Environment Build Plans, rollback/split responses, and pointers to reviewed environment build outputs. They are planning or reviewed build records, not runtime support claims.

## Runtime Layout

Runtime environment paths, conda roots, container images, cache locations, and artifact directories should be recorded explicitly before implementation support is claimed.

Until such runtime artifacts exist and have been checked, environment and runtime paths remain planning conventions.
