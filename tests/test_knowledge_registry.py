import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "knowledge_registry"
LAYER1 = REGISTRY / "layer1" / "task_catalog.md"
LAYER2 = REGISTRY / "layer2"
PROTOCOL = REGISTRY / "protocols" / "layer1_2_selection"


EXPECTED_ANALYSIS_PROBLEMS = {
    "Artifact Correction",
    "Cell Type Inference",
    "Cell-Cell Communication",
    "Data Quality Control",
    "Denoising / Signal Recovery",
    "Domain / Clustering",
    "Gene Expression Prediction / Imputation",
    "Graph / Neighborhood",
    "Integration",
    "Normalization",
    "Panel Design",
    "Phenotype- / Cohort-linked Spatial Feature and Niche Analysis",
    "Program Discovery",
    "Segmentation",
    "Spatial Clonal Analysis",
    "Spatial Contrast Testing",
    "Spatial Perturbation Analysis",
    "Spatial Trajectory Analysis",
    "Spatially Variable Gene Detection",
    "Super-resolution",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def parse_layer1_routes() -> list[dict[str, str]]:
    routes = []
    for line in read_text(LAYER1).splitlines():
        if not line.startswith("| ") or line.startswith("| ---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] == "Analysis Problem":
            continue
        assert len(cells) == 5
        routes.append(
            {
                "analysis_problem": cells[0],
                "analysis_target": cells[1],
                "main_input_or_signal": cells[2],
                "target_output": cells[3],
                "route": cells[4].strip("`"),
            }
        )
    return routes


def test_layer1_routes_cover_active_20_topic_registry():
    routes = parse_layer1_routes()

    assert len(routes) == 20
    assert {route["analysis_problem"] for route in routes} == EXPECTED_ANALYSIS_PROBLEMS
    assert all(route["route"].startswith("knowledge_registry/layer2/") for route in routes)


def test_selection_policy_matches_layer1_routes_and_existing_layer2_files():
    layer1_routes = parse_layer1_routes()
    policy = read_json(PROTOCOL / "selection_policy.json")

    assert policy["registry_root"] == "knowledge_registry"
    assert policy["authority_status"] == "repo_authoritative_layer1_2_knowledge"
    assert len(policy["routes"]) == 20
    assert policy["routes"] == layer1_routes

    for route in policy["routes"]:
        path = ROOT / route["route"]
        assert path.exists(), route["route"]
        assert path.parent == LAYER2


def test_layer2_topic_files_have_required_section_order():
    topic_files = sorted(
        path
        for path in LAYER2.glob("*.md")
        if path.name not in {"README.md", "method_selection_standard.md"}
    )

    assert len(topic_files) == 20
    for path in topic_files:
        text = read_text(path)
        headings = [
            text.index("## Problem Boundary"),
            text.index("## Method Feature Table"),
            text.index("## Decision Tree"),
        ]
        assert headings == sorted(headings), path


def test_protocol_enforces_closed_world_agent_selection():
    agent = read_text(PROTOCOL / "agent.md")
    policy = read_json(PROTOCOL / "selection_policy.json")
    schema = read_json(PROTOCOL / "selection_policy.schema.json")

    assert "Read `knowledge_registry/layer1/task_catalog.md`" in agent
    assert "Open the exact `Route`" in agent
    assert "Do not begin by searching for packages" in agent
    assert "out_of_formal_review" in agent
    assert "Do not provide:" in agent

    assert "default_candidate_space" in policy["closed_world_policy"]
    assert "external_package_exception" in policy["closed_world_policy"]
    assert "forbidden_claims" in schema["required"]
    for claim in [
        "default_method",
        "runtime_support",
        "adapter_available",
        "execution_ready",
        "docker_or_conda_available",
    ]:
        assert claim in policy["forbidden_claims"]


def test_no_positive_runtime_or_default_method_claims_in_registry():
    scanned_files = [
        path
        for path in REGISTRY.rglob("*")
        if path.is_file() and path.suffix in {".md", ".json"}
    ]
    positive_patterns = [
        re.compile(r"\bhas runtime support\b", re.IGNORECASE),
        re.compile(r"\bis runtime ready\b", re.IGNORECASE),
        re.compile(r"\bis execution ready\b", re.IGNORECASE),
        re.compile(r"\bdefault method is\b", re.IGNORECASE),
        re.compile(r"\badapter is available\b", re.IGNORECASE),
        re.compile(r"\bdocker .* is available\b", re.IGNORECASE),
        re.compile(r"\bconda .* is available\b", re.IGNORECASE),
    ]

    flagged = []
    for path in scanned_files:
        text = read_text(path)
        for pattern in positive_patterns:
            if pattern.search(text):
                flagged.append((path.relative_to(ROOT).as_posix(), pattern.pattern))

    assert flagged == []


def test_static_scenarios_anchor_expected_layer1_routes():
    routes = {route["analysis_problem"]: route["route"] for route in parse_layer1_routes()}

    scenarios = {
        "standard AnnData normalization before downstream analysis": "Normalization",
        "cell-cell ligand receptor communication between annotated cell types": "Cell-Cell Communication",
        "spatial neighbor graph construction and neighborhood enrichment": "Graph / Neighborhood",
        "condition associated spatial contrast between treated and control tissue": "Spatial Contrast Testing",
        "outcome linked tissue niche features across a patient cohort": "Phenotype- / Cohort-linked Spatial Feature and Niche Analysis",
        "spatial response to perturbation guides in a screen": "Spatial Perturbation Analysis",
    }

    assert set(scenarios.values()).issubset(routes)
    assert routes["Normalization"] == "knowledge_registry/layer2/normalization.md"
    assert routes["Cell-Cell Communication"] == "knowledge_registry/layer2/cell_cell_communication.md"
    assert routes["Graph / Neighborhood"] == "knowledge_registry/layer2/graph_neighborhood.md"
    assert routes["Spatial Contrast Testing"] == "knowledge_registry/layer2/spatial_contrast_testing.md"
    assert (
        routes["Phenotype- / Cohort-linked Spatial Feature and Niche Analysis"]
        == "knowledge_registry/layer2/phenotype_cohort_linked_spatial_feature_niche_analysis.md"
    )
    assert routes["Spatial Perturbation Analysis"] == "knowledge_registry/layer2/spatial_perturbation_analysis.md"

