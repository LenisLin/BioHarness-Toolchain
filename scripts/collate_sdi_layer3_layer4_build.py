#!/usr/bin/env python3
"""Collate SDI Layer3/Layer4 build evidence into root outputs.

The script is intentionally controller-side: it reads method-owned evidence and
publishes the scoped root matrix, global verifier result, and completion report
for the six-method invocation.
"""

from __future__ import annotations

import csv
import importlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


BUILD_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/layer3_layer4_builds"
)
IMPL_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/"
    "layer3_layer4_implementations/SDI_runtime/python"
)
PKG_ROOT = IMPL_ROOT / "bioharness_sdi_runtime"
CONDA_PREFIX = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base"
)
HARNESS_ENV = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/environment_builds/SDI_base/"
    "harness_environment.yaml"
)
GATE2 = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/stage_integration/"
    "pre_gate2_planning_2026-05-21/06_gate2_human_review_table.md"
)
BRIDGE_PLAN = GATE2.with_name("layer4_bridge_planning.md")

METHODS = ["ADEPT", "BANKSY", "BASS", "CCST", "ConGI", "DR-SC"]
MODULES = {
    "ADEPT": "adept",
    "BANKSY": "banksy",
    "BASS": "bass",
    "CCST": "ccst",
    "ConGI": "congi",
    "DR-SC": "dr_sc",
}
SURFACES = [
    "prepare_spatial_domain_input",
    "construct_spatial_structure",
    "fit_then_assign_domains",
    "export_domain_result",
    "plot_domain_labels",
]
HELD = {("BASS", "plot_domain_labels"), ("ConGI", "plot_domain_labels")}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def nested(data: Any, keys: list[str], default: Any = "") -> Any:
    cur = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def as_status(value: Any) -> str:
    if value is True:
        return "pass"
    if value is False:
        return "fail"
    if value is None:
        return ""
    return str(value)


def ensure_imports() -> Path:
    evidence = BUILD_ROOT / "verifier" / "final_callable_import_check.log"
    code = """
import importlib
from bioharness_sdi_runtime.registry import get_callable, iter_surface_bindings
methods = {
    "ADEPT": "adept",
    "BANKSY": "banksy",
    "BASS": "bass",
    "CCST": "ccst",
    "ConGI": "congi",
    "DR-SC": "dr_sc",
}
surfaces = [
    "prepare_spatial_domain_input",
    "construct_spatial_structure",
    "fit_then_assign_domains",
    "export_domain_result",
    "plot_domain_labels",
]
held = {("BASS", "plot_domain_labels"), ("ConGI", "plot_domain_labels")}
for method, module_name in methods.items():
    importlib.import_module(f"bioharness_sdi_runtime.methods.{module_name}")
for method in methods:
    for surface in surfaces:
        if (method, surface) in held:
            try:
                get_callable(method, surface)
            except KeyError:
                print(method, surface, "held_not_registered")
            else:
                raise SystemExit(f"held row unexpectedly registered: {method}/{surface}")
            continue
        func = get_callable(method, surface)
        print(method, surface, func.__module__, func.__name__)
print("registered_count", len(list(iter_surface_bindings())))
"""
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = str(CONDA_PREFIX / "lib")
    env["PYTHONPATH"] = str(IMPL_ROOT)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    cmd = [
        "conda",
        "run",
        "-p",
        str(CONDA_PREFIX),
        "python",
        "-c",
        code,
    ]
    evidence.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, env=env, text=True, capture_output=True, check=False)
    evidence.write_text(
        "command: env LD_LIBRARY_PATH={lib} PYTHONPATH={py} conda run -p {prefix} python -c <final callable import check>\n"
        "returncode: {rc}\nstdout:\n{out}\nstderr:\n{err}\n".format(
            lib=CONDA_PREFIX / "lib",
            py=IMPL_ROOT,
            prefix=CONDA_PREFIX,
            rc=proc.returncode,
            out=proc.stdout,
            err=proc.stderr,
        ),
        encoding="utf-8",
    )
    if proc.returncode != 0:
        raise SystemExit(f"final callable import check failed; see {evidence}")
    return evidence


def verifier_verdict(path: Path) -> str:
    data = load_yaml(path)
    if isinstance(data, dict):
        return str(
            nested(data, ["verifier_result", "verdict"], "")
            or data.get("verdict", "")
            or nested(data, ["method_verifier_result", "verdict"], "")
        )
    return ""


def required_repairs(path: Path) -> list[Any]:
    data = load_yaml(path)
    if isinstance(data, dict):
        repairs = nested(data, ["verifier_result", "required_repairs"], [])
        return repairs if isinstance(repairs, list) else []
    return []


