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
artifact_state_policy:
phase_goal:
reference_documents:
execution_environment:
output_requirements:
subagent_plan:
completion_verifier:
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
- `artifact_state_policy` records the reviewed handling of prior artifacts for reruns.
- `phase_goal` states the task for this invocation only.
- `reference_documents` lists the repo documents and templates the new Codex window must read first.
- `reference_documents` should be phase-specific and minimal. Prefer the current phase workflow document, the filled reviewed planning artifact, the directly relevant output template or required-output section, storage/runtime rules when output paths are involved, and only the cross-phase support document needed for the current boundary.
- Do not include neighboring phase workflow documents by default. For example, an `environment_build_execution` prompt should not load `layer3_layer4_build.md`, `author_case_execution.md`, or validation workflow docs unless the filled planning record explicitly requires a boundary check from that phase.
- `execution_environment` records the complete reviewed environment invocation for this phase, including conda prefix, command-level environment variables when required, Python command form, R command form when used, and embedded backend preflight requirements when a selected execution surface crosses language runtimes.
- `output_requirements` should point to the current phase workflow document's positive completion definition or Definition of Done when one exists, output template requirements, and filled planning sections rather than duplicating phase policy text.
- For `layer3_layer4_build`, `output_requirements` should reference `layer3_layer4_build.md` and the `layer3_layer4_*` templates rather than restating workflow, verifier, publication, or output-schema rules.
- For `environment_build_execution`, output requirements must reference the filled planning record's package-manager/source-build policy, safe backend load targets, workflow/source-locator exclusions, repair-first sequence, clean branch retry conditions, and rewrite handoff rules when relevant.
- For `method_validation`, the prompt must reference `docs/layer3_4/method_validation/` and its local templates. The prompt must include a validation scope, stage-gated subagent plan, reviewed output root, reviewed environment evidence, consumed build evidence, first execution surface evidence for each included method, and reviewed artifact paths for stage handoffs when they already exist.
- For execution phases, `execution_environment` should use this template:

```yaml
execution_environment:
  conda_prefix:
  command_env:
    LD_LIBRARY_PATH: <conda_prefix>/lib
    LD_PRELOAD: <when required by reviewed native-library evidence>
  python_invocation: env LD_LIBRARY_PATH=<conda_prefix>/lib conda run -p <conda_prefix> python
  r_invocation: env LD_LIBRARY_PATH=<conda_prefix>/lib conda run -p <conda_prefix> Rscript
  method_runtime_boundary:
    required_package_family:
    language_bridge:
    native_library_policy:
    backend_smoke_path:
  embedded_r_preflight_required_methods:
    - <method_id>
  embedded_r_preflight_command:
```

The prompt records the complete invocation that enters the reviewed prefix. When environment build evidence records command-level environment variables or method runtime boundary requirements, the invocation prompt and method handoffs inherit that command form without simplification.

- For rerun workflows, `artifact_state_policy` must name stale artifact roots, the reviewed action for each root (`delete_before_rebuild`, `archive_then_rebuild`, `reuse_as_input`, or `do_not_touch`), and the new output root. Existing environment/build/implementation outputs are not downstream-consumable unless this policy explicitly selects them as current input evidence.
- For Layer3/Layer4 implementation package reruns, do not archive stale artifacts inside the active output package root. Prefer `delete_before_rebuild` or a fresh reviewed output root; if `archive_then_rebuild` is explicitly reviewed, the archive root must be outside the active package root.
- The prompt must not introduce public raw-file, locator, or backend-private input modes beyond the reviewed Gate1/Gate2 callable contract.
- For spatial image-aware methods, the prompt must reference the reviewed ST image alignment contract, including platform family, coordinate semantics, image source/key, and transform evidence when required.
- The prompt must not invent image locators, image-key defaults, scalefactor defaults, or patch-state rules absent from reviewed planning/build evidence.
- Any shorthand or relative path in `input_artifacts`, `output_requirements`, or `subagent_plan` must have a concrete base root defined in the filled planning artifact or in the prompt header. Prefer absolute paths when the path is an execution-critical artifact or source root.
- Invocation prompts must not be the only place where new semantic build constraints, source-root interpretations, or output-root policies are recorded. If execution requires a new constraint, record it first in the filled planning artifact or reviewed addendum/Gate review, then reference it from the prompt.
- `output_package_root` is a reviewed evidence path. If the active sandbox cannot write to it, the execution window should request permission or stop before implementation; it must not redirect outputs to repo-local, `/tmp`, or another unreviewed root.
- `subagent_plan` is defined for the current invocation. For `layer3_layer4_build`, multi-method invocations use one method-level subagent per build-required method and dispatch method subagents in batches of at most 6 active methods. The execution window follows `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md`: prepare method prompts, dispatch method-subagent batches, wait for method status for the current batch before opening the next batch, return repair requests to the affected method subagent or final collation step, rerun the affected checks after repair, run verifier handoff, and publish only after publishability checks and global verifier `PASS`.
- For `method_validation`, multi-method invocations follow `docs/layer3_4/method_validation/method_validation_workflow.md`. The main execution window dispatches method subagents by stage, in batches of at most 6 active methods, records dispatch evidence, runs the stage verifier, and advances only verifier-accepted methods to the next stage.
- `completion_verifier` is required for `layer3_layer4_build` and `method_validation` prompts. It records verifier prompt path, scope, and handoff evidence location. Phase-specific verifier rules come from the verifier template listed in the phase reference pack.
- For `layer3_layer4_build`, invocation prompts must not restate completion matrix fields, per-row YAML schema, verifier pass rules, publication gates, or `downstream_selectable` rules except by referencing `layer3_layer4_build.md` and the `layer3_layer4_*` templates. They may record instance facts such as denominator, held rows, source roots, output root, implementation namespace, and method-level work assignment.
- For `layer3_layer4_build`, invocation prompts should point to the reviewed action inventory source paths, including Gate 2 bridge planning and method prompt `native_or_rewrite_actions`, without restating, renaming, or overriding the build rules for reviewed action reconciliation.
- For `layer3_layer4_build`, `stop_condition` references the completion boundary defined by the `layer3_layer4_*` templates, including verifier pass, publication collation, and final publication artifacts. Other phases may use their phase-specific executable completion, next phase, or human gate boundary.
- `completion_report` lists the fields the new Codex window must report when the phase is complete. When the phase workflow document defines a Completion Report section, this field may point to that section.

