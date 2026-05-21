# Supplemental Reading

## Purpose

This file defines the targeted rereading pass triggered by an integration-readiness audit, parent-function extraction, Layer4 bridge planning, environment integration, or a functional-testing planning question tied to an existing author-case locator.

Supplemental reading answers a specific evidence question. It does not rerun full repository reading, install packages, run methods, design adapters, decide support, or replace build/execution evidence evaluation.

Environment supplemental reading is only for audit closure before downstream environment integration, or for audit-queued locator defects with exact configuration, install, CI, container, or dependency evidence targets. After audit closure, environment integration should not keep open a generic "continue reading the repository" item; unresolved environment questions route to text conflict organization or `execution_evidence_needed_after_gate2`.

Validation supplemental reading after audit closure may clarify stage-specific, bridge-specific, or expected-behavior questions from existing author-case locators. It should not rediscover basic author-case asset locators that should have been closed by the integration-readiness audit.

## Scope Types

- `stage_scoped`: answers a source-visible question needed to classify or bound a parent-function candidate across methods.
- `method_stage_scoped`: answers a source-visible question for one method's bridge to a candidate parent function.
- `method_scoped`: answers a method-level environment, validation, output, or package-coverage question that affects integration.

Environment `method_scoped` requests must name concrete locators or a concrete missing-locator defect. They should not permit a broad reread after the audit has already closed.

## Stage-Specific Remediation Boundaries

Audit-closing remediation repairs repository-reading package readiness defects before downstream integration.

Gate 1 remediation repairs parent-function, execution-surface, or method x surface route evidence before downstream integration. It may support re-review of affected Gate 1 items.

Targeted planning repair after Gate 2 repairs specific planning-record defects found during downstream planning review. It is limited to `layer4_bridge_planning`, `environment_integration_planning`, and `functional_testing_planning`.

Targeted planning repair may read official external static documentation, vignettes, or example repositories only when linked by the method's official README, site, or repository. It must record such evidence as static locator evidence and return an updated planning record for Gate 2 review.

## Inputs

- Audit or stage-integration request ID.
- Scope type.
- Target method or methods.
- Target parent-function candidate, if applicable.
- Evidence package pointers.
- Exact source, docs, configuration, notebook, output, or validation locators to inspect.
- NAS output path for the filled supplemental-reading return.

## Subagent Prompt

Use this prompt shape for a targeted read-only assignment:

```text
Read only the specified locators for the named method and request ID.

Return source-visible evidence that answers the stated question. Include file paths,
symbols, notebook cells, configuration keys, output names, or documentation anchors
when visible.

Do not install dependencies, run code, perform import/load checks, design adapters, choose planning
routes, assign implementation status, make support decisions, infer behavior without
source evidence, or broaden the task into full repository reading.

If the question cannot be answered from the allowed locators, state the unresolved
point and route it to the appropriate queue: supplemental reading with narrower or
additional locators, execution evidence deferred queue, environment integration, or
functional-testing planning.
```

## Supplemental Request Intake Table

| Request ID | Triggering File / Pass | Scope Type | Method(s) | Parent Function Candidate | Allowed Locators | Question | NAS Return Path |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Stage-Scoped Return Table

| Request ID | Parent Function Candidate | Methods Compared | Source-Visible Shared Pattern | Source-Visible Divergence | Decision Impact | Remaining Gap |
| --- | --- | --- | --- | --- | --- | --- |

## Method x Parent-Function Return Table

| Request ID | Method | Parent Function Candidate | Native Entry Point / Helper | Required Input / State Evidence | Output / Mutation Evidence | Bridge-Relevant Impact | Remaining Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Method-Scoped Return Table

| Request ID | Method | Evidence Area | Locator Read | Source-Visible Finding | Integration Impact | Remaining Gap |
| --- | --- | --- | --- | --- | --- | --- |

## Resolved / Unresolved Decision Impact Table

| Request ID | Decision Affected | Resolved? | Evidence Pointer | If Unresolved, Routed To | Next Action |
| --- | --- | --- | --- | --- | --- |

## Boundary

Supplemental reading is evidence input for integration. It is not runtime evidence, environment build output, functional evaluation, adapter design, wrapper design, rewrite approval, final support decision, or production-readiness evidence.

Unresolved runtime questions route back to the execution evidence deferred queue or to the relevant next step after Gate 2 downstream planning review. Filled supplemental-reading outputs belong in the NAS feature-level integration package, not in repo docs.

Audit-closed environment and validation locator gaps should not be reopened as open-ended supplemental reading. Runtime, download, install, import, and author-case execution questions stay deferred until a reviewed planning record routes them to the relevant next step.
