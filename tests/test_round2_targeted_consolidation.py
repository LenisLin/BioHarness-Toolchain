import scripts.build_round1_expanded_outputs as registry
import scripts.build_round2_targeted_consolidation as supplement


def master_row(
    analysis_problem: str,
    subtask: str,
    method_name: str,
    method_family: str,
    title: str,
    doi: str,
    pmid: str,
    year: str,
    venue: str,
    discovery_route: str,
    discovery_source: str,
    evidence_basis: str,
    accessibility: str,
    github_url: str,
    compute: str,
) -> dict[str, str]:
    return {
        "Analysis Problem": analysis_problem,
        "Subtask": subtask,
        "Method Name": method_name,
        "Method Family": method_family,
        "Primary Ecosystem": "",
        "Title": title,
        "DOI": doi,
        "PMID": pmid,
        "Year": year,
        "Venue": venue,
        "Discovery Route": discovery_route,
        "Discovery Source": discovery_source,
        "Evidence Basis": evidence_basis,
        "Accessibility": accessibility,
        "GitHub URL": github_url,
        "Compute Requirement": compute,
        "Registry Status": "Include",
        "Notes": "",
    }


def supplement_rows():
    all_rows = supplement.build_all_rows()
    return [row for rows in all_rows.values() for row in rows]


def test_round2_topics_and_actions_are_encoded():
    topic_names = [topic["analysis_problem"] for topic in supplement.SUPPLEMENT_TOPICS]

    assert topic_names == [
        "Spatial Trajectory Analysis",
        "Spatial Clonal Analysis",
        "Spatial Perturbation Analysis",
        "Comparative Analysis",
        "Program Discovery",
        "Segmentation",
        "Super-resolution",
    ]

    rows = supplement_rows()
    actions = {
        (row["Analysis Problem"], row["Method Name"]): row["_authoritative_action"]
        for row in rows
    }

    assert actions[("Spatial Trajectory Analysis", "STT")] == "add"
    assert actions[("Spatial Trajectory Analysis", "spVelo")] == "add"
    assert actions[("Spatial Clonal Analysis", "CalicoST")] == "add"
    assert actions[("Spatial Perturbation Analysis", "CONCERT")] == "update_existing"
    assert actions[("Spatial Trajectory Analysis", "CASCAT")] == "no_change"
    assert actions[("Comparative Analysis", "SpatialGEE")] == "no_change"
    assert actions[("Segmentation", "segger")] == "replace_existing"
    assert actions[("Super-resolution", "FICTURE")] == "add"
    assert ("Spatial Perturbation Analysis", "SpatialProp") not in actions


