# Tool Taxonomy

## Purpose

This document is the current repo-level authority for reusable `Layer 2` rules.

It defines what `Layer 2` must produce for any topic, how topic-level selection artifacts relate to one another, and which parts of topic work can later be promoted into reusable policy.

## Status

This document is authoritative for reusable `Layer 2` structure and process.

It does not freeze:

- topic-specific branch logic
- topic-specific benchmark whitelists
- per-tool execution details
- `Layer 3` execution-surface design

Those remain in topic artifacts or later-phase documents.

## Layer 1 / Layer 2 Boundary

Layer 1 is the compact agent-facing toolbox catalog. It should expose one entry per task family or analysis problem, not the full Layer 1 method registry.

Layer 1 entries should be short family cards. They help the agent decide which task family to enter and then route to the relevant Layer 2 material.

Layer 2 is entered only after a task family is selected. It produces a method knowledge pack, a method table, and a decision tree for that task family.

Layer 1 and Layer 2 are agent-facing knowledge layers. Layer 2 answers `when to choose`, not `how to run`.

## Layer 2 Role

`Layer 2` exists to support `when to choose`, not `how to run`.

It operates at the level of:

- task slot
- tool family
- algorithm options
- distinguishing characteristics
- branch-local ranking evidence

It does not define:

- commands
- parameter lists
- input schemas
- execution surfaces
- environment bindings
- adapter boundaries
- adapter internals
- callable signatures
- repo or module structure

Layer 2 output should include enough fields to support Layer 3 entry review, but a Layer 2 field is not an implementation claim.

## Suggested Layer 1 Family Card

```yaml
family_id: spatial_domain_identification
display_name: Spatial domain identification
when_to_use:
  - identify tissue domains
  - cluster spatially coherent regions
  - discover tumor/stroma/interface regions
typical_inputs:
  - expression matrix
  - spatial coordinates
  - optional histology image
typical_outputs:
  - domain labels
  - spatial plots
  - optional latent embedding
route_to_layer2: docs_or_artifact_path
not_for:
  - ligand-receptor inference
  - cell type deconvolution
  - cell segmentation
```

## Recommended Layer 2 Field Set

Topic-specific Layer 2 schemas may vary, but future method knowledge packs should consider fields such as:

- `native_ecosystem`
- `backend_language`
- `native_object_model`
- `callable_surface_type`
- `required_input_modalities`
- `optional_input_modalities`
- `histology_policy`
- `multi_slice_support`
- `gpu_policy`
- `reference_required`
- `output_type`
- `output_schema_candidate`
- `installation_risk`
- `api_stability`
- `maintenance_status`
- `license_status`
- `minimal_test_data_available`
- `validation_anchor`
- `adapter_candidate_status`

`adapter_candidate_status` is a Layer 3 promotion signal, not an implementation claim. Controlled values:

- `core_anchor`
- `thin_adapter`
- `strong_wrapper`
- `rewrite_candidate`
- `legacy_capsule`
- `hold`

This signal is preliminary. If a method is promoted after Layer 2 selection, a Layer 3/4 `MethodExecutionPlanningRecord` should refine it into separate Layer 3 surface planning, Layer 4 backend binding, environment assignment, validation requirements, and a documented rewrite decision.

## Standard Topic Artifacts

Every topic that reaches `Layer 2` should eventually produce the following three artifacts:

1. a `subtable .csv`
2. a `field registry .json`
3. a standalone `decision tree` file

These artifacts have distinct roles:

- the `subtable .csv` stores row-level topic results
- the `field registry .json` defines field meaning, fill rules, and controlled values
- the `decision tree` encodes topic-level selection logic derived from the subtable

Human-readable companion documents may exist, but they do not replace the required artifact set above.

## Field Model

### Shared fields

Shared fields carry reusable selection signals that may appear across multiple topics.

Examples include:

- canonical tool identity
- method-family label
- high-level input picture
- high-level output object
- coarse compute requirement
- code access state
- evidence-source classification

### Topic-specific fields

Topic-specific fields are allowed only when they add real selection value inside the current topic.

They should not be promoted to reusable shared fields unless they recur across multiple topics with stable meaning.

### Temporary fields

Some fields may exist only during topic bootstrapping.

`Tier` is the current example:

- it is a temporary pilot-only retrieval or coverage field
- it should not become the long-term recommendation mechanism
- once a topic-level decision tree is stable, recommendation priority should move into the tree and `Tier` should be removed

## Decision Tree Contract

The `decision tree` is a formal `Layer 2` artifact.

It must satisfy all of the following:

- be generated after the topic subtable exists
- derive its branch logic from subtable fields rather than from a separate subjective system
- remain a selection artifact rather than an execution artifact
- keep benchmark or review evidence as branch-local ranking support rather than root-level universal ranking

The tree may be stored in any shareable format, but it must remain a standalone file rather than being embedded as a table column.

## Benchmark And Review Use

When suitable benchmark or review literature exists for a topic:

- a benchmark or review pass is required before the topic-level decision tree is finalized
- the evidence should be used for branch-local ranking, tie-breaks, or metric-specific ordering
- it should not replace task-fit branching
- it should not be converted into a global all-method ranking

When no suitable benchmark or review literature exists:

- the topic may proceed using a logic review instead
- the absence of suitable benchmark or review support should be stated explicitly in the topic artifact

Specific benchmark or review whitelist contents are topic-local and should not be frozen in this document.

## Topic Workflow

The expected `Layer 2` workflow for a new topic is:

1. freeze the topic candidate set
2. freeze the topic field schema
3. produce the topic `subtable .csv`
4. produce the topic `field registry .json`
5. run a benchmark or review pass when suitable literature exists, otherwise run a logic review
6. build the topic `decision tree`
7. perform at least one review or audit pass

Only after this sequence is complete should the topic be considered ready for `Layer 3` entry review.

Layer 3 entry review should not become a second independent repository audit. For promoted methods, it should normally start the Layer 3/4 co-design workflow described in [Layer 3/4 Co-design](82_layer3_4_codesign.md), while keeping final Layer 3 and Layer 4 artifacts separate.

## Promotion Rule

Topic conclusions should only be promoted into repo-level policy when they are:

- reusable across topics
- stated independently of one topic's local branch structure
- evidence-bounded rather than convenience-driven

Topic-specific branch logic, edge-case method placement, and local comparator decisions should remain in topic artifacts unless later evidence shows they generalize.

## Non-Goals

This document does not:

- freeze any one topic's local decision tree
- define benchmark whitelist contents
- define runtime implementations
- define execution-surface counts
- define wrapper or adapter boundaries
- define final callable signatures
