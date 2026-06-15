#!/usr/bin/env python3
"""Write method-subagent prompts for the SDI Layer3/Layer4 build."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

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
PACKAGE_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/repository_reading_first_round_2026-05-15/packages"
)
SOURCE_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/repository_reading_first_round_2026-05-15/source_repos"
)
PLANNING_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/stage_integration/pre_gate2_planning_2026-05-21"
)


SURFACES = [
    "prepare_spatial_domain_input",
    "construct_spatial_structure",
    "fit_then_assign_domains",
    "export_domain_result",
    "plot_domain_labels",
]

METHODS = {
    "ADEPT": {
        "held": [],
        "actions": {
            "prepare_spatial_domain_input": "ADEPT_main.py, run_all.py, st_loading_utils.py, GAAE/utils.py initialize",
            "construct_spatial_structure": "get_kNN, Transfer_pytorch_Data, adata.uns[\"Spatial_Net\"]",
            "fit_then_assign_domains": "GAAE, train_ADEPT_use_DE, impute, mclust_R",
            "export_domain_result": "adata_out.obs[\"mclust_impute\"] or canonical adata.obs[\"domain\"] produced by fit",
            "plot_domain_labels": "sc.pl.spatial save blocks in ADEPT_main.py",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData with X, aligned obs/var, and spatial coordinates",
            "construct_spatial_structure": "standard spatial structure field, default adata.obsp[\"spatial_connectivities\"]",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from mclust_impute labels",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf",
        },
    },
    "BANKSY": {
        "held": [],
        "actions": {
            "prepare_spatial_domain_input": "AnnData examples, filtering utilities, coordinate keys",
            "construct_spatial_structure": "initialize_banksy, generate_spatial_weights_fixed_nbrs, create_nbr_matrix, generate_banksy_matrix",
            "fit_then_assign_domains": "run_banksy_multiparam or selected Leiden core path, run_Leiden_partition",
            "export_domain_result": "canonical adata.obs[\"domain\"] from prior fit; results_df/labels provenance only",
            "plot_domain_labels": "plot_banksy.py::plot_results and _plot_labels",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData with aligned expression and spatial coordinates",
            "construct_spatial_structure": "BANKSY spatial weights/context with standard structure field",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from selected Leiden labels",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf",
        },
    },
    "BASS": {
        "held": ["plot_domain_labels"],
        "actions": {
            "prepare_spatial_domain_input": "createBASSObject, BASS.preprocess, BASS S4 class",
            "construct_spatial_structure": "BASS.preprocess, BASSFit, Potts C++ path",
            "fit_then_assign_domains": "BASS.run, BASSFit, BASS.postprocess",
            "export_domain_result": "BASS@results$z canonical labels; BASS@results$c provenance only",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData plus private BASS object/state",
            "construct_spatial_structure": "fused spatial context, default adata.obsm[\"spatial_context\"]",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from postprocessed BASS@results$z",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
        },
    },
    "CCST": {
        "held": [],
        "actions": {
            "prepare_spatial_domain_input": "data_generation_ST.py, data_generation_merfish.py, read_h5, adata_preprocess",
            "construct_spatial_structure": "get_adj, CCST.py::get_graph",
            "fit_then_assign_domains": "run_CCST.py, Encoder, DGI training, clustering utilities",
            "export_domain_result": "canonical adata.obs[\"domain\"]; types.txt/h5ad provenance only if produced by fit",
            "plot_domain_labels": "draw_map and ST/MERFISH plotting blocks",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData with generated feature/coordinate provenance",
            "construct_spatial_structure": "adata.obsp[\"spatial_connectivities\"] aligned to obs",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from current fit/clustering path",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf",
        },
    },
    "ConGI": {
        "held": ["plot_domain_labels"],
        "actions": {
            "prepare_spatial_domain_input": "Dataset, load_ST_file, build_her2st_data, adata_preprocess_hvg, dataset.py image patch construction",
            "construct_spatial_structure": "Dataset spatial coordinate and image-patch state; ConGI context/refinement helpers",
            "fit_then_assign_domains": "train, SpaCLR, TrainerSpaCLR, mclust_R, res_search_fixed_clus",
            "export_domain_result": "canonical adata.obs[\"domain\"]; output/<name>_pred.csv provenance only",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared image-aware AnnData plus private library/image patch state",
            "construct_spatial_structure": "fused coordinate/image context, default adata.obsm[\"spatial_context\"]",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from current ConGI fit labels",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
        },
    },
    "DR-SC": {
        "held": [],
        "actions": {
            "prepare_spatial_domain_input": "DR.SC, DR.SC.Seurat, DR.SC_fit, Seurat/matrix entry paths",
            "construct_spatial_structure": "getAdj.Seurat, getAdj_reg, getAdj_auto, getAdj_manual",
            "fit_then_assign_domains": "drsc, icmem_heterCpp, EMmPCpp_heter, selectModel, Seurat writeback",
            "export_domain_result": "canonical adata.obs[\"domain\"]; spatial.drsc.cluster provenance only",
            "plot_domain_labels": "spatialPlotClusters, drscPlot, mbicPlot domain cluster plotting only",
        },
        "strict": {
            "prepare_spatial_domain_input": "Prepared AnnData plus private DR-SC Seurat or matrix/coordinate state",
            "construct_spatial_structure": "adata.obsp[\"spatial_connectivities\"] or reviewed equivalent context",
            "fit_then_assign_domains": "adata.obs[\"domain\"] from selected spatial.drsc.cluster metadata",
            "export_domain_result": "domain_labels.csv with obs_id,domain",
            "plot_domain_labels": "domain_plot.png and domain_plot.pdf",
        },
    },
}


def yamlish(mapping: dict[str, str]) -> str:
    return "\n".join(f"  {k}: {v}" for k, v in mapping.items())


def prompt_for(method: str, cfg: dict[str, object]) -> str:
    held = cfg["held"]
    build_required = [surface for surface in SURFACES if surface not in held]
    method_dir = BUILD_ROOT / method
    prompt_path = BUILD_ROOT / "method_prompts" / f"{method}_layer3_layer4_method_prompt.md"
    module_path = PKG_ROOT / "methods" / f"{method.lower().replace('-', '_')}.py"
    read_only_inputs = [
        str(PLANNING_ROOT / "06_gate2_human_review_table.md"),
        str(PLANNING_ROOT / "layer4_bridge_planning.md"),
        "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/environment_builds/SDI_base/harness_environment.yaml",
        "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/environment_builds/SDI_base/environment_build.jsonl",
        str(PACKAGE_ROOT / method / "05_code_reading_plan.md"),
        str(PACKAGE_ROOT / method / "06_code_function_family_evidence.md"),
        str(PACKAGE_ROOT / method / "07_output_validation.md"),
        str(SOURCE_ROOT / method),
    ]
    reference_documents = [
        "docs/layer3_4/stage_integration/layer3_layer4_build.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md",
        "docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md",
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
        "current_artifact_root": str(BUILD_ROOT),
        "implementation_root": str(IMPL_ROOT),
        "method_build_output_root": str(method_dir),
        "owned_paths": [str(module_path), str(method_dir), str(prompt_path)],
        "read_only_inputs": read_only_inputs,
        "minimum_reference_documents": reference_documents,
        "reference_documents": reference_documents,
        "execution_environment": {
            "conda_prefix": "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base",
            "command_env": {
                "LD_LIBRARY_PATH": "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib",
            },
            "python_invocation": "env LD_LIBRARY_PATH=/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib conda run -p /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base python",
            "r_invocation": "env LD_LIBRARY_PATH=/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib conda run -p /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base Rscript",
            "runtime_import_setup": f"PYTHONPATH={IMPL_ROOT}",
        },
        "reviewed_rows": {"build_required": build_required, "held": held},
        "surface_order": SURFACES,
        "strict_outputs": cfg["strict"],
        "native_or_rewrite_actions": cfg["actions"],
        "private_state_policy": f"Follow the method-chain state table in layer4_bridge_planning.md for {method}.",
        "held_rows": held,
        "method_verifier": f"write {method_dir}/verifier/method_verifier_result.yaml using the completion verifier template",
        "return_evidence": [
            "method-owned Layer3 callable files",
            "method-owned Layer4 implementation files",
            "layer3_method_config.yaml",
            "per-row build_output_result.yaml",
            "per-row build_audit.yaml",
            "method_chain_lifecycle_trace.yaml",
            "method verifier result",
        ],
        "stop_condition": "Stop only for method verifier PASS, phase-start missing input, unavailable method-subagent dispatch, or reviewed-boundary contradiction requiring return to review.",
    }
    prompt_fields_yaml = yaml.safe_dump(prompt_fields, sort_keys=False).rstrip()
    prompt_fields_block = "        " + prompt_fields_yaml.replace("\n", "\n        ")
    return dedent(
        f"""
        You are Codex working in /home/lenislin/Experiment/projects/BioHarness-Toolchain-ST.

        Current analysis_problem:
        spatial_domain_identification

        Current workflow_phase:
        layer3_layer4_build

        Method assignment:
        {method}

        Prompt fields:
        ```yaml
{prompt_fields_block}
        ```

        Task:
        Implement this method's reviewed Layer3 / Layer4 execution surfaces inside the owned paths only. For every build-required row assigned to this method, the registered Layer3 callable must reach method-owned Layer4 code that executes the reviewed native action, accepted runtime-only compatibility glue, accepted bounded equivalent implementation, or prior-reviewed algorithmic rewrite action, and uses produced state/output/artifact to close the reviewed strict-output contract. Do not satisfy strict-output contracts with mock/fake backend behavior, placeholder state, dummy, random, or synthetic strict output, contract-only strict-output generation, or output-affecting rewrite without preservation/equivalence evidence.

        A skeleton implementation is not sufficient. Action names in metadata, YAML, comments, lifecycle prose, dictionaries, or state containers are not implementation. A method-owned Layer4 binding must import/call/start/fail-closed reach the reviewed native/glue/rewrite boundary before `PASS`.

        Owned paths:
        - {module_path}
        - {method_dir}/
        - {prompt_path}

        Shared runtime boundary:
        - Shared files under {PKG_ROOT} outside methods/ already exist and are method-agnostic helpers only.
        - Do not edit other method modules.
        - Do not implement GraphST.

        Read-only inputs:
        {chr(10).join(f"- {item}" for item in read_only_inputs)}

        Reference documents to read first:
        {chr(10).join(f"- {item}" for item in reference_documents)}

        Execution environment:
        conda_prefix: /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base
        command_env:
          LD_LIBRARY_PATH: /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib
        python_invocation: env LD_LIBRARY_PATH=/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib conda run -p /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base python
        r_invocation: env LD_LIBRARY_PATH=/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base/lib conda run -p /mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/runtime_artifacts/conda_prefixes/SDI_base Rscript
        runtime_import_setup: PYTHONPATH={IMPL_ROOT}

        Reviewed rows:
        - build_required: {", ".join(build_required)}
        - held: {", ".join(held) if held else "none"}

        Reviewed surface order:
        {", ".join(SURFACES)}

        Strict outputs:
        {yamlish(cfg["strict"])}

        Reviewed native or rewrite actions:
        {yamlish(cfg["actions"])}

        Private-state and handoff policy:
        Follow the method-chain state table in layer4_bridge_planning.md for {method}. Prior-surface private state may be consumed by later surfaces; public outputs remain canonical AnnData state or declared artifacts only.

        Implementation requirements:
        1. Read the method source package and localized source files enough to confirm signatures, call behavior, return values, mutations, private state, artifact behavior, and call order inside the reviewed route.
        2. Write {method_dir}/layer3_method_config.yaml with no default values.
        3. Implement {module_path} with Layer3 callable functions named by the reviewed surfaces. Each callable must accept/load config and pass config values into method-owned Layer4 binding functions in the same module. The binding must contain executable import/call/start/fail-closed boundary evidence for reviewed actions; action names in metadata are not implementation.
        4. Register build-required surfaces through bioharness_sdi_runtime.registry.register_surface.
        5. For each build-required row, write {method_dir}/<surface>/build_output_result.yaml and build_audit.yaml with config consumption, action binding list, import evidence, backend-load evidence, selected bridge smoke-check status, strict-output closure, anti-surrogate audit, runtime_execution.status=not_attempted_in_build unless you actually start a route, and boundary non-claims.
        6. Write {method_dir}/method_chain_lifecycle_trace.yaml.
        7. Write method-level verifier evidence under {method_dir}/verifier/method_verifier_result.yaml with PASS only if all build-required rows close under the template requirements.
        8. Run callable import evidence with the exact PYTHONPATH/invocation above and record logs under {method_dir}/logs/.
        9. Run route-level backend-load checks through the complete reviewed invocation when feasible. If no additional backend load is required beyond method-owned module import, record not_required with a concrete reason. For R/rpy2, PyTorch/PyG, package helper APIs, object-conversion, image patch, or runtime-only glue boundaries, record selected bridge smoke-check evidence that enters the method-owned Layer4 path and reaches the first selected native/glue boundary when feasible.
        10. Do not run method validation, author-case replay, biological result comparison, data downloads, or GraphST work.

        Return status:
        PASS, FAIL_WITH_REPAIRS, or STOP_BEFORE_IMPLEMENTATION. `FAIL_WITH_REPAIRS` is a repair packet for the current method iteration, not a completed package state. If re-dispatched with a repair packet, begin from the affected surface/evidence class and implement or narrow the repair rather than re-reporting the same skeleton-only state. Include evidence root, changed files, verifier result path, first unresolved repair if any, and exact command evidence you ran.
        """
    ).strip() + "\n"


def main() -> None:
    prompt_dir = BUILD_ROOT / "method_prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    for method, cfg in METHODS.items():
        method_dir = BUILD_ROOT / method
        method_dir.mkdir(parents=True, exist_ok=True)
        (method_dir / "logs").mkdir(exist_ok=True)
        (method_dir / "verifier").mkdir(exist_ok=True)
        prompt_path = prompt_dir / f"{method}_layer3_layer4_method_prompt.md"
        prompt_path.write_text(prompt_for(method, cfg), encoding="utf-8")


if __name__ == "__main__":
    main()
