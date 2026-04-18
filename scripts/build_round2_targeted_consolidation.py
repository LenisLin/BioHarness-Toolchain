from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.build_round1_expanded_outputs as registry


RUN_DATE = "2026-04-13"
MAIN_WINDOW = ("2015-01-01", "2026-04-11")
AUTHORITATIVE_CSV = registry.AUTHORITATIVE_CSV
CONSOLIDATION_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-13_round2_consolidation_report.md"
)
ROUND2_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-13_round2_targeted_completion_audit.md"
)


def s(
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
    authoritative_action: str,
    exclusion: str = "",
    notes: str = "",
    replace_analysis_problem: str = "",
    replace_subtask: str = "",
) -> dict[str, str]:
    row = registry.m(
        subtask,
        family,
        name,
        title,
        doi,
        pmid,
        year,
        venue,
        route,
        source,
        access,
        github,
        compute,
        decision,
        exclusion,
        notes,
    )
    row["_authoritative_action"] = authoritative_action
    if replace_analysis_problem:
        row["_replace_analysis_problem"] = replace_analysis_problem
    if replace_subtask:
        row["_replace_subtask"] = replace_subtask
    return row


SUPPLEMENT_TOPICS = [
    {
        "analysis_problem": "Spatial Trajectory Analysis",
        "slug": "spatial_trajectory_analysis",
        "run_objective": (
            "Revisit the sparse trajectory topic under a strict-core policy and only "
            "promote methods whose primary contribution is spatial trajectory or lineage inference."
        ),
        "scope_confirmation": [
            "Strict-core rule applied: broad pseudo-spatiotemporal embedding or toolkit-style methods were not promoted into the authoritative trajectory core.",
            "Boundary or access-limited methods were retained in scratch only as Pending rows.",
        ],
        "active_stable_subtask_window": ["Spatial trajectory inference"],
        "deferred_candidate_subtasks": [
            "Broad pseudo-spatiotemporal ordering",
            "Tri-modality lineage tracing",
        ],
        "benchmark_seeds": [
            "No dedicated benchmark seed for spatial trajectory inference was found in-window.",
        ],
        "review_seeds": [
            "Trajectory-oriented review coverage was weaker than the direct whitelist venue evidence and was used only as an indexing layer.",
        ],
        "whitelist_results": [
            "Cell Systems confirmed SpaTrack as the existing anchor.",
            "Nature Methods added STT.",
            "Genome Biology added spVelo.",
            "Nucleic Acids Research surfaced CASCAT, but it failed consolidation readiness on accessibility/executability grounds.",
            "Nature Communications surfaced SpaceFlow and stLearn, but both failed the chosen strict-core boundary.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the strict-core additions.",
        ],
        "direct_results": [
            "Direct search also surfaced LineageMap, but it remained boundary-heavy because it depends on tri-modality spatial lineage tracing rather than transcriptomics-first trajectory inference alone.",
        ],
        "date_reaudit": [
            "STT published 2024-05-16 (Nature Methods).",
            "spVelo published 2025-08-11 (Genome Biology).",
            "CASCAT published 2025-08-19 (Nucleic Acids Research).",
            "LineageMap preprint posted 2026-01-22; in-window, but not promoted because of topic-boundary issues rather than date uncertainty.",
        ],
        "methods": [
            s(
                "Spatial trajectory inference",
                "Optimal transport trajectory inference",
                "SpaTrack",
                "Inferring cell trajectories of spatial transcriptomics via optimal transport analysis",
                "10.1016/j.cels.2025.101194",
                "39904341",
                2025,
                "Cell Systems",
                "Direct search",
                "Existing authoritative anchor re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/yzf072/spaTrack",
                "CPU",
                "Include",
                "no_change",
                notes="Existing anchor retained; no authoritative writeback needed.",
            ),
            s(
                "Spatial trajectory inference",
                "Multiscale tensor dynamics",
                "STT",
                "Spatial transition tensor of single cells",
                "10.1038/s41592-024-02266-x",
                "38755322",
                2024,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted trajectory-method search",
                "Yes",
                "https://github.com/cliffzhou92/STT",
                "CPU",
                "Include",
                "add",
                notes="Consolidation-ready strict-core trajectory method with public repo, install instructions, and example notebooks.",
            ),
            s(
                "Spatial trajectory inference",
                "Spatial RNA velocity inference",
                "spVelo",
                "spVelo: RNA velocity inference for multi-batch spatial transcriptomics data",
                "10.1186/s13059-025-03701-8",
                "40790237",
                2025,
                "Genome Biology",
                "Direct search",
                "Whitelist venue sweep: Genome Biology + targeted trajectory-method search",
                "Yes",
                "https://github.com/VivLon/spVelo",
                "Optional GPU",
                "Include",
                "add",
                notes="Consolidation-ready trajectory method with explicit install steps and tutorial notebook.",
            ),
            s(
                "Spatial trajectory inference",
                "Tree-shaped structural causal model",
                "CASCAT",
                "Inferring causal trajectories from spatial transcriptomics using CASCAT",
                "10.1093/nar/gkaf791",
                "40829806",
                2025,
                "Nucleic Acids Research",
                "Direct search",
                "Whitelist venue sweep: Nucleic Acids Research + targeted trajectory-method search",
                "Pending",
                "",
                "Optional GPU",
                "Pending",
                "no_change",
                notes="Scientifically strong, but current code availability is a paper-reported deposit rather than a clearly maintained public repository with a stable executable path.",
            ),
            s(
                "Spatial trajectory inference",
                "Spatially constrained manifold learning",
                "SpaceFlow",
                "SpaceFlow: mapping single-cell spatial transcriptome trajectories by deep manifold learning",
                "10.1038/s41467-022-31739-w",
                "35835774",
                2022,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + targeted trajectory-method search",
                "Yes",
                "https://github.com/hongleir3/SpaceFlow",
                "CPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because it fails the chosen strict-core trajectory boundary; pseudo-spatiotemporal ordering is broader than the accepted primary trajectory core.",
            ),
            s(
                "Spatial trajectory inference",
                "Spatial trajectory-aware graph learning",
                "stLearn",
                "Robust mapping of spatiotemporal trajectories and cell-cell interactions in healthy and diseased tissues",
                "10.1038/s41467-023-43120-6",
                "38007580",
                2023,
                "Nature Communications",
                "Direct search",
                "Whitelist venue sweep: Nature Communications + targeted trajectory overlap check",
                "Yes",
                "https://github.com/BiomedicalMachineLearning/stLearn",
                "CPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because trajectory is a module inside a broader toolkit rather than the sole primary contribution.",
            ),
            s(
                "Spatial trajectory inference",
                "Tri-modality lineage-tree inference",
                "LineageMap",
                "Integrative Inference of Spatially Resolved Cell Lineage Trees using LineageMap",
                "10.64898/2026.01.19.700383",
                "41648248",
                2026,
                "bioRxiv",
                "Direct search",
                "Direct gap-filling search after whitelist sweep",
                "Yes",
                "https://github.com/ZhangLabGT/LineageMap",
                "Unclear",
                "Pending",
                "no_change",
                notes="In-window by date, but held in scratch only because the current first-layer trajectory topic would distort its tri-modality lineage-tracing contribution.",
            ),
        ],
        "label_stable": "Yes. `Spatial Trajectory Analysis` remains a stable top-level label.",
        "subtask_sufficient": (
            "Yes for the strict-core consolidation pass. `Spatial trajectory inference` remains sufficient if broader pseudo-time and tri-modality branches stay out of the authoritative core."
        ),
        "family_assessment": (
            "Yes. New consolidated methods remain methodological and keep the topic distinct from domain discovery and generic manifold learning."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed for the strict-core writeback. Broader trajectory-adjacent methods remain scratch-only."
        ),
    },
    {
        "analysis_problem": "Spatial Clonal Analysis",
        "slug": "spatial_clonal_analysis",
        "run_objective": (
            "Revisit the sparse clonal-analysis topic and promote only methods that satisfy venue, accessibility, and topic-fit gates."
        ),
        "scope_confirmation": [
            "This pass kept `Spatial subclone detection` as the stable subtask window.",
            "Methods outside whitelist/ecosystem-exception venues were not promoted without a stronger override basis.",
        ],
        "active_stable_subtask_window": ["Spatial subclone detection"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed for spatial clonal analysis was found in-window.",
        ],
        "review_seeds": [
            "Broader spatial cancer genomics reviews confirmed the ecosystem is small but did not supersede direct method evidence.",
        ],
        "whitelist_results": [
            "Nature Methods re-confirmed Clonalscope and added CalicoST.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the whitelist-supported set.",
        ],
        "direct_results": [
            "Direct gap-filling search retained STARCH as a panorama-level comparator but not a consolidation-ready addition.",
        ],
        "date_reaudit": [
            "CalicoST published 2024-10-30 (Nature Methods).",
        ],
        "methods": [
            s(
                "Spatial subclone detection",
                "Copy-number-based subclone inference",
                "Clonalscope",
                "Cancer subclone detection based on DNA copy number in single-cell and spatial omic sequencing data",
                "10.1038/s41592-025-02773-5",
                "40954304",
                2025,
                "Nature Methods",
                "Direct search",
                "Existing authoritative anchor re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/seasoncloud/Clonalscope",
                "CPU",
                "Include",
                "no_change",
                notes="Existing anchor retained; no authoritative writeback needed.",
            ),
            s(
                "Spatial subclone detection",
                "Allele-specific copy number and phylogeography inference",
                "CalicoST",
                "Inferring allele-specific copy number aberrations and tumor phylogeography from spatially resolved transcriptomics",
                "10.1038/s41592-024-02438-9",
                "39478176",
                2024,
                "Nature Methods",
                "Direct search",
                "Whitelist venue sweep: Nature Methods + targeted clonal-analysis search",
                "Yes",
                "https://github.com/raphael-group/CalicoST",
                "CPU",
                "Include",
                "add",
                notes="Consolidation-ready addition with public repo, install instructions, and tutorials.",
            ),
            s(
                "Spatial subclone detection",
                "Copy-number-driven tumor clone inference",
                "STARCH",
                "STARCH: joint analysis of copy number and spatial transcriptomics for tumor clone reconstruction",
                "10.1088/1478-3975/abbe99",
                "",
                2021,
                "Physical Biology",
                "Direct search",
                "Direct gap-filling search after whitelist and ecosystem-exception sweeps",
                "Yes",
                "https://github.com/raphael-group/STARCH",
                "CPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because the venue path is outside whitelist/ecosystem-exception support and the current evidence does not justify override-based authoritative promotion.",
            ),
        ],
        "label_stable": "Yes. `Spatial Clonal Analysis` remains a stable top-level label.",
        "subtask_sufficient": (
            "Yes. `Spatial subclone detection` remains sufficient for current first-layer consolidation."
        ),
        "family_assessment": (
            "Yes. The new addition stays squarely within clonal-structure inference rather than generic tumor-state analysis."
        ),
        "revision_needed": (
            "No urgent protocol revision is needed."
        ),
    },
    {
        "analysis_problem": "Spatial Perturbation Analysis",
        "slug": "spatial_perturbation_analysis",
        "run_objective": (
            "Re-audit the perturbation topic under strict protocol rules and confirm whether any row is consolidation-ready."
        ),
        "scope_confirmation": [
            "Reusable computational methods were required; assay or workflow papers alone were not treated as primary methods.",
            "This pass preserved uncertainty about ecosystem sparsity and did not pad the topic with workflow papers.",
        ],
        "active_stable_subtask_window": ["Spatial perturbation-response modeling"],
        "deferred_candidate_subtasks": [
            "Workflow-derived perturbation analysis",
            "Cross-tissue perturbation transfer",
        ],
        "benchmark_seeds": [
            "No dedicated benchmark seed was found.",
        ],
        "review_seeds": [
            "No dedicated review seed specific to spatial perturbation-response modeling was found.",
        ],
        "whitelist_results": [
            "Whitelist sweeps did not add a stable peer-reviewed computational core.",
        ],
        "exception_results": [
            "Ecosystem-exception sweeps did not add a stable peer-reviewed computational core either.",
        ],
        "direct_results": [
            "Direct search re-confirmed CONCERT as the clearest named computational candidate.",
            "Workflow papers were re-seen but did not expose a reusable standalone computational method that fit the current topic.",
        ],
        "date_reaudit": [
            "CONCERT preprint posted in 2025; still preprint-only.",
        ],
        "methods": [
            s(
                "Spatial perturbation-response modeling",
                "Niche-aware generative modeling",
                "CONCERT",
                "CONCERT predicts niche-aware perturbation responses in spatial transcriptomics",
                "10.1101/2025.11.08.686890",
                "41292874",
                2025,
                "bioRxiv",
                "Direct search",
                "Direct gap-filling search after benchmark, review, and venue sweeps found no stable peer-reviewed core; 2026-04-13 supplement re-confirmed public code.",
                "Yes",
                "https://github.com/mims-harvard/CONCERT",
                "Required GPU",
                "Pending",
                "update_existing",
                notes="Existing first-layer row retained; GitHub and accessibility metadata now re-confirmed, but the method remains preprint-only and frontier-facing.",
            ),
        ],
        "label_stable": (
            "Only partially. `Spatial Perturbation Analysis` remains a useful exploratory label, but still lacks a mature computational core."
        ),
        "subtask_sufficient": (
            "Only partially. `Spatial perturbation-response modeling` remains a placeholder subtask for a very small, frontier-heavy method pool."
        ),
        "family_assessment": (
            "Yes. The retained candidate remains methodological, but it is frontier-facing and below stable-core maturity."
        ),
        "revision_needed": (
            "No immediate schema change is required for this pass, but the topic should remain under explicit maturity caution."
        ),
    },
    {
        "analysis_problem": "Comparative Analysis",
        "slug": "comparative_analysis",
        "run_objective": (
            "Confirm that the current comparative-analysis core still fits the local rules and re-audit exact date status for 2026 rows."
        ),
        "scope_confirmation": [
            "This pass kept `Spatial differential expression / comparison` as the stable subtask window.",
            "Boundary methods that drift toward between-group SVG or broader atlas comparison were not promoted into new authoritative rows.",
        ],
        "active_stable_subtask_window": ["Spatial differential expression / comparison"],
        "deferred_candidate_subtasks": [
            "Cross-condition niche comparison",
            "Comparative atlas-level alignment",
        ],
        "benchmark_seeds": [
            "SpatialGEE benchmarking paper and comparative-analysis benchmarking remained the main benchmark layer.",
        ],
        "review_seeds": [
            "Differential-expression review coverage was re-used as an indexing layer rather than a stopping rule.",
        ],
        "whitelist_results": [
            "Whitelist support for C-SIDE and Niche-DE remained intact.",
            "Whitelist gap search surfaced SPADE as a boundary method, not a consolidation-ready comparative core addition.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the current core.",
        ],
        "direct_results": [
            "No new stable comparative-analysis method changed the topic map during this pass.",
        ],
        "date_reaudit": [
            "SpatialGEE exact publication date re-confirmed as 2026-02-11, which is inside the current 2026-04-11 cutoff window.",
        ],
        "methods": [
            s(
                "Spatial differential expression / comparison",
                "Cell-type-specific differential expression",
                "C-SIDE",
                "Cell type-specific inference of differential expression in spatial transcriptomics",
                "10.1038/s41592-022-01575-3",
                "36050488",
                2022,
                "Nature Methods",
                "Benchmark seed",
                "Existing authoritative comparative core re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/dmcable/spacexr",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Spatial differential expression / comparison",
                "Niche-differential expression",
                "Niche-DE",
                "Niche-DE: niche-differential gene expression analysis in spatial transcriptomics data identifies context-dependent cell-cell interactions",
                "10.1186/s13059-023-03159-6",
                "38217002",
                2024,
                "Genome Biology",
                "Direct search",
                "Existing authoritative comparative core re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Spatial differential expression / comparison",
                "Generalized estimating equation differential analysis",
                "SpatialGEE",
                "A comparative study of statistical methods for identifying differentially expressed genes in spatial transcriptomics",
                "10.1371/journal.pcbi.1013956",
                "41671295",
                2026,
                "PLOS Computational Biology",
                "Benchmark seed",
                "Existing authoritative row exact-date re-audited on 2026-04-13 and confirmed as 2026-02-11 within the current window.",
                "Yes",
                "https://github.com/pwei101/SpatialGEE",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained; no corrective writeback needed after exact-date re-audit.",
            ),
            s(
                "Spatial differential expression / comparison",
                "Between-group spatial pattern analysis",
                "SPADE",
                "Spatial pattern and differential expression analysis with spatial transcriptomic data",
                "",
                "39470725",
                2024,
                "Nucleic Acids Research",
                "Direct search",
                "Whitelist venue sweep: Nucleic Acids Research + targeted comparative-analysis gap search",
                "Yes",
                "https://github.com/thecailab/SPADE",
                "CPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because its primary contribution sits closer to between-group spatial pattern / SVG analysis than to the current stable comparative-analysis core.",
            ),
        ],
        "label_stable": "Only partially. `Comparative Analysis` remains broader than the current stable method core.",
        "subtask_sufficient": (
            "Yes for the current first-layer core. `Spatial differential expression / comparison` remains the accepted stable subtask window."
        ),
        "family_assessment": (
            "Yes. The current included methods remain methodological and the boundary method is clearly documented as such."
        ),
        "revision_needed": (
            "No immediate writeback beyond exact-date re-audit is needed."
        ),
    },
    {
        "analysis_problem": "Program Discovery",
        "slug": "program_discovery",
        "run_objective": (
            "Confirm that the current program-discovery core still satisfies the narrow first-layer definition and hold boundary-heavy methods in scratch only."
        ),
        "scope_confirmation": [
            "This pass kept `Multicellular / program discovery` narrow and did not absorb tissue-module or broader end-to-end modeling methods into the authoritative core.",
            "Boundary methods were retained in scratch only when promotion would distort the current taxonomy.",
        ],
        "active_stable_subtask_window": ["Multicellular / program discovery"],
        "deferred_candidate_subtasks": [
            "Tissue module discovery",
            "Segmentation-free tissue representation",
            "Broader community discovery",
        ],
        "benchmark_seeds": [
            "No dedicated benchmark seed for program discovery was found.",
        ],
        "review_seeds": [
            "Review coverage was used only as an indexing layer for factor and multicellular-state methods.",
        ],
        "whitelist_results": [
            "The existing authoritative core of DIALOGUE, scITD, CellPie, and SPICEMIX remained coherent under the narrow definition.",
            "Whitelist gap search surfaced BayesTME and SPACE as boundary methods rather than core additions.",
        ],
        "exception_results": [
            "Genome Medicine surfaced STModule as a useful boundary method but not a consolidation-ready core addition.",
        ],
        "direct_results": [
            "No new clean program-discovery core addition was found after applying the current narrow taxonomy.",
        ],
        "date_reaudit": [],
        "methods": [
            s(
                "Multicellular / program discovery",
                "Coordinated latent program modeling",
                "DIALOGUE",
                "DIALOGUE maps multicellular programs in tissue from single-cell or spatial transcriptomics data",
                "10.1038/s41587-022-01288-0",
                "35513526",
                2022,
                "Nature Biotechnology",
                "Direct search",
                "Existing authoritative row re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/livnatje/DIALOGUE",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Multicellular / program discovery",
                "Interpretable tensor decomposition",
                "scITD",
                "Coordinated, multicellular patterns of transcriptional variation that stratify patient cohorts are revealed by tensor decomposition",
                "10.1038/s41587-024-02411-z",
                "39313646",
                2025,
                "Nature Biotechnology",
                "Direct search",
                "Existing authoritative row re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/kharchenkolab/scITD",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Multicellular / program discovery",
                "Probabilistic latent variable modeling",
                "SPICEMIX",
                "SPICEMIX enables integrative single-cell spatial modeling of cell identity",
                "10.1038/s41588-022-01256-z",
                "36624346",
                2023,
                "Nature Genetics",
                "Review seed",
                "Existing authoritative row re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "https://github.com/ma-compbio/SpiceMix",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Multicellular / program discovery",
                "Joint non-negative matrix factorization",
                "CellPie",
                "CellPie: a scalable spatial transcriptomics factor discovery method via joint non-negative matrix factorization",
                "10.1093/nar/gkaf251",
                "40167331",
                2025,
                "Nucleic Acids Research",
                "Direct search",
                "Existing authoritative row re-confirmed during 2026-04-13 supplement review",
                "Yes",
                "",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Multicellular / program discovery",
                "End-to-end Bayesian spatial modeling",
                "BayesTME",
                "BayesTME: An end-to-end method for multiscale spatial transcriptional profiling of the tissue microenvironment",
                "10.1016/j.cels.2023.06.003",
                "37473731",
                2023,
                "Cell Systems",
                "Direct search",
                "Whitelist venue sweep: Cell Systems + targeted program-discovery boundary search",
                "Yes",
                "https://github.com/tansey-lab/bayestme",
                "CPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because the method is broader than the current narrow program-discovery definition and would blur deconvolution, spatial programs, and community outputs.",
            ),
            s(
                "Multicellular / program discovery",
                "Bayesian tissue module discovery",
                "STModule",
                "STModule: identifying tissue modules to uncover spatial components and characteristics of transcriptomic landscapes",
                "10.1186/s13073-025-01441-9",
                "40033360",
                2025,
                "Genome Medicine",
                "Direct search",
                "Targeted ecosystem-adjacent search after whitelist program-discovery review",
                "Yes",
                "https://github.com/rwang-z/STModule",
                "Optional GPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because it behaves more like tissue-module discovery than a clean multicellular-program core addition under the current taxonomy.",
            ),
            s(
                "Multicellular / program discovery",
                "Interaction-aware cell embedding",
                "SPACE",
                "Tissue module discovery in single-cell-resolution spatial transcriptomics data via cell-cell interaction-aware cell embedding",
                "10.1016/j.cels.2024.05.001",
                "38823396",
                2024,
                "Cell Systems",
                "Direct search",
                "Whitelist venue sweep: Cell Systems + targeted program-discovery boundary search",
                "Pending",
                "",
                "Optional GPU",
                "Pending",
                "no_change",
                notes="Held in scratch only because it is closer to tissue-module and community discovery than to the current narrow program-discovery core.",
            ),
        ],
        "label_stable": "Yes. `Program Discovery` remains a usable top-level analysis problem.",
        "subtask_sufficient": (
            "Yes for the current narrow core, but later expansion would still need a second-pass taxonomy review."
        ),
        "family_assessment": (
            "Yes. The authoritative core remains methodological and narrower than the surrounding boundary methods."
        ),
        "revision_needed": (
            "No immediate authoritative writeback beyond scratch-only boundary documentation is needed."
        ),
    },
    {
        "analysis_problem": "Segmentation",
        "slug": "segmentation",
        "run_objective": (
            "Close the remaining segger taxonomy question by keeping it in Segmentation and moving it into the stable segmentation subtask."
        ),
        "scope_confirmation": [
            "segger remains a segmentation method, not a super-resolution method.",
            "The method is now mapped to the stable segmentation subtask rather than a separate joint segmentation branch.",
        ],
        "active_stable_subtask_window": ["Cell segmentation / transcript assignment"],
        "deferred_candidate_subtasks": [
            "Joint segmentation plus annotation",
        ],
        "benchmark_seeds": [
            "No new benchmark seed was needed for this taxonomy-closure pass.",
        ],
        "review_seeds": [
            "No new review seed was needed for this taxonomy-closure pass.",
        ],
        "whitelist_results": [
            "No whitelist result changed the earlier segmentation evidence base.",
        ],
        "exception_results": [
            "No ecosystem-exception result changed the earlier segmentation evidence base.",
        ],
        "direct_results": [
            "segger remains in Segmentation after manual taxonomy closure and is no longer treated as a super-resolution candidate.",
        ],
        "date_reaudit": [],
        "methods": [
            s(
                "Cell segmentation / transcript assignment",
                "Graph neural network link prediction",
                "segger",
                "Segger: Fast and accurate cell segmentation of imaging-based spatial transcriptomics data",
                "10.1101/2025.03.14.643160",
                "40161614",
                2025,
                "bioRxiv",
                "Direct search",
                "2026-04-13 taxonomy closure kept segger in Segmentation and moved it into the stable segmentation subtask.",
                "Pending",
                "https://github.com/elihei2/segger",
                "Optional GPU",
                "Pending",
                "replace_existing",
                notes="Retained as a frontier segmentation method while keeping its preprint and accessibility caveats explicit.",
                replace_analysis_problem="Segmentation",
                replace_subtask="Joint segmentation plus annotation",
            ),
        ],
        "label_stable": "Yes. `Segmentation` remains a stable top-level topic and segger now follows that stable subtask mapping.",
        "subtask_sufficient": (
            "Yes. `Cell segmentation / transcript assignment` remains the stable first-layer subtask for this pass."
        ),
        "family_assessment": (
            "Yes. segger remains methodological and no longer needs a separate subtask for this taxonomy closure."
        ),
        "revision_needed": (
            "No urgent schema revision is needed; this pass closes a placement decision rather than expanding the segmentation taxonomy."
        ),
    },
    {
        "analysis_problem": "Super-resolution",
        "slug": "super_resolution",
        "run_objective": (
            "Close the FICTURE boundary question by placing it in Super-resolution under the existing stable subtask."
        ),
        "scope_confirmation": [
            "FICTURE is treated as a super-resolution method in this pass.",
            "The method is forced into the existing stable super-resolution subtask by explicit taxonomy decision rather than by creating a new subtask.",
        ],
        "active_stable_subtask_window": ["Resolution enhancement of spot-based spatial transcriptomics"],
        "deferred_candidate_subtasks": [],
        "benchmark_seeds": [
            "No dedicated benchmark seed was needed for this taxonomy-closure pass.",
        ],
        "review_seeds": [
            "No dedicated review seed was needed for this taxonomy-closure pass.",
        ],
        "whitelist_results": [
            "Nature Methods verification confirmed FICTURE as a whitelist-venue method under the user-directed super-resolution placement.",
        ],
        "exception_results": [
            "No ecosystem-exception venue result was needed for this placement.",
        ],
        "direct_results": [
            "FICTURE was removed from boundary tracking and promoted into the super-resolution topic after manual taxonomy closure.",
        ],
        "date_reaudit": [
            "FICTURE published 2024-09-19 (Nature Methods).",
        ],
        "methods": [
            s(
                "Resolution enhancement of spot-based spatial transcriptomics",
                "Segmentation-free spatial factorization",
                "FICTURE",
                "FICTURE: scalable segmentation-free analysis of submicron-resolution spatial transcriptomics",
                "10.1038/s41592-024-02415-2",
                "39266749",
                2024,
                "Nature Methods",
                "Direct search",
                "2026-04-13 taxonomy closure moved FICTURE from boundary tracking into Super-resolution after Nature Methods and GitHub re-verification.",
                "Yes",
                "https://github.com/seqscope/ficture",
                "CPU",
                "Include",
                "add",
                notes="Promoted from boundary tracking into Super-resolution after manual taxonomy closure.",
            ),
        ],
        "label_stable": "Yes. `Super-resolution` remains stable and now explicitly absorbs FICTURE.",
        "subtask_sufficient": (
            "Yes for this pass. The existing stable super-resolution subtask is being used as the accepted landing place for FICTURE."
        ),
        "family_assessment": (
            "Yes. FICTURE is still represented methodologically even under the forced existing subtask."
        ),
        "revision_needed": (
            "No immediate subtask expansion is required because the placement is now closed by manual taxonomy decision."
        ),
    },
]


