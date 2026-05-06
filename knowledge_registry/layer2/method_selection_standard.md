# Layer 2 Method Selection Standard

This document defines the Layer 2 method-selection presentation standard for the BioHarness spatial transcriptomics knowledge registry.

Layer 2 topic files are agent-facing method-selection results. They help an agent choose methods within a selected Layer 1 `Analysis Problem`. They are not command manuals, parameter schemas, environment bindings, adapter designs, default-method policies, or execution-readiness claims.

Layer 2 topic completion is defined separately by `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/TOPIC_COMPLETION_STANDARD.md`. A knowledge-registry topic Markdown file is rendered only from a completed Layer 2 working/evidence package.

## Topic Unit

The Layer 2 topic unit is the Layer 1 `Analysis Problem`.

The registry `Subtask` field is not a Layer 2 knowledge-registry hierarchy level. It may inform working branches, but Layer 2 topic files should use analysis-topic and method-branch language.

If two method branches cannot share a candidate-set context, field model, or decision tree, they may later be handled as separate analysis topics. That split is a manual decision, not an automatic consequence of the registry `Subtask` field.

## Working And Registry Artifacts

Layer 2 has two artifact classes.

Working/evidence artifacts support construction, review, consistency checks, evidence traceability, caveat tracking, and later engineering review. They remain outside the knowledge-registry presentation layer, normally under the non-registry Layer 2 results workspace.

Knowledge-registry artifacts are compact agent-facing method-selection files under `knowledge_registry/layer2`.

## Registry Generation Gate

Before a Layer 2 topic Markdown file is generated, the corresponding Layer 2 topic package must be complete under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/TOPIC_COMPLETION_STANDARD.md`.

The completed package should include:

- `README.md`
- `topic_scope.md`
- `field_registry.json`
- `method_table.csv`
- `method_table.md`
- `method_table.json`
- `review_decision_tree.md`
- `closure.md`

## Topic Markdown Shape

Each completed Analysis Problem should have one knowledge-registry Markdown file:

```text
knowledge_registry/layer2/<analysis_problem_slug>.md
```

Each topic Markdown must contain these sections, in this order:

1. `Problem boundary`
2. `Method feature table`
3. `Decision tree`

Do not create a topic Markdown for unfinished topics.

## Method Feature Table

The method feature table should be compact but decision-useful. It must preserve the completed topic's candidate set and should not silently omit methods that belong to that topic's frozen Layer 2 package.

Topic tables use a small shared base plus topic-specific selection fields.

Base fields:

| Column | Purpose |
| --- | --- |
| `Method` | Canonical method name. |
| `Selection role` | Positive role of the method in the analysis problem. |
| `Main input/signal` | Main data signal or input condition relevant to method selection. |
| `Main output` | High-level output object. |

Optional shared cues may be added when useful, such as `Feature summary`, `Modality cue`, `Multi-sample/batch cue`, or `Compute/code cue`.

Topic-specific selection fields are allowed when they carry real method-selection value inside the current Analysis Problem. Examples include spatial specificity, reference dependence, resolution, branch family, perturbation design, cohort structure, modality, or other problem-local cues. Keep these fields few, explicit, and derived from the completed working/evidence package.

The table should use positive selection language. Avoid exclusionary columns such as `Avoid when` or `Do Not Start With This When`; use the decision tree to express conditional routing instead.

## Decision Tree

The decision tree must be embedded in the same topic Markdown file.

Use condition-branch language that an agent can follow directly:

```text
If ...
- Prefer / consider ...

If ...
- Prefer / consider ...
```

The knowledge-registry tree should be compressed from the topic's working `review_decision_tree.md`. It should preserve method-selection branches and scientific target conditions while leaving retrieval details, benchmark queries, evidence spot-check tables, coverage ledgers, source links, and engineering handoff notes in the working/evidence package.

Benchmark or review evidence may support branch-local ordering or tie-breaking, but it must not become a universal all-method ranking.

## Content Boundaries

Layer 2 topic files should not include:

- source artifact links
- long caveat or uncertainty notes
- exclusionary method-description columns
- commands
- parameter schemas
- package installation steps
- callable signatures
- environment bindings
- adapter boundaries
- adapter internals
- default-method claims
- execution-readiness claims
- runtime-support claims

These details belong in working/evidence artifacts or later engineering-stage artifacts, not in Layer 2 method-selection presentation.

## Recommended Topic Slugs

| Analysis Problem | Formal topic file |
| --- | --- |
| Artifact Correction | `artifact_correction.md` |
| Cell Type Inference | `cell_type_inference.md` |
| Cell-Cell Communication | `cell_cell_communication.md` |
| Data Quality Control | `data_quality_control.md` |
| Denoising / Signal Recovery | `denoising_signal_recovery.md` |
| Domain / Clustering | `domain_clustering.md` |
| Gene Expression Prediction / Imputation | `gene_expression_prediction_imputation.md` |
| Graph / Neighborhood | `graph_neighborhood.md` |
| Integration | `integration.md` |
| Normalization | `normalization.md` |
| Panel Design | `panel_design.md` |
| Phenotype- / Cohort-linked Spatial Feature and Niche Analysis | `phenotype_cohort_linked_spatial_feature_niche_analysis.md` |
| Program Discovery | `program_discovery.md` |
| Segmentation | `segmentation.md` |
| Spatial Clonal Analysis | `spatial_clonal_analysis.md` |
| Spatial Contrast Testing | `spatial_contrast_testing.md` |
| Spatial Perturbation Analysis | `spatial_perturbation_analysis.md` |
| Spatial Trajectory Analysis | `spatial_trajectory_analysis.md` |
| Spatially Variable Gene Detection | `spatially_variable_gene_detection.md` |
| Super-resolution | `super_resolution.md` |

## Current Scope

This standard defines the method-selection presentation contract only. It does not create topic-specific files by itself.
