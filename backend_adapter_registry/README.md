# Backend Adapter Registry Blueprint

This directory is reserved for generic Layer 4 registry guidance or promoted implementation-facing adapter specs if a higher-authority project document accepts them into repository state.

Layer 4 artifacts describe backend adapter, wrapper, or rewrite bindings for Layer 3 execution surfaces. They may include backend function names, source paths, call graphs, parameter mapping, input/output conversion, filesystem policy, environment binding, smoke tests, fidelity tests, and failure translation.

Every Layer 3 functional surface must be represented in Layer 4 with a binding status: `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`. A Layer 4 draft may be accepted for planning with file-level evidence, but critical backend entrypoints, parameter mappings, and output mappings must reach symbol-level or line-level evidence before MVP adapter implementation starts.

Draft adapter specs may use `source_symbol_not_resolved_in_current_inventory` only as an explicit blocker with `implementation_blocker: true` and `resolution_required_before: MVP_adapter_implementation`. It is not allowed in implementation-ready adapter specs.

Method-specific intermediate adapter drafts must remain in the NAS results workspace until promoted. Live method audit packs are NAS artifacts. Project docs describe the process, not the live intermediate outputs. Their presence is not a production adapter claim, and `implementation_status` must remain `not_implemented` unless actual runtime code exists.
