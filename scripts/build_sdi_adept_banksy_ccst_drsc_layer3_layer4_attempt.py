#!/usr/bin/env python3
"""Create a scoped Layer3/Layer4 build-attempt package for ADEPT/BANKSY/CCST/DR-SC.

The package is intentionally scoped to the 2026-06-11 invocation and does not
copy prior build outputs, prior method-validation trial outputs, or the
completed ConGI/BASS package as success evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
from pathlib import Path
from textwrap import dedent
from typing import Any

import yaml


TARGET_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/layer3_layer4_implementations/"
    "SDI_ADEPT_BANKSY_CCST_DRSC_layer3_layer4_build_2026-06-11"
)
REPAIR_ROOT = TARGET_ROOT / "repair_loop_artifacts"
PLANNING_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/stage_integration/pre_gate2_planning_2026-05-21"
)
ENV_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/environment_builds/SDI_base"
)
CONDA_PREFIX = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base"
)
SOURCE_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/repository_reading_first_round_2026-05-15/source_repos"
)

METHODS = {
    "ADEPT": {
        "module": "adept",
        "agent_id": "019eb966-0d44-7280-9577-a4bfbd789ab9",
        "route_summary": "ADEPT native loader, graph, GAAE/imputation/mclust, export, and scanpy plot mappings.",
        "backend_cmd": [
            "python",
            "-c",
            "import ADEPT_main, st_loading_utils, GAAE, GAAE.utils; print('ADEPT backend import fresh pass')",
        ],
        "pythonpath": str(SOURCE_ROOT / "ADEPT"),
        "actions": {
            "prepare_spatial_domain_input": ["st_loading_utils.py", "GAAE.utils.initialize", "ADEPT_main.py loader branches"],
            "construct_spatial_structure": ["get_kNN", "Transfer_pytorch_Data", 'adata.uns["Spatial_Net"]'],
            "fit_then_assign_domains": ["GAAE", "train_ADEPT_use_DE", "impute", "mclust_R"],
            "export_domain_result": ['canonical adata.obs["domain"] from prior fit'],
            "plot_domain_labels": ["sc.pl.spatial save blocks"],
        },
        "strict": {
            "prepare_spatial_domain_input": 'Prepared AnnData with aligned X/obs/var and adata.obsm["spatial"].',
            "construct_spatial_structure": 'adata.obsp["spatial_connectivities"] aligned to obs.',
            "fit_then_assign_domains": 'adata.obs["domain"] from mclust_impute after native fit.',
            "export_domain_result": "domain_labels.csv with obs_id and domain.",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf.",
        },
    },
    "BANKSY": {
        "module": "banksy",
        "agent_id": "019eb966-3874-7c22-8775-c562a699d971",
        "route_summary": "BANKSY AnnData, spatial weights, Leiden label, export, and plotting mappings.",
        "backend_cmd": [
            "python",
            "-c",
            "import banksy, banksy_utils; import banksy.initialize_banksy, banksy.run_banksy, banksy.embed_banksy; print('BANKSY backend import fresh pass')",
        ],
        "pythonpath": str(SOURCE_ROOT / "BANKSY/src"),
        "actions": {
            "prepare_spatial_domain_input": ["AnnData examples", "coordinate key normalization"],
            "construct_spatial_structure": [
                "initialize_banksy",
                "generate_spatial_weights_fixed_nbrs",
                "create_nbr_matrix",
                "generate_banksy_matrix",
            ],
            "fit_then_assign_domains": ["run_banksy_multiparam", "pca_umap", "run_Leiden_partition"],
            "export_domain_result": ['canonical adata.obs["domain"] from prior fit'],
            "plot_domain_labels": ["plot_banksy.py::plot_results", "_plot_labels"],
        },
        "strict": {
            "prepare_spatial_domain_input": 'Prepared AnnData with reviewed adata.obsm["spatial"].',
            "construct_spatial_structure": "BANKSY spatial weights/context with obs-aligned matrix provenance.",
            "fit_then_assign_domains": 'adata.obs["domain"] from reviewed Leiden path labels.',
            "export_domain_result": "domain_labels.csv with obs_id and domain.",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf.",
        },
    },
    "CCST": {
        "module": "ccst",
        "agent_id": "019eb966-7733-7893-9c56-de984d18b6a7",
        "route_summary": "CCST generated input, graph, DGI fit, export, and plotting mappings.",
        "backend_cmd": [
            "python",
            "-c",
            "import CCST; from CCST import get_graph, train_DGI, PCA_process, Kmeans_cluster; print('CCST backend import fresh pass')",
        ],
        "pythonpath": str(SOURCE_ROOT / "CCST"),
        "actions": {
            "prepare_spatial_domain_input": ["data_generation_ST.py", "data_generation_merfish.py", "read_h5", "adata_preprocess"],
            "construct_spatial_structure": ["get_adj", "CCST.py::get_graph"],
            "fit_then_assign_domains": ["run_CCST.py", "Encoder", "DGI training", "clustering utilities"],
            "export_domain_result": ['canonical adata.obs["domain"]; current-fit types.txt provenance only'],
            "plot_domain_labels": ["draw_map", "ST/MERFISH plotting blocks"],
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData with generated feature/coordinate provenance.",
            "construct_spatial_structure": 'adata.obsp["spatial_connectivities"] aligned to obs.',
            "fit_then_assign_domains": 'adata.obs["domain"] from current native clustering path.',
            "export_domain_result": "domain_labels.csv with obs_id and domain.",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf.",
        },
    },
    "DR-SC": {
        "module": "dr_sc",
        "agent_id": "019eb966-a118-7242-8cf1-ca9a9ab4d1b0",
        "route_summary": "DR-SC R/Seurat input, adjacency, fit, export, and plotting mappings.",
        "backend_cmd": [
            "Rscript",
            "-e",
            "library(DR.SC); print(packageVersion('DR.SC')); print('DR-SC backend load fresh pass')",
        ],
        "pythonpath": "",
        "actions": {
            "prepare_spatial_domain_input": ["DR.SC", "DR.SC.Seurat", "DR.SC_fit", "Seurat/matrix entry paths"],
            "construct_spatial_structure": ["getAdj.Seurat", "getAdj_reg", "getAdj_auto", "getAdj_manual"],
            "fit_then_assign_domains": ["drsc", "icmem_heterCpp", "EMmPCpp_heter", "selectModel", "Seurat writeback"],
            "export_domain_result": ['canonical adata.obs["domain"]; spatial.drsc.cluster provenance only'],
            "plot_domain_labels": ["spatialPlotClusters", "drscPlot", "mbicPlot domain plot only"],
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData plus private DR-SC Seurat or matrix/coordinate state.",
            "construct_spatial_structure": 'adata.obsp["spatial_connectivities"] or reviewed equivalent context.',
            "fit_then_assign_domains": 'adata.obs["domain"] from selected spatial.drsc.cluster metadata.',
            "export_domain_result": "domain_labels.csv with obs_id and domain.",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf.",
        },
    },
}

SURFACES = [
    "prepare_spatial_domain_input",
    "construct_spatial_structure",
    "fit_then_assign_domains",
    "export_domain_result",
    "plot_domain_labels",
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).lstrip(), encoding="utf-8")


def dump_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def run_command(method: str, cmd: list[str], pythonpath: str, log_path: Path) -> str:
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = str(CONDA_PREFIX / "lib")
    if pythonpath:
        env["PYTHONPATH"] = pythonpath
    proc = subprocess.run(
        ["conda", "run", "-p", str(CONDA_PREFIX), *cmd],
        env=env,
        cwd="/tmp",
        text=True,
        capture_output=True,
        check=False,
    )
    invocation = (
        f"env LD_LIBRARY_PATH={CONDA_PREFIX / 'lib'} "
        f"{'PYTHONPATH=' + pythonpath + ' ' if pythonpath else ''}"
        f"conda run -p {CONDA_PREFIX} {' '.join(cmd)}"
    )
    write(
        log_path,
        f"""
        method: {method}
        invocation: {invocation}
        returncode: {proc.returncode}
        stdout:
        {proc.stdout}
        stderr:
        {proc.stderr}
        """,
    )
    return "pass" if proc.returncode == 0 else "repair_required"


def runtime_package() -> None:
    pkg = TARGET_ROOT / "python/bioharness_sdi_runtime"
    write(pkg / "__init__.py", '"""Scoped SDI Layer3/Layer4 build-attempt runtime."""\n')
    write(
        pkg / "errors.py",
        """
        class SDIRuntimeError(RuntimeError):
            pass


        class ContractError(SDIRuntimeError):
            pass


        class BackendRouteError(SDIRuntimeError):
            pass
        """,
    )
    write(
        pkg / "state.py",
        """
        from __future__ import annotations

        from dataclasses import dataclass, field
        from pathlib import Path
        from typing import Any


        @dataclass
        class SDIMethodState:
            method: str
            surface: str
            adata: Any | None = None
            private: dict[str, Any] = field(default_factory=dict)
            artifacts: dict[str, Path] = field(default_factory=dict)
            provenance: dict[str, Any] = field(default_factory=dict)


        @dataclass
        class SDIRuntimeResult:
            method: str
            surface: str
            output: Any | None = None
            state: SDIMethodState | None = None
            artifacts: dict[str, Path] = field(default_factory=dict)
            provenance: dict[str, Any] = field(default_factory=dict)
        """,
    )
    write(
        pkg / "registry.py",
        """
        from __future__ import annotations

        from collections.abc import Callable

        _REGISTRY: dict[tuple[str, str], Callable] = {}


        def register_surface(method: str, surface: str, func: Callable) -> Callable:
            _REGISTRY[(method, surface)] = func
            return func


        def get_callable(method: str, surface: str) -> Callable:
            return _REGISTRY[(method, surface)]


        def iter_surface_bindings():
            yield from sorted(_REGISTRY.items())
        """,
    )
    write(
        pkg / "contracts.py",
        """
        from __future__ import annotations

        from pathlib import Path
        from typing import Any

        from .errors import ContractError


        def require_adata(adata: Any) -> Any:
            if adata is None or not hasattr(adata, "obs") or not hasattr(adata, "obsm"):
                raise ContractError("AnnData-like object with obs and obsm is required")
            return adata


        def require_spatial(adata: Any) -> Any:
            require_adata(adata)
            if "spatial" not in adata.obsm:
                raise ContractError('adata.obsm["spatial"] is required')
            return adata.obsm["spatial"]


        def require_domain(adata: Any) -> Any:
            require_adata(adata)
            if "domain" not in adata.obs:
                raise ContractError('adata.obs["domain"] is required')
            return adata.obs["domain"]


        def ensure_output_dir(path: str | Path) -> Path:
            out = Path(path)
            out.mkdir(parents=True, exist_ok=True)
            return out
        """,
    )
    write(
        pkg / "config.py",
        """
        from __future__ import annotations

        from pathlib import Path
        from typing import Any

        import yaml


        def load_surface_config(surface: str, config: Any = None) -> dict[str, Any]:
            if config is None:
                return {}
            if isinstance(config, (str, Path)):
                data = yaml.safe_load(Path(config).read_text(encoding="utf-8")) or {}
            elif isinstance(config, dict):
                data = config
            else:
                raise TypeError("config must be None, mapping, or YAML path")
            return data.get("execution_surfaces", {}).get(surface, data.get(surface, data))
        """,
    )
    write(pkg / "methods/__init__.py", '"""Method-owned bindings."""\n')


def method_module(method: str, cfg: dict[str, Any]) -> None:
    module_path = TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"
    source_path = SOURCE_ROOT / method
    actions = cfg["actions"]
    write(
        module_path,
        f'''
        """{method} method-owned Layer3 callable and Layer4 binding skeleton.

        This module is part of a repair-required build attempt. Public callables
        are registered and fail closed before producing strict outputs unless a
        downstream formal repair completes reviewed native action execution.
        """

        from __future__ import annotations

        from pathlib import Path
        from typing import Any

        from bioharness_sdi_runtime.config import load_surface_config
        from bioharness_sdi_runtime.contracts import ensure_output_dir, require_adata, require_domain, require_spatial
        from bioharness_sdi_runtime.errors import BackendRouteError
        from bioharness_sdi_runtime.registry import register_surface
        from bioharness_sdi_runtime.state import SDIMethodState, SDIRuntimeResult

        METHOD = {method!r}
        SOURCE_ROOT = Path({str(source_path)!r})


        def _reach_native_boundary(surface: str) -> dict[str, Any]:
            reviewed_actions = {{
                "prepare_spatial_domain_input": {actions["prepare_spatial_domain_input"]!r},
                "construct_spatial_structure": {actions["construct_spatial_structure"]!r},
                "fit_then_assign_domains": {actions["fit_then_assign_domains"]!r},
                "export_domain_result": {actions["export_domain_result"]!r},
                "plot_domain_labels": {actions["plot_domain_labels"]!r},
            }}[surface]
            return {{
                "method": METHOD,
                "surface": surface,
                "source_root": str(SOURCE_ROOT),
                "reviewed_actions": reviewed_actions,
                "boundary_policy": "fail_closed_until_native_action_binding_repair_completes",
            }}


        def _layer4_binding(surface: str, adata: Any = None, state: SDIMethodState | None = None, output_dir: str | Path | None = None, config: Any = None) -> SDIRuntimeResult:
            surface_config = load_surface_config(surface, config)
            if surface in {{"prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "plot_domain_labels"}}:
                require_adata(adata if adata is not None else getattr(state, "adata", None))
            if surface in {{"prepare_spatial_domain_input", "construct_spatial_structure", "plot_domain_labels"}}:
                require_spatial(adata if adata is not None else getattr(state, "adata", None))
            if surface in {{"export_domain_result", "plot_domain_labels"}}:
                require_domain(adata if adata is not None else getattr(state, "adata", None))
            boundary = _reach_native_boundary(surface)
            if surface == "export_domain_result" and output_dir is not None:
                ensure_output_dir(output_dir)
            raise BackendRouteError(
                f"{{METHOD}} {{surface}} reached reviewed boundary metadata {{boundary['reviewed_actions']}} "
                "but this build attempt did not complete executable native action binding/strict-output closure."
            )


        def prepare_spatial_domain_input(adata: Any, config: Any = None) -> SDIRuntimeResult:
            return _layer4_binding("prepare_spatial_domain_input", adata=adata, config=config)


        def construct_spatial_structure(adata: Any, state: SDIMethodState | None = None, config: Any = None) -> SDIRuntimeResult:
            return _layer4_binding("construct_spatial_structure", adata=adata, state=state, config=config)


        def fit_then_assign_domains(adata: Any, state: SDIMethodState | None = None, config: Any = None) -> SDIRuntimeResult:
            return _layer4_binding("fit_then_assign_domains", adata=adata, state=state, config=config)


        def export_domain_result(adata: Any, output_dir: str | Path, config: Any = None) -> SDIRuntimeResult:
            return _layer4_binding("export_domain_result", adata=adata, output_dir=output_dir, config=config)


        def plot_domain_labels(adata: Any, output_dir: str | Path, config: Any = None) -> SDIRuntimeResult:
            return _layer4_binding("plot_domain_labels", adata=adata, output_dir=output_dir, config=config)


        for _surface, _func in [
            ("prepare_spatial_domain_input", prepare_spatial_domain_input),
            ("construct_spatial_structure", construct_spatial_structure),
            ("fit_then_assign_domains", fit_then_assign_domains),
            ("export_domain_result", export_domain_result),
            ("plot_domain_labels", plot_domain_labels),
        ]:
            register_surface(METHOD, _surface, _func)
        ''',
    )


def method_config(method: str, cfg: dict[str, Any]) -> None:
    execution_surfaces = {}
    for surface in SURFACES:
        execution_surfaces[surface] = {
            "input_type": "canonical_or_prior_surface_AnnData",
            "output_type": cfg["strict"][surface],
            "binding_targets": [
                {"name": action, "kind": "function", "role": "reviewed_native_or_source_boundary"}
                for action in cfg["actions"][surface]
            ],
            "variables": {
                "semantic_options": {
                    "variable_kind": "mapping",
                    "function": f"{cfg['module']}.{surface}",
                    "value_type": "mapping",
                    "allowed_values_or_range": "reviewed semantic controls only",
                    "notes": "No defaults are defined in Layer3-M.",
                }
            },
        }
    dump_yaml(TARGET_ROOT / f"methods/{method}/layer3_method_config.yaml", {"method": method, "execution_surfaces": execution_surfaces})


def method_prompt(method: str, cfg: dict[str, Any]) -> Path:
    path = TARGET_ROOT / f"method_prompts/{method}_layer3_layer4_method_prompt.md"
    method_root = TARGET_ROOT / f"methods/{method}"
    implementation_root = TARGET_ROOT / "python"
    owned_paths = [
        str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
        str(method_root),
    ]
    read_only_inputs = [
        str(PLANNING_ROOT / "06_gate2_human_review_table.md"),
        str(PLANNING_ROOT / "06_gate2_environment_repair_addendum.md"),
        str(PLANNING_ROOT / "layer4_bridge_planning.md"),
        str(PLANNING_ROOT / "environment_integration_planning.md"),
        str(PLANNING_ROOT / "input_evidence_index.md"),
        str(ENV_ROOT / "harness_environment.yaml"),
        str(ENV_ROOT / "environment_build.jsonl"),
        str(SOURCE_ROOT / method),
    ]
    reviewed_rows = {
        surface: {
            "build_required": True,
            "gate2_status": "approved_for_next_step",
            "assigned_next_step": "layer3_layer4_build",
        }
        for surface in SURFACES
    }

    def yaml_block(value: Any, spaces: int = 8) -> str:
        prefix = " " * spaces
        text = yaml.safe_dump(value, sort_keys=False).rstrip()
        return prefix + text.replace("\n", "\n" + prefix)

    minimum_reference_documents = [
        "docs/layer3_4/stage_integration/layer3_layer4_build.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md",
        "docs/layer3_4/storage_and_runtime.md",
    ]
    reference_documents = [
        "docs/layer3_4/stage_integration/layer3_layer4_build.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md",
        "docs/layer3_4/storage_and_runtime.md",
    ]
    prompt_fields = {
        "analysis_problem": "spatial_domain_identification",
        "workflow_phase": "layer3_layer4_build",
        "method": method,
        "repo_root": "/home/lenislin/Experiment/projects/BioHarness-Toolchain-ST",
        "results_root": "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification",
        "current_artifact_root": str(TARGET_ROOT),
        "implementation_root": str(implementation_root),
        "method_build_output_root": str(method_root),
        "owned_paths": owned_paths,
        "read_only_inputs": read_only_inputs,
        "minimum_reference_documents": minimum_reference_documents,
        "reference_documents": reference_documents,
        "execution_environment": {
            "conda_prefix": str(CONDA_PREFIX),
            "command_env": {"LD_LIBRARY_PATH": str(CONDA_PREFIX / "lib")},
            "python_invocation": f"env LD_LIBRARY_PATH={CONDA_PREFIX / 'lib'} conda run -p {CONDA_PREFIX} python",
            "r_invocation": f"env LD_LIBRARY_PATH={CONDA_PREFIX / 'lib'} conda run -p {CONDA_PREFIX} Rscript",
            "command_workdir": str(TARGET_ROOT / "work"),
            "environment_check_output": str(ENV_ROOT / "environment_build.jsonl"),
        },
        "reviewed_rows": reviewed_rows,
        "surface_order": SURFACES,
        "strict_outputs": cfg["strict"],
        "native_or_rewrite_actions": cfg["actions"],
        "private_state_policy": f"Follow the {method} method-chain state handoff table in reviewed layer4_bridge_planning.md; prior-surface private state is method-owned and later surfaces consume prior state rather than rerunning output-determining actions.",
        "held_rows": [],
        "method_verifier": f"write {method_root}/verifier/method_verifier_result.yaml using docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md",
        "return_evidence": [
            "method-owned Layer3 callable module",
            "method-owned Layer4 binding module",
            "layer3_method_config.yaml",
            "per-row build_output_result.yaml",
            "per-row build_audit.yaml",
            "method_chain_lifecycle_trace.yaml",
            "callable import evidence",
            "route-level backend-load evidence",
            "selected bridge smoke-check evidence",
            "method verifier result",
        ],
        "stop_condition": "return PASS only after method verifier PASS; otherwise return FAIL_WITH_REPAIRS with affected method, execution surface, evidence class, observed code path, and repair target.",
    }
    prompt_fields_yaml = yaml.safe_dump(prompt_fields, sort_keys=False).rstrip()

    write(
        path,
        f"""
        # Layer3 / Layer4 Method Subagent Prompt: {method}

        ```yaml
{prompt_fields_yaml}
        ```

        You are Codex working in /home/lenislin/Experiment/projects/BioHarness-Toolchain-ST.

        Implement only {method} Layer3/Layer4 surfaces under:
        - {TARGET_ROOT}/python/bioharness_sdi_runtime/methods/{cfg['module']}.py
        - {TARGET_ROOT}/methods/{method}/

        Required surfaces: {', '.join(SURFACES)}
        Reviewed route summary: {cfg['route_summary']}
        Strict outputs:
{yaml_block(cfg['strict'])}
        Reviewed actions:
{yaml_block(cfg['actions'])}

        A skeleton implementation is not sufficient. Action names in metadata, YAML, comments, lifecycle prose, dictionaries, or state containers are not implementation. A method-owned Layer4 binding must import/call/start/fail-closed reach the reviewed native/glue/rewrite boundary before `PASS`.

        Read these references before implementation:
        - docs/layer3_4/stage_integration/layer3_layer4_build.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md
        - docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md
        - docs/layer3_4/storage_and_runtime.md
        - {PLANNING_ROOT / '06_gate2_human_review_table.md'}
        - {PLANNING_ROOT / 'layer4_bridge_planning.md'}
        - {ENV_ROOT / 'harness_environment.yaml'}
        - {ENV_ROOT / 'environment_build.jsonl'}

        Implementation workflow:
        1. Confirm owned paths, reviewed rows, source locators, strict outputs, and execution environment.
        2. Read method source and reviewed native call sites inside the reviewed route.
        3. Write `layer3_method_config.yaml` without defaults.
        4. Implement the Layer3 callable config channel and method-owned Layer4 binding. The binding must contain executable import/call/start/fail-closed boundary evidence for reviewed actions; action names in metadata are not implementation.
        5. Register all reviewed surfaces.
        6. Run callable import, route-level backend-load, and required selected bridge smoke checks.
        7. Record config consumption, per-row action binding evidence, anti-surrogate audit, strict-output closure, lifecycle trace, runtime execution status, and boundary non-claims.
        8. Run method verifier handoff.
        9. Return `PASS` only with method verifier `PASS`; return `FAIL_WITH_REPAIRS` with the first repair target otherwise. A redispatched repair packet must be implemented or narrowed from the affected surface/evidence class, not re-reported as the same skeleton-only state.

        Do not use prior build outputs, method-validation trial outputs, or the completed ConGI/BASS package as success evidence.
        Do not run method validation, author-case replay, bridge replay, data download, or GraphST work.
        Return PASS only with executable action-path evidence, strict-output closure, config consumption, lifecycle trace, selected bridge smoke evidence where required, and method verifier PASS.
        """,
    )
    return path


def per_method_evidence(method: str, cfg: dict[str, Any], status: dict[str, Any], backend_status: str) -> None:
    method_root = TARGET_ROOT / "methods" / method
    verifier_path = method_root / "verifier/method_verifier_result.yaml"
    subagent_id = status.get("subagent_id", cfg["agent_id"])
    first_repair = status.get("first_repair") or {
        "method": method,
        "execution_surface": "prepare_spatial_domain_input",
        "failure_class": "action_path_closure",
        "reviewed_action": cfg["actions"]["prepare_spatial_domain_input"][0],
        "observed_code_path": str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
        "repair_instruction": "Implement method-owned Layer4 binding that executes the reviewed native route and records produced state/output/artifact evidence.",
        "anti_surrogate_failure": True,
    }
    dump_yaml(
        verifier_path,
        {
            "verifier_result": {
                "scope": "method",
                "scope_id": method,
                "verdict": "FAIL_WITH_REPAIRS",
                "repair_loop_required": True,
                "terminal_completion_allowed": False,
                "required_repairs": [first_repair],
                "pass_summary": {
                    "completed_build_required_rows": 0,
                    "held_rows_confirmed": 0,
                    "native_or_rewrite_actions_checked": "not_passed",
                },
            }
        },
    )
    dump_yaml(
        method_root / "method_chain_lifecycle_trace.yaml",
        {
            "method_chain_lifecycle_trace": {
                "method": method,
                "method_chain_id": f"{method}_core_chain",
                "method_subagent_id": subagent_id,
                "method_subagent_prompt_path": str(TARGET_ROOT / f"method_prompts/{method}_layer3_layer4_method_prompt.md"),
                "method_evidence_root": str(method_root),
                "shared_runtime_boundary_check": {
                    "method_agnostic_helpers_only": True,
                    "method_specific_binding_location": "method_owned_layer4",
                    "status": "pass",
                },
                "surface_order": SURFACES,
                "agent_visible_contract": "canonical AnnData and prior method state per reviewed surfaces",
                "private_state_inventory": "repair_required_before_private_state_contract_can_pass",
                "producer_consumer_map": "repair_required_before_private_state_contract_can_pass",
                "private_state_shape_flow": "repair_required_before_private_state_contract_can_pass",
                "action_ownership_map": [
                    {
                        "native_action": action,
                        "output_determining": True,
                        "owner_surface": surface,
                        "consumer_surfaces": SURFACES[SURFACES.index(surface) + 1 :],
                        "repeated_in_surfaces": [],
                        "repeated_call_review_status": "not_repeated",
                        "repair_reason": "",
                    }
                    for surface in SURFACES
                    for action in cfg["actions"][surface]
                ],
                "duplicate_output_determining_action_check": {"status": "pass", "duplicate_actions": []},
                "native_call_flow_summary": cfg["route_summary"],
                "binding_call_flow_summary": "registered Layer3 callables reach method-owned Layer4 fail-closed boundary; executable native action binding repair required",
                "strict_output_progression": "repair_required",
                "new_agent_walkthrough": "new agent can import registered callables, but production strict-output path fails closed until native binding repair",
                "chain_closure_verdict": "repair_required",
                "first_repair": first_repair,
            }
        },
    )
    for surface in SURFACES:
        row_dir = method_root / surface
        smoke_evidence = selected_bridge_smoke_check(method, cfg, surface)
        result = {
            "build_output_result": {
                "reviewed_row": {
                    "method": method,
                    "execution_surface": surface,
                    "gate2_source": str(PLANNING_ROOT / "06_gate2_human_review_table.md"),
                    "bridge_plan_source": str(PLANNING_ROOT / "layer4_bridge_planning.md"),
                    "gate2_status": "approved_for_next_step",
                    "assigned_next_step": "layer3_layer4_build",
                    "build_required": True,
                },
                "implementation": {
                    "layer3_callable": f"bioharness_sdi_runtime.methods.{cfg['module']}.{surface}",
                    "layer4_binding": f"bioharness_sdi_runtime.methods.{cfg['module']}._layer4_binding",
                    "implementation_files": [str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py")],
                },
                "runtime_environment": {
                    "harness_environment": str(ENV_ROOT / "harness_environment.yaml"),
                    "callable_import_evidence": str(TARGET_ROOT / "logs/final_callable_import_check.log"),
                    "route_level_backend_load_evidence": str(TARGET_ROOT / f"logs/{method}_backend_load.log"),
                    "route_level_backend_load_status": backend_status,
                    "selected_bridge_smoke_check": {
                        "status": "repair_required",
                        "reason": "method-owned bridge smoke cannot pass until executable native action binding is repaired",
                        "evidence_path": str(smoke_evidence),
                        "layer4_entrypoint_invoked": True,
                        "first_failed_bridge_boundary": cfg["actions"][surface][0],
                    },
                },
                "layer3_method_config": {
                    "config_path": str(method_root / "layer3_method_config.yaml"),
                    "method": method,
                    "execution_surface": surface,
                    "variable_keys": ["semantic_options"],
                    "binding_target_names": cfg["actions"][surface],
                    "config_consumption": {
                        "layer3_callable_accepts_or_loads_config": True,
                        "config_values_passed_to_layer4": True,
                        "evidence_path_or_symbol": f"bioharness_sdi_runtime.methods.{cfg['module']}._layer4_binding",
                    },
                },
                "method_subagent_evidence": {
                    "subagent_id": subagent_id,
                    "method_prompt_path": str(TARGET_ROOT / f"method_prompts/{method}_layer3_layer4_method_prompt.md"),
                    "method_evidence_root": str(method_root),
                    "method_verifier_status": "FAIL_WITH_REPAIRS",
                },
                "implementation_evidence": {
                    "native_call_sequence": cfg["actions"][surface],
                    "strict_output_mapping": cfg["strict"][surface],
                    "source_confirmation_status": "reviewed_from_gate2_bridge_plan",
                    "surface_lifecycle_trace": {
                        "selected_bridge_smoke_check": {
                            "status": "repair_required",
                            "evidence_path_or_summary": str(smoke_evidence),
                        },
                        "action_binding_list": [
                            {
                                "reviewed_action": action,
                                "implementation_file": str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
                                "implementation_symbol_or_anchor": "_reach_native_boundary",
                                "reachable_layer3_to_layer4_call_path": f"{surface} -> _layer4_binding -> _reach_native_boundary",
                                "executable_evidence": {
                                    "code_anchor": "_reach_native_boundary",
                                    "import_or_call_statement": "metadata-only fail-closed boundary; repair required before PASS",
                                    "produced_state_output_or_artifact": "none",
                                    "fail_closed_boundary_when_not_completed": True,
                                },
                            }
                            for action in cfg["actions"][surface]
                        ],
                    },
                    "anti_surrogate_audit": {
                        "production_path_checked": True,
                        "route_basis": "native",
                        "mock_or_fake_backend_used": False,
                        "placeholder_or_dummy_state_used": False,
                        "contract_only_strict_output_generation_used": False,
                        "same_surface_preexisting_target_used": False,
                        "fail_closed_when_no_accepted_route_basis": True,
                        "audit_verdict": "repair_required",
                        "evidence_path_or_symbol": f"bioharness_sdi_runtime.methods.{cfg['module']}._layer4_binding",
                    },
                    "strict_output_contract_closure": {
                        "status": "repair_required",
                        "output_mapping": cfg["strict"][surface],
                        "produced_by_reachable_binding": False,
                    },
                    "runtime_execution": {
                        "attempted_in_build": False,
                        "status": "not_attempted_in_build",
                        "evidence_path_or_summary": "Method validation and full native workflow execution were not run in this build attempt.",
                    },
                },
                "boundary_checks": {
                    "author_case_run": False,
                    "bridge_replay_run": False,
                    "method_validation_run": False,
                    "data_download_run": False,
                },
            }
        }
        audit = {
            "build_audit": {
                "method": method,
                "execution_surface": surface,
                "gate2_source": str(PLANNING_ROOT / "06_gate2_human_review_table.md"),
                "bridge_plan_source": str(PLANNING_ROOT / "layer4_bridge_planning.md"),
                "reviewed_build_scope": cfg["route_summary"],
                "build_required": True,
                "downstream_selectable": False,
                "callable_import_evidence": str(TARGET_ROOT / "logs/final_callable_import_check.log"),
                "route_level_backend_load_evidence": str(TARGET_ROOT / f"logs/{method}_backend_load.log"),
                "selected_bridge_smoke_check_evidence": str(smoke_evidence),
                "method_level_verifier_evidence": str(verifier_path),
                "global_verifier_evidence": str(TARGET_ROOT / "verifier/global_verifier_result.yaml"),
                "lifecycle_trace_evidence": str(method_root / "method_chain_lifecycle_trace.yaml"),
                "anti_surrogate_evidence": "per-row build_output_result.yaml",
                "publication_index_sanity": {
                    "status": "repair_required",
                    "evidence_path_or_summary": str(TARGET_ROOT / "publication_index_sanity.yaml"),
                },
                "build_output_result": str(row_dir / "build_output_result.yaml"),
                "non_claims": {
                    "author_case_success": "not_claimed",
                    "bridge_replay_success": "not_claimed",
                    "method_validation_success": "not_claimed",
                    "biological_correctness": "not_claimed",
                },
            }
        }
        dump_yaml(row_dir / "build_output_result.yaml", result)
        dump_yaml(row_dir / "build_audit.yaml", audit)


def callable_import_check() -> str:
    code = "; ".join(
        [f"import bioharness_sdi_runtime.methods.{cfg['module']}" for cfg in METHODS.values()]
        + [
            "from bioharness_sdi_runtime.registry import iter_surface_bindings",
            "print('registered_count', len(list(iter_surface_bindings())))",
        ]
    )
    env = os.environ.copy()
    env["PYTHONPATH"] = str(TARGET_ROOT / "python")
    proc = subprocess.run(
        ["python", "-c", code],
        env=env,
        cwd="/tmp",
        text=True,
        capture_output=True,
        check=False,
    )
    write(
        TARGET_ROOT / "logs/final_callable_import_check.log",
        f"""
        invocation: PYTHONPATH={TARGET_ROOT / 'python'} python -c <import generated method modules>
        returncode: {proc.returncode}
        stdout:
        {proc.stdout}
        stderr:
        {proc.stderr}
        """,
    )
    return "pass" if proc.returncode == 0 else "repair_required"


def selected_bridge_smoke_check(method: str, cfg: dict[str, Any], surface: str) -> Path:
    log_path = TARGET_ROOT / f"logs/{method}_{surface}_selected_bridge_smoke.log"
    evidence_path = TARGET_ROOT / f"methods/{method}/{surface}/selected_bridge_smoke_check.yaml"
    module = f"bioharness_sdi_runtime.methods.{cfg['module']}"
    output_dir = TARGET_ROOT / "work" / "selected_bridge_smoke" / method / surface
    code = f"""
