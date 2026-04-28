# Task Adapters

## Purpose

Define the planned high-frequency spatial transcriptomics downstream task adapters that could become the first execution surfaces for BioHarness-Toolchain.

## Status

All adapters in this document are planned unless a future implementation, contract instance, or surface manifest explicitly marks one as implemented. The current repository contains blueprint schemas and illustrative examples, not a production adapter runtime.

## Adapter Set

Do not create one adapter per method by default. Prefer one task-family adapter with multiple backend candidates.

Example:

```text
spatial_domain_detection
  backend: banksy
  backend: bayesspace
  backend: spagcn
  backend: graphst
  backend: stlearn
```

| Adapter | Status | Purpose | Primary input | Primary output | Likely backend | Validation focus |
| --- | --- | --- | --- | --- | --- | --- |
| `load_and_validate_spatial_data` | planned | Load spatial transcriptomics data and check structure | h5ad / Visium / matrix + metadata | validated AnnData / SpatialData | AnnData, Scanpy, Squidpy | object type, spatial coordinates, metadata |
| `qc_spatial_anndata` | planned | Generate QC metrics and filtering suggestions | AnnData | QC report, filtered object optional | Scanpy | obs/var metrics, mitochondrial genes, counts |
| `normalize_and_hvg` | planned | Normalize counts and select HVGs | AnnData | normalized AnnData | Scanpy | layers, var flags, count preservation |
| `reduce_and_cluster` | planned | PCA/UMAP/neighbors/clustering | AnnData | embeddings and cluster labels | Scanpy | obsm/obs fields, cluster key |
| `build_spatial_neighbors` | planned | Construct spatial graph | AnnData with spatial coordinates | spatial graph in obsp/uns | Squidpy | spatial key, graph shape |
| `neighborhood_enrichment` | planned | Test neighborhood enrichment between clusters | AnnData with spatial graph and cluster key | enrichment matrix, plots | Squidpy | cluster categories, result matrix |
| `spatial_autocorrelation` | planned | Compute Moran's I / related spatial statistics | AnnData with spatial graph | ranked spatial genes | Squidpy | graph availability, score table |
| `spatially_variable_genes` | planned | Identify spatially variable genes | AnnData | gene ranking/table | Squidpy / SpatialDE-like tools | result schema |
| `spatial_domain_detection` | planned | Detect spatial tissue domains | AnnData | domain labels, plots | Squidpy / graph methods / model-specific tools | domain key, cluster count |
| `cell_type_annotation_bridge` | planned | Map annotations from scRNA-seq or reference labels | AnnData + reference | annotation labels/scores | Scanpy/scvi-tools/celltypist-like tools | label fields, confidence scores |
| `deconvolution_bridge` | planned | Estimate cell type proportions in spots | spatial data + scRNA reference | proportions table | cell2location / RCTD / SPOTlight-like tools | proportion matrix |
| `ligand_receptor_analysis` | planned | Analyze spatially aware cell-cell communication | AnnData + labels | interaction table/network | COMMOT / CellChat / NicheNet-like tools | sender/receiver labels, interaction schema |
| `image_feature_extraction` | planned | Extract histology/image features | spatial image + coordinates | image features linked to spots/cells | Squidpy image / skimage / OpenCV | coordinate alignment |
| `spatial_visualization` | planned | Generate standardized spatial plots | AnnData + keys | figures | Scanpy/Squidpy/Matplotlib | figure files, key existence |
| `generate_analysis_report` | planned | Produce reproducible summary report | outputs + provenance | HTML/Markdown/PDF report | nbconvert/quarto/custom templates | complete sections, artifact links |
| `export_reproducible_artifacts` | planned | Package outputs for replay | analysis directory | manifest, logs, environment metadata | custom harness utilities | checksums, versions, manifest |

## Foundation Adapters

These are substrate-level adapters:

- `load_and_validate_spatial_data`
- `qc_spatial_anndata`
- `normalize_and_hvg`
- `reduce_and_cluster`
- `build_spatial_neighbors`
- `spatial_visualization`
- `generate_analysis_report`
- `export_reproducible_artifacts`

## Method-Family Adapters

These correspond to scientific task families and can have multiple backends:

