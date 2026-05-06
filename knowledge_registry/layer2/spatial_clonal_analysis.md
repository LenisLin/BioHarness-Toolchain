# Spatial Clonal Analysis

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Spatial Clonal Analysis`.

This topic covers spatial clone, subclone, copy-number, allele-specific CNA, point-mutation clone, and copy-number-profile subclone analysis. Allele-specific CNA, total CNA, point-mutation clone deconvolution, and copy-number-profile subclone calls are not interchangeable signal bases.

Use another Layer 1 problem first when the requested endpoint is ordinary cell type inference, domain clustering, phenotype association, or expression contrast without clonal signal. Do not treat `SlideCNA` as a strong subclone caller, and do not make `STARCH` a default; both are branch-specific options with signal-resolution limits.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Clonal Signal Basis | Matched Data Dependence | Allele / Mutation Resolution | Spot Mixture Handling | Spatial Scope Cue | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CalicoST | infer allele-specific CNAs, clone labels, tumor phylogeography, and optional tumor proportion from SRT | SRT transcript counts + allele counts at germline SNPs + spatial coordinates from one or more slices | allele-specific copy-number profiles + clone labels + phylogeny/phylogeography | allele-specific CNA | SRT + allele counts | allele-specific CNA | models tumor admixture | multi-slice / phylogeography | CPU; code available |
| Clonalscope | detect cancer subclones, label malignant cells or spots, and trace spatially segregated subclones using copy-number profiles | single-cell or spatial omic copy-number profiles, with optional matched bulk DNA sequencing prior information | subclone assignments + malignant labels + traced spatial subclone patterns | copy-number profile | optional matched DNA | copy-number-profile subclone | supports single-cell and ST | multi-dataset / general | CPU; code available |
| STARCH | infer total-copy-number profiles and spatial clone assignments from ST expression data | spatial transcriptomics expression matrix + spatial coordinates / spot graph | copy-number profiles + spot clone assignments | total CNA from expression | ST only | total-CNA clone | assumes dominant clone per spot | single or adjacent sections | CPU; code available |
| Tumoroscope | infer clone proportions in each ST spot and clone-specific expression by integrating genomic, image, and spatial transcriptomic data | ST mutation read counts + clone genotypes from bulk DNA/WES + pathology-image-derived cell counts + expression matrix | spot-level clone proportions + refined cell counts + clone-specific expression profiles | somatic point mutation + expression | ST + matched DNA + pathology image | somatic mutation clone | deconvolves clone proportions | spot mixture deconvolution | CPU; code available |
| SlideCNA | detect spatial CNA patterns and potential subclones from high-resolution sparse spatial transcriptomics | sparse Slide-seq-like ST expression data + spatial coordinates + non-malignant reference spots or beads | binned spatial CNA scores + CNA-defined clusters / potential subclone patterns | spatial CNA from sparse expression | ST + reference spots | total-CNA spatial pattern | bins sparse spots | high-resolution sparse ST | CPU; code available |

## Decision Tree

If usable allele counts at germline SNPs are available and the goal is allele-specific CNA clones or phylogeography:
- Prefer / consider `CalicoST`.
- Keep allele-specific signal and matched validation expectations separate from total-expression CNA methods.

If copy-number profiles or compatible CNA estimates are already available and the goal is general subclone detection across spatial or single-cell tumor omics:
- Prefer / consider `Clonalscope`.
- Keep optional matched DNA priors and input CNA quality visible.

If the available data are ST expression plus coordinates and the goal is coarse total-CNA spatial clone assignment:
- Consider `STARCH`.
- Do not treat it as a default or as allele-specific, point-mutation, or current broad validation evidence.

If matched bulk DNA or WES-derived clone genotypes, ST mutation reads, and pathology-derived cell-count priors are available:
- Prefer / consider `Tumoroscope` for spot-level point-mutation clone mixture deconvolution.
- Keep matched-data dependence and spot-mixture assumptions explicit.

If the data are sparse high-resolution Slide-seq-like ST and the goal is spatial CNA recovery or potential CNA-defined subclone patterns:
- Consider `SlideCNA`.
- Frame outputs as binned spatial CNA scores and potential subclone patterns rather than strong standalone subclone calls.

If the signal basis is missing or ambiguous:
- Resolve whether the task has allele-specific CNA, total CNA, point-mutation clone, or copy-number-profile evidence before selecting a method.
