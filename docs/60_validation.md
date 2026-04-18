# Validation

## Purpose

Record a working blueprint for the quality gates that future execution surfaces may need before BioHarness can treat a run as trustworthy.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md).

## Current Working Direction

The current blueprint treats Round 2 validation as a three-stage gate rather than a single success flag. Every bounded task should be able to explain what was checked before execution, during execution, and after artifacts are produced.

## Validation Stages

### `preflight`

`preflight` checks happen before any surface starts running.

They include:

- input data presence and schema checks
- parameter-shape validation against the chosen surface
- environment-profile resolution
- detection of actions that require explicit approval before execution

### `runtime`

`runtime` checks govern what the harness is allowed to do while execution is live.

They include:

- approval gates for sensitive or expensive actions
- guardrails around filesystem, network, and secret access
- run-state capture into `RunRecord`
- interruption or escalation when a blocked action appears

### `post-run`

`post-run` checks happen after artifacts are emitted.

They include:

- artifact presence and shape checks
- domain-level sanity checks such as label coverage or output completeness
- comparison against the promised output contract
- release, block, or manual-review decisions recorded in `ValidationReport`

## Default Manual Approval Triggers

The following actions require explicit human approval unless a later policy says otherwise:

- writing to an `authoritative CSV`
- writing to a `NAS report`
- accessing an `external resource` that depends on secrets
- launching a `high-cost GPU` execution path
- executing a change that mutates the `baseline registry`

## Validation Artifacts

- `RunRecord` preserves structured execution state for resume and compaction.
- `ValidationReport` records `preflight` and `post-run` outcomes plus final release status.
- Golden scenarios under [evals](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/evals) act as regression anchors for approval rules and resume behavior.

## Acceptance Standard

A future execution surface should not be considered BioHarness-ready unless it can:

- identify its required validation hooks before dispatch
- produce enough structured state to resume after compaction
- explain when manual review is required instead of implying success

## Non-Goals

- This phase does not define a full benchmark harness or runtime implementation.
- This phase does not replace scientific review; it sketches substrate-level gates that would need to happen before scientific interpretation.
