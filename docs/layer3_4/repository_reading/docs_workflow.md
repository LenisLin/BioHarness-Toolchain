# Docs Workflow Reader

## Purpose

The Docs Workflow Reader records author-visible workflows from README files, docs, tutorials, notebooks, vignettes, examples, and usage pages.

It builds a documentation workflow index for later repository reading. Multiple tutorials or examples must be recorded separately, with the primary function demonstrated by each item. Filled method-specific evidence belongs under the designated NAS output root; this repository document keeps only the generic workflow, template, and pointer structure.

This reader does not select methods, define a final Layer 3 surface, design Layer 4 adapters, or treat documentation examples as observed runtime behavior.

## Subagent Prompt

```text
You are the Docs Workflow Reader for a Layer 3/4 repository-reading package.

Objective:
- Read assigned README, docs, tutorials, notebooks, vignettes, examples, and usage pages.
- Build an author-visible workflow index.
- Record each tutorial or example as a separate item.
- Identify the primary purpose demonstrated by each tutorial or example.
- Record documented inputs, outputs, parameters, options, and usage caveats.
- Record visible case/example code, data, author-result, and output mentions as static locators for Output/Validation Reader follow-up.

Inputs:
- method_id:
- analysis_problem:
- source census pointer:
- docs/example candidate paths:
- NAS output root for filled reader outputs:
- reading mode:

Work:
1. Read assigned documentation and usage materials.
2. Fill the Docs / Tutorial Workflow Table.
3. Write Markdown notes using the notes template.

Return the YAML envelope, the completed table, and Markdown notes.
```

## Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Docs/Workflow Reader
  assigned_scope:
    - README
    - docs
    - tutorials
    - examples
    - notebooks_if_assigned
  return_format: one_table_plus_markdown_notes
```

## Docs / Tutorial Workflow Table

| Doc Item ID | Source Type | Path / Evidence Locator | Primary Tutorial Purpose | Workflow Segment Covered | Case / Example Code Mentioned | Data Mentioned | Author Result Mentioned | Output Mentioned | Parameter / Option Mentioned | Follow-Up Reader |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| README_QUICKSTART | README |  | quickstart / basic usage | install, load input, run method, view output |  |  |  |  |  | Docs/Workflow; Environment if install notes; Output/Validation if case assets are mentioned |
| EXAMPLE_001 | example |  | single tutorial/example purpose | input prep, execution, output |  |  |  |  |  | Output/Validation; Code Reading Planner |
| EXAMPLE_002 | example |  | single tutorial/example purpose | data grouping, execution, output |  |  |  |  |  | Output/Validation; Code Reading Planner |
| NOTEBOOK_001 | notebook |  | tutorial purpose | selected sections/cells |  |  |  |  |  | Docs/Workflow; Output/Validation |

Do not judge whether a documented case is runnable. This reader only records author-visible case entry points and forwards them to Output/Validation Reader.

## Markdown Notes

### Author-Recommended Workflow

### Tutorial / Example Functional Index

- `EXAMPLE_001`
  - Main function demonstrated:
  - Dataset or input pattern:
  - Output shown:
  - Lookup value for later readers:

### Documented Inputs

### Documented Outputs

### Documented Parameters Or Options

### Documentation Gaps
