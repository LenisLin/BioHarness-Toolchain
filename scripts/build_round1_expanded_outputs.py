from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


RUN_DATE = "2026-04-11"
WINDOW = ("2015-01-01", "2026-04-11")
AUTHORITATIVE_CSV = "/mnt/NAS_21T/ProjectData/BioHarness/2026-04-10_spatial_method_survey_v1.csv"
AUTHORITATIVE_REPORT = "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/2026-04-11_authoritative_reconcile_report.md"

SCRATCH_FIELDS = [
    "Analysis Problem",
    "Subtask",
    "Method Family",
    "Method Name",
    "Title",
    "DOI",
    "PMID",
    "Year",
    "Venue",
    "Discovery Route",
    "Discovery Source",
    "Accessibility",
    "GitHub URL",
    "Compute Requirement",
    "Round 1 Decision",
    "Exclusion Reason",
    "Notes",
]

MASTER_FIELDS = [
    "Analysis Problem",
    "Subtask",
    "Method Name",
    "Method Family",
    "Primary Ecosystem",
    "Title",
    "DOI",
    "PMID",
    "Year",
    "Venue",
    "Discovery Route",
    "Discovery Source",
    "Evidence Basis",
    "Accessibility",
    "GitHub URL",
    "Compute Requirement",
    "Registry Status",
    "Notes",
]

BOUNDARY_FIELDS = [
    "Source Trigger",
    "Item Type",
    "Method Name",
    "Title",
    "Candidate Analysis Problem",
    "Candidate Subtask",
    "Reason Held Out",
    "Next Action",
    "Notes",
]

BOUNDARY_DATE = "2026-04-12"

WHITELIST_VENUES = {
    "Nature",
    "Cell",
    "Science",
    "Nature Methods",
    "Nature Biotechnology",
    "Nature Genetics",
    "Genome Biology",
    "Nucleic Acids Research",
    "Cell Systems",
    "Science Advances",
    "Nature Communications",
    "Proceedings of the National Academy of Sciences of the United States of America",
    "International Conference on Learning Representations",
    "Conference on Neural Information Processing Systems",
}

ECOSYSTEM_EXCEPTION_VENUES = {
    "Bioinformatics",
    "Briefings in Bioinformatics",
    "BMC Bioinformatics",
}

def m(
    subtask: str,
    family: str,
    name: str,
    title: str,
    doi: str,
    pmid: str,
    year: int,
    venue: str,
    route: str,
    source: str,
    access: str,
    github: str,
    compute: str,
    decision: str,
    exclusion: str = "",
    notes: str = "",
) -> dict[str, str]:
    return {
        "Subtask": subtask,
        "Method Family": family,
        "Method Name": name,
        "Title": title,
        "DOI": doi,
        "PMID": pmid,
        "Year": str(year),
        "Venue": venue,
        "Discovery Route": route,
        "Discovery Source": source,
        "Accessibility": access,
        "GitHub URL": github,
        "Compute Requirement": compute,
        "Round 1 Decision": decision,
        "Exclusion Reason": exclusion,
        "Notes": notes,
    }


def b(
    source_trigger: str,
    item_type: str,
    method_name: str,
    title: str,
    candidate_analysis_problem: str,
    candidate_subtask: str,
    reason_held_out: str,
    next_action: str,
    notes: str = "",
) -> dict[str, str]:
    return {
        "Source Trigger": source_trigger,
        "Item Type": item_type,
        "Method Name": method_name,
        "Title": title,
        "Candidate Analysis Problem": candidate_analysis_problem,
        "Candidate Subtask": candidate_subtask,
        "Reason Held Out": reason_held_out,
        "Next Action": next_action,
        "Notes": notes,
    }


BOUNDARY_CANDIDATES = [
    b(
        "User-supplied priority paper",
        "Workflow paper",
        "",
        "Simultaneous CRISPR screening and spatial transcriptomics reveal intracellular, intercellular, and functional transcriptional circuits",
        "Spatial Perturbation Analysis",
        "Workflow-derived perturbation analysis",
        "The paper is primarily a biological workflow and does not expose a clearly reusable standalone computational method for the current registry.",
        "Recheck only if a named reusable method or software package is later identified.",
    ),
]


PROTOCOL_CHANGES = [
    "Expanded Round 1 scope from 8 topics to 15 topics, activating Segmentation, Super-resolution, Spatial Gene Prediction, Spatial Perturbation Analysis, Program Discovery, Spatial Trajectory Analysis, and Spatial Clonal Analysis.",
    "Replaced abbreviated venue labels with full venue names, including Nucleic Acids Research, Proceedings of the National Academy of Sciences of the United States of America, International Conference on Learning Representations, and Conference on Neural Information Processing Systems.",
    "Restricted conference retrieval to main-conference papers only, excluding workshop outputs.",
    "Moved temporary run notes and temporary summary outputs off docs/ and onto NAS.",
    "Locked the search window to 2015-01-01 through 2026-04-11.",
    "Removed the pilot-era 8-12 method cap and replaced it with a source-layer exhaustion stop rule.",
    "Made whitelist venue sweep and ecosystem-exception sweep mandatory documented steps for every topic.",
    "Marked earlier Batch 1 scratch outputs as reference inputs only and kept the authoritative NAS CSV frozen for the whole expanded run.",
]


PRIOR_BATCH1_METHODS = {
    "Spatially Variable Gene Detection": {
        "SpatialDE",
        "SPARK",
        "SPARK-X",
        "SOMDE",
        "nnSVG",
        "BSP",
        "STANCE",
        "PROST",
    },
    "Cell Type Inference": {
        "RCTD",
        "cell2location",
        "CARD",
        "STdeconvolve",
        "DestVI",
        "stereoscope",
        "Tangram",
        "CytoSPACE",
    },
    "Cell-Cell Communication": {
        "Giotto",
        "stLearn",
        "SpaOTsc",
        "COMMOT",
        "SpaTalk",
        "SpatialDM",
        "MISTy",
        "SVCA",
    },
}


