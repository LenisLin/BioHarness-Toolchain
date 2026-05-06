# Layer 1 Knowledge Registry Entry

This directory is the repo-authoritative Layer 1 problem-routing entry for the BioHarness knowledge registry.

The source/evidence Layer 1 registry remains in `/mnt/NAS_21T/ProjectData/BioHarness/results/layer1/`. This entry is the compact agent-facing routing view.

Layer 1 is the compact problem-routing level. It helps an agent choose one active `Analysis Problem` using scientific target, input signal, and target output. It is not a method recommendation or execution-readiness layer.

## Current Entry

- `task_catalog.md`: compact Layer 1 routing table plus problem-routing logic for the active Analysis Problem set.

The task catalog does not list methods, counts, PMID/DOI evidence, or execution claims. It does include explicit Layer 2 routes for agent-facing handoff after problem selection.