def strip_meta(row: dict[str, str]) -> dict[str, str]:
    return {field: row.get(field, "") for field in registry.SCRATCH_FIELDS}


def build_topic_rows(topic: dict[str, object]) -> list[dict[str, str]]:
    rows = []
    for method in topic["methods"]:
        row = dict(method)
        row["Analysis Problem"] = topic["analysis_problem"]
        rows.append(row)
    return rows


def build_all_rows() -> dict[str, list[dict[str, str]]]:
    return {
        topic["analysis_problem"]: build_topic_rows(topic)
        for topic in SUPPLEMENT_TOPICS
    }


def topic_supplement_markdown(topic: dict[str, object], rows: list[dict[str, str]]) -> str:
    decisions = [
        "| Method Name | Operational Status | Authoritative Action |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        decisions.append(
            f"| {row['Method Name']} | {row['Round 1 Decision']} | {row['_authoritative_action']} |"
        )
    return f"""# {RUN_DATE} {topic['analysis_problem']} Supplement Note

## Run Objective

{topic['run_objective']}

## Scope Confirmation

{registry.bullets(topic['scope_confirmation'])}

## Active Stable Subtask Window

{registry.bullets(topic['active_stable_subtask_window'])}

## Deferred Candidate Subtasks

{registry.bullets(topic['deferred_candidate_subtasks'])}

## Benchmark Seeds Used

{registry.bullets(topic['benchmark_seeds'])}

## Review Seeds Used

{registry.bullets(topic['review_seeds'])}

## Whitelist Venue Sweep Results

{registry.bullets(topic['whitelist_results'])}

## Ecosystem-Exception Venue Sweep Results

{registry.bullets(topic['exception_results'])}

## Direct-Search Supplementation Results

{registry.bullets(topic['direct_results'])}

## Exact-Date Re-Audit

{registry.bullets(topic['date_reaudit'])}

## Included Methods

{registry.method_table(rows, {"Include"})}

## Pending Boundary Methods

{registry.method_table(rows, {"Pending"})}

## Consolidation Decisions

{chr(10).join(decisions)}

## Is The Top-Level Label Stable?

{topic['label_stable']}

## Is The Current Subtask Layer Sufficient?

{topic['subtask_sufficient']}

## Did Method Family Remain Methodological?

{topic['family_assessment']}

## Is Protocol Or Schema Revision Needed Before Formal Promotion?

{topic['revision_needed']}
"""


