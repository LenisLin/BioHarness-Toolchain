# Reading Plan Risk Review

## Purpose

The Reading Plan Risk Review is a review-agent prompt for checking whether Source/Census output is ready for downstream repository readers.

It reviews file-category coverage, downstream reader ownership, context-size handling, metadata-only boundaries, and repository-reading conventions. It does not assign reading-depth categories, request runtime evidence, perform Method Integrator work, or create key-question mapping.

The review should preserve Layer 3/4 documentation boundaries: blueprint, planning, implementation, and production-readiness claims must remain distinct; schema examples, pilot notes, and reader templates must not be described as implemented runtime capability.

## Review Agent Prompt

```text
You are reviewing a Source/Census reading plan before downstream repository readers are dispatched.

Objective:
- Check whether repository file categories are covered.
- Check whether each file category has a clear downstream reader owner.
- Check whether large, generated, binary, data, model, and notebook-output files are marked for metadata-only reading or exclusion.
- Check whether docs, tutorials, examples, config files, source modules, output/plot modules, tests, and CI/container files are routed to the expected reader types.
- Check whether the plan respects the repository-reading workflow and Layer 3/4 documentation boundaries.

Review boundaries:
- Review the reading plan only.
- Do not perform method selection.
- Do not review writing style.
- Do not perform broad scientific audit.
- Do not request runtime evidence.
- Do not create key-question mapping.
- Do not create a Method Integrator output.

Inputs:
- task inputs:
- Source/Census Reader output:
- workflow reference:
- source census template reference:

Work:
1. Fill the Reading Plan Review Table.
2. Write Corrections To Insert Into Reading Plan.
3. Write Review Notes.

Return the YAML envelope, completed table, and Markdown notes.
```

## Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Reading Plan Risk Reviewer
  review_scope: reading_plan_only
  review_result: ready_for_reader_dispatch | revise_reading_plan | source_census_incomplete
  return_format: review_table_plus_markdown_corrections
```

## Reading Plan Review Table

| Check Area | What To Review | Source/Census Evidence | Issue Found | Required Plan Adjustment | Severity |
| --- | --- | --- | --- | --- | --- |
| file category coverage | docs, examples, notebooks, tests, manifests, source modules, output/plot modules, data/binary/generated, CI/container |  |  |  | low/medium/high |
| downstream reader ownership | every readable category has an assigned reader |  |  |  |  |
| context-size handling | large notebooks, generated outputs, large data/model files use metadata-only or exclusion |  |  |  |  |
| docs/tutorial handling | multiple tutorials/examples can be separately located for Docs/Workflow reading |  |  |  |  |
| environment config handling | config/install/CI/container files are assigned to Environment Reader |  |  |  |  |
| code reading assignment | source modules are assigned to Code Reading Planner, not directly over-expanded |  |  |  |  |
| output/validation ownership | tests, examples, output/plot/export modules are visible to Output/Validation Reader |  |  |  |  |
| repository localization | local source root, provenance, and cleanup status are present before downstream readers |  |  |  |  |
| repository-reading boundary | plan does not require method selection, runtime execution, key-question mapping, or adapter design |  |  |  |  |
| NAS output pointer | filled reader outputs have a designated NAS output root or documented placeholder |  |  |  |  |

If the local source root is missing, treat it as a reading-plan issue. Do not send downstream readers to perform direct remote-repository reading except for recording external documentation or data locators that are outside the localized source snapshot.

## Corrections To Insert Into Reading Plan

- Correction:
  - Affected category or reader:
  - Reason:
  - Text or instruction to insert:

## Review Notes

### Dispatch Readiness

### Coverage Issues

### Ownership Issues

### Context-Size Issues

### Documentation Boundary Issues
