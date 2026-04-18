from pathlib import Path
import json


PILOT_PATH = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md"
)
SUBTABLE_MD_PATH = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_subtable.md"
)
SUBTABLE_JSON_PATH = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_subtable.json"
)


def test_domain_identification_layer2_candidate_freeze_is_expanded():
    pilot = PILOT_PATH.read_text()
    subtable_md = SUBTABLE_MD_PATH.read_text()

    assert "27 tools" in pilot
    assert "27 tools for this pass" in subtable_md
    for method_name in ("ADEPT", "ConGI", "SpaceFlow", "conST"):
        assert method_name in pilot
        assert method_name in subtable_md


def test_domain_identification_layer2_json_rows_match_expanded_candidate_set():
    with SUBTABLE_JSON_PATH.open() as handle:
        data = json.load(handle)

    rows = data["rows"]
    candidate_freeze_order = data["candidate_freeze_order"]
    row_names = {row["Tool Name"] for row in rows}

    assert len(rows) == 27
    assert len(candidate_freeze_order) == 27
    for method_name in ("ADEPT", "ConGI", "SpaceFlow", "conST"):
        assert method_name in row_names
        assert method_name in candidate_freeze_order

    assert all("Tier" not in row for row in rows)


def test_const_row_matches_current_layer2_decision():
    with SUBTABLE_JSON_PATH.open() as handle:
        data = json.load(handle)

    const_row = next(row for row in data["rows"] if row["Tool Name"] == "conST")

    assert const_row["Method Family"] == "Multimodal contrastive graph learning"
    assert (
        const_row["Main Input"]
        == "ST matrix + spatial coordinates + optional histology image"
    )
    assert (
        const_row["Main Use in This Topic"]
        == "spatial domain identification with multimodal contrastive graph embedding"
    )
    assert const_row["Closest Alternatives"] == "GraphST; DeepST; SiGra"
    assert const_row["Compute Requirement"] == "Optional GPU"
    assert const_row["Code Access"] == "available"
    assert const_row["Primary Code Link"] == "https://github.com/ys-zong/conST"
    assert const_row["Evidence Source"] == "benchmark/review"
    assert const_row["Image Signal Use"] == "optional"
    assert const_row["External Biological Guidance"] == "none"
    assert const_row["Cross-slice Support"] == "single-slice only"
    assert const_row["Batch Handling"] == "not addressed"
    assert (
        const_row["Main Spatial Prior"]
        == "deep multimodal fusion + contrastive graph embedding"
    )
