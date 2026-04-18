# Rewrite Policy

## Purpose

Record a working blueprint for how Round 2 may later decide whether a tool should stay behind a thin adapter, move behind a stronger wrapper, or enter a rewrite track.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries in [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md).

## Current Working Direction

The current proposal evaluates rewrite decisions from an `agent-runtime` perspective rather than from software novelty alone. The default order under discussion is:

1. keep mature frameworks behind a thin adapter
2. add a `wrapper` when the public callable surface needs tightening
3. escalate to rewrite only when wrapper-level control is not enough

## Rewrite Signals

The following signals would raise rewrite priority if this blueprint is accepted:

- no stable CLI/API or no maintainable callable entry path
- severe environment fragmentation across methods in the same task family
- output cannot be validated in a reliable post-run step
- failure semantics are implicit, silent, or package-internal only
- the package exposes too much low-level detail for an agent to use safely

## Preferred Responses

| Condition | Preferred response |
| --- | --- |
| Mature package with a stable CLI/API and clear artifacts | Thin adapter plus fixed best-practice template |
| Callable path exists but parameters, outputs, or logs are inconsistent | Stronger wrapper with explicit surface contract |
| Environment fragmentation blocks reliable dispatch | Consolidate behind shared `EnvironmentProfile` definitions |
| Output cannot be validated or failure semantics remain opaque after wrapping | Candidate for rewrite or deeper internal reimplementation |

## Guardrails

- Round 1 inclusion does not imply rewrite priority.
- Large, mature frameworks should not become rewrite targets by default.
- Rewrite should be justified by execution reliability, validation quality, or operator burden, not by abstract architectural preference.
- When the main pain point is interface control rather than algorithmic weakness, use a wrapper first.

## Deferred Questions

- Exact per-tool rewrite thresholds still depend on repository review and benchmark evidence.
- Acceleration-oriented rewrites remain in scope, but only after callable stability and validation quality are understood.
