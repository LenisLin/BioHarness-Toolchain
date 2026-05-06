# Layer Boundary

Layer 1 is the compact problem-routing level. It helps an agent choose one active spatial transcriptomics `Analysis Problem` using scientific target, input signal, and target output. It is not a method recommendation layer.

Layer 2 is topic-specific method-selection knowledge. It supports method comparison and selection logic within the selected analysis problem. It is not a command manual, parameter schema, environment binding, adapter-internal design, default-method policy, or execution-readiness claim.

Layer 1 inclusion does not imply Layer 2 recommendation. Layer 2 selection does not imply downstream engineering support.

# Current State

The current agent-facing Layer 1/2 entry is this repo `knowledge_registry/`.

The underlying source/evidence artifacts remain under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/` and `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/`.

The current active Layer 1/Layer 2 mapping is the 2026-05-06 reconciliation and topic-confirmation status. It records 20 active Analysis Problems with ready Layer 2 working/evidence packages.

The Layer 1 entry is `layer1/task_catalog.md`, a compact routing table plus problem-routing logic.

The Layer 2 standard is `layer2/method_selection_standard.md`. Topic files are added under `layer2/` after the corresponding working/evidence package is complete and are rendered only for currently tracked completed topics.

# Deferred

This knowledge registry does not define commands, parameter schemas, environment bindings, adapter internals, production adapters, environment capsules, default methods, or execution readiness.
