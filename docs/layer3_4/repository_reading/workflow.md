# Repository Reading Workflow

## Purpose

This workflow defines how Layer 3/4 planning reads a method repository and reviews a reusable repository-reading package.

Repository reading organizes repository-visible material for later design work. It does not perform method selection, freeze Layer 3 execution surfaces, implement Layer 4 adapters, validate runtime behavior, or establish production readiness.

## Workflow Scope

Repository reading covers:

- repository localization and local source-root preparation
- source census and file-category assignment
- reading-plan risk review
- docs/workflow reading
- environment configuration reading
- code reading planning and function-family reading
- output and validation-cue reading
- repository-reading package review

The workflow stops at package review. Method Integrator work, key-question mapping, parent-function abstraction, environment planning, Layer 4 support decisions, and validation planning are later stages.

## Initial Localization Inputs

Each repository-reading task should receive these inputs before Repository Localization Agent runs:

- `method_id`
- `analysis_problem`
- `source URL or evidence root`
- `NAS layer3_4 root`
- `NAS method root`
- `requested source ref / release if known`
- `repository localization policy`
- `NAS output root for filled reader outputs`
- `reading mode`

## Downstream Reader Inputs After Localization

Downstream readers should receive:

- `method_id`
- `analysis_problem`
- `source URL or evidence root`
- `Repository Localization Agent output`
- `local repository path from Repository Localization Agent`
- `NAS output root for filled reader outputs`
- `reading mode`

## Dispatch Order

```text
Initial localization inputs
  -> Repository Localization Agent
  -> downstream reader inputs after localization
  -> Source/Census Reader
  -> Reading Plan Risk Reviewer
  -> Docs/Workflow Reader
  -> Environment Reader
  -> Code Reading Planner
       -> Code Function-Family Readers
  -> Output/Validation Reader
  -> Reading Package Review
```

## Reader Output Overview

Reader outputs should provide concise tables and notes that identify relevant repository material, reading boundaries, downstream routing targets, unresolved gaps, and corrections to the reading plan.

Filled method-specific reader outputs belong under the NAS output root. Repository docs keep reusable workflow, empty templates, and NAS pointer conventions. Localized source repositories live under the NAS method root and are not copied into repo docs.

## Package Lifecycle

1. Establish the source locator and version boundary.
2. Localize the repository to NAS and pass the local repository path to Source/Census.
3. Build a repository census from the local repository path and mark generated, binary, data, model, or large notebook-output files as metadata-only or excluded.
4. Create a reading plan and risk review from the census.
5. Read author-visible documentation and workflows.
6. Read configuration files, dependency evidence, author-stated versions, and optional runtime paths.
7. Plan code reading from repository structure and docs.
8. Read critical function families and execution paths within the planned scope.
9. Extract output, author-provided test/example/tutorial/notebook, repository-provided fixture if present, and validation-cue evidence.
10. Review the reading package for coverage, omissions, boundary issues, NAS pointers, author-case eligibility needs, blocked or deferred author cases, runtime-observation needs, and package-level notes.

Downstream readers should read `local_repository_path` first. External documentation, data, model, or case-asset links should be recorded only as external locators unless a separately scoped task explicitly permits download or runtime access.

The package is structurally usable when all required sections are present, even if some sections document gaps. A documented absence is preferable to an unstated assumption.

Package review output is an input to integration-readiness audit. It is not the audit itself.

## Separation Rules

- Layer 2 method-selection rationale stays outside this package.
- Layer 3 parent-function design is informed later by package evidence; it is not defined inside reader notes.
- Layer 4 adapter or rewrite design is informed later by package evidence; it is not implemented or frozen inside reader notes.
- Method-specific filled evidence stays in NAS artifacts.
- Repo docs preserve common workflow and templates only.