TOPICS = [
    {
        "analysis_problem": "Preprocessing",
        "slug": "preprocessing",
        "run_objective": (
            "Expand Round 1 preprocessing coverage beyond the pilot-era omission and capture "
            "the current computational core without collapsing denoising, contamination correction, "
            "and quality control into an unqualified catch-all."
        ),
        "scope_confirmation": [
            "This pass targeted computational preprocessing methods applied to measured spatial transcriptomics profiles before downstream clustering or inference.",
            "Experimental assay engineering, imaging-based cell segmentation, and explicit super-resolution methods were treated as adjacent topics, not preprocessing rows.",
        ],
        "active_stable_subtask_window": ["Denoising / artifact correction"],
        "deferred_candidate_subtasks": [
            "Normalization / scaling",
            "Cross-slice quality harmonization",
            "Segmentation-coupled transcript reassignment",
        ],
        "benchmark_seeds": [
            "No dedicated preprocessing benchmark seed was identified within the 2015-01-01 to 2026-04-11 window.",
        ],
        "review_seeds": [
            "Cancer Cell 2022, Spatial transcriptomics (PMID 36099884), used as a general survey anchor for preprocessing pain points rather than as a stopping boundary.",
        ],
        "whitelist_results": [
            "Nature Methods sweep surfaced Sprod and SpotSweeper as direct additions.",
            "Nature Communications sweep surfaced SpotClean and MIST as direct additions.",
            "No main-conference papers from International Conference on Learning Representations or Conference on Neural Information Processing Systems met the stable preprocessing window.",
        ],
        "exception_results": [
            "Bioinformatics, Briefings in Bioinformatics, and BMC Bioinformatics sweeps did not add a clearly superior preprocessing method beyond the whitelist core for this subtask window.",
        ],
        "direct_results": [
            "User-prioritized direct search also added SpotGF as a published denoising method built around optimal-transport-based gene filtering.",
        ],
        "methods": [
            m(
                "Denoising / artifact correction",
                "Probabilistic contamination correction",
                "SpotClean",
                "SpotClean adjusts for spot swapping in spatial transcriptomics data",
                "10.1038/s41467-022-30587-y",
                "35624112",
                2022,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + targeted PubMed search for spatial transcriptomics contamination correction",
                "Yes",
                "https://github.com/zijianni/SpotClean",
                "CPU",
                "Include",
                notes="Core spot-swapping correction method for spot-based spatial transcriptomics preprocessing.",
            ),
            m(
                "Denoising / artifact correction",
                "Latent graph denoising",
                "Sprod",
                "Sprod for de-noising spatially resolved transcriptomics data based on position and image information",
                "10.1038/s41592-022-01560-w",
                "35927477",
                2022,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted PubMed search for spatial transcriptomics denoising",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Strong preprocessing representative that explicitly uses morphology and coordinates for denoising.",
            ),
            m(
                "Denoising / artifact correction",
                "Region-aware imputation",
                "MIST",
                "Region-specific denoising identifies spatial co-expression patterns and intra-tissue heterogeneity in spatially resolved transcriptomics data",
                "10.1038/s41467-022-34567-0",
                "36376296",
                2022,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + targeted PubMed search for spatial transcriptomics denoising and imputation",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included as a denoising and imputation method within the stable preprocessing core.",
            ),
            m(
                "Denoising / artifact correction",
                "Spatially aware quality control",
                "SpotSweeper",
                "SpotSweeper: spatially aware quality control for spatial transcriptomics",
                "10.1038/s41592-025-02713-3",
                "40481362",
                2025,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted PubMed search for spatial transcriptomics quality control",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Expanded the preprocessing topic beyond denoising by adding explicit spatial quality control.",
            ),
            m(
                "Denoising / artifact correction",
                "Optimal-transport gene filtering",
                "SpotGF",
                "SpotGF: Denoising spatially resolved transcriptomics data using an optimal transport-based gene filtering algorithm",
                "10.1093/bioinformatics/btaf145",
                "",
                2025,
                "Bioinformatics",
                "Direct search",
                "User-prioritized direct search after preprocessing registry review",
                "Yes",
                "https://github.com/illuminate6060/SpotGF",
                "CPU",
                "Include",
                notes="Added as a published denoising method that complements the existing contamination-correction and graph-denoising rows.",
            ),
        ],
        "label_stable": "Yes. `Preprocessing` is a defensible top-level label for Round 1.",
        "subtask_sufficient": (
            "Only partially. `Denoising / artifact correction` is stable enough for the current expanded run, "
            "but it does not yet absorb normalization-only or segmentation-coupled preprocessing methods cleanly."
        ),
        "family_assessment": (
            "Yes. The included rows kept `Method Family` algorithmic rather than task-like, using labels such as "
            "`Latent graph denoising` and `Spatially aware quality control`."
        ),
        "revision_needed": (
            "Yes. Preprocessing still needs a clearer split between denoising, contamination correction, QC, and "
            "enhancement before any formal promotion beyond the stable core."
        ),
        "taxonomy_blockers": [
            "Preprocessing remains broader than the current stable subtask window.",
        ],
    },
    {
        "analysis_problem": "Spatially Variable Gene Detection",
        "slug": "spatially_variable_gene_detection",
        "run_objective": (
            "Reopen the prior Batch 1 SVG shard and extend it into a formal expanded run that documents the full "
            "source-layer search rather than stopping at the pilot-sized core."
        ),
        "scope_confirmation": [
            "This pass retained `Overall SVG detection` as the stable core while formally accepting the cell-type-specific branch and a narrow gene-centric tissue-pattern branch.",
            "Domain-coupled SVG methods were redirected toward neighboring domain-identification tasks when that yielded a cleaner first-layer placement.",
        ],
        "active_stable_subtask_window": [
            "Overall SVG detection",
            "Cell-type-specific SVG detection",
            "Gene-centric tissue pattern mining",
        ],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "Li et al. Genome Biology 2025, Systematic benchmarking of computational methods to identify spatially variable genes (PMID 40968359).",
            "Chen et al. Genome Biology 2024, Evaluating spatially variable gene detection methods for spatial transcriptomics data (PMID 38225676).",
        ],
        "review_seeds": [
            "Yan et al. Nature Communications 2025, Categorization of 34 computational methods to detect spatially variable genes from spatially resolved transcriptomics data (PMID 39880807).",
            "Das Adhikari et al. Computational and Structural Biotechnology Journal 2024, Recent advances in spatially variable gene detection in spatial transcriptomics (PMID 38370977).",
        ],
        "whitelist_results": [
            "Whitelist sweep reaffirmed the stable core around SpatialDE, SPARK, SPARK-X, nnSVG, BSP, and HEARTSVG.",
            "No main-conference papers from International Conference on Learning Representations or Conference on Neural Information Processing Systems added a stable new SVG method within the current subtask window.",
        ],
        "exception_results": [
            "Bioinformatics sweep retained SOMDE as the main ecosystem-exception method with continuing impact.",
            "No new Briefings in Bioinformatics or BMC Bioinformatics method displaced the existing stable core.",
        ],
        "direct_results": [
            "Direct gap-filling search added HEARTSVG beyond the earlier narrow Batch 1 scratch set.",
            "Direct search also confirmed STANCE, ctSVG, and Celina as accepted methods for the cell-type-specific SVG branch.",
            "User-prioritized boundary reconciliation also promoted STMiner into a dedicated gene-centric tissue-pattern branch.",
        ],
        "methods": [
            m(
                "Overall SVG detection",
                "Gaussian process regression",
                "SpatialDE",
                "SpatialDE: identification of spatially variable genes",
                "10.1038/nmeth.4636",
                "29553579",
                2018,
                "Nature Methods",
                "Review seed",
                "Yan et al. Nature Communications 2025 SVG categorization review",
                "Yes",
                "https://github.com/Teichlab/SpatialDE",
                "CPU",
                "Include",
                notes="Canonical overall SVG baseline retained from the earlier formal pass.",
            ),
            m(
                "Overall SVG detection",
                "Generalized linear spatial model",
                "SPARK",
                "Statistical analysis of spatial expression patterns for spatially resolved transcriptomic studies",
                "10.1038/s41592-019-0701-7",
                "31988518",
                2020,
                "Nature Methods",
                "Benchmark seed",
                "Li et al. Genome Biology 2025 benchmarking study",
                "Yes",
                "https://github.com/xzhoulab/SPARK",
                "CPU",
                "Include",
                notes="Stable benchmark-backed SVG method.",
            ),
            m(
                "Overall SVG detection",
                "Non-parametric covariance test",
                "SPARK-X",
                "SPARK-X: non-parametric modeling enables scalable and robust detection of spatial expression patterns for large spatial transcriptomic studies",
                "10.1186/s13059-021-02404-0",
                "34154649",
                2021,
                "Genome Biology",
                "Benchmark seed",
                "Li et al. Genome Biology 2025 benchmarking study",
                "Yes",
                "https://github.com/xzhoulab/SPARK",
                "CPU",
                "Include",
                notes="Scalable extension of the SPARK family retained in the stable core.",
            ),
            m(
                "Overall SVG detection",
                "Self-organizing map",
                "SOMDE",
                "SOMDE: a scalable method for identifying spatially variable genes with self-organizing map",
                "10.1093/bioinformatics/btab471",
                "34165490",
                2021,
                "Bioinformatics",
                "Review seed",
                "Das Adhikari et al. 2024 review + ecosystem-exception sweep",
                "Yes",
                "https://github.com/XuegongLab/SOMDE",
                "CPU",
                "Include",
                notes="Retained through the ecosystem-exception path with explicit documentation this time.",
            ),
            m(
                "Overall SVG detection",
                "Nearest-neighbor Gaussian process",
                "nnSVG",
                "nnSVG for the scalable identification of spatially variable genes using nearest-neighbor Gaussian processes",
                "10.1038/s41467-023-39748-z",
                "37429865",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Li et al. Genome Biology 2025 benchmarking study",
                "Yes",
                "https://github.com/lmweber/nnSVG",
                "CPU",
                "Include",
                notes="Strong whitelist-supported core method.",
            ),
            m(
                "Overall SVG detection",
                "Granularity-based non-parametric statistic",
                "BSP",
                "Dimension-agnostic and granularity-based spatially variable gene identification using BSP",
                "10.1038/s41467-023-43256-5",
                "37963892",
                2023,
                "Nature Communications",
                "Review seed",
                "Yan et al. Nature Communications 2025 SVG categorization review",
                "Yes",
                "https://github.com/juexinwang/BSP",
                "CPU",
                "Include",
                notes="Stable overall SVG method retained from the earlier run.",
            ),
            m(
                "Overall SVG detection",
                "Distribution-free statistical test",
                "HEARTSVG",
                "HEARTSVG: a fast and accurate method for identifying spatially variable genes in large-scale spatial transcriptomics",
                "10.1038/s41467-024-49846-1",
                "38972896",
                2024,
                "Nature Communications",
                "Direct search",
                "Direct gap-filling search after benchmark, review, and venue sweeps",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="New stable addition beyond the earlier narrow Batch 1 scratch set.",
            ),
            m(
                "Cell-type-specific SVG detection",
                "Unified statistical model",
                "STANCE",
                "STANCE: a unified statistical model to detect cell-type-specific spatially variable genes in spatial transcriptomics",
                "10.1038/s41467-025-57117-w",
                "39979358",
                2025,
                "Nature Communications",
                "Direct search",
                "Direct gap-filling search after seed-guided SVG expansion",
                "Yes",
                "https://github.com/Cui-STT-Lab/STANCE",
                "CPU",
                "Include",
                notes="Included as a cell-type-specific SVG method after this branch was accepted as a stable first-layer subtask.",
            ),
            m(
                "Cell-type-specific SVG detection",
                "Cell-type-specific statistical model",
                "ctSVG",
                "Identifying cell-type-specific spatially variable genes with ctSVG",
                "10.1186/s13059-025-03870-6",
                "41361894",
                2025,
                "Genome Biology",
                "Direct search",
                "Direct gap-filling search after boundary-branch check",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included as a cell-type-specific SVG method after this branch was accepted as a stable first-layer subtask.",
            ),
            m(
                "Cell-type-specific SVG detection",
                "Spatially varying coefficient model",
                "Celina",
                "Statistical identification of cell type-specific spatially variable genes in spatial transcriptomics",
                "10.1038/s41467-025-56280-4",
                "39865128",
                2025,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after cell-type-specific SVG branch audit",
                "Yes",
                "https://github.com/pekjoonwu/CELINA",
                "CPU",
                "Include",
                notes="Included as a cell-type-specific SVG method after this branch was accepted as a stable first-layer subtask.",
            ),
            m(
                "Gene-centric tissue pattern mining",
                "Gene-centric spatial pattern mining",
                "STMiner",
                "STMiner: Gene-centric spatial transcriptomics for deciphering tumor tissues",
                "10.1016/j.xgen.2025.100771",
                "39947134",
                2025,
                "Cell Genomics",
                "Direct search",
                "User-prioritized boundary reconciliation after gene-pattern branch acceptance",
                "Yes",
                "https://github.com/xjtu-omics/STMiner",
                "CPU",
                "Include",
                notes="Included in the accepted gene-centric tissue-pattern branch because the method's primary contribution is pattern mining from gene-level spatial distributions.",
            ),
        ],
        "label_stable": "Yes. `Spatially Variable Gene Detection` remains a stable top-level Round 1 analysis problem.",
        "subtask_sufficient": (
            "Yes for the accepted first-layer scope. `Overall SVG detection`, `Cell-type-specific SVG detection`, and `Gene-centric tissue pattern mining` now cover the stable SVG branches."
        ),
        "family_assessment": (
            "Yes. The stable rows kept `Method Family` algorithmic, and the boundary pressure remained in `Subtask` "
            "rather than leaking into `Method Family`."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the accepted SVG branches."
        ),
        "taxonomy_blockers": [
        ],
    },
    {
        "analysis_problem": "Integration",
        "slug": "integration",
        "run_objective": (
            "Establish a stable expanded Round 1 view of spatial transcriptomics integration methods centered on "
            "multi-slice alignment and cross-condition integration."
        ),
        "scope_confirmation": [
            "This pass focused on methods whose primary contribution is alignment, integration, or cross-slice harmonization of spatial transcriptomics datasets.",
            "Methods whose primary value is clustering, deconvolution, or gene prediction were retained in their neighboring topics even if they expose integration side-effects.",
        ],
        "active_stable_subtask_window": ["Multi-slice alignment / integration"],
        "deferred_candidate_subtasks": [
            "Cross-modal scRNA-seq plus ST coupling",
            "Alignment-free latent factor integration",
        ],
        "benchmark_seeds": [
            "Benchmarking data integration methods for spatial transcriptomics (PMID 39123269).",
            "A comprehensive benchmarking framework for spatial transcriptomics data integration (PMID 41024097).",
        ],
        "review_seeds": [
            "Strategies and software for integration of spatial transcriptomic and single-cell data (PMID 40568931).",
        ],
        "whitelist_results": [
            "Whitelist sweep reinforced PASTE, STalign, PRECAST, GraphST, SLAT, CAST, and SANTO as the main published integration layer.",
            "No main-conference papers from International Conference on Learning Representations or Conference on Neural Information Processing Systems displaced the journal-centered integration core.",
        ],
        "exception_results": [
            "No additional ecosystem-exception venue method overtook the whitelist core for the active alignment/integration window.",
        ],
        "direct_results": [
            "Direct search added PASTE2 as a partial-overlap extension and GPSA as a geometry-aware alignment addition.",
            "The 2026 Nature Computational Science alignment benchmark also prompted inclusion checks for DeST-OT and cross-topic duplication of GraphST under integration.",
            "User-prioritized direct search also added SPACEL as a published multi-slice architecture framework with explicit 3D alignment outputs.",
        ],
        "methods": [
            m(
                "Multi-slice alignment / integration",
                "Optimal transport alignment",
                "PASTE",
                "Alignment and integration of spatial transcriptomics data",
                "10.1038/s41592-022-01459-6",
                "35577957",
                2022,
                "Nature Methods",
                "Benchmark seed",
                "2024 and 2025 integration benchmarking studies",
                "Yes",
                "https://github.com/raphael-group/paste",
                "CPU",
                "Include",
                notes="Canonical baseline for multi-slice alignment and consensus integration.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Partial optimal transport alignment",
                "PASTE2",
                "Partial alignment of multislice spatially resolved transcriptomics data",
                "",
                "37553263",
                2023,
                "bioRxiv",
                "Direct search",
                "Direct gap-filling search after benchmark and review seeding",
                "Yes",
                "https://github.com/raphael-group/paste2",
                "CPU",
                "Include",
                notes="Included as a frontier extension of the PASTE family despite preprint-only status because its ecosystem relevance is already clear in the first-layer registry.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Diffeomorphic metric mapping",
                "STalign",
                "STalign: Alignment of spatial transcriptomics data using diffeomorphic metric mapping",
                "10.1038/s41467-023-43915-7",
                "38065970",
                2023,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + direct integration gap search",
                "Yes",
                "https://github.com/JEFworks-Lab/STalign",
                "CPU",
                "Include",
                notes="Retained for cross-technology alignment and coordinate-framework mapping.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Graph attention integration",
                "STAligner",
                "Integrating spatial transcriptomics data across different conditions, technologies and developmental stages",
                "10.1038/s43588-023-00528-w",
                "38177758",
                2023,
                "Nature Computational Science",
                "Benchmark seed",
                "Integration benchmark and review seeding",
                "Yes",
                "https://github.com/zhoux85/STAligner",
                "Optional GPU",
                "Include",
                notes="Promoted under a narrow Benchmark Override after repeated independent benchmark support confirmed it as an in-scope integration method.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Deep spatial architecture learning",
                "SPACEL",
                "SPACEL: deep learning-based characterization of spatial transcriptome architectures",
                "10.1038/s41467-023-43220-3",
                "37990022",
                2023,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after architecture-method audit",
                "Yes",
                "https://github.com/QuKunLab/SPACEL",
                "Optional GPU",
                "Include",
                notes="Added here as a cross-topic duplicate because Scube performs explicit 3D slice alignment and tissue stacking.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Probabilistic embedding and alignment",
                "PRECAST",
                "Probabilistic embedding, clustering, and alignment for integrating spatial transcriptomics data with PRECAST",
                "10.1038/s41467-023-35947-w",
                "36653349",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Integration benchmark studies and review seeds",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Kept in the stable integration core despite also exposing clustering outputs.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Gaussian process spatial alignment",
                "GPSA",
                "Non-rigid alignment of spatially resolved transcriptomics data with Gaussian process spatial alignment",
                "",
                "37592182",
                2023,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted gap-filling search",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included as a non-rigid alignment method complementary to optimal-transport approaches.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Graph self-supervised contrastive learning",
                "GraphST",
                "Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST",
                "10.1038/s41467-023-36796-3",
                "36859400",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Yan et al. Nature Computational Science 2026 alignment benchmark + clustering benchmark cross-check",
                "Yes",
                "https://github.com/JinmiaoChenLab/GraphST",
                "Optional GPU",
                "Include",
                notes="Added here as a cross-topic duplicate because integration is one of GraphST's explicit primary outputs.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Spatial manifold alignment",
                "SLAT",
                "Spatial-linked alignment tool (SLAT) for aligning heterogenous slices",
                "",
                "",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Yan et al. Nature Computational Science 2026 alignment benchmark",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Benchmark-supported slice-alignment method added to broaden the published integration layer beyond transport-only methods.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Single-cell-resolution search-and-match alignment",
                "CAST",
                "Search and match across spatial omics samples at single-cell resolution",
                "",
                "",
                2024,
                "Nature Methods",
                "Benchmark seed",
                "Yan et al. Nature Computational Science 2026 alignment benchmark",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Included as a published high-resolution alignment method highlighted by the 2026 alignment benchmark.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Coarse-to-fine alignment and stitching",
                "SANTO",
                "SANTO: a coarse-to-fine alignment and stitching method for spatial omics",
                "",
                "",
                2024,
                "Nature Communications",
                "Benchmark seed",
                "Yan et al. Nature Computational Science 2026 alignment benchmark",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Published stitching and alignment method added from the 2026 benchmark-supported literature set.",
            ),
            m(
                "Multi-slice alignment / integration",
                "Optimal transport spatiotemporal alignment",
                "DeST-OT",
                "DeST-OT: alignment of spatiotemporal transcriptomics data",
                "",
                "",
                2025,
                "Cell Systems",
                "Benchmark seed",
                "Yan et al. Nature Computational Science 2026 alignment benchmark",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Published spatiotemporal alignment method added because the benchmark treats it as part of the current alignment landscape.",
            ),
        ],
        "label_stable": "Yes. `Integration` is stable at the top level for Round 1.",
        "subtask_sufficient": (
            "Yes for the present run. `Multi-slice alignment / integration` captured the stable core cleanly, while "
            "cross-modal prediction methods were deferred to neighboring topics."
        ),
        "family_assessment": (
            "Yes. Method-family labels stayed algorithmic and did not collapse into generic integration language."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed before coordinator review. Frontier extensions such as PASTE2 are now "
            "retained explicitly in the first-layer registry while cross-modal prediction methods remain deferred."
        ),
        "taxonomy_blockers": [
            "Cross-modal prediction methods remain adjacent to this topic but were intentionally handled under Spatial Gene Prediction.",
        ],
    },
    {
        "analysis_problem": "Graph / Neighborhood",
        "slug": "graph_neighborhood",
        "run_objective": (
            "Add a stable neighborhood-focused layer to Round 1 without collapsing it into spatial domain clustering or "
            "ligand-receptor communication."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose primary contribution is learning neighborhood, niche, or local graph representations from spatial data.",
            "Methods centered on tissue-domain segmentation or explicit cell-cell communication inference were treated as adjacent boundary cases.",
        ],
        "active_stable_subtask_window": ["Neighborhood / niche representation learning"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed for neighborhood representation methods was identified within the required window.",
        ],
        "review_seeds": [
            "Matrix Biology 2020, Spatial-omics: Novel approaches to probe cell heterogeneity and extracellular matrix biology (PMID 32416243), used as an early review anchor.",
            "Broader spatial transcriptomics reviews were used only to locate neighborhood-analysis subproblems, not as stopping boundaries.",
        ],
        "whitelist_results": [
            "Whitelist sweep surfaced CellCharter, NSF, and NNMF as the clearest stable niche-representation methods.",
            "No main-conference papers from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable neighborhood core under the current admission rules.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the whitelist-supported neighborhood core.",
        ],
        "direct_results": [
            "Direct search added mNSF as a multi-sample extension while keeping the accepted neighborhood scope focused on niche representation methods.",
            "Cross-checking against the spatial clustering benchmark also surfaced SOTIP as a neighborhood-oriented microenvironment representation method.",
            "User-prioritized review of newer niche-representation papers also added ENVI as a covariance-based niche representation and spatial inference framework.",
        ],
        "methods": [
            m(
                "Neighborhood / niche representation learning",
                "Spatial niche clustering",
                "CellCharter",
                "CellCharter reveals spatial cell niches associated with tissue remodeling and cell plasticity",
                "10.1038/s41588-023-01588-4",
                "38066188",
                2024,
                "Nature Genetics",
                "Direct search",
                "Whitelist venue sweep: Nature Genetics + targeted neighborhood-method search",
                "Yes",
                "https://github.com/CSOgroup/cellcharter",
                "CPU",
                "Include",
                notes="Strong stable representative for niche representation and comparison across cohorts.",
            ),
            m(
                "Neighborhood / niche representation learning",
                "Non-negative spatial factorization",
                "NSF",
                "Nonnegative spatial factorization applied to spatial genomics",
                "10.1038/s41592-022-01687-w",
                "36587187",
                2023,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + neighborhood representation search",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Retained as a factorization-based neighborhood representation method.",
            ),
            m(
                "Neighborhood / niche representation learning",
                "Multi-sample spatial factorization",
                "mNSF",
                "Multi-sample non-negative spatial factorization",
                "10.1186/s13059-025-03601-x",
                "40457480",
                2025,
                "Genome Biology",
                "Direct search",
                "Published Genome Biology version confirmed during neighborhood supplement review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included after the published Genome Biology version resolved the earlier venue and metadata uncertainty.",
            ),
            m(
                "Neighborhood / niche representation learning",
                "Neighborhood nonnegative matrix factorization",
                "NNMF",
                "Neighborhood nonnegative matrix factorization identifies patterns and spatially-variable genes in large-scale spatial transcriptomics data",
                "10.1186/s13059-025-03846-6",
                "41546049",
                2026,
                "Genome Biology",
                "Direct search",
                "Whitelist venue sweep: Genome Biology + targeted neighborhood-method search",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="New 2026 addition that broadens the neighborhood-representation layer beyond the older factorization methods.",
            ),
            m(
                "Neighborhood / niche representation learning",
                "Covariance niche representation plus conditional variational autoencoder",
                "ENVI",
                "The covariance environment defines cellular niches for spatial inference",
                "10.1038/s41587-024-02193-4",
                "38565973",
                2025,
                "Nature Biotechnology",
                "Direct search",
                "User-prioritized niche-representation audit after neighborhood topic review",
                "Yes",
                "https://github.com/dpeerlab/ENVI",
                "Optional GPU",
                "Include",
                notes="Included as a niche-representation and spatial inference framework centered on covariance-defined cellular neighborhoods.",
            ),
            m(
                "Neighborhood / niche representation learning",
                "Optimal-transport microenvironment modeling",
                "SOTIP",
                "SOTIP: an optimal-transport-based framework for identifying spatial domains in tissues",
                "",
                "",
                2022,
                "Nature Communications",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added under neighborhood analysis because tissue microenvironment representation is one of its primary practical outputs.",
            ),
        ],
        "label_stable": "Yes. `Graph / Neighborhood` is usable as a Round 1 top-level label.",
        "subtask_sufficient": (
            "Yes for the accepted scope. `Neighborhood / niche representation learning` now cleanly captures the intended first-layer neighborhood methods."
        ),
        "family_assessment": (
            "Yes for the core. Boundary pressure arose from methods whose primary output straddles multiple adjacent tasks."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the accepted neighborhood-representation scope."
        ),
        "taxonomy_blockers": [
        ],
    },
    {
        "analysis_problem": "Spatial Trajectory Analysis",
        "slug": "spatial_trajectory_analysis",
        "run_objective": (
            "Add a first-layer trajectory topic for methods whose primary contribution is reconstructing spatially informed developmental or state-transition paths."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose primary output is spatial trajectory or lineage inference from spatial transcriptomics.",
            "Methods centered on neighborhood representation or static domain discovery were kept in their neighboring topics rather than treated as trajectory methods.",
        ],
        "active_stable_subtask_window": ["Spatial trajectory inference"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed for spatial trajectory inference was identified within the required window.",
        ],
        "review_seeds": [
            "No trajectory-specific review with cleaner spatial-method coverage than the direct method paper was identified within the required window.",
        ],
        "whitelist_results": [
            "Cell Systems sweep surfaced SpaTrack as the current published anchor for spatial trajectory inference.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems displaced this trajectory anchor within the current window.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the current Cell Systems anchor for this subtask.",
        ],
        "direct_results": [
            "User-prioritized boundary reconciliation moved SpaTrack out of held-out status once spatial trajectory inference was accepted as a top-level first-layer topic.",
        ],
        "methods": [
            m(
                "Spatial trajectory inference",
                "Optimal transport trajectory inference",
                "SpaTrack",
                "Inferring cell trajectories of spatial transcriptomics via optimal transport analysis",
                "10.1016/j.cels.2025.101194",
                "39904341",
                2025,
                "Cell Systems",
                "Direct search",
                "User-prioritized boundary reconciliation after trajectory-topic acceptance",
                "Yes",
                "https://github.com/yzf072/spaTrack",
                "CPU",
                "Include",
                notes="Included as the anchor method for the accepted spatial trajectory inference topic.",
            ),
        ],
        "label_stable": "Yes. `Spatial Trajectory Analysis` is now an accepted first-layer top-level label for Round 1.",
        "subtask_sufficient": (
            "Yes for the current first-layer scope. `Spatial trajectory inference` captures the accepted trajectory contribution without forcing it into graph or neighborhood branches."
        ),
        "family_assessment": (
            "Yes. The included method stayed methodological and did not require taxonomy leakage into neighboring graph or lineage wording."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the accepted trajectory branch."
        ),
        "taxonomy_blockers": [],
    },
    {
        "analysis_problem": "Program Discovery",
        "slug": "program_discovery",
        "run_objective": (
            "Add a multicellular program-discovery layer for methods whose primary contribution is learning interpretable "
            "programs, factors, or coordinated tissue states from spatially resolved data."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose main output is multicellular programs, latent factors, or coordinated cellular states rather than domain labels alone.",
            "Generic representation-learning papers and segmentation-free tissue representation methods were kept outside this initial stable window unless multicellular program discovery was the explicit primary task.",
        ],
        "active_stable_subtask_window": ["Multicellular / program discovery"],
        "deferred_candidate_subtasks": [
            "Segmentation-free tissue representation",
            "Spatial factor discovery beyond transcriptomics-first scope",
        ],
        "benchmark_seeds": [
            "No dedicated benchmark seed for multicellular or factor-based program discovery was identified within the required window.",
        ],
        "review_seeds": [
            "Nature Reviews Genetics 2025 deconvolution review was used only as a cross-topic anchor for cell-identity factor methods such as SPICEMIX.",
        ],
        "whitelist_results": [
            "Whitelist venue checks supported scITD, DIALOGUE, CellPie, and SPICEMIX as a coherent first program-discovery seed set.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems added a cleaner initial seed method than the journal-backed set.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the whitelist-supported seed set.",
        ],
        "direct_results": [
            "User-prioritized direct search formalized DIALOGUE and CellPie as part of a dedicated multicellular-program topic rather than leaving them only in boundary tracking.",
            "User-prioritized review of multicellular factor methods also added scITD and SPICEMIX as initial program-discovery anchors.",
        ],
        "methods": [
            m(
                "Multicellular / program discovery",
                "Interpretable tensor decomposition",
                "scITD",
                "Coordinated, multicellular patterns of transcriptional variation that stratify patient cohorts are revealed by tensor decomposition",
                "10.1038/s41587-024-02411-z",
                "39313646",
                2025,
                "Nature Biotechnology",
                "Direct search",
                "User-prioritized direct search for multicellular program methods",
                "Yes",
                "https://github.com/kharchenkolab/scITD",
                "CPU",
                "Include",
                notes="Included as a cohort-stratifying multicellular program discovery method grounded in interpretable tensor decomposition.",
            ),
            m(
                "Multicellular / program discovery",
                "Coordinated latent program modeling",
                "DIALOGUE",
                "DIALOGUE maps multicellular programs in tissue from single-cell or spatial transcriptomics data",
                "10.1038/s41587-022-01288-0",
                "35513526",
                2022,
                "Nature Biotechnology",
                "Direct search",
                "User-prioritized direct search after Program Discovery topic audit",
                "Yes",
                "https://github.com/livnatje/DIALOGUE",
                "CPU",
                "Include",
                notes="Included as a direct multicellular program discovery method for tissue-resolved data.",
            ),
            m(
                "Multicellular / program discovery",
                "Joint non-negative matrix factorization",
                "CellPie",
                "CellPie: a scalable spatial transcriptomics factor discovery method via joint non-negative matrix factorization",
                "10.1093/nar/gkaf251",
                "40167331",
                2025,
                "Nucleic Acids Research",
                "Direct search",
                "User-prioritized direct search after Program Discovery topic audit",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included as a scalable spatial factor discovery method that fits the multicellular program branch.",
            ),
            m(
                "Multicellular / program discovery",
                "Probabilistic latent variable modeling",
                "SPICEMIX",
                "SPICEMIX enables integrative single-cell spatial modeling of cell identity",
                "10.1038/s41588-022-01256-z",
                "36624346",
                2023,
                "Nature Genetics",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review + Program Discovery topic audit",
                "Yes",
                "https://github.com/ma-compbio/SpiceMix",
                "CPU",
                "Include",
                notes="Included as a cell-identity and factor-modeling method that cleanly fits multicellular program discovery.",
            ),
        ],
        "label_stable": "Yes. `Program Discovery` is now a usable first-layer top-level analysis problem.",
        "subtask_sufficient": (
            "Yes for the initial seed set. `Multicellular / program discovery` is broad enough to hold the current factor and multicellular-state methods without becoming a generic representation bucket."
        ),
        "family_assessment": (
            "Yes. The method-family labels stayed methodological and centered on program, factor, or tensor discovery rather than generic representation learning."
        ),
        "revision_needed": (
            "Yes for later expansion. Segmentation-free representation and broader cell-program methods still need a second-pass boundary review before this topic grows further."
        ),
        "taxonomy_blockers": [
            "Segmentation-free tissue representation remains outside the current program-discovery window.",
        ],
    },
    {
        "analysis_problem": "Domain / Clustering",
        "slug": "domain_clustering",
        "run_objective": (
            "Build an expanded spatial-domain-identification layer that goes beyond the earlier pilot topics while keeping "
            "task boundaries against neighborhood modeling and SVG coupling explicit."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose primary contribution is spatial domain identification or clustering.",
            "Methods whose main value lies in neighborhood representation, explicit communication modeling, or coupled SVG discovery were treated as adjacent boundary cases.",
        ],
        "active_stable_subtask_window": ["Spatial domain identification"],
        "deferred_candidate_subtasks": [
            "Functional landscape discovery",
            "Domain-coupled SVG prioritization",
        ],
        "benchmark_seeds": [
            "Benchmarking clustering methods for spatially resolved transcriptomics data (PMID 38491270).",
            "Comprehensive benchmarking and scalability analysis of computational tools for spatial domain identification in transcriptomics (PMID 41472857).",
        ],
        "review_seeds": [
            "Benchmarking and integrating multi-slice clustering methods for spatial transcriptomics (PMID 40966657).",
        ],
        "whitelist_results": [
            "Whitelist sweep retained BayesSpace, SpaGCN, STAGATE, GraphST, BANKSY, BASS, SEDR, SpatialPCA, and DR-SC as the dominant published domain-identification layer.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems added a stable new domain-identification method beyond the journal core.",
        ],
        "exception_results": [
            "No Bioinformatics, Briefings in Bioinformatics, or BMC Bioinformatics method displaced the whitelist-supported core.",
        ],
        "direct_results": [
            "Direct gap-filling search added SpaSEG and STCC as newer domain-identification additions.",
            "Benchmark-guided gap filling also added published domain-identification methods such as CCST, DeepST, PRECAST, stLearn, and SpatialPrompt when their clustering or domain output was explicit.",
            "User-prioritized domain-method review also added MENDER, SpaTopic, STAMP, SPACEL, SiGra, PROST, and Pianno as explicit spatial architecture, annotation, or domain-identification methods.",
        ],
        "methods": [
            m(
                "Spatial domain identification",
                "Bayesian spatial clustering",
                "BayesSpace",
                "Spatial transcriptomics at subspot resolution with BayesSpace",
                "10.1038/s41587-021-00935-2",
                "34083791",
                2021,
                "Nature Biotechnology",
                "Benchmark seed",
                "2024 and 2025 spatial clustering benchmarking studies",
                "Yes",
                "https://github.com/edward130603/BayesSpace",
                "CPU",
                "Include",
                notes="Stable benchmark-backed core method for domain identification.",
            ),
            m(
                "Spatial domain identification",
                "Graph autoencoder with iterative imputation",
                "ADEPT",
                "ADEPT: a graph autoencoder with imputation and iterative clustering for robust spatial transcriptomics clustering",
                "10.1093/bib/bbad144",
                "37235055",
                2023,
                "Briefings in Bioinformatics",
                "Benchmark seed",
                "Genome Biology 2024 and Nature Methods 2024 spatial clustering benchmarks + targeted method-paper check",
                "Yes",
                "https://github.com/maiziezhoulab/ADEPT",
                "Optional GPU",
                "Include",
                notes="Included because benchmark coverage and the method paper support robust spatial-domain identification through graph autoencoding with iterative imputation.",
            ),
            m(
                "Spatial domain identification",
                "Graph convolutional network",
                "SpaGCN",
                "SpaGCN: Integrating gene expression, spatial location and histology to identify spatial domains and spatially variable genes by graph convolutional network",
                "10.1038/s41592-021-01255-8",
                "34711970",
                2021,
                "Nature Methods",
                "Benchmark seed",
                "Spatial clustering benchmark seeds",
                "Yes",
                "https://github.com/jianhuupenn/SpaGCN",
                "Optional GPU",
                "Include",
                notes="Core domain-identification method retained despite its secondary SVG functionality.",
            ),
            m(
                "Spatial domain identification",
                "Graph attention auto-encoder",
                "STAGATE",
                "Deciphering spatial domains from spatially resolved transcriptomics with an adaptive graph attention auto-encoder",
                "",
                "35365632",
                2022,
                "Nature Communications",
                "Benchmark seed",
                "Spatial clustering benchmark seeds",
                "Yes",
                "https://github.com/zhanglabtools/STAGATE",
                "Optional GPU",
                "Include",
                notes="Stable core method for graph-based spatial domain learning.",
            ),
            m(
                "Spatial domain identification",
                "Graph self-supervised contrastive learning",
                "GraphST",
                "Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST",
                "10.1038/s41467-023-36796-3",
                "36859400",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Spatial clustering benchmark seeds",
                "Yes",
                "https://github.com/JinmiaoChenLab/GraphST",
                "Optional GPU",
                "Include",
                notes="Retained under Domain / Clustering because clustering is its primary stable contribution in this survey.",
            ),
            m(
                "Spatial domain identification",
                "Spatially regularized deep graph network",
                "SpaceFlow",
                "SpaceFlow: mapping single-cell spatial transcriptome trajectories by deep manifold learning",
                "10.1038/s41467-022-31739-w",
                "35835774",
                2022,
                "Nature Communications",
                "Benchmark seed",
                "Genome Biology 2024 spatial clustering benchmark + SRTBenchmark continuity recommendations",
                "Yes",
                "https://github.com/hongleir/SpaceFlow",
                "Optional GPU",
                "Include",
                notes="Included because benchmark and public-method materials explicitly support domain segmentation despite the method's trajectory-adjacent framing.",
            ),
            m(
                "Spatial domain identification",
                "Bayesian multiscale clustering",
                "BASS",
                "BASS: multi-scale and multi-sample analysis enables accurate cell type clustering and spatial domain detection in spatial transcriptomic studies",
                "",
                "",
                2022,
                "Genome Biology",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark + NAR 2025 domain benchmark",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Benchmark-supported Bayesian domain-identification method added from the published clustering benchmark set.",
            ),
            m(
                "Spatial domain identification",
                "Graph neural network clustering",
                "SEDR",
                "Unsupervised spatially embedded deep representation of spatial transcriptomics",
                "",
                "",
                2024,
                "Genome Medicine",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark + NAR 2025 domain benchmark",
                "Yes",
                "https://github.com/JinmiaoChenLab/SEDR",
                "Optional GPU",
                "Include",
                notes="Published deep-representation domain method retained because both benchmark papers include it in the current clustering landscape.",
            ),
            m(
                "Spatial domain identification",
                "Spatially aware dimension reduction",
                "SpatialPCA",
                "SpatialPCA: low-dimensional representation and spatial domain detection for spatial transcriptomics",
                "",
                "",
                2022,
                "Nature Communications",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark + NAR 2025 domain benchmark",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added because the clustering benchmarks repeatedly treat SpatialPCA as a core published domain-identification baseline.",
            ),
            m(
                "Spatial domain identification",
                "Joint dimension reduction and clustering",
                "DR-SC",
                "Joint dimension reduction and clustering analysis for single-cell RNA-seq and spatial transcriptomics data",
                "",
                "",
                2024,
                "Biometrics",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark + NAR 2025 domain benchmark",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Published joint dimension-reduction and clustering method added after benchmark-guided reassessment.",
            ),
            m(
                "Spatial domain identification",
                "Graph neural network clustering",
                "CCST",
                "Cell clustering for spatial transcriptomics data with graph neural networks",
                "",
                "",
                2022,
                "Nature Computational Science",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Benchmark-listed clustering method added because spatial-domain identification is one of its explicit use cases.",
            ),
            m(
                "Spatial domain identification",
                "Multi-range cellular-context representation",
                "MENDER",
                "MENDER: fast and scalable tissue structure identification in spatial omics data",
                "10.1038/s41467-023-44367-9",
                "38182575",
                2024,
                "Nature Communications",
                "Direct search",
                "User-prioritized domain-identification audit after benchmark reassessment",
                "Yes",
                "https://github.com/yuanzhiyuan/MENDER",
                "CPU",
                "Include",
                notes="Included as a fast, scalable tissue-structure identification method with explicit multi-slice alignment capability.",
            ),
            m(
                "Spatial domain identification",
                "Deep pathological-architecture learning",
                "DeepST",
                "Define and visualize pathological architectures of human tissues from spatially resolved transcriptomics using deep learning",
                "",
                "",
                2022,
                "Computational and Structural Biotechnology Journal",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark + targeted published-method check",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Added as a published deep-learning spatial-domain method surfaced by the clustering benchmark literature.",
            ),
            m(
                "Spatial domain identification",
                "Histology-guided contrastive learning",
                "ConGI",
                "Identifying spatial domain by adapting transcriptomics with histology through contrastive learning",
                "10.1093/bib/bbad048",
                "",
                2023,
                "Briefings in Bioinformatics",
                "Benchmark seed",
                "Genome Biology 2024 spatial clustering benchmark + targeted paper check",
                "Yes",
                "https://github.com/biomed-AI/ConGI",
                "Optional GPU",
                "Include",
                notes="Included because benchmark coverage treats it as an image-guided spatial-domain method with especially strong tumor-dataset relevance.",
            ),
            m(
                "Spatial domain identification",
                "Topic-model spatial domain discovery",
                "SpaTopic",
                "SpaTopic: A statistical learning framework for exploring tumor spatial architecture from spatially resolved transcriptomic data",
                "10.1126/sciadv.adp4942",
                "39331720",
                2024,
                "Science Advances",
                "Direct search",
                "User-prioritized direct search for tumor spatial architecture methods",
                "Yes",
                "https://github.com/compbioNJU/SpaTopic",
                "CPU",
                "Include",
                notes="Included because the method explicitly identifies and compares pathology-relevant spatial domains from tumor ST data.",
            ),
            m(
                "Spatial domain identification",
                "Neighborhood-kernel clustering",
                "BANKSY",
                "BANKSY unifies cell typing and tissue domain segmentation for scalable spatial omics data analysis",
                "10.1038/s41588-024-01664-3",
                "38413725",
                2024,
                "Nature Genetics",
                "Direct search",
                "Whitelist venue sweep: Nature Genetics + targeted domain-method search",
                "Yes",
                "https://github.com/prabhakarlab/Banksy_py",
                "CPU",
                "Include",
                notes="Included here because domain segmentation is one of BANKSY's primary stable outputs.",
            ),
            m(
                "Spatial domain identification",
                "Probabilistic embedding, clustering, and alignment",
                "PRECAST",
                "Probabilistic embedding, clustering, and alignment for integrating spatial transcriptomics data with PRECAST",
                "10.1038/s41467-023-35947-w",
                "36653349",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Spatial clustering benchmarks + cross-topic duplication from integration",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Duplicated here because clustering and domain identification are explicit outputs alongside integration.",
            ),
            m(
                "Spatial domain identification",
                "Spatial trajectory-aware graph learning",
                "stLearn",
                "Robust mapping of spatiotemporal trajectories and cell-cell interactions in healthy and diseased tissues",
                "10.1038/s41467-023-43120-6",
                "38007580",
                2023,
                "Nature Communications",
                "Benchmark seed",
                "Li et al. Nature Methods 2024 spatial clustering benchmark",
                "Yes",
                "https://github.com/BiomedicalMachineLearning/stLearn",
                "CPU",
                "Include",
                notes="Added as a cross-topic duplicate because the clustering benchmark explicitly treats stLearn as a spatial-domain method.",
            ),
            m(
                "Spatial domain identification",
                "Multimodal contrastive graph learning",
                "conST",
                "conST: an interpretable multi-modal contrastive learning framework for spatial transcriptomics",
                "10.1101/2022.01.14.476408",
                "",
                2022,
                "bioRxiv",
                "Benchmark seed",
                "Genome Biology 2024 spatial clustering benchmark + targeted repository check",
                "Yes",
                "https://github.com/ys-zong/conST",
                "Optional GPU",
                "Include",
                notes="Included because the clustering benchmark explicitly treats conST as a spatial-domain method and it fills the multimodal contrastive bridge inside the current domain-identification landscape.",
            ),
            m(
                "Spatial domain identification",
                "Spatially aware deconvolution and domain identification",
                "SpatialPrompt",
                "SpatialPrompt: spatially aware scalable and accurate tool for spot deconvolution and domain identification in spatial transcriptomics",
                "",
                "",
                2025,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review + targeted domain-identification overlap check",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Included here as a cross-topic duplicate because domain identification is explicit in the method title and review coverage.",
            ),
            m(
                "Spatial domain identification",
                "Convolutional multitask learning",
                "SpaSEG",
                "SpaSEG: unsupervised deep learning for multi-task analysis of spatially resolved transcriptomics",
                "10.1186/s13059-025-03697-1",
                "40734184",
                2025,
                "Genome Biology",
                "Direct search",
                "Whitelist venue sweep: Genome Biology + gap-filling search for post-benchmark methods",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Newer addition with strong empirical coverage across platforms and tasks.",
            ),
            m(
                "Spatial domain identification",
                "Interpretable topic-model dimension reduction",
                "STAMP",
                "Interpretable spatially aware dimension reduction of spatial transcriptomics with STAMP",
                "10.1038/s41592-024-02463-8",
                "39407016",
                2024,
                "Nature Methods",
                "Direct search",
                "User-prioritized direct search for interpretable domain and topic models",
                "Yes",
                "https://github.com/JinmiaoChenLab/scTM",
                "Optional GPU",
                "Include",
                notes="Included because STAMP returns spatial topics and gene modules that align with biological domains in tissue.",
            ),
            m(
                "Spatial domain identification",
                "Deep spatial architecture learning",
                "SPACEL",
                "SPACEL: deep learning-based characterization of spatial transcriptome architectures",
                "10.1038/s41467-023-43220-3",
                "37990022",
                2023,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after architecture-method audit",
                "Yes",
                "https://github.com/QuKunLab/SPACEL",
                "Optional GPU",
                "Include",
                notes="Included here because Splane explicitly identifies spatial domains that are coherent across multiple slices.",
            ),
            m(
                "Spatial domain identification",
                "Image-augmented graph transformer",
                "SiGra",
                "SiGra: single-cell spatial elucidation through an image-augmented graph transformer",
                "10.1038/s41467-023-41437-w",
                "37699885",
                2023,
                "Nature Communications",
                "Direct search",
                "User-prioritized whitelist omission audit after domain-method reconciliation",
                "Yes",
                "https://github.com/QSong-github/SiGra",
                "Optional GPU",
                "Include",
                notes="Included because image-augmented graph learning is used directly for spatial domain identification and tissue-structure recovery.",
            ),
            m(
                "Spatial domain identification",
                "Pattern-recognition framework",
                "PROST",
                "PROST: quantitative identification of spatially variable genes and domain detection in spatial transcriptomics",
                "10.1038/s41467-024-44835-w",
                "38238417",
                2024,
                "Nature Communications",
                "Review seed",
                "Yan et al. Nature Communications 2025 SVG categorization review + domain reassignment",
                "Yes",
                "https://github.com/Tang-Lab-super/PROST",
                "CPU",
                "Include",
                notes="Included here because its coupled domain-discovery objective fits ordinary spatial domain identification better than the accepted SVG branches.",
            ),
            m(
                "Spatial domain identification",
                "Marker-guided Bayesian semantic annotation",
                "Pianno",
                "Pianno: a probabilistic framework automating semantic annotation for spatial transcriptomics",
                "10.1038/s41467-024-47152-4",
                "38565531",
                2024,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after annotation-branch audit + domain reassignment",
                "Yes",
                "https://github.com/yuqiuzhou/Pianno",
                "CPU",
                "Include",
                notes="Included here because its semantic annotation objective aligns more closely with domain identification than with deconvolution.",
            ),
            m(
                "Spatial domain identification",
                "Consensus clustering",
                "STCC",
                "STCC enhances spatial domain detection through consensus clustering of spatial transcriptomics data",
                "10.1101/gr.280031.124",
                "40355284",
                2025,
                "Genome Research",
                "Direct search",
                "Direct gap-filling search after benchmark and venue sweeps",
                "Yes",
                "https://github.com/hucongcong97/STCC",
                "CPU",
                "Include",
                notes="Included as a published domain-identification addition with a public implementation repository.",
            ),
        ],
        "label_stable": "Yes. `Domain / Clustering` is stable at the top level.",
        "subtask_sufficient": (
            "Yes for the stable core. `Spatial domain identification` cleanly holds the main benchmarked methods, "
            "although functional-landscape discovery still pushes beyond it."
        ),
        "family_assessment": (
            "Yes. The included methods stayed algorithmic, and the boundary pressure remained in adjacent subtasks."
        ),
        "revision_needed": (
            "No urgent protocol change is needed for the accepted domain-identification scope."
        ),
        "taxonomy_blockers": [],
    },
    {
        "analysis_problem": "Cell Type Inference",
        "slug": "cell_type_inference",
        "run_objective": (
            "Reopen the earlier Batch 1 cell-type-inference pass, preserve the stable deconvolution core, "
            "and expand coverage until the source layers are exhausted."
        ),
        "scope_confirmation": [
            "This pass kept `Cell type deconvolution` as the stable window.",
            "High-resolution mapping and placement methods that materially reconstruct cell-level spatial assignments were absorbed into the deconvolution layer for the current first-layer scope.",
        ],
        "active_stable_subtask_window": ["Cell type deconvolution"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "Li et al. Nature Communications 2023, Comprehensive benchmarking with guidelines for cellular deconvolution of spatial transcriptomics data.",
            "Spotless benchmarking paper (PMID 38787371), used to check whether post-2023 deconvolution additions materially changed the stable core.",
        ],
        "review_seeds": [
            "Nature Reviews Genetics 2025, Deconvolution methods for cell-type inference in spatial transcriptomics.",
        ],
        "whitelist_results": [
            "Whitelist sweep retained the benchmark-backed core and added no main-conference replacement method from International Conference on Learning Representations or Conference on Neural Information Processing Systems.",
            "Nucleic Acids Research sweep supported STRIDE as a stable deconvolution addition.",
        ],
        "exception_results": [
            "Briefings in Bioinformatics sweep added DSTG, AdRoit, and NLSDeconv as ecosystem-exception deconvolution methods.",
            "No additional Bioinformatics or BMC Bioinformatics method displaced the stable deconvolution core.",
        ],
        "direct_results": [
            "Direct gap-filling search added SpatialDWLS and SPOTlight as historically important deconvolution methods beyond the earlier narrow Batch 1 slice.",
            "The 2025 Nature Reviews Genetics deconvolution review also surfaced later published methods such as Redeconve, SpatialPrompt, SPADE, SONAR, FAST, CellsFromSpace, Celloscope, stVAE, SMART, STIE, and SpatialScope.",
            "User-prioritized direct search also added Starfysh, Tangram, CytoSPACE, and STdGCN as high-resolution scRNA-seq plus ST deconvolution or mapping methods now retained in the deconvolution layer.",
            "Pianno was redirected to Domain / Clustering because its semantic annotation objective aligns more closely with spatial domain identification.",
        ],
        "methods": [
            m(
                "Cell type deconvolution",
                "Probabilistic mixture model",
                "RCTD",
                "Robust decomposition of cell type mixtures in spatial transcriptomics",
                "10.1038/s41587-021-00830-w",
                "33603203",
                2022,
                "Nature Biotechnology",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/dmcable/spacexr",
                "CPU",
                "Include",
                notes="Stable benchmark-backed deconvolution representative.",
            ),
            m(
                "Cell type deconvolution",
                "Bayesian latent variable model",
                "cell2location",
                "Cell2location maps fine-grained cell types in spatial transcriptomics",
                "10.1038/s41587-021-01139-4",
                "35027729",
                2022,
                "Nature Biotechnology",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/BayraktarLab/cell2location",
                "Optional GPU",
                "Include",
                notes="Reference-based deconvolution method with strong ecosystem adoption.",
            ),
            m(
                "Cell type deconvolution",
                "Spatial correlation model",
                "CARD",
                "Spatially informed cell-type deconvolution for spatial transcriptomics",
                "10.1038/s41587-022-01273-7",
                "35501392",
                2022,
                "Nature Biotechnology",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/YMa-lab/CARD",
                "CPU",
                "Include",
                notes="Stable deconvolution core method.",
            ),
            m(
                "Cell type deconvolution",
                "Topic model",
                "STdeconvolve",
                "Reference-free cell type deconvolution of multi-cellular pixel-resolution spatially resolved transcriptomics data",
                "10.1038/s41467-022-30033-z",
                "35487922",
                2022,
                "Nature Communications",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/JEFworks-Lab/STdeconvolve",
                "CPU",
                "Include",
                notes="Reference-free deconvolution representative retained from earlier runs.",
            ),
            m(
                "Cell type deconvolution",
                "Variational latent variable model",
                "DestVI",
                "DestVI identifies continuums of cell types in spatial transcriptomics data",
                "10.1038/s41587-022-01272-8",
                "35449415",
                2022,
                "Nature Biotechnology",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/scverse/scvi-tools",
                "Optional GPU",
                "Include",
                notes="Continuous cell-state deconvolution retained in the stable core.",
            ),
            m(
                "Cell type deconvolution",
                "Probabilistic generative model",
                "stereoscope",
                "Single-cell and spatial transcriptomics enables probabilistic inference of cell type topography",
                "10.1038/s42003-020-01247-y",
                "33037292",
                2020,
                "Communications Biology",
                "Benchmark seed",
                "Li et al. Nature Communications 2023 deconvolution benchmark",
                "Yes",
                "https://github.com/almaan/stereoscope",
                "Optional GPU",
                "Include",
                notes="Included as a benchmark-supported deconvolution method because its ecosystem maturity and task fit justify first-layer inclusion despite the non-whitelist venue.",
            ),
            m(
                "Cell type deconvolution",
                "Weighted least squares deconvolution",
                "SpatialDWLS",
                "SpatialDWLS: accurate deconvolution of spatial transcriptomic data",
                "10.1186/s13059-021-02362-7",
                "33971932",
                2021,
                "Genome Biology",
                "Direct search",
                "Whitelist venue sweep: Genome Biology + targeted deconvolution gap search",
                "Yes",
                "https://github.com/rdong08/spatialDWLS",
                "CPU",
                "Include",
                notes="Important direct-search addition beyond the earlier narrow Batch 1 slice.",
            ),
            m(
                "Cell type deconvolution",
                "Seeded non-negative matrix factorization regression",
                "SPOTlight",
                "SPOTlight: seeded NMF regression to deconvolute spatial transcriptomics spots with single-cell transcriptomes",
                "10.1093/nar/gkab043",
                "33544846",
                2021,
                "Nucleic Acids Research",
                "Direct search",
                "Whitelist venue sweep: Nucleic Acids Research + targeted deconvolution gap search",
                "Yes",
                "https://github.com/MarcElosua/SPOTlight",
                "CPU",
                "Include",
                notes="Stable deconvolution addition anchored by a whitelist-venue sweep.",
            ),
            m(
                "Cell type deconvolution",
                "Topic-model deconvolution",
                "STRIDE",
                "STRIDE: accurately decomposing and integrating spatial transcriptomics using single-cell RNA sequencing",
                "10.1093/nar/gkac150",
                "35253896",
                2022,
                "Nucleic Acids Research",
                "Direct search",
                "Whitelist venue sweep: Nucleic Acids Research + targeted deconvolution gap search",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included as a stable whitelist-supported topic-model deconvolution method.",
            ),
            m(
                "Cell type deconvolution",
                "Graph convolutional deconvolution",
                "DSTG",
                "DSTG: deconvoluting spatial transcriptomics data through graph-based artificial intelligence",
                "10.1093/bib/bbaa414",
                "33480403",
                2021,
                "Briefings in Bioinformatics",
                "Direct search",
                "Ecosystem-exception sweep: Briefings in Bioinformatics + targeted deconvolution gap search",
                "Yes",
                "https://github.com/Su-informatics-lab/DSTG",
                "Optional GPU",
                "Include",
                notes="Exception-venue method retained with explicit documentation this time.",
            ),
            m(
                "Cell type deconvolution",
                "Robust compositional inference",
                "AdRoit",
                "AdRoit is an accurate and robust method to infer complex transcriptome composition",
                "",
                "",
                2022,
                "Briefings in Bioinformatics",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added from the 2025 deconvolution review as a published robust compositional inference method.",
            ),
            m(
                "Cell type deconvolution",
                "Dampened weighted least squares deconvolution",
                "NLSDeconv",
                "NLSDeconv: an accurate and efficient cell-type deconvolution method for spatial transcriptomics data",
                "",
                "",
                2023,
                "Briefings in Bioinformatics",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Published review-supported deconvolution method added to cover the weighted-regression branch more completely.",
            ),
            m(
                "Cell type deconvolution",
                "Single-cell-resolution reconstruction",
                "Redeconve",
                "Spatial transcriptomics deconvolution at single-cell resolution using Redeconve",
                "",
                "",
                2023,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "https://github.com/ZxZhou4150/Redeconve",
                "Optional GPU",
                "Include",
                notes="Added as a published single-cell-resolution reconstruction method highlighted by the deconvolution review.",
            ),
            m(
                "Cell type deconvolution",
                "Spatially aware deconvolution and domain identification",
                "SpatialPrompt",
                "SpatialPrompt: spatially aware scalable and accurate tool for spot deconvolution and domain identification in spatial transcriptomics",
                "",
                "",
                2025,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Included because the deconvolution review treats it as a published deconvolution method with explicit spatial awareness.",
            ),
            m(
                "Cell type deconvolution",
                "Domain-specific cell-type estimation",
                "SPADE",
                "SPADE: spatial deconvolution for domain specific cell-type estimation",
                "",
                "",
                2025,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "https://github.com/thecailab/SPADE",
                "CPU",
                "Include",
                notes="Added because the published deconvolution review explicitly includes a domain-specific estimation branch.",
            ),
            m(
                "Cell type deconvolution",
                "Spatially weighted Poisson-gamma deconvolution",
                "SONAR",
                "SONAR enables cell type deconvolution with spatially weighted Poisson-gamma model for spatial transcriptomics",
                "",
                "",
                2024,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Review-supported published deconvolution method added to strengthen the probabilistic-model branch.",
            ),
            m(
                "Cell type deconvolution",
                "Flexible deconvolution framework",
                "FAST",
                "Flexible analysis of spatial transcriptomics data (FAST): a deconvolution approach",
                "",
                "",
                2024,
                "BMC Bioinformatics",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added as a published deconvolution framework explicitly covered by the 2025 review.",
            ),
            m(
                "Cell type deconvolution",
                "Reference-free deconvolution and annotation",
                "CellsFromSpace",
                "CellsFromSpace: a fast, accurate, and reference-free tool to deconvolve and annotate spatially distributed omics data",
                "",
                "",
                2024,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Published reference-free deconvolution and annotation method added from the review-guided supplement pass.",
            ),
            m(
                "Cell type deconvolution",
                "Marker-gene probabilistic deconvolution",
                "Celloscope",
                "Celloscope: a probabilistic model for marker-gene-driven cell type deconvolution in spatial transcriptomics data",
                "",
                "",
                2022,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added to represent marker-gene-driven probabilistic deconvolution within the first-layer registry.",
            ),
            m(
                "Cell type deconvolution",
                "Variational autoencoder deconvolution",
                "stVAE",
                "stVAE deconvolves cell-type composition in large-scale cellular resolution spatial transcriptomics",
                "",
                "",
                2025,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Published variational deconvolution method added from the review's later-method layer.",
            ),
            m(
                "Cell type deconvolution",
                "Deep transcriptomic reconstruction",
                "SpatialScope",
                "SpatialScope: Spatial transcriptomic reconstruction at cellular level",
                "",
                "",
                2024,
                "Nature Communications",
                "Direct search",
                "Targeted gap-filling search after deconvolution benchmark and review seeding",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Added as a foundational published method that links cell-type inference with cellular-resolution transcriptomic reconstruction.",
            ),
            m(
                "Cell type deconvolution",
                "Similarity-aware reference mapping",
                "SMART",
                "Deconvolving spatial transcriptomics data with tissue morphology similarity and adversarial domain adaptation",
                "",
                "",
                2025,
                "Genome Biology",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "https://github.com/yyolanda/SMART",
                "Optional GPU",
                "Include",
                notes="Published deconvolution method added to capture morphology-aware domain-adaptation approaches.",
            ),
            m(
                "Cell type deconvolution",
                "Single-cell-level deconvolution and clustering",
                "STIE",
                "Single-cell level deconvolution, convolution, and clustering in in situ capturing-based spatial transcriptomics",
                "",
                "",
                2024,
                "Nature Communications",
                "Review seed",
                "Nature Reviews Genetics 2025 deconvolution review",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added because the review covers it as a published deconvolution method for in situ capturing-based assays.",
            ),
            m(
                "Cell type deconvolution",
                "Reference-free histology-aware generative deconvolution",
                "Starfysh",
                "Starfysh integrates spatial transcriptomic and histologic data to reveal heterogeneous tumor-immune hubs",
                "10.1038/s41587-024-02173-8",
                "38514799",
                2025,
                "Nature Biotechnology",
                "Direct search",
                "User-prioritized direct search after deconvolution and tumor-microenvironment audit",
                "Yes",
                "https://github.com/azizilab/starfysh",
                "Optional GPU",
                "Include",
                notes="Included as a reference-free deconvolution and state-inference method that also supports cross-sample hub analysis.",
            ),
            m(
                "Cell type deconvolution",
                "Deep learning alignment model",
                "Tangram",
                "Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram",
                "10.1038/s41592-021-01264-7",
                "34711971",
                2021,
                "Nature Methods",
                "Direct search",
                "Direct gap-filling search after benchmark and review seeding + later deconvolution reassignment",
                "Yes",
                "https://github.com/broadinstitute/Tangram",
                "Optional GPU",
                "Include",
                notes="Included in the deconvolution layer because its scRNA-seq-to-space mapping objective is being treated as a high-resolution deconvolution-style method in the current first-layer registry.",
            ),
            m(
                "Cell type deconvolution",
                "High-resolution alignment model",
                "CytoSPACE",
                "High-resolution alignment of single-cell and spatial transcriptomes with CytoSPACE",
                "10.1038/s41587-023-01697-9",
                "36879008",
                2023,
                "Nature Biotechnology",
                "Direct search",
                "Direct gap-filling search after benchmark and review seeding + later deconvolution reassignment",
                "Yes",
                "https://github.com/digitalcytometry/cytospace",
                "CPU",
                "Include",
                notes="Included in the deconvolution layer because its high-resolution cell placement objective is being treated as a deconvolution-adjacent reconstruction method.",
            ),
            m(
                "Cell type deconvolution",
                "Graph convolutional deconvolution",
                "STdGCN",
                "STdGCN: spatial transcriptomic cell-type deconvolution using graph convolutional networks",
                "10.1186/s13059-024-03353-0",
                "39103939",
                2024,
                "Genome Biology",
                "Direct search",
                "User-prioritized whitelist omission audit after deconvolution reconciliation",
                "Yes",
                "https://github.com/luoyuanlab/stdgcn",
                "Optional GPU",
                "Include",
                notes="Included as a published graph-based deconvolution method with direct benchmarking support in the accepted deconvolution branch.",
            ),
        ],
        "label_stable": "Yes. `Cell Type Inference` remains a stable top-level analysis problem.",
        "subtask_sufficient": (
            "Yes for the current accepted first-layer scope. The deconvolution layer now absorbs the accepted high-resolution mapping and reconstruction methods in this branch."
        ),
        "family_assessment": (
            "Yes. The included rows keep `Method Family` methodological while the accepted deconvolution scope now covers both compositional and high-resolution mapping-style methods."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the current first-layer cell-type scope."
        ),
        "taxonomy_blockers": [],
    },
    {
        "analysis_problem": "Comparative Analysis",
        "slug": "comparative_analysis",
        "run_objective": (
            "Add a comparison-oriented analytical layer for spatial transcriptomics while keeping it distinct from "
            "SVG detection and domain identification."
        ),
        "scope_confirmation": [
            "This pass focused on differential or comparative analyses that explicitly model spatial structure.",
            "Generic visualization frameworks and downstream biology portals were excluded unless they introduced a concrete comparative method.",
        ],
        "active_stable_subtask_window": ["Spatial differential expression / comparison"],
        "deferred_candidate_subtasks": [
            "Cross-condition niche comparison",
            "Comparative atlas-level alignment",
        ],
        "benchmark_seeds": [
            "A comparative study of statistical methods for identifying differentially expressed genes in spatial transcriptomics (PMID 41671295).",
        ],
        "review_seeds": [
            "From bulk RNA sequencing to spatial transcriptomics: a comparative review of differential gene expression analysis methods (PMID 41353326).",
        ],
        "whitelist_results": [
            "Whitelist sweep retained C-SIDE and Niche-DE as the clearest stable comparative-analysis methods.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable comparative core.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the whitelist-supported comparative core.",
        ],
        "direct_results": [
            "Direct gap-filling search added SpatialGEE as the main benchmark-supported non-whitelist comparative method needed to exhaust the source layers.",
        ],
        "methods": [
            m(
                "Spatial differential expression / comparison",
                "Cell-type-specific differential expression",
                "C-SIDE",
                "Cell type-specific inference of differential expression in spatial transcriptomics",
                "10.1038/s41592-022-01575-3",
                "36050488",
                2022,
                "Nature Methods",
                "Benchmark seed",
                "2026 comparative benchmarking study + 2025 review",
                "Yes",
                "https://github.com/dmcable/spacexr",
                "CPU",
                "Include",
                notes="Stable core method for cell-type-specific comparative analysis in spatial transcriptomics.",
            ),
            m(
                "Spatial differential expression / comparison",
                "Niche-differential expression",
                "Niche-DE",
                "Niche-DE: niche-differential gene expression analysis in spatial transcriptomics data identifies context-dependent cell-cell interactions",
                "10.1186/s13059-023-03159-6",
                "38217002",
                2024,
                "Genome Biology",
                "Direct search",
                "Whitelist venue sweep: Genome Biology + targeted comparative-analysis gap search",
                "Yes",
                "https://github.com/kaishumason/NicheDE",
                "CPU",
                "Include",
                notes="Included because it models comparative expression shifts conditioned on spatial niche context.",
            ),
            m(
                "Spatial differential expression / comparison",
                "Generalized estimating equation differential analysis",
                "SpatialGEE",
                "A comparative study of statistical methods for identifying differentially expressed genes in spatial transcriptomics",
                "10.1371/journal.pcbi.1013956",
                "41671295",
                2026,
                "PLOS Computational Biology",
                "Benchmark seed",
                "2026 comparative benchmarking study",
                "Yes",
                "https://github.com/pwei101/SpatialGEE",
                "CPU",
                "Include",
                notes="Promoted under a narrow Benchmark Override after direct benchmark support was cross-checked against the current comparative-analysis window.",
            ),
        ],
        "label_stable": "Only partially. `Comparative Analysis` is useful for Round 1 retrieval, but it remains broader than the current stable method core.",
        "subtask_sufficient": (
            "`Spatial differential expression / comparison` is sufficient for a stable first layer, but broader comparative atlas and cross-condition branches remain underspecified."
        ),
        "family_assessment": (
            "Yes. The recorded methods stayed methodological, but the topic itself is still broad enough to need later pruning."
        ),
        "revision_needed": (
            "Yes. Comparative analysis still needs a clearer long-term split between spatial DE, cross-condition niche comparison, and larger atlas-comparison workflows."
        ),
        "taxonomy_blockers": [
            "The top-level topic remains broader than the current stable subtask window.",
        ],
    },
    {
        "analysis_problem": "Spatial Clonal Analysis",
        "slug": "spatial_clonal_analysis",
        "run_objective": (
            "Add a first-layer clonal-analysis topic for methods whose primary contribution is identifying spatially resolved subclones or clonal structure."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose main output is spatial subclone detection or clonal composition analysis from spatial omics data.",
            "Generic comparative-analysis methods and tumor-state inference methods were kept in neighboring topics unless explicit subclone detection was the primary objective.",
        ],
        "active_stable_subtask_window": ["Spatial subclone detection"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed for spatial subclone detection was identified within the required window.",
        ],
        "review_seeds": [
            "No review seed with better direct coverage than the method paper was identified within the required window.",
        ],
        "whitelist_results": [
            "Nature Methods sweep surfaced Clonalscope as the current published anchor for spatial subclone detection.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems displaced this clonal-analysis anchor within the current window.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the current Nature Methods anchor for this subtask.",
        ],
        "direct_results": [
            "User-prioritized boundary reconciliation moved Clonalscope out of comparative-analysis holdout status once spatial clonal analysis was accepted as a top-level topic.",
        ],
        "methods": [
            m(
                "Spatial subclone detection",
                "Copy-number-based subclone inference",
                "Clonalscope",
                "Cancer subclone detection based on DNA copy number in single-cell and spatial omic sequencing data",
                "10.1038/s41592-025-02773-5",
                "40954304",
                2025,
                "Nature Methods",
                "Direct search",
                "User-prioritized boundary reconciliation after clonal-topic acceptance",
                "Yes",
                "https://github.com/seasoncloud/Clonalscope",
                "CPU",
                "Include",
                notes="Included as the anchor method for the accepted spatial subclone detection topic.",
            ),
        ],
        "label_stable": "Yes. `Spatial Clonal Analysis` is now an accepted first-layer top-level label for Round 1.",
        "subtask_sufficient": (
            "Yes for the current first-layer scope. `Spatial subclone detection` captures the accepted clonal-analysis contribution without forcing it into comparative analysis."
        ),
        "family_assessment": (
            "Yes. The included method stayed methodological and did not require fallback to a generic comparative-analysis label."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the accepted clonal-analysis branch."
        ),
        "taxonomy_blockers": [],
    },
    {
        "analysis_problem": "Cell-Cell Communication",
        "slug": "cell_cell_communication",
        "run_objective": (
            "Reopen the earlier narrow cell-cell-communication pass, document the full source-layer search, and "
            "preserve the separation between ligand-receptor inference and broader interaction-effect modeling."
        ),
        "scope_confirmation": [
            "This pass retained `Ligand-receptor communication inference` as the stable current window.",
            "Broader interaction-effect and multiview neighborhood models remained explicit boundary branches rather than being forced into ligand-receptor inference.",
        ],
        "active_stable_subtask_window": [
            "Ligand-receptor communication inference",
            "Neighborhood / interaction-effect modeling",
        ],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed equivalent to the SVG or deconvolution benchmarks was identified within the required window.",
        ],
        "review_seeds": [
            "Nat Rev Genet 2021, Integrating single-cell and spatial transcriptomics to elucidate intercellular tissue dynamics.",
            "Nat Rev Genet 2023, The diversification of methods for studying cell-cell interactions and communication.",
            "Decoding cell-cell communication using spatial transcriptomics (PMID 39984677).",
        ],
        "whitelist_results": [
            "Whitelist sweep retained Giotto, SpaOTsc, COMMOT, SpaTalk, SpatialDM, and stLearn as the existing stable ligand-receptor core, and added NicheNet and CellChat as major transcriptomics communication baselines.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems yielded a stable addition under the current ligand-receptor window.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the existing stable core for the ligand-receptor branch.",
        ],
        "direct_results": [
            "Direct gap-filling search did not add a clearly superior new ligand-receptor method beyond the earlier narrow formal pass, while confirming that accepted interaction-effect models now belong in a dedicated CCC subtask.",
            "User-prioritized baseline checks added NicheNet and CellChat as important transcriptomics communication baselines, and later direct checks added CellNEST, STCase, and SPIDER as additional published communication methods.",
            "User-prioritized direct search also added Spacia as a published interaction-effect model that goes beyond ligand-receptor-only inference.",
        ],
        "methods": [
            m(
                "Ligand-receptor communication inference",
                "Spatial neighborhood graph scoring",
                "Giotto",
                "Giotto: a toolbox for integrative analysis and visualization of spatial expression data",
                "10.1186/s13059-021-02286-2",
                "33685491",
                2021,
                "Genome Biology",
                "Review seed",
                "Nat Rev Genet 2021 review + whitelist venue sweep",
                "Yes",
                "https://github.com/RubD/Giotto",
                "CPU",
                "Include",
                notes="Retained as a stable ligand-receptor-compatible core method from the earlier formal pass.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Ligand-target regulatory potential modeling",
                "NicheNet",
                "NicheNet: modeling intercellular communication by linking ligands to target genes",
                "10.1038/s41592-019-0667-5",
                "31819264",
                2020,
                "Nature Methods",
                "Review seed",
                "Nat Rev Genet 2023 review + user-prioritized CCC baseline audit",
                "Yes",
                "https://github.com/saeyslab/nichenetr",
                "CPU",
                "Include",
                notes="Included as a major transcriptomics communication baseline that remains useful for spatial CCC interpretation.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Database-guided communication network inference",
                "CellChat",
                "Inference and analysis of cell-cell communication using CellChat",
                "10.1038/s41467-021-21246-9",
                "33597522",
                2021,
                "Nature Communications",
                "Review seed",
                "Nat Rev Genet 2023 review + user-prioritized CCC baseline audit",
                "Yes",
                "https://github.com/sqjin/CellChat",
                "CPU",
                "Include",
                notes="Included as a widely used communication baseline with strong ecosystem adoption.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Trajectory-aware ligand-receptor scoring",
                "stLearn",
                "Robust mapping of spatiotemporal trajectories and cell-cell interactions in healthy and diseased tissues",
                "10.1038/s41467-023-43120-6",
                "38007580",
                2023,
                "Nature Communications",
                "Direct search",
                "Direct search after review seeding + whitelist venue sweep",
                "Yes",
                "https://github.com/BiomedicalMachineLearning/stLearn",
                "CPU",
                "Include",
                notes="Kept in the stable ligand-receptor window despite known method-family leakage risk.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Optimal transport signaling inference",
                "SpaOTsc",
                "Inferring spatial and signaling relationships between cells from single cell transcriptomic data",
                "10.1038/s41467-020-15968-5",
                "32350282",
                2020,
                "Nature Communications",
                "Review seed",
                "Nat Rev Genet 2021 review",
                "Yes",
                "https://github.com/zcang/SpaOTsc",
                "CPU",
                "Include",
                notes="Early spatial communication method retained in the stable branch.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Collective optimal transport",
                "COMMOT",
                "Screening cell-cell communication in spatial transcriptomics via collective optimal transport",
                "10.1038/s41592-022-01728-4",
                "36690742",
                2023,
                "Nature Methods",
                "Direct search",
                "Direct search after review seeding + whitelist venue sweep",
                "Yes",
                "https://github.com/zcang/COMMOT",
                "CPU",
                "Include",
                notes="Stable whitelist-supported CCC method.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Knowledge graph-based ligand-receptor inference",
                "SpaTalk",
                "Knowledge-graph-based cell-cell communication inference for spatially resolved transcriptomic data with SpaTalk",
                "10.1038/s41467-022-32111-8",
                "35908020",
                2022,
                "Nature Communications",
                "Direct search",
                "Direct search after review seeding + whitelist venue sweep",
                "Yes",
                "https://github.com/ZJUFanLab/SpaTalk",
                "CPU",
                "Include",
                notes="Retained in the stable core with explicit provenance this time.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Spatially co-expressed ligand-receptor analysis",
                "SpatialDM",
                "SpatialDM for rapid identification of spatially co-expressed ligand-receptor and revealing cell-cell communication patterns",
                "10.1038/s41467-023-39608-w",
                "37414760",
                2023,
                "Nature Communications",
                "Direct search",
                "Direct search after review seeding + whitelist venue sweep",
                "Yes",
                "https://github.com/StatBiomed/SpatialDM",
                "CPU",
                "Include",
                notes="Retained as a stable ligand-receptor method despite some earlier method-family leakage concerns.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Graph attention relay-network inference",
                "CellNEST",
                "CellNEST reveals cell-cell relay networks using attention mechanisms on spatial transcriptomics",
                "",
                "",
                2024,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after CCC review and master-registry audit",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Added as a published relay-network communication method absent from the earlier narrow CCC slice.",
            ),
            m(
                "Ligand-receptor communication inference",
                "Subgraph-based graph attention communication inference",
                "STCase",
                "Deciphering cell-cell communication at single-cell resolution for spatial transcriptomics with subgraph-based graph attention network",
                "",
                "",
                2025,
                "Nature Communications",
                "Direct search",
                "User-prioritized direct search after CCC review and master-registry audit",
                "Yes",
                "https://github.com/Lzcstan/STCase",
                "Optional GPU",
                "Include",
                notes="Added because the method is a published single-cell-resolution CCC model and fits the current communication topic cleanly.",
            ),
            m(
                "Spatially variable ligand-receptor interaction inference",
                "Functional-support ligand-receptor interaction inference",
                "SPIDER",
                "Finding spatially variable ligand-receptor interactions with functional support from downstream genes",
                "10.1038/s41467-025-62988-0",
                "",
                2025,
                "Nature Communications",
                "Direct search",
                "User-prioritized ligand-receptor direct search",
                "Yes",
                "https://github.com/deepomicslab/SPIDER",
                "CPU",
                "Include",
                notes="Added as a published spatially variable ligand-receptor interaction method with explicit downstream functional support.",
            ),
            m(
                "Neighborhood / interaction-effect modeling",
                "Multiview interaction modeling",
                "MISTy",
                "Explainable multiview framework for dissecting spatial relationships from highly multiplexed data",
                "10.1186/s13059-022-02663-5",
                "35422018",
                2022,
                "Genome Biology",
                "Review seed",
                "Nat Rev Genet 2023 review",
                "Yes",
                "https://github.com/saezlab/mistyR",
                "CPU",
                "Include",
                notes="Included in the dedicated CCC interaction-effect subtask because multiview neighborhood influence modeling is now accepted in first-layer scope.",
            ),
            m(
                "Neighborhood / interaction-effect modeling",
                "Spatial variance component analysis",
                "SVCA",
                "Modeling Cell-Cell Interactions from Spatial Molecular Data with Spatial Variance Component Analysis",
                "10.1016/j.celrep.2019.08.077",
                "31577949",
                2019,
                "Cell Reports",
                "Review seed",
                "Nat Rev Genet 2023 review",
                "Yes",
                "https://github.com/damienArnol/svca",
                "CPU",
                "Include",
                notes="Included in the dedicated CCC interaction-effect subtask because interaction-variance modeling is now accepted in first-layer scope.",
            ),
            m(
                "Neighborhood / interaction-effect modeling",
                "Bayesian multiple-instance communication inference",
                "Spacia",
                "Mapping cellular interactions from spatially resolved transcriptomics data",
                "10.1038/s41592-024-02408-1",
                "39227721",
                2024,
                "Nature Methods",
                "Direct search",
                "User-prioritized direct search after interaction-modeling branch audit",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Included in the dedicated CCC interaction-effect subtask as a published spatial interaction model beyond ligand-receptor-only inference.",
            ),
        ],
        "label_stable": "Yes. `Cell-Cell Communication` remains a stable top-level analysis problem.",
        "subtask_sufficient": (
            "Yes for the accepted first-layer scope. Ligand-receptor inference and interaction-effect modeling now cover the stable CCC branches."
        ),
        "family_assessment": (
            "Mostly yes, but the same leakage risks noted in the earlier coordinator review remain for stLearn, SpaTalk, and SpatialDM."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the current first-layer CCC scope."
        ),
        "taxonomy_blockers": [],
    },
    {
        "analysis_problem": "Segmentation",
        "slug": "segmentation",
        "run_objective": (
            "Activate segmentation as a formal Round 1 topic and map the current computational core for assigning transcripts to cells in imaging-based spatial transcriptomics."
        ),
        "scope_confirmation": [
            "This pass focused on computational cell segmentation and transcript assignment for imaging-based or subcellular spatial transcriptomics.",
            "General image segmentation tools without a spatial transcriptomics-specific contribution were not treated as primary methods in this topic.",
        ],
        "active_stable_subtask_window": ["Cell segmentation / transcript assignment"],
        "deferred_candidate_subtasks": [
            "Joint segmentation plus annotation",
            "Nucleus-first segmentation transfer learning",
        ],
        "benchmark_seeds": [
            "Impact and correction of segmentation errors in spatial transcriptomics (PMID 41559218), used as a benchmark-like seed for the segmentation error landscape.",
        ],
        "review_seeds": [
            "No dedicated segmentation review with better topic coverage than the benchmark-like error study was identified within the required window.",
        ],
        "whitelist_results": [
            "Whitelist sweep retained Baysor, SCS, and Bering as the stable journal-backed core.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable segmentation core.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the stable whitelist-supported segmentation core.",
        ],
        "direct_results": [
            "Direct search added UCS and segger as newer segmentation candidates, and both were retained in the first-layer registry under the current segmentation scope.",
            "segger was later reconciled into the stable segmentation subtask rather than left in a separate joint segmentation branch.",
        ],
        "methods": [
            m(
                "Cell segmentation / transcript assignment",
                "Bayesian molecule assignment",
                "Baysor",
                "Cell segmentation in imaging-based spatial transcriptomics",
                "",
                "34650268",
                2022,
                "Nature Biotechnology",
                "Direct search",
                "Whitelist venue sweep: Nature Biotechnology + targeted segmentation-method search",
                "Yes",
                "https://github.com/kharchenkolab/Baysor",
                "CPU",
                "Include",
                notes="Canonical imaging-based ST segmentation baseline.",
            ),
            m(
                "Cell segmentation / transcript assignment",
                "Graph-based segmentation",
                "SCS",
                "SCS: cell segmentation for high-resolution spatial transcriptomics",
                "10.1038/s41592-023-01939-3",
                "37429992",
                2023,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted segmentation-method search",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Stable high-resolution segmentation method.",
            ),
            m(
                "Cell segmentation / transcript assignment",
                "Transferred graph embeddings",
                "Bering",
                "Bering: joint cell segmentation and annotation for spatial transcriptomics with transferred graph embeddings",
                "10.1038/s41467-025-60898-9",
                "40681510",
                2025,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + targeted segmentation-method search",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Newer stable segmentation method with strong benchmark evidence.",
            ),
            m(
                "Cell segmentation / transcript assignment",
                "Unified deep segmentation",
                "UCS",
                "UCS: A Unified Approach to Cell Segmentation for Subcellular Spatial Transcriptomics",
                "10.1002/smtd.202400975",
                "39763408",
                2025,
                "Small Methods",
                "Direct search",
                "Direct gap-filling search after whitelist and exception sweeps",
                "Yes",
                "https://github.com/YangLabHKUST/UCS",
                "Optional GPU",
                "Include",
                notes="Promoted under a narrow Benchmark Override after multiple benchmark-like segmentation studies supported same-task inclusion.",
            ),
            m(
                "Cell segmentation / transcript assignment",
                "Graph neural network link prediction",
                "segger",
                "Segger: Fast and accurate cell segmentation of imaging-based spatial transcriptomics data",
                "10.1101/2025.03.14.643160",
                "40161614",
                2025,
                "bioRxiv",
                "Direct search",
                "Direct gap-filling search after whitelist and exception sweeps",
                "Pending",
                "https://github.com/elihei2/segger",
                "Optional GPU",
                "Include",
                notes="Retained as a frontier segmentation method in the stable segmentation subtask after later taxonomy closure, while keeping its preprint and accessibility caveats explicit.",
            ),
        ],
        "label_stable": "Yes. `Segmentation` is stable enough to activate as a Round 1 analysis problem.",
        "subtask_sufficient": (
            "Yes for the current core. `Cell segmentation / transcript assignment` is a stable first-layer subtask."
        ),
        "family_assessment": (
            "Yes. The included method families remained algorithmic and avoided conflating segmentation with annotation."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the stable segmentation core, although frontier preprint methods should remain explicitly flagged as emerging entries."
        ),
        "taxonomy_blockers": [
            "Joint segmentation-plus-annotation methods remain adjacent to Cell Type Inference.",
        ],
    },
    {
        "analysis_problem": "Super-resolution",
        "slug": "super_resolution",
        "run_objective": (
            "Activate super-resolution as a formal Round 1 topic while keeping it distinct from gene prediction and from experimental high-resolution assay design."
        ),
        "scope_confirmation": [
            "This pass targeted computational methods that increase effective spatial resolution or reconstruct denser expression maps from lower-resolution measurements.",
            "Assay papers defining new experimental platforms were not treated as primary methods in this computational topic.",
            "Segmentation-free microscopic-resolution reconstruction methods were also allowed here when their primary practical output was super-resolved tissue architecture rather than segmentation itself.",
        ],
        "active_stable_subtask_window": ["Resolution enhancement of spot-based spatial transcriptomics"],
        "deferred_candidate_subtasks": [
            "Histology-only gene prediction",
            "Experimental platform super-resolution",
        ],
        "benchmark_seeds": [
            "No dedicated super-resolution benchmark seed was identified within the required window.",
        ],
        "review_seeds": [
            "Recent spatial transcriptomics reviews were used to locate this branch, but no dedicated super-resolution review displaced direct venue sweeping as the main indexing path.",
        ],
        "whitelist_results": [
            "Whitelist sweep retained XFuse, TESLA, iStar, and later FICTURE as the clearest journal-backed super-resolution core under the current taxonomy.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable super-resolution core.",
        ],
        "exception_results": [
            "Briefings in Bioinformatics did not add a stronger super-resolution method than the whitelist core for the active window.",
        ],
        "direct_results": [
            "Direct gap-filling search added scstGCN and Spotiphy to complement the stable super-resolution layer.",
            "User-prioritized taxonomy closure later moved FICTURE out of boundary tracking and into the super-resolution topic.",
        ],
        "methods": [
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Deep data fusion",
                "XFuse",
                "Super-resolved spatial transcriptomics by deep data fusion",
                "10.1038/s41587-021-01075-3",
                "34845373",
                2022,
                "Nature Biotechnology",
                "Direct search",
                "Whitelist venue sweep: Nature Biotechnology + targeted super-resolution search",
                "Yes",
                "https://github.com/maaskola/xfuse",
                "Optional GPU",
                "Include",
                notes="Foundational super-resolution method for the topic.",
            ),
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Histology-guided machine learning",
                "TESLA",
                "Deciphering tumor ecosystems at super resolution from spatial transcriptomics with TESLA",
                "10.1016/j.cels.2023.03.008",
                "37164011",
                2023,
                "Cell Systems",
                "Direct search",
                "Whitelist venue sweep: Cell Systems + targeted super-resolution search",
                "Yes",
                "https://github.com/jianhuupenn/TESLA",
                "Optional GPU",
                "Include",
                notes="Stable whitelist-supported super-resolution method for tumor ecosystems.",
            ),
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Hierarchical image feature extraction",
                "iStar",
                "Inferring super-resolution tissue architecture by integrating spatial transcriptomics with histology",
                "10.1038/s41587-023-02019-9",
                "38168986",
                2024,
                "Nature Biotechnology",
                "Direct search",
                "Whitelist venue sweep: Nature Biotechnology + targeted super-resolution search",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Recent stable addition bridging super-resolution and histology-guided prediction.",
            ),
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Segmentation-free spatial factorization",
                "FICTURE",
                "FICTURE: scalable segmentation-free analysis of submicron-resolution spatial transcriptomics",
                "10.1038/s41592-024-02415-2",
                "39266749",
                2024,
                "Nature Methods",
                "Direct search",
                "User-prioritized boundary reassignment after super-resolution taxonomy closure + Nature Methods verification",
                "Yes",
                "https://github.com/seqscope/ficture",
                "CPU",
                "Include",
                notes="Added to super-resolution after taxonomy closure because the method reconstructs microscopic tissue architecture from ultra-high-resolution spatial measurements without relying on cell segmentation.",
            ),
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Vision Transformer plus graph convolution",
                "scstGCN",
                "Inferring single-cell resolution spatial gene expression via fusing spot-based spatial transcriptomics, location, and histology using GCN",
                "",
                "39656774",
                2024,
                "Briefings in Bioinformatics",
                "Direct search",
                "Ecosystem-exception sweep: Briefings in Bioinformatics + targeted super-resolution search",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Added through the ecosystem-exception path to exhaust the current source layers.",
            ),
            m(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Histology-aware pseudo-single-cell reconstruction",
                "Spotiphy",
                "Spotiphy enables single-cell spatial whole transcriptomics across an entire section",
                "10.1038/s41592-025-02622-5",
                "40074951",
                2025,
                "Nature Methods",
                "Direct search",
                "User-prioritized direct search after super-resolution audit",
                "Yes",
                "https://github.com/jyyulab/Spotiphy",
                "Optional GPU",
                "Include",
                notes="Included as a super-resolution method because it reconstructs single-cell-resolved whole-transcriptome maps from section-level ST data.",
            ),
        ],
        "label_stable": "Yes. `Super-resolution` is stable enough to activate as a Round 1 topic.",
        "subtask_sufficient": (
            "Yes for a first-layer computational topic. The current window cleanly captures methods that densify lower-resolution spatial measurements."
        ),
        "family_assessment": (
            "Yes. Method-family labels stayed algorithmic and did not collapse into generic high-resolution language."
        ),
        "revision_needed": (
            "Yes, but only for later promotion policy. The main unresolved issue is how to treat strong methods published outside the current venue whitelist."
        ),
        "taxonomy_blockers": [
            "Several strong methods blur the line between super-resolution and spatial gene prediction.",
        ],
    },
    {
        "analysis_problem": "Spatial Gene Prediction",
        "slug": "spatial_gene_prediction",
        "run_objective": (
            "Activate spatial gene prediction as a formal Round 1 topic and separate it from both cell-type inference and super-resolution."
        ),
        "scope_confirmation": [
            "This pass targeted methods whose primary contribution is predicting unmeasured or spatially missing gene expression patterns from scRNA-seq, histology, or both.",
            "Methods whose primary contribution is deconvolution or pure resolution enhancement were treated as adjacent topics unless their prediction objective was dominant.",
        ],
        "active_stable_subtask_window": ["Gene expression completion / prediction"],
        "deferred_candidate_subtasks": [
            "Histology-only digital pathology prediction",
            "Cross-modal mapping that is better represented under cell placement",
        ],
        "benchmark_seeds": [
            "Benchmarking data integration methods for spatial transcriptomics (PMID 35577954), used because it explicitly compares transcript distribution prediction methods.",
            "Computational benchmarking of translational potential in spatial gene prediction from histology images (PMID 39934114).",
        ],
        "review_seeds": [
            "Strategies and software for integration of spatial transcriptomic and single-cell data (PMID 40568931).",
        ],
        "whitelist_results": [
            "Whitelist sweep retained SpaGE and other prediction-native methods as the clearest core anchors for the current topic.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable prediction core under the current admission rules.",
        ],
        "exception_results": [
            "Briefings in Bioinformatics sweep added Hist2ST and THItoGene as ecosystem-exception prediction methods.",
            "Bioinformatics sweep added stPlus as a reference-based enhancement method adjacent to the stable prediction window.",
        ],
        "direct_results": [
            "User-prioritized direct checks also added SpatialScope, GHIST, TISSUE, and STASCAN to better cover cellular-resolution reconstruction, histology-driven prediction, uncertainty-aware prediction analysis, and fine-resolution spatial completion.",
        ],
        "methods": [
            m(
                "Gene expression completion / prediction",
                "Shared latent-space enhancement",
                "SpaGE",
                "SpaGE: Spatial Gene Enhancement using scRNA-seq",
                "10.1093/nar/gkaa740",
                "32955565",
                2020,
                "Nucleic Acids Research",
                "Direct search",
                "Whitelist venue sweep: Nucleic Acids Research + targeted gene-prediction search",
                "Yes",
                "https://github.com/tabdelaal/SpaGE",
                "CPU",
                "Include",
                notes="Canonical scRNA-seq-assisted spatial gene prediction method.",
            ),
            m(
                "Gene expression completion / prediction",
                "Transformer plus graph neural network prediction",
                "Hist2ST",
                "Spatial transcriptomics prediction from histology jointly through Transformer and graph neural networks",
                "",
                "35849101",
                2022,
                "Briefings in Bioinformatics",
                "Direct search",
                "Ecosystem-exception sweep: Briefings in Bioinformatics + targeted gene-prediction search",
                "Yes",
                "https://github.com/biomed-AI/Hist2ST",
                "Optional GPU",
                "Include",
                notes="Stable ecosystem-exception method for histology-driven gene prediction.",
            ),
            m(
                "Gene expression completion / prediction",
                "Hybrid neural network prediction",
                "THItoGene",
                "THItoGene: a deep learning method for predicting spatial transcriptomics from histological images",
                "10.1093/bib/bbad464",
                "38145948",
                2023,
                "Briefings in Bioinformatics",
                "Direct search",
                "Ecosystem-exception sweep: Briefings in Bioinformatics + targeted gene-prediction search",
                "Yes",
                "https://github.com/yrjia1015/THItoGene",
                "Optional GPU",
                "Include",
                notes="Included to exhaust the image-driven prediction layer beyond Hist2ST.",
            ),
            m(
                "Gene expression completion / prediction",
                "Cellular-resolution transcriptomic reconstruction",
                "SpatialScope",
                "SpatialScope: Spatial transcriptomic reconstruction at cellular level",
                "",
                "",
                2024,
                "Nature Communications",
                "Direct search",
                "Targeted gap-filling search after transcript-distribution benchmark review",
                "Yes",
                "",
                "Optional GPU",
                "Include",
                notes="Added because it is a foundational published method for cellular-resolution reconstruction from spatial transcriptomics.",
            ),
            m(
                "Gene expression completion / prediction",
                "Histology-driven deep prediction",
                "GHIST",
                "Spatial gene expression at single-cell resolution from histology using deep learning with GHIST",
                "10.1038/s41467-024-53174-5",
                "39452475",
                2024,
                "Nature Communications",
                "Direct search",
                "User-prioritized histology-driven prediction search",
                "Yes",
                "https://github.com/SydneyBioX/GHIST",
                "Optional GPU",
                "Include",
                notes="Added as a published histology-only prediction framework that clearly belongs in the spatial gene prediction branch.",
            ),
            m(
                "Gene expression completion / prediction",
                "Uncertainty-calibrated prediction analysis",
                "TISSUE",
                "TISSUE: uncertainty-calibrated prediction of single-cell spatial transcriptomics improves downstream analyses",
                "10.1038/s41592-024-02595-x",
                "39609107",
                2024,
                "Nature Methods",
                "Direct search",
                "User-prioritized prediction-method search after master-registry audit",
                "Yes",
                "",
                "CPU",
                "Include",
                notes="Added because uncertainty-calibrated prediction is a distinct published contribution within the current prediction topic.",
            ),
            m(
                "Gene expression completion / prediction",
                "Multimodal spatial completion",
                "STASCAN",
                "STASCAN deciphers fine-resolution cell distribution maps in spatial transcriptomics by deep learning",
                "10.1186/s13059-024-03421-5",
                "39439006",
                2024,
                "Genome Biology",
                "Direct search",
                "User-prioritized whitelist omission audit after prediction-topic reconciliation",
                "Yes",
                "https://github.com/AbbyWY/STASCAN",
                "Optional GPU",
                "Include",
                notes="Included in the approved prediction branch as a multimodal spatial completion method that refines fine-resolution spatial structure from expression and histology.",
            ),
            m(
                "Gene expression completion / prediction",
                "Reference-based enhancement",
                "stPlus",
                "stPlus: a reference-based method for the accurate enhancement of spatial transcriptomics",
                "10.1093/bioinformatics/btab298",
                "34252941",
                2021,
                "Bioinformatics",
                "Direct search",
                "Ecosystem-exception sweep: Bioinformatics + targeted gene-prediction search",
                "Yes",
                "https://github.com/xy-chen16/stPlus",
                "CPU",
                "Include",
                notes="Included as a reference-based enhancement method that fits the current prediction window better than preprocessing.",
            ),
        ],
        "label_stable": "Yes. `Spatial Gene Prediction` is stable enough as a Round 1 topic.",
        "subtask_sufficient": (
            "Yes for the current expanded run. `Gene expression completion / prediction` captures the main computational objective cleanly."
        ),
        "family_assessment": (
            "Yes. Method-family labels remained methodological and avoided collapsing back into generic integration language."
        ),
        "revision_needed": (
            "Yes for later promotion. The main remaining ambiguity is how to separate prediction-native methods from adjacent super-resolution and mapping-style workflows."
        ),
        "taxonomy_blockers": [
            "Some methods still straddle gene prediction, super-resolution, and mapping.",
        ],
    },
    {
        "analysis_problem": "Spatial Perturbation Analysis",
        "slug": "spatial_perturbation_analysis",
        "run_objective": (
            "Activate spatial perturbation analysis as an advanced Round 1 topic and capture frontier computational methods that model perturbation effects in spatial transcriptomics."
        ),
        "scope_confirmation": [
            "This pass targeted computational methods that analyze or model perturbation effects while preserving spatial context.",
            "General perturbation-screening assays without a reusable computational method were not treated as primary methods.",
        ],
        "active_stable_subtask_window": ["Spatial perturbation-response modeling"],
        "deferred_candidate_subtasks": [
            "Niche-aware perturbation simulation",
            "Cross-tissue perturbation transfer",
        ],
        "benchmark_seeds": [
            "No dedicated spatial-perturbation benchmark seed was identified within the required window.",
        ],
        "review_seeds": [
            "No dedicated spatial-perturbation review specific to spatial transcriptomics was identified within the required window.",
        ],
        "whitelist_results": [
            "Whitelist journal sweeps did not surface a stable, peer-reviewed spatial-perturbation core comparable to the mature topics.",
            "No main-conference paper from International Conference on Learning Representations or Conference on Neural Information Processing Systems entered the stable core under the current rules.",
        ],
        "exception_results": [
            "Ecosystem-exception venue sweeps did not surface a stable peer-reviewed core either.",
        ],
        "direct_results": [
            "Direct gap-filling search surfaced CONCERT as the clearest current computational candidate, and it was retained as a frontier first-layer method under the new topic.",
        ],
        "methods": [
            m(
                "Spatial perturbation-response modeling",
                "Niche-aware generative modeling",
                "CONCERT",
                "CONCERT predicts niche-aware perturbation responses in spatial transcriptomics",
                "10.1101/2025.11.08.686890",
                "41292874",
                2025,
                "bioRxiv",
                "Direct search",
                "Direct gap-filling search after benchmark, review, and venue sweeps found no stable peer-reviewed core",
                "Pending",
                "",
                "Required GPU",
                "Include",
                notes="Included as a frontier spatial-perturbation method despite preprint-only status because the topic is intentionally capturing emerging computational methods.",
            ),
        ],
        "label_stable": (
            "Only partially. `Spatial Perturbation Analysis` is a useful exploratory Round 1 label, but the literature is still too immature for a stable mature-method core."
        ),
        "subtask_sufficient": (
            "No. `Spatial perturbation-response modeling` is a reasonable placeholder, but the current method set is too small and too preprint-heavy for full stability."
        ),
        "family_assessment": (
            "Yes. The recorded candidates stayed methodological, but they remain frontier methods rather than stable entries."
        ),
        "revision_needed": (
            "Yes. This topic should remain explicitly frontier-facing until a larger peer-reviewed core appears."
        ),
        "taxonomy_blockers": [
            "The topic lacks a mature peer-reviewed computational core within the current time window.",
            "Both current candidates remain preprints.",
        ],
    },
]


