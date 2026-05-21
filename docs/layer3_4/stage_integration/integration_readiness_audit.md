# Integration Readiness Audit

## Purpose

This file defines the feature-level audit that checks whether first-round method-specific repository-reading packages are sufficient to enter stage integration.

The audit reviews repository-reading package completeness for integration use. It does not reread method repositories, design parent functions, decide Layer4 support, install packages, run methods, or claim runtime readiness.

## Inputs

- Method package roots for all methods included in the feature-level integration pass.
- Repository localization outputs and local source-root provenance.
- `05_code_reading_plan.md`
- `06_code_function_family_evidence.md`
- `04_environment_config.md`
- `07_output_validation.md`
- `08_package_review.md`

## Audit Workflow

1. Package intake: confirm package roots, method IDs, version/source boundaries, NAS evidence pointers, and required reader outputs.
2. Stage evidence readiness: check whether code-reading plans and function-family evidence can support parent-function extraction without inference.
3. Method environment readiness: check whether dependency sources, author-stated constraints, and core/optional boundary evidence are closed enough for later environment integration triage.
4. Method validation readiness: check whether author case files, small-case code locators, case data locators, author result locators/forms, expected outputs, and runtime/download deferred needs are visible enough for later functional-testing planning.
5. Gap routing: classify each gap by the downstream action it requires.
6. Audit-closing remediation: route reading defects, supplemental-reading needs, and current-pass template defects to repair, reread, or explicit deferral before downstream integration.
7. Re-check affected readiness cells after remediation outputs are available.
8. Supplemental reading queue: create targeted source-reading requests for integration-relevant evidence questions.
9. Execution evidence deferred queue: isolate questions that require installation, execution, import/load checks, resource observation, download checks, or author-case runs.
10. Template update queue: record reusable package-template defects separately from method evidence gaps unless the template defect blocks current-pass evidence interpretation.

## Package Intake Table

| Method | Package Root | Source / Version Boundary | Required Outputs Present? | NAS Evidence Pointer | Intake Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |

## Stage Design Readiness Table

| Method | Candidate Stage Evidence Present | Native Entry Points Visible | Inputs / State Visible | Outputs / Mutations Visible | Decision-Relevant Gaps | Readiness Category |
| --- | --- | --- | --- | --- | --- | --- |

## Method Environment Readiness Table

| Method | Dependency Sources Located | Author-Stated Constraints Visible | Core / Optional Boundary Evidence | Known Text Conflicts | Environment Reread Needed? | Deferred Execution Evidence Need | Readiness Category |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Method Validation Readiness Table

| Method | Author Case Files Located | Small-Case Code Locator Status | Case Data Locator Status | Author Result Locator / Form Status | Expected Output Visible | Locator Reread Needed? | Runtime / Download Deferred Need | Readiness Category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Gap Routing Table

| Gap ID | Method | Evidence Area | Gap Description | Integration Impact | Routing Category | Target Queue / File |
| --- | --- | --- | --- | --- | --- | --- |

## Supplemental Reading Queue

| Request ID | Method | Scope Type | Candidate Stage, If Any | Exact Locator(s) To Read | Question To Answer | Expected Return |
| --- | --- | --- | --- | --- | --- | --- |

## Execution Evidence Deferred Queue

| Deferred ID | Method | Question | Why Static Evidence Is Insufficient | Execution Evidence Surface | Gate 2 Review Needed Before Evidence? |
| --- | --- | --- | --- | --- | --- |

## Template Update Queue

| Template Issue ID | Affected Reader / Template | Defect Or Missing Field | Why It Matters For Integration | Proposed Template Update | Evidence Package Affected |
| --- | --- | --- | --- | --- | --- |

## Audit-Closing Remediation Table

| Remediation ID | Method | Evidence Area | Trigger Category | Required Remediation | Remediation Output Pointer | Re-Check Result | Downstream Eligibility |
| --- | --- | --- | --- | --- | --- | --- | --- |

Allowed downstream eligibility values:

- `eligible_for_downstream_integration`
- `eligible_with_execution_evidence_deferred`
- `not_eligible_until_repaired`
- `deferred_for_this_pass`
- `not_applicable`

## Readiness Categories

`Readiness Category` is assigned per evidence area, not per method. The same method may have different categories in Stage Design, Environment, and Validation readiness tables.

