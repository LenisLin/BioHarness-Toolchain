# Scope

## Purpose

Define the project boundary for BioHarness-Toolchain.

## In Scope

- Spatial transcriptomics downstream analysis as the first vertical.
- Toolchain assets, substrate blueprints, contracts, execution-surface planning, validation scaffolds, and supporting scripts/tests.
- Task-level adapter design for high-frequency spatial transcriptomics workflows.
- Dependency-aware environment planning through explicit environment profiles or future environment capsules.
- Typed input/output contracts, validation hooks, provenance records, and auditable output expectations.
- Reliability evaluation criteria for execution, repair, provenance, and adapter handoff.

## Out Of Scope

- Generic biomedical agent behavior.
- Upper-level reasoning, planning, or brain responsibilities outside the toolchain substrate.
- Audit and governance responsibilities outside the repository's local validation/provenance scaffolds.
- Replacing mature scientific ecosystems such as Scanpy, Squidpy, AnnData, SpatialData, PyTorch, R spatial tools, Nextflow, Snakemake, or MCP.
- Claiming biological correctness from runtime success alone.
- Freezing topic-specific Layer 2 decisions into Layer 3 execution defaults before the documented gate is complete.

## Relationship To Existing Ecosystems

The harness should use mature tools rather than rewrite them wholesale. Scanpy, Squidpy, AnnData, SpatialData, PyTorch, and related tools should usually be wrapped through thin adapters with explicit contracts.

The project should only consider rewrites for fragile scripts, unstable wrappers, inconsistent I/O glue, and agent-unfriendly notebook fragments where wrapping cannot provide reliable execution, validation, or failure semantics.

Workflow engines solve reproducible pipeline execution. This harness solves LLM-facing task selection, contract validation, typed execution, error classification, and provenance. MCP-style tool schemas may expose capabilities to an agent, but a schema is not an execution guarantee. This harness is responsible for binding a task-level capability to a validated environment, a data contract, concrete adapter logic, post-run validation, and provenance.

## Current Limits

The repository is still in blueprint stage. It does not yet provide production task adapters, environment capsules, a runtime dispatcher, or completed reliability benchmarks.