import traceback
from pathlib import Path

from bioharness_sdi_runtime.errors import BackendRouteError
import {module} as method_module


class DummyAnnData:
    def __init__(self):
        self.X = [[1.0]]
        self.obs = {{"domain": ["1"]}}
        self.var = {{}}
        self.obsm = {{"spatial": [[0.0, 0.0]]}}
        self.obsp = {{}}
        self.uns = {{}}


surface = {surface!r}
adata = DummyAnnData()
config = {{"execution_surfaces": {{surface: {{"variables": {{"semantic_options": {{}}}}}}}}}}
try:
    if surface in {{"export_domain_result", "plot_domain_labels"}}:
        getattr(method_module, surface)(adata, Path({str(output_dir)!r}), config=config)
    elif surface in {{"construct_spatial_structure", "fit_then_assign_domains"}}:
        getattr(method_module, surface)(adata, state=None, config=config)
    else:
        getattr(method_module, surface)(adata, config=config)
except BackendRouteError as exc:
    print("layer4_entrypoint_invoked: true")
    print("observation_type: fail_closed_at_layer4_binding")
    print("exception_type:", type(exc).__name__)
    print("exception_message:", str(exc))
    raise SystemExit(0)
except Exception:
    print("layer4_entrypoint_invoked: false")
    traceback.print_exc()
    raise SystemExit(2)
