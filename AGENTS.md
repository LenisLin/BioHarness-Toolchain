# BioHarness Toolchain Repo Instructions

This file sets stable repo-wide instructions for Codex sessions in this repository.
Keep it short. Put detailed topic logic and evolving substrate design in the relevant project docs or topic artifacts, not here.

- Nested `AGENTS.md` or `AGENTS.override.md` files may add narrower rules for subtrees.
- When opening a new Codex window for focused work, start from the narrowest relevant directory.

## Repo Role

- This repository is the tools and infrastructure repository within BioHarness.
- In scope: toolchain assets, substrate blueprints, contracts, execution-surface planning, validation scaffolds, and supporting scripts/tests for the current vertical.
- Out of scope here: audit, governance, and upper-level reasoning or brain responsibilities.

## Current Direction

- The first vertical remains spatial transcriptomics downstream analysis.
- The Layer 1 method registry provides the baseline evidence for what methods exist.
- The current substrate phase is a bioagent-oriented tool substrate effort. It is not a continuation of broad Layer 1 table expansion.
- Layer 1 registry inclusion does not by itself imply core candidacy, a stable execution surface, or rewrite priority.
- Do not describe pilots, examples, or blueprint artifacts as frozen architecture unless a current project document explicitly locks the decision.

## Durable Sources Of Truth

- Start with:
  - `README.md`
  - `docs/README.md`
  - `docs/overview.md`
  - `docs/scope.md`
  - `docs/layer1_2/layer1_method_registry_and_substrate_transition.md`
- Use `docs/layer1_2/layer1_method_registry_and_substrate_transition.md` as the current anchor for Layer 1 method-registry state and the minimum agreed substrate transition note.
- Record unresolved substrate questions in the narrowest relevant current project document or topic artifact. Do not recreate a central working buffer unless the project explicitly reopens that workflow.
- For tasks that touch substrate design, load only the relevant sections of:
  - `docs/substrate/environment_strategy.md`
  - `docs/references/agent_runtime_reference.md`
  - `docs/substrate/interface_contract.md`
  - `docs/substrate/rewrite_policy.md`
  - `docs/substrate/validation.md`
- Treat material under `contracts/`, `skills/`, `surface_registry/`, and `evals/` as blueprint artifacts unless a higher-authority document says otherwise.
- If a decision is not written in the current project docs or the relevant current topic artifact, it is not frozen.

## Layer Discipline

- Layer 1: analysis-problem and task-family routing.
- Layer 2: task-family method knowledge pack and decision tree.
- Layer 3: execution surface registry and callable contract.
- Layer 4: backend adapter, wrapper, or rewrite implementation.
- Layer 1 and Layer 2 are knowledge layers.
- Layer 3 is the first machine-readable execution-planning layer.
- Layer 4 is the concrete implementation layer.
- The brain should normally receive Layer 1, then selected Layer 2, then selected Layer 3.
- Layer 4 should be exposed only for implementation, debugging, or audit.
- Do not collapse Layer 2 method-comparison material into Layer 3 execution surfaces.
- Do not collapse Layer 3 surface contracts into Layer 4 adapter code.
- Topic-specific Layer 2 freezes belong in the relevant topic artifact, not in this top-level file.
- The following remain post-research decisions unless frozen in the relevant current project document or topic artifact:
  - execution-surface counts
  - adapter boundaries
  - per-tool rewrite granularity
  - final callable signatures
  - internal module layout

## Discussion And Mutation Guardrails

- During design discussion, do not harden open substrate questions into repo-level engineering commitments.
- Do not modify NAS topic-pilot files or other authoritative external artifacts unless the task explicitly calls for that mutation.
- When work is topic-specific, update the relevant topic artifact before promoting anything into repo-wide instructions.
- Do not backfill topic-specific Layer 2 detail into this file unless it changes repo-wide policy.
- During the current scientific-planning and engineering-implementation phase, do not run strict language audits as a blocking review criterion.
- Documentation review should prioritize scientific semantic consistency, field/schema alignment, valid paths, and conflicts between planning and runtime status.
- Treat boundary phrases such as `planning-only`, `not implemented`, and `not production` as acceptable when they preserve factual status; raise them only when they create factual errors, semantic conflicts, or conflict with an explicit user request.

## Engineering Trial Vs Formal Development

- For non-trivial workflow expansion, first distinguish whether the task is an engineering trial or formal development.
- Treat unclear early-stage work as an engineering trial unless the task explicitly asks for executable or runtime support.
- During engineering trials, prefer documentation-first reading, minimum-common-denominator integration, and small staged experiments.
- Record trial assumptions and findings, but do not turn ordinary unknowns into formal blockers unless they affect the stated trial goal.
- During formal development, define preconditions, environment execution checks, validation gates, and acceptance checks before claiming executable support.
- Keep trial findings, prototype behavior, runtime support, production readiness, and stable architecture claims clearly separate.
- A successful trial may inform formal development, but does not by itself establish stable APIs, runtime support, or production readiness.

## Verification And Claims

- Do not claim a check passed unless you ran it.
- Do not present a hypothesis, pilot, or blueprint example as confirmed architecture.
- Keep non-trivial research or design claims traceable to local docs, current scripts/tests, or current artifacts when possible.

## Delegation And New Windows

- Use the narrowest relevant context.
- Pass task delta and the minimum file set needed for the subtask.
- Name concrete input paths, intended output path, and required verification target in every handoff.
- Prefer on-disk state over long chat summaries.
