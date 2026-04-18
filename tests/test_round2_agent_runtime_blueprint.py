import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONTRACTS = ROOT / "contracts"
EXAMPLES = CONTRACTS / "examples"
SURFACES = ROOT / "surface_registry"
EVALS = ROOT / "evals"
SKILLS = ROOT / "skills"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def test_agent_runtime_reference_is_explicitly_non_authoritative():
    reference = read_text(DOCS / "35_agent_runtime_reference.md")

    assert "working blueprint" in reference
    assert "not a current authority document" in reference
    assert "does not override" in reference
    assert "docs/15_round1_baseline_and_round2_prep.md" in reference
    assert "/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md" in reference
    assert "candidate mapping" in reference
    assert "https://openai.com/index/the-next-evolution-of-the-agents-sdk/" in reference
    assert "https://developers.openai.com/api/docs/guides/agents/sandboxes" in reference
    assert "https://developers.openai.com/api/docs/guides/tools-skills" in reference
    assert "https://developers.openai.com/api/docs/guides/agents/orchestration" in reference
    assert "https://modal.com/blog/building-with-modal-and-the-openai-agent-sdk" in reference
    assert "Frozen Mapping" not in reference


def test_working_buffer_keeps_existing_authority_order_intact():
    buffer_text = read_text(DOCS / "12_round2_working_buffer.md")

    assert "candidate blueprint material" in buffer_text
    assert "do not replace the existing authority order" in buffer_text
    assert "docs/35_agent_runtime_reference.md" in buffer_text
    assert "Open Questions" in buffer_text
    assert "Formal authority for the frozen runtime mapping now lives in" not in buffer_text


def test_environment_strategy_is_a_working_blueprint_not_a_freeze():
    strategy = read_text(DOCS / "30_env_strategy.md")

    assert "working blueprint" in strategy
    assert "not yet frozen" in strategy
    assert "Current Working Direction" in strategy
    assert "Harness vs Compute" in strategy
    assert "Harness responsibilities" in strategy
    assert "Compute responsibilities" in strategy
    assert "`EnvironmentProfile`" in strategy
    for field in [
        "profile_id",
        "isolation_mode",
        "base_stack",
        "resource_class",
        "storage_policy",
        "secrets_policy",
        "provider",
    ]:
        assert field in strategy
    assert "Current Decision" not in strategy


def test_interface_contract_doc_is_explicitly_provisional():
    contract_doc = read_text(DOCS / "40_interface_contract.md")

    assert "working blueprint" in contract_doc
    assert "not yet frozen" in contract_doc
    assert "Current Working Direction" in contract_doc
    for contract_name in [
        "SkillSpec",
        "ExecutionSurfaceSpec",
        "EnvironmentProfile",
        "RunRecord",
        "ValidationReport",
    ]:
        assert contract_name in contract_doc

    assert "smallest stable callable unit" in contract_doc
    assert "structured state" in contract_doc
    assert "manual review" in contract_doc
    assert "Current Decision" not in contract_doc


def test_validation_doc_is_provisional_and_preserves_existing_freezes():
    validation = read_text(DOCS / "60_validation.md")

    assert "working blueprint" in validation
    assert "not yet frozen" in validation
    assert "Current Working Direction" in validation
    assert "`preflight`" in validation
    assert "`runtime`" in validation
    assert "`post-run`" in validation
    assert "authoritative CSV" in validation
    assert "NAS report" in validation
    assert "external resource" in validation
    assert "high-cost GPU" in validation
    assert "baseline registry" in validation


def test_rewrite_policy_uses_agent_runtime_criteria_without_claiming_freeze():
    policy = read_text(DOCS / "50_rewrite_policy.md")

    assert "working blueprint" in policy
    assert "not yet frozen" in policy
    assert "Current Working Direction" in policy
    assert "agent-runtime" in policy
    assert "stable CLI/API" in policy
    assert "environment fragmentation" in policy
    assert "output cannot be validated" in policy
    assert "failure semantics" in policy
    assert "wrapper" in policy
    assert "Current Decision" not in policy


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


def test_blueprint_directories_explain_their_roles():
    assert (SKILLS / "README.md").exists()
    assert (CONTRACTS / "README.md").exists()
    assert (SURFACES / "README.md").exists()
    assert (EVALS / "README.md").exists()

    assert "task-level instructions and selection rules" in read_text(SKILLS / "README.md")
    assert "public contract schemas" in read_text(CONTRACTS / "README.md")
    assert "execution manifests" in read_text(SURFACES / "README.md")
    assert "golden scenarios" in read_text(EVALS / "README.md")


def test_spatial_domain_identification_assets_are_illustrative_only():
    skill_blueprint = read_text(SKILLS / "spatial_domain_identification.md")
    skill = read_json(EXAMPLES / "skill_spec.example.json")
    surface = read_json(
        SURFACES / "examples" / "spatial_domain_identification.spagcn.example.json"
    )
    evaluation = read_json(EVALS / "golden_scenarios" / "spatial_domain_identification_selection.json")

    assert "illustrative only" in skill_blueprint
    assert "does not freeze a current Layer 3 default" in skill_blueprint
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