`Readiness Category` and `Downstream Eligibility` are separate fields.

`Readiness Category` records the primary evidence problem in one readiness cell before or during remediation. `Downstream Eligibility` records whether that evidence area may enter downstream integration after required remediation, re-check, or explicit deferral.

Do not write downstream eligibility values into `Readiness Category`.

- `acceptable_for_integration`: current evidence is sufficient for the next planning step in this evidence area, with documented limitations. This does not imply runtime support, completeness, or production readiness.
- `supplemental_reading_needed`: a targeted static rereading task may change an integration decision.
- `reading_defect`: a required first-round package section is missing, internally inconsistent, or not traceable to source locators.
- `template_update_needed`: a reusable reader or template defect affects current evidence capture or interpretation.
- `execution_evidence_needed_after_gate2`: the question requires installation, import/load checking, method execution, runtime observation, download verification, or author-case reproduction.
- `not_applicable`: the method or evidence area is not applicable to the current pass.

## Readiness Category Action Rules

| Category | Required Action Before Downstream Use |
| --- | --- |
| `reading_defect` | Repair or rerun the affected package evidence before downstream integration. |
| `supplemental_reading_needed` | Complete audit-closing supplemental reading, then re-check the affected readiness cell. |
| `template_update_needed` | If current evidence is affected, update the template and rerun or supplement the affected reader. If only future templates are affected, record it in Template Update Queue without blocking. |
| `execution_evidence_needed_after_gate2` | Route to Execution Evidence Deferred Queue. After the deferred item is recorded, set downstream eligibility to `eligible_with_execution_evidence_deferred` if static planning can continue with explicit non-claims; otherwise use `deferred_for_this_pass`. |
| `acceptable_for_integration` | Evidence may enter the next planning step for this evidence area. |
| `not_applicable` | No action for this pass; record rationale. |

Priority for the primary category within one readiness cell:

```text
reading_defect
  > supplemental_reading_needed
  > execution_evidence_needed_after_gate2
  > template_update_needed
  > acceptable_for_integration
  > not_applicable
```

Multiple gaps must still be listed separately in the Gap Routing Table. The primary category is not a substitute for gap-level routing.

## Environment Readiness Rules

- If dependency locators are `unclear` or a key configuration source is missing from the evidence package, route the issue to `supplemental_reading_needed` or `reading_defect` before environment integration proceeds.
- If an author repository has no visible dependency documentation or manifests, record source-visible absence. That absence may still allow text integration, but it is not installability evidence.
- After audit closure, do not start generalized environment repository rereads. Environment questions should become text integration issues or `execution_evidence_needed_after_gate2` items such as solves, installs, or import/load checks.

## Validation Readiness Rules

- If an author case asset locator is `unclear`, close the locator issue before audit closure through targeted supplemental reading or classify it as a reading defect.
- If an asset is `not_provided_by_author`, record it as source-visible absence. It is not a reading failure, but it affects case eligibility.
- If data use `external_link_recorded_verification_needed`, defer link availability and download checks to a reviewed functional testing planning record whose next step is author-case/native workflow execution and BioHarness bridge replay. Do not verify external links in reading or audit.
- After audit closure, do not reopen broad validation reading to find basic case assets. Validation questions should use the locator table or route to functional testing planning records for later Gate 2 downstream planning review.

## Audit Closure Rule

Only audit-closed evidence should enter downstream integration.

An evidence area is audit-closed when its `Downstream Eligibility` is one of:

- `eligible_for_downstream_integration`
- `eligible_with_execution_evidence_deferred`
- `not_applicable`

`eligible_with_execution_evidence_deferred` means static planning may continue with explicit non-claims, while runtime, environment build/check, download, import/load, or author-case evidence remains deferred.

Readiness categories such as `execution_evidence_needed_after_gate2` are not closure states by themselves. They must be routed through the Execution Evidence Deferred Queue and reflected in `Downstream Eligibility`.

Audit closure does not establish runtime support, production readiness, biological correctness, or Gate 2 review status.

## Boundary

The audit does not install packages, run methods, perform import/load checks, rerun repository reading, define final parent functions, or make Layer4 support decisions.

Static package evidence can justify routing and integration eligibility only. It is not evidence of runtime support, production readiness, biological correctness, or executable environment availability.

Filled audit outputs belong in the NAS feature-level integration package. Repo files in this directory remain reusable instructions and templates.
