from pathlib import Path

import scripts.build_round1_expanded_outputs as registry


def build_all_rows():
    return {
        topic["analysis_problem"]: registry.build_topic_rows(topic)
        for topic in registry.TOPICS
    }


def build_authoritative_rows(tmp_path):
    rows, skipped = registry.build_authoritative_rows(
        build_all_rows(),
        tmp_path / "authoritative.csv",
    )
    return rows, skipped


def test_round1_taxonomy_updates_are_encoded():
    topic_names = [topic["analysis_problem"] for topic in registry.TOPICS]

    assert len(topic_names) == 15
    assert "Spatial Trajectory Analysis" in topic_names
    assert "Spatial Clonal Analysis" in topic_names

    named_boundary_methods = {
        row["Method Name"] for row in registry.BOUNDARY_CANDIDATES if row["Method Name"]
    }

    assert "FICTURE" not in named_boundary_methods
    assert "SpaTrack" not in named_boundary_methods
    assert "Clonalscope" not in named_boundary_methods
    assert "STMiner" not in named_boundary_methods
    assert "STANDS" not in named_boundary_methods
    assert "TACIT" not in named_boundary_methods
    assert "cellAdmix" not in named_boundary_methods


def test_authoritative_rows_match_final_merge_decisions(tmp_path):
    rows, skipped = build_authoritative_rows(tmp_path)
    keys = {
        (row["Analysis Problem"], row["Subtask"], row["Method Name"])
        for row in rows
    }
    method_names = {row["Method Name"] for row in rows}
    rows_by_name = {}
    for row in rows:
        rows_by_name.setdefault(row["Method Name"], []).append(row)

    assert ("Spatial Trajectory Analysis", "Spatial trajectory inference", "SpaTrack") in keys
    assert ("Spatial Clonal Analysis", "Spatial subclone detection", "Clonalscope") in keys
    assert (
        "Spatially Variable Gene Detection",
        "Gene-centric tissue pattern mining",
        "STMiner",
    ) in keys
    assert ("Cell Type Inference", "Cell type deconvolution", "STdGCN") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "SiGra") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "ADEPT") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "ConGI") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "SpaceFlow") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "conST") in keys
    assert (
        "Spatial Gene Prediction",
        "Gene expression completion / prediction",
        "STASCAN",
    ) in keys

    assert (
        "Spatially Variable Gene Detection",
        "Cell-type-specific SVG detection",
        "STANCE",
    ) in keys
    assert (
        "Spatially Variable Gene Detection",
        "Cell-type-specific SVG detection",
        "ctSVG",
    ) in keys
    assert (
        "Spatially Variable Gene Detection",
        "Cell-type-specific SVG detection",
        "Celina",
    ) in keys
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
    assert ("Domain / Clustering", "Spatial domain identification", "PROST") in keys
    assert ("Domain / Clustering", "Spatial domain identification", "Pianno") in keys
    assert ("Cell Type Inference", "Cell type deconvolution", "Tangram") in keys
    assert ("Cell Type Inference", "Cell type deconvolution", "CytoSPACE") in keys
    assert (
        "Cell-Cell Communication",
        "Neighborhood / interaction-effect modeling",
        "MISTy",
    ) in keys
    assert (
        "Cell-Cell Communication",
        "Neighborhood / interaction-effect modeling",
        "SVCA",
    ) in keys
    assert (
        "Cell-Cell Communication",
        "Neighborhood / interaction-effect modeling",
        "Spacia",
    ) in keys

    assert ("Domain / Clustering", "Spatial domain identification", "BANKSY") in keys
    assert (
        sum(
            row["Analysis Problem"] == "Domain / Clustering"
            and row["Subtask"] == "Spatial domain identification"
            for row in rows
        )
        == 27
    )
    assert sum(row["Method Name"] == "BANKSY" for row in rows) == 1
    assert (
        "Spatial Gene Prediction",
        "Gene expression completion / prediction",
        "Tangram",
    ) not in keys
    assert (
        "Segmentation",
        "Joint segmentation plus annotation",
        "segger",
    ) not in keys
    assert len(rows) == 131
    assert len(method_names) == 125

    for removed_method in {
        "SpaDCN",
        "spRefine",
        "saSpatial",
        "Spatial mixed models",
        "SuperST",
        "TACIT",
        "STANDS",
        "cellAdmix",
        "stImage",
        "SpatialProp",
    }:
        assert removed_method not in method_names

    expected_github_urls = {
        "ADEPT": "https://github.com/maiziezhoulab/ADEPT",
        "ConGI": "https://github.com/biomed-AI/ConGI",
        "GHIST": "https://github.com/SydneyBioX/GHIST",
        "Niche-DE": "https://github.com/kaishumason/NicheDE",
        "SPADE": "https://github.com/thecailab/SPADE",
        "SPIDER": "https://github.com/deepomicslab/SPIDER",
        "SpaceFlow": "https://github.com/hongleir/SpaceFlow",
        "STCC": "https://github.com/hucongcong97/STCC",
        "STCase": "https://github.com/Lzcstan/STCase",
        "SMART": "https://github.com/yyolanda/SMART",
        "SpotGF": "https://github.com/illuminate6060/SpotGF",
        "UCS": "https://github.com/YangLabHKUST/UCS",
        "conST": "https://github.com/ys-zong/conST",
        "stPlus": "https://github.com/xy-chen16/stPlus",
        "Redeconve": "https://github.com/ZxZhou4150/Redeconve",
    }
    for method_name, github_url in expected_github_urls.items():
        assert rows_by_name[method_name][0]["GitHub URL"] == github_url

    assert rows_by_name["STCC"][0]["Accessibility"] == "Yes"

    assert skipped == {}


def test_baseline_authority_doc_reflects_current_round1_state():
    baseline = Path("docs/15_round1_baseline_and_round2_prep.md").read_text()

    assert "15 analysis problems" in baseline
    assert "first-layer overview registry" in baseline
    assert "Round 1 inclusion does not imply round2 core candidacy" in baseline
    assert "tool substrate" in baseline
    assert "8-topic" in baseline
    assert "stable-core-only" in baseline
    assert "STT" in baseline
    assert "segger" in baseline

    summary = registry.summary_markdown(build_all_rows())
    assert "all 15 topics now have a scratch CSV" in summary
