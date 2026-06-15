# Validation Input Preparation Completion Verifier Prompt

## Purpose

Read-only verifier for validation input preparation evidence.

## Acceptance Rules

Accept `INPUT_READY` when `source_route_completion.completion_status` is complete, canonical AnnData exists, localization evidence is complete, required mapping evidence is recorded, downstream-selectable `prepare_spatial_domain_input` build evidence is recorded, readiness check passes, and image alignment readiness passes when the first surface requires image payload.

Accept `INPUT_REPAIR_REQUIRED` when source-route completion reached the current executable boundary and the remaining repair target is recorded.

Accept `INPUT_REPAIR_REQUIRED` when `prepare_spatial_domain_input` build evidence is missing, stale, or not downstream-selectable after source-route completion reaches the current executable boundary and the repair target is recorded.

Accept `INPUT_REPAIR_REQUIRED` when image alignment evidence is missing or fails after source-route completion reaches the current executable boundary and the repair target is recorded.

Accept `BLOCKED_EXTERNAL` when the next action requires network, permission, storage, credentials, or unavailable external service access.

Return `REPAIR_REQUIRED` when a direct_download route is reachable but no local artifact is written or linked.

Return `REPAIR_REQUIRED` when a portal_or_index route is probed but concrete method-required artifact selection is not recorded.

Return `REPAIR_REQUIRED` when an archive or native payload is available but evidence does not identify required canonical input fields and their extraction or normalized export route.

Return `REPAIR_REQUIRED` when a complex native object is summarized only by object name, class, or load success without field-level usability and identifier-consistency evidence.

Return `REPAIR_REQUIRED` when a language-bridge conversion error leaves required native fields unread and no native-runtime normalized export is recorded.

Return `REPAIR_REQUIRED` when path existence, format, or usability checks are skipped.

Return `REPAIR_REQUIRED` when usable artifacts exist but canonical AnnData construction is not attempted.

Return `REPAIR_REQUIRED` when a method result treats an incomplete source-route action as accepted `INPUT_REPAIR_REQUIRED`.

Return `REPAIR_REQUIRED` when an image-aware Visium/Xenium method marks `INPUT_READY` without separate spatial coordinate semantics, image pixel frame, transform evidence, and image alignment readiness pass when the first surface requires image payload.

## Output

```yaml
verifier_result:
  scope: method | package
  verdict: PASS | REPAIR_REQUIRED | BLOCKED_EXTERNAL
  method_acceptance:
    - method:
      accepted_status: INPUT_READY | INPUT_REPAIR_REQUIRED | BLOCKED_EXTERNAL
      evidence_path:
  required_repairs:
    - method:
      stage: validation_input_preparation
      repair_instruction:
      evidence_needed:
```
