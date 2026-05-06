# Layer 1 Task Catalog

This catalog is the compact Layer 1 agent-facing routing interface for BioHarness spatial transcriptomics work. It helps an agent choose one active `Analysis Problem` before opening Layer 2 method-selection material.

Current source of truth: the 2026-05-06 Layer 1/Layer 2 reconciliation and topic-confirmation status. Layer 1 records problem placement and routing only. It does not list methods, rank methods, expose method evidence, or make execution claims.

## Routing Table

| Analysis Problem | Analysis target | Main input or signal | Target output | Route |
| --- | --- | --- | --- | --- |
| Artifact Correction | technical or ambient artifacts in spatial measurements | measured spatial expression, coordinates, optional image or platform artifact signal | artifact-corrected spatial data object or correction report | `knowledge_registry/layer2/artifact_correction.md` |
| Cell Type Inference | cell identity, cell-type composition, or spatial cell-type placement | spatial expression, optional scRNA reference, marker genes, or annotations | cell-type labels, proportions, deconvolution maps, or annotation confidence | `knowledge_registry/layer2/cell_type_inference.md` |
| Cell-Cell Communication | communication, interaction, or neighborhood-effect signal between cells, spots, or cell groups | expression with cell labels or groups, spatial coordinates, LR priors, or neighborhood context | interaction scores, communication networks, spatial LR signals, or pathway-aware CCC summaries | `knowledge_registry/layer2/cell_cell_communication.md` |
| Data Quality Control | sample, spot, cell, gene, or image-derived data quality | raw or early spatial expression object with coordinates and quality metrics | quality flags, filtered data object, or QC report | `knowledge_registry/layer2/data_quality_control.md` |
| Denoising / Signal Recovery | same-resolution noisy or sparse measured spatial expression signal | measured spatial expression matrix with region, graph, or neighborhood context | denoised or recovered expression values at measured spatial units | `knowledge_registry/layer2/denoising_signal_recovery.md` |
| Domain / Clustering | spatially coherent tissue domains, regions, or structural compartments | spatial expression, coordinates, optional image features or graph context | domain labels, spatial clusters, embeddings, or region assignments | `knowledge_registry/layer2/domain_clustering.md` |
| Gene Expression Prediction / Imputation | unmeasured, missing, or cross-modal gene expression values | spatial expression plus spatial layout, reference data, image, or gene/cell networks | predicted, imputed, or completed spatial gene-expression maps | `knowledge_registry/layer2/gene_expression_prediction_imputation.md` |
| Graph / Neighborhood | local spatial neighborhoods, tissue niches, graphs, or cell-neighborhood structure | coordinates, cell labels, expression, morphology, or sample-level neighborhood context | spatial graphs, neighborhood features, niche labels, or local-context representations | `knowledge_registry/layer2/graph_neighborhood.md` |
| Integration | multiple spatial samples, slices, batches, technologies, or coordinate systems | multi-sample or multi-modal spatial expression with coordinates and optional images | integrated embeddings, aligned coordinates, harmonized samples, or joint representations | `knowledge_registry/layer2/integration.md` |
| Normalization | technical scaling or normalization of measured spatial expression | raw or quality-controlled count matrix with spatial sample metadata | normalized expression object ready for downstream analysis | `knowledge_registry/layer2/normalization.md` |
| Panel Design | gene panel or feature set for targeted spatial assays | candidate genes, references, prior marker sets, or assay constraints | selected spatial gene panel or feature set | `knowledge_registry/layer2/panel_design.md` |
| Phenotype- / Cohort-linked Spatial Feature and Niche Analysis | phenotype-, cohort-, or outcome-linked spatial features and tissue niches | spatial features, niche labels, patient/sample metadata, phenotype, or outcome variables | phenotype-associated spatial features, niche scores, or cohort-level associations | `knowledge_registry/layer2/phenotype_cohort_linked_spatial_feature_niche_analysis.md` |
| Program Discovery | latent tissue states, multicellular programs, modules, or coordinated expression programs | spatial expression with optional cell labels, niches, or multi-sample context | program scores, latent factors, module assignments, or spatial program maps | `knowledge_registry/layer2/program_discovery.md` |
| Segmentation | cells, spots, transcripts, boundaries, or spatial units | imaging, transcript locations, morphology, or spatial molecular measurements | segmentation labels, cell boundaries, spatial units, or transcript-to-cell assignments | `knowledge_registry/layer2/segmentation.md` |
| Spatial Clonal Analysis | clones, subclones, copy-number states, or lineage-derived tumor structures | spatial molecular data with genotype, copy-number, mutation, or lineage signal | spatial clone labels, subclone maps, or clonal composition summaries | `knowledge_registry/layer2/spatial_clonal_analysis.md` |
| Spatial Contrast Testing | condition, group, niche, domain, or tissue-context differences | spatial features with condition, group, domain, niche, or sample metadata | differential spatial features, contrast statistics, or condition-associated effects | `knowledge_registry/layer2/spatial_contrast_testing.md` |
| Spatial Perturbation Analysis | spatial response to perturbation, intervention, screen, or altered tissue state | spatial expression plus perturbation labels, guides, treatment, or intervention metadata | perturbation-response effects, spatial response maps, or niche-aware perturbation summaries | `knowledge_registry/layer2/spatial_perturbation_analysis.md` |
| Spatial Trajectory Analysis | spatially organized transitions, progressions, dynamics, or lineage-like states | spatial expression, coordinates, optional time, pseudotime, lineage, or state cues | spatial trajectories, transition maps, ordered states, or spatial dynamics summaries | `knowledge_registry/layer2/spatial_trajectory_analysis.md` |
| Spatially Variable Gene Detection | genes with spatially structured expression patterns | spatial expression with coordinates, optional cell-type or domain context | ranked spatially variable genes, pattern classes, or spatial gene sets | `knowledge_registry/layer2/spatially_variable_gene_detection.md` |
| Super-resolution | finer spatial resolution or subspot spatial structure | lower-resolution spatial expression with coordinates, optional image or reference signal | higher-resolution expression representation or refined spatial tissue map | `knowledge_registry/layer2/super_resolution.md` |

