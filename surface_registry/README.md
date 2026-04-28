# Surface Registry Blueprint

This directory stores execution manifests for future Layer 3 surfaces.

Layer 3 is the execution surface registry and callable contract layer. It stores stable callable surface manifests, not backend adapter implementations.

Surface manifests may be drafted from `MethodExecutionPlanningRecord` outputs, with historical or lightweight `MethodEngineeringAudit` notes as supporting evidence. They should separate functional surfaces from backend function bindings. The registry should not store raw backend code.

Each manifest should define:

- the stable surface identifier
- the input and output contracts
- the bound environment profile
- validation hooks and approval requirements
- typed failure modes
- optional Layer 4 backend adapter references

Layer 3 surfaces may reference Layer 4 `BackendAdapterSpec` IDs when available. The reference does not make backend internals agent-facing by default.

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
