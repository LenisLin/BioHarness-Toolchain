# Evaluation

## Purpose

This document defines how evaluation is organized across the BioHarness substrate.

In this context, evaluation includes both layered validation of substrate objects and harness-level assessment of system behavior. The object being evaluated changes by scale: routes, decision trees, handoffs, parent surfaces, backend bindings, runtime results, and harness-mediated workflows.

The goal is to make evaluation evidence proportional to the decision or claim it supports: routing decisions at Layer 1, method-selection decisions at Layer 2, execution-surface decisions at Layer 3, backend/adaptation decisions at Layer 4, runtime-result acceptance, and harness-level claims about burden, efficiency, completion, and reliability.

## Evaluation Flow

BioHarness evaluation follows the substrate development flow. Early stages evaluate knowledge and design artifacts: whether a request can be routed, whether method selection is supported, and whether a selected method can be represented through a stable execution surface. Later stages evaluate implementation-facing artifacts: whether a surface is bound to backend behavior, whether adaptation changes scientific behavior, whether a runtime result satisfies its contract, and whether the implemented harness improves execution reliability.

Each validation stage should identify the object being validated, the evidence used for validation, and the decision that the validation supports.

## Layer 1 Routing Validation

Layer 1 routing validation evaluates whether the task catalog can map a user request to the appropriate `Analysis Problem`.

Validation should use routing scenarios that cover clear single-endpoint requests, ambiguous scientific endpoints, multi-endpoint requests that require route splitting, and requests that name a method or package outside the formal registry.

The selected route should follow the user's scientific object and target output, open the Layer 2 file listed by the current task catalog, and record out-of-formal cases without silently expanding the formal candidate space.

## Layer 2 Method-Selection Validation

Layer 2 validation evaluates whether method selection within an `Analysis Problem` is supported by the completed working/evidence package. The decision tree is the central validation object.

Validation should use decision-tree scenarios that cover the main topic branches, representative branch-triggering user intents, branch-local tie-breaks, ambiguity cases, and cases where benchmark or review evidence is absent and logic review is used instead.

The branch choice should follow the topic's problem boundary, use fields present in the method feature table, keep the candidate set inside the selected Layer 2 topic, preserve branch-local caveats, and avoid turning local benchmark or review evidence into a universal all-method ranking.

Decision-tree validation should also check whether branch conditions are distinguishable enough for agent use. If two branches cannot be separated by the user's scientific object, target output, modality, data structure, or intended result, the topic needs additional review before it can support a stable handoff.

## Handoff Validation

Handoff validation evaluates whether information moves between substrate stages without losing the decision context needed by the next stage.

Layer 1 to Layer 2 handoff validation should preserve the scientific object, target output, route rationale, ambiguity state, out-of-formal status, and selected Layer 2 topic.

Layer 2 to Layer 3/4 handoff validation should preserve the selected analysis problem, Layer 2 route, decision-tree branch, candidate method or method family, selection caveats, hard constraints, and unresolved review items needed for execution-surface planning.

Handoff validation should use representative prompt, policy, template, or future-skill scenarios. The next stage should receive the context it needs without adding unsupported claims about executable support, environment availability, adapter availability, or production support.

## Layer 3 Execution-Surface Validation

Layer 3 validation evaluates whether a task-specific unified interface can represent the shared scientific action across selected methods in the same task family.

For example, multiple spatial domain identification backends may expose different package functions, parameter names, object assumptions, and output locations. Layer 3 validation checks whether these methods can be invoked through one stable parent surface with semantic inputs, bounded parameters, expected outputs, validation expectations, typed failure behavior, provenance expectations, and agent-visible control boundaries.

Validation should use interface scenarios that include representative backend methods and, where available, author-provided examples or tutorials that exercise the intended task behavior. Each scenario should be expressed through the Layer 3 parent surface; backend-specific function names, object conversions, and output extraction remain Layer 4 responsibilities.

The same parent surface should express the task intent across backend variation without exposing backend internals to the agent and without erasing scientifically meaningful differences between methods.

