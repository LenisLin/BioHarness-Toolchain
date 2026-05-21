# Method Repository Reading

## Purpose

This document is the overview and navigation entry for Layer 3/4 method repository reading.

Repository reading is an engineering-planning activity. It assembles repository-visible evidence for later parent-function abstraction, environment planning, Layer 4 support design, and validation planning. It is not runtime implementation, adapter implementation, production readiness, or biological correctness validation.

Repository reading may feed later stage integration through Code Planner stage-inform groups and code-reader evidence, but it does not perform parent-function extraction.

Repository reading stops at package review. Integration-readiness audit begins in `stage_integration/`.

## Current Package

Use [repository_reading](repository_reading/) for the current repository-reading workflow framework.

The current package covers:

- package workflow and task inputs
- repository localization and local source-root provenance
- source census reader
- reading plan and risk review reader
- docs workflow reader
- environment config reader
- code reading planner and code function-family reader
- output validation reader
- reading package review and omission check

The current package intentionally stops before key-question mapping. It does not add a Method Integrator file.

## Stage Position

Layer 3/4 work proceeds through:

1. design framing
2. engineering planning
3. abstraction
4. formal result presentation

Repository reading belongs to engineering planning. It extracts evidence for later design decisions. It does not freeze final parent-function fields, final Layer 4 implementation decisions, reviewed environment build outputs, validation thresholds, or production-readiness criteria.

## Evidence Location

Repository docs should preserve generic workflow, templates, and pointer conventions.

Filled method-specific evidence should remain in the current NAS result subtree for the relevant Layer 3/4 planning case, for example:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/
```

Localized source repositories should use:

```text
/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/<analysis_problem>/<method_id>/source_repository/<repo_name>/
```

Repository localization output is an evidence source root for reading and planning. It is not runtime support, installability evidence, or production readiness.

Repo-level planning documents may point to NAS evidence packages. They should not reproduce filled source census tables, code-reading notes, or method-specific evidence packs.

## Boundary

Repository reading should keep the layers separate:

- Layer 2 method-selection material remains outside Layer 3/4 repository-reading templates.
- Layer 3 parent-function design may use repository-reading evidence later, but reader notes do not define public execution surfaces.
- Layer 4 support planning may use repository-reading evidence later, but reader notes do not implement adapters, wrappers, rewrites, environment build outputs, or runtime implementations.

## Non-Claims

This overview and the repository-reading package do not establish:

- runtime support
- implemented adapters
- executable reviewed environment builds
- production readiness
- biological correctness
- final parent-function output contracts
- final Layer 4 adapter or rewrite boundaries