If a required input artifact is missing, the new Codex window should stop and report the missing input rather than inferring an upstream gate, recreating a missing upstream review, or substituting an unreviewed artifact.

## Minimal Reference Document Packs

Use these as defaults, then add only filled planning artifacts required by the current invocation.

| Workflow Phase | Default Repo References |
| --- | --- |
| `environment_build_execution` | `docs/layer3_4/stage_integration/environment_build_execution.md`; `docs/layer3_4/stage_integration/environment_integration_planning.md`; `docs/layer3_4/stage_integration/environment_integration_planning_templates/environment_integration_planning_template.md` required-output and load-check sections; `docs/layer3_4/storage_and_runtime.md`; `docs/layer3_4/stage_integration/templates/acceptance_checklist.md` environment-build section only. |
| `layer3_layer4_build` | `docs/layer3_4/stage_integration/layer3_layer4_build.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_workflow.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_anti_surrogate_audit.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_method_config_template.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_outputs.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_build_audit_outputs.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_verifier_prompt.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_completion_report.md`; `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_acceptance_checklist.md`; `docs/layer3_4/storage_and_runtime.md`. |
| `author_case_native_workflow_and_bridge_replay` | `docs/layer3_4/stage_integration/author_case_execution.md`; reviewed validation-scope artifact; consumed environment/build evidence paths; `docs/layer3_4/storage_and_runtime.md`. |
| `method_validation` | `docs/layer3_4/method_validation/README.md`; `docs/layer3_4/method_validation/method_validation_workflow.md`; `docs/layer3_4/method_validation/validation_input_preparation.md`; `docs/layer3_4/method_validation/validation_reference_preparation.md`; `docs/layer3_4/method_validation/method_harness_validation.md`; `docs/layer3_4/method_validation/templates/validation_input_preparation_method_prompt.md`; `docs/layer3_4/method_validation/templates/validation_input_preparation_outputs.md`; `docs/layer3_4/method_validation/templates/validation_input_preparation_completion_verifier_prompt.md`; `docs/layer3_4/method_validation/templates/validation_reference_preparation_method_prompt.md`; `docs/layer3_4/method_validation/templates/validation_reference_preparation_outputs.md`; `docs/layer3_4/method_validation/templates/validation_reference_preparation_completion_verifier_prompt.md`; `docs/layer3_4/method_validation/templates/method_harness_validation_prompt.md`; `docs/layer3_4/method_validation/templates/method_harness_validation_outputs.md`; `docs/layer3_4/method_validation/templates/method_harness_validation_surface_config.yaml`; `docs/layer3_4/method_validation/templates/method_harness_validation_completion_verifier_prompt.md`; `docs/layer3_4/method_validation/templates/method_harness_validation_completion_report.md`; `docs/layer3_4/method_validation/templates/method_validation_acceptance_checklist.md`; reviewed validation-scope artifact; consumed build evidence; consumed environment evidence; `docs/layer3_4/storage_and_runtime.md`. |

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