def build_topic_rows(topic: dict[str, object]) -> list[dict[str, str]]:
    rows = []
    for method in topic["methods"]:
        row = dict(method)
        row["Analysis Problem"] = topic["analysis_problem"]
        rows.append(row)
    return rows


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None documented."


def method_table(rows: list[dict[str, str]], decisions: set[str]) -> str:
    filtered = [row for row in rows if row["Round 1 Decision"] in decisions]
    if not filtered:
        return "No rows recorded.\n"
    lines = [
        "| Method Name | Current Subtask | Method Family | Discovery Route | Operational Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in filtered:
        lines.append(
            f"| {row['Method Name']} | {row['Subtask']} | {row['Method Family']} | {row['Discovery Route']} | {row['Round 1 Decision']} |"
        )
    return "\n".join(lines)


def write_csv(
    path: Path,
    rows: list[dict[str, str]],
    fieldnames: list[str] = SCRATCH_FIELDS,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def topic_order_map() -> dict[str, int]:
    return {topic["analysis_problem"]: index for index, topic in enumerate(TOPICS)}


def sort_authoritative_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    order = topic_order_map()
    return sorted(
        rows,
        key=lambda row: (
            order.get(row["Analysis Problem"], 999),
            row["Subtask"].lower(),
            row["Method Name"].lower(),
        ),
    )


def clean_text(value: str) -> str:
    return " ".join((value or "").split()).strip()


def normalize_evidence_basis_text(value: str) -> str:
    text = clean_text(value).replace("`", "")
    if not text:
        return ""
    for old, new in (
        ("Boundary method: ", ""),
        ("Stable core method", "Core method"),
        ("Stable benchmark-backed", "Benchmark-backed"),
        ("Stable whitelist-supported", "Whitelist-supported"),
        ("Stable ecosystem-exception", "Ecosystem-exception"),
        ("Stable deconvolution", "Deconvolution"),
        ("Stable preprocessing", "Preprocessing"),
        ("Stable overall", "Overall"),
        ("New stable addition", "New addition"),
        ("Strong stable representative", "Strong representative"),
        ("stable preprocessing core", "first-layer preprocessing registry"),
        ("stable deconvolution core", "first-layer deconvolution registry"),
        ("stable ligand-receptor-compatible core method", "ligand-receptor-compatible method"),
        ("stable ligand-receptor method", "ligand-receptor method"),
        ("stable ligand-receptor window", "current ligand-receptor window"),
        ("stable contribution", "primary contribution"),
        ("stable addition", "addition"),
        ("retained in the stable core", "retained in the first-layer registry"),
        ("Retained in the stable core", "Retained in the first-layer registry"),
        ("stable representative", "representative"),
        ("Stable ", ""),
        ("stable ", ""),
        ("stable core", "first-layer registry"),
        ("stable branch", "first-layer registry"),
        ("stable window", "current topic window"),
        ("stable neighborhood core", "current neighborhood registry"),
        ("scratch-only", "first-layer registry"),
        ("pending manual coordinator review", "later coordinator review"),
    ):
        text = text.replace(old, new)
    return clean_text(text)


def build_evidence_basis(row: dict[str, str]) -> str:
    decision = row.get("Round 1 Decision", "")
    exclusion = clean_text(row.get("Exclusion Reason", ""))
    notes = clean_text(row.get("Notes", ""))
    source = clean_text(row.get("Discovery Source", ""))

    if decision == "Pending":
        if source:
            cleaned_source = normalize_evidence_basis_text(source).rstrip(".")
            return f"Included in the first-layer registry from expanded retrieval; {cleaned_source}."
        return "Included in the first-layer registry from expanded retrieval; later taxonomy or policy review may still refine its standing."
    if notes:
        return normalize_evidence_basis_text(notes)
    if exclusion:
        return normalize_evidence_basis_text(exclusion)
    if source:
        return normalize_evidence_basis_text(source)
    return "Included in the first-layer registry from expanded retrieval."


def registry_row_from_scratch(row: dict[str, str]) -> dict[str, str]:
    return {
        "Analysis Problem": row["Analysis Problem"],
        "Subtask": row["Subtask"],
        "Method Name": row["Method Name"],
        "Method Family": row["Method Family"],
        "Primary Ecosystem": "",
        "Title": row["Title"],
        "DOI": row["DOI"],
        "PMID": row["PMID"],
        "Year": row["Year"],
        "Venue": row["Venue"],
        "Discovery Route": row["Discovery Route"],
        "Discovery Source": row["Discovery Source"],
        "Evidence Basis": build_evidence_basis(row),
        "Accessibility": row["Accessibility"],
        "GitHub URL": row["GitHub URL"],
        "Compute Requirement": row["Compute Requirement"],
        "Registry Status": "Include",
        "Notes": row.get("Notes", ""),
    }


def registry_row_from_existing_master(row: dict[str, str]) -> dict[str, str]:
    if "Registry Status" in row:
        return {field: row.get(field, "") for field in MASTER_FIELDS}
    return {
        "Analysis Problem": row["Analysis Problem"],
        "Subtask": row["Subtask"],
        "Method Name": row["Method Name"],
        "Method Family": row["Method Family"],
        "Primary Ecosystem": "",
        "Title": row["Title"],
        "DOI": row["DOI"],
        "PMID": row["PMID"],
        "Year": row["Year"],
        "Venue": row["Venue"],
        "Discovery Route": row["Discovery Route"],
        "Discovery Source": row["Discovery Source"],
        "Evidence Basis": build_evidence_basis(row),
        "Accessibility": row["Accessibility"],
        "GitHub URL": row["GitHub URL"],
        "Compute Requirement": row["Compute Requirement"],
        "Registry Status": "Include" if row.get("Round 1 Decision", "Include") in {"Include", "Pending"} else "Exclude",
        "Notes": row.get("Notes", ""),
    }


def registry_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (row["Analysis Problem"], row["Subtask"], row["Method Name"])


def build_authoritative_rows(
    all_rows: dict[str, list[dict[str, str]]],
    authoritative_csv: Path,
) -> tuple[list[dict[str, str]], dict[str, list[dict[str, str]]]]:
    current_rows = read_csv_rows(authoritative_csv)
    merged: dict[tuple[str, str, str], dict[str, str]] = {}
    skipped_rows: dict[str, list[dict[str, str]]] = {}
    valid_topics = set(topic_order_map())

    for row in current_rows:
        normalized = registry_row_from_existing_master(row)
        if normalized["Registry Status"] == "Include" and normalized["Analysis Problem"] not in valid_topics:
            merged[registry_key(normalized)] = normalized

    for rows in all_rows.values():
        for row in rows:
            decision = row.get("Round 1 Decision", "")
            if decision in {"Include", "Pending"}:
                normalized = registry_row_from_scratch(row)
                merged[registry_key(normalized)] = normalized
            else:
                skipped_rows.setdefault("exclude-not-imported", []).append(dict(row))

    return sort_authoritative_rows(list(merged.values())), skipped_rows


def load_existing_scratch_rows(scratch_root: Path) -> dict[str, list[dict[str, str]]]:
    all_rows: dict[str, list[dict[str, str]]] = {}
    for topic in TOPICS:
        path = scratch_root / f"{RUN_DATE}_{topic['slug']}.csv"
        all_rows[topic["analysis_problem"]] = read_csv_rows(path)
    return all_rows


def boundary_candidates_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        f"# {BOUNDARY_DATE} Boundary Method Candidates",
        "",
        "These methods were reviewed during the first-layer full-registry refresh but were intentionally held out of the master registry because the current first-layer taxonomy would distort their primary contribution.",
        "",
        "## Held-Out Items",
        "",
        "| Method Name | Candidate Analysis Problem | Candidate Subtask | Reason Held Out | Next Action |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['Method Name'] or '(workflow / unnamed)'} | {row['Candidate Analysis Problem']} | {row['Candidate Subtask']} | {row['Reason Held Out']} | {row['Next Action']} |"
        )
    return "\n".join(lines)


def authoritative_report_markdown(
    merged_rows: list[dict[str, str]],
    previous_rows: list[dict[str, str]],
    skipped_rows: dict[str, list[dict[str, str]]],
) -> str:
    previous_norm = [registry_row_from_existing_master(row) for row in previous_rows]
    previous_by_key = {registry_key(row): row for row in previous_norm if row["Registry Status"] == "Include"}
    merged_by_key = {registry_key(row): row for row in merged_rows}

    preserved = sorted(
        key for key in merged_by_key.keys() & previous_by_key.keys()
    )
    added = sorted(
        key for key in merged_by_key.keys() - previous_by_key.keys()
    )
    removed = sorted(
        key for key in previous_by_key.keys() - merged_by_key.keys()
    )

    per_topic = [
        "| Analysis Problem | Rows |",
        "| --- | ---: |",
    ]
    topic_counts = Counter(row["Analysis Problem"] for row in merged_rows)
    for analysis_problem in sorted(
        topic_counts,
        key=lambda topic: topic_order_map().get(topic, 999),
    ):
        per_topic.append(f"| {analysis_problem} | {topic_counts[analysis_problem]} |")

    skip_sections = []
    for reason in sorted(skipped_rows):
        names = ", ".join(
            sorted({f"{row['Analysis Problem']} / {row['Subtask']} / {row['Method Name']}" for row in skipped_rows[reason]})
        )
        skip_sections.append(f"- `{reason}`: {names}")

    duplicates = []
    seen_names: dict[str, list[tuple[str, str]]] = {}
    for row in merged_rows:
        seen_names.setdefault(row["Method Name"], []).append((row["Analysis Problem"], row["Subtask"]))
    for method_name, contexts in sorted(seen_names.items()):
        if len(contexts) > 1:
            ctx = "; ".join(f"{analysis_problem} / {subtask}" for analysis_problem, subtask in contexts)
            duplicates.append(f"- `{method_name}`: {ctx}")

    added_lines = [
        f"- `{analysis_problem} / {subtask} / {method_name}`"
        for analysis_problem, subtask, method_name in added
    ]
    removed_lines = [
        f"- `{analysis_problem} / {subtask} / {method_name}`"
        for analysis_problem, subtask, method_name in removed
    ]

    return f"""# {RUN_DATE} Master Registry Consolidation Report

## Summary

- Previous authoritative rows: {len(previous_rows)}
- Final authoritative rows: {len(merged_rows)}
- Preserved rows: {len(preserved)}
- Added rows: {len(added)}
- Removed rows: {len(removed)}

## Added Rows

{chr(10).join(added_lines) if added_lines else '- No new rows were added.'}

## Removed Rows

{chr(10).join(removed_lines) if removed_lines else '- No prior authoritative rows were removed.'}

## Per-Topic Final Counts

{chr(10).join(per_topic)}

## Methods With Multiple Topic Contexts

{chr(10).join(duplicates) if duplicates else '- No duplicate method names across topic contexts.'}

## Skipped Expanded Rows

{chr(10).join(skip_sections) if skip_sections else '- No expanded rows were skipped.'}
"""


def topic_markdown(topic: dict[str, object], rows: list[dict[str, str]]) -> str:
    return f"""# {topic['analysis_problem']} Retrieval Run

## Run Objective

{topic['run_objective']}

## Scope Confirmation

{bullets(topic['scope_confirmation'])}

## Active Stable Subtask Window

{bullets(topic['active_stable_subtask_window'])}

## Deferred Candidate Subtasks

{bullets(topic['deferred_candidate_subtasks'])}

## Benchmark Seeds Used

{bullets(topic['benchmark_seeds'])}

## Review Seeds Used

{bullets(topic['review_seeds'])}

## Whitelist Venue Sweep Results

{bullets(topic['whitelist_results'])}

## Ecosystem-Exception Venue Sweep Results

{bullets(topic['exception_results'])}

## Direct-Search Supplementation Results

{bullets(topic['direct_results'])}

## Included Methods

{method_table(rows, {"Include"})}

## Pending Boundary Methods

{method_table(rows, {"Pending"})}

## Is The Top-Level Label Stable?

{topic['label_stable']}

## Is The Current Subtask Layer Sufficient?

{topic['subtask_sufficient']}

## Did Method Family Remain Methodological?

{topic['family_assessment']}

## Is Protocol Or Schema Revision Needed Before Formal Promotion?

{topic['revision_needed']}
"""


def summary_markdown(all_rows: dict[str, list[dict[str, str]]]) -> str:
    per_topic_lines = [
        "| Analysis Problem | Total Methods | Include | Pending | Exclude |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    source_lines = [
        "| Analysis Problem | Benchmark seed | Review seed | Direct search |",
        "| --- | ---: | ---: | ---: |",
    ]
    added_lines = []
    blocker_lines = []

    for topic in TOPICS:
        analysis_problem = topic["analysis_problem"]
        rows = all_rows[analysis_problem]
        counts = Counter(row["Round 1 Decision"] for row in rows)
        route_counts = Counter(row["Discovery Route"] for row in rows)
        per_topic_lines.append(
            f"| {analysis_problem} | {len(rows)} | {counts['Include']} | {counts['Pending']} | {counts['Exclude']} |"
        )
        source_lines.append(
            f"| {analysis_problem} | {route_counts['Benchmark seed']} | {route_counts['Review seed']} | {route_counts['Direct search']} |"
        )
        prior = PRIOR_BATCH1_METHODS.get(analysis_problem, set())
        added = [row["Method Name"] for row in rows if row["Method Name"] not in prior]
        if added:
            added_lines.append(f"- `{analysis_problem}`: {', '.join(sorted(dict.fromkeys(added)))}")
        if topic["taxonomy_blockers"] or "Yes." in topic["revision_needed"]:
            blockers = topic["taxonomy_blockers"] or ["Topic still needs manual taxonomy review."]
            blocker_lines.append(f"- `{analysis_problem}`: {'; '.join(blockers)}")

    return f"""# {RUN_DATE} Round 1 Expanded Summary

## Protocol Changes Made At Run Start

{bullets(PROTOCOL_CHANGES)}

## Per-Topic Method Counts

{chr(10).join(per_topic_lines)}

## Source Composition By Topic

{chr(10).join(source_lines)}

## Methods Added Beyond Earlier Pilot And Narrow Batch 1 Runs

{chr(10).join(added_lines) if added_lines else '- No additions beyond earlier pilot artifacts were recorded.'}

## Topics Still Blocked By Taxonomy Gaps

{chr(10).join(blocker_lines) if blocker_lines else '- No material taxonomy blockers remain.'}

## Coordinator Review Readiness

Expanded Round 1 retrieval is complete enough for coordinator review because all 15 topics now have a scratch CSV, a run note, and explicit source-layer documentation.

Authoritative promotion should remain frozen during this run. Partial promotion may be considered only after manual review of mature stable cores such as Spatially Variable Gene Detection, Integration, Domain / Clustering, Cell Type Inference, Segmentation, Super-resolution, Spatial Gene Prediction, Spatial Trajectory Analysis, and Spatial Clonal Analysis.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-root",
        default="/mnt/NAS_21T/ProjectData/BioHarness",
        help="Base output directory for round1_expanded_scratch, round1_runs, and round1_reports.",
    )
    parser.add_argument(
        "--reconcile-authoritative",
        action="store_true",
        help="Rebuild the first-layer NAS master registry from the expanded scratch set.",
    )
    parser.add_argument(
        "--reconcile-from-existing-scratch",
        action="store_true",
        help="When reconciling, load existing scratch CSVs from --out-root instead of regenerating topic outputs from embedded topic definitions.",
    )
    parser.add_argument(
        "--authoritative-csv",
        default=AUTHORITATIVE_CSV,
        help="Master registry CSV path to read and rewrite during consolidation.",
    )
    parser.add_argument(
        "--authoritative-report",
        default=AUTHORITATIVE_REPORT,
        help="Markdown report path for the master-registry consolidation summary.",
    )
    args = parser.parse_args()

    out_root = Path(args.out_root)
    scratch_root = out_root / "round1_expanded_scratch"
    runs_root = out_root / "round1_runs"
    reports_root = out_root / "round1_reports"

    if args.reconcile_from_existing_scratch:
        all_rows = load_existing_scratch_rows(scratch_root)
    else:
        all_rows: dict[str, list[dict[str, str]]] = {}

        for topic in TOPICS:
            rows = build_topic_rows(topic)
            all_rows[topic["analysis_problem"]] = rows
            write_csv(scratch_root / f"{RUN_DATE}_{topic['slug']}.csv", rows)
            write_markdown(
                runs_root / f"{RUN_DATE}_{topic['slug']}.md",
                topic_markdown(topic, rows),
            )

        summary = summary_markdown(all_rows)
        write_markdown(
            reports_root / f"{RUN_DATE}_round1_expanded_summary.md",
            summary,
        )
        write_markdown(
            reports_root / f"{RUN_DATE}_round1_expanded_summary_v2.md",
            summary,
        )

    write_csv(
        scratch_root / f"{BOUNDARY_DATE}_boundary_method_candidates.csv",
        BOUNDARY_CANDIDATES,
        fieldnames=BOUNDARY_FIELDS,
    )
    write_markdown(
        reports_root / f"{BOUNDARY_DATE}_boundary_method_candidates.md",
        boundary_candidates_markdown(BOUNDARY_CANDIDATES),
    )

    if args.reconcile_authoritative:
        authoritative_csv = Path(args.authoritative_csv)
        previous_rows = read_csv_rows(authoritative_csv)
        merged_rows, skipped_rows = build_authoritative_rows(all_rows, authoritative_csv)
        write_csv(authoritative_csv, merged_rows, fieldnames=MASTER_FIELDS)
        write_markdown(
            Path(args.authoritative_report),
            authoritative_report_markdown(merged_rows, previous_rows, skipped_rows),
        )


if __name__ == "__main__":
    main()
