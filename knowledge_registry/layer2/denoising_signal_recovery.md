# Denoising / Signal Recovery

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Denoising / Signal Recovery`.

This topic covers same-resolution recovery of noisy, sparse, or locally degraded measured spatial expression. The target output stays on the measured spot, cell, or coordinate grid rather than creating finer geometry or claiming new unmeasured expression.

Use another Layer 1 problem first when the requested output is unmeasured-gene prediction, histology-to-expression prediction, or super-resolution. Recovered, smoothed, or reconstructed values remain model-processed signals rather than new direct measurements.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Correction Target | Reference Dependence | Spatial Signal Use | Image Signal Use | Output Alteration Level | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MIST | region-specific missing-value imputation and denoising | target-sample measured spatial transcriptomics matrix with region context | same-resolution denoised or imputed expression matrix | same-resolution expression signal | none or optional local graph/prior | required | not primary | same-grid expression recovery | CPU; code available |
| SpotGF | denoising through spatially informed gene filtering | target-sample measured spatial transcriptomics expression matrix | filtered/denoised gene set or expression signal | gene filtering / expression signal | none or optional local graph/prior | optional | not primary | feature/gene filtering and signal cleanup | CPU; code available |
| Sprod | image- and position-informed denoising/imputation | target-sample measured ST with positions and image information | same-resolution denoised spatial expression values | same-resolution expression signal | none or optional local graph/prior | required | used | same-grid expression recovery | CPU; code available |
| DiffusionST | deep generative enhancement and denoising for ST quality improvement | target-sample measured ST matrix with spatial context | denoised spatial transcriptomics expression at the existing spots | same-resolution expression signal | none or optional local graph/prior | required | not primary | same-grid expression recovery | Optional GPU; code available |
| stGRL | graph contrastive denoising and imputation coupled to spatial-domain representation | target-sample measured ST with spatial graph/context | denoised or recovered expression representation at the same grid | same-resolution expression signal | none or optional local graph/prior | required | not primary | same-grid expression recovery | Optional GPU; code available |
| GNTD | graph-guided tensor decomposition recovers same-resolution measured-coordinate ST signal | spatial gene expression tensor plus spatial spot graph and optional gene functional graph | imputed/reconstructed spatial expression tensor for measured coordinates | same-resolution expression signal | none or optional local graph/prior | required | not primary | same-grid expression recovery | Optional GPU; code available |
| SPCS | spatial and pattern smoothing recovers same-resolution expression signal | ST expression matrix plus spot positions and expression-pattern neighborhoods | smoothed ST expression values and optional existing-grid blank-spot padding | same-resolution expression signal | none or optional local graph/prior | required | not primary | same-grid expression recovery | CPU; code available |

## Decision Tree

If the output must stay on the measured spot, cell, or coordinate grid:
- Continue within this topic.

If the branch is region-aware denoising from spatial-expression structure:
- Prefer / consider `MIST`.

If the branch is gene filtering or signal cleanup rather than full value recovery:
- Prefer / consider `SpotGF`.

If image or position information is an explicit denoising signal:
- Prefer / consider `Sprod`.

If graph or diffusion-style denoising is the main modeling branch:
- Prefer / consider `DiffusionST` for generative diffusion enhancement.
- Prefer / consider `stGRL` when joint graph representation and domain-aware recovery are desired.

If tensor or spatial-pattern reconstruction is the main modeling branch:
- Prefer / consider `GNTD` for graph-guided tensor decomposition.
- Prefer / consider `SPCS` for spatial-and-pattern smoothing on the existing grid.

After choosing the branch:
- Route to `Gene Expression Prediction / Imputation` when the output is unmeasured-gene or reference-derived expression prediction.
- Route to `Super-resolution` when the output is finer-geometry reconstruction.
- Keep denoised output framed as processed recovery signal, not direct truth about newly measured biology.