def round2_report_markdown(all_rows: dict[str, list[dict[str, str]]]) -> str:
    per_topic = [
        "| Analysis Problem | Total Rows | Include | Pending | Exclude |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    date_lines = [
        "- `SpatialGEE` exact publication date re-confirmed as 2026-02-11; in-window, no corrective writeback required.",
        "- `LineageMap` exact preprint posting date re-confirmed as 2026-01-22; in-window, but still held out because of topic-boundary issues.",
        "- `FICTURE` exact publication date re-confirmed as 2024-09-19; whitelist venue and public code were both re-confirmed before promotion.",
    ]
    ready_lines = []
    held_lines = []

    for topic in SUPPLEMENT_TOPICS:
        rows = all_rows[topic["analysis_problem"]]
        counts = Counter(row["Round 1 Decision"] for row in rows)
        per_topic.append(
            f"| {topic['analysis_problem']} | {len(rows)} | {counts['Include']} | {counts['Pending']} | {counts['Exclude']} |"
        )
        for row in rows:
            action = row["_authoritative_action"]
            label = f"`{topic['analysis_problem']} / {row['Subtask']} / {row['Method Name']}`"
            if action in {"add", "update_existing", "replace_existing"}:
                ready_lines.append(f"- {label}: `{action}`")
            elif row["Round 1 Decision"] == "Pending":
                held_lines.append(f"- {label}: {row['Notes']}")

    return f"""# {RUN_DATE} Round-2 Targeted Completion Audit (NAS Copy)

## Summary

- This NAS report replaces the temporary local audit draft and keeps all consolidation-facing evidence outside `docs/`.
- Strict defaults applied in this pass:
  - `Strict Protocol`
  - `Strict Core`
  - `Re-audit First`
- No authoritative CSV rebuild was attempted until the supplement scratch CSVs and supplement notes were prepared.

## Per-Topic Supplement Counts

{chr(10).join(per_topic)}

## Consolidation-Ready Actions

{chr(10).join(ready_lines) if ready_lines else '- No consolidation-ready actions recorded.'}

## Held-Out Or Scratch-Only Evidence

{chr(10).join(held_lines) if held_lines else '- No held-out evidence recorded.'}

## Exact-Date Re-Audit Results

{chr(10).join(date_lines)}

## Protocol-Compliance Check

- Temporary audit content has been migrated to NAS artifacts.
- Authoritative CSV writeback in this pass is limited to:
  - adding `STT`
  - adding `spVelo`
  - adding `CalicoST`
  - adding `FICTURE`
  - moving `segger` into the stable segmentation subtask
  - updating `CONCERT` metadata if and only if current supplement evidence re-confirms public code and accessibility.
- `CASCAT`, `SpaceFlow`, `stLearn`, `STARCH`, `SPADE`, `BayesTME`, `STModule`, `SPACE`, and `LineageMap` remain outside authoritative writeback in this pass.
"""


