# Contracts Blueprint

This directory stores public contract schemas for the substrate runtime blueprint.

The schemas define stable planning-layer objects that future harness code may depend on directly, plus lightweight engineering-stage artifacts used before runtime contracts are finalized:

- `SkillSpec`
- `ExecutionSurfaceSpec`
- `EnvironmentProfile`
- `BackendAdapterSpec`
- `RunRecord`
- `ValidationReport`
- `MethodEngineeringAudit`

`ExecutionSurfaceSpec` is a Layer 3 contract for stable callable surfaces. `BackendAdapterSpec` is a Layer 4 implementation-facing contract for adapter, wrapper, or rewrite bindings.

`MethodEngineeringAudit` is an engineering-stage artifact, not a runtime API. It captures repository/code inspection notes for promoted Layer 2 methods and feeds separate Layer 3 `ExecutionSurfaceSpec` and Layer 4 `BackendAdapterSpec` drafts.

Example instances live under [contracts/examples](examples) so the contract layer can be reviewed before runtime code is written.
