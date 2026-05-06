# Segmentation

## Problem Boundary

Use this Layer 2 file after Layer 1 routes the task to `Segmentation`.

This topic covers direct cell segmentation and transcript-to-cell assignment, upstream transcript or fluorescence spot detection, histology or IF image-processing support for segmentation workflows, and joint image segmentation plus classification. These outputs are not interchangeable: spot coordinates, support-image outputs, transcript assignments, cell masks, and classified image objects should be kept distinct during selection.

Use another Layer 1 problem first when the primary task is downstream cell type inference, neighborhood analysis, communication analysis, or trajectory interpretation. Keep explicit boundary language for support-image and spot-detection rows, and retain the preprint caveat for `segger`.

## Method Feature Table

| Method | Selection role | Main input/signal | Main output | Segmentation Branch | Primary Segmentation Signal | Transcript Assignment Role | Annotation Coupling | Modality Fit | Compute/code cue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baysor | cell segmentation and transcript-to-cell assignment for imaging-based spatial transcriptomics | imaging-based ST molecule coordinates + gene identities, with optional prior segmentation or co-stain information | cell segmentation boundaries plus molecule assignments | cell segmentation / transcript assignment | transcript coordinates | primary | none | imaging-based ST | CPU; code available |
| Bering | joint noise-aware cell segmentation and molecular annotation | subcellular ST transcript coordinates and gene identities, with graph representations and optional pretrained transfer models | cell segmentation plus molecular or cell annotation outputs | cell segmentation / transcript assignment | graph transcript colocalization | primary | joint molecular annotation | subcellular ST | Optional GPU; code available |
| SCS | cell segmentation and spot assignment for high-resolution spatial transcriptomics | high-resolution ST spots or transcripts plus imaging data | cell assignments for high-resolution ST spots or transcripts | cell segmentation / transcript assignment | image + transcript signal | primary | none | subcellular ST | Optional GPU; code available |
| segger | fast transcript-to-cell link prediction for cell segmentation | imaging-based ST transcript coordinates, gene identities, and candidate cell context; optional scRNA-seq information may improve assignments | transcript-to-cell links and segmented cell assignments | cell segmentation / transcript assignment | heterogeneous graph transcript-cell signal | primary | optional scRNA/reference | imaging-based ST | Optional GPU; code available |
| UCS | unified cell segmentation across subcellular ST platforms | subcellular ST transcript data plus nuclei staining or nuclei segmentation information | cell segmentation and transcript assignment outputs | cell segmentation / transcript assignment | nuclei + transcript signal | primary | downstream only | subcellular ST | Optional GPU; code available |
| BIDCell | biologically informed cell segmentation for subcellular spatial transcriptomics | subcellular spatial transcriptomics data with transcript locations and morphology or cell-shape priors | segmented cells and transcript-to-cell assignments for subcellular ST data | cell segmentation / transcript assignment | image + transcript signal | primary | unclear | subcellular ST | Optional GPU; code available |
| VistoSeg | image-processing and segmentation-workflow support for spatial transcriptomics histology images | Visium or related high-resolution histology or immunofluorescence images paired with spatial transcriptomics data | processed histology or IF image features and segmentation-support outputs, not direct transcript-to-cell assignments | histology image processing / segmentation support | tissue image | not primary | downstream only | broad spatial omics | CPU; code available |
| STCellbin | cell-boundary based binning and generation of single-cell expression profiles from high-resolution ST | high-resolution spatial transcriptomics data with cell boundary images, especially Stereo-seq-like settings | cell-boundary informed bins and single-cell gene expression profiles | cell segmentation / transcript assignment | image + transcript signal | primary | none | subcellular ST | CPU; code available |
| Spotiflow | raw transcript spot detection upstream of imaging-based ST segmentation | 2D or 3D fluorescence microscopy images with spot-like transcript signals | detected spot coordinates | transcript spot detection | fluorescence image spots | upstream spot detection | none | RNA FISH / fluorescence microscopy | Optional GPU; code available |
| Piscis | automatic deep-learning spot detection for RNA FISH-derived imaging data | RNA FISH or fluorescence microscopy images with manually or synthetically annotated spot examples for training context | detected spot coordinates | transcript spot detection | fluorescence image spots | upstream spot detection | none | RNA FISH / fluorescence microscopy | Optional GPU; code available |
| CelloType | joint image-based instance segmentation and classification | multiplexed tissue or spatial-omics images | segmented and classified tissue objects or cells | joint segmentation / classification | tissue image | not primary | joint image classification | multiplex tissue / spatial omics image | Optional GPU; code available |

## Decision Tree

If the required output is raw transcript or fluorescence spot coordinates:
- Prefer / consider `Spotiflow` or `Piscis`.
- Treat these as upstream spot-detection rows rather than direct cell segmentation.

If the required output is histology or IF image processing that supports a segmentation workflow:
- Prefer / consider `VistoSeg`.
- Do not treat it as direct transcript-to-cell assignment or direct molecular cell segmentation.

If the required output is transcript-to-cell assignment, cell masks, or segmented cells from imaging-based or subcellular spatial transcriptomics:
- Continue within the cell-segmentation and transcript-assignment branch.

If a transcript-coordinate-first baseline is needed:
- Prefer / consider `Baysor`.

If segmentation should be coupled to molecular annotation or transfer learning:
- Prefer / consider `Bering`.

If useful imaging data are available and spot-to-cell assignment is central:
- Prefer / consider `SCS`.

If large imaging-based transcript assignment is central and preprint-level evidence is acceptable for the selection stage:
- Prefer / consider `segger`.
- Keep its preprint and independent-replication caveat visible.

If reliable nuclei information is available and nuclei-plus-transcript segmentation is scientifically appropriate:
- Prefer / consider `UCS`.

If biologically informed self-supervised boundary inference is the intended route:
- Prefer / consider `BIDCell`.

If reliable cell-boundary images already exist and cell-boundary-based binning is the real target:
- Prefer / consider `STCellbin`.

If the required output is image-object segmentation coupled to classification:
- Prefer / consider `CelloType`.
- Keep classification coupling visible rather than treating it as a transcript-coordinate-first assignment method.

After choosing a branch:
- Separate support-image, spot-detection, transcript-assignment, and classification-coupled outputs before comparing methods.
- Re-check whether annotation coupling or reference influence is scientifically intended before preferring `Bering`, `segger`, or `CelloType`.
