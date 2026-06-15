#!/usr/bin/env python3
"""Run Stage3 method_harness_validation orchestration for the SDI six-method package."""

from __future__ import annotations

import argparse
import csv
import importlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback
from typing import Any

import yaml


METHODS = ["ADEPT", "BANKSY", "BASS", "CCST", "ConGI", "DR-SC"]
SURFACE_ORDER_FALLBACK = {
    "ADEPT": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result", "plot_domain_labels"],
    "BANKSY": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result", "plot_domain_labels"],
    "BASS": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result"],
    "CCST": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result", "plot_domain_labels"],
    "ConGI": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result"],
    "DR-SC": ["prepare_spatial_domain_input", "construct_spatial_structure", "fit_then_assign_domains", "export_domain_result", "plot_domain_labels"],
}


def read_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=False)


def nested(data: Any, keys: list[str], default: Any = None) -> Any:
    cur = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def existing(path_text: str | None) -> bool:
    return bool(path_text) and Path(path_text).exists()


def load_chain(build_root: Path, method: str) -> list[str]:
    trace_path = build_root / "methods" / method / "method_chain_lifecycle_trace.yaml"
    if not trace_path.exists():
        return SURFACE_ORDER_FALLBACK[method]
    trace = read_yaml(trace_path)
    root = trace.get("method_chain_lifecycle_trace", trace)
    return list(root.get("surface_order") or SURFACE_ORDER_FALLBACK[method])


def reviewed_conda_invocation(conda_prefix: Path, build_root: Path) -> dict[str, Any]:
    return {
        "conda_prefix": str(conda_prefix),
        "python_executable": str(conda_prefix / "bin" / "python"),
        "rscript_executable": str(conda_prefix / "bin" / "Rscript"),
        "command_pattern": f"env LD_LIBRARY_PATH={conda_prefix}/lib PYTHONPATH={build_root} conda run -p {conda_prefix} python <stage3_runner>",
        "environment": {
            "LD_LIBRARY_PATH": str(conda_prefix / "lib"),
            "PYTHONPATH": str(build_root),
            "PATH_PREFIX": str(conda_prefix / "bin"),
        },
    }


def base_surface_config(method: str, method_out: Path) -> dict[str, Any]:
    export_path = method_out / "outputs" / "harness" / "domain_labels.csv"
    plot_dir = method_out / "outputs" / "harness" / "plots"
    if method == "ADEPT":
        return {
            "prepare_spatial_domain_input": {"coordinate_key": "spatial"},
            "construct_spatial_structure": {"radius": 400},
            "fit_then_assign_domains": {"num_cluster": 7, "random_seed": 0, "device_id": "0", "n_epochs": 1000},
            "export_domain_result": {"output_path": str(export_path)},
            "plot_domain_labels": {"output_dir": str(plot_dir)},
        }
    if method == "BANKSY":
        return {
            "prepare_spatial_domain_input": {"coord_key": "spatial", "spatial_obsm_key": "spatial"},
            "construct_spatial_structure": {
                "num_neighbours": 15,
                "lambda_list": [0.2],
                "max_m": 1,
                "nbr_weight_decay": "scaled_gaussian",
            },
            "fit_then_assign_domains": {
                "pca_dims": [20],
                "resolutions": [0.7],
                "partition_seed": 1234,
                "num_nn": 50,
                "num_iterations": -1,
            },
            "export_domain_result": {"output_path": str(export_path)},
            "plot_domain_labels": {"output_dir": str(plot_dir)},
        }
    if method == "BASS":
        return {
            "prepare_spatial_domain_input": {"section_key": "spatialLIBD_p1"},
            "construct_spatial_structure": {"spatial_context_key": "spatial_context"},
            "fit_then_assign_domains": {"domain_key": "domain"},
            "export_domain_result": {"output_path": str(export_path)},
        }
    if method == "CCST":
        return {
            "prepare_spatial_domain_input": {"data_family": "MERFISH"},
            "construct_spatial_structure": {"spatial_connectivities_key": "spatial_connectivities"},
            "fit_then_assign_domains": {"domain_key": "domain", "n_clusters": 5},
            "export_domain_result": {"output_path": str(export_path)},
            "plot_domain_labels": {"output_dir": str(plot_dir)},
        }
    if method == "ConGI":
        return {
            "prepare_spatial_domain_input": {"library_id": "151509", "img_key": "hires"},
            "construct_spatial_structure": {"spatial_context_key": "spatial_context"},
            "fit_then_assign_domains": {"domain_key": "domain", "n_clusters": 7, "batch_size": 32},
            "export_domain_result": {"output_path": str(export_path)},
        }
    if method == "DR-SC":
        return {
            "prepare_spatial_domain_input": {"platform_family": "Visium"},
            "construct_spatial_structure": {"spatial_connectivities_key": "spatial_connectivities"},
            "fit_then_assign_domains": {"domain_key": "domain", "candidate_k": 7},
            "export_domain_result": {"output_path": str(export_path)},
            "plot_domain_labels": {"output_dir": str(plot_dir)},
        }
    raise KeyError(method)


