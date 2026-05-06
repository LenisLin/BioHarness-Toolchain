# Normalization

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Normalization`.

This topic currently keeps one dedicated spatial-aware normalization candidate, `SpaNorm`, for already measured spatial expression matrices when library-size effects may be spatially structured. Use it as a dedicated spatial-aware option with caution rather than as a guarantee that spatial biology will be preserved. Backbone or baseline workflow context remains visible here through `Scanpy`, `Seurat/sctransform`, `scran/scater`, `Giotto`, and `Squidpy`.

These backbone packages are visible to the agent but are not counted as dedicated spatial-aware normalization candidates and are not ranked against `SpaNorm`. Use another Layer 1 problem first when the task is panel design, denoising, artifact correction, QC, spatially variable gene detection, or expression prediction.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Normalization Branch | Spatial Signal Use | Backbone Context | Output Alteration Level |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SpaNorm | normalize measured spatial transcriptomics expression by modeling library-size effects while preserving spatial biology when assumptions hold | Spatial transcriptomics count matrix with spatial coordinates | normalized expression matrix for downstream spatial analyses | post-capture spatial-aware normalization | explicit spatial normalization model | Scanpy; Seurat/sctransform; scran/scater; Giotto; Squidpy | normalized expression |

## Decision Tree

If the active task is dedicated spatial-aware normalization of an already measured spatial expression matrix and library-size effects may be spatially structured:
- Consider `SpaNorm`, while keeping open the possibility that normalization can also attenuate real spatial structure when technical depth and biology are entangled.

If the request is for routine workflow normalization, HVG selection, or preprocessing context rather than a dedicated spatial-aware normalization candidate:
- Use `Scanpy` for AnnData/scverse workflow context.
- Use `Seurat/sctransform` for R/Seurat workflow context.
- Use `scran/scater` for Bioconductor workflow context.
- Use `Giotto` for broad spatial workflow context.
- Use `Squidpy` for broad spatial workflow context around AnnData objects.

Across both branches:
- Keep `Scanpy`, `Seurat/sctransform`, `scran/scater`, `Giotto`, and `Squidpy` visible as backbone context only.
- Do not count or rank those backbone workflows as dedicated spatial-aware normalization candidates against `SpaNorm`.
- Carry the caveat that normalization can attenuate real spatial biology when technical depth and tissue structure are entangled.