def merge_supplement_into_authoritative(
    current_rows: list[dict[str, str]],
    supplement_rows: list[dict[str, str]],
) -> tuple[
    list[dict[str, str]],
    list[tuple[str, str, str]],
    list[tuple[str, str, str]],
    list[tuple[str, str, str]],
    list[tuple[str, str, str, str]],
]:
    merged = {
        registry.registry_key(registry.registry_row_from_existing_master(row)): registry.registry_row_from_existing_master(row)
        for row in current_rows
    }
    added: list[tuple[str, str, str]] = []
    updated: list[tuple[str, str, str]] = []
    moved: list[tuple[str, str, str]] = []
    skipped: list[tuple[str, str, str, str]] = []

    for row in supplement_rows:
        action = row.get("_authoritative_action", "no_change")
        if action == "no_change":
            continue
        normalized = registry.registry_row_from_scratch(row)
        key = registry.registry_key(normalized)
        exists = key in merged
        if action == "add":
            merged[key] = normalized
            if exists:
                updated.append(key)
            else:
                added.append(key)
        elif action == "update_existing":
            if exists:
                merged[key] = normalized
                updated.append(key)
            else:
                skipped.append((*key, "missing-existing-row"))
        elif action == "replace_existing":
            replace_analysis_problem = row.get("_replace_analysis_problem", normalized["Analysis Problem"])
            replace_subtask = row.get("_replace_subtask", "")
            replace_candidates = [
                existing_key
                for existing_key in list(merged)
                if existing_key[0] == replace_analysis_problem
                and existing_key[2] == normalized["Method Name"]
                and (not replace_subtask or existing_key[1] == replace_subtask)
            ]
            if not replace_candidates:
                skipped.append((*key, "missing-replaced-row"))
                continue
            for existing_key in replace_candidates:
                if existing_key != key:
                    del merged[existing_key]
            merged[key] = normalized
            moved.append(key)
        else:
            skipped.append((*key, f"unknown-action:{action}"))

    return registry.sort_authoritative_rows(list(merged.values())), added, updated, moved, skipped


