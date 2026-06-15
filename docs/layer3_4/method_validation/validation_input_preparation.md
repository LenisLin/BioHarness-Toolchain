# Validation Input Preparation

## Purpose

Prepare method-scoped canonical validation input for later harness validation.

This workflow obtains the method validation payload, prepares canonical AnnData, and checks that the input can enter the first execution surface, `prepare_spatial_domain_input`.

## Required Output

```yaml
validation_input_preparation_result:
  method:
  accepted_status: INPUT_READY | INPUT_REPAIR_REQUIRED | BLOCKED_EXTERNAL
  source_payload:
  localization_status: available | repair_required | blocked_external
  localization_evidence:
    local_check:
    remote_route:
    resolved_artifacts:
    portal_resolution:
    helper_package_route:
    source_route_completion:
      local_existing_check:
      remote_resolution:
      download_or_localize:
      unpack_or_extract:
      artifact_selection:
      path_existence_check:
      format_check:
      usability_check:
      completion_status: complete | repair_required | blocked_external
  canonical_input_status: available | repair_required | blocked_external
  canonical_input_record:
    path:
    object_type: AnnData
    expression_source:
    observation_source:
    feature_source:
    coordinate_source:
    spatial_coordinate_contract:
      platform_family:
      observation_unit: spot | cell | bin | other | unknown
      coordinate_semantics:
      coordinate_unit_or_frame:
      coordinate_range:
    image_payload_source:
    image_alignment_record:
      required_for_method: true | false
      image_source:
      image_key_or_resolution:
      image_shape:
      coordinate_to_image_transform_evidence:
      readiness_alignment_check:
        status: pass | fail | not_applicable
        reason:
  first_execution_surface:
    surface_name: prepare_spatial_domain_input
    build_evidence:
    public_contract:
    strict_output:
    readiness_check: pass | fail | blocked_external | not_run
    output_record:
  input_preparation_evidence:
  repair_target:
  files_written:
```

## Workflow

1. Confirm method payload, reviewed local target, remote locator, locator type, required files, data target, and helper package route.
2. Check reviewed local target and record local_existing_check.
3. For direct_download, download or locate the reviewed artifact under the method data directory.
4. For portal_or_index, resolve the reviewed page/index to concrete method-required artifacts, then download or locate them under the method data directory.
5. For package_data_route, use the named helper package and record produced local artifacts.
6. For archives or native containers, complete the extraction/read workflow before canonical construction:
   - Identify the native object classes and the source fields for expression, observations, features, coordinates, and required image payload.
   - Use direct language-bridge conversion for simple list, matrix, and data.frame-like containers when it preserves field names and dimensions.
   - For complex native containers such as S4, S4Vectors DFrame, Seurat, SingleCellExperiment, or SummarizedExperiment objects, normalize required fields in the native runtime into stable artifacts such as MatrixMarket, CSV, TSV, or JSON summaries before Python-side AnnData construction.
   - Record dimensions, row and column identifiers, selected fields, normalized artifact paths, and identifier consistency checks.
7. Run path existence, format, and usability checks on localized or extracted artifacts.
8. Build canonical AnnData from checked artifacts and record expression, observation, feature, coordinate, and image sources.
9. For image-aware Visium/Xenium methods, record image alignment evidence before running `prepare_spatial_domain_input`.
10. Apply deterministic field mapping required by prepare_spatial_domain_input.
11. Run prepare_spatial_domain_input when canonical AnnData and downstream-selectable first-surface build evidence are available.
12. Return INPUT_READY only when canonical AnnData exists, readiness check passes, and image alignment readiness passes when the first surface requires image payload.
13. Return INPUT_REPAIR_REQUIRED only after source-route completion reaches the current executable boundary and a concrete input-contract, native-object conversion, field mapping, coordinate, image, image-alignment, or build-evidence repair target is recorded.
14. Return BLOCKED_EXTERNAL when progress requires network, permission, storage, credentials, or unavailable external service access.

Missing image alignment evidence is `INPUT_REPAIR_REQUIRED`, not `TERMINAL_FAIL`.
