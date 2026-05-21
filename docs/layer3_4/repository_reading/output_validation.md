# Output Validation Reader

## Purpose

The Output Validation Reader records output candidates, output locations, validation cues, author-provided examples, tests, tutorials, notebooks, repository-provided fixtures when present, plot/export artifacts, and runtime-observation needs.

Runtime-observation needs are future verification needs. They are not completed runtime evidence and do not establish runtime support, biological validation, or production readiness.

## Subagent Prompt

```text
You are the Output Validation Reader for a Layer 3/4 method repository-reading package.

Objective:
- Extract repository-visible evidence for output candidates and validation cues.
- Locate author case assets, including case/workflow entries, small-case code, data locators, author result locators, and expected outputs.
- Record where outputs appear and what future verification would be needed.

Required inputs:
- method_id:
- Source/Census artifact:
- Docs workflow artifact, if available:
- Code reading artifacts, if available:
- Assigned author-provided tests, examples, tutorials, notebooks, repository-provided fixtures if present, output docs, plot/export evidence, or output-related source files:
- NAS output path for filled method-specific evidence:

Work:
1. Read author-provided tests, examples, tutorials, notebooks, repository-provided fixtures if present, output docs, plot/export evidence, and output-related source files when assigned.
2. Fill the Author Case Asset Locator Table.
3. Record output candidates and where they appear.
4. Record validation cues, required author cases, upstream test data, runtime inputs, and runtime-observation needs.
5. Do not propose synthetic, minimal, or BioHarness-created fixtures as the current functional-testing route. If author-provided cases lack data, instructions, or expected outputs, record the blocker.
6. Separate static repository evidence from future runtime verification.

Boundaries:
- Do not define final Layer 3 return contracts.
- Do not treat plots, screenshots, examples, tests, or repository-provided fixtures as biological validation.
- Do not treat plots, screenshots, examples, tests, or repository-provided fixtures as production readiness.
- Do not claim runtime support from static evidence.
- Do not download data or external assets.
- Do not check URL availability.
- Do not run notebooks or scripts.
- Do not copy case code into repository docs or filled validation packages; record pointers to the localized source repository or external source URL instead.
- Record only static locators and future verification needs.
- Do not add filled method-specific evidence to repository docs; filled evidence belongs in the method-specific NAS package.

Return using the structure below.
```

## Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Output/Validation Reader
  inputs_used:
    source_census:
    docs_workflow:
    code_reading:
    assigned_output_evidence:
  return_format: output_evidence_plus_validation_cues
  runtime_observation_needs_are_future_verification: true
  nas_output_path:
```

## Output Evidence Table

| Output Item ID | Output Candidate | Evidence Locator | Where It Appears | Observed Shape / Content | Required Or Optional In Source | Related Tutorial / Code Area | Reader Observation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OUT_001 |  |  | docs / example / notebook / test / repository_fixture / source / artifact / unclear |  | required / optional / unclear |  |  |

## Author Case Asset Locator Table

| Case ID | Case / Workflow Locator | Small-Case Code Provided? | Small-Case Code Locator | Data Provided? | Data Locator / Link | Data Location Type | Download Verification State | Author Result Provided? | Author Result Locator | Result Form | Expected Output Or Check | Reader Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allowed values for `Small-Case Code Provided?`:

- `yes`
- `no`
- `unclear`

Allowed values for `Data Provided?`:

- `yes`
- `no`
- `unclear`

Allowed values for `Data Location Type`:

- `repo_bundled`
- `package_data`
- `external_link`
- `generated_by_workflow`
- `not_provided`
- `unclear`

Allowed values for `Download Verification State`:

- `not_checked_static_only`
- `repo_path_visible`
- `external_link_recorded_verification_needed`
- `author_claims_downloadable_verification_needed`
- `not_applicable`
- `unclear_requires_reread`

Allowed values for `Author Result Provided?`:

- `yes`
- `no`
- `unclear`

Allowed values for `Result Form`:

- `notebook_output`
- `figure`
- `table`
- `saved_artifact`
- `log`
- `text_description`
- `not_provided`
- `unclear`

Use `not_provided` only when source evidence indicates the author did not provide the asset. Use `unclear` when the reader cannot tell from the assigned evidence and a targeted reread may be needed. In downstream review or audit, source-visible absence may be summarized as `not_provided_by_author`.

## Validation Cue Table

| Validation Cue ID | Cue Type | Evidence Locator | What The Cue Checks | Required Author Case / Upstream Test Data / Runtime Input | Runtime Observation Needed | Reader Observation |
| --- | --- | --- | --- | --- | --- | --- |
| VAL_001 | unit_test / repository_fixture / example_output / notebook_output / expected_shape / expected_field / deterministic_seed / benchmark_note / visual_check / other / unclear |  |  |  | yes / no / unclear |  |

## Markdown Notes

### Output Summary

### Author Case Asset Locator Summary

### Validation Cue Summary

### Author-Case Eligibility And Runtime Observation Needs

### Output / Validation Gaps

## Reader Boundary

| Item | Output Validation Reader |
| --- | --- |
| Record output candidates | yes |
| Record where outputs appear | yes |
| Record author case asset locators | yes |
| Record validation cues | yes |
| Record author-case eligibility and runtime-observation needs | yes |
| Download data, check URLs, or run notebooks/scripts | no |
| Copy case code into repository docs or filled validation packages | no; record pointers only |
| Propose synthetic or minimal BioHarness fixtures for current functional testing | no |
| Define final Layer 3 return contract | no |
| Claim runtime support from static evidence | no |
| Establish biological correctness | no |
| Establish production readiness | no |
