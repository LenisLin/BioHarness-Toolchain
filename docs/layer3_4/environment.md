# Environment

## Purpose

Layer 3/4 environment design turns method-specific author-visible environment evidence into Text Anchors, environment branches, Environment Build Plans, and reviewed environment build output.

Environment planning is part of the execution scheme. It does not by itself establish runtime support.

This document describes the current Layer3/4 stage-integration environment workflow. It does not change substrate or contract-layer `EnvironmentProfile` concepts.

## Environment Evidence

For each method support design, record the author-visible runtime shape:

- language ecosystem
- package manager
- install files
- dependency constraints
- GPU/CUDA assumptions
- R/Python bridge assumptions
- optional runtime paths
- container, CI, or automation evidence

The result is environment planning evidence, not an executable environment claim.

## Environment Branches

Environment branches are path-safe human-readable host conda environment keys for one analysis problem. They organize selected dependency boundaries and compatible methods before Gate 2 review.

Use `<analysis_problem_code>_<branch_label>` for the branch key where practical. For example, `SDI_base` can identify the base branch for spatial domain identification. Natural-language role descriptions belong in branch role or compatibility notes, not in the path key.

Environment branch planning should identify:

- Text Anchors and source/config locators;
- selected core dependency boundaries;
- gated optional dependency boundaries;
- Layer3 interface targets that the branch is intended to serve;
- the reviewed output path for later environment build execution.

Static dependency risk alone does not justify a final hold or branch split. A stronger split or hold decision requires reviewed build output, impossible dependency constraints, or another explicit implementation-backed reason.

## Environment Build Plan

An Environment Build Plan is the Gate-2-reviewable plan for host conda environment assembly, update, and planned load checks.

It should define the Conda Build Spec, step-by-step build instructions, rollback and split response, and required environment build outputs:

```text
harness_environment.yaml
environment_build.yaml
environment_build.jsonl
```

Install/load checks are internal checks inside the reviewed environment build plan. They are not the workflow's top-level name and do not by themselves establish method workflow success.

The current stage integration workflow supports host conda environment build/update/check only. Docker build is out of scope here.

## Reviewed Build Output

Reviewed environment build output is produced only after Gate 2 approves a filled environment integration planning record and assigns `environment_build_execution`.

`harness_environment.yaml` is the reviewed environment binding record for downstream engineering workflows. Later Layer3/Layer4 build, author-case execution, bridge replay, and validation planning may reference the reviewed environment binding record (`harness_environment.yaml`) or the reviewed environment build output path instead of unreviewed environment records.

Formal harness presentation is resolved later and should not rely on agent-side YAML inference.

## Readiness Boundary

Environment planning and reviewed environment build output do not establish runtime support, functional correctness, production readiness, final support status, method workflow success, author-case success, algorithmic equivalence, or biological correctness.

Optional backend paths should be disabled or marked unavailable until the relevant reviewed build output and later runtime or validation evidence support them.
