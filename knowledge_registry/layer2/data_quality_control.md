# Data Quality Control

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Data Quality Control`.

This topic covers stage-aware quality-control methods for raw or prepared spatial data objects, including upstream preprocessing plus QC, prepared-object automated QC reporting, post-count local or regional spatial QC, and post-localization 3D overlap QC.

Use another Layer 1 problem first when the main task is direct artifact correction, normalization, denoising, segmentation, or biological interpretation. QC flags and overlap summaries are review signals, not direct claims about biology.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | QC Target Level | Input Processing Stage | Platform Scope | Spatial Artifact Handling | Pipeline Breadth | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SpotSweeper | detect local or regional post-count spatial QC artifacts that may be missed by global count filters | processed spatial transcriptomics counts with spatial coordinates | spatial QC flags, local artifact summaries, and candidate regions for contextual review | local/regional spatial QC | post-count / prepared object | spatial transcriptomics with coordinates | focused local/regional artifact flags | focused QC module | CPU; code available |
| SpatialQC | automated quality-control reporting, filtering, and data-cleaning support for spatial transcriptome data | spatial transcriptomics data in supported object formats with spatial coordinates and sample/gene/cell or spot metadata | QC reports, filtered spatial transcriptome objects, and cell/spot/gene quality summaries | automated report + filtering | prepared spatial transcriptome object | cross-platform spatial transcriptome data | general QC / optional spatial review | automated QC reporting/data-cleaning | CPU; code available |
| ovrlpy | quantify vertical overlap or spatial co-localization patterns as quality-control evidence after transcript localization | transcript localization tables with x/y/z coordinates after molecule detection and localization | overlap metrics, 3D localization summaries, and QC evidence for manual/contextual review | 3D molecule/coordinate overlap | post-transcript-localization | molecule-localization spatial assays with z information | vertical overlap / co-localization evidence | focused QC module | CPU; code available |
| stPipe | perform upstream preprocessing and QC before downstream spatial analysis | raw or near-raw sequencing-based spatial transcriptomics data and associated metadata | processed spatial transcriptomics objects, QC summaries, and preprocessing outputs | upstream preprocessing/QC | raw / near-raw preprocessing | sequencing-based spatial transcriptomics | general upstream QC, not focused artifact correction | preprocessing + QC workflow | CPU; code available |

## Decision Tree

If the input is raw or near-raw sequencing-based spatial transcriptomics data and the task is preprocessing plus QC:
- Prefer / consider `stPipe`.

If the input is a prepared spatial transcriptome object and the goal is automated QC reporting, filtering, or data cleaning:
- Prefer / consider `SpatialQC`.

If the input is a prepared post-count spatial object and the main concern is local or regional spatial artifacts:
- Prefer / consider `SpotSweeper`.

If the input is post-localization transcript coordinates with z information and the QC question is vertical overlap or 3D co-localization evidence:
- Prefer / consider `ovrlpy`.

After choosing the stage-compatible branch:
- Do not force head-to-head ranking across incompatible processing stages or data objects.
- Review QC calls against tissue morphology, platform artifacts, and sample handling before treating them as meaningful spatial biology.