- `spatial_domain_detection`
- `cell_type_deconvolution`
- `ligand_receptor_analysis`
- `spatially_variable_genes`
- `multi_slice_integration`
- `cell_segmentation_bridge`
- `spatial_gene_prediction`
- `super_resolution_bridge`

The first MVP should include foundation adapters plus at least one method-family adapter to demonstrate that the project is not merely a scverse workflow wrapper. The preferred first method-family candidate remains `spatial_domain_detection` / `spatial_domain_identification`, because it already has Layer 2 pilot material. A second strong candidate is `cell_type_deconvolution` or `ligand_receptor_analysis`, because these better demonstrate dependency and ecosystem heterogeneity.

## Layer 3/4 Co-design For Promoted Methods

Layer 2 can cover many methods. Not every Layer 2 method should enter Layer 3/4 planning.

Only promoted methods should receive `MethodExecutionPlanningRecord` work. For each promoted method, engineers should derive both a functional surface and backend binding from one planning record. The outputs remain separate: a Layer 3 `ExecutionSurfaceSpec` and a Layer 4 `BackendAdapterSpec`.

The current generic method execution planning template is `MethodExecutionPlanningRecord v0.7.1`. It preserves the v0.7 architecture and adds stricter review rules: every Layer 3 functional surface must have Layer 4 binding coverage, evidence resolution must be recorded, and acceptance is split across template acceptance, implementation readiness, and production readiness.

Each promoted method must inherit the task-family canonical surface before generating a method-specific Layer 3 surface. For spatial domain identification, method-specific surfaces such as `spatial_domain_identification.banksy.v1` should inherit from `spatial_domain_identification.canonical.v1`.

The preferred first co-design pilot remains `spatial_domain_detection` / `spatial_domain_identification`. The first pilot order is:

```text
1. BANKSY v0.7.0 accepted as a template trial, not implementation-ready
2. v0.7.1 template patch
3. SpaGCN Layer3/4 co-design
4. hold / legacy / no-clean-API negative case
```

This order validates the template and co-design process. It does not freeze BANKSY or SpaGCN as default methods and does not claim that any adapter is implemented.

The BANKSY v0.7.0 target is `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/BANKSY/v0.7.0/`. BANKSY source retrieval outputs are stored under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/banksy/`. The BANKSY v0.6.1 recovery package is a failed/stress-test example for the co-design workflow, not the current template and not a final source. These artifacts are blueprint/protocol evidence only; they do not claim a production adapter, environment capsule, runtime validator, smoke fixture, or runtime-cost result. BANKSY is not MVP implementation-ready, and its environment probe is a separate future task.

For spatial domain identification, the first co-design batch should cover a representative set rather than every method:

```text
1. one scverse/Squidpy or simple graph baseline
2. one R / Bioconductor / Bayesian method
3. one histology-aware method
4. one deep learning or GNN method
5. one multi-slice or integration-aware method if available
6. one implementation-stable MVP candidate
```

These are selection principles, not mandatory method names. Any examples should remain illustrative unless the current Layer 2 authority selects them.

## Research-Grade / Hold Adapters

These are scientifically important but should not be early MVP targets unless readiness improves:

- `spatial_clonal_analysis`
- `spatial_trajectory_analysis`
- `spatial_perturbation_response`
- `program_discovery`

## Contract Shape

Each adapter should eventually bind to the public contract layer described in [Interface Contract](40_interface_contract.md):

- a `SkillSpec` or equivalent task-level entry point
- an `ExecutionSurfaceSpec` for the smallest stable callable surface
- an `EnvironmentProfile` or future environment capsule
- a `RunRecord` for resumable state
- a `ValidationReport` for release, block, or manual-review decisions
- a future `BackendAdapterSpec` when a Layer 4 binding exists

## Adapter Design Rules

- Prefer mature backend tools behind thin adapters.
- Keep task-level names stable even when backend tools change.
- Hide package-specific parameter quirks from the LLM-facing surface.
- Validate input contracts before execution and output contracts after execution.
- Return typed failures rather than unclassified tracebacks when possible.
- Record provenance sufficient for replay or manual review.

## Non-Goals

- This document does not freeze final adapter names, callable signatures, or parameter schemas.
- This document does not claim that all listed backend tools are compatible in one environment.
- This document does not replace topic-specific Layer 2 method selection artifacts.
