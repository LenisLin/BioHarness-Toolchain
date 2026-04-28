# Reliability Evaluation

## Purpose

Define candidate evaluation criteria for the spatial transcriptomics execution harness.

## Status

This document is a working blueprint. It does not report benchmark results and does not claim that a benchmark harness already exists.

## Evaluation Focus

The evaluation target is runtime reliability for LLM-facing bioinformatics execution, not only biological correctness. A useful harness should reduce environment and execution failures, make failures easier to repair, and produce auditable outputs. It should not promise to eliminate failures or replace scientific review.

## Execution-Level Metrics

- first-run success rate
- environment-related failure rate
- output contract satisfaction rate
- average repair turns
- median tool-call count
- median wall-clock time
- token/context spent on setup and debugging
- cross-machine replay success rate
- provenance completeness

## Agent-Level Metrics

- invalid tool call rate
- tool selection stability
- unnecessary environment modification rate
- recovery rate from typed failures
- irrelevant clarification rate
- rate of falling back to raw shell debugging

## Workflow-Level Metrics

- complete QC report generation
- reproducible artifact generation
- notebook/script export completeness
- successful handoff between adapters
- consistency of output schema across datasets

## Benchmark Design Principles

- Separate execution reliability from biological discovery claims.
- Use small synthetic or public datasets before large real workflows.
- Include dependency and data-contract perturbations that reflect realistic failure modes.
- Compare against an agent baseline that receives tool documentation but no curated execution harness.
- Record failures as typed events so repair behavior can be measured.

## Perturbation Benchmark

Candidate perturbations:

- `adata.obsm["spatial"]` missing
- spatial key exists but shape is invalid
- `cluster_key` missing
- `cluster_key` exists but is not categorical
- histology image path invalid
- scale factor metadata missing
- reference gene symbols mismatch spatial object
- GPU backend unavailable
- package API changes result key
- output file generated but AnnData key not written
- spatial graph empty or disconnected
- sparse matrix unexpectedly densified

## Evaluation Comparison

- Baseline agent: given README/docs/tool docs and allowed to debug.
- Harness agent: constrained to Layer 1/2/3 plus typed failure feedback and environment profiles.

The first benchmark should not attempt to prove better biological discovery. The goal is reliable, auditable, reproducible execution.

## Non-Goals

- This document does not define a finalized benchmark suite.
- This document does not invent biological benchmark results.
- This document does not treat runtime success as proof that the scientific conclusion is correct.
