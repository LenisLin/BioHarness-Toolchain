# Parent Function Extraction

## Purpose

This file defines the agent workflow for extracting and organizing parent-function candidates from multi-method stage evidence before human confirmation.

Extraction starts only after integration-readiness audit routing has identified the usable evidence set for the feature-level integration pass.

## Core Model

A `feature` is the analysis-problem container. A feature is not itself a callable parent function.

Parent functions are stage-level execution functions extracted after comparing methods under the same feature. A single method can provide stage evidence, but it cannot define a parent function alone.

Code Planner stage-inform groups are method-local reading aids. They become useful only when multiple methods under the same feature are compared.

## Inputs

- Stage-inform groups from method-specific Code Reading Planner outputs.
- Code Function-Family Reader outputs.
- Output/Validation cues for output-related stages.
- Package review gaps when they identify missing code or output evidence.
- Integration-readiness audit outputs from `integration_readiness_audit.md`.
- Completed supplemental-reading outputs from `supplemental_reading.md`.

## Agent Workflow

1. Collect method-local stage evidence whose Stage Design evidence area is audit-closed with `Downstream Eligibility` of `eligible_for_downstream_integration` or `eligible_with_execution_evidence_deferred`. Environment or validation categories should not globally block stage extraction unless the Stage Design evidence area itself is not audit-closed.
2. Add completed supplemental-reading evidence only when it resolves an audit or extraction request.
3. Preserve the method-native source locators, entrypoints, controls, mutations, and gaps.
4. Cluster method-local groups into one or more provisional stage-level parent-function candidates only when they appear functionally comparable.
5. Draft rough parent-function records for candidates that have enough cross-method evidence to support human review.
6. For each rough parent-function draft, record the construction basis, method coverage, semantic conflicts, and method x surface planning-level alignment route draft.
7. Identify divergent implementation details instead of forcing them into one backend-shaped parent function.
8. Prepare explicit human-review questions for each provisional parent-function candidate.
9. Do not decide final parent functions, implementation support states, adapters, wrappers, rewrites, environment readiness, validation status, or runtime feasibility.

## Stage Evidence Inventory Table

| Method | Method-Local Group | Native Entry Points | Functional Role | Input Evidence | Output/Mutation Evidence | Native Controls / State | Key Gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Candidate Stage Clustering Table

| Provisional Common Stage | Methods Contributing Evidence | Shared Functional Pattern | Divergent Implementation Details | Initial Concern |
| --- | --- | --- | --- | --- |

## Parent Function Coverage Matrix

| Parent Function Candidate | Methods With Direct Evidence | Methods With Internal / No-op / Not-Applicable Route | Methods Not Covered | Coverage Rationale | Semantic Conflict Check | Core Function Coverage Note |
| --- | --- | --- | --- | --- | --- | --- |

## Parent Function Construction Basis Table

| Parent Function Candidate | Standard Action | Standard Input Contract | Strict Main Output Contract | Native Evidence Used | Native Details Excluded From Layer 3 | Downstream Bridge Note |
| --- | --- | --- | --- | --- | --- | --- |

## Method x Surface Alignment Route Draft Table

| Method | Parent Function Candidate | Method-Local Stage Evidence | Same-Semantics Fit | Native Input / Output Shape | Initial Alignment Route | Route Rationale | Open Mapping Gaps | Downstream Bridge Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Initial alignment routes are planning-level hypotheses for later bridge work. Use the current Gate 1 route values when evidence supports them: `adapter`, `wrapper`, `compatibility_rewrite`, `algorithmic_rewrite`, or `hold`. If a route is not established, use `hold` with a concrete reason rather than an unknown state.

Extraction should follow semantic-first grouping. A method-local stage that is fused into setup, fitting, or output handling can still belong to the same parent-function candidate when the scientific execution role is shared. Do not mark a retained method as unsupported only because the native code does not expose the stage as a separate function. Record the fused/internal evidence and the planning-level alignment route instead.

These routes are not final support decisions, Gate 2 review status values, or runtime evidence.

## Agent Output

The agent output should include:

- provisional stage-level parent-function candidates;
- supporting method evidence;
- a rough parent-function draft for each candidate;
- construction-basis notes for standard action, input, and strict main output;
- method coverage and non-coverage notes;
- method x surface planning-level alignment route drafts;
- notes distinguishing semantic fit from implementation route;
- divergence notes;
- candidate adjacent-stage boundary issues;
- human-review questions;
- evidence gaps that may require additional source reading.

## Supplemental Reading Requests

When extraction identifies a source gap that may change a parent-function candidate decision, record a targeted supplemental-reading request through `supplemental_reading.md` instead of filling the gap by inference.

Use supplemental reading when the missing source evidence may affect:

- parent-function candidate classification;
- standard AnnData input interpretation;
- standard output or result assignment;
- method-native state boundary;
- backend controls that affect scientific output;
- wrapper mapping or failure translation;
- functional-test target definition.

Do not request supplemental reading for optional plot styling, display-only behavior, non-core diagnostic artifacts, basic validation-asset discovery after audit closure, or questions that require runtime observation rather than source reading.

## Boundary

This workflow produces rough parent-function drafts for Gate 1 review. It does not finalize parent functions, permit downstream bridges, or claim runtime support.
