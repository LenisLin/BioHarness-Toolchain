# Validation Input Preparation Method Prompt

## Prompt Fields

```yaml
analysis_problem:
method:
method_output_root:
owned_paths:
read_only_inputs:
case_data:
canonical_input_requirement:
first_execution_surface:
  surface_name: prepare_spatial_domain_input
  build_evidence:
  public_contract:
  strict_output:
execution_environment:
return_evidence:
stop_condition:
```

## Status Values

```text
INPUT_READY
INPUT_REPAIR_REQUIRED
BLOCKED_EXTERNAL
```

## Source Route Completion

Complete the reviewed source route before returning a method status.

For local targets, check the reviewed local path and record path, format, and usability evidence.

For direct_download, resolve the reviewed locator, download or locate the artifact under the method data directory, then check path, format, and usability.

For portal_or_index, resolve the portal or index to concrete method-required artifacts, record selected artifacts and selection reason, download or locate them, then check path, format, and usability.

For package_data_route, use the named helper package and record the local artifacts it produces.

For archives, zip files, RData/RDA, Seurat objects, or other native containers, run a field-level extraction workflow for canonical AnnData sources.

For native containers:
1. Record loaded object names, native classes, dimensions, and available row or column identifiers.
2. Select the expression, observation, feature, coordinate, and required image fields needed by the canonical input.
3. Use direct bridge conversion only when the object behaves as a simple list, matrix, or data.frame and the converted object preserves names, dimensions, and values.
4. For complex native objects, export the selected fields from the native runtime into stable artifacts such as MatrixMarket, CSV, TSV, or JSON summary files.
5. Read the stable artifacts from Python and verify identifier consistency before building AnnData.
6. Record source field, target AnnData field, transformation, artifact path, and identifier consistency result for each selected field.

A reachability probe is route evidence. Source route completion requires the local artifact, field-level extraction or normalized export evidence, path checks, format checks, and usability checks, or a concrete external blocker.

For image-aware Visium/Xenium methods, record image alignment evidence before running `prepare_spatial_domain_input`. The canonical input record must distinguish spatial coordinate semantics from image pixel frame and must record image source, image key or resolution, image shape, coordinate-to-image transform evidence, and readiness alignment check status.

## Status Rules

Return `INPUT_READY` when source-route completion is complete, canonical AnnData exists, required mapping evidence is recorded, `prepare_spatial_domain_input` accepts the input, and image alignment readiness passes when the first surface requires image payload.

Return `INPUT_REPAIR_REQUIRED` when source-route completion has reached the current executable boundary and the remaining gap is a concrete input-contract, conversion, field-mapping, coordinate, image-payload, image-alignment, native-object, or first-surface build-evidence repair.

Missing image alignment evidence is `INPUT_REPAIR_REQUIRED`, not `TERMINAL_FAIL`.

Use the `prepare_spatial_domain_input` contract to guide deterministic input adjustment. Record each adjustment with source field, target field, and reason.

Return `BLOCKED_EXTERNAL` when the next required source-route action needs network, permission, storage, credentials, or unavailable external service access.