def test_round2_merge_only_adds_and_updates_intended_rows():
    current_rows = [
        master_row(
            "Spatial Trajectory Analysis",
            "Spatial trajectory inference",
            "SpaTrack",
            "Optimal transport trajectory inference",
            "Inferring cell trajectories of spatial transcriptomics via optimal transport analysis",
            "10.1016/j.cels.2025.101194",
            "39904341",
            "2025",
            "Cell Systems",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/yzf072/spaTrack",
            "CPU",
        ),
        master_row(
            "Spatial Clonal Analysis",
            "Spatial subclone detection",
            "Clonalscope",
            "Copy-number-based subclone inference",
            "Cancer subclone detection based on DNA copy number in single-cell and spatial omic sequencing data",
            "10.1038/s41592-025-02773-5",
            "40954304",
            "2025",
            "Nature Methods",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/seasoncloud/Clonalscope",
            "CPU",
        ),
        master_row(
            "Spatial Perturbation Analysis",
            "Spatial perturbation-response modeling",
            "CONCERT",
            "Niche-aware generative modeling",
            "CONCERT predicts niche-aware perturbation responses in spatial transcriptomics",
            "10.1101/2025.11.08.686890",
            "41292874",
            "2025",
            "bioRxiv",
            "Direct search",
            "Existing row",
            "Existing row",
            "Pending",
            "",
            "Required GPU",
        ),
        master_row(
            "Comparative Analysis",
            "Spatial differential expression / comparison",
            "SpatialGEE",
            "Generalized estimating equation differential analysis",
            "A comparative study of statistical methods for identifying differentially expressed genes in spatial transcriptomics",
            "10.1371/journal.pcbi.1013956",
            "41671295",
            "2026",
            "PLOS Computational Biology",
            "Benchmark seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/pwei101/SpatialGEE",
            "CPU",
        ),
        master_row(
            "Domain / Clustering",
            "Spatial domain identification",
            "BANKSY",
            "Neighborhood-kernel clustering",
            "BANKSY unifies cell typing and tissue domain segmentation for scalable spatial omics data analysis",
            "10.1038/s41588-024-01664-3",
            "38413725",
            "2024",
            "Nature Genetics",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/prabhakarlab/Banksy_py",
            "CPU",
        ),
        master_row(
            "Segmentation",
            "Joint segmentation plus annotation",
            "segger",
            "Graph neural network link prediction",
            "Segger: Fast and accurate cell segmentation of imaging-based spatial transcriptomics data",
            "10.1101/2025.03.14.643160",
            "40161614",
            "2025",
            "bioRxiv",
            "Direct search",
            "Existing row",
            "Existing row",
            "Pending",
            "https://github.com/elihei2/segger",
            "Optional GPU",
        ),
    ]

    merged_rows, added, updated, moved, skipped = supplement.merge_supplement_into_authoritative(
        current_rows,
        supplement_rows(),
    )

    keys = {
        (row["Analysis Problem"], row["Subtask"], row["Method Name"])
        for row in merged_rows
    }
    names = {row["Method Name"] for row in merged_rows}
    concert = next(row for row in merged_rows if row["Method Name"] == "CONCERT")

    assert ("Spatial Trajectory Analysis", "Spatial trajectory inference", "STT") in keys
    assert ("Spatial Trajectory Analysis", "Spatial trajectory inference", "spVelo") in keys
    assert ("Spatial Clonal Analysis", "Spatial subclone detection", "CalicoST") in keys
    assert (
        "Super-resolution",
        "Resolution enhancement of spot-based spatial transcriptomics",
        "FICTURE",
    ) in keys
    assert (
        "Segmentation",
        "Cell segmentation / transcript assignment",
        "segger",
    ) in keys
    assert (
        "Segmentation",
        "Joint segmentation plus annotation",
        "segger",
    ) not in keys

    assert "CASCAT" not in names
    assert "SpaceFlow" not in names
    assert "stLearn" not in {
        row["Method Name"]
        for row in merged_rows
        if row["Analysis Problem"] == "Spatial Trajectory Analysis"
    }
    assert "STARCH" not in names
    assert "SPADE" not in names
    assert "BayesTME" not in names

    assert concert["Accessibility"] == "Yes"
    assert concert["GitHub URL"] == "https://github.com/mims-harvard/CONCERT"

    assert ("Spatial Trajectory Analysis", "Spatial trajectory inference", "STT") in added
    assert ("Spatial Trajectory Analysis", "Spatial trajectory inference", "spVelo") in added
    assert ("Spatial Clonal Analysis", "Spatial subclone detection", "CalicoST") in added
    assert (
        "Super-resolution",
        "Resolution enhancement of spot-based spatial transcriptomics",
        "FICTURE",
    ) in added
    assert ("Spatial Perturbation Analysis", "Spatial perturbation-response modeling", "CONCERT") in updated
    assert (
        "Segmentation",
        "Cell segmentation / transcript assignment",
        "segger",
    ) in moved
    assert skipped == []


def test_strip_meta_returns_scratch_schema_only():
    row = supplement.s(
        "Spatial trajectory inference",
        "Multiscale tensor dynamics",
        "STT",
        "Spatial transition tensor of single cells",
        "10.1038/s41592-024-02266-x",
        "38755322",
        2024,
        "Nature Methods",
        "Direct search",
        "Whitelist venue sweep",
        "Yes",
        "https://github.com/cliffzhou92/STT",
        "CPU",
        "Include",
        "add",
        notes="Consolidation-ready.",
    )
    row["Analysis Problem"] = "Spatial Trajectory Analysis"

    stripped = supplement.strip_meta(row)

    assert set(stripped) == set(registry.SCRATCH_FIELDS)
    assert stripped["Method Name"] == "STT"
    assert "_authoritative_action" not in stripped
