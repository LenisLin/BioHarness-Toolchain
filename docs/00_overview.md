# Overview

## Purpose

BioHarness-Toolchain is the tools and infrastructure repository for a domain-limited bioinformatics execution harness focused on spatial transcriptomics downstream analysis.

The core project direction is:

> A dependency-aware, contract-based, auditable bioinformatics execution harness for reliable spatial transcriptomics downstream analysis by LLM agents.

This project is not another tool-using biomedical agent. It is a domain-limited execution harness for spatial transcriptomics downstream analysis. Its goal is to compress the open-ended tool-selection, dependency-resolution, interface-mapping, and execution-validation problem into a curated set of typed, validated, auditable task adapters.

BioHarness-Toolchain converts open-ended spatial transcriptomics tool use into a staged substrate: Layer 1 routes an agent to the correct task family; Layer 2 selects methods using curated evidence and decision trees; Layer 3 exposes stable execution surfaces; Layer 4 binds those surfaces to dependency-isolated backend adapters, wrappers, or rewrites.

This repository separates tool knowledge from tool execution. Layer 1 and Layer 2 are knowledge layers used for task-family routing and method selection. Layer 3 defines stable execution surfaces that can be reasoned about without reading backend package internals. Layer 4 binds those surfaces to concrete backend adapters, wrappers, or rewrites. Layer 4 is not normally shown to the main LLM brain.

## Current Position

The repository currently contains blueprint material rather than a production runtime:

- documentation for Layer 1, Layer 2, Layer 3, and candidate Layer 4 concepts
- JSON schemas and illustrative examples for public contract objects
- a spatial domain identification Layer 2 pilot anchored in external NAS artifacts
- tests that preserve current documentation and schema expectations

The project should eventually focus on roughly 10-20 high-frequency spatial transcriptomics downstream task adapters. Those adapters are roadmap components unless backed by code or explicit execution manifests.

## Why Execution Harnesses Matter

Biomedical agents are moving beyond pure prompt engineering toward multi-tool systems and execution harnesses. Recent work such as [SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration](https://www.nature.com/articles/s43588-025-00849-y), [CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data](https://www.nature.com/articles/s41592-026-03029-6), [Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://pubmed.ncbi.nlm.nih.gov/41912700/), [Agentic AI and the rise of in silico team science in biomedical research](https://www.nature.com/articles/s41587-026-03035-1), and [Making large language models reliable data science programming copilots for biomedical research](https://www.nature.com/articles/s41551-025-01587-2) shows the growing interest in tool-aware biomedical agents and reliable biomedical data-science assistance.

BioHarness-Toolchain takes a narrower role. It treats reliable execution as the central substrate problem for one domain: spatial transcriptomics downstream analysis. Tool calling is not the same as reliable tool execution. A function schema can expose a capability to an agent, but it does not guarantee that dependencies are compatible, required object fields exist, output artifacts are valid, or downstream steps can consume the result.

## Documentation Entry Points

- [Scope](10_scope.md)
- [Layer 1 method registry and substrate transition](15_layer1_method_registry_and_substrate_transition.md)
- [Tool taxonomy and Layer 2 rules](20_tool_taxonomy.md)
- [Harness architecture](25_harness_architecture.md)
- [Environment strategy](30_env_strategy.md)
- [Agent runtime reference](35_agent_runtime_reference.md)
- [Interface contract](40_interface_contract.md)
- [Task adapters](45_task_adapters.md)
- [Rewrite policy](50_rewrite_policy.md)
- [Validation](60_validation.md)
- [Reliability evaluation](70_reliability_evaluation.md)
- [Layer 3 and Layer 4 design](80_layer3_layer4_design.md)
- [Layer 3/4 co-design](82_layer3_4_codesign.md)
- [Spatial domain Layer 3 entry example](85_spatial_domain_layer3_entry_example.md)
- [Roadmap](90_roadmap.md)

## Status Boundary

Do not read this repository as claiming that production adapters, environment capsules, validators, or benchmarks already exist. Current contract schemas, examples, surface manifests, skills, and eval scenarios are blueprint artifacts unless a future authority document or implementation says otherwise.
