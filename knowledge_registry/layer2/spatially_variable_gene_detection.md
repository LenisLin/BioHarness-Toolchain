# Spatially Variable Gene Detection

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Spatially Variable Gene Detection`.

This topic covers gene-level spatial variability tasks, including overall SVG detection, cell-type-specific SVG detection, cell-type-conditional spatial correlation, gene-centric tissue-pattern mining, and cell-type-adjusted SVG clustering or feature selection. These branches are not interchangeable, and their outputs should not be flattened into one generic SVG ranking problem.

Use another Layer 1 problem first when the requested output is normalization, denoising, imputation, domain clustering without a gene-level SVG question, cell type inference, communication analysis, or trajectory analysis. Keep branch-local benchmark guidance inside the relevant branch rather than turning it into a cross-branch or all-method ranking.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | SVG Branch | Cell-Type Context | Primary Statistical Output | Spatial Pattern Scale | Benchmark Coverage | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Celina | cell-type-specific SVG detection | spatial expression matrix + spatial coordinates + cell type composition or labels | cell-type-specific SVG calls and statistics | cell-type-specific SVG detection | cell-type-specific | ctSVG calls / p-values | cell-type-resolved | branch benchmark retrieved | CPU; code available |
| ctSVG | cell-type-specific SVG detection | spatial expression matrix + spatial coordinates + cell type composition or labels | cell-type-specific SVG calls and significance statistics | cell-type-specific SVG detection | cell-type-specific | ctSVG calls / p-values | cell-type-resolved | branch benchmark retrieved | CPU; code access unclear |
| STANCE | cell-type-specific SVG detection with unified modeling | spatial expression matrix + spatial coordinates + cell type composition or labels | cell-type-specific SVG calls and statistics | cell-type-specific SVG detection | cell-type-specific | ctSVG calls / p-values | cell-type-resolved | branch benchmark retrieved | CPU; code available |
| STMiner | gene-centric tissue-pattern mining rather than classical hypothesis-test SVG calling | spatial expression matrix + spatial coordinates, typically tissue-scale tumor spatial data | gene-level spatial tissue patterns and interpretable pattern summaries | gene-centric tissue pattern mining | none | gene pattern summaries | tissue-pattern | method-paper only | CPU; code available |
| BSP | overall SVG detection with dimension-agnostic granularity testing | spatial expression matrix + spatial coordinates | ranked SVGs and statistical evidence | overall SVG detection | none | ranked genes / p-values | multi-scale / granularity | review-screened only | CPU; code available |
| HEARTSVG | fast overall SVG detection for large-scale spatial transcriptomics | large-scale spatial expression matrix + spatial coordinates | ranked SVGs and statistical evidence | overall SVG detection | none | ranked genes / p-values | global / overall | method-paper only | CPU; code access unclear |
| nnSVG | scalable overall SVG detection with nearest-neighbor Gaussian-process approximation | spatial expression matrix + spatial coordinates | ranked SVGs and statistical evidence | overall SVG detection | none | ranked genes / p-values | local / nearest-neighbor | broad benchmark retrieved | CPU; code available |
| SOMDE | overall SVG detection after self-organizing-map compression | spatial expression matrix + spatial coordinates | ranked SVGs and statistical evidence | overall SVG detection | none | ranked genes / p-values | global / overall | review-screened only | CPU; code available |
| SPARK | overall SVG detection with count-aware spatial modeling | spatial count matrix + spatial coordinates | ranked SVGs and calibrated test statistics when assumptions hold | overall SVG detection | none | ranked genes / p-values | global / overall | broad benchmark retrieved | CPU; code available |
| SPARK-X | scalable and robust overall SVG detection | large spatial expression matrix + spatial coordinates | ranked SVGs and statistical evidence | overall SVG detection | none | ranked genes / p-values | global / overall | broad benchmark retrieved | CPU; code available |
| SpatialDE | canonical overall SVG detection baseline | spatial expression matrix + spatial coordinates | ranked SVGs and spatial expression pattern statistics | overall SVG detection | none | ranked genes / p-values | global / overall | broad benchmark retrieved | CPU; code available |
| spVC | detection and interpretation of spatial gene expression variation | spatial expression matrix + spatial coordinates, with cell-type-aware interpretation when applicable | spatial variation coefficients and gene-level variation evidence | overall SVG detection | unclear | variation coefficients | global / overall | branch benchmark retrieved | CPU; code access unclear |
| InSituCor | finding spatially correlated genes conditional on cell type landscape | spatial expression matrix + spatial coordinates + cell type landscape | cell-type-conditional spatial correlation gene sets | cell-type-conditional SVG detection | cell-type-conditional | conditional correlation calls | cell-type-resolved | method-paper only | CPU; code access unclear |
| SPACE-SVG | SVG clustering adjusted for cell type effect and downstream domain-supporting feature selection | spatial expression matrix + spatial coordinates + cell type effect estimates | cell-type-adjusted SVG clusters / selected spatial features | SVG clustering / feature selection | cell-type-adjusted | SVG clusters / selected features | cell-type-resolved | method-paper only | CPU; code access unclear |

## Decision Tree

If the intended output is cell-type-specific SVG calls:
- Prefer / consider `Celina`, `STANCE`, or `ctSVG`.
- Keep cell type context, false-positive control, and non-target-cell leakage caveats visible.

If the intended output is spatial gene correlation conditional on the cell type landscape:
- Prefer / consider `InSituCor`.
- Do not substitute it for direct ctSVG calling or overall SVG ranking.

If cell type effects should be adjusted while clustering or selecting SVGs:
- Prefer / consider `SPACE-SVG`.
- Keep its boundary with feature selection and domain-support workflows visible.

If the real deliverable is gene-centric tissue-pattern interpretation rather than conventional calibrated SVG testing:
- Prefer / consider `STMiner`.

If the task is overall SVG detection with large-data or scalability pressure:
- Prefer / consider `SPARK-X`, `nnSVG`, or `HEARTSVG`.
- Use broad benchmark guidance only inside this overall-SVG branch, not as a universal default rule.

If the task is overall SVG detection without a strict scalability-first requirement:
- Prefer / consider `SpatialDE` for a canonical Gaussian-process baseline.
- Prefer / consider `SPARK` for count-aware spatial modeling on moderate data.
- Prefer / consider `BSP` for a non-parametric or granularity-oriented route.
- Prefer / consider `SOMDE` when self-organizing-map compression is scientifically attractive.
- Prefer / consider `spVC` when interpretable spatial variation coefficients are central, while keeping its branch-boundary caveat visible.

After choosing a branch:
- Keep benchmark comparisons branch-local.
- Keep caveats about cell type context, calibration, compression, and boundary interpretation in the reading path rather than encoding them as exclusionary table columns.
