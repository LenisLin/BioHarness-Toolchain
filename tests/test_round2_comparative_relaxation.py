import csv
import subprocess
import sys
from pathlib import Path

import scripts.build_round2_comparative_relaxation as relaxation


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
    all_rows = relaxation.build_all_rows()
    return [row for rows in all_rows.values() for row in rows]


def test_comparative_relaxation_topics_and_actions_are_encoded():
    topic_names = [topic["analysis_problem"] for topic in relaxation.SUPPLEMENT_TOPICS]

    assert topic_names == ["Comparative Analysis"]

    rows = supplement_rows()
    actions = {
        (row["Analysis Problem"], row["Method Name"]): row["_authoritative_action"]
        for row in rows
    }

    assert actions[("Comparative Analysis", "C-SIDE")] == "no_change"
    assert actions[("Comparative Analysis", "Niche-DE")] == "no_change"
    assert actions[("Comparative Analysis", "SpatialGEE")] == "no_change"
    assert actions[("Comparative Analysis", "SPADE")] == "add"
    assert actions[("Comparative Analysis", "STcompare")] == "add"


def test_comparative_relaxation_merge_adds_spade_and_stcompare():
    current_rows = [
        master_row(
            "Comparative Analysis",
            "Spatial differential expression / comparison",
            "C-SIDE",
            "Cell-type-specific differential expression",
            "Cell type-specific inference of differential expression in spatial transcriptomics",
            "10.1038/s41592-022-01575-3",
            "36050488",
            "2022",
            "Nature Methods",
            "Benchmark seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/dmcable/spacexr",
            "CPU",
        ),
        master_row(
            "Comparative Analysis",
            "Spatial differential expression / comparison",
            "Niche-DE",
            "Niche-differential expression",
            "Niche-DE: niche-differential gene expression analysis in spatial transcriptomics data identifies context-dependent cell-cell interactions",
            "10.1186/s13059-023-03159-6",
            "38217002",
            "2024",
            "Genome Biology",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/kaishumason/NicheDE",
            "CPU",
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

    merged_rows, added, updated, moved, skipped = relaxation.merge_supplement_into_authoritative(
        current_rows,
        supplement_rows(),
    )

    comparative_rows = [
        row for row in merged_rows if row["Analysis Problem"] == "Comparative Analysis"
    ]
    comparative_names = [row["Method Name"] for row in comparative_rows]

    assert len(merged_rows) == 6
    assert len(comparative_rows) == 5
    assert comparative_names == [
        "C-SIDE",
        "Niche-DE",
        "SpatialGEE",
        "SPADE",
        "STcompare",
    ]
    assert (
        "Comparative Analysis",
        "Spatial differential expression / comparison",
        "SPADE",
    ) in added
    assert (
        "Comparative Analysis",
        "Spatial differential expression / comparison",
        "STcompare",
    ) in added
    assert updated == []
    assert moved == []
    assert skipped == []


def test_comparative_relaxation_main_writes_outputs(tmp_path):
    out_root = tmp_path / "nas"
    authoritative_csv = tmp_path / "authoritative.csv"
    round2_report = tmp_path / "round2_report.md"
    consolidation_report = tmp_path / "consolidation_report.md"

    current_rows = [
        master_row(
            "Comparative Analysis",
            "Spatial differential expression / comparison",
            "C-SIDE",
            "Cell-type-specific differential expression",
            "Cell type-specific inference of differential expression in spatial transcriptomics",
            "10.1038/s41592-022-01575-3",
            "36050488",
            "2022",
            "Nature Methods",
            "Benchmark seed",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/dmcable/spacexr",
            "CPU",
        ),
        master_row(
            "Comparative Analysis",
            "Spatial differential expression / comparison",
            "Niche-DE",
            "Niche-differential expression",
            "Niche-DE: niche-differential gene expression analysis in spatial transcriptomics data identifies context-dependent cell-cell interactions",
            "10.1186/s13059-023-03159-6",
            "38217002",
            "2024",
            "Genome Biology",
            "Direct search",
            "Existing row",
            "Existing row",
            "Yes",
            "https://github.com/kaishumason/NicheDE",
            "CPU",
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
    ]

    authoritative_csv.parent.mkdir(parents=True, exist_ok=True)
    with authoritative_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(current_rows[0].keys()))
        writer.writeheader()
        writer.writerows(current_rows)

    subprocess.run(
        [
            sys.executable,
            "scripts/build_round2_comparative_relaxation.py",
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

    scratch_csv = out_root / "round1_expanded_scratch" / "2026-04-15_comparative_analysis.csv"
    supplement_note = out_root / "round1_runs" / "2026-04-15_comparative_analysis_supplement.md"

    assert scratch_csv.exists()
    assert supplement_note.exists()
    assert round2_report.exists()
    assert consolidation_report.exists()

    with authoritative_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    comparative_names = [
        row["Method Name"] for row in rows if row["Analysis Problem"] == "Comparative Analysis"
    ]
    assert comparative_names == [
        "C-SIDE",
        "Niche-DE",
        "SpatialGEE",
        "SPADE",
        "STcompare",
    ]

    scratch_rows = list(csv.DictReader(scratch_csv.open(newline="", encoding="utf-8")))
    scratch_by_name = {row["Method Name"]: row for row in scratch_rows}
    assert scratch_by_name["SPADE"]["Round 1 Decision"] == "Include"
    assert scratch_by_name["STcompare"]["Round 1 Decision"] == "Include"
