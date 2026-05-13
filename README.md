# BioHarness-Toolchain

BioHarness-Toolchain is the tools and infrastructure repository for a dependency-aware, contract-based, auditable bioinformatics execution harness within the broader BioHarness framework.

The first vertical is spatial transcriptomics downstream analysis. The current substrate phase organizes tool selection, dependency planning, execution-surface mapping, backend binding, validation, and provenance into a staged four-layer toolchain.

## Status

Blueprint and planning stage. The repository contains documentation, JSON schemas, illustrative examples, tests, and the repo-authoritative Layer 1/2 spatial transcriptomics `knowledge_registry/`.

Current Layer 3/4 method planning uses `MethodExecutionPlanningRecord v0.7.1`. The active planning case is `spatial_domain_identification`.

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
