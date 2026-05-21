# Code Reading

## Purpose

This file defines two reusable repository-reading roles:

- Code Reading Planner
- Code Function-Family Reader

Code reading provides source-level evidence for later parent-function abstraction, wrapper design, Layer 4 support planning, validation planning, and implementation-readiness review.

Code reading may identify method-local stage-inform groups that help later same-feature stage integration. These groups are reading-focus aids and do not define parent functions.

It does not select methods, define final Layer 3 surfaces, choose Gate 1 planning routes, write adapter or wrapper designs, claim runtime behavior, or establish production readiness.

## Code Reading Planner

### Subagent Prompt

```text
You are the Code Reading Planner for a Layer 3/4 method repository-reading package.

Objective:
- Convert source census, reading-plan review, docs workflow, and environment evidence into a source-reading plan organized by function families.
- Assign source areas to Code Function-Family Readers for source-level evidence extraction.
- Identify method-local stage-inform code groups when useful for avoiding missed evidence in later same-feature parent-function / execution-surface alignment.

Required inputs:
- method_id:
- Source/Census artifact:
- Reading-plan risk review artifact:
- Docs workflow artifact, if available:
- Environment config artifact, if available:
- Analysis-problem lenses, if provided:
- NAS output path for filled method-specific evidence:

Work:
1. Read source-module assignments from Source/Census and the reading-plan risk review.
2. Use docs/workflow and environment evidence only to locate source areas, author-visible entrypoints, and apparent functional responsibilities.
3. Divide code by actual source responsibilities into function families. Do not force function families to match any reference lens or fixed row set.
4. Use analysis-problem lenses if provided, but treat them as reading focus aids rather than required table rows.
5. Identify code areas that need source-level reading, code areas that can be handled by metadata, and code areas that should remain out of scope for the package.
6. Identify method-local stage-inform code groups that may matter for later same-feature parent-function / execution-surface alignment.
7. Treat stage-inform groups as reading-focus aids only.
8. Do not force stage-inform groups to match a fixed parent-function vocabulary.
9. For each group, decide whether helper functions or local dependencies are critical to include in the current code-reading pass.
10. Use stage-inform groups only to guide function-family planning and code-reader assignment.
11. Assign function families and locators to Code Function-Family Readers.

Boundaries:
- Do not perform deep function reading.
- Do not choose a Layer 4 support path.
- Do not write wrapper or adapter design.
- Do not define final parent functions.
- Do not define final Layer 3 surfaces.
- Do not treat stage-inform groups as parent functions.
- Do not perform multi-method parent-function / execution-surface alignment in a single-method repository-reading package.
- Do not choose Layer 4 planning routes from stage-inform groups.
- Do not claim runtime behavior from source presence.
- Do not add filled method-specific evidence to repository docs; filled evidence belongs in the method-specific NAS package.

Return the structure below.
```

### Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Code Reading Planner
  source_locator:
  inputs_used:
    source_census:
    reading_plan_review:
    docs_workflow:
    environment_config:
    analysis_problem_lenses:
  return_format: flexible_code_reading_plan
  nas_output_path:
```

### Code Corpus Overview Table

| Code Area ID | Path / Evidence Locator | Apparent Functional Role | Size / Context Risk | Read Mode | Suggested Handling |
| --- | --- | --- | --- | --- | --- |
| CODE_AREA_001 |  |  | low/medium/high/unknown | targeted_symbol / targeted_call_path / selective_file / metadata_only |  |

### Stage-Inform Code Group Table

| Stage-Inform Group ID | Provisional Group Name | Why This Group Matters For Later Same-Feature Alignment | Primary Source Scope | Critical Dependency Handling | Suggested Code Reader | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- |
| SIG01 |  |  |  | include / defer / unclear, with reason | Code-A | Method-local reading focus only; not a parent function. |

### Function Family Plan Table

| Family ID | Function Family Name | Functional Responsibility | Candidate Files | Candidate Symbols If Observed | Evidence Needed For Later Design | Suggested Code Reader | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FF01 |  |  |  |  | input contract / output contract / parameter mapping / wrapper behavior / validation cue / failure handling / unclear | Code-A |  |

### Code Reader Assignment Table

| Code Reader ID | Owned Family IDs | Files / Locators To Read | Evidence Focus | Must Extract | Out Of Scope | Handoff Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Code-A |  |  |  | source behavior; inputs; outputs; controls; side effects; dependencies; failure/resource points | support decision; adapter design; parent-function finalization |  |

Handoff notes may reference Stage-Inform Group IDs. Referencing a SIG only indicates reading focus. Code Readers should still use the existing Function / Block, Interface Evidence, Parameter And Control, Integration Cue, and Side Effect/Failure/Resource tables. Code Readers must not define parent functions.

### Planner Gaps

| Gap ID | Missing Or Unclear Area | Evidence Searched | Impact On Code Reading | Suggested Follow-Up |
| --- | --- | --- | --- | --- |
| CODE_GAP_001 |  |  |  |  |

## Code Function-Family Reader

### Subagent Prompt

```text
You are a Code Function-Family Reader for a Layer 3/4 method repository-reading package.

