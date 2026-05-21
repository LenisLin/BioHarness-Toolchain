# Evaluation

## Purpose

Layer 3/4 evaluation defines how a planned or implemented BioHarness execution path will be checked against its parent-function contract and compared with the native method behavior it claims to preserve.

Evaluation evidence must be proportional to the claim. Runtime completion does not prove biological correctness or algorithmic equivalence.

In the current stage-integration workflow, evaluation is primarily validation-handling and comparison planning. Post-implementation validation begins only after reviewed build output, reviewed environment build output when required, and author-case/native workflow or bridge-replay evidence have been produced under the relevant parent-function contract.

## Native-Behavior Comparison

When a backend is adapted through an adapter, wrapper, or rewrite, evaluation should define:

- native comparison target
- BioHarness-supported path
- author-provided case, tutorial, vignette, example, repository-provided test data, or explicitly approved validation fixture
- version and environment boundary
- seed and stochasticity policy
- output metrics
- tolerance or review criteria
- known non-equivalences

For clustering or spatial domain identification, validation should account for label permutation, domain count, no-empty-domain checks, ARI/NMI/AMI when appropriate, and spatial sanity checks.

In current stage-integration functional testing, author-provided cases are the primary evidence source. Synthetic or minimal BioHarness-created fixtures belong to runtime-result validation only if explicitly approved by a current design document.

## Evidence Boundaries

Static review can pass when the design is structurally valid and has no unsupported production claims.

Build/execution actions begin only when the relevant Gate 2-reviewed planning item has `approved_for_next_step` and an assigned post-Gate2 step. Layer3 / Layer4 build should produce `build_output_result.yaml` and `build_audit.yaml`. These build outputs can support later execution and bridge replay, but they do not by themselves establish runtime support, output-contract satisfaction, native-behavior preservation, algorithmic equivalence, or biological correctness.

Gate 3, when used, is a post-implementation harness integration review. It checks whether implemented Layer4 behavior, reviewed environment build output and later reproducibility evidence, validation evidence, output-contract observation, provenance, and failure handling are coherent enough to enter production-readiness review. Gate 3 acceptance does not establish production readiness by itself.

Production readiness requires actual implementation, successful runtime validation, observed output contract satisfaction, provenance emission, reviewed environment build output, and later reproducibility evidence.
