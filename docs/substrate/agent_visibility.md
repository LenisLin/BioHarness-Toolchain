# Agent Visibility

## Purpose

This document defines the default visibility boundary for the BioHarness agent brain.

In this document, `agent brain` means the reasoning component of an LLM-based agent: the part of the system that receives context, selects actions, interprets structured feedback, and decides whether to continue, repair, or stop.

This document explains which substrate layers should enter the default brain context during task routing, method selection, execution-surface planning, failure handling, and implementation, debugging, or audit workflows.

The goal is to keep routine agent reasoning focused on task intent, method choice, execution surfaces, validation expectations, and structured outcomes without loading backend package internals into the default brain context.

## Status Boundary

This document is a substrate visibility-policy blueprint. It does not implement runtime routing, access control, sandbox isolation, trace redaction, or production debugging behavior.

Implementation-backed visibility behavior must come from runtime code, accepted implementation records, executable manifests, validation reports, or another current authority document.

## Default Visibility Model

BioHarness uses progressive context disclosure. The agent brain should receive the minimum substrate layer needed for the current decision.

| Layer | Default brain visibility | What the agent brain should use it for | What should remain outside default brain context |
| --- | --- | --- | --- |
| Layer 1 | Visible at task-routing time. | Identify the relevant analysis problem or task family. | Broad method-registry rows and implementation candidates. |
| Layer 2 | Visible after Layer 1 routing. | Compare methods, assumptions, decision rules, and topic-specific evidence. | Callable signatures, backend adapters, environment bindings, and final runtime defaults. |
| Layer 3 | Visible after method selection and the documented handoff gate. | Plan execution through stable semantic inputs, bounded parameters, expected outputs, validation expectations, provenance expectations, and typed failure behavior. | Backend function names, backend file paths, package-private parameters, internal object keys, and implementation call graphs. |
| Layer 4 | Hidden from default brain context. | Used for implementation, debugging, audit, adapter development, or targeted failure investigation. | Routine scientific reasoning and default method-selection context. |

## Progressive Disclosure Path

The intended context path is staged:

1. The agent starts with Layer 1 task-family routing material.
2. After a task family is selected, the agent receives the relevant Layer 2 method-selection material.
3. After method selection and handoff review, the agent may receive the relevant Layer 3 execution surface.
4. During normal execution planning, the agent brain should reason over the Layer 3 surface rather than backend package internals.
5. After execution, the agent should receive structured success, failure, validation, and provenance summaries.
6. Layer 4 details should be exposed only when a limited implementation, debugging, audit, or failure-investigation workflow requires them.

This staged path is intended to reduce repeated reconstruction of execution context in the model conversation. It does not remove the need for scientific judgment, method review, implementation evidence, or runtime validation.

## Layer 4 Exposure Conditions

Layer 4 may be inspected when the current workflow requires one of the following:

- implementing or reviewing a backend adapter, wrapper, capsule, or rewrite
- debugging a failed execution after typed failure summaries are insufficient
- auditing provenance, backend evidence, parameter mappings, input conversion, output mapping, or failure translation
- resolving an implementation-readiness blocker before adapter work begins
- checking whether a backend-specific behavior invalidates a Layer 3 surface assumption

In those cases, Layer 4 enters the task-specific debug, implementation, or audit context. It does not become part of the default brain context.

Layer 4 exposure should be limited to the evidence needed for the current task. It should not become part of routine agent reasoning only because the backend repository is available.

## Agent-Visible Parameter Boundary

Agent-visible controls should be semantic, bounded, and scientifically meaningful.

Examples of agent-facing controls include input object selection, target task family, declared modality requirements, random-seed policy, output label alias, and coarse method parameters when the Layer 2 evidence and Layer 3 surface justify exposing them.

Backend function names, raw file paths, temporary filenames, package-private knobs, unsafe memory flags, backend optimization parameters, internal object keys, low-level output namespaces, directory layouts, and backend output prefixes should remain adapter-controlled or forbidden for routine agent control.

Optional backend paths that require unverified runtime dependencies should not become agent-selectable until the relevant environment evidence or runtime probe supports that exposure.

## Failure And Debug Visibility

The default brain context should receive typed success, failure, validation, and provenance summaries before raw backend traces.

A typed failure summary should give enough information for the agent brain to decide whether to inspect object fields, repair an input mapping, switch an environment profile, request human approval, or stop for manual review.

Raw backend traces, package logs, and Layer 4 binding details should be exposed only when the structured summary is insufficient for the current debugging or audit task.

## Technical Position

Many scientific-agent system designs place substantial emphasis on the agent: how it reasons, selects tools, writes or edits analysis code, executes notebooks, coordinates sub-agents, or repairs workflows.

BioHarness shifts the design emphasis to the execution substrate around the agent. The central object is not a more general scientific brain, but a staged and auditable tool substrate for one domain: spatial transcriptomics downstream analysis.

This shift changes the default visibility boundary. Instead of asking the agent brain to repeatedly read package documentation, infer object contracts, repair dependency assumptions, and inspect backend-specific code paths, BioHarness aims to move those details into curated layers, stable execution surfaces, backend adapter records, environment evidence, validation expectations, provenance records, and typed failure summaries.

The visibility model is therefore part of the project's technical position. It treats brain context exposure as an architectural decision: the agent brain should see enough information to make scientific and execution-planning decisions, while backend implementation detail remains available for implementation, debugging, and audit rather than becoming default reasoning context.

This is a blueprint claim, not a benchmark result. It does not establish that BioHarness improves task success, biological correctness, or production reliability. Those claims would require implementation-backed artifacts and reliability evaluation.
