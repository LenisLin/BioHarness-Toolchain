import csv
import subprocess
import sys

import scripts.build_round2_nep_benchmark_update as nep


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
    all_rows = nep.build_all_rows()
    return [row for rows in all_rows.values() for row in rows]


def test_nep_benchmark_topics_and_actions_are_encoded():
    topic_names = [topic["analysis_problem"] for topic in nep.SUPPLEMENT_TOPICS]

    assert topic_names == ["Cell-Cell Communication"]

    rows = supplement_rows()
    actions = {
        (row["Analysis Problem"], row["Method Name"]): row["_authoritative_action"]
        for row in rows
    }

    assert actions[("Cell-Cell Communication", "Giotto")] == "no_change"
    assert actions[("Cell-Cell Communication", "MISTy")] == "no_change"
    assert actions[("Cell-Cell Communication", "COZI")] == "add"


def test_nep_benchmark_merge_adds_cozi_before_spider():
    current_rows = [
        master_row(
            "Cell-Cell Communication",
            "Ligand-receptor communication inference",
            "Giotto",
            "Spatial neighborhood graph scoring",
            "Giotto: a toolbox for integrative analysis and visualization of spatial expression data",
            "10.1186/s13059-021-02286-2",
            "33685491",
            "2021",
            "Genome Biology",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/RubD/Giotto",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "MISTy",
            "Multiview interaction modeling",
            "Explainable multiview framework for dissecting spatial relationships from highly multiplexed data",
            "10.1186/s13059-022-02663-5",
            "35422018",
            "2022",
            "Genome Biology",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/saezlab/mistyR",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "Spacia",
            "Bayesian multiple-instance communication inference",
            "Mapping cellular interactions from spatially resolved transcriptomics data",
            "10.1038/s41592-024-02408-1",
            "39227721",
            "2024",
            "Nature Methods",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "SVCA",
            "Spatial variance component analysis",
            "Modeling Cell-Cell Interactions from Spatial Molecular Data with Spatial Variance Component Analysis",
            "10.1016/j.celrep.2019.08.077",
            "31577949",
            "2019",
            "Cell Reports",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/damienArnol/svca",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Spatially variable ligand-receptor interaction inference",
            "SPIDER",
            "Functional-support ligand-receptor interaction inference",
            "Finding spatially variable ligand-receptor interactions with functional support from downstream genes",
            "10.1038/s41467-025-62988-0",
            "",
            "2025",
            "Nature Communications",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/deepomicslab/SPIDER",
            "CPU",
        ),
        master_row(
            "Preprocessing",
            "Denoising / artifact correction",
            "SpotClean",
            "Probabilistic contamination correction",
            "SpotClean adjusts for spot swapping in spatial transcriptomics data",
            "10.1038/s41467-022-30587-y",
            "35624112",
            "2022",
            "Nature Communications",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/zijianni/SpotClean",
            "CPU",
        ),
    ]

    merged_rows, added, updated, moved, skipped = nep.merge_supplement_into_authoritative(
        current_rows,
        supplement_rows(),
    )

    ccc_rows = [row for row in merged_rows if row["Analysis Problem"] == "Cell-Cell Communication"]
    ccc_names = [row["Method Name"] for row in ccc_rows]

    assert len(merged_rows) == 7
    assert len(ccc_rows) == 6
    assert ccc_names == [
        "Giotto",
        "MISTy",
        "Spacia",
        "SVCA",
        "COZI",
        "SPIDER",
    ]
    assert (
        "Cell-Cell Communication",
        "Neighborhood / interaction-effect modeling",
        "COZI",
    ) in added
    assert updated == []
    assert moved == []
    assert skipped == []


def test_nep_benchmark_main_writes_outputs(tmp_path):
    out_root = tmp_path / "nas"
    authoritative_csv = tmp_path / "authoritative.csv"
    round2_report = tmp_path / "round2_report.md"
    consolidation_report = tmp_path / "consolidation_report.md"

    current_rows = [
        master_row(
            "Cell-Cell Communication",
            "Ligand-receptor communication inference",
            "Giotto",
            "Spatial neighborhood graph scoring",
            "Giotto: a toolbox for integrative analysis and visualization of spatial expression data",
            "10.1186/s13059-021-02286-2",
            "33685491",
            "2021",
            "Genome Biology",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/RubD/Giotto",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "MISTy",
            "Multiview interaction modeling",
            "Explainable multiview framework for dissecting spatial relationships from highly multiplexed data",
            "10.1186/s13059-022-02663-5",
            "35422018",
            "2022",
            "Genome Biology",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/saezlab/mistyR",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "Spacia",
            "Bayesian multiple-instance communication inference",
            "Mapping cellular interactions from spatially resolved transcriptomics data",
            "10.1038/s41592-024-02408-1",
            "39227721",
            "2024",
            "Nature Methods",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Neighborhood / interaction-effect modeling",
            "SVCA",
            "Spatial variance component analysis",
            "Modeling Cell-Cell Interactions from Spatial Molecular Data with Spatial Variance Component Analysis",
            "10.1016/j.celrep.2019.08.077",
            "31577949",
            "2019",
            "Cell Reports",
            "Review seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/damienArnol/svca",
            "CPU",
        ),
        master_row(
            "Cell-Cell Communication",
            "Spatially variable ligand-receptor interaction inference",
            "SPIDER",
            "Functional-support ligand-receptor interaction inference",
            "Finding spatially variable ligand-receptor interactions with functional support from downstream genes",
            "10.1038/s41467-025-62988-0",
            "",
            "2025",
            "Nature Communications",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/deepomicslab/SPIDER",
            "CPU",
        ),
    ]

    authoritative_csv.parent.mkdir(parents=True, exist_ok=True)
    with authoritative_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(current_rows[0].keys()))
        writer.writeheader()
        writer.writerows(current_rows)

    subprocess.run(
        [
            sys.executable,
            "scripts/build_round2_nep_benchmark_update.py",
            "--out-root",
            str(out_root),
            "--reconcile-authoritative",
            "--authoritative-csv",
            str(authoritative_csv),
            "--round2-report",
            str(round2_report),
            "--consolidation-report",
            str(consolidation_report),
        ],
        check=True,
    )

    scratch_csv = out_root / "round1_expanded_scratch" / "2026-04-16_cell_cell_communication.csv"
    supplement_note = out_root / "round1_runs" / "2026-04-16_cell_cell_communication_supplement.md"

    assert scratch_csv.exists()
    assert supplement_note.exists()
    assert round2_report.exists()
    assert consolidation_report.exists()

    with authoritative_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    ccc_names = [
        row["Method Name"] for row in rows if row["Analysis Problem"] == "Cell-Cell Communication"
    ]
    assert ccc_names == [
        "Giotto",
        "MISTy",
        "Spacia",
        "SVCA",
        "COZI",
        "SPIDER",
    ]

    ccc_by_name = {
        row["Method Name"]: row for row in rows if row["Analysis Problem"] == "Cell-Cell Communication"
    }
    assert ccc_by_name["COZI"]["Method Family"] == "Conditional z-score neighbor preference analysis"
    assert ccc_by_name["COZI"]["Venue"] == "Nature Communications"
    assert ccc_by_name["COZI"]["GitHub URL"] == "https://github.com/SchapiroLabor/coziR"

    report_text = round2_report.read_text(encoding="utf-8")
    assert "Squidpy" in report_text
    assert "Scimap" in report_text
    assert "IMCRtools" in report_text
    assert "histoCAT" in report_text
    assert "SEA" in report_text
