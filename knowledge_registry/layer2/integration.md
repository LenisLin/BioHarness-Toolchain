# Integration

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Integration`.

This topic covers alignment, latent integration, 3D reconstruction, batch correction, multimodal integration, mosaic multi-omics integration, and cross-sample harmonization for spatial omics. These branches are not interchangeable: coordinate transforms, latent embeddings, count-level correction, 3D tissue maps, and modality-completion outputs should remain distinct during selection.

The current Integration freeze is accepted as 22 candidate rows. `SpaMosaic`, `INSPIRE`, `SpatialCOC`, and `SSpMosaic` are official Integration candidates in the current state, not temporary footnotes. No single best-method sequence is implied by this table or tree.

Use another Layer 1 problem first when the requested endpoint is cell type inference, program discovery, domain clustering, or phenotype association without an integration deliverable. Keep over-alignment, geometry distortion, biological signal removal, modality imbalance, and model opacity visible throughout selection.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Integration Target | Geometry / Model Cue | Cross-Sample Cue | Primary Risk Cue | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAST | cross-sample spatial matching and alignment at single-cell resolution | single-cell or high-resolution spatial omics samples with expression and coordinates | matched cells or spots and aligned spatial correspondence map | search-and-match mapping | search-and-match | single-cell or high-resolution samples | scale sensitivity | Optional GPU; code available |
| DeST-OT | alignment across spatial and temporal transcriptomics states | spatiotemporal transcriptomics samples with expression, coordinates, and time or progression structure | spatiotemporally aligned correspondence or trajectory map | spatiotemporal alignment | optimal transport | spatiotemporal series | temporal-model mismatch | CPU; code available |
| GPSA | non-rigid alignment through smooth spatial warping | spatial genomics datasets with expression features and coordinates | aligned spatial coordinates or latent spatial mapping | coordinate alignment | gaussian process non-rigid warp | same-platform or related spatial genomics samples | scale sensitivity | CPU; code available |
| GraphST | spatially informed representation integration linked to clustering and deconvolution workflows | spatial expression matrix and spatial graph or coordinates | integrated representation or embedding with downstream clustering/deconvolution support | latent embedding integration | graph contrastive representation | spatial samples with graph-neighborhood signal | multi-task objective entanglement | Optional GPU; code available |
| PASTE | pairwise slice alignment and consensus integration | multiple spatial transcriptomics slices with expression and spatial coordinates | aligned slices and consensus slice representation | pairwise slice alignment | optimal transport | same-platform comparable slices | over-alignment of noncorresponding tissue | CPU; code available |
| PASTE2 | partial alignment for multislice spatially resolved transcriptomics | multiple spatial transcriptomics slices with partial overlap or missing regions | partial slice alignment and matched overlapping regions | partial overlap alignment | partial optimal transport | partial or missing-overlap slices | partial-overlap mismatch | CPU; code available |
| PRECAST | joint probabilistic embedding, clustering, and alignment for spatial data integration | multiple spatial transcriptomics samples with expression and coordinates | integrated embedding, aligned samples, and cluster labels | latent embedding integration | probabilistic embedding | multiple spatial transcriptomics samples | cluster-alignment coupling | CPU; code available |
| SANTO | coarse-to-fine alignment and stitched tissue reconstruction | spatial omics sections or fields requiring alignment and stitching | stitched and aligned spatial omics map | stitching and coordinate alignment | coarse-to-fine stitching | multi-section or field-stitching data | stitching distortion | Optional GPU; code available |
| SLAT | alignment of heterogeneous slices through spatial-linked correspondence | heterogeneous spatial transcriptomics slices with expression and spatial structure | aligned heterogeneous slices and correspondence links | heterogeneous slice alignment | spatial-linked manifold alignment | heterogeneous slices | heterogeneity overfit | Optional GPU; code available |
| SPACEL | 3D slice alignment and tissue architecture stacking through the SPACEL framework | spatial transcriptomics slices with expression, coordinates, and optional image or architecture context | aligned 3D tissue architecture or stacked spatial map | 3D reconstruction | deep spatial architecture model | serial sections for 3D tissue context | model opacity and scale burden | Optional GPU; code available |
| STalign | coordinate-framework alignment through diffeomorphic metric mapping | spatial transcriptomics data with coordinates and optionally cross-technology spatial maps | diffeomorphic transform and aligned spatial coordinates | coordinate alignment | diffeomorphic mapping | cross-section or cross-technology spatial maps | geometry distortion | CPU; code available |
| STAligner | graph-attention integration across samples, conditions, technologies, and developmental stages | multiple spatial transcriptomics datasets across conditions, technologies, or stages | integrated embedding and aligned spatial domains | latent embedding integration | graph attention representation | cross-condition or cross-technology samples | biological signal removal | Optional GPU; code available |
| STAIR | end-to-end spatial transcriptomic alignment, integration, and 3D reconstruction | serial spatial transcriptomics sections for alignment, integration, and 3D reconstruction | aligned integrated sections and reconstructed 3D tissue map | 3D reconstruction | end-to-end 3D integration | serial sections for 3D reconstruction | model opacity and scale burden | Optional GPU; code available |
| MaskGraphene | interpretable joint representation for multi-slice and multi-condition integration | multi-slice and multi-condition spatial transcriptomics datasets | joint integrated representation with interpretability hooks | latent embedding integration | masked self-supervised graph representation | multi-slice and multi-condition samples | representation-objective ambiguity | Optional GPU; code available |
| spCLUE | contrastive unified analysis across single-slice and multi-slice data | single-slice and multi-slice spatial transcriptomics datasets | unified spatial representation for single-slice and multi-slice analysis | latent embedding integration | contrastive representation | single-slice and multi-slice samples | representation-objective ambiguity | Optional GPU; code available |
| VR-Omics | automated integration of multi-slice data in 2D and 3D | multi-slice spatial transcriptomics data for 2D or 3D integration | integrated 2D or 3D multi-slice spatial map | 2D/3D multi-slice integration | automated 2D/3D integration | multi-slice 2D or 3D data | automation opacity | Optional GPU; code available |
| MISO | multimodal spatial omics integration for resolving tissue complexity | multimodal spatial omics data from tissue sections | multimodal tissue-complexity model or integrated representation | multimodal modeling | multimodal spatial omics model | multimodal tissue sections | modality imbalance | Optional GPU; code available |
| Crescendo | count-level batch correction and cross-sample harmonization | single-cell spatial transcriptomics count data across batches or samples | batch-corrected count data or corrected representation for visualization and spatial gene pattern analysis | batch correction | batch-correction model | single-cell spatial count batches | biological signal removal | CPU; code available |
| SpaMosaic | integrate mosaic spatial multi-omics data while preserving spatial and cross-modality structure | spatial multi-omics datasets with partially observed modalities across samples or tissue sections | integrated spatial multi-omics representation and modality-completion or harmonized feature outputs | multimodal modeling | multimodal spatial omics model | mosaic spatial multi-omics samples | modality imbalance and cross-modality imputation bias | Optional GPU; code available |
| INSPIRE | integrate heterogeneous spatial transcriptomics datasets with interpretable spatially aware modeling | multiple spatial transcriptomics datasets from diverse sources with expression and spatial context | integrated representation and interpretable spatial factors or components for cross-dataset comparison | latent embedding integration | unclear | diverse-source spatial transcriptomics datasets | interpretability and representation-objective ambiguity | Optional GPU; code available |
| SpatialCOC | perform spatial continuous mapping and cross-omics correction for spatial multi-omics integration | spatial multi-omics data requiring continuous spatial mapping and cross-omics correction | cross-omics corrected representation and continuous spatial mapping outputs | multimodal modeling | multimodal spatial omics model | spatial cross-omics samples | cross-omics overcorrection | Optional GPU; code available |
| SSpMosaic | integrate and annotate single-cell and spatial omics data using interpretable gene programs | single-cell and spatial omics data with expression features suitable for interpretable gene-program modeling | integrated representation, gene-program factors, and annotation-supporting outputs | latent embedding integration | probabilistic embedding | single-cell and spatial omics pairing | annotation and gene-program boundary leakage | Optional GPU; code available |

## Decision Tree

If the deliverable is explicit coordinate alignment or slice correspondence:
- Prefer / consider `PASTE` for comparable slices, `PASTE2` for partial overlap, `STalign` for diffeomorphic coordinate mapping, `GPSA` for smooth non-rigid warping, `CAST` for high-resolution search-and-match correspondence, and `SLAT` for heterogeneous slice alignment.
- Keep geometry distortion, partial-overlap mismatch, and over-alignment of noncorresponding tissue visible.

If the deliverable is stitching, 3D reconstruction, or serial-section tissue assembly:
- Prefer / consider `SANTO`, `SPACEL`, `STAIR`, or `VR-Omics` according to whether the central cue is stitching, deep tissue architecture, end-to-end 3D reconstruction, or automated 2D/3D integration.
- Keep model opacity, scale burden, and reconstruction assumptions separate from ordinary batch correction.

If the deliverable is latent representation integration across samples, conditions, technologies, or slices:
- Prefer / consider `GraphST`, `PRECAST`, `STAligner`, `MaskGraphene`, `spCLUE`, or `INSPIRE`.
- Keep clustering, domain, and representation objectives distinct from explicit coordinate transforms.

If the deliverable is count-level or single-cell spatial batch correction:
- Prefer / consider `Crescendo`.
- Check whether biological condition signal may be removed with batch signal before using corrected output downstream.

If the deliverable is multimodal or mosaic spatial omics integration:
- Prefer / consider `MISO`, `SpaMosaic`, `SpatialCOC`, or `SSpMosaic` depending on whether the core cue is multimodal tissue modeling, missing-modality mosaic integration, cross-omics correction, or interpretable gene-program integration.
- Keep modality imbalance, cross-modality imputation bias, and annotation or program boundary leakage visible.

If no branch fits cleanly:
- Re-check whether the task is really Integration or whether the output belongs to Cell Type Inference, Domain / Clustering, Program Discovery, Spatial Contrast Testing, or another Layer 1 problem.
