# Gene Expression Prediction / Imputation

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Gene Expression Prediction / Imputation`.

This topic covers prediction, imputation, reconstruction, refinement, calibration, or completion of unmeasured or missing spatial gene-expression values. The main branch families here are histology-to-expression prediction, reference-assisted missing-gene or genome-wide imputation, cellular-resolution reconstruction, post-prediction calibration or refinement, and unmeasured-location prediction.

Use another Layer 1 problem first when the main task is same-grid denoising, super-resolution from a measured fine-geometry anchor, or cell type inference. Predicted or imputed expression remains model-derived signal rather than direct measurement, and branch selection should keep leakage, reference mismatch, morphology hallucination, and circular downstream validation visible.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Prediction Route | Input Dependence | Reference Dependence | Resolution Target | Uncertainty Handling | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GHIST | predict spatial gene expression at single-cell resolution from histology | histology images with paired training data or learned histology-expression mapping | predicted single-cell-resolution spatial gene expression | histology-to-expression prediction | histology-required | none or learned training pairs | single-cell or cellular-resolution inferred expression | not primary | Optional GPU; code available |
| Hist2ST | predict spot-level spatial transcriptomics from histology | histology image patches with spatial context and paired ST training data | predicted spatial transcriptomics expression profiles | histology-to-expression prediction | histology-required | none or learned training pairs | spatial expression prediction | not primary | Optional GPU; code available |
| THItoGene | predict spatial transcriptomics from histological images | histological images with learned histology-to-ST mapping | predicted spatial transcriptomics expression | histology-to-expression prediction | histology-required | none or learned training pairs | spatial expression prediction | not primary | Optional GPU; code available |
| FmH2ST | generate spatial transcriptomics from histological images using foundation-model features | histology images and foundation-model visual features | generated or predicted spatial transcriptomics expression | histology-to-expression generation | histology-required | none or learned training pairs | spatial expression prediction | not primary | Optional GPU; code available |
| OmiCLIP | bridge histopathology with spatial transcriptomics for image-to-expression prediction and related retrieval tasks | histopathology images with visual-omics representation learning context | predicted or aligned spatial omics/expression representation | visual-omics prediction | histology-required | none or learned training pairs | spatial expression prediction | not primary | Optional GPU; code available |
| SpaGE | enhance spatial expression by predicting genes from a shared latent space with scRNA-seq | measured spatial expression for shared genes plus scRNA-seq reference | enhanced or imputed spatial expression for unmeasured genes | reference-assisted missing-gene imputation | reference-required | scRNA/reference-dependent | genome-wide or missing-gene expression | not primary | CPU; code available |
| stPlus | enhance spatial transcriptomics and predict genes using scRNA-seq information | spatial transcriptomics matrix plus single-cell reference | enhanced spatial expression with predicted missing genes | reference-assisted expression enhancement | reference-required | scRNA/reference-dependent | genome-wide or missing-gene expression | not primary | CPU; code available |
| SpatialScope | reconstruct transcriptome-wide spatial expression at cellular resolution | spatial transcriptomics data plus single-cell reference | cellular-resolution inferred transcriptomic reconstruction | cellular-resolution transcriptomic reconstruction | reference-required | scRNA/reference-dependent | single-cell or cellular-resolution inferred expression | not primary | Optional GPU; code available |
| STASCAN | predict fine-resolution spatial cellular distribution in captured or uncharted areas | spatial gene expression profiles plus histology images | fine-resolution cell distribution or spatial completion map | multimodal spatial completion | measured-ST-and-context-required | unclear | single-cell or cellular-resolution inferred expression | not primary | Optional GPU; code available |
| stAI | impute missing genes in single-cell spatial transcriptomics with coupled cell-type annotation | single-cell spatial transcriptomics with missing genes and annotation context | imputed missing genes and cell-type annotations | missing-gene imputation and annotation | measured-ST-and-context-required | unclear | genome-wide or missing-gene expression | not primary | Optional GPU; code available |
| TISSUE | calibrate uncertainty around spatial gene-expression predictions and support uncertainty-aware downstream use | predicted spatial expression values with calibration context from measured spatial data | prediction intervals and uncertainty-aware expression-prediction summaries | uncertainty calibration | prediction-input-required | baseline-prediction-dependent | spatial expression prediction | explicit calibration | CPU; code available |
| ENGEP | ensemble reference-assisted model predicts unmeasured spatial gene expression | spatial query expression matrix plus same- or similar-tissue sc/snRNA-seq references | predicted expression levels for spatially unmeasured genes | ensemble reference-assisted missing-gene prediction | reference-required | scRNA/reference-dependent | genome-wide or missing-gene expression | not primary | CPU; code available |
| iSpatial | reference-assisted model infers transcriptome-wide spatial expression values | limited-gene spatial transcriptomics or FISH data plus scRNA-seq reference | genome-wide inferred spatial expression | genome-wide spatial expression inference | reference-required | scRNA/reference-dependent | genome-wide or missing-gene expression | not primary | CPU; code available |
| stDiff | diffusion model performs reference-assisted missing gene expression imputation | measured/shared spatial genes plus reference single-cell transcriptomics | imputed missing spatial expression and enhanced ST data | diffusion-model missing-gene imputation | reference-required | scRNA/reference-dependent | genome-wide or missing-gene expression | not primary | Optional GPU; code available |
| SPRITE | post-processing/meta-algorithm improves imputed or predicted spatial expression values | baseline spatial expression predictions plus gene and cell networks | refined predicted spatial expression for target genes | prediction post-processing / refinement | prediction-input-required | baseline-prediction-dependent | genome-wide or missing-gene expression | post-prediction refinement | CPU; code available |
| DIST | deep model predicts spatial expression values at unmeasured locations and enhances measured spots | array-based spatial transcriptomics expression maps and spatial layout | imputed expression at unmeasured locations and enhanced expression profiles | unmeasured-location expression imputation | measured-ST-and-context-required | unclear | unmeasured-location expression | not primary | Optional GPU; code available |
| STGAT | graph-attention model predicts expression from histology and bulk RNA context; exclude same-name deconvolution paper | training ST data with spot image/coordinates/expression plus target WSI and bulk RNA-seq | spot-level predicted gene-expression profiles and tissue labels | histology and bulk-assisted expression prediction | histology-required | bulk-RNA-and-ST-training-dependent | spatial expression prediction | not primary | Optional GPU; code available |

## Decision Tree

If histology or WSI-derived signal is the main driver of expression prediction:
- Prefer / consider `GHIST`, `Hist2ST`, `THItoGene`, `FmH2ST`, `OmiCLIP`, or `STGAT`.
- Keep the branch focused on predicted expression from morphology-linked inputs rather than same-grid denoising or direct measurement claims.

If the main goal is missing-gene or genome-wide imputation from measured spatial signal plus a reference:
- Prefer / consider `SpaGE`, `stPlus`, `ENGEP`, `iSpatial`, or `stDiff`.
- Keep reference dependence explicit and review tissue match before treating imputed genes as downstream evidence.

If the main goal is cellular-resolution or high-resolution transcriptomic reconstruction:
- Prefer / consider `SpatialScope`, `stAI`, or `STASCAN`.
- Keep reconstruction, annotation coupling, and fine-resolution completion distinct from ordinary spot-level proportion estimation or direct single-cell truth.

If predictions already exist and the branch question is calibration or refinement:
- Prefer / consider `TISSUE` for uncertainty-aware calibration.
- Prefer / consider `SPRITE` for post-prediction refinement using gene or cell-network context.
- Do not treat calibration or refinement rows as first-pass generators of expression values.

If the stated endpoint is expression prediction at unmeasured locations rather than missing genes within measured locations:
- Prefer / consider `DIST`.
- Re-check whether the requested output is an imputed expression surface rather than super-resolution or segmentation.

After choosing the branch:
- Keep predicted or imputed expression separate from direct measurement in downstream interpretation.
- Keep leakage, reference mismatch, morphology hallucination, and circular validation caveats in the reading path rather than as negative table columns.
- Do not force one cross-branch ordering across histology, reference-assisted, reconstruction, calibration, and unmeasured-location families.