def source_resolution_notes(method: str) -> dict[str, Any]:
    notes = {
        "ADEPT": {
            "construct_spatial_structure.radius": "Stage2 native command --radius 400.",
            "fit_then_assign_domains.num_cluster": "Stage2 native command --cluster_num 7; normalized to Layer3-M num_cluster.",
            "fit_then_assign_domains.random_seed": "Stage2 author_parameter_fidelity records train_ADEPT_use_DE random_seed=0.",
            "prepare_spatial_domain_input.coordinate_key": "Canonical input schema uses adata.obsm['spatial']; Stage2 reports canonical input unchanged.",
        },
        "BANKSY": {
            "construct_spatial_structure.num_neighbours": "Stage2 tutorial evidence records k_geom=15.",
            "construct_spatial_structure.lambda_list": "Stage2 actual_execution_parameters records lambda_list=[0.2].",
            "fit_then_assign_domains.resolutions": "Stage2 actual_execution_parameters records resolutions=[0.7].",
            "fit_then_assign_domains.partition_seed": "Stage2 actual_execution_parameters records partition_seed=1234.",
            "prepare_spatial_domain_input.coord_key": "Canonical input schema uses adata.obsm['spatial']; Stage2 reports canonical input unchanged.",
        },
        "BASS": {
            "prepare_spatial_domain_input.section_key": "Stage2 author case is spatialLIBD_p1.RData.",
            "fit_then_assign_domains.domain_key": "Layer3-M selected canonical result field is adata.obs['domain'].",
        },
        "CCST": {
            "prepare_spatial_domain_input.data_family": "Stage2 author parameters data_name=MERFISH/data_type=sc.",
            "fit_then_assign_domains.n_clusters": "Stage2 author_default_or_tutorial_parameters records n_clusters=5.",
            "fit_then_assign_domains.domain_key": "Layer3-M selected canonical result field is adata.obs['domain'].",
        },
        "ConGI": {
            "prepare_spatial_domain_input.library_id": "Stage1/Stage2 canonical route uses 10x Visium library 151509.",
            "prepare_spatial_domain_input.img_key": "Stage1 materialized hires/lowres image payload; hires selected as method-facing image selector.",
            "fit_then_assign_domains.n_clusters": "Stage2 reference describes n_clusters derived from metadata and preserved in patched mclust route.",
            "fit_then_assign_domains.batch_size": "Stage2 GPU resource retry accepted batch_size=32.",
        },
        "DR-SC": {
            "prepare_spatial_domain_input.platform_family": "Stage2 DLPFC vignette evidence records platform='Visium'.",
            "fit_then_assign_domains.candidate_k": "Stage2 DLPFC vignette evidence records K=7.",
            "fit_then_assign_domains.domain_key": "Layer3-M selected canonical result field is adata.obs['domain'].",
        },
    }
    return notes[method]


def read_table(path: Path) -> tuple[list[dict[str, str]], str | None, str | None]:
    delimiter = "\t" if path.suffix.lower() in {".tsv", ".txt"} else ","
    with path.open("r", encoding="utf-8") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        if "\t" in sample and sample.count("\t") >= sample.count(","):
            delimiter = "\t"
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = [dict(row) for row in reader]
    if not rows:
        return rows, None, None
    columns = list(rows[0].keys())
    id_candidates = ["obs_id", "observation_id", "spot_id", "cell_id", "barcode", "index", "id"]
    result_candidates = ["domain", "cluster", "label", "cluster_label", "cluster_labels", "congi_cluster_label", "spatial.drsc.cluster"]
    id_field = next((c for c in columns if c in id_candidates), columns[0])
    result_field = next((c for c in columns if c in result_candidates), columns[-1])
    return rows, id_field, result_field


def compare_tables(reference_path: Path, harness_path: Path) -> dict[str, Any]:
    ref_rows, ref_id, ref_result = read_table(reference_path)
    har_rows, har_id, har_result = read_table(harness_path)
    ref_map = {str(row[ref_id]): str(row[ref_result]) for row in ref_rows if ref_id in row and ref_result in row}
    har_map = {str(row[har_id]): str(row[har_result]) for row in har_rows if har_id in row and har_result in row}
    shared = sorted(set(ref_map) & set(har_map))
    exact = None
    ari = None
    metric_records: list[dict[str, Any]] = []
    if shared:
        ref_vec = [ref_map[key] for key in shared]
        har_vec = [har_map[key] for key in shared]
        exact = sum(1 for a, b in zip(ref_vec, har_vec) if a == b) / len(shared)
        metric_records.append({
            "formula_or_function": "sum(reference_label == harness_label) / shared_count",
            "package": "python standard library",
            "version": sys.version.split()[0],
            "call_signature": "exact_label_match_fraction(reference_vector, harness_vector)",
            "input_vectors": {"reference": ref_result, "harness": har_result, "shared_count": len(shared)},
            "preprocessing": "Labels coerced to strings after inner join by observation id.",
            "value": exact,
            "reason_when_not_computed": None,
        })
        try:
            from sklearn.metrics import adjusted_rand_score

            ari = float(adjusted_rand_score(ref_vec, har_vec))
            metric_records.append({
                "formula_or_function": "sklearn.metrics.adjusted_rand_score",
                "package": "scikit-learn",
                "version": importlib.import_module("sklearn").__version__,
                "call_signature": "adjusted_rand_score(reference_vector, harness_vector)",
                "input_vectors": {"reference": ref_result, "harness": har_result, "shared_count": len(shared)},
                "preprocessing": "Labels coerced to strings after inner join by observation id.",
                "value": ari,
                "reason_when_not_computed": None,
            })
        except Exception as exc:
            metric_records.append({
                "formula_or_function": "sklearn.metrics.adjusted_rand_score",
                "package": "scikit-learn",
                "version": None,
                "call_signature": "adjusted_rand_score(reference_vector, harness_vector)",
                "input_vectors": {"reference": ref_result, "harness": har_result, "shared_count": len(shared)},
                "preprocessing": "Labels coerced to strings after inner join by observation id.",
                "value": None,
                "reason_when_not_computed": repr(exc),
            })
    return {
        "evidence": {
            "reference_file": str(reference_path),
            "reference_load_result": {"status": "pass", "row_count": len(ref_rows), "id_field": ref_id, "result_field": ref_result},
            "harness_file": str(harness_path),
            "harness_load_result": {"status": "pass", "row_count": len(har_rows), "id_field": har_id, "result_field": har_result},
            "shared_name_comparison": {
                "shared_id_field": {"reference": ref_id, "harness": har_id},
                "reference_count": len(ref_map),
                "harness_count": len(har_map),
                "shared_count": len(shared),
                "reference_only_count": len(set(ref_map) - set(har_map)),
                "harness_only_count": len(set(har_map) - set(ref_map)),
            },
            "metric_records": metric_records,
        },
        "judgment": {
            "conclusion": "consistent" if shared and (ari is not None and ari >= 0.99 or exact == 1.0) else "inconsistent",
            "reason": "Judgment is based on loaded reference and harness tables joined by observation id.",
            "uncertainty_or_limits": "Metric comparison validates harness output behavior against Stage2 reference labels; it does not establish biological correctness or algorithmic equivalence.",
        },
    }


