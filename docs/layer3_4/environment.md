# Environment

## Purpose

Layer 3/4 environment design turns author-visible environment evidence into Text Anchors, Method Dependency Groups, an analysis-problem-level Environment Build Plan by default, and reviewed environment build output.

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

## Environment Build Planning

Pre-Gate2 environment planning records Text Anchors, selected core and optional dependency boundaries, Method Dependency Groups, analysis-problem-level assembly order, planned checks, failure responses, split triggers, and required outputs.

Environment build planning is analysis-problem-level by default. Method-specific dependency evidence is organized into Method Dependency Groups so each method's dependency sources, selected core path, optional path, and risk evidence remain reviewable without becoming one output target per method.

Environment build planning may name a path-safe Environment Build Target for reviewed execution/output organization. Use `<analysis_problem_code>_<build_target_label>` where practical. For example, `SDI_environment_build_plan` can identify the current spatial-domain-identification initial build target. Natural-language role descriptions belong in build-target role or compatibility notes, not in the path key.

An Environment Build Target is the reviewed execution/output target for an Environment Build Plan. It is not a default per-method object, and it is not created merely because a method has dependency evidence.

Environment build planning should identify:

- Text Anchors and source/config locators;
- selected core dependency boundaries;
- gated optional dependency boundaries;
- Layer3 interface targets that the build target is intended to serve;
- assembly order and planned build/load checks;
- failure response and Split Triggers;
- the reviewed output path for later environment build execution.

Split Triggers record text-evidence risks such as version, language, GPU/CUDA, or R-bridge conflicts during planning. Actual split decisions require reviewed implementation/environment build evidence, impossible documented constraints, or later review. Static dependency risk alone does not justify a final hold, branch split, output path, or per-method environment target.

## Environment Build Plan

An Environment Build Plan is the Gate-2-reviewable plan for host conda environment assembly, update, and planned load checks for the reviewed Environment Build Target.

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

`harness_environment.yaml` is the reviewed environment binding record for downstream engineering workflows. The `environment_branch` field name is kept inside this future file as a reviewed binding key produced after environment build execution; it is not a pre-Gate2 text-derived branch. Later Layer3/Layer4 build, author-case execution, bridge replay, and validation planning may reference the reviewed environment binding record (`harness_environment.yaml`) or the reviewed environment build output path instead of unreviewed environment records.

Formal harness presentation is resolved later and should not rely on agent-side YAML inference.

## Readiness Boundary

Environment planning and reviewed environment build output do not establish runtime support, functional correctness, production readiness, final support status, method workflow success, author-case success, algorithmic equivalence, or biological correctness.

Optional backend paths should be disabled or marked unavailable until the relevant reviewed build output and later runtime or validation evidence support them.
