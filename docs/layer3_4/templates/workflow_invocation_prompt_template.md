# Workflow Invocation Prompt Template

## Purpose

Use this template to prepare a new Codex-window prompt for one Layer3/4 engineering workflow phase and one `Analysis Problem`.

This template covers Layer3/4 engineering workflow invocation. It does not cover Layer1/2 topic construction, replace phase workflow documents, create human gate decisions, or establish runtime support, production readiness, final support status, formal harness presentation, algorithmic equivalence, or biological correctness.

The template organizes the current phase, reference documents, input artifacts, output requirements, subagent plan, stop condition, and completion report for the next Codex window. Invocation prompts are thin dispatch records; they should not restate phase execution policy or become policy authority.

## Invocation Header

```yaml
analysis_problem:
workflow_phase:
repo_root:
results_root:
current_artifact_root:
input_artifacts:
output_package_root:
phase_goal:
reference_documents:
output_requirements:
subagent_plan:
stop_condition:
completion_report:
```

## How To Fill This Template

- `analysis_problem` names the current analysis problem or feature container.
- `workflow_phase` should be a human-readable phase name from the current Layer3/4 workflow documents.
- `repo_root` points to the BioHarness-Toolchain repository.
- `results_root` points to the NAS results root.
- `current_artifact_root` points to the existing artifact directory used as the phase input boundary.
- `input_artifacts` lists concrete artifact paths required by the new Codex window.
- `output_package_root` identifies where this phase should write filled records, evidence packages, or reports.
- `phase_goal` states the task for this invocation only.
- `reference_documents` lists the repo documents and templates the new Codex window must read first.
- `output_requirements` should point to the current phase workflow document, output template requirements, and filled planning sections rather than duplicating phase policy text.
- `subagent_plan` is defined for the current invocation. It may be empty when subagents are unnecessary.
- `stop_condition` states the next phase boundary or human gate where the new Codex window must stop.
- `completion_report` lists the fields the new Codex window must report when the phase is complete. When the phase workflow document defines a Completion Report section, this field may point to that section.

If a required input artifact is missing, the new Codex window should stop and report the missing input rather than inferring an upstream gate, recreating a missing upstream review, or substituting an unreviewed artifact.

## Prompt Skeleton For New Codex Window

```text
You are Codex working in <repo_root>.

Current analysis_problem:
<analysis_problem>

Current workflow_phase:
<workflow_phase>

Phase goal:
<phase_goal>

Input artifacts:
<input_artifacts>

Current artifact root:
<current_artifact_root>

Output package root:
<output_package_root>

Read these reference documents first:
<reference_documents>

Output requirements:
<output_requirements>

Subagent plan:
<subagent_plan>

Workflow boundary:
- Use the current phase workflow documents and output templates as authority.
- Treat this prompt as a thin dispatch record, not execution-policy authority.
- Do not infer missing upstream gates or substitute missing required input artifacts.
- If required input artifacts are missing, stop and report the missing input.
- Keep repo instruction/template files separate from filled NAS records.
- If the phase uses a reviewed flexible-resolution or branch policy, follow that policy exactly; do not infer unreviewed dependency families, branch scopes, output paths, or rewrite authority.
- Do not introduce new branch rules, overwrite rules, dependency rules, output-state rules, or rewrite authority in this invocation prompt.
- Record instance-specific policy changes in the filled planning artifact or reviewed addendum before invoking execution.
- Stop at <stop_condition>.

Completion report:
<completion_report>
```

## Self-Check Before Sending The Prompt

- Is the workflow phase explicit?
- Are the required input artifacts concrete paths?
- Do the reference documents match the current phase?
- Are the output requirements concrete enough for the new Codex window?
- Do the output requirements point to phase docs or filled planning sections instead of duplicating policy?
- Is the stop condition explicit?
- Does the prompt avoid generating a human gate decision?
- Does the prompt avoid treating repo instruction or template files as filled NAS records?
- Does the prompt remain thin, without new branch rules, overwrite rules, dependency rules, or rewrite authority?
