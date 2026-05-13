# Substrate Documentation

This directory contains the current substrate-level blueprint and policy documents for the BioHarness spatial transcriptomics execution substrate.

These documents describe how the substrate is organized, what information should be visible to the agent brain, how execution environments are planned, how backend adaptation intensity is described, and how layered validation and harness-level evaluation are framed. They are navigation and design documents, not implementation-backed evidence of production runtime support.

## Recommended Reading Order

1. [Substrate Architecture](architecture.md): Four-layer substrate framing for routing, method knowledge, execution surfaces, and backend implementation.
2. [Agent Visibility](agent_visibility.md): Default visibility boundary for what the agent brain should receive during routing, method selection, execution planning, failure handling, debugging, and audit.
3. [Environment Strategy](environment_strategy.md): Environment profiles, capsule candidates, and runtime packaging direction for the compute substrate.
4. [Adaptation Policy](adaptation_policy.md): Decision language for core/basic packages, adapters, wrappers, compatibility rewrites, algorithmic rewrites, and exclusion from the active method base.
5. [Evaluation](evaluation.md): Merged framework for layered validation of substrate objects and harness-level evaluation of system behavior.

## Document Roles

| Document | Role |
| --- | --- |
| [Substrate Architecture](architecture.md) | Defines the current four-layer substrate model and separates knowledge layers, execution surfaces, and backend implementation concerns. |
| [Agent Visibility](agent_visibility.md) | Defines progressive context disclosure and the default boundary between agent-facing substrate context and hidden Layer 4 implementation detail. |
| [Environment Strategy](environment_strategy.md) | Describes the intended method-first environment assembly, profile/capsule structure, and Docker-delivered runtime packaging direction. |
| [Adaptation Policy](adaptation_policy.md) | Provides the policy vocabulary for deciding whether a package is a core/basic anchor, adapter target, wrapper target, rewrite candidate, or excluded method-base candidate. |
| [Evaluation](evaluation.md) | Organizes evidence for local substrate validation decisions and for higher-level claims about harness-mediated workflow behavior. |
