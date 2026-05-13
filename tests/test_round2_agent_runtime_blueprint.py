import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTRACTS = ROOT / "contracts"
EXAMPLES = CONTRACTS / "examples"
SURFACES = ROOT / "surface_registry"
EVALS = ROOT / "evals"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def test_schema_bundle_and_examples_exist_for_all_public_contracts():
    expected_contracts = {
        "skill_spec": ["skill_id", "analysis_problem", "selection_signals", "default_surface"],
        "execution_surface_spec": [
            "surface_id",
            "analysis_problem",
            "input_contract",
            "parameter_template",
            "environment_profile",
            "output_artifacts",
            "validation_hooks",
        ],
        "environment_profile": [
            "profile_id",
            "isolation_mode",
            "base_stack",
            "resource_class",
            "storage_policy",
            "secrets_policy",
            "provider",
        ],
        "backend_adapter_spec": [
            "adapter_id",
            "surface_id",
            "runtime_language",
            "environment_profile",
            "entrypoint",
            "rewrite_level",
            "visibility",
        ],
        "run_record": ["run_id", "skill_id", "surface_id", "status", "state_summary"],
        "validation_report": [
            "report_id",
            "run_id",
            "preflight",
            "post_run",
            "final_status",
            "manual_review_required",
        ],
    }

    for stem, required_fields in expected_contracts.items():
        schema_path = CONTRACTS / f"{stem}.schema.json"
        example_path = EXAMPLES / f"{stem}.example.json"

        schema = read_json(schema_path)
        example = read_json(example_path)

        assert schema["type"] == "object"
        assert schema["title"]
        assert schema["required"]
        assert schema["properties"]

        for field in required_fields:
            assert field in schema["required"]
            assert field in schema["properties"]
            assert field in example

        assert example["example_status"] == "illustrative_example"
        assert "authority_note" in example


def test_spatial_domain_identification_assets_are_illustrative_only():
    skill = read_json(EXAMPLES / "skill_spec.example.json")
    surface = read_json(
        SURFACES / "examples" / "spatial_domain_identification.spagcn.example.json"
    )
    evaluation = read_json(EVALS / "golden_scenarios" / "spatial_domain_identification_selection.json")

    assert skill["example_status"] == "illustrative_example"
    assert skill["skill_id"] == "example_spatial_domain_identification"
    assert skill["analysis_problem"] == "Domain / Clustering"
    assert skill["default_surface"] == surface["surface_id"]
    assert "histology available" in skill["selection_signals"]
    assert surface["example_status"] == "illustrative_example"
    assert surface["surface_id"] == "example.spatial_domain_identification.spagcn"
    assert surface["analysis_problem"] == "Domain / Clustering"
    assert surface["validation_hooks"] == ["preflight.schema", "post_run.domain_labels"]
    assert "does not freeze SpaGCN as the current default surface" in surface["authority_note"]
    assert evaluation["skill_id"] == skill["skill_id"]
    assert evaluation["expected_surface"] == surface["surface_id"]
    assert evaluation["decision_status"] == "not_frozen"
    assert evaluation["illustrative_only"] is True


def test_examples_cover_gpu_approval_authoritative_writes_and_resume_state():
    environment = read_json(EXAMPLES / "environment_profile.example.json")
    run_record = read_json(EXAMPLES / "run_record.example.json")
    report = read_json(EXAMPLES / "validation_report.example.json")
    gpu_eval = read_json(EVALS / "golden_scenarios" / "gpu_execution_requires_approval.json")
    writeback_eval = read_json(EVALS / "golden_scenarios" / "authoritative_writeback_requires_review.json")
    resume_eval = read_json(EVALS / "golden_scenarios" / "run_record_resume_compaction.json")

    assert environment["resource_class"] == "cpu"
    assert environment["approval_required"] is False
    assert environment["example_status"] == "illustrative_example"
    assert report["manual_review_required"] is True
    assert "authoritative artifact writeback" in report["blocking_reasons"]
    assert run_record["state_summary"]["resume_strategy"] == "structured state rehydration"
    assert gpu_eval["approval_gate"] == "required"
    assert gpu_eval["illustrative_only"] is True
    assert writeback_eval["manual_review_required"] is True
    assert writeback_eval["illustrative_only"] is True
    assert resume_eval["resume_from"] == run_record["run_id"]
    assert resume_eval["illustrative_only"] is True
