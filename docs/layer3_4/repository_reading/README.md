# Repository Reading

## Purpose

This directory defines the reusable Layer 3/4 repository-reading package for method repositories.

Repository reading is an engineering-planning workflow. It assembles auditable evidence for later parent-function abstraction, environment planning, Layer 4 support design, and validation planning. It does not implement adapters, define final callable contracts, establish runtime support, or establish production readiness.

Method-specific filled evidence belongs in the current NAS result subtree for the relevant analysis problem. Repository docs keep the common workflow, reusable templates, and pointers.

Localized source repositories also belong under the NAS method root. Repository docs should store only templates and path conventions; they should not copy localized source trees into repo documentation. A localized source snapshot is an evidence input for reading and planning, not runtime support, installability evidence, or production readiness.

## Package Files

Read in this order:

1. [Workflow](workflow.md): stage boundary, workflow scope, task inputs, dispatch order, and package lifecycle.
2. [Repository localization](repository_localization.md): localize the remote source repository into the NAS method root, record provenance, remove `.git/` history, and return the local source root.
3. [Source census](source_census.md): source version note, repository tree, file categories, reader assignment, and metadata-only or exclusion notes.
4. [Reading plan and risk review](reading_plan_risk_review.md): scope control, reader allocation, reading-plan risk table and corrections.
5. [Docs workflow](docs_workflow.md): README, tutorials, notebooks, examples, and author-visible workflow evidence.
6. [Environment config](environment_config.md): configuration files, author-stated versions, dependency constraints, and optional runtime paths.
7. [Code reading](code_reading.md): Code Reading Planner and Code Function-Family Reader templates in one file.
8. [Output validation](output_validation.md): output candidates, author-provided examples, tests, tutorials, repository-provided fixtures when present, validation cues, and runtime-observation needs.
9. [Reading package review](reading_package.md): lightweight review prompt for coverage, omissions, boundary issues, NAS pointers, and future verification needs.

## Boundary

This package is a blueprint for evidence extraction and package review. It deliberately stops before Method Integrator work and key-question mapping.

Do not use these templates to claim:

- runtime support
- implemented adapters or wrappers
- executable reviewed environment builds
- production readiness
- biological correctness
- final Layer 3 parent-function contracts
- final Layer 4 adapter boundaries

## Evidence Location

For a filled method package, store the method-specific artifacts under the current NAS result location for the relevant Layer 3/4 planning case and link to them from repo-level summaries.

Use repository docs for:

- workflow rules
- role prompts
- empty templates
- boundary rules
- NAS pointer conventions

Use NAS artifacts for:

- localized source repository snapshots used as evidence input
- method-specific source census outputs
- filled reader tables
- method-specific notes
- conflict and gap notes
- runtime observations when separately scoped runs are performed
