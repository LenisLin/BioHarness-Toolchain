# Method Validation

This directory defines post-build method-level harness testing for Layer3/4.

Method validation is a small, method-scoped test stage. It runs after reviewed environment evidence and downstream-selectable Layer3/4 build evidence exist.

Method validation has three workflow units:

1. `validation_input_preparation`: prepare reviewed canonical validation input.
2. `validation_reference_preparation`: prepare native or expected reference evidence.
3. `method_harness_validation`: run the BioHarness Layer3 callable chain using a generated selected-surface config derived from Stage2 parameter evidence and Layer3-M exposed variables, then check runtime behavior, output contract evidence, selected Layer3 invocation evidence, and consistency.

Input preparation and reference preparation are prerequisites. They produce repair records when incomplete. Method harness validation subagents write verifier candidate results. Package-level terminal results are written only after verifier acceptance.

## Orchestration

Package-level orchestration is defined in `method_validation_workflow.md`.

Each stage uses method subagents in batches of at most 6 methods. Each stage has verifier acceptance before its evidence is consumed by the next stage.

Terminal package results are written only from verifier-accepted `method_harness_validation` results.
