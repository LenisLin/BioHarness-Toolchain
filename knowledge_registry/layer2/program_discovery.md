# Program Discovery

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Program Discovery`.

This topic covers latent tissue-state, multicellular-program, topic, factor, gradient, co-expression, gene-set-correlation, regulatory-program-style, and tissue-module discovery outputs from spatial transcriptomics. These outputs are interpretation-oriented summaries and should not be described as direct mechanism discovery, direct regulatory proof, or a separate standalone GRN analysis problem.

Use another Layer 1 problem first when the requested output is domain clustering alone, cell type inference, communication analysis, trajectory analysis, or perturbation response. Keep branch heterogeneity explicit so factor, topic, network, regulatory-program, and tissue-module outputs are not flattened into one ranking problem.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Program Family | Program Output Type | Spatial Coupling | Reference Dependence | Multi-sample Cue | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CellPie | scalable factor discovery for spatially organized multicellular programs | spatial transcriptomics count matrix + spatial coordinates, potentially multiple samples | non-negative factors/program loadings + sample/spot/cell scores | factor / NMF | factors and program scores | spatial factor structure | reference-free | suited when cross-sample factor structure matters | CPU; code pending/manual review |
| DIALOGUE | mapping coordinated multicellular programs in tissue | single-cell or spatial transcriptomics data with cell-type/context annotations | multicellular program scores and coordinated gene programs across cell types | multicellular latent program | cell-type-coordinated programs | tissue/context-aware, not purely coordinate-first | annotation-dependent | can support cohort or condition program comparison when annotations are harmonized | CPU; code available |
| scITD | discovering interpretable multicellular programs that stratify patient or sample cohorts | multi-sample single-cell or spatial transcriptomics tensors with cell-type and sample axes | tensor components linking genes, cell types, and samples/cohorts | tensor decomposition | tensor components / cohort programs | indirect through cell/state/sample structure | annotation-dependent | strong; cohort/sample axis is central | CPU; code available |
| SPICEMIX | integrative factor modeling of spatial cell identity and latent tissue programs | spatial transcriptomics with optional single-cell reference or identity cues | latent factors, cell-identity mixtures, and spatially organized state estimates | probabilistic latent variable | latent identity/program factors | explicit spatial mixture modeling | optional/reference-informed | unclear | CPU; code available |
| STAMP | spatial topic and gene-module discovery | spatial transcriptomics count matrix + spatial coordinates | spatial topics, topic proportions, and associated gene modules | spatial topic model | topics and gene modules | explicit coordinate-aware topic structure | reference-free | unclear | Optional GPU; code available |
| SpaTM | inferring spatially informed transcriptional programs with topic models | spatial transcriptomics count matrix + spatial coordinates | spatial topics / transcriptional programs with gene weights | spatial topic model | topics / transcriptional programs | explicit spatially informed topics | reference-free | unclear | CPU; code pending/manual review |
| FISHFactor | probabilistic factor discovery for subcellular spatial transcriptomics | subcellular-resolution spatial transcriptomics molecule/count data | spatial factors and factor loadings at subcellular resolution | probabilistic spatial factor | subcellular factors | subcellular spatial factor model | reference-free | unclear | CPU; code pending/manual review |
| SpatialCorr | detecting gene sets with spatially varying correlation / co-program structure | spatial transcriptomics expression + spatial coordinates + user-defined gene sets | gene-set correlation statistics and spatially varying co-program calls | gene-set correlation | spatially varying gene-set correlations | explicit spatially varying correlation | gene-set-dependent | unclear | CPU; code pending/manual review |
| SpaceX | estimating spatial co-expression networks for coordinated module discovery | spatial transcriptomics expression + spatial coordinates | spatial gene co-expression network estimates | spatial co-expression network | co-expression network / modules | explicit spatial network model | reference-free | unclear | CPU; code pending/manual review |
| SpaGRN | boundary-sensitive spatial regulatory-program annotation and scoring | spatial transcriptomics expression + spatial coordinates, with regulatory motif/network priors as applicable | spatial regulatory-program-style annotations and scores | boundary-sensitive regulatory-program output | regulatory-program-style annotations / scores | spatially informed regulatory-program annotations | regulatory-prior-dependent | unclear | CPU; code pending/manual review |
| SPACE | interaction-aware tissue module discovery | single-cell-resolution spatial transcriptomics expression + spatial cell-cell context | cell embeddings and tissue modules shaped by cell-cell interactions | interaction-aware tissue module | tissue modules / interaction-aware embeddings | cell-cell interaction-aware spatial embedding | reference-free | unclear | Optional GPU; code pending/manual review |
| spMOCA | spatially informed co-expression analysis for gene program discovery | spatial transcriptomics expression + spatial coordinates | co-expression patterns/modules from matrix-normal modeling | spatial co-expression model | co-expression programs/modules | explicit spatial covariance/co-expression model | reference-free | unclear | CPU; code pending/manual review |
| LSGI | interpretable spatial gradient analysis for program/pattern discovery | spatial transcriptomics expression + spatial coordinates | spatial gradients and interpretable gene/program patterns | spatial gradient analysis | gradients / spatial program patterns | explicit spatial gradient structure | reference-free | unclear | CPU; code pending/manual review |

## Decision Tree

If the desired output is a coordinated multicellular or cohort-level program:
- Prefer / consider `DIALOGUE` for coordinated programs across annotated cell types or compartments.
- Prefer / consider `scITD` when cohort or sample-stratifying tensor components are central.
- Prefer / consider `CellPie` for scalable unsupervised factor discovery.
- Prefer / consider `SPICEMIX` when program discovery is coupled to spatial cell-identity mixture modeling.

If the desired output is a spatial topic, factor, or continuous spatial program pattern:
- Prefer / consider `STAMP` or `SpaTM` for spatial topics and associated gene modules or transcriptional programs.
- Prefer / consider `FISHFactor` when the dataset is subcellular-resolution and factor discovery is central.
- Prefer / consider `LSGI` when continuous spatial gradients are central.

If the desired output is gene-set correlation or spatial co-expression rather than latent topics or factors:
- Prefer / consider `SpatialCorr` when predefined gene sets are central.
- Prefer / consider `SpaceX` for spatial co-expression networks.
- Prefer / consider `spMOCA` for model-based spatial co-expression programs or modules.

If the desired output is a boundary-sensitive regulatory-program-style annotation or score:
- Prefer / consider `SpaGRN`.
- Keep regulatory-program interpretation framed as prior-dependent and indirect rather than direct mechanism discovery.

If the desired output is interaction-aware tissue modules from single-cell-resolution spatial transcriptomics:
- Prefer / consider `SPACE`.
- Keep method identity and output interpretation explicit because the name is ambiguous across the literature.

If no branch fits cleanly:
- Record the mismatch and request manual review rather than forcing a default reading order across incompatible output types.
