# Spatial Domain Identification Skill Blueprint

## Purpose

Provide a future Layer 1 skill entry for spatial domain identification tasks.

This file is illustrative only and does not freeze a current Layer 3 default.

## Selection Rules

- prefer this skill when the user goal is tissue-domain calling or domain-level clustering
- route through histology-aware defaults when histology is available
- keep Layer 2 comparison cues in sync with `/mnt/NAS_21T/ProjectData/BioHarness/2026-04-16_domain_identification_layer2_pilot.md`

## Default Surface

- `example.spatial_domain_identification.spagcn`

## Validation Notes

- require schema preflight before dispatch
- require domain-label post-run checks before release
