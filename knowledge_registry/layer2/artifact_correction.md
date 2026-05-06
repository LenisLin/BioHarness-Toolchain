# Artifact Correction

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Artifact Correction`.

This topic covers artifact-mechanism-specific correction of already measured spatial signal, including spot swapping or local contamination, vignetting or intensity-field distortion, molecular admixture after assignment, and Xenium-specific signal contamination or transcript spillover.

Use another Layer 1 problem first when the requested output is quality-control flagging, segmentation, same-grid denoising, unmeasured-gene prediction, or super-resolution. Treat corrected output as model-processed signal rather than direct proof of ground-truth biology.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Artifact Mechanism | Data Object | Platform Scope | Correction Scope | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SpotClean | correct spot swapping or local contamination effects in spot-based spatial transcriptomics | spot-level spatial transcriptomics count data with spatial neighborhood structure | artifact-corrected expression estimates and contamination-aware summaries | spot swapping / local contamination | spot-level count matrix with spatial coordinates | spot-based spatial transcriptomics | expression correction / contamination adjustment | CPU; code available |
| Non-parametric Vignetting Correction | correct non-uniform vignetting or position-dependent signal attenuation | spatial transcriptomics image or sparse spatial signal affected by position-dependent intensity attenuation | vignetting-corrected spatial signal or expression-like matrix | vignetting / position-dependent intensity field | image or sparse spatial signal | platforms with measurable vignetting/intensity-field artifact | spatial intensity-field correction | CPU; code available |
| cellAdmix | correct molecular admixture effects after cell/molecule assignment | cell-level or molecule-assigned spatial transcriptomics data with suspected admixture across neighboring cells or compartments | admixture-adjusted expression estimates or corrected cell-level signals | molecular admixture | cell-level or molecule-assigned spatial expression data | cell-level or molecule-resolved spatial assays | molecular admixture adjustment | CPU; code available |
| SPLIT | correct Xenium-specific signal contamination and transcript spillover effects | Xenium spatial transcriptomics transcript calls or expression matrix with spatial molecule context | contamination-aware Xenium expression estimates, transcript-spillover diagnostics, or corrected downstream-ready signal | Xenium signal contamination / transcript spillover | Xenium transcript calls or expression object | Xenium-specific | signal-contamination correction | CPU; code available |

## Decision Tree

If the suspected artifact is spot swapping or local contamination in a spot-level count matrix:
- Prefer / consider `SpotClean`.

If the suspected artifact is vignetting or position-dependent intensity attenuation in an image-linked or sparse spatial signal:
- Prefer / consider `Non-parametric Vignetting Correction`.

If the suspected artifact is molecular admixture across assigned cells or compartments:
- Prefer / consider `cellAdmix`.

If the platform is Xenium and the suspected artifact is signal contamination or transcript spillover:
- Prefer / consider `SPLIT`.

After identifying the mechanism:
- Keep the method aligned with the data object and platform scope rather than forcing a cross-branch comparison.
- Route to `Data Quality Control` when the task is artifact flagging or review rather than signal correction.
- Review corrected output against morphology, platform metadata, and known tissue structure before treating changes as biological signal.
