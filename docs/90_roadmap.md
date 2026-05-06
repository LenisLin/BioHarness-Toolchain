# Roadmap

## Purpose

Record the current staged transition from Layer 1 registry curation into reusable `Layer 2` method-selection work, then into a domain-limited spatial transcriptomics execution harness.

## Current Decision

The first vertical remains spatial transcriptomics downstream analysis. Runtime work should target a curated set of roughly 10-20 high-frequency task adapters rather than a broad generic biomedical agent.

## Current Status

- Layer 1/2 agent-facing knowledge is now represented in the repo `knowledge_registry/` as 20 active `Analysis Problem` routes plus Layer 2 topic files.
- Layer 2 topic completion standard remains anchored in NAS working/evidence packages and the repo method-selection standard.
- Spatial domain identification remains an early canonical working/evidence example; the current agent-facing registry is broader than that pilot.
- BANKSY v0.7.0 is accepted as a Layer3/4 template trial, but not MVP implementation-ready.
- Layer 3/4 have not entered production implementation.

## Next Phase

Layer 2 topic completion standard and knowledge-registry maintenance:

- keep the Layer 2 topic completion standard aligned with completed NAS working/evidence packages
- keep `knowledge_registry/layer2/method_selection_standard.md` as the compact agent-facing rendering contract
- complete any future Analysis Problem as a full topic package before adding it to `knowledge_registry/layer2`
- identify promoted methods for representative Layer 3/4 co-design after topic closure

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

Before an Analysis Problem moves into `knowledge_registry/layer2` method-selection presentation and later Layer 3 entry review, it should have a complete topic package:

- `README.md`
- `topic_scope.md`
- `field_registry.json`
- `method_table.csv`
- `method_table.md`
- `method_table.json`
- `review_decision_tree.md`
- `closure.md`

The complete topic package precedes knowledge-registry rendering. The Layer 2 output is one agent-facing Markdown file per completed Analysis Problem. That file should contain a problem boundary, a method feature table, and an embedded decision tree.

A topic should not be treated as ready for knowledge-registry rendering unless the complete working/evidence package exists. Representative Layer 3/4 audit handoff should come from the topic closure package and should not be treated as runtime support.

Crossing into Layer 3 means the topic is eligible for execution-surface planning, environment-profile binding, public interface contract work, rewrite or wrapper evaluation, and validation-hook planning. It does not by itself freeze any per-tool execution design or runtime support.

Layer 3/4 conceptual separation remains in force during this gate. Once promoted, a method can enter a `MethodExecutionPlanningRecord` that produces separate Layer 3 and Layer 4 drafts from the same repository/code inspection.

## Milestone 1: Layer 1 / Layer 2 Knowledge Stabilization

- Repo `knowledge_registry/` with compact Layer 1 routing and 20 active Analysis Problems.
- Layer 1/2 selection protocol for closed-world agent use.
- Layer 2 method-selection standard.
- Layer 2 topic completion standard.
- Layer 2 method-selection files for completed Analysis Problems.
- Spatial domain identification canonical completed working/evidence example.
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
