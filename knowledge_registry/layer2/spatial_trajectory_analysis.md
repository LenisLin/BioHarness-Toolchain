# Spatial Trajectory Analysis

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Spatial Trajectory Analysis`.

This topic covers spatial differentiation trajectories, spatial RNA velocity, latent spatiotemporal embedding or pseudotime, state-transition modeling, fate-landscape learning, and causal trajectory inference. These outputs are model-based summaries of transition structure, velocity, ordered states, or trajectory topology rather than direct proof of lineage, migration, fate commitment, or experimental causality.

Use another Layer 1 problem first when the requested output is domain clustering, cell type inference, communication analysis, perturbation response, or preprocessing without an explicit trajectory question. Keep reference mismatch, representation-learning entanglement, and causal-language caveats visible throughout selection.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Trajectory Branch | Splicing / Velocity Dependence | Spatial Coupling Mode | Reference Dependence | Temporal / Multi-sample Cue | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SpaTrack | Reconstruct spatial cell differentiation trajectories using expression and spatial position in transition costs. | Spatial transcriptomics expression with spatial coordinates; multiple samples or temporal intervals can be used when available. | Spatial trajectory topology, differentiation paths, and dynamic driver cues. | differentiation trajectory | not primary | coordinates in transition cost | reference-free | multi-sample / temporal interval | CPU; code available |
| spVelo | Infer RNA velocity and spatially resolved transcriptional dynamics across multi-batch spatial datasets. | Multi-batch spatial transcriptomics data with spatial information and RNA-velocity-relevant expression dynamics. | Spatial RNA velocity estimates, trajectory patterns, uncertainty cues, driver markers, and related downstream dynamic summaries. | spatial RNA velocity | uses splicing / velocity signal | spatial graph / constraints | reference-free | multi-batch | Optional GPU; code available |
| STT | Characterize cell-state-specific dynamics and spatial state transitions through a multiscale transition tensor. | Spatial transcriptomics with spatial coordinates and messenger RNA splicing information. | Four-dimensional transition tensor, local tensor streamlines, and long-time transition paths among attractors. | spatial RNA velocity | uses splicing / velocity signal | spatial graph / constraints | reference-free | single-sample compatible | CPU; code available |
| SIRV | Infer spatial RNA velocities at single-cell resolution when spatial assays lack direct spliced/unspliced capture. | Spatial transcriptomics data enriched with spliced and unspliced mRNA expression from matched or relevant reference scRNA-seq data. | Spatial RNA velocities and spatial differentiation trajectories at single-cell resolution. | spatial RNA velocity | reference-imputed splicing / velocity | spatial graph / constraints | scRNA-reference-assisted | single-sample compatible | CPU; code available |
| PearlST | Infer spatiotemporal structures, including trajectory inference and pseudotime analysis, through latent spatial embeddings. | Spatial transcriptomics expression, spatial coordinates, and histology image features when available. | Low-dimensional latent embeddings, spatial domains, temporal trajectories, and pseudotime summaries. | spatiotemporal embedding / pseudotime | not primary | histology + spatial features | reference-free | time-course helpful | Optional GPU; code available |
| TopoVelo | infer topological velocity and spatially coupled cell-state dependencies for model-based cell-state transition analysis | Spatial transcriptomic data for jointly modeling spatial and temporal cell-state transition dynamics. | Velocity estimates, spatial cell-state dependencies, and model-based cell-state transition patterns. | spatial RNA velocity | uses splicing / velocity signal | spatially coupled dynamics | reference-free | time-course helpful | Optional GPU; code access unclear |
| CASCAT | infer model-based causal-style spatial trajectories using conditional-dependence pruning and a tree-shaped structural causal model | Spatial transcriptomics expression with spatial coordinates and graph construction for trajectory inference. | Model-based causal-style cell graph, trajectory tree, pseudotime, and cluster-level trajectory interpretation. | causal trajectory | not primary | spatially refined causal graph | reference-free | single-sample compatible | Optional GPU; code available |
| STORIES | learn model-based fate-landscape structure from spatial transcriptomics using optimal transport | spatial transcriptomics expression with spatial coordinates and cell-state context for fate-landscape inference | Model-framed fate-landscape representation, transition structure, and trajectory interpretation for spatial cell states. | differentiation trajectory | not primary | coordinates in transition cost | reference-free | time-course helpful | CPU; code available |
| stVCR | model spatiotemporal dynamics of single cells from spatial transcriptomics | spatial transcriptomics data with single-cell state information and temporal or progression context | spatiotemporal cell-state dynamics, trajectory or pseudotime-style summaries, and dynamic interpretation cues | spatiotemporal embedding / pseudotime | not primary | spatially coupled dynamics | reference-free | multi-sample / temporal interval | Optional GPU; code available |

## Decision Tree

If the primary question is spatial RNA velocity or cell-fate dynamics from velocity-like signal:
- Continue within the velocity branch.

If a matched or relevant scRNA-seq reference is needed to supply spliced or unspliced information:
- Prefer / consider `SIRV`.
- Keep reference mismatch and reference-composition bias visible.

If the velocity problem is explicitly multi-batch:
- Prefer / consider `spVelo`.

If multiscale transition dynamics, attractors, or streamlines are central:
- Prefer / consider `STT`.

If spatially coupled topological velocity interpretation is central:
- Prefer / consider `TopoVelo`.

If the primary question is expression-plus-location differentiation trajectory rather than velocity:
- Prefer / consider `SpaTrack` for optimal-transport trajectory reconstruction.
- Prefer / consider `STORIES` when fate-landscape framing is the real target.
- Keep directionality and fate language framed as model interpretation rather than lineage proof.

If the primary question is latent spatiotemporal structure or pseudotime from representation learning:
- Prefer / consider `PearlST` for latent spatiotemporal structure with spatial or image-feature integration.
- Prefer / consider `stVCR` when spatiotemporal single-cell dynamics are central.
- Keep representation and objective entanglement caveats visible.

If the explicit target is a causal or Markovian tree-shaped trajectory:
- Prefer / consider `CASCAT`.
- Keep causal wording framed as model-based trajectory structure rather than experimental causality.

If no branch fits cleanly:
- Re-check whether the task is really trajectory analysis or whether another Layer 1 problem should come first.
