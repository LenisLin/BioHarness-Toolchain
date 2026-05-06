# Agent Protocol: Layer 1/2 Selection

Use this protocol when a user asks for spatial transcriptomics downstream analysis planning, method choice, or tool selection inside BioHarness.

## Core Rule

Start from the repo-authoritative Layer 1/2 knowledge registry. Do not begin by searching for packages, recalling packages from memory, or proposing external tools.

Required entry order:

1. Read `knowledge_registry/layer1/task_catalog.md`.
2. Choose the best matching `Analysis Problem` using the user's scientific object and target output first. Use input signals only to break ties.
3. Open the exact `Route` listed in the Layer 1 table.
4. Use the selected Layer 2 topic file's `Problem boundary`, `Method feature table`, and `Decision tree` to choose branch-local methods.
5. Return the selected problem, route, branch rationale, candidate method or methods, and caveats.

## Closed-World Selection

For ordinary tasks, the formal candidate space is closed:

- Use only the 20 active `Analysis Problem` values in `knowledge_registry/layer1/task_catalog.md`.
- Use only the methods listed in the selected `knowledge_registry/layer2/*.md` file.
- Do not add package names from memory or outside literature.
- Do not turn broad backbone packages into dedicated method-table candidates unless the topic file marks them that way.

If the user explicitly asks about a method, package, paper, or update that is outside the registry, mark the situation as `out_of_formal_review`. Explain that it requires a separate source/evidence update before it can be merged into ordinary Layer 1/2 selection.

## Ambiguity Handling

If the user's request contains more than one scientific endpoint, split it into multiple Layer 1 routes and handle each separately.

If multiple routes remain plausible after checking scientific object and target output, report the ambiguity and ask for the missing endpoint or signal. Do not force a method choice from a weak route.

If the user names a package but the scientific endpoint maps elsewhere, route by endpoint first and mention the named package only as a user-provided constraint or out-of-formal item.

## Scientific Claim Boundary

Describe Layer 2 outputs as inferred, scored, summarized, predicted, reconstructed, associated, or interpreted according to the topic file. Do not describe model outputs as experimentally proven mechanisms or causal truth.

For communication, perturbation, phenotype/cohort, trajectory, and clonal tasks, keep association, model structure, pathway-aware interpretation, and causal claims separate. Only use causal language when the topic file explicitly limits it to model assumptions or interpretation.

## Forbidden Outputs

Do not provide:

- package installation instructions
- commands
- parameter schemas
- Docker or conda runtime claims
- environment capsule availability
- adapter or wrapper readiness
- Layer 3/4 execution-surface claims
- default-method claims
- universal method rankings across incompatible branches

## Recommended Response Shape

Use a compact handoff:

```text
Layer 1 route: <Analysis Problem>
Why this route: <scientific object + target output>
Layer 2 file: <knowledge_registry/layer2/...md>
Branch logic: <decision-tree branch followed>
Candidate method(s): <method names from the selected topic only>
Caveats: <evidence-bounded limitations or ambiguity>
Out-of-formal status: none | out_of_formal_review_required
```

