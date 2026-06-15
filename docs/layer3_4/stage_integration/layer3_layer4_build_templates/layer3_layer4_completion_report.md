# Layer3 / Layer4 Completion Report Template

## Purpose

This report is filled after the build workflow, outputs, and verifier checks for a `layer3_layer4_build` invocation are complete.

Fields come from the current build invocation's final published package and verifier evidence.

## Completion Report Fields

Completion reporting is emitted for the completed invocation after action-path closure, strict-output contract closure, method-level verifier pass, final callable-import, route-level backend-load, selected bridge smoke-check, lifecycle, per-row result, and audit evidence collation into the draft publication package, publication index sanity pass on the draft completion matrix, draft package publishability, and global verifier pass on the draft publication package.

Do not emit this completion report for a `FAIL_WITH_REPAIRS` verifier result, method-subagent repair packet, publication-index repair finding, or collation repair finding. Those records are transient builder repair evidence. A completion report requires global verifier `PASS`, publication-index sanity `pass`, no unresolved repairs, no unresolved repair-required findings, and final publication artifacts written after verifier `PASS`. A final completion report must not record `FAIL_WITH_REPAIRS` as the completed invocation status, fallback package status, final matrix status, or downstream-selectable basis.

Every completed invocation reports:

- output root and completion matrix path;
- package layout path;
- denominator counts: total rows, build-required rows, held rows, downstream-selectable rows;
- method-subagent execution summary for multi-method invocations;
- method evidence roots and method verifier pass summary;
- Layer3-M config path summary by method;
- config consumption status summary;
- selected bridge smoke-check summary by method/surface, including required/not-required status and unresolved repair classes if any;
- any methods/rows without config because held or not build-required;
- global verifier pass summary;
- shared runtime boundary summary;
- lifecycle trace summary by method;
- per-row result and audit pointer summary;
- publication index sanity summary;
- audit evidence summary, including anti-surrogate and lifecycle evidence paths;
- final publication summary;
- build-boundary non-claims.
