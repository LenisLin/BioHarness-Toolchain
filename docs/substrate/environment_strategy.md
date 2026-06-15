# Environment Strategy

## Purpose

This document defines the environment strategy for the BioHarness compute substrate.

The purpose is to make scientific-tool execution depend on preassembled and reviewable runtime environments rather than on ad hoc package installation, version repair, or dependency inference by an agent during task execution. In the intended substrate, the agent or harness selects a bounded execution surface and an associated environment profile. The compute side receives that selection and runs it inside an environment that is expected to carry the required dependency stack, resource assumptions, artifact policy, logging behavior, and failure-reporting path.

This document describes the intended design direction. It does not replace method-specific engineering records, lockfiles, Dockerfiles, Install-Load evidence, fixture runs, or validation reports.

## Environment Strategy For Compute

The main contribution of the environment layer is to make compute execution more explicit and less dependent on conversation-time repair. For spatial transcriptomics methods, a callable function or command is usually insufficient by itself. Successful execution also depends on Python or R versions, package managers, system libraries, CUDA or CPU assumptions, object formats, temporary files, output locations, logging behavior, and optional runtime paths.

BioHarness therefore treats environment design as a compute concern. The harness should not need to derive installation steps at dispatch time when an environment profile is already available. The compute substrate should provide a concrete environment target, enforce the relevant resource and isolation assumptions, execute the selected surface, and return artifacts, logs, and structured failure information in a predictable form.

This design keeps the environment layer close to implementation without making backend package internals part of the default agent context. The agent-facing side can reason over method choice, execution surfaces, and profile selection. The compute-facing side carries the dependency stack and runtime details needed to make the selected surface executable.

## Method-First Environment Assembly

Environment work should start from the individual method repository rather than from a global environment template. Each method should first be read in the context provided by its authors: installation instructions, package descriptors, environment files, notebooks, scripts, Docker material, CI files, documented runtime entrypoints, optional dependencies, and resource notes.

This method-first pass preserves the original execution assumptions before BioHarness attempts to consolidate them. It should identify the main runtime shape, such as Python, R, mixed R/Python, script-based execution, notebook-based execution, container-only execution, CPU execution, GPU execution, or an unclear route. For spatial transcriptomics, this pass will often separate broad environment families such as scverse-style Python workflows, Seurat-oriented R workflows, Bioconductor-oriented workflows, image-heavy workflows, deep-learning workflows, and reporting or artifact-generation workflows. It should also identify whether optional paths are part of the core workflow or only support plotting, clustering, reporting, image utilities, bridges between languages, or acceleration.

The result of this phase is not a BioHarness runtime claim. It is an environment assembly view for the method: a compact description of what the upstream project appears to require and which parts need later confirmation through environment construction, import/load checks, fixture runs, or implementation review.

## Minimum-Common-Denominator Consolidation

After method-specific assembly, BioHarness should compare methods within the same task family and look for a minimum common set of compatible environments. The goal is not to force every method into one large global environment. The goal is to group methods whose dependency stacks, resource assumptions, and runtime routes can reasonably share a conda environment without making execution fragile.

The runtime families identified during method-first assembly become the input to this comparison. Some methods may fit a shared environment after dependency comparison. Others may require a dedicated environment because of old package pins, CUDA constraints, incompatible language bridges, system libraries, or backend-specific runtime assumptions.

The consolidation step should prefer the smallest environment that supports the intended task path. Optional paths should be evaluated separately from the core path. A method that uses an optional R bridge, GPU extra, image dependency, or visualization backend should not force that dependency into a shared environment unless it is part of the intended execution surface.

For a specific analysis problem, a planning package may choose a consolidated-first Install-Load policy. This is not a global one-environment architecture. Fallback Runtime Profiles should be evidence-driven after Install-Load review or impossible documented constraints.

## Method Runtime Boundary In Consolidated Environments

A consolidated environment may contain packages for more than one method, but execution should still enter the selected method's reviewed runtime boundary. Shared prefix membership does not imply that unrelated method package stacks may be imported before the selected backend route runs.

After method selection, the environment profile or method binding should preserve the selected route's required package family, native-library assumptions, and backend smoke path. When a shared environment changes native-library behavior through unrelated package stacks, use a method-specific invocation policy, preload policy, wrapper boundary, or dedicated profile.

## Profile And Capsule Design

`EnvironmentProfile` is the substrate object used to describe an environment target that the harness or compute layer can select. It should be serializable, reviewable, and stable enough to connect execution surfaces to concrete runtime preparation. The current schema shape is recorded in [contracts/environment_profile.schema.json](../../contracts/environment_profile.schema.json).

An environment profile should capture the dimensions that affect dispatch and execution: a stable profile identifier, the isolation mode, the dependency stack, the resource class, storage and artifact behavior, secret handling, and the execution provider or provider placeholder used by the current implementation stage. These fields are not meant to reproduce every package-install detail in prose. They provide the stable handle by which BioHarness can refer to an assembled compute environment.

Candidate capsules are the higher-level grouping formed from profile comparison. A capsule represents a candidate environment family for one or more related task paths or method families. Capsule names should refer back to the consolidated runtime families rather than restating the full dependency review. They describe grouping logic, not a completed runtime inventory.

The profile and capsule structure is important because it connects two otherwise separate activities. Method-first assembly records what individual tools require. Task-family consolidation turns compatible requirements into a smaller number of selectable compute targets. The resulting profiles and capsules are the intended presentation layer for environment selection.

## Compatibility And Performance Adaptation

Environment consolidation should first try to preserve upstream scientific behavior. The preferred responses to incompatibility are environment isolation, a dedicated profile, a wrapper boundary, optional-path deferral, or a legacy capsule when that is the clearest way to keep the original method usable.

When incompatibility affects non-core execution components, BioHarness may consider limited compatibility adaptation. This can include changes to input/output handling, file paths, artifact export, logging, visualization, data movement, optional helper code, or runtime glue. Performance-oriented changes, such as parallelization or more efficient data transfer, may also be considered when they are separable from the scientific algorithm and when their expected effect can be checked.

The strategy should remain conservative near the scientific core. Changes that affect graph construction, model fitting, loss functions, inference behavior, clustering logic, stochastic behavior, GPU/CPU numerical paths, or other components that determine scientific output need explicit documentation. If an alternative implementation is used because the original path cannot be made compatible, the planning record should state what changed, what original behavior it is compared against, what validation is required, and what uncertainty remains.

This adaptation policy is part of environment strategy because dependency conflicts often reveal the need for wrappers, compatibility edits, or dedicated capsules. It should not turn environment consolidation into an implicit rewrite program. Interface and runtime standardization can be useful; scientific equivalence requires separate evidence.

## Target Runtime Package

The intended delivery form is a set of task- or method-oriented conda environments carried by Docker-delivered runtime artifacts. The exact Docker granularity can be decided later: one image may carry multiple named environments, or different task families may receive separate images if isolation, size, resource class, or deployment constraints justify that split.

This target form gives BioHarness a concrete compute packaging direction. The agent or harness selects an execution surface and environment profile. The compute layer runs the selected surface inside the corresponding prepared environment once the required runtime artifacts exist. Logs, artifacts, environment identifiers, and structured failure information are returned for validation and provenance.

The current document defines the design direction for that environment substrate. Concrete runtime support should be established by later environment artifacts, reproducible builds, import checks, fixture runs, validation reports, and implementation records.