Objective:
- Read only the files, locators, and function families assigned by the Code Reading Planner.
- Extract source-visible evidence for later parent-function abstraction, wrapper design, Layer 4 support planning, validation planning, and implementation-readiness review.

Required inputs:
- method_id:
- Code Reading Planner output:
- Assigned Code Reader ID:
- Owned Family IDs:
- Assigned files / locators:
- NAS output path for filled method-specific evidence:

Work:
1. Read only the assigned files, locators, and function families. Follow local dependencies only when they are necessary to understand the owned family, and record the reason.
2. Extract functional role, source-visible behavior, inputs, outputs or mutations, parameters and controls, calls and dependencies, object/file/artifact effects, side effects, failure/resource points, and follow-up needs.
3. Record wrapper-relevant and Layer 4 planning cues as evidence cues, without turning them into design decisions.
4. Separate source observation from future runtime-observation needs.

Boundaries:
- Do not define final parent functions.
- Do not choose a Layer 4 support path.
- Do not write wrapper or adapter design.
- Do not define final Layer 3 surfaces.
- Do not claim runtime behavior from static source reading.
- Do not add filled method-specific evidence to repository docs; filled evidence belongs in the method-specific NAS package.

Return the structure below.
```

### Return Structure

```yaml
reader_return:
  method_id:
  reader_role: Code Function-Family Reader
  assigned_code_reader_id:
  owned_family_ids:
  assigned_files_or_locators:
  return_format: function_family_tables_plus_markdown_notes
  follow_up_needs:
  nas_output_path:
```

### Function / Block Reading Table

| Family ID | File / Evidence Locator | Symbol / Code Block | Functional Role | Observed Source Behavior | Inputs Read | Outputs Produced Or Mutated | Key Controls | Calls Or Depends On | Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF01 |  |  |  |  |  |  |  |  |  |

### Interface Evidence Table

| Evidence ID | Family ID | File / Evidence Locator | Native Object / Field / Path | Direction | Shape / Type If Visible | Alignment Or Indexing Assumption If Visible | Parent-Function Relevance Cue | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IFACE_001 | FF01 |  |  | input / output / mutation / file / unclear |  |  |  |  |

### Parameter And Control Evidence Table

| Control ID | Family ID | File / Evidence Locator | Native Parameter Or Control | Default / Allowed Values If Visible | Controls Which Behavior | Required Or Optional If Visible | Later Design Relevance Cue | Boundary Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTRL_001 | FF01 |  |  |  |  | required / optional / unclear |  |  |

### Integration Cue Table

| Cue ID | Family ID | File / Evidence Locator | Cue Type | Source Observation | Why It Matters For Later Wrapper Or Layer 4 Planning | Follow-Up |
| --- | --- | --- | --- | --- | --- | --- |
| CUE_001 | FF01 |  | entrypoint / object_model / dependency / file_io / parameter_mapping / output_mapping / validation / failure_handling / resource / other / unclear |  |  |  |

### Side Effect, Failure, And Resource Table

| Item ID | Family ID | File / Evidence Locator | Item Type | Source Observation | Trigger Or Condition If Visible | Consequence For Planning | Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ITEM_001 | FF01 |  | side_effect / failure / resource / dependency / artifact / mutation / other / unclear |  |  |  |  |

### Markdown Notes

### Function Family Summary

### Source Behavior Summary

### Interface Evidence Summary

### Parameter And Control Summary

### Integration Cues

### Side Effects, Failure Points, And Resource Notes

### Follow-Up Needs

### Non-Claims

### Granularity Rules

- Prefer symbol-level reading when the assigned source area exposes clear functions, classes, methods, or command entrypoints.
- Use code-block reading when behavior is embedded in notebooks, scripts, or module-level execution.
- Use call-path reading when an author-visible entrypoint delegates across several small functions.
- Use selective-file reading for compact files where symbol isolation would hide important behavior.
- Use metadata-only handling for files that establish package structure, versioning, or packaging context but do not need source-behavior extraction.
- Record local dependency expansion only when it is needed to understand the owned family.
- Include a helper or dependency in the current code-reading pass when it determines standard input interpretation, major method-native state construction, main output or label assignment, scientific-output-affecting controls, mutation or file side effects relevant to standardization, or failure behavior needed for wrapper or error translation.
- Defer a helper or dependency when it only affects optional plot styling, display-only behavior, non-core diagnostic artifacts, optional artifact naming outside current scope, or packaging/license context outside source behavior.

### Planner And Function-Family Reader Boundary

| Item | Code Reading Planner | Code Function-Family Reader |
| --- | --- | --- |
| Define function families from repository structure | yes | no |
| Assign files to code readers | yes | no |
| Deep-read function behavior | no | yes |
| Record source-visible inputs, outputs, and object effects | no | yes |
| Extract parameter and control evidence | no | yes |
| Extract wrapper-relevant evidence cues | plan the focus | record evidence cues |
| Identify missing code areas | yes | within owned family |
| Choose Gate 1 planning-route outcome | no | no |
| Define parent-function contract | no | no |
| Write wrapper or adapter design | no | no |
