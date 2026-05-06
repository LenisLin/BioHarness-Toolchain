# Super-resolution

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Super-resolution`.

This topic covers finer-geometry reconstruction, enhanced-resolution representation, generated high-density profiles, and measured high-density or submicron representation when the output remains anchored to target-sample measured spatial expression or spatial omics. Keep measured-versus-inferred status explicit: `FICTURE` stays on the measured high-density or submicron representation side, not the generated-upsampling side.

Use another Layer 1 problem first when the output is unmeasured expression predicted without a target-sample measured spatial anchor, same-grid denoising or recovery, direct cell segmentation, or cell type labeling. Pseudo-cell, single-cell-resolution, high-density, or cell-level outputs in this topic remain inferred reconstructions unless the input already contains measured fine-geometry signal.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Resolution Target | Image Signal Use | External Reference Dependence | Output Geometry | Cellular Reconstruction Mode | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FICTURE | segmentation-free analysis of already fine-geometry spatial transcriptomics for factor-level representation | target-sample measured submicron or high-density spatial transcriptomics data | segmentation-free fine-scale spatial factor and tissue-feature maps | measured high-density/factor representation | none | reference-free | factor map | not primary | CPU; code available |
| iStar | histology-guided inference of super-resolution tissue architecture | target-sample spot-based spatial transcriptomics with matched histology | super-resolved tissue architecture and inferred fine-resolution expression map | tissue architecture inference | required | reference-free | high-resolution tissue map | histology-guided architecture inference | Optional GPU; code available |
| scstGCN | single-cell-resolution spatial gene-expression inference from fused expression, location, and image signals | target-sample spot-based ST, spatial coordinates, and histology image | inferred single-cell-resolution spatial gene-expression map | single-cell-resolution expression | required | reference-free | single-cell-resolution expression map | graph/image fusion | Optional GPU; code available |
| Spotiphy | single-cell spatial whole-transcriptome reconstruction across an entire tissue section | target-sample section-level spatial transcriptomics with image/context features | pseudo-single-cell whole-transcriptome spatial map | pseudo-single-cell whole transcriptome | required | unclear | pseudo-single-cell whole-section map | pseudo-single-cell reconstruction | Optional GPU; code available |
| TESLA | super-resolution reconstruction for tumor ecosystem analysis | target-sample spatial transcriptomics with histology image | super-resolved spatial expression and tissue-ecosystem maps | tumor ecosystem super-resolution | required | reference-free | histology-guided super-resolution map | histology-guided reconstruction | Optional GPU; code available |
| XFuse | deep-learning fusion of image and expression data for super-resolved spatial transcriptomics | target-sample spatial transcriptomics with matched histology | super-resolved spatial expression map | super-resolved expression | required | reference-free | super-resolved expression grid | deep image-expression fusion | Optional GPU; code available |
| ImSpiRE | image feature-aided subspot resolution enhancement and imputation of unmeasured tissue regions | target-sample spatial transcriptomics with histology image features | image-aided enhanced-resolution spatial expression map | subspot resolution enhancement | required | reference-free | subspot transcriptional profile | image-feature-aided optimal transport | CPU; code available |
| soScope | cross-platform generative enhancement of spatial omics profiles to subspot or enhanced spatial resolution | target-sample spatial omics data with cross-platform enhancement context | enhanced-resolution tissue characterization or expression representation | cross-platform enhanced-resolution omics | required | unclear | enhanced-resolution spatial omics profile | generative spatial omics enhancement | Optional GPU; code available |
| iSCALE | cellular-level tissue-architecture reconstruction beyond conventional platform resolution at large tissue scale | large-area target-sample spatial transcriptomics with tissue architecture context | cellular-level inferred tissue architecture and reconstructed expression map | large-area cellular architecture | unclear | unclear | large-area cellular-level map | large-area reconstruction | Optional GPU; code available |
| STAGE | generation of high-density spatial transcriptomics from lower-density spatial inputs | sparse target-sample spatial transcriptomics inputs | generated high-density spatial transcriptomics profiles | high-density ST generation | unclear | unclear | generated high-density ST profile | high-density generation | Optional GPU; code available |
| Thor | support cell-level investigation by reconstructing or analyzing spatial transcriptomics together with histology | target-sample spatial transcriptomics with matched histology | histology-aware cell-level spatial transcriptomics representation | large-area cellular architecture | required | unclear | large-area cellular-level map | histology-guided reconstruction | Optional GPU; code available |

## Decision Tree

If the task lacks target-sample measured spatial expression or spatial-omics anchoring for the requested output:
- Route to `Gene Expression Prediction / Imputation` rather than `Super-resolution`.

If the input already contains measured submicron or high-density spatial signal and the goal is segmentation-free fine-scale representation:
- Prefer / consider `FICTURE`.
- Keep its output framed as measured high-density factor or tissue-feature representation rather than generated subspot upsampling.

If matched histology is central to reconstructing finer geometry from lower-resolution target-sample data:
- Prefer / consider `iStar` for histology-guided tissue-architecture inference.
- Prefer / consider `TESLA` when tumor-ecosystem interpretation is central.
- Prefer / consider `XFuse` for deep image-expression fusion.
- Prefer / consider `ImSpiRE` for image-feature-aided subspot enhancement and redistribution.

If the requested output is inferred single-cell-resolution or pseudo-cell reconstruction from target-sample data:
- Prefer / consider `scstGCN` for graph-plus-image single-cell-resolution expression inference.
- Prefer / consider `Spotiphy` for pseudo-single-cell whole-section reconstruction.
- Prefer / consider `Thor` when histology-aware cell-level investigation is the intended framing.

If large tissue area or generated higher-density representation is central:
- Prefer / consider `iSCALE` for large-area cellular-level reconstruction.
- Prefer / consider `STAGE` for generated high-density spatial transcriptomics profiles.
- Prefer / consider `soScope` when cross-platform enhanced-resolution spatial omics framing is central.

After choosing a branch:
- Keep measured versus inferred outputs explicit in downstream interpretation.
- Do not describe pseudo-cell, single-cell-resolution, high-density inferred, or cell-level inferred outputs as direct molecule-level single-cell measurements.
- Route back to `Segmentation` or `Cell Type Inference` when those become the primary endpoint rather than adjacent downstream interpretation.
