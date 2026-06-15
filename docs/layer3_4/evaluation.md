# Evaluation

## Purpose

Layer 3/4 evaluation defines how a planned or implemented BioHarness execution path will be checked against its parent-function contract and compared with the native method behavior it claims to preserve.

Evaluation evidence must be proportional to the claim. Runtime completion does not prove biological correctness or algorithmic equivalence.

In the current stage-integration workflow, evaluation is primarily validation-handling and comparison planning. Post-build method validation begins only after reviewed environment evidence, downstream-selectable Layer3/4 build evidence, and prepared validation inputs are available. Input preparation and reference preparation are prerequisite evidence; method harness validation is the run that checks the BioHarness execution path against the parent-function contract.

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

## Case Output Consistency

Author-case preparation and method harness validation may compare execution-surface output with the expected result or author-case output recorded for the selected case.

Use author tutorial or example parameters when they are specified. Use method defaults when the author workflow does not specify a value. Use seed `619` when seed control is exposed and the author workflow does not fix another seed.

For clustering or spatial domain labels, compare labels with a permutation-aware method when label identities are arbitrary. The review may also compare output files, required fields, row counts, domain counts, and expected artifact presence when those are the relevant expected outputs.

When outputs differ, record the difference and review whether it is acceptable for the selected case. Acceptable differences may still support `harness_validation_status: pass` for the case. Unacceptable differences support `harness_validation_status: terminal_fail` only when method harness validation preconditions were available and should record the repair route.

## Evidence Boundaries

Static review can pass when the design is structurally valid and has no unsupported production claims.

Build/execution actions begin only when the relevant Gate 2-reviewed planning item has `approved_for_next_step` and an assigned post-Gate2 step. Layer3 / Layer4 completion evidence consists of a completed `layer3_layer4_build_completion_matrix.tsv` plus per-row `build_output_result.yaml`, `build_audit.yaml`, callable import evidence plus route-level backend load evidence for downstream-selectable build-required rows. Later execution and replay consume downstream-selectable rows only when the referenced environment evidence includes route-level backend load evidence for the selected Layer4 route. These build outputs do not by themselves establish runtime support, output-contract satisfaction, native-behavior preservation, algorithmic equivalence, or biological correctness.

Post-implementation coherence review may be recorded as ordinary evidence when required. It can check whether implemented Layer4 behavior, reviewed environment build output and later reproducibility evidence, validation evidence, output-contract observation, provenance, and failure handling are coherent enough to inform production-readiness review, but it is not a named gate or production-readiness decision.

Production readiness requires actual implementation, successful runtime validation, observed output contract satisfaction, provenance emission, reviewed environment build output, and later reproducibility evidence.
