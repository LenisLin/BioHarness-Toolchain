# Overview

## Purpose

BioHarness-Toolchain is the tools and infrastructure repository for a domain-limited bioinformatics execution substrate. The first vertical is spatial transcriptomics downstream analysis.

The project is being shaped toward a dependency-aware, contract-based, auditable execution harness for LLM-agent use. In the current repository, that direction is represented mainly by documentation, schemas, examples, planning records, and validation scaffolds rather than production task adapters.

The project does not aim to replace scientific reasoning by the agent. It aims to move routine execution context into curated project artifacts so that the agent can spend more of its limited context on scientific framing, method justification, and result interpretation.

## Problem Formation

Earlier biomedical-agent work, including tool-aware and multi-agent systems, provided examples of agents participating in complex computational-biology workflows. Much of that work centered on the agent itself: reasoning, tool use, collaboration among agents, and automated analysis behavior.

Recent coding-agent workflows make a complementary issue more visible. Agent performance can depend substantially on the system around the agent: tool exposure, execution sandboxes, dependency isolation, interface contracts, failure handling, and validation. For bioinformatics, this external substrate is not incidental. Package environments are difficult to reconstruct, analysis objects carry domain-specific assumptions, and many methods expose incompatible inputs, parameters, outputs, and runtime expectations.

In this setting, a large share of the model's context can be consumed by execution logistics: deciding which tool family is relevant, choosing among diverse methods, mapping data objects into package-specific interfaces, repairing dependency failures, and checking whether outputs are usable. BioHarness-Toolchain treats that burden as the core problem. The project aims to move routine execution context into curated layers, contracts, adapters, and validation scaffolds so that LLM agents can spend more of their limited context on scientific framing, method justification, and result interpretation.

This problem framing is informed by prior biomedical-agent and tool-aware data-science work, including [SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration](https://www.nature.com/articles/s43588-025-00849-y), [CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data](https://www.nature.com/articles/s41592-026-03029-6), [Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://pubmed.ncbi.nlm.nih.gov/41912700/), [Agentic AI and the rise of in silico team science in biomedical research](https://www.nature.com/articles/s41587-026-03035-1), and [Making large language models reliable data science programming copilots for biomedical research](https://www.nature.com/articles/s41551-025-01587-2). These references help motivate the execution-reliability problem addressed here; they do not establish the repository's current execution capability or freeze its internal architecture.

## Four-Layer Framing

BioHarness separates analysis-problem routing, method knowledge, execution surfaces, and backend implementation.

- Layer 1 helps route the analysis problem or task family.
- Layer 2 carries concrete method knowledge, comparison rules, and topic-specific decision trees.
- Layer 3 defines stable execution surfaces for agent-facing planning.
- Layer 4 binds those surfaces to backend adapters, wrappers, or rewrites.

Layer 1 and Layer 2 are knowledge layers. Layer 3 is the first machine-readable execution-planning layer. Layer 4 is the concrete implementation layer and should normally be hidden from the main agent unless implementation, debugging, or audit requires it.

## Current Position

The repository currently contains blueprint material:

- documentation for Layer 1, Layer 2, Layer 3, and candidate Layer 4 concepts
- JSON schemas and illustrative examples for public contract objects
- a spatial domain identification Layer 2 pilot anchored in external NAS artifacts
- planning templates and examples for Layer 3/4 method review
- tests that preserve current schema and machine-readable artifact expectations

The intended execution scope is a curated set of high-frequency spatial transcriptomics downstream task adapters. Those adapters remain planning components until backed by code, executable manifests, or another implementation-backed authority.

See [Documentation Map](README.md) for the full reading path.

## Status Boundary

Current contract schemas, examples, surface manifests, skills, and eval scenarios are blueprint artifacts. They should not be read as production task adapters, validated runtime support, or frozen internal architecture unless a future authority document, executable artifact, or implementation record gives them implementation-backed status.