def _write_intermediate_adata(adata: Any, path: Path, repair_attempts: list[dict[str, Any]], surface: str) -> str | None:
    if not hasattr(adata, "write_h5ad"):
        return None
    try:
        adata.write_h5ad(path)
        return str(path)
    except Exception as exc:
        repaired = adata.copy()
        root = repaired.uns.get("_bioharness_private") if hasattr(repaired, "uns") else None
        if isinstance(root, dict):
            repaired.uns["_bioharness_private_serialization_repr"] = repr(root)
            del repaired.uns["_bioharness_private"]
            try:
                repaired.write_h5ad(path)
                repair_attempts.append({
                    "surface": surface,
                    "repair_class": "serialization",
                    "status": "repaired",
                    "reason": f"Original AnnData write failed on private-state serialization: {type(exc).__name__}: {exc}",
                    "action": "Wrote an intermediate h5ad copy with uns['_bioharness_private'] represented as text; in-memory object used for subsequent surfaces was unchanged.",
                    "artifact": str(path),
                })
                return str(path)
            except Exception as retry_exc:
                repair_attempts.append({
                    "surface": surface,
                    "repair_class": "serialization",
                    "status": "failed",
                    "reason": f"{type(retry_exc).__name__}: {retry_exc}",
                })
        raise


def _attempt_adept_ground_truth_alias(adata: Any, repair_attempts: list[dict[str, Any]]) -> bool:
    if not hasattr(adata, "obs") or "Ground Truth" in adata.obs:
        return False
    candidates = ["annotation_Annotation", "label", "Annotation", "annotation"]
    for column in candidates:
        if column in adata.obs:
            adata.obs["Ground Truth"] = adata.obs[column].astype(str)
            repair_attempts.append({
                "surface": "fit_then_assign_domains",
                "repair_class": "field_alias",
                "status": "repaired",
                "reason": "ADEPT native fit requires adata.obs['Ground Truth'] for ARI bookkeeping.",
                "action": f"Aliased existing canonical obs column {column!r} to 'Ground Truth' before one retry.",
            })
            return True
    repair_attempts.append({
        "surface": "fit_then_assign_domains",
        "repair_class": "field_alias",
        "status": "failed",
        "reason": "No canonical annotation-like obs column was available for ADEPT Ground Truth alias.",
    })
    return False


def invoke_chain(method: str, build_root: Path, canonical_input: Path, surface_config: dict[str, Any], chain: list[str], method_out: Path) -> dict[str, Any]:
    sys.path.insert(0, str(build_root))
    import anndata as ad

    from spatial_domain_identification.registry import get_callable

    logs_dir = method_out / "logs"
    harness_dir = method_out / "outputs" / "harness"
    logs_dir.mkdir(parents=True, exist_ok=True)
    harness_dir.mkdir(parents=True, exist_ok=True)
    adata = ad.read_h5ad(canonical_input)
    current: Any = adata
    state: Any = None
    invocations = []
    repair_attempts: list[dict[str, Any]] = []
    produced_artifact: str | None = None
    reason_if_not_produced: str | None = None
    status = "pass"

    for surface in chain:
        fn = get_callable(method, surface)
        cfg = dict(surface_config.get(surface) or {})
        started = time.time()
        output_artifact = None
        entry: dict[str, Any] = {
            "surface": surface,
            "callable_or_command": f"spatial_domain_identification.registry.get_callable({method!r}, {surface!r})",
            "config": cfg,
            "status": "failed",
            "output_artifact": None,
            "reason": None,
            "environment": {
                "python": sys.executable,
                "LD_LIBRARY_PATH": os.environ.get("LD_LIBRARY_PATH"),
                "PYTHONPATH": os.environ.get("PYTHONPATH"),
            },
            "workdir": str(method_out),
            "logs": {"traceback": str(logs_dir / f"{surface}_traceback.log")},
            "return_code": None,
        }
        try:
            if surface == "export_domain_result":
                output_path = Path(cfg.get("output_path") or harness_dir / "domain_labels.csv")
                if method in {"ADEPT"}:
                    result = fn(current, output_path=output_path, config=cfg, state=state)
                elif method in {"BANKSY"}:
                    result = fn(current, output_path=output_path, config=cfg)
                else:
                    result = fn(current, output_path, config=cfg)
                if isinstance(result, tuple):
                    output_artifact, state = result
                else:
                    output_artifact = result
                produced_artifact = str(output_artifact)
                current = current
            elif surface == "plot_domain_labels":
                output_dir = Path(cfg.get("output_dir") or harness_dir / "plots")
                if method in {"ADEPT"}:
                    result = fn(current, output_dir=output_dir, config=cfg, state=state)
                    if isinstance(result, tuple):
                        output_artifact, state = result
                    else:
                        output_artifact = result
                elif method in {"BANKSY"}:
                    output_artifact = fn(current, output_dir=output_dir, config=cfg)
                else:
                    output_artifact = fn(current, output_dir, config=cfg)
            else:
                if method == "ADEPT":
                    try:
                        result = fn(current, config=cfg, state=state)
                    except Exception as exc:
                        if surface == "fit_then_assign_domains" and "Ground Truth" in str(exc) and _attempt_adept_ground_truth_alias(current, repair_attempts):
                            result = fn(current, config=cfg, state=state)
                        else:
                            raise
                    if isinstance(result, tuple) and len(result) == 2:
                        current, state = result
                    else:
                        current = result
                else:
                    current = fn(current, config=cfg)
                output_artifact = _write_intermediate_adata(current, harness_dir / f"{surface}_adata.h5ad", repair_attempts, surface)
            entry["status"] = "pass"
            entry["output_artifact"] = stringify(output_artifact)
            entry["return_code"] = 0
        except Exception as exc:
            status = "failed"
            reason_if_not_produced = f"{type(exc).__name__}: {exc}"
            with Path(entry["logs"]["traceback"]).open("w", encoding="utf-8") as handle:
                traceback.print_exc(file=handle)
            entry["status"] = "failed"
            entry["reason"] = reason_if_not_produced
            entry["return_code"] = 1
            invocations.append(entry)
            break
        finally:
            entry["duration_seconds"] = round(time.time() - started, 3)
        invocations.append(entry)

    return {
        "status": status,
        "surface_invocations": invocations,
        "produced_artifact": produced_artifact,
        "reason_if_not_produced": reason_if_not_produced,
        "attempted_repairs": repair_attempts,
    }


