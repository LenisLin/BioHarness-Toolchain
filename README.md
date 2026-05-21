# BioHarness-Toolchain

BioHarness-Toolchain is the tools and infrastructure repository for a dependency-aware, contract-based, auditable bioinformatics execution harness within the broader BioHarness framework.

The first vertical is spatial transcriptomics downstream analysis. The current substrate phase organizes tool selection, dependency planning, execution-surface mapping, backend binding, validation, and provenance into a staged four-layer toolchain.

## Status

Blueprint and planning stage. The repository contains documentation, JSON schemas, illustrative examples, tests, and the repo-authoritative Layer 1/2 spatial transcriptomics `knowledge_registry/`.

Current Layer 3/4 planning is organized around strict parent functions, environment planning, Layer 4 support, bounded evaluation, downstream planning records, and Gate 2 human review tables. The active planning case is `spatial_domain_identification`.

## Engineering Implementation vs Formal Harness Presentation

Current pre-repository-reading, Gate 1, Gate 2, post-Gate2 build/execution, and Gate 3 workflows are engineering implementation and review workflows. They produce planning records, review tables, build outputs, environment records, and validation/provenance evidence.

These workflows are not the final user-facing or agent-facing harness presentation. Formal harness presentation is later than the current engineering implementation/review workflows. In future formal use, the system resolves and binds the selected Layer 2 method, selected Layer 3 execution surface, and reviewed environment binding before execution.

`harness_environment.yaml`, `environment_build.yaml`, `environment_build.jsonl`, and `runtime_environment_selection.tsv` are engineering records, reproducibility records, or selection-index inputs. They are not the final harness UI, prompt contract, or an entry point for an agent to freely infer execution environment from YAML, JSONL, or TSV files.

## Documentation

Start with [docs/README.md](docs/README.md) for the current Documentation Map, reading order, and directory roles.

## Packaging Hygiene

Manual review exports should exclude generated/cache files such as `.git/`, `.pytest_cache/`, `__pycache__/`, and `*.pyc`. Recommended export:

```bash
git archive --format=zip --output BioHarness-Toolchain-ST-docs.zip HEAD
```

## Documentation Map

- [Documentation Map](docs/README.md)
- [Layer 1/2 knowledge registry](knowledge_registry/README.md)
