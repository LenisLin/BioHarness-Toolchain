# BioHarness-Toolchain

BioHarness-Toolchain is the tools and infrastructure repository for a dependency-aware, contract-based, auditable bioinformatics execution harness within the broader BioHarness framework.

The first vertical is spatial transcriptomics downstream analysis. The project is not another generic biomedical agent, and it is not merely a prompt-engineering, documentation, or RAG project. It is a domain-limited execution substrate intended to sit between LLM agents and mature bioinformatics tools.

The goal is to compress open-ended tool selection, dependency resolution, interface mapping, execution validation, and provenance capture into a curated set of typed, validated, auditable task adapters. The current planning target is roughly 10-20 high-frequency spatial transcriptomics downstream adapters.

Tool calling is not the same as reliable tool execution. In bioinformatics, a function schema alone is insufficient because successful execution depends on software environments, object structure, data contracts, filesystem side effects, statistical assumptions, and downstream compatibility.

BioHarness-Toolchain converts open-ended spatial transcriptomics tool use into a staged substrate: Layer 1 routes an agent to the correct task family; Layer 2 selects methods using curated evidence and decision trees; Layer 3 exposes stable execution surfaces; Layer 4 binds those surfaces to dependency-isolated backend adapters, wrappers, or rewrites.

This repository separates tool knowledge from tool execution. Layer 1 and Layer 2 are knowledge layers used for task-family routing and method selection. Layer 3 defines stable execution surfaces that can be reasoned about without reading backend package internals. Layer 4 binds those surfaces to concrete backend adapters, wrappers, or rewrites. The default reasoning brain should normally stop at Layer 3.

## What This Repository Is

- A documentation and blueprint repository for a spatial transcriptomics execution harness.
- A place to define task ontologies, adapter contracts, environment profiles, validation hooks, provenance records, and reliability evaluation targets.
- A controlled execution substrate for LLM-facing workflows, not an upper-level reasoning or governance layer.
- A bridge to mature tools such as AnnData, Scanpy, Squidpy, SpatialData, PyTorch-based methods, R tools, and report-generation utilities.

## What This Repository Is Not

- It is not a replacement for Scanpy, Squidpy, AnnData, SpatialData, PyTorch, Nextflow, Snakemake, MCP, or mature spatial transcriptomics methods.
- It is not a general-purpose biomedical agent.
- It is not a benchmark-result claim about biological correctness.
- It does not yet implement production adapters, environment capsules, validators, or runtime dispatch.

## Status

Blueprint stage. The repository contains documentation, JSON schemas, illustrative examples, tests, and Layer 1 / Layer 2 spatial transcriptomics artifacts. Runtime implementation details remain roadmap items unless a specific file says otherwise.

Current Layer 3/4 method planning uses `MethodExecutionPlanningRecord v0.7.1`, a small patch over v0.7. BANKSY v0.7.0 is accepted as a template trial only; no method has runtime support in this repository.

## Packaging Hygiene

Manual review exports should exclude generated/cache files such as `.git/`, `.pytest_cache/`, `__pycache__/`, and `*.pyc`. Recommended export:

```bash
git archive --format=zip --output BioHarness-Toolchain-ST-docs.zip HEAD
```

## Documentation Map

- [Overview](docs/00_overview.md)
- [Scope](docs/10_scope.md)
- [Layer 1 method registry and substrate transition](docs/15_layer1_method_registry_and_substrate_transition.md)
- [Tool taxonomy and Layer 2 rules](docs/20_tool_taxonomy.md)
- [Harness architecture](docs/25_harness_architecture.md)
- [Environment strategy](docs/30_env_strategy.md)
- [Agent runtime reference](docs/35_agent_runtime_reference.md)
- [Interface contract](docs/40_interface_contract.md)
- [Task adapters](docs/45_task_adapters.md)
- [Rewrite policy](docs/50_rewrite_policy.md)
- [Validation](docs/60_validation.md)
- [Reliability evaluation](docs/70_reliability_evaluation.md)
- [Layer 3 and Layer 4 design](docs/80_layer3_layer4_design.md)
- [Layer 3/4 co-design](docs/82_layer3_4_codesign.md)
- [Layer 3/4 method execution planning protocol](docs/83_layer3_4_method_execution_planning_protocol.md)
- [Spatial domain Layer 3 entry example](docs/85_spatial_domain_layer3_entry_example.md)
- [Roadmap](docs/90_roadmap.md)
