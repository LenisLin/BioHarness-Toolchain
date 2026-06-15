# Validation Input Preparation Outputs

## Required Method Result

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

## Output Rule

`source_route_completion` records the executed acquisition path before canonical input status is interpreted.

`download_or_localize`, `unpack_or_extract`, and `artifact_selection` may be `not_applicable` only with a recorded reason.

For native containers, `unpack_or_extract: complete` means the result identifies the native object classes, selected canonical fields, extraction or normalized export route, and evidence path.

For normalized native exports, `artifact_selection` records both the original native payload and the stable artifacts used for Python-side canonical AnnData construction.

`canonical_input_status: available` means canonical AnnData exists and is ready for `prepare_spatial_domain_input`.

`public_contract` and `strict_output` record the contract summary or evidence path used for this readiness check; they do not require the input-preparation subagent to re-audit the surface contract.

`INPUT_READY` requires `source_route_completion.completion_status: complete`, canonical AnnData, downstream-selectable `prepare_spatial_domain_input` build evidence, a passing readiness check, and image alignment readiness pass when the first surface requires image payload.

`INPUT_REPAIR_REQUIRED` requires source-route completion to reach the current executable boundary and a concrete repair target. Missing image alignment evidence is `INPUT_REPAIR_REQUIRED`, not a terminal harness validation failure.

A route probe without required local artifact handling, unpack/extract/read evidence, path check, format check, usability check, or canonical input attempt is verifier repair evidence, not an accepted method result.

A native-container result with object names or class summaries but no required field extraction, normalized export, identifier consistency check, or canonical input attempt is verifier repair evidence.

Input-preparation gaps remain Stage 1 repair records and are not terminal harness validation failures.