## Layer 4 Backend And Adaptation Validation

Layer 4 validation evaluates whether the hidden adapter, wrapper, or rewrite implementation correctly satisfies the Layer 3 parent surface for a specific backend.

Validation should use backend-binding and adaptation scenarios supported by repository evidence and, where feasible, the backend's author-provided examples or tutorials. These scenarios should check entrypoints, parameter mapping, input conversion, output extraction, artifact handling, environment binding, failure translation, and validation hooks.

Adapter and wrapper validation should show that the backend can be reached through the Layer 3 parent surface while preserving the backend's scientific behavior. Compatibility rewrite scenarios should compare the original upstream path and the BioHarness-compatible path on an appropriate fixture where feasible. Algorithmic rewrite scenarios require explicit review of the scientific-core behavior being changed and the validation evidence needed before implementation proceeds.

## Runtime Result Validation

Runtime result validation evaluates whether a concrete invocation of the selected Layer 3 parent surface satisfied its contract.

Validation should use fixture runs and observed runtime checks covering preflight input and parameter validation, environment-profile resolution, runtime state capture, post-run artifact and output-contract checks, typed failure handling, provenance capture, and validation-report emission.

Runtime completion is not sufficient by itself. A usable runtime result should produce inspectable outputs, artifacts, logs, validation outcomes, and provenance records. Visual sanity checks may detect obvious artifact failures, but they should be treated as sanity checks rather than evidence of biological correctness or algorithmic equivalence.

When runtime validation exposes backend-specific failures, Layer 4 evidence may be inspected for debugging or audit. That debug path does not make backend internals part of the ordinary agent-facing call surface.

## Harness-Level Evaluation

Harness-level evaluation assesses whether an implemented BioHarness substrate improves execution reliability, auditability, and coding-agent efficiency across workflows.

Evaluation should use controlled workflow scenarios that compare BioHarness-mediated execution against coding-agent workflows using the same or comparable tasks, inputs, and failure perturbations.

The main working hypotheses are:

1. `Environment and interface burden`: BioHarness reduces coding-agent time spent on environment identification, environment configuration, interface reconstruction, backend-specific parameter mapping, and execution repair.
2. `Context burden`: BioHarness reduces context consumed by compute setup, dependency reasoning, interface mapping, backend documentation reading, and backend debugging.
3. `Scientific reasoning budget`: BioHarness preserves more interaction budget for scientific reasoning by moving compute-interface burden into substrate artifacts. This can be measured by the share of turns, tokens, or time spent on scientific task framing, method choice, validation judgment, and result interpretation rather than environment or interface repair.
4. `Task efficiency`: BioHarness improves total task completion time and step-level processing time, especially at handoff, interface selection, execution setup, failure handling, and output validation steps.
5. `Task completion and runnable result quality`: BioHarness improves overall task completion rate, final runnable result quality, output-contract satisfaction, and validation-report completeness.
6. `Step-level accuracy`: BioHarness improves route choice, method-selection accuracy, execution-surface selection, failure interpretation, provenance handling, and output-contract handling.

The current planning comparator set should include GPT-5.4, GPT-5.5, GPT-5.3-Codex, GLM, DeepSeek-V4, and Claude Code 4.6/4.7 Opus/Sonnet. Benchmark records should capture the exact model version, agent interface, date, tool access, context window, execution environment, task set, and scoring rubric used for each comparison.

## Evaluation Method

Each evaluation scenario should identify the object being evaluated, the evidence used for evaluation, and the decision the evidence supports.

The validation method should match the artifact being evaluated. Knowledge-layer validation uses document and scenario review. Handoff validation uses prompt, policy, template, or skill trials. Layer 3 validation uses parent-surface interface scenarios. Layer 4 validation uses backend evidence, examples, tutorials, fixtures, and implementation checks. Runtime validation uses observed execution. Harness-level evaluation uses controlled workflow comparison.

When validation supports scientific-equivalence, runtime-support, or reliability claims, the comparison target and uncertainty should be stated explicitly.
