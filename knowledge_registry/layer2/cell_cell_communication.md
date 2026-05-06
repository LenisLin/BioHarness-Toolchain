# Cell-Cell Communication

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Cell-Cell Communication`.

This topic covers methods whose primary role is to infer, compare, score, or interpret communication, ligand-receptor interaction, neighbor preference, relay-network structure, interaction effects, or pathway-aware CCC signals between cells, spots, cell types, or tissue compartments.

Use another Layer 1 problem first when the requested output is normalization, denoising, integration, cell type inference, domain clustering, or trajectory analysis without an explicit communication or interaction question.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | CCC Branch | Spatial Specificity | Ligand-Receptor Dependence | Resolution / Grouping Level | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CellChat | Broad LR network interpretation for annotated cell groups. | Grouped expression with LR database context. | Cell-group communication network and pathway summaries. | ligand-receptor communication inference | spatial use case; not spatial-first | required | cell group / cluster | CPU; code available |
| CellNEST | Relay-network or graph-attention CCC over spatial cells or spots. | Spatial expression, coordinates, LR pairs, optional annotations. | Direct and relay CCC edges with graph outputs. | relay / graph communication inference | coordinate-aware graph | required | cell / spot | Optional GPU; code available |
| COMMOT | Spatial sender-receiver communication with geometry or transport signal. | Spatial expression, coordinates, LR or pathway priors. | Spatial communication directions and LR/pathway signals. | ligand-receptor communication inference | coordinate-aware spatial transport | required | spot / cell / region | CPU; code available |
| NicheNet | Ligand-to-target regulatory interpretation in receiver cells. | Sender/receiver expression, candidate ligands, target genes, prior network. | Ranked ligands and ligand-target regulatory links. | ligand-target communication interpretation | non-spatial baseline with spatial use case | required plus ligand-target prior | cell group / receiver program | CPU; code available |
| SpaOTsc | Early transport-style spatial signaling or mapping-linked CCC. | Single-cell expression, spatial positions, signaling gene sets. | Spatial mapping and inferred signaling relationships. | ligand-receptor communication inference | coordinate-aware spatial transport / mapping | optional signaling-gene orientation | cell / spot | CPU; code available |
| SpaTalk | Knowledge-graph-supported spatial LR interpretation. | Spatial expression, cell or spot annotations, LR pairs, knowledge graph. | LR-mediated communication events and pathway-style summaries. | ligand-receptor communication inference | spatially resolved LR inference | required | cell / spot / cell type | CPU; code available |
| SpatialDM | Spatial co-expression style LR testing. | Spatial expression, coordinates, LR database. | Significant spatial LR pairs and communication-pattern summaries. | ligand-receptor communication inference | spatial co-expression | required | spot / cell / LR pair | CPU; code available |
| DeepTalk | Single-cell-resolution spatial CCC with paired scRNA/ST context. | Aligned spatial transcriptomics and scRNA-seq expression with spatial affinities. | Predicted single-cell CCC patterns and graph-attention outputs. | single-cell graph communication inference | coordinate-aware with scRNA/ST integration | required | single cell | Optional GPU; code available |
| stLearn | CCC readout inside a broader spatial trajectory or tissue-context workflow. | Spatial expression, coordinates, optional image context, LR pairs. | LR interaction scores with related spatial or trajectory outputs. | ligand-receptor communication inference | spatial workflow with trajectory context | required for CCC module | spot / region / cell type | CPU; code available |
| COZI | Cell-type neighbor-preference or cohort tissue-architecture comparison. | Cell coordinates, cell-type labels, sample or cohort grouping. | Neighbor-preference scores for cell-type pairs. | neighborhood / interaction-effect modeling | cell-neighborhood graph | not primary | cell-type pair / sample | CPU; code available |
| MISTy | Multiview contextual influence over markers, cell types, or targets. | Spatial features with configurable local and broader views. | View-specific importance and variance-explained interaction summaries. | neighborhood / interaction-effect modeling | configurable multiview neighborhood context | not primary | cell / spot / marker target | CPU; code available |
| Spacia | Probabilistic spatial interaction modeling. | Spatial expression with cellular neighborhoods or bags and interaction features. | Predicted cellular interaction signals and spatial interaction maps. | neighborhood / interaction-effect modeling | spatial interaction model | optional / not primary | cell / spot / neighborhood | CPU; code access unclear |
| SVCA | Variance-component framing of spatial interaction effects. | Spatial molecular features with neighborhoods or spatial units. | Variance components and interaction-effect estimates. | neighborhood / interaction-effect modeling | spatial variance / neighborhood effect | not primary | cell / spatial unit / feature | CPU; code available |
| SPIDER | Spatially variable LR interactions with downstream support. | Spatial expression, LR pairs, downstream genes or TFs, interface profiles. | Spatially variable LR interactions and supported interface signals. | spatially variable ligand-receptor inference | spatially variable LR interface | required plus downstream support | LR interaction / interface | CPU; code available |
| Scriabin | Single-cell-level comparative CCC. | Single-cell expression with cell-level CCC features; spatial context optional. | Single-cell-level CCC comparison features and interaction summaries. | comparative single-cell CCC | single-cell CCC with spatial use cases | required / CCC prior-based | single cell | CPU; code access unclear |
| CausalCCC | Pathway-aware interpretation of existing CCC calls. | Single-cell or spatial expression plus existing LR pairs or user-defined inputs. | Pathway-aware communication interpretations and visualizations. | causal pathway-aware communication interpretation | accepts spatial or single-cell CCC inputs | downstream / user-supplied | pathway / interacting cell type | CPU; web-server boundary |

## Decision Tree

If the requested output is cell-label neighborhood preference or interaction-effect modeling rather than molecular LR calls:
- Prefer / consider `COZI` for conditional neighbor-preference scores over cell-type pairs or cohort tissue-architecture comparison.
- Prefer / consider `MISTy` for multiview contextual influence over markers, targets, or spatial views.
- Prefer / consider `SVCA` for variance decomposition of spatial interaction effects.
- Prefer / consider `Spacia` for probabilistic spatial interaction modeling when code-access uncertainty is acceptable for the selection stage.

If the requested output is a broad LR communication network or sender-receiver summary:
- Prefer / consider `CellChat` for widely used cell-group LR network interpretation.
- Prefer / consider `NicheNet` when ligand-to-target regulatory potential in receiver cells is central.

If spatial geometry, tissue distance, transport, or spatially patterned LR signal is central:
- Prefer / consider `COMMOT` for geometry-aware transport-style communication.
- Consider `SpaOTsc` for early transport-linked spatial signaling workflows.
- Prefer / consider `SpatialDM` for spatial LR co-expression style testing.
- Prefer / consider `SPIDER` for spatially variable LR interactions with downstream functional support.
- Prefer / consider `SpaTalk` when knowledge-graph-supported spatial LR interpretation is desired.

If single-cell or relay-network resolution is central:
- Prefer / consider `CellNEST` for relay-network CCC or graph attention over spatial cells or spots.
- Prefer / consider `DeepTalk` when paired or aligned scRNA-seq plus spatial data support single-cell-resolution CCC.
- Prefer / consider `Scriabin` for single-cell-level comparative CCC when spatial contact is not the primary signal.

If CCC is embedded in a broader workflow or downstream pathway interpretation:
- Prefer / consider `stLearn` when LR scoring is needed inside a broader spatial trajectory or tissue-context workflow.
- Prefer / consider `CausalCCC` when LR calls already exist and the next question is pathway-aware interpretation across interacting cell types.

After choosing the scientific branch:
- Use CPU-labeled candidates for conservative reading paths.
- Add graph or deep-learning candidates when scale, reference match, and calibration can be evaluated.
- Treat unclear code access or web-server-only use surfaces as selection-stage constraints, not as local execution evidence.
