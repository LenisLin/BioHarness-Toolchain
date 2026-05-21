# Scope

## Purpose

Define the problem boundary for BioHarness-Toolchain and the responsibilities this repository owns.

## Problem Boundary

BioHarness-Toolchain addresses the execution-substrate burden that appears when LLM agents perform spatial transcriptomics downstream analysis. The repository is not responsible for replacing scientific reasoning by the agent. It is responsible for organizing task routing, method evidence, execution-surface planning, environment assumptions, validation hooks, and provenance scaffolds so that routine execution context is not repeatedly reconstructed in the model context.

The first vertical remains spatial transcriptomics downstream analysis. Work outside that vertical should not be treated as in scope unless a current project document or topic artifact explicitly expands the boundary.

## Layer Responsibilities

Layer 1 owns analysis-problem and task-family routing. It helps the agent identify the kind of downstream analysis being requested. Layer 1 registry inclusion does not imply core candidacy, executable status, stable surface status, or rewrite priority.

Layer 2 owns concrete method knowledge for a task family: method comparison, selection rules, assumptions, and topic-specific decision trees. Layer 2 does not define callable runtime interfaces, backend bindings, or final execution defaults.

Layer 3 owns agent-facing execution surfaces after a method family has passed the documented handoff gate. Layer 3 should express stable task contracts and execution-planning surfaces, not backend package internals or full method-comparison logic.

Layer 4 owns concrete backend adapters, wrappers, compatibility rewrites, or algorithmic rewrites. Layer 4 is implementation-facing and should normally be hidden from the main agent unless implementation, debugging, or audit requires it.

## In Scope

- Spatial transcriptomics downstream analysis as the first vertical.
- Layer 1/2 knowledge artifacts for analysis-problem routing and method selection.
- Layer 3 execution-surface planning for promoted task families.
- Layer 4 adapter, wrapper, rewrite, and validation scaffolds where explicitly planned or implemented.
- Dependency-aware environment planning through explicit environment profiles or future environment capsules.
- Typed input/output contracts, validation hooks, provenance records, and auditable output expectations.
- Reliability evaluation criteria for execution, repair, provenance, context burden, and adapter handoff.
- Supporting scripts and tests that preserve current documentation, schema, and scaffold behavior.

## Out Of Scope

- Generic biomedical agent behavior.
- Upper-level reasoning, planning, or brain responsibilities outside the toolchain substrate.
- Audit and governance responsibilities outside the repository's local validation/provenance scaffolds.
- Replacing mature scientific ecosystems such as Scanpy, Squidpy, AnnData, SpatialData, PyTorch, or R spatial tools.
- Replacing workflow engines such as Nextflow or Snakemake.
- Treating MCP-style tool schemas as execution guarantees.
- Claiming biological correctness from runtime success alone.
- Treating Layer 1 registry inclusion as implementation-candidate status.
- Freezing topic-specific Layer 2 decisions into Layer 3 execution defaults before the documented gate is complete.
- Maintaining every upstream package option as an agent-facing parameter.

## Current Limits

The repository is still in blueprint stage. It does not yet provide production task adapters, executable environment capsules, a runtime dispatcher, or completed reliability benchmarks.
