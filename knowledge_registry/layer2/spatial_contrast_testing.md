# Spatial Contrast Testing

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Spatial Contrast Testing`.

This topic covers explicit contrasts across condition, group, niche, domain, anatomical template, or covariate design when the target output is a spatially aware contrast statistic, effect estimate, differential spatial feature, or pattern-comparison result. Do not mix direct contrast testing with phenotype association, cohort-linked niche prioritization, or within-sample spatially variable gene detection.

Use another Layer 1 problem first when the requested endpoint is phenotype-linked association without a direct contrast, generic SVG ranking within one sample, registration or integration, deconvolution, or niche discovery. Registration, niche definition, deconvolution, and spatial-autocorrelation choices can create false positives and must remain visible in branch selection.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Required Contrast Signal | Main Contrast Output | Estimand Class | Spatial Structure Requirement | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-SIDE | testing cell-type-specific expression changes across explicit condition or covariate contrasts | ST count matrix + spatial coordinates + cell type weights or reference-informed assignments + condition/covariate design | cell-type-specific DE genes and effect estimates | condition/covariate plus cell-type weights | cell-type-specific DE genes and effect estimates | cell-type-specific condition contrast | cell type mixture / reference-informed | CPU; code available |
| Niche-DE | testing expression changes conditioned on local niche or neighborhood definitions | ST or spatial single-cell expression + spatial coordinates + cell or spot annotations + niche/context variables | niche-differential genes and context-dependent interaction signals | condition/covariate within niches | niche-differential genes and context-conditioned signals | niche-conditioned condition contrast | neighborhood/niche definitions | CPU; code available |
| SPADE | testing between-group spatial expression patterns and differential expression without requiring registration | ST expression matrix + spatial coordinates + group or condition labels | spatial pattern statistics and differentially expressed or differentially patterned genes | group or condition labels | spatial pattern statistics and differentially expressed or patterned genes | between-group spatial expression/pattern contrast | coordinates / pattern; registration not central | CPU; code available |
| SpatialGEE | testing condition or covariate effects with spatial-correlation-aware statistical modeling | ST expression matrix + spatial coordinates + condition/covariate design | DE genes, statistical tests, and model-based effect estimates | condition/covariate design | DE genes, statistical tests, and model-based effect estimates | spatial-correlation-aware condition contrast | spatial correlation model | CPU; code available |
| STcompare | comparing differential spatial patterning across structurally matched tissues | structurally matched ST datasets + expression matrices + spatial coordinates | differentially spatially patterned genes and tissue-pattern comparison results | structurally matched tissue comparison | differentially spatially patterned genes and tissue-pattern comparison results | matched-tissue spatial pattern contrast | structural comparability required | CPU; code available |
| SpatialSPM | performing pixel-wise statistical testing on registered spatial gene-expression pattern images | multiple ST datasets + expression matrices + spatial coordinates + anatomical or template registration workflow | registered expression images, statistical parametric maps, T-scores, and correlation maps | registered multi-sample or template design | registered expression images, statistical parametric maps, T-scores, and correlation maps | registered pixel-wise pattern contrast | registration/template required | CPU; code available |

## Decision Tree

If the explicit contrast is cell-type-specific expression change:
- Prefer / consider `C-SIDE` when reliable cell type weights or reference-informed assignments support the design.
- Review reference mismatch and composition-condition confounding before interpreting effects.

If the explicit contrast is niche- or local-context-conditioned expression:
- Prefer / consider `Niche-DE`.
- Review niche construction and annotation stability before interpreting context-conditioned effects.

If the explicit contrast is between-group spatial expression or pattern differences without requiring registration:
- Prefer / consider `SPADE`.
- Keep spatial autocorrelation, sampling density, and tissue-resolution differences visible.

If the explicit contrast is a spatial-correlation-aware condition or covariate model:
- Prefer / consider `SpatialGEE`.
- Treat benchmark support as branch-local, not as a global default.

If the explicit contrast is differentially spatially patterned genes in structurally matched tissues:
- Consider `STcompare` with a preprint confidence caveat.
- Do not turn preprint status into a hard exclusion when structural comparability is the real branch-fit condition.

If the explicit contrast is registered pixel-wise pattern testing on comparable tissue images or templates:
- Prefer / consider `SpatialSPM`.
- Keep registration, smoothing, and template choices visible as possible false-positive sources.

If the task asks for phenotype association, cohort niche prioritization, within-sample SVG detection, or preprocessing:
- Route to the matching Layer 1 problem before choosing a contrast-testing method.
