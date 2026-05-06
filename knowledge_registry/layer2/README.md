# Layer 2 Knowledge Registry Entry

This directory is the repo-authoritative Layer 2 method-selection entry for the BioHarness knowledge registry.

Layer 2 topic files are compact agent-facing method-selection results. They help an agent choose methods within a selected Layer 1 analysis problem.

Layer 2 topic files are not commands, parameter schemas, environment bindings, adapter internals, default-method claims, or runtime-readiness claims.

## Current Standard

- `/mnt/NAS_21T/ProjectData/BioHarness/results/layer2/TOPIC_COMPLETION_STANDARD.md`: Layer 2 topic completion standard for working/evidence packages.
- `method_selection_standard.md`: Layer 2 method-selection presentation standard.

Topic files are created only after the corresponding working/evidence artifacts are complete. Unfinished topics should not have method-selection drafts here.

## Current Topic Files

- `cell_cell_communication.md`: topic file for CCC branch-local method selection.
- `artifact_correction.md`: topic file for artifact-mechanism-local correction selection.
- `data_quality_control.md`: topic file for stage-aware spatial QC selection.
- `denoising_signal_recovery.md`: topic file for same-resolution denoising and signal-recovery selection.
- `normalization.md`: topic file for dedicated spatial-aware normalization plus backbone workflow context.
- `panel_design.md`: topic file for pre-assay targeted panel-design selection.
- `super_resolution.md`: topic file for measured-anchor super-resolution and fine-geometry reconstruction selection.
- `spatial_trajectory_analysis.md`: topic file for spatial trajectory, velocity, pseudotime, and model-based trajectory-structure selection.
- `spatially_variable_gene_detection.md`: topic file for branch-aware spatially variable gene detection selection.
- `segmentation.md`: topic file for segmentation, spot-detection, and support-image branch selection.
- `program_discovery.md`: topic file for heterogeneous program, topic, factor, network, and module discovery selection.
- `gene_expression_prediction_imputation.md`: topic file for branch-aware expression prediction, imputation, reconstruction, calibration, and refinement selection.
- `cell_type_inference.md`: topic file for deconvolution, annotation, placement, reconstruction, and specialized cell-state inference selection.
- `domain_clustering.md`: topic file for branch-aware spatial domain, clustering, semantic, and alignment-aware selection.
- `integration.md`: topic file for alignment, representation, batch-correction, 3D, and multimodal integration selection.
- `graph_neighborhood.md`: topic file for neighborhood, niche, motif, factor, reconstruction, and spatial-context selection.
- `phenotype_cohort_linked_spatial_feature_niche_analysis.md`: topic file for phenotype- and cohort-linked spatial feature, niche, and community-feature association.
- `spatial_contrast_testing.md`: topic file for spatially aware condition, niche, cell-type, and registered-pattern contrast testing.
- `spatial_perturbation_analysis.md`: topic file for perturbation response, counterfactual-style interpretation, observed-effect, and regulator-prioritization selection.
- `spatial_clonal_analysis.md`: topic file for allele-specific CNA, total-CNA, mutation-clone, and spatial CNA-pattern selection.
