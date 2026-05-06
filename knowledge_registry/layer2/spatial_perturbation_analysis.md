# Spatial Perturbation Analysis

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Spatial Perturbation Analysis`.

This topic covers spatial perturbation-response prediction, causal-style counterfactual tissue modeling, observed perturbation-effect detection, perturbation-responsive pattern prioritization, and spatiotemporal perturbation regulator prioritization. Observed effects, attribution rankings, and counterfactual generation are not the same as experimental proof of causal perturbation mechanisms.

Use another Layer 1 problem first when the requested endpoint is ordinary spatial contrast testing without perturbation framing, phenotype association, trajectory analysis without intervention signal, or generic gene ranking. Keep CONCERT preprint status, Celcomen assumption-bound causal language, and River/Perturb-STNet non-causal prioritization caution visible.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Perturbation Question Type | Spatial Modeling / Pattern Emphasis | Direct Perturbation Data Cue | Validation Evidence Scope | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONCERT | predicting spatially localized perturbation responses across patches, tissue borders, and cellular niches | spatial perturbation transcriptomics with gene-expression measurements, spatial coordinates, and perturbation context | predicted post-perturbation spatial expression response and niche-aware response summaries | response prediction | niche kernels | measured perturbation-response ST | method-paper benchmark plus case studies | Required GPU; code available |
| Celcomen | modeling assumption-bound intra- and inter-cellular program structure and generating counterfactual post-perturbation spatial transcriptomics | spatial transcriptomics or single-cell/tissue data represented for causal graph neural modeling | assumption-bound causal-style program representations and counterfactual spatial transcriptomics predictions | causal counterfactual | causal-graph-model program structure under explicit assumptions | unclear | method-paper simulations plus tissue case studies | Optional GPU; code available |
| Spatial-ZEDNet | detecting spatially differentially expressed genes and differentially activated genes under exposure, perturbation, or treatment conditions | condition-labeled spatial transcriptomics data with expression, spatial coordinates, and control versus perturbed or treatment context | spatial DEGs, spatial DAGs, and condition-specific perturbation-effect summaries | observed perturbation-effect detection | spatial differential activation | condition-labeled spatial omics | method-paper benchmark plus case studies | CPU; code available |
| River | prioritizing genes or features with perturbation-responsive differential spatial expression patterns across conditions | multi-slice or multi-condition spatial omics data with expression, spatial coordinates, and condition or slice labels | ranked DSEP genes or features with attribution-supported spatial and non-spatial components | perturbation-responsive pattern prioritization | spatial pattern attribution | condition-labeled spatial omics | method-paper benchmark plus case studies | Optional GPU; code available |
| Perturb-STNet | ranking spatial and temporal differentially expressed regulators and perturbation-associated network summaries | single-cell or spatially resolved data with spatial coordinates, time or trajectory context, and control versus perturbed conditions | pSTDERs, perturbation-associated regulatory-network summaries, and regulator/cell/neighborhood interaction visualizations | spatiotemporal perturbation regulator prioritization | spatiotemporal network regulator prioritization | condition-labeled spatial omics | method-paper benchmark plus case studies | CPU; code available |

## Decision Tree

If the question is predictive spatial perturbation-response modeling with local niche, border, or microenvironment context:
- Consider `CONCERT` when preprint-level evidence and GPU-dependent frontier modeling are acceptable for selection.
- Treat predicted spatial responses as model outputs needing downstream biological validation.

If the question is counterfactual tissue perturbation modeling with explicit causal-disentanglement assumptions:
- Prefer / consider `Celcomen`.
- Keep causal language assumption-bound and separate from experimentally confirmed perturbation effects.

If the question is observed perturbation or treatment effect detection in spatial expression or activation:
- Prefer / consider `Spatial-ZEDNet`.
- Treat detected DEGs or DAGs as condition-associated effects, not counterfactual causal proof.

If the question is ranking perturbation-responsive spatial expression patterns across slices or conditions:
- Prefer / consider `River`.
- Keep attribution and DSEP ranking language as prioritization, not causal mechanism.

If the question is spatial and temporal regulator or network-effect prioritization under perturbation:
- Prefer / consider `Perturb-STNet`.
- Keep regulator rankings and networks as assumption-bound prioritization outputs.

If the task asks only for a direct group contrast, phenotype association, or trajectory without intervention metadata:
- Route to the matching Layer 1 problem before choosing a perturbation-analysis method.