Artifact state policy:
<artifact_state_policy>

Read these reference documents first:
<reference_documents>

Execution environment:
<execution_environment>

Output requirements:
<output_requirements>

Subagent plan:
<subagent_plan>

Completion verifier:
<verifier prompt path, scope, handoff evidence location>

Workflow boundary:
- Use the current phase workflow documents and output templates as authority.
- Keep this prompt as a thin dispatch record that references current phase authority, reviewed input artifacts, reviewed output roots, and reviewed boundary policies.
- Use the reviewed input artifacts as the phase input boundary. If a required input artifact is missing, stop and report the missing input.
- Keep repo instruction/template files separate from filled NAS records.
- If the phase uses a reviewed flexible-resolution or branch policy, follow that policy exactly.
- Record branch rules, overwrite rules, dependency rules, output-state rules, and rewrite authority in the filled planning artifact or reviewed addendum before invoking execution.
- Record instance-specific policy changes in the filled planning artifact or reviewed addendum before invoking execution.
- For `layer3_layer4_build`, execute the referenced `layer3_layer4_*` workflow and templates as the phase authority.
- Use `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md` for each build-required method assignment.
- Point method handoffs to the reviewed action inventory source from Gate 2 bridge planning and method prompt `native_or_rewrite_actions`; do not restate, rename, summarize, or override the reviewed action reconciliation rules in this invocation prompt.
- Keep method implementation inside method subagent assignments; the main implementation window handles dispatch, repair routing, method verifier handoff, draft publication package collation, global verifier handoff on the draft publication package, and publication.
- For `layer3_layer4_build`, dispatch method subagents in batches of at most 6 active methods. Do not treat a `FAIL_WITH_REPAIRS` method return as batch closure. If any method in the current batch returns `FAIL_WITH_REPAIRS`, consume it through the repair loop and wait for repaired `PASS` or an allowed stop condition before dispatching the next batch.
- Treat verifier or method `FAIL_WITH_REPAIRS` as an internal repair-loop signal, not as a terminal method state, terminal package status, fallback package status, completion-report state, or downstream-selection basis. Return the first repair target to the affected method subagent or final collation step, require the affected implementation/evidence path to be repaired and rechecked, and continue the loop until `PASS` or an allowed stop condition is reached.
- Do not emit a final completion report, final publication matrix, or downstream-selectable rows from a `FAIL_WITH_REPAIRS` result. A repair-required record may be kept only as transient builder evidence or external-interruption evidence.
- Publish registry, matrix, per-row records, and report only after method evidence, Layer3-M config production, callable config projection and consumption evidence, anti-surrogate-checked action-path closure, strict-output contract closure, post-synthesis audit-status confirmation, final evidence collation into the draft publication package, draft package publishability checks, and global verifier pass on the draft publication package.
- Record only invocation-specific facts in this prompt: denominator, held rows, source roots, output root, implementation namespace, method assignments, and required input artifacts.
- For `method_validation`, use the templates under `docs/layer3_4/method_validation/templates/`.
- Route input and reference preparation gaps to repair states before method harness validation.
- Write terminal package results only from verifier-accepted method harness validation results.
- For environment builds, use reviewed safe backend load targets from the filled planning record.
- For environment build failures, follow the reviewed repair-first sequence before writing held-out evidence.
- Resolve shorthand paths through base roots recorded in filled planning artifacts or this prompt header.
- Run execution commands through the complete reviewed invocation recorded in `execution_environment`, including command-level environment variables required by environment build evidence.
- If the reviewed output package root is not writable under the active sandbox, request the needed permission or stop and report the permission issue.
- Stop at <stop_condition>.

