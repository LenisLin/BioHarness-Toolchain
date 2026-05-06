# Layer 1/2 Selection Protocol

This directory defines the agent-facing selection protocol for the BioHarness spatial transcriptomics Layer 1/2 knowledge registry.

The protocol constrains an agent to use `knowledge_registry/layer1/task_catalog.md` for problem routing before opening exactly the relevant `knowledge_registry/layer2/*.md` method-selection file.

This is a knowledge-layer protocol. It is not a Python API, runtime dispatcher, command contract, environment binding, adapter plan, default-method policy, or execution-readiness claim.

## Files

- `agent.md`: natural-language operating instructions for an LLM or agent.
- `selection_policy.json`: machine-readable routing and guardrail policy.
- `selection_policy.schema.json`: structural schema for the policy file.

## Required Use

For ordinary spatial transcriptomics downstream-analysis tasks, the agent should stay inside this registry:

1. Identify the scientific object and requested target output.
2. Select one Layer 1 `Analysis Problem`, or split into multiple Layer 1 problems when the user asks for multiple endpoints.
3. Open the matching Layer 2 topic file.
4. Select methods only within that topic's method table and decision tree.
5. Report uncertainty, ambiguity, or out-of-formal requests explicitly instead of inventing new routes or packages.

