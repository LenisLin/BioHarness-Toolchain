# Environment Strategy

## Purpose

Record a working blueprint for Round 2 environment design without locking the repository into a single execution provider.

## Status

This document is a working blueprint and is not yet frozen. It does not override the current authority boundaries stated in [docs/15_round1_baseline_and_round2_prep.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/15_round1_baseline_and_round2_prep.md).

## Current Working Direction

Round 2 now treats environment handling as a first-class architecture concern rather than as a later implementation detail. The operative design is provider-neutral and uses the same separation that recent agent runtimes emphasize: the orchestration harness stays lightweight and stateful, while compute remains isolated and disposable.

## Harness vs Compute

### Harness responsibilities

- decompose the user task into a bounded analysis action
- resolve the right skill and default execution surface
- check approval requirements before expensive or sensitive actions
- maintain structured state summaries for resume and compaction
- evaluate outputs and decide whether post-run validation is sufficient

### Compute responsibilities

- execute the chosen surface inside an isolated runtime
- provide the required dependency stack and resource class
- enforce filesystem, network, and secret boundaries
- emit logs, artifacts, and failure signals in a predictable shape
- avoid leaking package-internal complexity back to the harness

This split keeps BioHarness aligned with current agent-runtime practice while avoiding a hard dependency on any one provider. Modal is a useful reference for the separation itself, not a required execution backend.

## `EnvironmentProfile`

`EnvironmentProfile` is the candidate public abstraction for environment selection in the current working blueprint. It is designed to be serializable, reviewable, and reusable across providers if later accepted.

| Field | Meaning |
| --- | --- |
| `profile_id` | Stable identifier for the profile. |
| `isolation_mode` | Isolation boundary such as container, sandbox, or remote worker. |
| `base_stack` | Named dependency stack or pinned package family. |
| `resource_class` | Coarse resource tier such as CPU, GPU, or high-memory GPU. |
| `storage_policy` | Artifact, cache, and mount behavior. |
| `secrets_policy` | Whether external credentials are disallowed, inherited, or explicitly mounted. |
| `provider` | Execution provider or provider-neutral placeholder. |

The repository blueprint may also carry optional operational fields such as `approval_required`, `network_policy`, and `retention_policy`, but those do not replace the required core fields above.

## Operating Rules

- The harness should not infer package-level install steps at run time when an `EnvironmentProfile` already exists.
- A surface that requires `high-cost GPU` execution should resolve to a named profile instead of ad hoc flags.
- Access to an `external resource` with secrets should be routed through explicit approval and a documented `secrets_policy`.
- Environment definitions are planning artifacts for this phase; they do not yet imply a committed runtime implementation under `src/`.

## Repository Blueprint Mapping

- Human-readable policy stays in this document and [docs/35_agent_runtime_reference.md](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/docs/35_agent_runtime_reference.md).
- Machine-readable contract shape lives in [contracts/environment_profile.schema.json](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/contracts/environment_profile.schema.json).
- Example profiles live under [contracts/examples](/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST/contracts/examples).

## Non-Goals

- This phase does not commit BioHarness to Modal, OpenAI sandboxes, Kubernetes, or any other single execution target.
- This phase does not define per-tool Dockerfiles, cluster topology, or deployment automation.
