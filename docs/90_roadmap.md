# Roadmap

## Purpose

Record the current staged transition from Layer 1 registry curation into reusable `Layer 2` topic work, then into a domain-limited spatial transcriptomics execution harness.

## Current Decision

The first vertical remains spatial transcriptomics downstream analysis. Runtime work should target a curated set of roughly 10-20 high-frequency task adapters rather than a broad generic biomedical agent.

## Current Status

- Layer 1 has been largely established as a toolbox/task-family catalog.
- Layer 2 is being completed topic by topic.
- Spatial domain identification is the first Layer 2 pilot.
- BANKSY v0.7.0 is accepted as a Layer3/4 template trial, but not MVP implementation-ready.
- Layer 3/4 have not entered production implementation.

## Next Phase

Layer 2 spatial domain identification closure:

- finish method table
- finish decision tree
- clarify field coverage
- identify promoted methods for co-design

Layer 3/4 co-design pilot:

- adopt `MethodExecutionPlanningRecord v0.7.1` for promoted-method planning
- treat BANKSY v0.7.0 as an accepted template trial, not an implementation-ready adapter
- complete the v0.7.1 template/documentation/schema patch
- then run SpaGCN Layer3/4 co-design
- then run a hold / legacy / no-clean-API negative case
- produce Layer 3 `ExecutionSurfaceSpec` drafts
- produce Layer 4 `BackendAdapterSpec` drafts
- assign environment profiles
- record rewrite decisions
- freeze the template and co-design process before claiming production adapters
- choose 1-2 methods for eventual MVP implementation only after the planning process is accepted

Current pilot artifact:

- BANKSY v0.7.0 target root is `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/BANKSY/v0.7.0/`. BANKSY source retrieval outputs remain under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/banksy/`.

The BANKSY v0.6.1 recovery package is now a failed/stress-test example for the planning workflow, not the current template and not a final source. Method-specific outputs remain outside project docs because they are intermediate method-engineering artifacts. Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. They do not move Layer 3/4 into production implementation.

BANKSY environment probing is a separate future task. SpaGCN Layer3/4 co-design is next after the v0.7.1 patch; SpaGCN is not complete.

Do not wait for every topic's Layer 2 to be fully complete before piloting Layer 3/4. Use spatial domain identification as a vertical slice to validate the whole design. Lessons from the vertical slice should feed back into Layer 2 field definitions for other topics.

## Layer 2 Gate

Before any topic moves into `Layer 3`, it should have:

- a frozen candidate set
- a topic `subtable .csv`
- a topic `field registry .json`
- a completed benchmark or review pass when suitable literature exists, or an explicit logic review otherwise
- a standalone `decision tree`
- at least one review or audit pass

A topic should not be treated as ready for `Layer 3` unless this gate is complete. Crossing into `Layer 3` means the topic is eligible for execution-surface planning, environment-profile binding, public interface contract work, rewrite or wrapper evaluation, and validation-hook planning. It does not by itself freeze any per-tool execution design.

Layer 3/4 conceptual separation remains in force during this gate. Once promoted, a method can enter a `MethodExecutionPlanningRecord` that produces separate Layer 3 and Layer 4 drafts from the same repository/code inspection.

## Milestone 1: Layer 1 / Layer 2 Knowledge Stabilization

- Compact Layer 1 toolbox catalog.
- Task-family cards.
- Layer 2 method field registry.
- Spatial domain identification Layer 2 pilot.
- Decision tree format.
- Layer 3 entry review template.

## Milestone 2: Foundation Adapters And First Method-Family Co-design

Planned foundation adapter specs:

- `load_and_validate_spatial_data`
- `qc_spatial_anndata`
- `normalize_and_hvg`
- `reduce_and_cluster`
- `build_spatial_neighbors`
- `neighborhood_enrichment`
- `spatial_autocorrelation`
- `spatial_visualization`
- `generate_analysis_report`
- `export_reproducible_artifacts`

First method-family candidate:

- `spatial_domain_detection`

For promoted candidate backends, perform `MethodExecutionPlanningRecord v0.7.1` work and draft separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` artifacts, without claiming implementation.

The first pilot order is BANKSY v0.7.0 as the accepted template trial, the v0.7.1 patch, SpaGCN, and then a hold / legacy / no-clean-API negative case. The target is to freeze the template and co-design process, not to immediately claim a production adapter.

## Milestone 3: Environment Capsules

Planned environment work:

- `scverse-core` capsule
- `reporting` capsule
- `r-seurat-core`
- `r-bioc-spatial`
- deep-spatial CPU/GPU profiles
- `image-spatial`
- smoke-test strategy for each capsule

## Milestone 4: Advanced Method-Family Adapters

Planned advanced adapters:

- `cell_type_deconvolution`
- `ligand_receptor_analysis`
- `spatially_variable_genes`
- `multi_slice_integration`
- `image_feature_extraction`

## Milestone 5: Reliability Benchmark

Planned evaluation work:

- perturbation benchmark
- cross-machine replay test
- baseline agent vs harness agent
- token/debugging overhead measurement
- typed failure recovery evaluation

## Deferred Items

- Later vertical sequencing beyond the current first vertical
- Production runtime implementation sequencing after the first accepted `Layer 3` families
- Final evidence threshold separating `Core Anchor`, `Wrapper Candidate`, `Rewrite Candidate`, and `Hold`
