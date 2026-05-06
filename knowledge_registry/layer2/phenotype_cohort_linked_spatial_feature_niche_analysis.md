# Phenotype- / Cohort-linked Spatial Feature and Niche Analysis

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Phenotype- / Cohort-linked Spatial Feature and Niche Analysis`.

This topic covers phenotype-, cohort-, condition-, survival-, or outcome-linked spatial feature and niche association. The deliverable is association, prioritization, or phenotype-linked niche interpretation, not causal proof.

Use another Layer 1 problem first when the requested endpoint is direct condition-contrast testing, within-sample spatially variable gene detection, generic Graph / Neighborhood discovery without cohort signal, pathology severity scoring, or direct cell type inference. `CytoCommunity` appears here only for phenotype/cohort-linked tissue cellular neighborhood or community-feature use.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Phenotype / Cohort Signal | Main Feature or Niche Output | Estimand Class | Transfer / Representation Dependence | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TissueMosaic | learning cross-sample tissue motif representations for cohort- or condition-associated spatial features | multi-sample ST or spatial single-cell datasets + coordinates and optional image-like or cell-type channels | self-supervised tissue representations, motif enrichment, and motif-associated differential features | multi-sample / cohort labels | self-supervised tissue representations, motif enrichment, and motif-associated differential features | cohort-level representation / motif association | self-supervised tissue representation | Optional GPU; code available |
| SpaLinker | linking spatial tumor microenvironment features to phenotype or clinical outcome signals through bulk cohorts | ST data + spatial features + bulk RNA-seq cohort profiles with clinical phenotype annotations | phenotype-associated spatial TME features, factors, and linked architectures | bulk cohort phenotypes | phenotype-associated spatial TME features, factors, and linked architectures | bulk-linked phenotype association | bulk-to-spatial transfer | Optional GPU; code access unclear |
| TiRank | prioritizing phenotype-associated cells, spots, and spatial niches for clinical biomarker discovery | bulk RNA-seq expression with clinical or phenotype table plus scRNA-seq or spatial transcriptomics inference data | TiRank scores, TiRank labels, and phenotype-associated spatial or cellular niches | bulk clinical phenotype or outcome signal | TiRank score/label and phenotype-associated niches or subpopulations | clinical phenotype-linked niche prioritization | bulk-to-scRNA/ST phenotype transfer | Optional GPU; code available |
| stClinic | identifying clinically or phenotypically relevant niches from integrated spatial multi-slice or multi-omics data | multi-slice spatial omics profiles, spatial coordinates, and optional clinical or phenotype labels | phenotype-linked niches, slice-level niche vectors, niche weights, predicted hazard ratios or class labels, and interpreted high-risk or phenotype-associated niches | clinical phenotype, survival, class label, or cohort signal | clinically relevant niches, niche vectors, and phenotype-linked niche weights | clinical phenotype-linked niche discovery | multi-slice graph integration and supervised phenotype weighting | Optional GPU; code available |
| CytoCommunity | identifying cohort- or phenotype-associated tissue cellular neighborhoods and community features | spatial cell phenotypes or spatial expression with coordinates, neighborhood graph, and cohort/condition/phenotype labels | cohort-associated tissue cellular neighborhoods, community features, and niche summaries | cohort, condition, or phenotype labels | cohort-associated tissue cellular neighborhoods, community features, and niche summaries | cohort-linked cellular neighborhood feature discovery | supervised graph/neighborhood representation | Optional GPU; code available |

## Decision Tree

If the deliverable is learned tissue motifs or cohort-associated spatial representations across many samples:
- Prefer / consider `TissueMosaic`.
- Keep acquisition, composition, preprocessing confounding, and representation-opacity caveats visible.

If the deliverable is bulk-cohort-linked spatial tumor microenvironment feature association:
- Prefer / consider `SpaLinker`.
- Keep bulk-to-spatial transfer, tumor purity, and phenotype-label confounding visible.

If the deliverable is phenotype-associated cell, spot, or niche prioritization transferred from clinical bulk cohorts:
- Prefer / consider `TiRank`.
- Keep association, transfer, and gene-coverage caveats visible rather than treating prioritization as causality.

If the deliverable is clinically or phenotypically relevant niche discovery from multi-slice or multi-omics spatial data:
- Prefer / consider `stClinic`.
- Keep supervised label leakage, representation opacity, batch, slice, and tissue-composition confounding visible.

If the deliverable is cohort- or phenotype-associated tissue cellular neighborhoods or community features:
- Prefer / consider `CytoCommunity` only in this phenotype/cohort-linked use.
- Route generic unsupervised neighborhood discovery back to `Graph / Neighborhood`.

If the task asks for a direct contrast statistic, condition-specific DE test, or spatial pattern contrast:
- Route to `Spatial Contrast Testing` rather than this association and prioritization topic.