def consolidation_report_markdown(
    merged_rows: list[dict[str, str]],
    previous_rows: list[dict[str, str]],
    added: list[tuple[str, str, str]],
    updated: list[tuple[str, str, str]],
    moved: list[tuple[str, str, str]],
    skipped: list[tuple[str, str, str, str]],
) -> str:
    topic_counts = Counter(row["Analysis Problem"] for row in merged_rows)
    per_topic = [
        "| Analysis Problem | Rows |",
        "| --- | ---: |",
    ]
    for analysis_problem in sorted(topic_counts, key=lambda topic: registry.topic_order_map().get(topic, 999)):
        per_topic.append(f"| {analysis_problem} | {topic_counts[analysis_problem]} |")

    added_lines = [
        f"- `{analysis_problem} / {subtask} / {method_name}`"
        for analysis_problem, subtask, method_name in added
    ]
    updated_lines = [
        f"- `{analysis_problem} / {subtask} / {method_name}`"
        for analysis_problem, subtask, method_name in updated
    ]
    skipped_lines = [
        f"- `{analysis_problem} / {subtask} / {method_name}`: {reason}"
        for analysis_problem, subtask, method_name, reason in skipped
    ]

    return f"""# {RUN_DATE} Round-2 Consolidation Report

## Summary

- Previous authoritative rows: {len(previous_rows)}
- Final authoritative rows: {len(merged_rows)}
- Added rows: {len(added)}
- Updated rows: {len(updated)}
- Moved rows: {len(moved)}
- Removed rows: 0

## Added Rows

{chr(10).join(added_lines) if added_lines else '- No new rows were added.'}

## Updated Existing Rows

{chr(10).join(updated_lines) if updated_lines else '- No existing rows were updated.'}

## Moved Rows

{chr(10).join(f"- `{analysis_problem} / {subtask} / {method_name}`" for analysis_problem, subtask, method_name in moved) if moved else '- No existing rows were moved.'}

## Skipped Actions

{chr(10).join(skipped_lines) if skipped_lines else '- No merge actions were skipped.'}

## Per-Topic Final Counts

{chr(10).join(per_topic)}
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
        help="Overlay the approved round-2 supplement changes onto the authoritative master registry.",
    )
    parser.add_argument(
        "--authoritative-csv",
        default=AUTHORITATIVE_CSV,
        help="Master registry CSV path to read and rewrite during consolidation.",
    )
    parser.add_argument(
        "--consolidation-report",
        default=CONSOLIDATION_REPORT,
        help="Markdown report path for the round-2 reconciliation summary.",
    )
    parser.add_argument(
        "--round2-report",
        default=ROUND2_REPORT,
        help="Markdown report path for the NAS copy of the round-2 audit summary.",
    )
    args = parser.parse_args()

    out_root = Path(args.out_root)
    scratch_root = out_root / "round1_expanded_scratch"
    runs_root = out_root / "round1_runs"
    reports_root = out_root / "round1_reports"

    all_rows = build_all_rows()
    for topic in SUPPLEMENT_TOPICS:
        rows = all_rows[topic["analysis_problem"]]
        registry.write_csv(
            scratch_root / f"{RUN_DATE}_{topic['slug']}.csv",
            [strip_meta(row) for row in rows],
        )
        registry.write_markdown(
            runs_root / f"{RUN_DATE}_{topic['slug']}_supplement.md",
            topic_supplement_markdown(topic, rows),
        )

    registry.write_markdown(
        Path(args.round2_report),
        round2_report_markdown(all_rows),
    )
    registry.write_csv(
        scratch_root / f"{registry.BOUNDARY_DATE}_boundary_method_candidates.csv",
        registry.BOUNDARY_CANDIDATES,
        fieldnames=registry.BOUNDARY_FIELDS,
    )
    registry.write_markdown(
        reports_root / f"{registry.BOUNDARY_DATE}_boundary_method_candidates.md",
        registry.boundary_candidates_markdown(registry.BOUNDARY_CANDIDATES),
    )

    if args.reconcile_authoritative:
        authoritative_csv = Path(args.authoritative_csv)
        previous_rows = registry.read_csv_rows(authoritative_csv)
        flat_rows = [row for rows in all_rows.values() for row in rows]
        merged_rows, added, updated, moved, skipped = merge_supplement_into_authoritative(
            previous_rows,
            flat_rows,
        )
        registry.write_csv(authoritative_csv, merged_rows, fieldnames=registry.MASTER_FIELDS)
        registry.write_markdown(
            Path(args.consolidation_report),
            consolidation_report_markdown(
                merged_rows,
                previous_rows,
                added,
                updated,
                moved,
                skipped,
            ),
        )


if __name__ == "__main__":
    main()
