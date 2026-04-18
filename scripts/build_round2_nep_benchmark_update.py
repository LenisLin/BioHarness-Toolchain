from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.build_round1_expanded_outputs as registry


RUN_DATE = "2026-04-16"
MAIN_WINDOW = ("2015-01-01", "2026-04-16")
AUTHORITATIVE_CSV = registry.AUTHORITATIVE_CSV
ROUND2_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-16_round2_nep_benchmark_screening_report.md"
)
CONSOLIDATION_REPORT = (
    "/mnt/NAS_21T/ProjectData/BioHarness/round1_reports/"
    "2026-04-16_round2_nep_benchmark_consolidation_report.md"
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
    insert_before_method: str = "",
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
    if insert_before_method:
        row["_insert_before_method"] = insert_before_method
    return row


SUPPLEMENT_TOPICS = [
    {
        "analysis_problem": "Cell-Cell Communication",
        "slug": "cell_cell_communication",
        "run_objective": (
            "Screen the 2026 Nature Communications cellular-neighbor-preference benchmark and "
            "promote only new methods that satisfy the current first-layer CCC admission rules."
        ),
        "scope_confirmation": [
            "The benchmark article is treated as a benchmark seed rather than as an automatic authoritative import list.",
            "Methods already represented in the current first-layer registry remain no-change anchors.",
            "Only newly screened methods with a dedicated primary contribution and a stable public code path are eligible for authoritative writeback.",
        ],
        "active_stable_subtask_window": [
            "Neighborhood / interaction-effect modeling",
        ],
        "deferred_candidate_subtasks": [
            "Toolkit-embedded neighbor-enrichment modules",
            "Auxiliary interpretability scores without standalone method packaging",
        ],
        "benchmark_seeds": [
            "Nature Communications 2026, Comparison and optimization of cellular neighbor preference methods for quantitative tissue analysis (DOI 10.1038/s41467-026-71699-z).",
        ],
        "review_seeds": [
            "No additional review seed displaced the benchmark article as the dominant evidence source for this narrow screening pass.",
        ],
        "whitelist_results": [
            "The benchmark article itself is a whitelist-venue source and supports screening of quantitative cellular-neighbor-preference methods.",
            "COZI is the only new screened method in the article that cleanly satisfies the current standalone-method criterion for authoritative admission.",
        ],
        "exception_results": [
            "No ecosystem-exception venue override was needed in this pass.",
        ],
        "direct_results": [
            "Code-availability review indicates that COZI has independent public implementations, while several benchmarked alternatives are embedded as modules or benchmark wrappers inside broader tool ecosystems.",
            "Existing master-registry coverage already includes Giotto and MISTy, so the benchmark does not justify duplicate authoritative rows for them.",
        ],
        "date_reaudit": [
            "Targeted PubMed DOI/title searches found no PubMed-indexed record for DOI 10.1038/s41467-026-71699-z as of 2026-04-16.",
            "The article page reports public COZI implementations through COZIpy and coziR; the authoritative CSV will store the coziR GitHub repository as the single GitHub URL field.",
        ],
        "screened_holdouts": [
            "`SEA`: held out because the benchmark treats it as a shared or adapted implementation path rather than a clearly packaged standalone method repository.",
            "`Squidpy`, `Scimap`, `IMCRtools`, and `histoCAT`: held out because the benchmarked NEP functionality is module-level inside broader tool suites, not their sole primary first-layer contribution under the current row-unit policy.",
            "`CCR`: held out because it functions as an auxiliary scoring/interpretability layer rather than as a standalone method entry for the current registry schema.",
            "`CellCharter`: not promoted here because it is already represented under `Graph / Neighborhood`, which remains the cleaner first-layer placement for that method family.",
        ],
        "methods": [
            s(
                "Ligand-receptor communication inference",
                "Spatial neighborhood graph scoring",
                "Giotto",
                "Giotto: a toolbox for integrative analysis and visualization of spatial expression data",
                "10.1186/s13059-021-02286-2",
                "33685491",
                2021,
                "Genome Biology",
                "Benchmark seed",
                "Existing authoritative CCC anchor re-confirmed during 2026-04-16 NEP benchmark screening",
                "Yes",
                "https://github.com/RubD/Giotto",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Neighborhood / interaction-effect modeling",
                "Multiview interaction modeling",
                "MISTy",
                "Explainable multiview framework for dissecting spatial relationships from highly multiplexed data",
                "10.1186/s13059-022-02663-5",
                "35422018",
                2022,
                "Genome Biology",
                "Benchmark seed",
                "Existing authoritative CCC interaction-effect anchor re-confirmed during 2026-04-16 NEP benchmark screening",
                "Yes",
                "https://github.com/saezlab/mistyR",
                "CPU",
                "Include",
                "no_change",
                notes="Existing authoritative row retained.",
            ),
            s(
                "Neighborhood / interaction-effect modeling",
                "Conditional z-score neighbor preference analysis",
                "COZI",
                "Comparison and optimization of cellular neighbor preference methods for quantitative tissue analysis",
                "10.1038/s41467-026-71699-z",
                "",
                2026,
                "Nature Communications",
                "Benchmark seed",
                "Nature Communications 2026 cellular-neighbor-preference benchmark + code-availability review",
                "Yes",
                "https://github.com/SchapiroLabor/coziR",
                "CPU",
                "Include",
                "add",
                notes="Admitted as a dedicated cellular-neighbor-preference method introduced in a whitelist-venue benchmark study with public standalone COZI implementations.",
                insert_before_method="SPIDER",
            ),
        ],
        "label_stable": (
            "Yes for the narrow update. `Cell-Cell Communication` remains stable, and this pass only extends the interaction-effect branch with a benchmark-screened standalone NEP method."
        ),
        "subtask_sufficient": (
            "Yes. `Neighborhood / interaction-effect modeling` remains sufficient for COZI because the method focuses on quantitative local-neighbor preference rather than on ligand-receptor inference."
        ),
        "family_assessment": (
            "Yes. COZI enters with a method-family label that stays algorithmic and avoids collapsing the benchmark into generic toolkit language."
        ),
        "revision_needed": (
            "No schema revision is required. Future benchmark-driven additions should still prove standalone method identity, public executability, and clean first-layer placement before promotion."
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

## Screened Hold-Out Methods

{registry.bullets(topic['screened_holdouts'])}

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
    holdout_lines = []

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
        for line in topic["screened_holdouts"]:
            holdout_lines.append(f"- {line}")

    return f"""# {RUN_DATE} Round-2 NEP Benchmark Screening Report

## Summary

- This NAS report screens the 2026 Nature Communications cellular-neighbor-preference benchmark under the current strict first-layer admission policy.
- The benchmark article is treated as a benchmark seed, not as a blanket authoritative promotion list.
- Only one new method passed the current admission screen: `COZI`.

## Per-Topic Supplement Counts

{chr(10).join(per_topic)}

## Authoritative Writeback Actions

{chr(10).join(ready_lines) if ready_lines else '- No authoritative writeback actions recorded.'}

## Evidence Re-Audit Notes

{chr(10).join(date_lines)}

## Screened Hold-Out Methods

{chr(10).join(holdout_lines)}

## Critical-Evidence Caveat

- `COZI` is admitted because the benchmark article introduces and evaluates it in a whitelist venue and the article reports public standalone implementations.
- The screened hold-outs remain scientifically relevant, but the current evidence does not justify authoritative promotion because they behave as toolkit modules, benchmark wrappers, or auxiliary scores rather than clean standalone first-layer method rows.

## Protocol-Compliance Check

- No CSV schema changes were introduced.
- The only authoritative writeback in this pass is adding `COZI`.
- Existing authoritative rows such as `Giotto` and `MISTy` remain unchanged.
"""


def _insert_key_at_position(
    ordered_keys: list[tuple[str, str, str]],
    new_key: tuple[str, str, str],
    row_meta: dict[str, str],
) -> None:
    target_problem = new_key[0]
    insert_before_method = row_meta.get("_insert_before_method", "")

    insertion_index: int | None = None
    if insert_before_method:
        for idx, key in enumerate(ordered_keys):
            if key[0] == target_problem and key[2] == insert_before_method:
                insertion_index = idx
                break

    if insertion_index is None:
        same_subtask = [
            idx
            for idx, key in enumerate(ordered_keys)
            if key[0] == target_problem and key[1] == new_key[1]
        ]
        if same_subtask:
            insertion_index = same_subtask[-1] + 1

    if insertion_index is None:
        same_problem = [
            idx for idx, key in enumerate(ordered_keys) if key[0] == target_problem
        ]
        insertion_index = same_problem[-1] + 1 if same_problem else len(ordered_keys)

    ordered_keys.insert(insertion_index, new_key)


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
    ordered_keys = [registry.registry_key(row) for row in normalized_current]

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
                _insert_key_at_position(ordered_keys, key, row)
        else:
            skipped.append((*key, f"unknown-action:{action}"))

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

    return f"""# {RUN_DATE} Round-2 NEP Benchmark Consolidation Report

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
        help="Overlay the approved NEP benchmark changes onto the authoritative master registry.",
    )
    parser.add_argument(
        "--authoritative-csv",
        default=AUTHORITATIVE_CSV,
        help="Master registry CSV path to read and rewrite during consolidation.",
    )
    parser.add_argument(
        "--round2-report",
        default=ROUND2_REPORT,
        help="Markdown report path for the NAS copy of the NEP benchmark screening summary.",
    )
    parser.add_argument(
        "--consolidation-report",
        default=CONSOLIDATION_REPORT,
        help="Markdown report path for the NEP benchmark reconciliation summary.",
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