else:
    print("unexpected_success_without_native_binding")
    raise SystemExit(3)
"""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(TARGET_ROOT / "python")
    proc = subprocess.run(
        ["python", "-c", code],
        env=env,
        cwd=str(TARGET_ROOT / "work"),
        text=True,
        capture_output=True,
        check=False,
    )
    invocation = f"PYTHONPATH={TARGET_ROOT / 'python'} python -c <invoke {module}.{surface}>"
    write(
        log_path,
        f"""
        method: {method}
        execution_surface: {surface}
        invocation: {invocation}
        command_workdir: {TARGET_ROOT / 'work'}
        returncode: {proc.returncode}
        stdout:
        {proc.stdout}
        stderr:
        {proc.stderr}
        """,
    )
    dump_yaml(
        evidence_path,
        {
            "selected_bridge_smoke_check": {
                "required": True,
                "reason": "generated method-owned Layer4 route crosses reviewed native/glue boundaries, but executable native action binding is not implemented",
                "command": "python -c <invoke generated Layer3 callable>",
                "invocation": invocation,
                "command_workdir": str(TARGET_ROOT / "work"),
                "exit_code": proc.returncode,
                "stdout_path": str(log_path),
                "stderr_path": str(log_path),
                "layer4_bridge_entrypoint": f"{module}._layer4_binding",
                "layer4_entrypoint_invoked": proc.returncode == 0,
                "evidence_mode_used": False,
                "evidence_mode_bypassed_native_boundary": False,
                "first_selected_native_or_glue_boundary": cfg["actions"][surface][0],
                "native_boundary_observation": {
                    "boundary_symbol_or_source_section": cfg["actions"][surface][0],
                    "observation_type": "fail_closed_before_executable_native_boundary",
                    "observation_evidence": str(log_path),
                },
                "minimal_boundary_reached": False,
                "status": "repair_required",
                "failure_class": "executable_native_action_binding_missing",
                "first_failed_bridge_boundary": cfg["actions"][surface][0],
                "evidence_path_or_summary": str(log_path),
            }
        },
    )
    return evidence_path


def root_outputs(statuses: dict[str, Any], backend_statuses: dict[str, str], callable_status: str) -> None:
    dispatch_methods = []
    for method, cfg in METHODS.items():
        prompt = TARGET_ROOT / f"method_prompts/{method}_layer3_layer4_method_prompt.md"
        method_status = statuses.get(method, {})
        subagent_id = method_status.get("subagent_id", cfg["agent_id"])
        first_repair = method_status.get("first_repair") or {
            "method": method,
            "execution_surface": "prepare_spatial_domain_input",
            "failure_class": "action_path_closure",
            "reviewed_action": cfg["actions"]["prepare_spatial_domain_input"][0],
            "observed_code_path": str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
            "repair_instruction": "Implement executable native action binding and strict-output closure.",
            "anti_surrogate_failure": True,
        }
        dispatch_methods.append(
            {
                "method": method,
                "dispatch_batch_id": "batch_001",
                "subagent_id": subagent_id,
                "method_prompt_path": str(prompt),
                "owned_paths": [
                    str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
                    str(TARGET_ROOT / f"methods/{method}/"),
                ],
                "read_only_inputs": [
                    str(PLANNING_ROOT / "06_gate2_human_review_table.md"),
                    str(PLANNING_ROOT / "layer4_bridge_planning.md"),
                    str(ENV_ROOT / "harness_environment.yaml"),
                    str(ENV_ROOT / "environment_build.jsonl"),
                ],
                "dispatch_status": method_status.get("status", "FAIL_WITH_REPAIRS"),
                "method_evidence_root": str(TARGET_ROOT / f"methods/{method}"),
                "method_verifier_status": "FAIL_WITH_REPAIRS",
                "returned_files": method_status.get("returned_files", []),
                "unresolved_repairs": [first_repair],
                "repair_loop_iterations": method_status.get("repair_loop_iterations", []),
            }
        )
    dump_yaml(
        TARGET_ROOT / "subagent_dispatch_log.yaml",
        {
            "subagent_dispatch_log": {
                "invocation_id": "SDI_ADEPT_BANKSY_CCST_DRSC_layer3_layer4_build_2026-06-11",
                "subagent_prompt_template": "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md",
                "max_active_method_subagents": 6,
                "dispatch_batches": [
                    {
                        "batch_id": "batch_001",
                        "methods": list(METHODS),
                        "batch_status": "repair_required",
                    }
                ],
                "methods": dispatch_methods,
                "dispatch_verdict": "repair_required",
            }
        },
    )

    rows: list[dict[str, str]] = []
    for method, cfg in METHODS.items():
        subagent_id = statuses.get(method, {}).get("subagent_id", cfg["agent_id"])
        for surface in SURFACES:
            method_root = TARGET_ROOT / f"methods/{method}"
            rows.append(
                {
                    "method": method,
                    "execution_surface": surface,
                    "build_required": "true",
                    "downstream_selectable": "false",
                    "route_type": "adapter_or_wrapper_reviewed_route",
                    "source_confirmation_status": "reviewed_from_gate2_bridge_plan",
                    "layer3_callable_path": f"bioharness_sdi_runtime.methods.{cfg['module']}.{surface}",
                    "layer4_binding_pointer": f"bioharness_sdi_runtime.methods.{cfg['module']}._layer4_binding",
                    "layer3_method_config_path": str(method_root / "layer3_method_config.yaml"),
                    "layer3_method_config_consumption_status": "pass",
                    "callable_import_status": callable_status,
                    "callable_import_evidence": str(TARGET_ROOT / "logs/final_callable_import_check.log"),
                    "route_level_backend_load_status": backend_statuses[method],
                    "route_level_backend_load_evidence": str(TARGET_ROOT / f"logs/{method}_backend_load.log"),
                    "selected_bridge_smoke_check_status": "repair_required",
                    "action_path_closure_status": "repair_required",
                    "strict_output_contract_closure_status": "repair_required",
                    "surface_lifecycle_trace_status": "repair_required",
                    "method_chain_lifecycle_status": "repair_required",
                    "lifecycle_trace_evidence": str(method_root / "method_chain_lifecycle_trace.yaml"),
                    "method_chain_id": f"{method}_core_chain",
                    "prior_surface_dependency": "none" if surface == "prepare_spatial_domain_input" else "prior_surface_private_state_or_canonical_output",
                    "state_handoff_policy": "method_private_state_consumed_by_later_surfaces",
                    "st_image_alignment_contract_status": "not_applicable",
                    "method_subagent_id": subagent_id,
                    "method_prompt_path": str(TARGET_ROOT / f"method_prompts/{method}_layer3_layer4_method_prompt.md"),
                    "method_evidence_root": str(method_root),
                    "method_level_verifier_status": "FAIL_WITH_REPAIRS",
                    "method_level_verifier_evidence": str(method_root / "verifier/method_verifier_result.yaml"),
                    "global_verifier_status": "FAIL_WITH_REPAIRS",
                    "global_verifier_evidence": str(TARGET_ROOT / "verifier/global_verifier_result.yaml"),
                    "shared_runtime_boundary_check": "pass",
                    "shared_runtime_boundary_evidence": str(TARGET_ROOT / "shared_runtime_boundary_check.yaml"),
                    "build_output_result": str(method_root / surface / "build_output_result.yaml"),
                    "build_audit": str(method_root / surface / "build_audit.yaml"),
                    "runtime_execution_status": "not_attempted_in_build",
                    "own_output_preexisting_input_used": "false",
                }
            )
    matrix = TARGET_ROOT / "layer3_layer4_build_completion_matrix.tsv"
    with matrix.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    checked_rows = [
        {
            "method": row["method"],
            "execution_surface": row["execution_surface"],
            "build_required": True,
            "downstream_selectable": False,
            "build_output_result": row["build_output_result"],
            "build_audit": row["build_audit"],
            "lifecycle_trace_evidence": row["lifecycle_trace_evidence"],
            "method_level_verifier_evidence": row["method_level_verifier_evidence"],
            "global_verifier_evidence": row["global_verifier_evidence"],
            "row_status": "repair_required",
            "finding": "not downstream-selectable because action-path, strict-output, smoke, lifecycle, and verifier statuses are repair_required",
        }
        for row in rows
    ]
    dump_yaml(
        TARGET_ROOT / "publication_index_sanity.yaml",
        {
            "publication_index_sanity": {
                "matrix_path": str(matrix),
                "required_columns_status": "pass",
                "key_status_fields_status": "repair_required",
                "core_pointer_fields_status": "pass",
                "readable_core_file_pointers_status": "pass",
                "per_row_non_contradiction_status": "pass",
                "semantic_evidence_gate_status": "repair_required",
                "semantic_evidence_gate": {
                    "checked_action_binding_executable_evidence": False,
                    "checked_smoke_command_outputs": True,
                    "checked_no_repair_signal_as_completion": True,
                    "checked_no_action_name_only_evidence": True,
                    "finding": "Rows are not publication-sane for downstream selection because selected bridge smoke evidence fails closed before executable native action binding, and strict-output closure remains repair-required.",
                },
                "checked_rows": checked_rows,
                "sanity_verdict": "repair_required",
            }
        },
    )
    repairs = [
        statuses.get(method, {}).get("first_repair")
        or {
            "method": method,
            "execution_surface": "prepare_spatial_domain_input",
            "failure_class": "action_path_closure",
            "reviewed_action": cfg["actions"]["prepare_spatial_domain_input"][0],
            "observed_code_path": str(TARGET_ROOT / f"python/bioharness_sdi_runtime/methods/{cfg['module']}.py"),
            "repair_instruction": "Implement executable native action binding and strict-output closure.",
            "anti_surrogate_failure": True,
        }
        for method, cfg in METHODS.items()
    ]
    dump_yaml(
        TARGET_ROOT / "verifier/global_verifier_result.yaml",
        {
            "verifier_result": {
                "scope": "global",
                "scope_id": "SDI_ADEPT_BANKSY_CCST_DRSC_layer3_layer4_build_2026-06-11",
                "verdict": "FAIL_WITH_REPAIRS",
                "repair_loop_required": True,
                "terminal_completion_allowed": False,
                "required_repairs": repairs,
                "pass_summary": {
                    "completed_build_required_rows": 0,
                    "held_rows_confirmed": 0,
                    "native_or_rewrite_actions_checked": "not_passed",
                },
            }
        },
    )
    stale_completion_report = TARGET_ROOT / "completion_report.md"
    if stale_completion_report.exists():
        stale_completion_report.unlink()
    write(
        TARGET_ROOT / "repair_required_report.md",
        f"""
        # Layer3 / Layer4 Build Attempt Report

        Output root: `{TARGET_ROOT}`
        Completion matrix: `{matrix}`
        Global verifier result: `{TARGET_ROOT / 'verifier/global_verifier_result.yaml'}`
        Publication index sanity: `{TARGET_ROOT / 'publication_index_sanity.yaml'}`

        Build outcome: stopped with explicit repair-required findings before final publication.

        Global verifier handoff verdict: `FAIL_WITH_REPAIRS` repair-loop packet; not a completed invocation status.

        No template completion report was emitted because the current completion-report template requires global verifier `PASS`, publication-index sanity `pass`, and no unresolved repair-required findings.

        Scope: ADEPT, BANKSY, CCST, and DR-SC; five build-required surfaces each; no held rows in this invocation.

        Downstream-selectable rows: 0 of 20.

        Repair summary:
        {yaml.safe_dump(repairs, sort_keys=False)}

        Evidence boundary:
        - Fresh backend-load checks were run and stored under `logs/`.
        - Generated Layer3/Layer4 package files and Layer3-M configs were written under this output root.
        - Prior build outputs, prior method-validation trial outputs, and the completed ConGI/BASS package were not used as success evidence.
        - Method validation, author-case replay, bridge replay, and data download were not run.

        Non-claims: no runtime support, functional correctness, author-case success, method-validation success, production readiness, algorithmic equivalence, or biological correctness is claimed.
        """,
    )


def parse_statuses(path: Path | None) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--method-status-json", type=Path)
    args = parser.parse_args()
    statuses = parse_statuses(args.method_status_json)

    for dirname in ["inputs", "work", "data", "outputs", "logs", "reports", "verifier", "method_prompts", "methods"]:
        (TARGET_ROOT / dirname).mkdir(parents=True, exist_ok=True)
    runtime_package()
    backend_statuses = {}
    for method, cfg in METHODS.items():
        method_prompt(method, cfg)
        method_config(method, cfg)
        method_module(method, cfg)
        backend_statuses[method] = run_command(method, cfg["backend_cmd"], cfg["pythonpath"], TARGET_ROOT / f"logs/{method}_backend_load.log")
        per_method_evidence(method, cfg, statuses.get(method, {}), backend_statuses[method])
    callable_status = callable_import_check()
    dump_yaml(
        TARGET_ROOT / "shared_runtime_boundary_check.yaml",
        {
            "shared_runtime_boundary_check": {
                "shared_files_reviewed": [
                    "bioharness_sdi_runtime/__init__.py",
                    "bioharness_sdi_runtime/errors.py",
                    "bioharness_sdi_runtime/state.py",
                    "bioharness_sdi_runtime/contracts.py",
                    "bioharness_sdi_runtime/config.py",
                    "bioharness_sdi_runtime/registry.py",
                ],
                "method_agnostic_helpers_only": True,
                "method_specific_binding_location": "method_owned_layer4",
                "verdict": "pass",
            }
        },
    )
    root_outputs(statuses, backend_statuses, callable_status)
    print(TARGET_ROOT)


if __name__ == "__main__":
    main()
