# Tool Taxonomy

## Purpose

This document is the current repo-level authority for reusable `Layer 2` rules.

It defines the boundary between Layer 1 analysis-problem routing, Layer 2 method-selection presentation, and later Layer 3/4 execution planning.

## Status

This document is authoritative for reusable `Layer 2` structure and process.

It does not freeze:

- topic-specific branch logic
- topic-specific benchmark whitelists
- per-tool execution details
- `Layer 3` execution-surface design

Those remain in topic artifacts or later-phase documents.

## Layer 1 / Layer 2 Boundary

Layer 1 is the compact agent-facing toolbox catalog. Its stable routing unit is the `Analysis Problem`.

Formal Layer 2 is entered only after an agent has selected a Layer 1 `Analysis Problem`. It presents method-selection results for that analysis problem.

The registry `Subtask` field is not a formal Layer 2 hierarchy level. It may inform working analysis or branch structure, but formal Layer 2 files should use analysis-topic and method-branch language instead of subtask directories or subtask package names.

If two method branches cannot share a candidate-set context, field model, or decision tree, they may later be discussed as separate analysis topics. That split is a manual decision, not an automatic consequence of the registry `Subtask` field.

Layer 1 and Layer 2 are agent-facing knowledge layers. Layer 2 answers `when to choose`, not `how to run`.

## Layer 2 Role

`Layer 2` exists to support `when to choose`, not `how to run`.

Layer 2 has a heavy working/evidence completion standard under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/TOPIC_COMPLETION_STANDARD.md`, and a lightweight formal presentation standard under `/mnt/NAS_21T/ProjectData/BioHarness/results/formal/layer2/method_selection_standard.md`.

It operates at the level of:

- analysis problem
- method branch
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
- default-method claims
- runtime-support claims

Layer 2 output may support later Layer 3 entry review, but Layer 2 selection does not imply Layer 3 or Layer 4 runtime support.

## Suggested Layer 1 Analysis Problem Card

```yaml
analysis_problem: Domain / Clustering
display_name: Domain / Clustering
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
route_to_layer2: formal/layer2/domain_clustering.md
```

## Recommended Layer 2 Field Set

Working/evidence schemas may vary by Analysis Problem, but they should preserve enough information to construct the formal method feature table and embedded decision tree.

Formal method feature tables should use compact, positive selection fields:

- `Method`
- `Selection role`
- `Main input/signal`
- `Main output`
- `Feature summary`
- `Modality cue`
- `Multi-sample/batch cue`
- `Compute/code cue`

Working/evidence materials may also track construction and Layer 3 review signals such as:

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

Layer 2 has two artifact classes.

Working/evidence artifacts support construction, review, and consistency checks. They remain outside the formal presentation layer, normally under the non-formal Layer 2 results workspace.

Before a formal Layer 2 topic Markdown file is generated, the corresponding working/evidence materials must include:

- `README.md`
- `topic_scope.md`
- `field_registry.json`
- `method_table.csv`
- `method_table.md`
- `method_table.json`
- `review_decision_tree.md`
- `closure.md`

Formal artifacts are final agent-facing method-selection files under `formal/layer2`. Each completed Analysis Problem should have one formal Markdown file containing:

1. `Problem boundary`
2. `Method feature table`
3. `Decision tree`

Do not create a formal topic Markdown for unfinished topics.

## Field Model

### Working/evidence fields

Working/evidence fields carry reusable and topic-local selection signals that support candidate-set review, method characterization, and formal presentation.

Examples include:

- canonical tool identity
- method-family label
- high-level input picture
- high-level output object
- coarse compute requirement
- code access state
- evidence-source classification

### Formal fields

Formal fields should be compact and decision-useful. They should use positive selection language and should not include exclusionary columns such as `Avoid when` or `Do Not Start With This When`.

### Topic-local fields

Topic-specific fields are allowed only when they add real selection value inside the current topic.

They should not be promoted to reusable shared fields unless they recur across multiple topics with stable meaning.

### Temporary fields

Some fields may exist only during topic bootstrapping.

`Tier` is the current example:

- it is a temporary pilot-only retrieval or coverage field
- it should not become the long-term recommendation mechanism
- once a topic-level decision tree is stable, recommendation priority should move into the tree and `Tier` should be removed

## Decision Tree Contract

The working/evidence package includes `review_decision_tree.md`. That file records the benchmark/review pass or logic review, coverage checks, evidence spot-checks, and the decision-tree basis for the topic.

The formal decision tree is then embedded in the formal `Layer 2` topic Markdown.

It must satisfy all of the following:

- be generated after the working/evidence materials are complete
- derive branch logic from the working/evidence materials rather than from a separate subjective system
- remain a selection artifact rather than an execution artifact
- keep benchmark or review evidence as branch-local ranking support rather than root-level universal ranking
- use condition-branch language that an agent can follow directly

The formal decision tree should be embedded in the same formal topic Markdown file as the problem boundary and method feature table. The heavier review detail stays in `review_decision_tree.md`.

## Benchmark And Review Use

When suitable benchmark or review literature exists for a topic:

- a benchmark or review pass is required before formal topic generation
- the evidence should be used for branch-local ranking, tie-breaks, or metric-specific ordering
- it should not replace task-fit branching
- it should not be converted into a global all-method ranking

When no suitable benchmark or review literature exists:

- the topic may proceed using a logic review instead
- the absence of suitable benchmark or review support should be stated explicitly in the working/evidence material

Specific benchmark or review whitelist contents are topic-local and should not be frozen in this document.

## Topic Workflow

The expected `Layer 2` workflow for an Analysis Problem is:

1. define the Analysis Problem boundary
2. run bounded retrieval
3. freeze the candidate set
4. produce the field registry `.json`
5. produce the full method table `.csv`, `.md`, and `.json`
6. run a benchmark/review pass when suitable literature exists, otherwise run a logic review
7. derive the review decision tree
8. write topic closure with representative Layer 3/4 audit batch
9. generate one formal topic Markdown with a problem boundary, method feature table, and embedded decision tree

A topic should not be treated as ready for formal rendering unless the complete working/evidence package exists. Representative `Layer 3/4` audit handoff should come from the topic closure package and should not be treated as runtime support.

Layer 3 entry review should not become a second independent repository audit. Review and audit concerns should already be handled inside the benchmark/review or logic-review material. For promoted methods, Layer 3 entry should normally start the Layer 3/4 co-design workflow described in [Layer 3/4 Co-design](82_layer3_4_codesign.md), while keeping final Layer 3 and Layer 4 artifacts separate.

## Promotion Rule

Topic conclusions should only be promoted into repo-level policy when they are:

- reusable across topics
- stated independently of one topic's local branch structure
- evidence-bounded rather than convenience-driven

Topic-specific branch logic, edge-case method placement, and local comparator decisions should remain in topic artifacts unless later evidence shows they generalize.

## Non-Goals

This document does not:

- freeze any one topic's local decision tree
- create any topic-specific formal method-selection file
- define benchmark whitelist contents
- define runtime implementations
- define execution-surface counts
- define wrapper or adapter boundaries
- define final callable signatures
