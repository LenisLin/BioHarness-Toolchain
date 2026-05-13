# Layer 1/2 To Layer 3/4 Handoff

## Purpose

Describe how Layer 1/2 knowledge artifacts provide the evidence package for Layer 3/4 execution planning.

Layer 1 routes a task to an `Analysis Problem`. Layer 2 organizes method-selection evidence for that problem. The handoff step carries the selected method context, constraints, and execution-relevant signals into a `MethodExecutionPlanningRecord` for Layer 3/4 planning.

## Handoff Position

The handoff sits at the exit of Layer 1/2 work. It belongs with Layer 1/2 documentation because it explains how scientific task framing and method-selection evidence become input to execution planning.

Layer 3/4 planning then uses this input to draft:

- a Layer 3 `ExecutionSurfaceSpec`
- a Layer 4 `BackendAdapterSpec`
- an environment profile or environment plan
- an adaptation decision
- validation and evaluation requirements

## Source Evidence

Layer 1/2 handoff should be grounded in the current source-of-truth order described in [Layer 1 method registry and substrate transition](layer1_method_registry_and_substrate_transition.md) and the reusable Layer 2 rules in [Tool taxonomy](tool_taxonomy.md).

For a completed Analysis Problem, the source package normally includes:

- problem boundary
- method feature table
- decision tree
- topic closure
- representative Layer 3/4 planning-review notes when available

## Layer 2 Gate

Before an Analysis Problem moves into `knowledge_registry/layer2` method-selection presentation and later Layer 3 entry review, it should have a complete topic package:

- `README.md`
- `topic_scope.md`
- `field_registry.json`
- `method_table.csv`
- `method_table.md`
- `method_table.json`
- `review_decision_tree.md`
- `closure.md`

The complete topic package precedes knowledge-registry rendering. The Layer 2 output is one agent-facing Markdown file per completed Analysis Problem. That file should contain a problem boundary, a method feature table, and an embedded decision tree.

Crossing into Layer 3 means the topic is eligible for execution-surface planning, environment-profile consideration, Layer 3/4 contract drafting, adaptation review, and validation planning. It does not by itself establish runtime support, adapter availability, or production readiness. Once promoted, a method can enter a `MethodExecutionPlanningRecord` that produces separate Layer 3 and Layer 4 drafts from the same repository and code inspection.

## Handoff Contents

A Layer 3/4 planning record should receive a compact handoff rather than the full Layer 2 working package. The handoff should preserve:

- `layer2_branch`
- `method_role`
- `selection_context`
- `caveats`
- `evidence_summary`
- `hardware_resource_tag`
- `applicability_notes`

Execution-relevant hard constraints should be carried forward as separate planning inputs:

- required modalities
- forbidden modalities
- required input object
- required spatial information
- histology requirement
- reference requirement
- GPU requirement
- multi-sample policy
- minimum dataset assumptions

## MethodExecutionPlanningRecord Field Range

Layer 1/2 handoff contributes the selected-method context and hard constraints to `MethodExecutionPlanningRecord v0.7.1`. It should inform:

- `layer2_to_layer3_handoff`
- `hard_constraints_for_layer3`
- `canonical_surface_reference`
- `environment_plan`
- `rewrite_decision`
- `validation_runtime_plan`
- `risk_register`
- `decision_log`

Layer 3/4 planning then resolves repository evidence, code evidence, execution-surface mapping, backend binding, environment planning, bounded-equivalence validation, and readiness gates inside the planning record. Where the protocol uses `rewrite_decision`, that field should be interpreted within the current adaptation-policy vocabulary.

## Evidence Translation

Layer 2 answers when a method is scientifically appropriate for a task family. Layer 3/4 planning translates the execution-relevant part of that evidence into:

- semantic inputs and outputs
- parameter policy
- coordinate and image requirements
- environment expectations
- backend binding targets
- adaptation signals
- validation and bounded-equivalence requirements

This translation keeps method-selection reasoning traceable while giving execution planning a compact and auditable starting point.

## Deferred Evidence Questions

The exact amount of repository, documentation, and runnable-code evidence required before a method becomes an implementation candidate remains a post-research decision. Until that threshold is frozen in a topic artifact or current project document, Layer 3/4 handoff should distinguish method-selection evidence from implementation readiness.

## Current Spatial Domain Use

For `spatial_domain_identification`, the current handoff path uses the NAS topic evidence and the repo Layer 1/2 registry context to support a small Layer 3/4 planning pilot. The pilot uses the `MethodExecutionPlanningRecord v0.7.1` protocol described in [Method execution planning protocol](../layer3_4/method_execution_planning_protocol.md) and the current Layer 3/4 workspace summary in [Layer 3/4 planning workspace](../layer3_4/README.md).
