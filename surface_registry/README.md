# Surface Registry Blueprint

This directory stores execution manifests for future Layer 3 surfaces.

Layer 3 is the execution surface registry and callable contract layer. It stores stable callable surface manifests, not backend adapter implementations.

Surface manifests may be drafted from `MethodExecutionPlanningRecord v0.7.1` outputs, with historical or lightweight `MethodEngineeringAudit` notes as supporting evidence. They should separate functional surfaces from backend function bindings. The registry should not store raw backend code.

Each manifest should define:

- the stable surface identifier
- the input and output contracts
- the bound environment profile
- validation hooks and approval requirements
- typed failure modes
- optional Layer 4 backend adapter references

Layer 3 surfaces may reference Layer 4 `BackendAdapterSpec` IDs when available. The reference does not make backend internals agent-facing by default.

Every Layer 3 functional stage should have a corresponding Layer 4 binding status in the implementation-facing `BackendAdapterSpec`: `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`. Missing or unresolved critical bindings block implementation readiness but do not make backend details agent-facing.

Layer 3 execution stage vocabulary:

```text
input_check
method_preprocessing
core_structure_building
model_fit_or_inference
output_assignment
artifact_export
final_validation
visualization
```

Layer 4 binding examples:

```text
backend package function names
script entrypoints
parameter mappings
input conversion logic
output extraction logic
temporary file layout
error translation
```

These files are blueprint execution manifests only. They are not yet a runtime dispatch layer.

Backend adapter specs belong under [contracts](../contracts) examples or a future implementation-facing registry, not directly mixed with surface manifests unless clearly separated.

Illustrative examples should live under `surface_registry/examples/` so they do not imply that a current Layer 3 default has been frozen.

The current `surface_registry/examples/spatial_domain_identification.spagcn.example.json` file is a legacy illustrative example using an older surface shape. Keep it as historical example material only; do not treat it as a live SpaGCN planning artifact or a v0.7.1 MethodExecutionPlanningRecord output.

Method-specific intermediate surface drafts must remain outside this repository until promoted. Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. BANKSY v0.7.0 is accepted as a template trial under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/BANKSY/v0.7.0/`; the BANKSY v0.6.1 draft is historical failed/stress-test material only. Neither record is a production surface claim.