## Problem Routing Logic

Use the user's requested scientific object and target output first, then use available input signals to break ties.

- If the goal is to check or filter raw spatial data quality: route to `Data Quality Control` -> `knowledge_registry/layer2/data_quality_control.md`.
- If the goal is to correct ambient, platform, image, or spatial artifacts: route to `Artifact Correction` -> `knowledge_registry/layer2/artifact_correction.md`.
- If the goal is expression scaling before downstream tasks: route to `Normalization` -> `knowledge_registry/layer2/normalization.md`.
- If the goal is same-resolution recovery of noisy or sparse measured signal: route to `Denoising / Signal Recovery` -> `knowledge_registry/layer2/denoising_signal_recovery.md`.
- If the goal is predicted or completed gene expression at missing or unmeasured locations: route to `Gene Expression Prediction / Imputation` -> `knowledge_registry/layer2/gene_expression_prediction_imputation.md`.
- If the goal is a targeted gene panel or measured feature set: route to `Panel Design` -> `knowledge_registry/layer2/panel_design.md`.
- If the goal is cell, transcript, boundary, or spatial-unit definition: route to `Segmentation` -> `knowledge_registry/layer2/segmentation.md`.
- If the goal is finer spatial resolution from lower-resolution data: route to `Super-resolution` -> `knowledge_registry/layer2/super_resolution.md`.
- If the goal is to align or jointly model samples, slices, batches, technologies, or coordinates: route to `Integration` -> `knowledge_registry/layer2/integration.md`.
- If the goal is local context, tissue niches, neighborhood features, or spatial graph construction: route to `Graph / Neighborhood` -> `knowledge_registry/layer2/graph_neighborhood.md`.
- If the goal is spatially coherent regions, domains, or clusters: route to `Domain / Clustering` -> `knowledge_registry/layer2/domain_clustering.md`.
- If the goal is genes ranked by spatial pattern or spatial variability: route to `Spatially Variable Gene Detection` -> `knowledge_registry/layer2/spatially_variable_gene_detection.md`.
- If the goal is latent programs, multicellular modules, or tissue states: route to `Program Discovery` -> `knowledge_registry/layer2/program_discovery.md`.
- If the goal is cell identity, cell-type composition, deconvolution, or annotation: route to `Cell Type Inference` -> `knowledge_registry/layer2/cell_type_inference.md`.
- If the goal is LR communication, sender-receiver interaction, neighborhood effect, or CCC pathway interpretation: route to `Cell-Cell Communication` -> `knowledge_registry/layer2/cell_cell_communication.md`.
- If the goal is differential spatial signal across conditions, groups, domains, or niches: route to `Spatial Contrast Testing` -> `knowledge_registry/layer2/spatial_contrast_testing.md`.
- If the goal is phenotype-, cohort-, or outcome-linked spatial feature or niche association: route to `Phenotype- / Cohort-linked Spatial Feature and Niche Analysis` -> `knowledge_registry/layer2/phenotype_cohort_linked_spatial_feature_niche_analysis.md`.
- If the goal is spatial progression, transition, trajectory, or ordered state analysis: route to `Spatial Trajectory Analysis` -> `knowledge_registry/layer2/spatial_trajectory_analysis.md`.
- If the goal is spatial organization of clones, subclones, CNV states, mutations, or tumor lineage structure: route to `Spatial Clonal Analysis` -> `knowledge_registry/layer2/spatial_clonal_analysis.md`.
- If the goal is spatial response to perturbation, intervention, treatment, or screen: route to `Spatial Perturbation Analysis` -> `knowledge_registry/layer2/spatial_perturbation_analysis.md`.
