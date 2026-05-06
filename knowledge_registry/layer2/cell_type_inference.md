# Cell Type Inference

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Cell Type Inference`.

This topic covers cell-type composition inference, cell-type annotation, deconvolution, state-aware inference, image-assisted inference, and spatial placement or reconstruction of cell-type signal. The main branch families here are reference-assisted spot deconvolution, marker-gene-assisted deconvolution, reference-free deconvolution or annotation, spatial or domain-aware deconvolution, image or histology-assisted inference, cell placement or single-cell reconstruction, and specialized state or boundary rows.

Use another Layer 1 problem first when the task is segmentation, domain clustering, denoising, or gene-expression prediction without a cell-identity question. Do not collapse cell placement or reconstruction into ordinary spot-proportion estimation, do not describe high-resolution placements as direct single-cell truth, and keep reference mismatch, marker bias, domain circularity, and image bias visible.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Reference Dependence | Resolution Target | Spatial Signal Use | Image Signal Use | Benchmark Coverage | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AdRoit | robust cell-type composition inference for mixed transcriptomes | bulk or spatial mixture expression + reference signatures | cell-type composition estimates | scRNA-reference-assisted | spot mixture | none | none | review-only coverage | CPU; code access unclear |
| CARD | spatially informed reference-based cell-type deconvolution | ST count matrix + spatial coordinates + scRNA-seq reference | cell-type proportion map | scRNA-reference-assisted | spot mixture | required | none | independent benchmark includes | CPU; code available |
| cell2location | fine-grained cell abundance mapping | ST count matrix + scRNA-seq reference signatures | cell-type abundance estimates per location | scRNA-reference-assisted | spot mixture | optional | none | independent benchmark includes | Optional GPU; code available |
| Celloscope | marker-gene-driven probabilistic deconvolution | ST count matrix + marker-gene cell-type cues | cell-type proportion estimates | marker-gene-assisted | spot mixture | optional | none | review-only coverage | CPU; code access unclear |
| CellsFromSpace | reference-free deconvolution and cell-type annotation | ST count matrix with spatial locations | cell-type components and annotations | reference-free | annotation | required | none | review-only coverage | CPU; code access unclear |
| CytoSPACE | cell placement / high-resolution alignment of single-cell and spatial profiles | ST spots + scRNA-seq reference + spatial coordinates | assigned single cells or cell types at spatial positions | scRNA-reference-assisted | cell placement | required | none | method-paper/local benchmark only | CPU; code available |
| DestVI | cell-type deconvolution with within-type cell-state continuums | ST count matrix + scRNA-seq reference with continuous states | cell-type proportions and state latent variables | scRNA-reference-assisted | cell-state/specialized | optional | none | independent benchmark includes | Optional GPU; code available |
| DSTG | graph-based spatial cell-type deconvolution | ST count matrix + spatial graph + reference information | cell-type proportions | scRNA-reference-assisted | spot mixture | required | none | method-paper/local benchmark only | Optional GPU; code available |
| NLSDeconv | efficient weighted least-squares cell-type deconvolution | ST count matrix + reference signatures | cell-type proportions | scRNA-reference-assisted | spot mixture | optional | none | review-only coverage | CPU; code access unclear |
| RCTD | robust reference-based decomposition of cell-type mixtures | ST count matrix + scRNA-seq reference | cell-type weights and singlet/doublet-style mixture calls | scRNA-reference-assisted | spot mixture | optional | none | independent benchmark includes | CPU; code available |
| Redeconve | single-cell-resolution spatial deconvolution/reconstruction | ST spots + scRNA-seq reference + spatial information | single-cell-resolution cell-type map | scRNA-reference-assisted | single-cell reconstruction | required | none | review-only coverage | Optional GPU; code available |
| SMART | marker-gene-assisted topic-model deconvolution | ST count matrix + marker-gene information | cell-type proportion/topic estimates | marker-gene-assisted | spot mixture | optional | none | method-paper/local benchmark only | Optional GPU; code access unclear |
| SONAR | spatially weighted probabilistic cell-type deconvolution | ST count matrix + spatial locations + cell-type signatures | cell-type proportion estimates | scRNA-reference-assisted | spot mixture | required | none | review-only coverage | CPU; code access unclear |
| SPADE | domain-specific cell-type proportion estimation | ST count matrix + spatial domains and cell-type reference cues | domain-aware cell-type estimates | scRNA-reference-assisted | spot mixture | required | none | review-only coverage | CPU; code available |
| SpatialDWLS | weighted least-squares cell-type deconvolution | ST count matrix + scRNA-seq reference | cell-type proportion estimates | scRNA-reference-assisted | spot mixture | optional | none | method-paper/local benchmark only | CPU; code available |
| SpatialPrompt | spatially aware spot deconvolution with domain context | ST count matrix + spatial coordinates and reference/domain cues | cell-type proportions and domain-linked outputs | scRNA-reference-assisted | spot mixture | required | none | review-only coverage | Optional GPU; code access unclear |
| SpatialScope | cellular-level transcriptomic reconstruction and deconvolution | ST spots + scRNA-seq reference | cellular-resolution transcriptomic map | scRNA-reference-assisted | single-cell reconstruction | required | none | method-paper/local benchmark only | Optional GPU; code access unclear |
| SPOTlight | seeded NMF regression deconvolution | ST count matrix + scRNA-seq reference or marker-derived signatures | cell-type proportions per spot | scRNA-reference-assisted | spot mixture | none | none | method-paper/local benchmark only | CPU; code available |
| Starfysh | reference-free tumor-microenvironment deconvolution using histology-aware latent factors | ST count matrix + histology image | cellular archetypes / spatial factor map | histology-aware reference-free | annotation | required | required | method-paper/local benchmark only | Optional GPU; code available |
| STdeconvolve | reference-free topic-model deconvolution | ST count matrix | cell-type-like topics and proportions | reference-free | spot mixture | none | none | independent benchmark includes | CPU; code available |
| STdGCN | graph convolutional cell-type deconvolution | ST count matrix + spatial graph + reference information | cell-type proportion estimates | scRNA-reference-assisted | spot mixture | required | none | method-paper/local benchmark only | Optional GPU; code available |
| stereoscope | probabilistic reference-based cell-type topography inference | ST count matrix + scRNA-seq reference | cell-type proportions / topography map | scRNA-reference-assisted | spot mixture | optional | none | independent benchmark includes | Optional GPU; code available |
| STIE | single-cell-level deconvolution, convolution, and clustering | ST count matrix + nuclear morphology/image signal | single-cell-level cell-type and cluster assignments | unclear | single-cell reconstruction | required | required | review-only coverage | CPU; code access unclear |
| STRIDE | cell-type decomposition and integration with scRNA-seq | ST count matrix + scRNA-seq reference | cell-type proportion estimates | scRNA-reference-assisted | spot mixture | optional | none | method-paper/local benchmark only | CPU; code access unclear |
| stVAE | VAE-based cell-type composition deconvolution | cellular-resolution or high-resolution ST data | cell-type composition estimates | scRNA-reference-assisted | spot mixture | optional | none | review-only coverage | Optional GPU; code access unclear |
| Tangram | mapping single-cell profiles to spatial locations | ST count matrix + scRNA-seq reference | cell-to-space alignment / cell-type map | scRNA-reference-assisted | cell placement | required | none | method-paper/local benchmark only | Optional GPU; code available |
| DeepScence | specialized inference of senescent-cell state in spatial context | single-cell/spatial expression data for senescence state detection | senescent-cell state labels or scores | unclear | cell-state/specialized | optional | none | method-paper/local benchmark only | Optional GPU; code access unclear |
| OmicsTweezer | distribution-independent cell deconvolution | multi-omics or spatial expression mixture data | cell-type deconvolution estimates | unclear | spot mixture | optional | none | method-paper/local benchmark only | Optional GPU; code access unclear |
| STAMapper | cell-type mapping and annotation in single-cell spatial transcriptomics | single-cell spatial transcriptomics expression data | cell-type annotations / spatial cell-type map | unclear | annotation | required | none | method-paper/local benchmark only | CPU; code access unclear |
| STHD | probabilistic high-definition cell typing | whole-transcriptome spatial data at spot or high-definition resolution | cell-type labels or probabilities | unclear | annotation | required | none | method-paper/local benchmark only | CPU; code access unclear |
| STALocator | localization of single-cell profiles using spatial transcriptomics | scRNA-seq profiles + spatial transcriptomics reference tissue | localized cells or cell-type map | scRNA-reference-assisted | cell placement | required | none | method-paper/local benchmark only | CPU; code access unclear |
| gwSPADE | gene-frequency-weighted reference-free deconvolution | ST count matrix with spatial expression frequencies | cell-type-like components / proportions | reference-free | spot mixture | required | none | method-paper/local benchmark only | CPU; code access unclear |
| DECLUST | cluster-based cell-type deconvolution | ST count matrix + spatial/cluster structure | cell-type proportion or cluster-associated estimates | unclear | spot mixture | required | none | method-paper/local benchmark only | CPU; code access unclear |
| PANDA | dual decoding of cell types and gene expression | ST count matrix with spot-adaptive expression modeling | cell-type proportions and gene-expression estimates | unclear | gene-expression deconvolution | optional | none | method-paper/local benchmark only | CPU; code access unclear |
| STged | gene-expression deconvolution linked to cell-type inference | ST count matrix + graph/spatial expression structure | deconvolved gene expression / inferred cell-type signal | unclear | gene-expression deconvolution | required | none | method-paper/local benchmark only | CPU; code access unclear |

## Decision Tree

If a matched scRNA-seq reference is intended and the desired output is spot-level proportions or abundances:
- Prefer / consider `AdRoit`, `CARD`, `cell2location`, `NLSDeconv`, `RCTD`, `SONAR`, `SpatialDWLS`, `SPOTlight`, `stereoscope`, or `STRIDE`.
- Consider `DestVI` when within-cell-type state variation is central rather than plain discrete proportions.

If marker genes are the intended cell-type cue rather than a full reference:
- Prefer / consider `Celloscope` or `SMART`.
- Consider `SPOTlight` only when seeded signature regression still matches the intended reading path.

If a reference-free route is the real goal:
- Prefer / consider `CellsFromSpace`, `STdeconvolve`, `gwSPADE`, or `DECLUST`.
- Consider `Starfysh` when reference-free inference is intentionally coupled to histology-aware latent structure.

If spatial neighborhoods, domains, or graphs should actively shape the inference:
- Prefer / consider `CARD`, `DSTG`, `SONAR`, `SPADE`, `SpatialPrompt`, or `STdGCN`.
- Keep domain-aware or graph-aware outputs distinct from independent downstream domain validation.

If the main question is image-, histology-, or nuclear-morphology-assisted inference:
- Prefer / consider `Starfysh` or `STIE`.
- Use this branch only when matched image or morphology signal is genuinely part of the scientific question.

If the task is cell placement, localization, or single-cell reconstruction rather than spot-mixture estimation:
- Prefer / consider `CytoSPACE`, `Redeconve`, `SpatialScope`, `Tangram`, or `STALocator`.
- Treat these rows as placement or reconstruction routes, not as ordinary spot-level proportion estimators.

If the task is a specialized state, annotation, or gene-expression-coupled boundary row:
- Prefer / consider `DeepScence` for senescent-cell-state detection.
- Prefer / consider `STAMapper` or `STHD` for single-cell-spatial annotation or high-definition cell typing.
- Prefer / consider `PANDA` or `STged` when cell-type inference is intentionally coupled to gene-expression deconvolution.
- Consider `OmicsTweezer` when distribution-independent or cross-omics deconvolution framing is the central branch cue.

After choosing the branch:
- Keep benchmark coverage as branch-local context, not as a cross-topic ordering rule.
- Keep reference mismatch, marker bias, domain circularity, image bias, and overprecision caveats visible in the reading path.
- Re-check whether the requested endpoint is composition, annotation, placement, reconstruction, or a specialized state before narrowing candidates.