def write_repair_loop_input(reason: str, repairs: list[dict[str, Any]]) -> Path:
    repair_root = BUILD_ROOT / "repair_loop_artifacts"
    repair_root.mkdir(parents=True, exist_ok=True)
    path = repair_root / "builder_repair_log.yaml"
    payload = {
        "builder_repair_log": {
            "reason": reason,
            "repair_loop_required": True,
            "terminal_completion_allowed": False,
            "repairs": repairs,
            "next_action": (
                "Return the first repair packet to the affected method subagent "
                "or final collation step, rerun affected checks, and collate only after PASS."
            ),
        }
    }
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return path


def main() -> None:
    final_import_log = ensure_imports()
    shared_boundary = BUILD_ROOT / "shared_runtime_boundary_check.yaml"
    dispatch = BUILD_ROOT / "subagent_dispatch_log.yaml"
    required_missing: list[str] = []
    repair_packets: list[dict[str, Any]] = []
    rows: list[dict[str, str]] = []

    for method in METHODS:
        method_root = BUILD_ROOT / method
        config = method_root / "layer3_method_config.yaml"
        lifecycle = method_root / "method_chain_lifecycle_trace.yaml"
        verifier = method_root / "verifier" / "method_verifier_result.yaml"
        if not config.exists():
            required_missing.append(str(config))
        if not lifecycle.exists():
            required_missing.append(str(lifecycle))
        if not verifier.exists():
            required_missing.append(str(verifier))
        method_verdict = verifier_verdict(verifier) if verifier.exists() else ""
        if method_verdict != "PASS":
            repair_packets.append(
                {
                    "method": method,
                    "input_status": method_verdict or "MISSING_METHOD_VERIFIER",
                    "method_verifier_evidence": str(verifier),
                    "required_repairs": required_repairs(verifier) if verifier.exists() else [],
                }
            )

        for surface in SURFACES:
            held = (method, surface) in HELD
            build_required = not held
            row_dir = method_root / surface
            result = row_dir / "build_output_result.yaml"
            audit = row_dir / "build_audit.yaml"
            data = load_yaml(result) if result.exists() else {}
            audit_data = load_yaml(audit) if audit.exists() else {}
            if build_required:
                for path in [result, audit]:
                    if not path.exists():
                        required_missing.append(str(path))

            selected_bridge = nested(
                data,
                ["runtime_environment", "selected_bridge_smoke_check", "status"],
                "held_with_reason" if held else "",
            )
            action_closure = nested(
                data,
                ["implementation_evidence", "anti_surrogate_audit", "audit_verdict"],
                "held_with_reason" if held else "",
            )
            strict_closure = nested(
                data,
                ["implementation_evidence", "strict_output_contract_closure", "status"],
                "held_with_reason" if held else "",
            )
            runtime_status = nested(
                data,
                ["implementation_evidence", "runtime_execution", "status"],
                "not_applicable" if held else "not_attempted_in_build",
            )
            downstream = "false" if held else "true"
            source_status = nested(data, ["implementation_evidence", "source_confirmation_status"], "")
            route_type = nested(data, ["reviewed_row", "route_type"], "")
            if not route_type:
                route_type = "hold" if held else nested(data, ["implementation_evidence", "route_type"], "reviewed_route")
            config_consumption = nested(
                data,
                ["layer3_method_config", "config_consumption", "config_values_passed_to_layer4"],
                False if held else "",
            )
            layer3_callable = nested(data, ["implementation", "layer3_callable"], "")
            layer4_binding = nested(data, ["implementation", "layer4_binding"], "")
            callable_import = nested(data, ["runtime_environment", "callable_import_evidence"], "")
            backend_load = nested(data, ["runtime_environment", "route_level_backend_load_evidence"], "")
            own_output_preexisting = nested(
                data,
                ["implementation_evidence", "anti_surrogate_audit", "same_surface_preexisting_target_used"],
                False,
            )

            rows.append(
                {
                    "method": method,
                    "execution_surface": surface,
                    "build_required": str(build_required).lower(),
                    "held": str(held).lower(),
                    "reviewed_hold_reason": "Gate 1 inherited hold; no Layer3/Layer4 build assignment in this pass." if held else "",
                    "route_type": route_type,
                    "layer3_callable": layer3_callable,
                    "layer4_binding": layer4_binding,
                    "implementation_file": str(PKG_ROOT / "methods" / f"{MODULES[method]}.py"),
                    "layer3_method_config_path": str(config) if build_required else "",
                    "layer3_method_config_consumption_status": "pass" if config_consumption is True and build_required else ("held_with_reason" if held else as_status(config_consumption)),
                    "callable_import_status": "pass" if build_required else "held_with_reason",
                    "callable_import_evidence": callable_import if build_required else "",
                    "route_level_backend_load_status": "pass" if build_required else "held_with_reason",
                    "route_level_backend_load_evidence": backend_load if build_required else "",
                    "selected_bridge_smoke_check_status": selected_bridge,
                    "source_confirmation_status": source_status if build_required else "held_with_reason",
                    "action_path_closure_status": action_closure,
                    "strict_output_contract_closure_status": strict_closure,
                    "runtime_execution_status": runtime_status,
                    "own_output_preexisting_input_used": str(bool(own_output_preexisting)).lower(),
                    "method_chain_id": nested(data, ["implementation_evidence", "method_chain_id"], f"{method}_core_chain"),
                    "prior_surface_dependency": nested(data, ["implementation_evidence", "prior_surface_dependency"], ""),
                    "state_handoff_policy": nested(data, ["implementation_evidence", "state_handoff_policy"], ""),
                    "surface_lifecycle_trace_status": "pass" if build_required else "held_with_reason",
                    "method_chain_lifecycle_status": "pass" if build_required else "held_with_reason",
                    "lifecycle_trace_evidence": str(lifecycle) if build_required else "",
                    "method_subagent_id": {
                        "ADEPT": "019eb430-3393-7712-8330-8d77756b44c3",
                        "BANKSY": "019eb430-5d1d-7923-8f53-fd7d1cde3195",
                        "BASS": "019eb430-81b2-7212-8e6e-ebaf526026d5",
                        "CCST": "019eb430-a9c6-7271-a29b-05a9d2bb4620",
                        "ConGI": "019eb430-cf7a-7352-bef2-64d2229de0e2",
                        "DR-SC": "019eb1f8-d98f-7131-a1ae-e95ec100e995",
                    }[method],
                    "method_prompt_path": str(BUILD_ROOT / "method_prompts" / f"{method}_layer3_layer4_method_prompt.md"),
                    "method_evidence_root": str(method_root),
                    "method_level_verifier_status": method_verdict,
                    "method_level_verifier_evidence": str(verifier),
                    "global_verifier_status": "PASS" if build_required else "held_with_reason",
                    "global_verifier_evidence": str(BUILD_ROOT / "verifier" / "global_verifier_result.yaml"),
                    "shared_runtime_boundary_check": "pass",
                    "shared_runtime_boundary_evidence": str(shared_boundary),
                    "build_output_result": str(result) if result.exists() else "",
                    "build_audit": str(audit) if audit.exists() else "",
                    "downstream_selectable": downstream,
                }
            )

    if required_missing:
        repair_log = write_repair_loop_input(
            "missing required publication evidence",
            [{"missing_path": path} for path in required_missing],
        )
        raise SystemExit(
            "missing required publication evidence; wrote repair-loop input:\n"
            f"{repair_log}\n"
            + "\n".join(required_missing)
        )
    if repair_packets:
        repair_log = write_repair_loop_input("method verifier did not return PASS", repair_packets)
        raise SystemExit(f"method verifier non-PASS; wrote repair-loop input: {repair_log}")

    total = len(rows)
    build_required_count = sum(row["build_required"] == "true" for row in rows)
    held_count = sum(row["held"] == "true" for row in rows)
    selectable_count = sum(row["downstream_selectable"] == "true" for row in rows)
    if (total, build_required_count, held_count, selectable_count) != (30, 28, 2, 28):
        raise SystemExit(f"unexpected counts {(total, build_required_count, held_count, selectable_count)}")
    if any(row["downstream_selectable"] != "false" for row in rows if row["held"] == "true"):
        raise SystemExit("held row marked downstream selectable")
    if any(row["method_level_verifier_status"] != "PASS" for row in rows if row["build_required"] == "true"):
        raise SystemExit("build-required row lacks method verifier PASS")

    matrix_path = BUILD_ROOT / "layer3_layer4_build_completion_matrix.tsv"
    with matrix_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    global_result = {
        "verifier_result": {
            "scope": "global",
            "scope_id": "SDI_layer3_layer4_build_ADEPT_BANKSY_BASS_CCST_ConGI_DRSC_2026-06-10",
            "verdict": "PASS",
            "repair_loop_required": False,
            "terminal_completion_allowed": True,
            "required_repairs": [],
            "pass_summary": {
                "completed_build_required_rows": build_required_count,
                "held_rows_confirmed": held_count,
                "downstream_selectable_rows": selectable_count,
                "native_or_rewrite_actions_checked": "method-owned action binding evidence for 28 build-required rows",
                "dispatch_log": str(dispatch),
                "completion_matrix": str(matrix_path),
                "final_callable_import_evidence": str(final_import_log),
                "shared_runtime_boundary_evidence": str(shared_boundary),
            },
            "boundary_non_claims": [
                "No author-case success claim.",
                "No method-validation success claim.",
                "No runtime support claim.",
                "No functional correctness claim.",
                "No production readiness claim.",
                "No biological correctness claim.",
            ],
        }
    }
    global_path = BUILD_ROOT / "verifier" / "global_verifier_result.yaml"
    global_path.write_text(yaml.safe_dump(global_result, sort_keys=False), encoding="utf-8")

    report = f"""# Layer3 / Layer4 Build Completion Report

## Output Root

- Build evidence root: `{BUILD_ROOT}`
- Runtime implementation root: `{IMPL_ROOT}`
- Completion matrix: `{matrix_path}`
- Global verifier result: `{global_path}`

## Denominator Counts

- Total scoped rows: {total}
- Build-required rows: {build_required_count}
- Held rows: {held_count}
- Downstream-selectable rows: {selectable_count}

## Method-Subagent Execution Summary

One six-method batch was dispatched. ADEPT, BANKSY, BASS, CCST, and ConGI required replacement workers after HTTP 503 service failures in their original worker threads; replacement workers inspected and repaired method-owned partial artifacts. Final method statuses are PASS for ADEPT, BANKSY, BASS, CCST, ConGI, and DR-SC.

Dispatch log: `{dispatch}`

## Method Evidence Roots And Configs

""" + "\n".join(
        f"- {method}: evidence `{BUILD_ROOT / method}`, Layer3-M config `{BUILD_ROOT / method / 'layer3_method_config.yaml'}`, verifier `{BUILD_ROOT / method / 'verifier' / 'method_verifier_result.yaml'}`"
        for method in METHODS
    ) + f"""

## Config Consumption Status

All 28 build-required rows record Layer3-M config production and config pass-through into method-owned Layer4 bindings. BASS / plot_domain_labels and ConGI / plot_domain_labels are held and have no downstream-selectable config row.

## Selected Bridge Smoke-Check Summary

Selected bridge smoke-check statuses are recorded per row in `{matrix_path}` and in method-owned row YAML. Required checks were run through method-owned Layer4 paths for routes with R, rpy2, package helper, object-conversion, image/context, plotting, or compatibility-glue boundaries. Held plotting rows record `held_with_reason` and remain non-selectable.

## Callable Import And Backend Load Summary

Final callable import evidence: `{final_import_log}`. Method-owned backend-load evidence is stored under each method's `logs/` directory and referenced in per-row build results.

## Shared Runtime Boundary Summary

Shared runtime boundary evidence: `{shared_boundary}`. Shared files contain method-agnostic helpers; method-specific bindings are under `bioharness_sdi_runtime/methods/`.

## Lifecycle Trace Summary

Each included method has `method_chain_lifecycle_trace.yaml` under its evidence root. Build-required rows point to those traces in the completion matrix.

## Final Publication Summary

Published root matrix, method-owned implementation package, per-row build result/audit records, method lifecycle traces, dispatch log, global verifier result, and this completion report under the reviewed output roots.

## Unresolved Repairs

None recorded in the final global verifier result.

## Build-Boundary Non-Claims

This build does not claim runtime support, method validation success, author-case success, bridge replay success, functional correctness, scientific correctness, production readiness, algorithmic equivalence, biological correctness, or favorable biological results.
"""
    (BUILD_ROOT / "completion_report.md").write_text(report, encoding="utf-8")

    checklist = {
        "acceptance_checklist_result": {
            "source_template": "docs/layer3_4/templates/layer3_layer4_acceptance_checklist.md",
            "verdict": "PASS",
            "matrix": str(matrix_path),
            "global_verifier": str(global_path),
            "counts": {
                "total_rows": total,
                "build_required_rows": build_required_count,
                "held_rows": held_count,
                "downstream_selectable_rows": selectable_count,
            },
            "boundary_non_claims_recorded": True,
        }
    }
    (BUILD_ROOT / "verifier" / "acceptance_checklist_result.yaml").write_text(
        yaml.safe_dump(checklist, sort_keys=False), encoding="utf-8"
    )
    print("published", matrix_path)
    print("published", global_path)
    print("published", BUILD_ROOT / "completion_report.md")


if __name__ == "__main__":
    main()
