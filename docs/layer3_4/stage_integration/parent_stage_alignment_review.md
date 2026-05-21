# Parent Function / Execution Surface Alignment Review

## Purpose

This file defines Gate 1: the human-in-the-loop review for stage-level parent-function candidates as execution-surface candidates.

Gate 1 confirms, revises, routes for repair, or defers candidate execution surfaces produced by agent-side extraction. Gate 1 reviews both semantic boundaries and method x surface planning-level alignment routes. It does not implement adapters, run methods, validate runtime behavior, or finalize Layer4 support decisions.

## Inputs

- Rough parent-function drafts from `parent_function_extraction.md`.
- Parent Function Coverage Matrix.
- Parent Function Construction Basis Table.
- Method x Surface Alignment Route Draft Table.
- Method evidence summaries and source locators.
- Known evidence gaps.

## Review Questions

For each parent-function candidate, review:

- Is this a cross-method function within the same feature?
- Does the candidate perform a real execution-layer action rather than only checking, auditing, or reporting readiness?
- Is the candidate supported by a substantial cross-method subset without semantic conflict?
- Can methods that do not implement this candidate be cleanly marked internal, no-op, not applicable, held, or deferred?
- Does each retained method have method-local stage evidence that fits the candidate surface semantics?
- If a method's native stage is fused into setup, fitting, or output handling, is the shared semantic role still clear enough for this surface?
- What is the planning-level alignment route for each method: `adapter`, `wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, or `hold`?
- Which route hypotheses are strong enough to enter downstream bridge planning?
- Which route hypotheses require targeted supplemental reading before bridge planning?
- Does the full parent-function set cover the retained methods' core functionality for the feature?
- Is it agent-visible, Layer4-internal, optional support, method-specific, or deferred?
- Can the standard input be expressed using AnnData?
- What standard output or mutation is expected?
- Are backend-native input/output differences Layer4-solvable without changing the Layer 3 contract?
- Is any apparent mismatch actually a semantic output mismatch that should be routed out of the feature?
- Which backend controls must remain hidden?
- Can methods implement this stage internally or as a no-op?
- Does the stage boundary overlap with adjacent preprocessing, inference, assignment, visualization, or validation work?
- What missing evidence would change the decision?

## Execution Surface Decision Table

| Parent Function Candidate | Gate 1 Decision | Agent Visibility | Standard Input | Strict Main Output | Boundary Notes | Blocks Downstream Bridge? | Re-Review Required? |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Method x Surface Semantic Coverage Table

| Method | Parent Function Candidate | Method-Local Stage Evidence | Same-Semantics Fit? | Fused / Internal Stage? | Semantic Notes |
| --- | --- | --- | --- | --- | --- |

## Method x Surface Alignment Route Table

| Method | Parent Function Candidate | Planning-Level Alignment Route | Route Rationale | Open Mapping Gaps | Downstream Bridge Action |
| --- | --- | --- | --- | --- | --- |

## Gate 1 Routing Table

| Item | Gate 1 Decision | Required Repair / Supplemental Reading | Blocks Downstream Bridge? | Evidence Preconditions | Explicit Non-Claims |
| --- | --- | --- | --- | --- | --- |

## Gate 1 Decision And Routing Values

Use one primary Gate 1 decision per parent-function candidate:

- `promote_to_downstream_bridge`
- `revise_stage_boundary`
- `route_to_supplemental_reading`
- `return_to_parent_extraction`
- `mark_layer4_internal`
- `mark_optional_support`
- `defer_missing_evidence`
- `reject_for_current_pass`

Only `promote_to_downstream_bridge` permits downstream method-to-parent bridge planning. Other decisions require repair, re-review, or explicit deferral before downstream use.

## Gate 1 Remediation Loop

Gate 1 remediation repairs static evidence gaps that affect parent-function boundaries, execution-surface scope, or method x surface planning routes.

Use Gate 1 remediation when the affected item has one of these issues:

- parent-function boundary is unclear;
- execution-surface scope is unclear;
- method x surface planning-route evidence is insufficient;
- stage-level shared pattern or divergence is unclear.

Gate 1 remediation may use targeted supplemental reading and then re-review only the affected Gate 1 items. It must not implement adapters or wrappers, perform environment build checks, run author cases, or use runtime observations.

Only items promoted by Gate 1 as `promote_to_downstream_bridge` may enter downstream integration. Items repaired through Gate 1 remediation must be re-reviewed before downstream bridge planning.

## Parent-Function Candidate Record Template

Use this template inside this file. Do not create a separate template file.

```yaml
parent_function_candidate:
  feature:
  parent_function_name:
  authority_status: planning_candidate
  agent_visibility: candidate / internal / optional
  execution_function:
    action:
    not_a_check_or_audit: true / false
  coverage:
    methods_with_direct_evidence:
    methods_with_internal_or_noop_route:
    methods_not_covered:
    coverage_rationale:
    semantic_conflict_check:
    feature_core_coverage_note:
  standard_contract:
    input:
      type: AnnData
      required_contents:
        - expression matrix
        - spatial coordinate matrix
      optional_contents:
        - image
        - annotations
    strict_main_output:
    auxiliary_artifacts_not_in_public_return:
  method_evidence:
    METHOD_ID:
      evidence_summary:
      native_entrypoints:
      native_input_output_shape:
      native_mapping_notes:
      gaps:
  method_alignment_routes:
    METHOD_ID:
      method_local_stage_evidence:
      same_semantics_fit: yes / no / unclear
      fused_or_internal_stage: yes / no / unclear
      planning_level_alignment_route: adapter / wrapper / compatibility_rewrite / algorithmic_rewrite / hold
      route_rationale:
      open_mapping_gaps:
      downstream_bridge_action:
  excluded_backend_controls:
  allowed_layer4_variation:
  unresolved_questions:
  gate1_decision: promote_to_downstream_bridge / revise_stage_boundary / route_to_supplemental_reading / return_to_parent_extraction / mark_layer4_internal / mark_optional_support / defer_missing_evidence / reject_for_current_pass
  required_repair_or_routing:
  blocks_downstream_bridge: true / false
  re_review_required: true / false
  evidence_preconditions:
  explicit_non_claims:
```

`planning_level_alignment_route` is a Gate 1 bridge-planning hypothesis. It is not a final Layer4 support decision and must not be used to claim implementation or runtime readiness.

## Boundary

Human review can promote a planning candidate, but it does not implement support, claim runtime readiness, or finalize production architecture.
