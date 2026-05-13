# Adaptation Policy

## Purpose

This document defines how BioHarness decides the adaptation intensity required for a package or method candidate within the current analysis problem.

The purpose is not to maximize package coverage. The purpose is to construct a method base that can support execution-surface planning, environment assembly, validation, and provenance. A method package enters this base only when BioHarness can define a credible execution path around it.

The policy starts from the confirmed core/basic package anchors. Additional packages are then assessed for whether they should be connected through an adapter, wrapped with additional execution logic, migrated through a compatibility rewrite, rewritten at the algorithmic level, or excluded from the active Layer 1 method base.

This document defines the decision language. Method-specific decisions belong in the relevant Layer 3/4 planning record or topic artifact.

## Core / Basic Package Anchor

The adaptation ladder starts from the core/basic package anchors. These packages form the substrate backbone for the current BioHarness method base.

The current core/basic package anchors are:

- AnnData
- Scanpy
- Squidpy
- SpatialData
- Seurat
- SpatialExperiment
- PyTorch

BioHarness builds environments, execution surfaces, adapters, wrappers, and compatibility work around these packages. They are not ordinary backend candidates and should not be modified as part of method-level adaptation.

Limited compatibility patches may be considered only for documented interoperability issues, such as a known version-specific compatibility bug. These patches should be recorded separately from method-level adaptation decisions and should not become a general route for changing core/basic package behavior.

For non-core packages, the adaptation level should be assessed within the current analysis problem. A package may receive a lower adaptation intensity when it is central to the task, appears upstream in the Layer 2 decision tree, is reused across selected methods in the same task family, or provides a stable object or execution convention needed by the method base.

## Adaptation Intensity

BioHarness uses an adaptation ladder rather than a binary wrapper-or-rewrite decision. The ladder is applied within the current analysis problem and current task family.

The preferred order is:

1. `Core/basic package`: use as a substrate anchor; do not modify except for documented compatibility patches.
2. `Adapter`: modify only the interface between the BioHarness execution surface and a stable backend API, CLI, or callable entrypoint.
3. `Wrapper`: add the minimum execution logic needed to make a backend workflow stable, such as object conversion, orchestration, path handling, artifact export, logging, validation hooks, or typed failure handling.
4. `Compatibility rewrite`: rewrite non-core compatibility code when interface adaptation and wrapper logic cannot make the method work inside the current method base.
5. `Algorithmic rewrite`: modify or replace scientific-core logic only under explicit review, comparison, and validation requirements.
6. `Exclude`: remove the package from the active Layer 1 method base for the current analysis problem.

A stronger adaptation level should be chosen only when weaker levels cannot support the intended execution surface, environment strategy, validation requirements, or provenance requirements.

The boundary between `Adapter` and `Wrapper` is the amount of execution logic owned by BioHarness. An adapter mainly translates interfaces. A wrapper adds execution logic around the backend while preserving the backend scientific core.

## Interface Standardization

Interface standardization is expected during adaptation. It can include input conversion, parameter normalization, output mapping, artifact layout, logging, typed failure translation, provenance capture, filesystem policy, and environment binding.

These changes are substrate work. They are intended to make execution more stable and auditable without changing the scientific method. Agent-facing surfaces should expose semantic controls, while adapters and wrappers absorb backend-specific names, paths, object keys, output locations, and error details.

Interface standardization does not by itself justify algorithmic rewrite. When the main issue is interface control, unstable I/O, weak artifact handling, or package-specific failure behavior, BioHarness should prefer adapter or wrapper work before considering rewrite.

## Rewrite Boundary

`Compatibility rewrite` and `Algorithmic rewrite` are separate decisions.

A compatibility rewrite targets non-core compatibility problems: old APIs, brittle glue code, file layout assumptions, object conversion, artifact export, logging, visualization, optional helper paths, or dependency migration. Its goal is to make the original method usable inside the BioHarness method base without changing the scientific core.

An algorithmic rewrite touches scientific-output-determining logic, such as graph construction, model fitting, loss functions, inference behavior, clustering logic, post-processing algorithms, stochastic behavior, or GPU/CPU numerical paths.

A compatibility rewrite requires comparison against the original behavior before equivalence is claimed. An algorithmic rewrite requires explicit scope, comparison target, validation plan, and review before implementation. A convenient reimplementation is not automatically scientifically equivalent to the original method.

## Exclude

`Exclude` means removing a package from the active Layer 1 method base for the current analysis problem.

Exclusion is appropriate when a package does not fit the analysis problem, cannot be connected to a verifiable execution path, depends on unsupported or incompatible runtime assumptions, exposes an unstable interface that cannot be wrapped, or would require scientific-core rewriting that is not justified for the current method base.

An excluded package should have a recorded reason. Exclusion is a method-base design decision, not a general claim that the package is scientifically invalid.

## Decision Recording

This document defines the policy language for adaptation intensity. It does not assign final adaptation levels to individual methods.

Method-specific records should state the selected adaptation level, the reason weaker levels are insufficient when a stronger level is selected, the evidence used for the decision, whether the scientific core is touched, and what validation or review is required before implementation.

Layer 1 registry inclusion does not by itself imply substrate inclusion. A package can be known to the evidence base while still being excluded from the active method base for the current analysis problem.
