# Layer 1/2 To Layer 3/4 Handoff

## Purpose

Describe how Layer 1/2 knowledge artifacts provide the evidence package for Layer 3/4 execution planning.

Layer 1 routes a task to an `Analysis Problem`. Layer 2 organizes method-selection evidence for that problem. The handoff step carries the selected method context, constraints, and execution-relevant signals into Layer 3/4 execution-scheme planning and the relevant downstream planning records.

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

Crossing into Layer 3 means the topic is eligible for execution-surface planning, environment-profile consideration, Layer 3/4 contract drafting, adaptation review, and validation planning. It does not by itself establish runtime support, adapter availability, or production readiness. Once promoted, a method can enter Layer 3/4 execution-scheme planning that creates or updates separate downstream planning records for parent-function fit, Layer4 bridge planning, environment integration planning, and functional testing planning.

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

## Layer 3/4 Planning Range

Layer 1/2 handoff contributes selected-method context and hard constraints to Layer 3/4 execution-scheme planning. It should inform:

- parent-function target
- strict input-contract constraints
- strict output-contract constraints
- environment planning inputs
- Layer 4 support signals
- bounded native-behavior evaluation requirements
- downstream planning record fields
- open planning questions and repair targets

Layer 3/4 planning then resolves repository evidence, code evidence, parent-function fit, backend support strategy, environment planning, bounded evaluation, storage boundaries, review stages, and Gate 2 named-next-step decisions. Adaptation decisions should use the current adaptation-policy vocabulary: `core_anchor`, `thin_adapter`, `strong_wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, `legacy_capsule`, or `hold`.

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

The exact amount of repository, documentation, and runnable-code evidence required before a method becomes an implementation candidate remains a post-research decision. Until that threshold is frozen in a topic artifact or current project document, Layer 3/4 handoff should distinguish method-selection evidence from entry into implementation/build as a Gate 2-reviewed named next step.

## Current Spatial Domain Use

For `spatial_domain_identification`, the current handoff path uses the NAS topic evidence and the repo Layer 1/2 registry context to support Layer 3/4 execution-scheme planning. The current Layer 3/4 entry points are [Layer 3/4 execution scheme](../layer3_4/README.md), [Stage integration](../layer3_4/stage_integration/README.md), and [Gate 2 downstream planning review](../layer3_4/stage_integration/downstream_planning_review.md).