Completion report:
<completion_report>
```

For full `method_validation`, the completion report should follow `docs/layer3_4/method_validation/templates/method_harness_validation_completion_report.md`. For a single-stage method-validation invocation, the completion report should reference that stage's local output and verifier templates.

## Self-Check Before Sending The Prompt

### General Prompt Self-Check

- Is the workflow phase explicit?
- Are the required input artifacts concrete paths?
- Do the reference documents match the current phase?
- Does `reference_documents` avoid loading adjacent phase workflow docs unless the current filled planning artifact explicitly needs them?
- Are the output requirements concrete enough for the new Codex window?
- Do the output requirements point to phase docs or filled planning sections instead of duplicating policy?
- Does `output_requirements` point to exact sections instead of duplicating whole policy text?
- When a phase workflow document has a positive completion definition or Definition of Done, do the output requirements point to it?
- Does the prompt avoid public raw-file, locator, or backend-private input modes beyond the reviewed Gate1/Gate2 callable contract?
- Are all shorthand or relative artifact/source paths grounded by a concrete base root?
- Does the prompt avoid being the only source for a new semantic build constraint or output-root policy?
- Does the prompt preserve reviewed output roots rather than authorizing unreviewed redirection?
- Is the stop condition explicit?
- Does the prompt avoid generating a human gate decision?
- Does the prompt avoid treating repo instruction or template files as filled NAS records?
- Does the prompt remain thin, without new branch rules, overwrite rules, dependency rules, or rewrite authority?

### Environment Build Self-Check

- For `environment_build_execution`, does the prompt point to reviewed safe backend load targets rather than introducing new import targets?
- For environment build failures, does the prompt reference reviewed repair, clean branch retry, and rewrite handoff policy before held-out evidence?

### Layer3/Layer4 Build Self-Check

- Does it reference `layer3_layer4_build.md` and the relevant `layer3_layer4_*` templates?
- Does it reference the anti-surrogate audit template?
- Does it reference the completion verifier template?
- Does it assign one method subagent per build-required method?
- Does each method handoff use `layer3_layer4_method_subagent_prompt.md`?
- Does it cap method-subagent dispatch batches at 6 active methods?
- Does it inherit the complete reviewed invocation from environment build evidence into method handoffs?
- Does it require every method in the current batch to reach final or repaired `PASS`, or an allowed stop condition, before dispatching the next batch?
- Does it require verifier and method repair findings to return to the affected method subagent or final collation step, rerun the affected implementation/evidence checks, and continue until repaired `PASS` or an allowed stop condition?
- Does it forbid `FAIL_WITH_REPAIRS` as a terminal output package, fallback package status, completion report state, final matrix state, or downstream-selection basis?
- Does it keep main-window work to dispatch, repair routing, verifier handoff, collation, and publication?
- Does it require method subagents to generate `layer3_method_config.yaml`?
- Does it require method subagents to generate per-surface callable config projections, not only descriptive Layer3-M variable schemas?
- Does it require config consumption evidence checked against Layer4 callable/parser accepted keys?
- Does it prohibit method-validation or Stage3 runtime-result claims as Layer3/Layer4 build evidence?
- Does it require final matrix independent audit statuses to come from main-window or verifier post-synthesis confirmation?
- Does it point to the reviewed action inventory source for method handoffs without restating or overriding reviewed action reconciliation rules?
- Does it avoid renaming or summarizing reviewed actions in the invocation prompt as a substitute for method-subagent reconciliation?
- Does it avoid authorizing mock/fake backends, placeholder state, or contract-only surrogate output as build success?
- For long-running Layer3/4 build routes, does the method handoff require runtime observation evidence rather than treating elapsed time alone as failure?
- Does it avoid creating a separate Layer3-M workflow/prompt/verifier?
- Does the stop condition reference the template-defined completion boundary?
- Does it record only invocation-specific facts and avoid restating phase policy?

### Method Validation Self-Check

- Does the prompt include a validation-scope table?
- Does each included method have validation input preparation evidence, reference preparation evidence, and a method harness validation handoff or reviewed artifact path?
- Does canonical validation input exist before method harness validation starts?
- Is verifier-accepted `REFERENCE_READY` evidence available before method harness validation?
- Does method harness validation consume reviewed environment evidence and downstream-selectable Layer3/4 build rows?
- Does the prompt include Layer3-M config evidence for each Stage3 method handoff?
- Does the prompt require Stage3 to generate `method_harness_validation_surface_config.yaml` before harness subagent dispatch?
- Does the prompt include the reviewed execution environment and command invocation?
- For R-backed Python surfaces, does the prompt require embedded-R preflight and a backend smoke path under the reviewed Python import order?
- Does the prompt record method runtime boundary fields when the selected route uses language bridges, GPU stacks, or native libraries?
- Does the completion report request harness validation status, failure class, reason, failure stage, runtime monitoring summary, output-contract observation, consistency review, provenance observation, and files written?
- For long-running execution surfaces, does the method handoff include runtime monitoring and reviewed stop conditions?
- Does each method subagent prompt use `docs/layer3_4/method_validation/templates/method_harness_validation_prompt.md`?
- Does the subagent plan include dispatch evidence and verifier handoff?
- Does the stop condition route input and reference preparation gaps to repair states before terminal method results?
- Does each input-preparation handoff include `prepare_spatial_domain_input` build evidence, public contract, and strict output?
- Does input preparation record source-route completion before Stage 2 consumes the evidence?
- Does the subagent plan dispatch input preparation, reference preparation, and harness validation as separate stages?
- Does each stage cap active method subagents at 6?
- Does each stage run its verifier before the next stage consumes the evidence?
- Do only methods accepted as `INPUT_READY` enter reference preparation?
- Do only methods accepted as `INPUT_READY` and `REFERENCE_READY` enter harness validation?