def stringify(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): stringify(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [stringify(v) for v in value]
    return value


def generate_prompt(path: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Method Harness Validation Prompt",
        "",
        "This prompt was instantiated by the Stage3 package orchestration runner.",
        "",
        "```yaml",
        yaml.safe_dump(data, sort_keys=False, allow_unicode=False).rstrip(),
        "```",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run_method_subprocess(script_path: Path, args: argparse.Namespace, method: str) -> int:
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = f"{args.conda_prefix}/lib"
    env["PYTHONPATH"] = str(args.build_root)
    env["PATH"] = f"{args.conda_prefix}/bin:{env.get('PATH', '')}"
    cmd = [
        "conda",
        "run",
        "-p",
        str(args.conda_prefix),
        "python",
        str(script_path),
        "method",
        "--method", method,
        "--stage1-root", str(args.stage1_root),
        "--stage2-root", str(args.stage2_root),
        "--build-root", str(args.build_root),
        "--env-root", str(args.env_root),
        "--conda-prefix", str(args.conda_prefix),
        "--output-root", str(args.output_root),
    ]
    log_dir = Path(args.output_root) / method / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    with (log_dir / "method_subagent_stdout.log").open("w", encoding="utf-8") as out, (log_dir / "method_subagent_stderr.log").open("w", encoding="utf-8") as err:
        proc = subprocess.run(cmd, cwd=str(args.output_root), env=env, text=True, stdout=out, stderr=err, check=False)
    return proc.returncode


def method_mode(args: argparse.Namespace) -> int:
    method = args.method
    stage1_result_path = Path(args.stage1_root) / method / "validation_input_preparation_result.yaml"
    stage2_result_path = Path(args.stage2_root) / method / "validation_reference_preparation_result.yaml"
    build_root = Path(args.build_root)
    env_root = Path(args.env_root)
    out_root = Path(args.output_root)
    method_out = out_root / method
    method_out.mkdir(parents=True, exist_ok=True)

    stage1 = read_yaml(stage1_result_path)["validation_input_preparation_result"]
    stage2 = read_yaml(stage2_result_path)["validation_reference_preparation_result"]
    canonical = Path(stage1["canonical_input_record"]["path"])
    primary = stage2.get("reference_artifacts", {}).get("primary", {})
    reference_field = "reference_artifacts.primary.standardized_artifact" if primary.get("standardized_artifact") else "reference_artifacts.primary.raw_artifact"
    reference_path = Path(primary.get("standardized_artifact") or primary.get("raw_artifact"))
    chain = load_chain(build_root, method)
    layer3_config_path = build_root / "methods" / method / "layer3_method_config.yaml"
    surface_config_path = method_out / "method_harness_validation_surface_config.yaml"
    prompt_path = method_out / "prompts" / "method_harness_validation_prompt.md"
    candidate_path = method_out / "method_harness_validation_candidate_result.yaml"
    config_doc = read_yaml(surface_config_path)
    surface_config = config_doc["surface_config"]
    conda_invocation = reviewed_conda_invocation(Path(args.conda_prefix), build_root)

    data_load = {"status": "not_attempted"}
    ref_load = {"status": "not_attempted"}
    surface_config_load = {"status": "pass", "path": str(surface_config_path)}
    required_fields = {"AnnData": ["X", "obs", "var", "obsm", "obs_names"]}
    try:
        import anndata as ad

        adata = ad.read_h5ad(canonical)
        data_load = {"status": "pass", "n_obs": int(adata.n_obs), "n_vars": int(adata.n_vars), "obsm_keys": list(adata.obsm.keys()), "obs_columns": list(map(str, adata.obs.columns))}
    except Exception as exc:
        data_load = {"status": "failed", "reason": repr(exc)}
    try:
        rows, id_field, result_field = read_table(reference_path)
        ref_load = {"status": "pass", "row_count": len(rows), "id_field": id_field, "result_field": result_field}
    except Exception as exc:
        ref_load = {"status": "failed", "reason": repr(exc)}

    invocation = invoke_chain(method, build_root, canonical, surface_config, chain, method_out)
    produced = bool(invocation.get("produced_artifact") and Path(invocation["produced_artifact"]).exists())
    comparison_ready = produced and invocation["produced_artifact"].endswith(".csv")
    result_comparison: dict[str, Any]
    candidate_status = "TERMINAL_FAIL"
    if comparison_ready:
        try:
            result_comparison = compare_tables(reference_path, Path(invocation["produced_artifact"]))
            candidate_status = "PASS"
        except Exception as exc:
            result_comparison = {
                "required_when": "candidate_workflow_status == PASS",
                "not_applicable_reason": f"comparison load failed after harness artifact production: {type(exc).__name__}: {exc}",
                "evidence": {},
                "judgment": {},
            }
            candidate_status = "TERMINAL_FAIL"
    else:
        result_comparison = {
            "required_when": "candidate_workflow_status == PASS",
            "not_applicable_reason": "No comparison-ready harness result was produced after selected Layer3 invocation evidence was recorded.",
            "evidence": {
                "reference_file": str(reference_path),
                "reference_load_result": ref_load,
                "harness_file": invocation.get("produced_artifact"),
                "harness_load_result": {"status": "not_loaded", "reason": invocation.get("reason_if_not_produced")},
                "shared_name_comparison": None,
                "metric_records": [],
            },
            "judgment": {},
        }

    candidate = {
        "method_harness_validation_candidate_result": {
            "method": method,
            "stage_handoff_evidence": {
                "instantiated_method_prompt": str(prompt_path),
                "stage1_input_preparation_result": str(stage1_result_path),
                "canonical_input_path": str(canonical),
                "stage2_reference_preparation_result": str(stage2_result_path),
                "reference_artifact_path": str(reference_path),
                "reference_artifact_source_field": reference_field,
                "surface_config_path": str(surface_config_path),
                "selected_layer3_surface_chain_evidence": str(build_root / "methods" / method / "method_chain_lifecycle_trace.yaml"),
                "reviewed_environment_evidence": [
                    str(env_root / "harness_environment.yaml"),
                    str(env_root / "environment_build.yaml"),
                    str(env_root / "environment_build.jsonl"),
                ],
            },
            "candidate_workflow_status": candidate_status,
            "data_input": {"canonical_input_path": str(canonical), "load_result": data_load, "required_fields": required_fields},
            "reference_input": {
                "reference_artifact_path": str(reference_path),
                "reference_artifact_source_field": reference_field,
                "reference_type": stage2.get("reference_mode", "native_or_static"),
                "load_result": ref_load,
                "id_field": ref_load.get("id_field"),
                "result_field": ref_load.get("result_field"),
            },
            "execution_input": {
                "selected_layer3_surface_chain": chain,
                "selected_layer3_contracts": str(layer3_config_path),
                "reviewed_build_evidence": [
                    str(build_root / "layer3_layer4_build_completion_matrix.tsv"),
                    str(build_root / "package_layout.yaml"),
                    str(build_root / "verifier" / "global_verifier_result.yaml"),
                    str(build_root / "publication_index_sanity.yaml"),
                    str(build_root / "logs" / "callable_import_all.log"),
                ],
                "reviewed_environment_evidence": [
                    str(env_root / "harness_environment.yaml"),
                    str(env_root / "environment_build.yaml"),
                    str(env_root / "environment_build.jsonl"),
                ],
                "conda_invocation": conda_invocation,
                "gpu_execution_policy": {
                    "gpu_required": method in {"ADEPT", "ConGI"},
                    "policy": "Use reviewed GPU route when native route requires GPU; no CPU fallback was applied by Stage3.",
                },
                "surface_config_path": str(surface_config_path),
                "surface_config_load_result": surface_config_load,
                "comparison_cues": {"compare_by": "shared observation identifiers when both reference and harness tables load"},
            },
            "harness_execution": {
                "interface_preparation": {"status": "pass" if data_load["status"] == "pass" else "failed", "attempts": []},
                "surface_invocations": invocation["surface_invocations"],
                "real_result_observation": {
                    "produced": comparison_ready,
                    "reason_if_not_produced": invocation.get("reason_if_not_produced"),
                    "attempted_repairs": invocation.get("attempted_repairs", []),
                    "raw_artifact": invocation.get("produced_artifact"),
                    "comparison_ready_artifact": invocation.get("produced_artifact") if comparison_ready else None,
                    "id_field": "obs_id" if comparison_ready else None,
                    "result_field": "domain" if comparison_ready else None,
                    "output_level": "observation",
                    "row_count": None,
                    "missing_result_count": None,
                },
            },
            "result_comparison": result_comparison,
            "failure_class": None if candidate_status == "PASS" else "method_harness_validation_no_comparison_ready_result",
            "failure_stage": None if candidate_status == "PASS" else "selected_layer3_surface_chain",
            "reason": None if candidate_status == "PASS" else invocation.get("reason_if_not_produced"),
            "runtime_monitoring_summary": {
                "execution_mode": "per-method subprocess under reviewed conda prefix",
                "selected_invocation_count": len(invocation["surface_invocations"]),
            },
            "files_written": [
                str(surface_config_path),
                str(prompt_path),
                str(candidate_path),
                str(method_out / "logs" / "method_subagent_stdout.log"),
                str(method_out / "logs" / "method_subagent_stderr.log"),
            ],
        }
    }
    write_yaml(candidate_path, candidate)
    return 0


def verify_candidate(path: Path) -> tuple[str, str | None, str | None]:
    if not path.exists():
        return "REPAIR_REQUIRED", "candidate result missing", "candidate_result_path"
    doc = read_yaml(path).get("method_harness_validation_candidate_result", {})
    handoff = doc.get("stage_handoff_evidence", {})
    required = [
        "instantiated_method_prompt",
        "stage1_input_preparation_result",
        "canonical_input_path",
        "stage2_reference_preparation_result",
        "reference_artifact_path",
        "reference_artifact_source_field",
        "surface_config_path",
        "selected_layer3_surface_chain_evidence",
        "reviewed_environment_evidence",
    ]
    missing = [key for key in required if not handoff.get(key)]
    if missing:
        return "REPAIR_REQUIRED", f"stage_handoff_evidence missing {missing}", "candidate stage_handoff_evidence"
    if not Path(handoff["surface_config_path"]).exists():
        return "REPAIR_REQUIRED", "surface config path missing", handoff["surface_config_path"]
    invocations = nested(doc, ["harness_execution", "surface_invocations"], [])
    if not invocations:
        return "REPAIR_REQUIRED", "selected Layer3 invocation evidence absent", "surface_invocations"
    for inv in invocations:
        if "config" not in inv:
            return "REPAIR_REQUIRED", "surface invocation missing actual config", inv.get("surface")
    conda = nested(doc, ["execution_input", "conda_invocation", "conda_prefix"])
    if not conda:
        return "REPAIR_REQUIRED", "reviewed conda invocation not recorded", "execution_input.conda_invocation"
    status = doc.get("candidate_workflow_status")
    if status == "PASS":
        judgment = nested(doc, ["result_comparison", "judgment", "conclusion"])
        evidence = nested(doc, ["result_comparison", "evidence", "shared_name_comparison"])
        if not judgment or not evidence:
            return "REPAIR_REQUIRED", "PASS candidate lacks evidence-first comparison judgment", "result_comparison"
    elif status == "TERMINAL_FAIL":
        reason = nested(doc, ["harness_execution", "real_result_observation", "reason_if_not_produced"])
        if not reason:
            return "REPAIR_REQUIRED", "TERMINAL_FAIL candidate lacks reason_if_not_produced", "real_result_observation"
        simple_repair_markers = ["IORegistryError", "Ground Truth", "No method registered for writing"]
        repairs = nested(doc, ["harness_execution", "real_result_observation", "attempted_repairs"], [])
        if any(marker in str(reason) for marker in simple_repair_markers) and not repairs:
            return "REPAIR_REQUIRED", "simple non-semantic repair appears available but was not attempted", "real_result_observation.attempted_repairs"
    else:
        return "REPAIR_REQUIRED", f"invalid candidate_workflow_status {status}", "candidate_workflow_status"
    return "PASS", None, None


def package_mode(args: argparse.Namespace) -> int:
    out_root = Path(args.output_root)
    out_root.mkdir(parents=True, exist_ok=True)
    dispatch_methods: list[dict[str, Any]] = []
    eligible: list[str] = []
    script_path = Path(__file__).resolve()
    env_root = Path(args.env_root)
    build_root = Path(args.build_root)

    for method in METHODS:
        method_out = out_root / method
        stage1_result_path = Path(args.stage1_root) / method / "validation_input_preparation_result.yaml"
        stage2_result_path = Path(args.stage2_root) / method / "validation_reference_preparation_result.yaml"
        layer3_config_path = build_root / "methods" / method / "layer3_method_config.yaml"
        method_out.mkdir(parents=True, exist_ok=True)
        entry = {
            "method": method,
            "method_output_root": str(method_out),
            "stage1_input_preparation_result": str(stage1_result_path),
            "stage2_reference_preparation_result": str(stage2_result_path),
            "layer3_method_config": str(layer3_config_path),
        }
        try:
            stage1 = read_yaml(stage1_result_path)["validation_input_preparation_result"]
            stage2 = read_yaml(stage2_result_path)["validation_reference_preparation_result"]
            canonical = stage1["canonical_input_record"]["path"]
            primary = stage2.get("reference_artifacts", {}).get("primary", {})
            reference_field = "reference_artifacts.primary.standardized_artifact" if primary.get("standardized_artifact") else "reference_artifacts.primary.raw_artifact"
            reference_path = primary.get("standardized_artifact") or primary.get("raw_artifact")
            chain = load_chain(build_root, method)
            missing_evidence = []
            if stage1.get("accepted_status") != "INPUT_READY":
                entry.update(stage3_dispatch_decision="excluded", dispatch_reason="Stage1 result is not INPUT_READY")
            elif stage2.get("accepted_status") != "REFERENCE_READY":
                entry.update(stage3_dispatch_decision="excluded", dispatch_reason="Stage2 result is not REFERENCE_READY")
            elif not existing(canonical):
                missing_evidence.append(canonical)
                entry.update(stage3_dispatch_decision="repair_route", dispatch_reason="canonical input path does not exist after Stage1 handoff")
            elif not existing(reference_path):
                missing_evidence.append(reference_path)
                entry.update(stage3_dispatch_decision="repair_route", dispatch_reason="extracted Stage2 reference_artifact_path does not exist")
            elif not layer3_config_path.exists():
                entry.update(stage3_dispatch_decision="repair_route", dispatch_reason="layer3_method_config.yaml is missing or unreadable")
            elif not (env_root / "harness_environment.yaml").exists():
                entry.update(stage3_dispatch_decision="repair_route", dispatch_reason="missing reviewed environment evidence")
            else:
                surface_config = {
                    "method": method,
                    "surface_config": {s: base_surface_config(method, method_out).get(s, {}) for s in chain},
                    "selected_layer3_callable_chain": chain,
                    "source_resolution": source_resolution_notes(method),
                    "stage2_parameter_resolution_scope": "selected Layer3-M exposed variables only; no full parameter audit performed",
                }
                surface_config_path = method_out / "method_harness_validation_surface_config.yaml"
                write_yaml(surface_config_path, surface_config)
                prompt_payload = {
                    "analysis_problem": "spatial_domain_identification",
                    "method": method,
                    "stage_handoff_evidence": {
                        "stage1_input_preparation_result": str(stage1_result_path),
                        "canonical_input_path": canonical,
                        "stage2_reference_preparation_result": str(stage2_result_path),
                        "reference_artifact_path": reference_path,
                        "reference_artifact_source_field": reference_field,
                        "surface_config_path": str(surface_config_path),
                    },
                    "method_output_root": str(method_out),
                    "canonical_validation_input": canonical,
                    "reference_evidence": {"reference_artifact_path": reference_path, "reference_artifact_source_field": reference_field},
                    "build_evidence": {"layer3_method_config": str(layer3_config_path), "selected_layer3_callable_chain": chain},
                    "environment_evidence": reviewed_conda_invocation(Path(args.conda_prefix), build_root),
                    "method_harness_surface_config": {"surface_config_path": str(surface_config_path), "load_required": True},
                    "stop_condition": "Do not write terminal method result unless selected Layer3 invocation evidence exists.",
                }
                prompt_path = method_out / "prompts" / "method_harness_validation_prompt.md"
                generate_prompt(prompt_path, prompt_payload)
                entry.update(
                    stage3_dispatch_decision="eligible",
                    dispatch_reason="Stage1 input, Stage2 reference artifact, selected Layer3 surface, Layer3-M config, and reviewed environment evidence are available",
                    canonical_input_path=canonical,
                    reference_artifact_path=reference_path,
                    reference_artifact_source_field=reference_field,
                    surface_config_path=str(surface_config_path),
                    surface_config_status="generated",
                    instantiated_method_prompt=str(prompt_path),
                    selected_layer3_surface_chain_evidence=str(build_root / "methods" / method / "method_chain_lifecycle_trace.yaml"),
                    reviewed_environment_evidence=[str(env_root / "harness_environment.yaml"), str(env_root / "environment_build.yaml"), str(env_root / "environment_build.jsonl")],
                    comparison_cues={"compare_by": "shared observation identifiers"},
                )
                eligible.append(method)
            if missing_evidence:
                entry["repair_target"] = missing_evidence
        except Exception as exc:
            entry.update(stage3_dispatch_decision="repair_route", dispatch_reason=f"required evidence unreadable: {type(exc).__name__}: {exc}", repair_target=str(method_out))
        dispatch_methods.append(entry)

    for method in eligible:
        rc = run_method_subprocess(script_path, args, method)
        entry = next(item for item in dispatch_methods if item["method"] == method)
        candidate_path = out_root / method / "method_harness_validation_candidate_result.yaml"
        verifier_path = out_root / method / "method_harness_validation_verifier_result.yaml"
        verdict, repair_reason, repair_target = verify_candidate(candidate_path)
        candidate_doc = read_yaml(candidate_path)["method_harness_validation_candidate_result"] if candidate_path.exists() else {}
        terminal_status = candidate_doc.get("candidate_workflow_status") if verdict == "PASS" else None
        terminal_path = None
        if verdict == "PASS":
            terminal_path = out_root / method / "terminal_method_harness_validation_result.yaml"
            write_yaml(terminal_path, {"terminal_method_harness_validation_result": candidate_doc})
        verifier_doc = {
            "verifier_result": {
                "scope": "method",
                "verifier_verdict": verdict,
                "method_acceptance": [
                    {
                        "method": method,
                        "method_workflow_terminal_status": terminal_status,
                        "candidate_result_path": str(candidate_path),
                        "terminal_result_path": str(terminal_path) if terminal_path else None,
                    }
                ] if verdict == "PASS" else [],
                "required_repairs": [] if verdict == "PASS" else [
                    {"method": method, "stage": "method_harness_validation", "repair_instruction": repair_reason, "evidence_needed": repair_target}
                ],
            }
        }
        write_yaml(verifier_path, verifier_doc)
        entry.update(
            candidate_result_path=str(candidate_path),
            verifier_result=str(verifier_path),
            subagent_status="completed_return_code_0" if rc == 0 else f"completed_return_code_{rc}",
            verifier_verdict=verdict,
            method_workflow_terminal_status=terminal_status,
            dispatch_status=None if verdict == "PASS" else "repair_required",
            terminal_result_path=str(terminal_path) if terminal_path else None,
            repair_target=None if verdict == "PASS" else repair_target,
        )

    accepted = [m for m in dispatch_methods if m.get("verifier_verdict") == "PASS"]
    repairs = [
        {"method": m["method"], "stage": "method_harness_validation", "repair_instruction": m.get("dispatch_reason") or "verifier repair required", "evidence_needed": m.get("repair_target")}
        for m in dispatch_methods
        if m.get("stage3_dispatch_decision") != "eligible" or m.get("verifier_verdict") not in {None, "PASS"}
    ]
    package_verdict = "PASS" if not repairs else "REPAIR_REQUIRED"
    package_verifier = {
        "verifier_result": {
            "scope": "package",
            "verifier_verdict": package_verdict,
            "method_acceptance": [
                {
                    "method": m["method"],
                    "method_workflow_terminal_status": m.get("method_workflow_terminal_status"),
                    "candidate_result_path": m.get("candidate_result_path"),
                    "terminal_result_path": m.get("terminal_result_path"),
                }
                for m in accepted
            ],
            "required_repairs": repairs,
        }
    }
    write_yaml(out_root / "method_harness_validation_completion_verifier_result.yaml", package_verifier)
    dispatch_log = {
        "method_validation_dispatch_log": {
            "invocation_id": "SDI_6methods_no_GraphST_stage3_method_harness_validation_2026-06-13",
            "stages": [
                {"stage": "validation_input_preparation", "source_package": str(args.stage1_root), "verifier_result": str(Path(args.stage1_root) / "stage1_input_preparation_verifier_result.yaml")},
                {"stage": "validation_reference_preparation", "source_package": str(args.stage2_root), "verifier_result": str(Path(args.stage2_root) / "validation_reference_preparation_batch_verifier_result.yaml")},
                {
                    "stage": "method_harness_validation",
                    "subagent_prompt_template": "docs/layer3_4/method_validation/templates/method_harness_validation_prompt.md",
                    "verifier_prompt_template": "docs/layer3_4/method_validation/templates/method_harness_validation_completion_verifier_prompt.md",
                    "max_active_method_subagents": 6,
                    "methods": dispatch_methods,
                },
            ],
            "package_terminal_results_written": bool(accepted),
        }
    }
    write_yaml(out_root / "method_validation_dispatch_log.yaml", dispatch_log)
    report = {
        "method_harness_validation_completion_report": {
            "included_methods": METHODS,
            "eligible_methods": eligible,
            "dispatched_methods": eligible,
            "verifier_verdict": package_verdict,
            "package_terminal_results_written": bool(accepted),
            "comparison_judgments_written": [
                m["method"] for m in dispatch_methods
                if m.get("terminal_result_path") and nested(read_yaml(Path(m["terminal_result_path"])), ["terminal_method_harness_validation_result", "result_comparison", "judgment", "conclusion"])
            ],
            "method_results": summarize_methods(dispatch_methods),
            "failures_blockers_and_repair_routes": repairs,
            "scope_note": "This report validates harness execution behavior and comparison evidence only; it does not claim author-case success, biological correctness, production readiness, or algorithmic equivalence.",
        }
    }
    write_yaml(out_root / "method_harness_validation_completion_report.yaml", report)
    (out_root / "method_harness_validation_completion_report.md").write_text(render_markdown_report(report["method_harness_validation_completion_report"]), encoding="utf-8")
    return 0 if package_verdict == "PASS" else 2


def summarize_methods(methods: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for item in methods:
        candidate = {}
        if item.get("candidate_result_path") and Path(item["candidate_result_path"]).exists():
            candidate = read_yaml(Path(item["candidate_result_path"]))["method_harness_validation_candidate_result"]
        rows.append({
            "method": item["method"],
            "verifier_verdict": item.get("verifier_verdict"),
            "method_workflow_terminal_status": item.get("method_workflow_terminal_status"),
            "stage3_dispatch_decision": item.get("stage3_dispatch_decision"),
            "dispatch_reason": item.get("dispatch_reason"),
            "dispatch_status": item.get("dispatch_status"),
            "surface_config_path": item.get("surface_config_path"),
            "surface_config_status": item.get("surface_config_status"),
            "surface_invocations": nested(candidate, ["harness_execution", "surface_invocations"], []),
            "candidate_result_path": item.get("candidate_result_path"),
            "terminal_result_path": item.get("terminal_result_path"),
            "data_input": candidate.get("data_input"),
            "reference_artifact_source_field": item.get("reference_artifact_source_field"),
            "reference_input": candidate.get("reference_input"),
            "execution_input": candidate.get("execution_input"),
            "selected_layer3_surface_chain": nested(candidate, ["execution_input", "selected_layer3_surface_chain"]),
            "reviewed_conda_invocation": nested(candidate, ["execution_input", "conda_invocation"]),
            "layer3_invocation_evidence": "present" if nested(candidate, ["harness_execution", "surface_invocations"]) else "absent",
            "gpu_resource_adjustment": nested(candidate, ["execution_input", "gpu_execution_policy"]),
            "real_result_observation": nested(candidate, ["harness_execution", "real_result_observation"]),
            "result_comparison": candidate.get("result_comparison"),
            "failure_class": candidate.get("failure_class"),
            "failure_stage": candidate.get("failure_stage"),
            "reason": candidate.get("reason"),
            "repair_route": item.get("repair_target"),
            "files_written": candidate.get("files_written"),
        })
    return rows


def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Method Harness Validation Completion Report",
        "",
        f"Verifier verdict: `{report['verifier_verdict']}`",
        "",
        f"Eligible methods: {', '.join(report['eligible_methods'])}",
        f"Dispatched methods: {', '.join(report['dispatched_methods'])}",
        f"Comparison judgments written: {', '.join(report['comparison_judgments_written']) or 'none'}",
        "",
        "## Method Results",
        "",
        "| Method | Verifier | Terminal status | Dispatch | Comparison |",
        "|---|---|---|---|---|",
    ]
    for row in report["method_results"]:
        comparison = nested(row, ["result_comparison", "judgment", "conclusion"], "not_written")
        lines.append(f"| {row['method']} | {row.get('verifier_verdict')} | {row.get('method_workflow_terminal_status')} | {row.get('stage3_dispatch_decision')} | {comparison} |")
    lines += ["", "## Scope Note", "", report["scope_note"], ""]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    for name in ["package", "method"]:
        p = sub.add_parser(name)
        p.add_argument("--stage1-root", type=Path, required=True)
        p.add_argument("--stage2-root", type=Path, required=True)
        p.add_argument("--build-root", type=Path, required=True)
        p.add_argument("--env-root", type=Path, required=True)
        p.add_argument("--conda-prefix", type=Path, required=True)
        p.add_argument("--output-root", type=Path, required=True)
        if name == "method":
            p.add_argument("--method", required=True, choices=METHODS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mode == "method":
        return method_mode(args)
    return package_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
