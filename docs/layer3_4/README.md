# Layer 3/4 Planning Workspace

This directory contains the current Layer 3/4 planning workspace for promoted method work. It is the place where Layer 1/2 method-selection evidence is translated into execution-surface planning, backend binding decisions, environment planning, rewrite decisions, and bounded-equivalence validation plans.

## Reading Order

1. [Layer 3 and Layer 4 design](layer3_layer4_design.md)
2. [Layer 3/4 co-design](codesign.md)
3. [Method execution planning protocol](method_execution_planning_protocol.md)
4. [Spatial domain Layer 3 entry example](spatial_domain_entry_example.md)
5. [Templates](templates/)

## Current Scientific Goal

For the first Layer 3/4 scientific planning case, the goal is to build a traceable planning path for identifying spatially coherent tissue regions or structural domains, from method-repository evidence through Layer 3/4 execution-substrate design.

The current case is `spatial_domain_identification`. It uses the NAS 27-tool freeze as the candidate pool, a pure random sample of 8 methods, fixed seed `20260508`, and one `MethodExecutionPlanningRecord v0.7.1` per sampled method.

## Planning Sequence

The current planning sequence has six phases:

1. Repository / Documentation Evidence Reading
2. Environment Configuration Abstraction
3. Layer3 Execution Surface Unification
4. Layer4 Binding / Wrapper / Rewrite Decision
5. Bounded-Equivalence Validation Plan
6. 8-Method Planning Pilot Walkthrough

Phase 1 reads each method repository and author-facing documentation to extract execution-design evidence: repository URL, version or commit, license, install-file locations, README/tutorial/notebook locations, package structure, main entrypoints, input objects or files, spatial-coordinate conventions, histology-image requirements, multi-sample or batch support, output-label location, visualization or export paths, example datasets, algorithm-core boundary, and documentation evidence level.

Phase 2 turns install, dependency, runtime, and automation evidence into environment planning fields: Python or R versions, CUDA/GPU, torch or tensorflow, AnnData/Scanpy, numpy/scipy, R packages, system libraries, optional dependencies, conflict candidates, shared-capsule candidates, dedicated-capsule risk, and future minimal check targets.

Phase 3 defines a canonical `spatial_domain_identification` execution surface and maps methods to the same scientific action. It covers semantic inputs, semantic parameters, outputs, artifacts, failure and provenance policy, AnnData versus separated matrix/coordinate/image inputs, coordinate source modes, target domain count or resolution, image use, batch or multi-sample policy, clustering backend, agent-visible parameters, and adapter-fixed parameters.

Phase 4 binds each functional coverage point to concrete backend behavior or wrapper responsibility: `input_check`, `method_preprocessing`, `core_structure_building`, `model_fit_or_inference`, `output_assignment`, `artifact_export`, `final_validation`, and `visualization`. Each binding records `backend_bound`, `wrapper_added`, `not_applicable`, or `requires_followup`, and records whether the algorithm core is touched.

Phase 5 defines bounded-equivalence validation plans within stated fixture, seed, version, metric, and tolerance boundaries. Wrapper checks cover schema, label alignment, artifacts, and provenance. Rewrite checks compare original and BioHarness-compatible paths where feasible. Stochastic, deep, or clustering methods should account for label permutation, ARI/NMI/AMI, domain count, no empty domain, and spatial sanity. Visual plausibility is a sanity check.

Phase 6 walks the 8 sampled methods through the preceding planning flow. It checks method work packages, review gates, record-filling rules, allowed `requires_followup` states, implementation-readiness blockers, and the existing BANKSY/SpaGCN status boundaries.

## Current Pilot State

BANKSY v0.7.0 is accepted as a Layer3/4 template trial. The current BANKSY target root is `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/BANKSY/v0.7.0/`, and BANKSY source retrieval outputs remain under `/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/spatial_domain_identification/banksy/`.

The BANKSY v0.6.1 recovery package is a failed/stress-test example for the planning workflow. SpaGCN is the next intended co-design target after the v0.7.1 planning alignment.

The 8-method planning pilot preserves the current BANKSY and SpaGCN implementation-readiness status while testing whether the planning record, reading protocol, environment abstraction, execution-surface mapping, binding decision, and bounded-equivalence plan are coherent across a small method sample.
