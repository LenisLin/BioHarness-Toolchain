from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.build_round1_expanded_outputs as registry


RUN_DATE = "2026-04-15"
MAIN_WINDOW = ("2015-01-01", "2026-04-11")
AUTHORITATIVE_CSV = registry.AUTHORITATIVE_CSV
ROUND2_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-15_round2_comparative_relaxation_report.md"
)
CONSOLIDATION_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-15_round2_comparative_relaxation_consolidation_report.md"
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
    return row


SUPPLEMENT_TOPICS = [
    {
        "analysis_problem": "Comparative Analysis",
        "slug": "comparative_analysis",
        "run_objective": (
            "Apply the user-approved comparative branch relaxation so that dedicated "
            "between-group spatial pattern methods can enter the authoritative first-layer registry."
        ),
        "scope_confirmation": [
            "The accepted subtask label remains `Spatial differential expression / comparison`.",
            "Within that subtask, `Between-group spatial pattern analysis` is now an admissible methodological branch when a method has a dedicated comparative scope and a public executable code path.",
            "This pass keeps the existing comparative core and only promotes methods justified by the relaxed branch rule.",
        ],
        "active_stable_subtask_window": ["Spatial differential expression / comparison"],
        "deferred_candidate_subtasks": [
            "Cross-condition niche comparison",
            "Comparative atlas-level alignment",
        ],
        "benchmark_seeds": [
            "SpatialGEE benchmarking paper remained the benchmark anchor for the comparative topic.",
        ],
        "review_seeds": [
            "Differential-expression review coverage was retained as a background indexing layer rather than a stopping rule.",
        ],
        "whitelist_results": [
            "Whitelist support for C-SIDE and Niche-DE remained intact.",
            "SPADE is now admitted because the relaxed branch explicitly includes peer-reviewed between-group spatial pattern analysis inside the comparative window.",
        ],
        "exception_results": [
            "No ecosystem-exception venue method displaced the current comparative set.",
        ],
        "direct_results": [
            "User-prioritized follow-up added STcompare as a public-code comparative spatial-pattern method for structurally matched tissues.",
            "STcompare remains preprint-only, so its first-layer admission depends on the explicit branch relaxation rather than on whitelist promotion.",
        ],
        "date_reaudit": [
            "SPADE PubMed record PMID 39470725 confirms a 2024-11-27 Nucleic Acids Research publication date.",
            "STcompare package site and GitHub repository citation both report bioRxiv 2025.11.21.689847 with DOI 10.1101/2025.11.21.689847.",
            "No PubMed PMID was found for STcompare as of 2026-04-15, so its metadata is anchored to package-site and repository citation text rather than PubMed indexing.",
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
                "Existing authoritative comparative core retained during 2026-04-15 branch-relaxation review",
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
                "Existing authoritative comparative core retained during 2026-04-15 branch-relaxation review",
                "Yes",
                "https://github.com/kaishumason/NicheDE",
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
                "Existing authoritative comparative core retained during 2026-04-15 branch-relaxation review",
                "Yes",
                "https://github.com/pwei101/SpatialGEE",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Spatial differential expression / comparison",
                "Between-group spatial pattern analysis",
                "SPADE",
                "Spatial pattern and differential expression analysis with spatial transcriptomic data",
                "10.1093/nar/gkae962",
                "39470725",
                2024,
                "Nucleic Acids Research",
                "Direct search",
                "Existing comparative boundary row promoted after the user-approved branch relaxation",
                "Yes",
                "https://github.com/thecailab/SPADE",
                "CPU",
                "Include",
                "add",
                notes="Admitted after the comparative branch was expanded to include between-group spatial pattern analysis; peer-reviewed Nucleic Acids Research method with public code.",
            ),
            s(
                "Spatial differential expression / comparison",
                "Between-group spatial pattern analysis",
                "STcompare",
                "STcompare: Comparative spatial transcriptomics data analysis to characterize differentially spatially patterned genes in structurally matched tissues",
                "10.1101/2025.11.21.689847",
                "",
                2025,
                "bioRxiv",
                "Direct search",
                "User-prioritized comparative-admission follow-up after branch relaxation",
                "Yes",
                "https://github.com/JEFworks-Lab/STcompare",
                "CPU",
                "Include",
                "add",
                notes="Admitted under the relaxed comparative branch as a public-code method focused on differential spatial pattern comparison across matched tissues; current evidence remains preprint-based.",
            ),
        ],
        "label_stable": (
            "More stable than before. `Comparative Analysis` still spans several methodological branches, but "
            "between-group spatial pattern analysis is now an explicit in-scope branch rather than an undocumented boundary case."
        ),
        "subtask_sufficient": (
            "Yes for the current first-layer registry. The existing subtask label still works as long as the method family clearly distinguishes mean-shift, niche-aware, GEE-style, and spatial-pattern branches."
        ),
        "family_assessment": (
            "Yes. The admitted methods remain methodological, and the branch relaxation is documented through explicit method-family labels rather than through a vague topic expansion."
        ),
        "revision_needed": (
            "No schema revision is required, but future comparative additions should explicitly state whether they contribute cell-type-specific differential expression, niche-differential expression, generalized differential analysis, or between-group spatial pattern analysis."
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
    ready_lines = []
    date_lines = []

    for topic in SUPPLEMENT_TOPICS:
        rows = all_rows[topic["analysis_problem"]]
        counts = Counter(row["Round 1 Decision"] for row in rows)
        per_topic.append(
            f"| {topic['analysis_problem']} | {len(rows)} | {counts['Include']} | {counts['Pending']} | {counts['Exclude']} |"
        )
        for row in rows:
            if row["_authoritative_action"] == "add":
                ready_lines.append(
                    f"- `{topic['analysis_problem']} / {row['Subtask']} / {row['Method Name']}`: `add`"
                )
        for line in topic["date_reaudit"]:
            date_lines.append(f"- {line}")

    return f"""# {RUN_DATE} Round-2 Comparative Relaxation Report

## Summary

- This NAS report records a user-approved relaxation of the comparative-analysis admission boundary.
- Historical 2026-04-11 and 2026-04-13 artifacts remain unchanged; this pass is an additive 2026-04-15 overlay.
- The admitted comparative branch now explicitly includes dedicated between-group spatial pattern methods with public code.

## Per-Topic Supplement Counts

{chr(10).join(per_topic)}

## Authoritative Writeback Actions

{chr(10).join(ready_lines) if ready_lines else '- No authoritative writeback actions recorded.'}

## Evidence Re-Audit Notes

{chr(10).join(date_lines)}

## Critical-Evidence Caveat

- `SPADE` is supported by a peer-reviewed, PubMed-indexed Nucleic Acids Research article plus public code.
- `STcompare` has public package documentation and repository code, but its current evidence base remains preprint-only and not PubMed-indexed as of 2026-04-15.
- This makes the comparative expansion scientifically explicit rather than silent: one promoted method is peer-reviewed, while the other is admitted under a documented first-layer policy relaxation with an explicit evidence caveat.

## Protocol-Compliance Check

- No CSV schema changes were introduced.
- The accepted subtask label remains `Spatial differential expression / comparison`.
- Authoritative writeback in this pass is limited to adding `SPADE` and `STcompare`.
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
    normalized_current = [
        registry.registry_row_from_existing_master(row)
        for row in current_rows
    ]
    merged = {
        registry.registry_key(row): row
        for row in normalized_current
    }
    added: list[tuple[str, str, str]] = []
    updated: list[tuple[str, str, str]] = []
    moved: list[tuple[str, str, str]] = []
    skipped: list[tuple[str, str, str, str]] = []
    ordered_new_keys: list[tuple[str, str, str]] = []

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
                ordered_new_keys.append(key)
        else:
            skipped.append((*key, f"unknown-action:{action}"))

    ordered_keys = [registry.registry_key(row) for row in normalized_current]
    target_problem = SUPPLEMENT_TOPICS[0]["analysis_problem"]
    last_topic_index = max(
        (idx for idx, key in enumerate(ordered_keys) if key[0] == target_problem),
        default=-1,
    )
    if ordered_new_keys:
        insertion_index = last_topic_index + 1 if last_topic_index >= 0 else len(ordered_keys)
        ordered_keys[insertion_index:insertion_index] = ordered_new_keys

    seen: set[tuple[str, str, str]] = set()
    ordered_rows: list[dict[str, str]] = []
    for key in ordered_keys:
        if key in seen:
            continue
        seen.add(key)
        ordered_rows.append(merged[key])
    for key, row in merged.items():
        if key not in seen:
            ordered_rows.append(row)

    return ordered_rows, added, updated, moved, skipped


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
    for analysis_problem in sorted(
        topic_counts,
        key=lambda topic: registry.topic_order_map().get(topic, 999),
    ):
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

    return f"""# {RUN_DATE} Round-2 Comparative Relaxation Consolidation Report

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
        help="Overlay the approved comparative-relaxation changes onto the authoritative master registry.",
    )
    parser.add_argument(
        "--authoritative-csv",
        default=AUTHORITATIVE_CSV,
        help="Master registry CSV path to read and rewrite during consolidation.",
    )
    parser.add_argument(
        "--round2-report",
        default=ROUND2_REPORT,
        help="Markdown report path for the NAS copy of the comparative-relaxation summary.",
    )
    parser.add_argument(
        "--consolidation-report",
        default=CONSOLIDATION_REPORT,
        help="Markdown report path for the comparative-relaxation reconciliation summary.",
    )
    args = parser.parse_args()

    out_root = Path(args.out_root)
    scratch_root = out_root / "round1_expanded_scratch"
    runs_root = out_root / "round1_runs"

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
