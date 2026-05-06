# Domain / Clustering

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Domain / Clustering`.

This topic covers spatial domain identification, tissue-region clustering, interpretable topic or semantic domain outputs, reference-informed segmentation, and alignment-aware or multimodal domain comparison. The main branch families here are expression-plus-coordinates methods, graph or neighborhood-prior methods, Bayesian or probabilistic clustering, image or morphology-informed domains, multi-slice or batch-aware domain comparison, multimodal-integration-aware domains, interpretable topic or semantic outputs, and reference-informed segmentation.

Use another Layer 1 problem first when the main task is cell-type deconvolution, SVG detection, gene-expression prediction, or image-only segmentation without a domain-selection endpoint. Do not flatten topic, module, embedding, or semantic outputs into ordinary cluster labels, do not assume image-guided domains are stable without matched morphology, and do not equate integration quality with domain quality.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Spatial Prior | Image Signal Use | Cross-slice / Batch Cue | Domain Output Granularity | Modality Integration Branch | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADEPT | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| BANKSY | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | neighborhood kernel prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| BASS | align and label spatial domains across slices, samples, or batches | one or more spatial expression slices with coordinates | discrete spatial domain labels | Bayesian/probabilistic spatial prior | none apparent | explicit or plausible multi-slice/batch branch | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| BayesSpace | infer probabilistic spatial domain labels with an explicit statistical prior | spatial expression matrix and spatial coordinates | discrete spatial domain labels | Bayesian/probabilistic spatial prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| CCST | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| ConGI | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and histology/image features when available | discrete spatial domain labels | image plus spatial-neighborhood prior | histology/image-informed | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| conST | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and optional histology/image features | discrete spatial domain labels | spatial graph/neighborhood prior | optional histology/image-informed boundary | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| DeepST | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and histology/image features when available | discrete spatial domain labels | image plus spatial-neighborhood prior | histology/image-informed | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| DR-SC | learn a spatially aware low-dimensional representation for domain structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatially aware low-dimensional prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| GraphST | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | explicit or plausible multi-slice/batch branch | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| MENDER | align and label spatial domains across slices, samples, or batches | spatial expression matrix and spatial coordinates | slice-aligned domain labels | spatial coordinates or neighborhood structure | none apparent | explicit or plausible multi-slice/batch branch | slice-aligned domain labels | expression + spatial coordinates branch | CPU; code available |
| Pianno | assign interpretable semantic domain annotations rather than only plain cluster labels | spatial expression and coordinates, optionally with markers or interpretability cues | semantic spatial domain annotations | Bayesian/probabilistic spatial prior | none apparent | single-slice first; cross-slice support unclear | semantic domain annotations | marker/semantic annotation branch | CPU; code available |
| PRECAST | align and label spatial domains across slices, samples, or batches | one or more spatial expression slices with coordinates | integrated embeddings and aligned domain clusters | Bayesian/probabilistic spatial prior | none apparent | explicit or plausible multi-slice/batch branch | slice-aligned domain labels | expression + spatial coordinates branch | CPU; code available |
| PROST | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial coordinates or neighborhood structure | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| SEDR | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| SiGra | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and histology/image features when available | discrete spatial domain labels | spatial graph/neighborhood prior | histology/image-informed | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| SpaceFlow | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| SPACEL | align and label spatial domains across slices, samples, or batches | spatial expression matrix and spatial coordinates | slice-aligned domain labels | spatial coordinates or neighborhood structure | none apparent | explicit or plausible multi-slice/batch branch | slice-aligned domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| SpaGCN | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and histology/image features when available | discrete spatial domain labels | spatial graph/neighborhood prior | histology/image-informed | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| SpaSEG | identify spatial domains using matched image or morphology cues with expression | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial coordinates or neighborhood structure | histology/image-informed | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code available |
| SpatialPCA | learn a spatial embedding or low-dimensional representation for downstream domain labeling | spatial expression matrix and spatial coordinates | spatial embedding or topics supporting domain labels | spatially aware low-dimensional prior | none apparent | single-slice first; cross-slice support unclear | embedding for downstream domain labels | expression + spatial coordinates branch | CPU; code available |
| SpatialPrompt | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial coordinates or neighborhood structure | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| SpaTopic | derive topic-, module-, or program-like spatial domain outputs for interpretation | spatial expression and coordinates, optionally with markers or interpretability cues | domain-associated topics/modules | spatial topic/domain prior | none apparent | single-slice first; cross-slice support unclear | domain-associated topics/modules | expression + spatial coordinates branch | CPU; code available |
| STAGATE | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | explicit or plausible multi-slice/batch branch | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| STAMP | derive topic-, module-, or program-like spatial domain outputs for interpretation | spatial expression and coordinates, optionally with markers or interpretability cues | spatial embedding or topics supporting domain labels | spatially aware low-dimensional prior | none apparent | single-slice first; cross-slice support unclear | domain-associated topics/modules | expression + spatial coordinates branch | Optional GPU; code available |
| STCC | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial coordinates or neighborhood structure | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| stLearn | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code available |
| Novae | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | explicit or plausible multi-slice/batch branch | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code available |
| IRIS | perform reference-informed tissue segmentation or domain labeling | spatial expression, coordinates, and external/reference information | discrete spatial domain labels | spatial coordinates or neighborhood structure | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | reference-informed branch | CPU; code access unclear |
| SpatialGlue | integrate paired spatial modalities to decode multi-omics spatial domains | paired spatial multi-omics profiles with coordinates | multi-omics spatial domain labels | spatial graph/neighborhood prior | optional multimodal/image branch unclear | explicit or plausible multi-slice/batch branch | multi-omics spatial domain labels | spatial multi-omics integration | Optional GPU; code access unclear |
| BINARY | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code access unclear |
| stDyer | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | Optional GPU; code access unclear |
| SpatialLeiden | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code access unclear |
| GraphPCA | learn a spatial embedding or low-dimensional representation for downstream domain labeling | spatial expression matrix and spatial coordinates | spatial embedding or topics supporting domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | embedding for downstream domain labels | expression + spatial coordinates branch | CPU; code access unclear |
| iIMPACT | identify spatial domains using matched image or morphology cues with expression | spatial expression, coordinates, and histology/image features when available | discrete spatial domain labels | image plus spatial-neighborhood prior | histology/image-informed | explicit or plausible multi-slice/batch branch | discrete spatial domain labels | expression + image/morphology branch | Optional GPU; code access unclear |
| MNMST | identify spatial domains with graph- or neighborhood-aware spatial structure | spatial expression matrix and spatial coordinates | discrete spatial domain labels | spatial graph/neighborhood prior | none apparent | single-slice first; cross-slice support unclear | discrete spatial domain labels | expression + spatial coordinates branch | CPU; code access unclear |
| SpaDo | align and label spatial domains across slices, samples, or batches | one or more spatial expression slices with coordinates | slice-aligned domain labels | spatial coordinates or neighborhood structure | none apparent | explicit or plausible multi-slice/batch branch | slice-aligned domain labels | expression + spatial coordinates branch | CPU; code access unclear |

## Decision Tree

If reference-informed tissue segmentation is explicitly intended:
- Prefer / consider `IRIS`.
- Keep atlas or reference dependence visible rather than treating this branch as ordinary unsupervised clustering.

If spatial multi-omics integration is central to the domain call:
- Prefer / consider `SpatialGlue`.
- Keep this branch distinct from optional image-aware or contrastive rows that are not explicit spatial multi-omics integration methods.

If matched histology, morphology, or image signal should actively guide domain boundaries:
- Prefer / consider `ConGI`, `conST`, `DeepST`, `iIMPACT`, `SiGra`, `SpaGCN`, or `SpaSEG`.
- Use this branch only when matched morphology is expected to carry real domain information.

If multi-slice, batch-aware, or cross-sample domain comparison is central:
- Prefer / consider `BASS`, `MENDER`, `PRECAST`, `SPACEL`, or `SpaDo`.
- Consider `GraphST`, `Novae`, or `STAGATE` only when broad graph representations are part of the comparison objective.

If interpretable topics, semantic labels, markers, or tissue programs are more important than plain partitions:
- Prefer / consider `Pianno`, `SpaTopic`, or `STAMP`.
- Keep topic, semantic, or module outputs explicit rather than rewriting them as ordinary cluster labels.

If a statistical or probabilistic clustering frame is preferred:
- Prefer / consider `BayesSpace`, `BASS`, `DR-SC`, or `PRECAST`.
- Use branch-local benchmark support only inside the matching dataset regime.

If graph, neighborhood, or spatial-representation learning is the main route:
- Prefer / consider `ADEPT`, `CCST`, `GraphST`, `SEDR`, `SpaceFlow`, `STAGATE`, `STCC`, `stDyer`, or `stLearn`.
- Consider `BINARY` when binarized graph-convolution framing is the real modeling cue.

If CPU-first neighborhood screening or spatially aware low-dimensional structure is the practical branch cue:
- Prefer / consider `BANKSY`, `GraphPCA`, `MNMST`, `PROST`, `SpatialLeiden`, or `SpatialPCA`.
- Keep scalable embedding or clustering outputs distinct from explicit multi-slice alignment or topic-style outputs.

If a newer broad-representation or foundation-model route is the intended reading branch:
- Prefer / consider `Novae`.
- Keep newer representation claims under manual review rather than treating them as a universal ordering signal.

After choosing the branch:
- Keep branch-local benchmark or review support inside the matching family rather than turning it into one ordering across all families.
- Keep image-match, integration-quality, topic-output, and reference-bias caveats in the reading path.
- Re-check whether the output should be a discrete domain label, a slice-aligned domain map, an embedding for downstream labels, or a semantic/topic interpretation.
