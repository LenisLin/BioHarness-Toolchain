#!/usr/bin/env python3
"""Write/update the SDI method-subagent dispatch log."""

from __future__ import annotations

import sys
from pathlib import Path
from textwrap import dedent


BUILD_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/layer3_layer4_builds"
)
METHODS = [
    ("ADEPT", "019eb430-3393-7712-8330-8d77756b44c3", "Herschel"),
    ("BANKSY", "019eb430-5d1d-7923-8f53-fd7d1cde3195", "Ramanujan"),
    ("BASS", "019eb430-81b2-7212-8e6e-ebaf526026d5", "Lagrange"),
    ("CCST", "019eb430-a9c6-7271-a29b-05a9d2bb4620", "Bernoulli"),
    ("ConGI", "019eb430-cf7a-7352-bef2-64d2229de0e2", "Dalton"),
    ("DR-SC", "019eb1f8-d98f-7131-a1ae-e95ec100e995", "Huygens"),
]


def main() -> None:
    statuses = {method: "running" for method, _, _ in METHODS}
    for item in sys.argv[1:]:
        method, status = item.split("=", 1)
        statuses[method] = status

    method_lines = []
    all_terminal = True
    all_pass = True
    any_repair = False
    for method, agent_id, nickname in METHODS:
        status = statuses[method]
        terminal = status in {"PASS", "FAIL_WITH_REPAIRS", "STOP_BEFORE_IMPLEMENTATION"}
        all_terminal = all_terminal and terminal
        all_pass = all_pass and status == "PASS"
        any_repair = any_repair or status == "FAIL_WITH_REPAIRS"
        prompt_path = BUILD_ROOT / "method_prompts" / f"{method}_layer3_layer4_method_prompt.md"
        evidence_root = BUILD_ROOT / method
        module_name = method.lower().replace("-", "_")
        unresolved_repairs = "[]" if status != "FAIL_WITH_REPAIRS" else f"""
                - method: {method}
                  execution_surface: prepare_spatial_domain_input
                  evidence_class: action_path_closure
                  observed_code_path: /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/layer3_layer4_implementations/SDI_runtime/python/bioharness_sdi_runtime/methods/{module_name}.py
                  repair_target: resume same-method implementation from the affected surface/evidence class"""
        repair_iterations = "[]" if status != "FAIL_WITH_REPAIRS" else f"""
                - iteration_id: {method}_repair_001
                  method: {method}
                  input_status: FAIL_WITH_REPAIRS
                  repair_packet:
                    execution_surface: prepare_spatial_domain_input
                    evidence_class: action_path_closure
                    observed_code_path: /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/layer3_layer4_implementations/SDI_runtime/python/bioharness_sdi_runtime/methods/{module_name}.py
                    repair_target: resume same-method implementation from the affected surface/evidence class
                  repair_assignment:
                    assigned_to_subagent_id: {agent_id}
                    assigned_at: pending_repair_loop_dispatch
                  repaired_iteration_status: FAIL_WITH_REPAIRS
                  repaired_evidence_root: {evidence_root}"""
        method_lines.append(
            f"""
            - method: {method}
              dispatch_batch_id: batch_001
              subagent_id: {agent_id}
              subagent_nickname: {nickname}
              method_prompt_path: {prompt_path}
              owned_paths:
                - /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/layer3_layer4_implementations/SDI_runtime/python/bioharness_sdi_runtime/methods/{module_name}.py
                - {evidence_root}/
              read_only_inputs:
                - /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/stage_integration/pre_gate2_planning_2026-05-21/06_gate2_human_review_table.md
                - /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/stage_integration/pre_gate2_planning_2026-05-21/layer4_bridge_planning.md
                - /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/repository_reading_first_round_2026-05-15/packages/{method}/
                - /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/repository_reading_first_round_2026-05-15/source_repos/{method}/
              dispatch_status: {status}
              method_evidence_root: {evidence_root}
              method_verifier_status: {status if status in {"PASS", "FAIL_WITH_REPAIRS"} else "pending"}
              returned_files: []
              unresolved_repairs: {unresolved_repairs}
              repair_loop_iterations: {repair_iterations}
            """
        )

    batch_status = "pass" if all_pass else ("terminal_nonpass" if all_terminal else "running")
    dispatch_verdict = "pass" if all_pass else ("repair_loop_required" if any_repair else ("blocked" if all_terminal else "running"))
    text = dedent(
        f"""
        subagent_dispatch_log:
          invocation_id: SDI_layer3_layer4_build_ADEPT_BANKSY_BASS_CCST_ConGI_DRSC_2026-06-10
          subagent_prompt_template: docs/layer3_4/templates/layer3_layer4_method_subagent_prompt.md
          max_active_method_subagents: 6
          replacement_dispatch_note: Original ADEPT, BANKSY, BASS, CCST, and ConGI workers terminated with HTTP 503 service errors before terminal method status; replacement workers were assigned to inspect and repair method-owned partial artifacts. DR-SC original worker returned PASS.
          dispatch_batches:
            - batch_id: batch_001
              methods:
                - ADEPT
                - BANKSY
                - BASS
                - CCST
                - ConGI
                - DR-SC
              batch_status: {batch_status}
          methods:
        {''.join(method_lines)}
          dispatch_verdict: {dispatch_verdict}
        """
    ).lstrip()
    (BUILD_ROOT / "subagent_dispatch_log.yaml").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
