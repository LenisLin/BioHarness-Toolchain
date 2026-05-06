# Panel Design

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Panel Design`.

This topic covers pre-assay targeted spatial transcriptomics panel or probe-set selection. The deliverable is an assay-design output such as a selected gene panel or probe set, not proof of spatially variable expression, causal marker status, or post-capture biological truth.

Use another Layer 1 problem first when the task is normalization, denoising, expression prediction, super-resolution, or downstream communication analysis.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Panel Design Branch | Reference or Label Dependence | Targeted Assay Constraint | Output Object | Evidence Status | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scGIST | select genes for targeted spatial transcriptomics panels with prioritized biological or technical gene sets | Single-cell expression data, cell labels or cell-type structure, prioritized gene sets, and target panel size | selected gene panel for targeted spatial transcriptomics assays | prioritized gene-set panel design | single-cell reference / labels used | required | selected gene panel | peer-reviewed method paper | CPU; code available |
| gpsFISH | select informative gene panels for targeted spatial transcriptomics experiments | single-cell or spatial reference expression data, candidate genes, and targeted spatial assay constraints | selected gene panel for targeted spatial transcriptomics assays | targeted spatial gene-panel selection | reference expression required | required | selected gene panel | peer-reviewed method paper | CPU; code available |
| Spapros | select probe sets for targeted spatial transcriptomics experiments | single-cell or spatial reference data, marker constraints, target cell types, and panel-size constraints | selected probe set or gene panel for targeted spatial transcriptomics assays | targeted probe-set selection | reference and target labels or constraints used | required | selected probe set / gene panel | peer-reviewed method paper | CPU; code available |
| PERSIST | select compact predictive gene panels for spatial transcriptomics | training expression data and spatial transcriptomics prediction or selection objective | small predictive gene panel for spatial transcriptomics | predictive robust gene selection | training data / selection objective dependent | required | small gene panel | peer-reviewed method paper | CPU; code available |
| ReconST | select an optimal gene panel for targeted spatial transcriptomics experiments | reference expression data and target spatial transcriptomics experiment constraints | selected gene panel for targeted spatial transcriptomics experiments | optimal gene-panel selection | reference and experiment-design dependent | required | selected gene panel | preprint / watchlist positive | CPU; code access unclear |

## Decision Tree

If prioritized gene sets, cell-type structure, and fixed panel size are central:
- Prefer / consider `scGIST`.

If the task is direct targeted spatial transcriptomics gene-panel selection from reference data and assay constraints:
- Prefer / consider `gpsFISH`.

If probe-set selection with target cell types, marker constraints, or panel-size constraints is central:
- Prefer / consider `Spapros`.

If the selection objective is predictive robustness for a compact panel:
- Prefer / consider `PERSIST`, while keeping prediction as the internal selection objective rather than the output object.

If preprint-level evidence and unclear code trace are acceptable and explicitly recorded:
- Consider `ReconST`.

Across these branches:
- Treat selected panels as assay-design outputs rather than proof of spatially variable genes or causal markers.
- Treat `ReconST` wording about an "optimal" panel or positive watchlist status as provisional preprint-era framing rather than a settled superiority claim.
- Treat predictive or reconstruction wording as panel-evaluation logic, not expression-map reconstruction, super-resolution, or gene-expression prediction output.
