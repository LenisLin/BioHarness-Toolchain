# Reading Package Review

## Purpose

This file provides a reusable review prompt and empty templates for checking a completed or partially completed method repository-reading package.

The review checks filled reader outputs for coverage, omissions, conflicts, missing pointers, boundary issues, author-case eligibility needs, and runtime-observation needs.

This is a repository-reading quality check. It is not a Method Integrator, key-question mapping, parent-function design, wrapper design, Layer 4 support decision, runtime-support claim, or production-readiness assessment.

Review results belong in the method-specific NAS package. Repository docs keep only the reusable prompt and empty review templates.

## Subagent Prompt

```text
You are the Reading Package Review agent for a Layer 3/4 method repository-reading package.

Objective:
- Review a completed or partially completed method repository-reading package for coverage, omissions, conflicts, boundary issues, missing pointers, author-case eligibility needs, and runtime-observation needs.
- Produce a compact omission and follow-up review that belongs in the method-specific NAS package.

Required inputs:
- method_id:
- analysis_problem:
- NAS package root:
- Reader output pointers:
- Repository localization output:
- Source/Census output:
- Reading plan and risk review output:
- Docs workflow output:
- Environment config output:
- Code reading plan:
- Code function-family reader outputs:
- Output validation output:

Work:
1. Review whether expected reader outputs are present or clearly marked as absent.
2. Check whether each reader output has enough pointer detail for later planning work.
3. Check whether the repository localization pointer is present.
4. Check whether dependency evidence locators are complete enough for audit closure.
5. Check whether author case asset locators are complete enough for audit closure.
6. Check whether `unclear` evidence is distinguished from `not_provided_by_author`.
7. Check that download, install, runtime, import/load check, author-case execution, and case-code copying needs are deferred or represented as pointers rather than claimed assets.
8. Record omissions, unresolved items, conflicts, author-case eligibility needs, blocked or deferred author cases, and runtime-observation needs.
9. Record boundary issues where static evidence is being over-read as runtime support, production readiness, a support decision, or a final Layer 3/4 design.
10. Record NAS pointer notes for filled method-specific evidence.
11. Include explicit non-claims.

Boundaries:
- Do not perform Method Integrator work.
- Do not perform key-question mapping.
- Do not design parent functions.
- Do not design wrappers or adapters.
- Do not choose Layer 4 support decisions.
- Do not claim runtime support.
- Do not assess production readiness.
- Do not add filled method-specific evidence to repository docs.

Return using the structure below.
```

## Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Reading Package Reviewer
  analysis_problem:
  nas_package_root:
  reviewed_reader_outputs:
  return_format: package_review_tables_plus_markdown_notes
```

## Reader Output Coverage Table

| Reader Output | Artifact Pointer | Reviewed Inputs | Coverage Note | Missing Or Unclear Items |
| --- | --- | --- | --- | --- |
| Method reading brief |  | task inputs and source boundary |  |  |
| Repository localization |  | local source root, provenance, git cleanup, retained metadata |  |  |
| Source census |  | source inventory and reader assignment |  |  |
| Reading plan risk review |  | scope control and corrections |  |  |
| Docs workflow |  | documentation, tutorials, examples, notebooks |  |  |
| Environment config |  | manifests, install docs, dependencies, containers, CI |  |  |
| Code reading plan |  | function-family plan and reader assignment |  |  |
| Code function-family reader outputs |  | source-level behavior and integration cues |  |  |
| Output validation |  | output candidates, validation cues, author-case eligibility/runtime-observation needs |  |  |

## Omission And Follow-Up Review Table

| Review Item ID | Review Area | Evidence Reviewed | Omission Or Unresolved Item | Why It Matters For Later Planning | Suggested Follow-Up |
| --- | --- | --- | --- | --- | --- |
| REVIEW_001 | repository_localization / source / docs / environment / environment_locator / code / output / author_case / author_case_asset_locator / case_code_locator / case_code_pointer_only / case_data_locator / author_result_locator / repository_test / download_verification_deferred / runtime_observation / NAS_pointer / other |  |  |  |  |

## Boundary Review Table

| Boundary Item ID | Evidence Locator | Potential Boundary Issue | Correct Repository-Reading Interpretation | Suggested Correction |
| --- | --- | --- | --- | --- |
| BOUNDARY_001 |  | static evidence treated as runtime support / example treated as production readiness / code cue treated as support decision / backend field treated as Layer 3 surface / other |  |  |

## Markdown Notes

### Package Review Summary

### Omission Summary

### Conflict Summary

### Author Case And Runtime Observation Needs

### Boundary Corrections

### NAS Pointer Notes

### Non-Claims

- does not establish runtime support
- does not establish production readiness
- does not define final Layer 3 parent-function contracts
- does not choose final Layer 4 support decisions
- does not replace Layer 2 method-selection evidence
- does not perform Method Integrator or key-question mapping
