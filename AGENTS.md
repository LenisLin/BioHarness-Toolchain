# BioHarness Toolchain Repo Instructions

This file sets stable repo-wide instructions for Codex sessions in this repository.
Keep it short. Put detailed topic logic and evolving Round 2 design in the relevant project docs or topic artifacts, not here.

- Nested `AGENTS.md` or `AGENTS.override.md` files may add narrower rules for subtrees.
- When opening a new Codex window for focused work, start from the narrowest relevant directory.

## Repo Role

- This repository is the tools and infrastructure repository within BioHarness.
- In scope: toolchain assets, substrate blueprints, contracts, execution-surface planning, validation scaffolds, and supporting scripts/tests for the current vertical.
- Out of scope here: audit, governance, and upper-level reasoning or brain responsibilities.

## Current Direction

- The first vertical remains spatial transcriptomics downstream analysis.
- Round 1 provides the baseline evidence for what methods exist.
- Round 2 is a bioagent-oriented tool substrate effort. It is not a continuation of broad Round 1 table expansion.
- Round 1 inclusion does not by itself imply Round 2 core candidacy, a stable execution surface, or rewrite priority.
- Do not describe working buffers, pilots, or blueprint examples as frozen architecture unless a project document explicitly locks the decision.

## Durable Sources Of Truth

- Start with:
  - `README.md`
  - `docs/10_scope.md`
  - `docs/12_round2_working_buffer.md`
  - `docs/15_round1_baseline_and_round2_prep.md`
- Use `docs/15_round1_baseline_and_round2_prep.md` as the current anchor for Round 1 baseline state and the minimum agreed Round 2 transition note.
- Use `docs/12_round2_working_buffer.md` for unresolved Round 2 questions and working hypotheses. It does not freeze architecture.
- For tasks that touch Round 2 substrate design, load only the relevant sections of:
  - `docs/30_env_strategy.md`
  - `docs/35_agent_runtime_reference.md`
  - `docs/40_interface_contract.md`
  - `docs/50_rewrite_policy.md`
  - `docs/60_validation.md`
- Treat material under `contracts/`, `skills/`, `surface_registry/`, and `evals/` as blueprint artifacts unless a higher-authority document says otherwise.
- If a decision is not written in the current project docs or the relevant current topic artifact, it is not frozen.

## Layer Discipline

- Layer 1: agent-facing tool directory.
- Layer 2: tool family, algorithm options, and distinguishing characteristics.
- Layer 3: rewritten or unified invocation layer.
- Layer 1 and Layer 2 are knowledge layers. Layer 3 is the first engineering-facing layer.
- Do not collapse Layer 2 comparison material into a claimed Layer 3 default unless that default has been explicitly frozen.
- Topic-specific Layer 2 freezes belong in the relevant topic artifact, not in this top-level file.
- The following remain post-research decisions unless frozen elsewhere:
  - execution-surface counts
  - adapter boundaries
  - per-tool rewrite granularity
  - final callable signatures
  - internal module layout

## Discussion And Mutation Guardrails

- During design discussion, do not harden open Round 2 questions into repo-level engineering commitments.
- Do not modify NAS topic-pilot files or other authoritative external artifacts unless the task explicitly calls for that mutation.
- When work is topic-specific, update the relevant topic artifact before promoting anything into repo-wide instructions.
- Do not backfill topic-specific Layer 2 detail into this file unless it changes repo-wide policy.

## Verification And Claims

- Do not claim a check passed unless you ran it.
- Do not present a hypothesis, pilot, or blueprint example as confirmed architecture.
- Keep non-trivial research or design claims traceable to local docs, current scripts/tests, or current artifacts when possible.

## Delegation And New Windows

- Use the narrowest relevant context.
- Pass task delta and the minimum file set needed for the subtask.
- Name concrete input paths, intended output path, and required verification target in every handoff.
- Prefer on-disk state over long chat summaries.
