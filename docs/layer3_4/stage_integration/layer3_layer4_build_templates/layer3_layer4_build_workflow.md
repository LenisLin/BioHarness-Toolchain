# Layer3 / Layer4 Build Workflow Template

## Purpose

This file is the execution workflow template indexed by `docs/layer3_4/stage_integration/layer3_layer4_build.md` for execution windows and method-level subagents.

It defines implementation-start checks, method-subagent dispatch, lifecycle trace checks, closure inspection, the build execution loop, and import-check boundaries for a Gate 2-reviewed `layer3_layer4_build` invocation.

Audit output shapes for lifecycle, anti-surrogate evidence, per-row build audit, and publication index sanity are defined in `layer3_layer4_build_audit_outputs.md`.

## Implementation-Start Checks

Before implementation begins, confirm that required Gate 2 rows, reviewed implementation contracts, source roots or source locators, environment reference, and reviewed output root are present. These implementation-start checks are the phase-start stop boundary.

After implementation-start checks pass, source-understanding gaps inside the reviewed route are implementation work in this build invocation. Rows enter verifier handoff only after the registered Layer3 callable, reachable Layer4 implementation path, action binding list, code-located action evidence, source evidence, and strict-output mapping are present.

For multi-method invocations, method-subagent dispatch is an implementation-start check. The build may dispatch method subagents in ordered batches, with at most 6 active method subagents in each batch. The build proceeds to publication only after every build-required method has an assigned method subagent, recorded dispatch evidence, all repair-loop returns consumed, and final or repaired `PASS` method evidence.

## Build-Ready Implementation Contract

Before implementation, each build-required row must have a reviewed implementation contract with:

- native call sequence;
- native call sites;
- source-observed call flow for adapter and wrapper rows;
- native return objects and source consumer patterns for adapter and wrapper rows;
- signature binding;
- canonical input or prior-state source;
- private state policy;
- private state shape or container form when state crosses surfaces;
- strict output mapping;
- artifact policy;
- result selection policy, when the native method can produce multiple candidate labels or result rows;
- method-chain state handoff policy, when prior-surface private state is consumed by later surfaces;
- reviewed compatibility rewrite handoff candidate, when applicable;
- runtime-only compatibility glue and bounded equivalence evidence, when implemented during build;
- selected bridge smoke check requirement when the row uses a language bridge, object conversion, backend initialization wrapper, package helper API, or runtime-only compatibility glue;
- anti-surrogate audit boundary, including route basis, preservation/equivalence evidence, fail-closed behavior when no accepted route basis exists, and runtime observation policy for long-running routes.

The reviewed contract is the build starting point.

## Method-Subagent Execution Boundary

For a multi-method build, implementation is method-owned.

The main implementation window performs:

- phase-start input checks;
- one method-subagent prompt per build-required method, instantiated from `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md` and checked against that template's Method Subagent Self-Check before dispatch;
- ordered method-subagent dispatch batches with at most 6 active methods per batch;
- method iteration status collection, repair-loop redispatch, and final or repaired `PASS` evidence before opening the next batch;
- explicit repair-loop enforcement: any `FAIL_WITH_REPAIRS` packet must produce a repair assignment, same-method redispatch or resumed implementation, rerun of the affected checks, and final repaired `PASS` evidence before later batches, global collation, or publication can proceed;
- method-agnostic shared package scaffolding;
- method evidence collation;
- final callable-import, route-level backend-load, selected bridge smoke-check, runtime adapter path, surface-binding semantic correspondence, reviewed action effect reconciliation, lifecycle, per-row result, and audit evidence collation into the draft publication package;
- post-synthesis audit-status normalization before final matrix publication: independent audit statuses are written or confirmed only after evidence exists and is inspected by the main implementation window or verifier, not copied as bare `pass` from method-subagent synthesis text;
- generation of `package_layout.yaml` after method evidence collation, derived from the invocation scope and draft completion matrix;
- publication index sanity check on the draft completion matrix;
- draft package publishability check;
- global verifier handoff on the draft publication package;
- final confirmation of `package_layout.yaml` after global verifier `PASS`, without changing method, surface, or row-record pointers unless the package is recollated and reverified;
- final registry, matrix, package layout, and report publication.

`package_layout.yaml` lists only current in-scope methods and reviewed denominator surfaces, and its pointers must target existing standard package locations. It is not publication index sanity row-level evidence and must not be added to the publication index sanity row logic.

### Method-Subagent Prompt Preparation

Before dispatching method subagents, the main implementation window must instantiate one prompt per build-required method from `docs/layer3_4/stage_integration/layer3_layer4_build_templates/layer3_layer4_method_subagent_prompt.md`.

A generated method-subagent prompt is dispatchable only when it fills the template's required prompt fields for the assigned method, including `analysis_problem`, `workflow_phase`, `method`, `repo_root`, `results_root`, `current_artifact_root`, `implementation_root`, `method_build_output_root`, `owned_paths`, `read_only_inputs`, `minimum_reference_documents`, `reference_documents`, `execution_environment`, `reviewed_rows`, `surface_order`, `strict_outputs`, `native_or_rewrite_actions`, `private_state_policy`, `held_rows`, `method_verifier`, `return_evidence`, and `stop_condition`.

The generated prompt must preserve the template's implementation workflow, required method evidence, return-status semantics, and stop conditions. In particular, it must state that `FAIL_WITH_REPAIRS` is a repair-loop packet for the current method iteration, not a completed method state, and that the main implementation window must redispatch or otherwise consume the repair before publication.

Before dispatch, the main implementation window must run the Method Subagent Self-Check from `layer3_layer4_method_subagent_prompt.md` against each generated method prompt. If a prompt does not pass the self-check, prompt preparation is `REPAIR_REQUIRED`; repair the prompt before dispatch. Do not dispatch an ad hoc, abbreviated, or template-incomplete method prompt as method-subagent evidence.

Each method subagent performs:

- method-owned Layer3 callable implementation;
- method-level Layer3-M variable schema generation;
- per-surface `callable_config_projection` generation or recording;
- config channel implementation proving that the projection can produce the key/value `config` shape accepted by the Layer4 callable or parser;
- method-owned Layer4 adapter, wrapper, runtime-only compatibility glue, bounded equivalent implementation, or prior-reviewed algorithmic rewrite implementation;
- downstream runtime adapter path readiness evidence for every build-required row proposed as downstream-selectable;
- surface-binding semantic correspondence evidence for each build-required row proposed as downstream-selectable;
- reviewed action effect reconciliation evidence for each build-required row proposed as downstream-selectable;
- method-chain lifecycle trace;
- config consumption evidence recording;
- anti-surrogate audit evidence for action-path closure;
- selected bridge smoke-check execution and evidence recording when required by the row boundary;
- method-level verifier handoff;
- method-local build evidence.

If method subagent dispatch is unavailable, the phase stops with `STOP_BEFORE_IMPLEMENTATION`.

A prompt-preparation defect is not method-subagent dispatch unavailability. If a generated method prompt is missing required template fields, reference documents, return-status semantics, stop conditions, or self-check coverage, record `REPAIR_REQUIRED` for prompt preparation and repair the prompt before dispatch. Do not convert prompt-preparation defects into method-level `STOP_BEFORE_IMPLEMENTATION` unless subagent dispatch itself is unavailable or a phase-start required input is genuinely missing.

Method iteration return status is one of `PASS`, `FAIL_WITH_REPAIRS`, or `STOP_BEFORE_IMPLEMENTATION`. `FAIL_WITH_REPAIRS` is terminal only for the current method-subagent iteration. It is not a final method state, not a package state, not a fallback package status, not a completion-report state, and not a controller stop condition. The main implementation window must consume it as a repair packet, record it as transient builder evidence, return the first repair to the same method assignment, apply or assign the repair in the method-owned implementation path, rerun from the affected surface/evidence class through the method verifier, and accept the method only after a repaired later iteration returns `PASS`.

Shared runtime files contain method-agnostic helpers only: interface checks, typed failures, object conversion, provenance helpers, and artifact writers. Method-specific reviewed action binding belongs in method-owned Layer4 code.

The public BioHarness interface is the registered Layer3 callable. Layer4 may privately execute reviewed native functions, accepted runtime-only compatibility glue, accepted bounded equivalent implementations, or prior-reviewed algorithmic rewrite actions.

Selected bridge smoke-check evidence is supporting evidence only. For a build-required row proposed as `downstream_selectable=true`, the registered Layer3 callable must also have an implemented downstream runtime adapter path. The normal callable path must not be smoke-check-only, `probe_backend`-only, unconditional deferred-runtime failure, or `NotImplementedError`. Build callable-path or bounded-adapter check status must not be used as a substitute for runtime adapter path implementation evidence.

Reviewed action inventory is derived from Gate 2 bridge planning and the method prompt's `native_or_rewrite_actions`. Method subagents must preserve reviewed action names in surface-binding semantic correspondence and reviewed action effect reconciliation records. They must not rename, summarize, or replace reviewed actions with handoff prose, adapter names, policy labels, provenance summaries, or source locators unless the record includes explicit reviewed bounded-equivalence or reviewed rewrite basis for that mapping.

## Method-Chain Lifecycle Trace Check

Layer3 / Layer4 build includes a method-chain lifecycle trace check for every method with build-required rows. The check is a source-backed implementation walkthrough. It traces how a new agent, using only the reviewed Layer3 public contract and registry, can call the surfaces in order while Layer4 creates and carries method-private state.

The lifecycle trace records:

- the agent-visible input contract for the method chain;
- the reviewed surface order;
- source-observed native call flow for adapter and wrapper rows as lifecycle context only;
- implemented binding call flow summary for each surface as lifecycle context only;
- a method-chain action ownership map naming each output-determining native action, its single owner surface, later consumer surfaces, and whether any repeated call is explicitly reviewed as non-output-determining and idempotent;
- duplicate-action check evidence for output-determining native actions across the reviewed surface order;
- anti-surrogate audit summary for each surface, including route basis, preservation/equivalence evidence, and runtime observation evidence for long-running routes when applicable;
- native return objects and source consumer patterns needed by each surface;
- private state created or updated by each surface;
- private state shape or container form when the state is consumed by later surfaces;
- private state consumed by later surfaces;
- canonical AnnData fields or public artifacts created by each surface;
- the strict-output or private state handoff target for each surface;
- the first surface adjusted inside the reviewed route before completion, when the chain is not yet closed under the reviewed contract.

A lifecycle trace passes when surface order is coherent, each consumed private state has an earlier producer, produced state shapes match source-observed consumer patterns, action ownership is recorded, and no output-determining action is duplicated across sequential surfaces without reviewed non-output-determining/idempotent rationale. Lifecycle trace does not replace surface-binding semantic correspondence, reviewed action effect reconciliation, anti-surrogate audit, or strict-output contract closure.

A lifecycle trace also requires method-chain action ownership closure: each output-determining native action has one owner surface, later surfaces consume produced prior state or strict output rather than re-executing that action, and any repeated native call is explicitly documented as non-output-determining, idempotent, and required by the native API boundary. A repeated fitting, training, MCMC, clustering, postprocessing, label-assignment, or other output-determining action across sequential surfaces is `REPAIR_REQUIRED`.

Lifecycle trace findings are builder-side repair inputs. The build execution loop consumes them through method-chain inspection and repairs from the first affected surface before verifier handoff.

## Build Execution Loop

For each method with one or more Gate2-approved build-required rows, keep that method's rows together because prior-surface private state may be consumed by later surfaces. In a multi-method invocation, the main implementation window instantiates all method prompts from `layer3_layer4_method_subagent_prompt.md`, runs the template self-check for each generated prompt, dispatches method-level implementation subagents in ordered batches of at most 6 methods, records dispatch evidence, waits for method iteration evidence for the current batch, consumes repairs before later batches, and then performs final collation only after all batches return `PASS`.

After implementation-start checks pass, the build loop has no repair-required final state. The executor may stop without publication only for `STOP_BEFORE_IMPLEMENTATION`, unavailable method-subagent dispatch, external interruption, or a documented contradiction with the reviewed Gate1/Gate2 boundary that requires return to review. All ordinary implementation, evidence, smoke-check, lifecycle, publication-index, or verifier repair findings must be routed back through the affected method subagent or final collation step and the loop must continue.

A repair-required package may be written only as transient builder evidence for debugging or external interruption. It is not a completed build package, must not be named or reported as final publication, must not contain downstream-selectable rows, and must not emit the completion report defined by `layer3_layer4_completion_report.md`.

The build loop is a control-flow specification only. Uppercase tokens name workflow-local states, placeholders, and abstract actions; they are not callable APIs, function names, or code-generation targets.

```text
PACKAGE_CLOSURE_STATUS = REPAIR_REQUIRED

WHILE PACKAGE_CLOSURE_STATUS != PASS:
    RUN PHASE IMPLEMENTATION-START CHECKS

    IF START_STATUS == STOP_BEFORE_IMPLEMENTATION:
        RECORD MISSING PHASE-START INPUTS
        STOP WITHOUT PUBLICATION

    PREPARE ONE METHOD SUBAGENT PROMPT PER BUILD-REQUIRED METHOD BY INSTANTIATING layer3_layer4_method_subagent_prompt.md
    RUN METHOD SUBAGENT PROMPT SELF-CHECK FOR EACH GENERATED PROMPT

    WHILE ANY METHOD_PROMPT_STATUS == REPAIR_REQUIRED:
        RECORD PROMPT PREPARATION FINDING
        REPAIR THE AFFECTED METHOD PROMPT BEFORE DISPATCH
        RERUN METHOD SUBAGENT PROMPT SELF-CHECK FOR EACH REPAIRED PROMPT

    PARTITION METHODS_WITH_BUILD_REQUIRED_ROWS INTO DISPATCH BATCHES OF AT MOST 6 METHODS
    RECORD SUBAGENT DISPATCH LOG WITH subagent_prompt_template POINTING TO layer3_layer4_method_subagent_prompt.md

    FOR EACH METHOD_BATCH:
        DISPATCH METHOD SUBAGENTS IN METHOD_BATCH
        RECORD BATCH DISPATCH EVIDENCE
        WAIT UNTIL EVERY METHOD IN METHOD_BATCH RETURNS METHOD ITERATION STATUS

        IF ANY METHOD_SUBAGENT_STATUS == STOP_BEFORE_IMPLEMENTATION:
            RECORD METHOD START FAILURE
            STOP WITHOUT PUBLICATION

        WHILE ANY METHOD_SUBAGENT_STATUS == FAIL_WITH_REPAIRS:
            RECORD REPAIR PACKET AS TRANSIENT BUILDER EVIDENCE
            RETURN FIRST REPAIR TO THE SAME METHOD ASSIGNMENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            WAIT FOR A REPAIRED METHOD ITERATION STATUS
            UPDATE SUBAGENT DISPATCH LOG REPAIR_LOOP_ITERATIONS
            DO NOT OPEN THE NEXT BATCH, COLLATE GLOBAL EVIDENCE, OR PUBLISH UNTIL THE AFFECTED METHOD RETURNS PASS

        IF ANY METHOD_SUBAGENT_STATUS != PASS:
            RECORD METHOD FAILURE
            STOP WITHOUT PUBLICATION

        INSPECT METHOD-CHAIN LIFECYCLE FOR EACH METHOD IN METHOD_BATCH

        IF METHOD_CHAIN_LIFECYCLE_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT ROW ACTION-PATH CLOSURE FOR EACH DOWNSTREAM-SELECTABLE BUILD-REQUIRED ROW IN METHOD_BATCH

        IF ROW_ACTION_PATH_CLOSURE_STATUS == REPAIR_REQUIRED:
            IF REPAIR_CLASS == observation_continues:
                CONTINUE OR RESUME REVIEWED RUNTIME OBSERVATION ACCORDING TO THE RECORDED NO-PROGRESS POLICY
            ELSE:
                RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
                APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
                RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
                RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT ST IMAGE ALIGNMENT CONTRACT FOR EACH METHOD IN METHOD_BATCH

        IF ST_IMAGE_ALIGNMENT_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT SELECTED BRIDGE SMOKE CHECKS FOR EACH METHOD IN METHOD_BATCH

        IF BRIDGE_SMOKE_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT DOWNSTREAM-RUNTIME-PATH READINESS FOR EACH PROPOSED DOWNSTREAM-SELECTABLE BUILD-REQUIRED ROW IN METHOD_BATCH

        IF DOWNSTREAM_RUNTIME_PATH_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT SURFACE-BINDING SEMANTIC CORRESPONDENCE FOR EACH PROPOSED DOWNSTREAM-SELECTABLE BUILD-REQUIRED ROW IN METHOD_BATCH

        IF SURFACE_BINDING_CORRESPONDENCE_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT REVIEWED ACTION EFFECT RECONCILIATION FOR EACH PROPOSED DOWNSTREAM-SELECTABLE BUILD-REQUIRED ROW IN METHOD_BATCH

        IF REVIEWED_ACTION_EFFECT_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

        INSPECT LAYER3-M CONFIG CALLABLE CONSUMPTION FOR EACH METHOD IN METHOD_BATCH

        IF CONFIG_CONSUMPTION_STATUS == REPAIR_REQUIRED:
            RETURN FIRST REPAIR TO THE SAME METHOD SUBAGENT
            APPLY OR ASSIGN THE REPAIR INSIDE THE METHOD-OWNED IMPLEMENTATION PATH
            RERUN THE AFFECTED SURFACE, EVIDENCE CLASS, METHOD CHECKS, AND METHOD VERIFIER
            RESTART FROM AFFECTED SURFACE BEFORE OPENING NEXT BATCH

    COLLATE FINAL CALLABLE-IMPORT, ROUTE-LEVEL BACKEND-LOAD, SELECTED BRIDGE SMOKE-CHECK, RUNTIME ADAPTER PATH, SURFACE-BINDING SEMANTIC CORRESPONDENCE, REVIEWED ACTION EFFECT RECONCILIATION, LIFECYCLE, PER-ROW RESULT, AND AUDIT EVIDENCE INTO THE DRAFT PUBLICATION PACKAGE

    NORMALIZE POST-SYNTHESIS AUDIT STATUSES ON THE DRAFT PUBLICATION PACKAGE:
        FOR EACH INDEPENDENT AUDIT FIELD IN THE DRAFT MATRIX:
            CONFIRM THE UNDERLYING EVIDENCE EXISTS IN THE DRAFT PACKAGE
            CONFIRM IT WAS INSPECTED BY THE MAIN WINDOW OR VERIFIER
            RECORD pass_after_synthesis_audit ONLY AFTER THAT CONFIRMATION
            RECORD repair_required WHEN EVIDENCE IS MISSING, UNREADABLE, OR INCONSISTENT
            DO NOT COPY BARE pass FROM METHOD-SUBAGENT SYNTHESIS TEXT INTO FINAL MATRIX INDEPENDENT AUDIT FIELDS

    SET proposed_downstream_selectable=true ONLY WHEN:
        NON-AUDIT EXECUTION CHECKS USE THEIR ALLOWED PASS VALUES
        INDEPENDENT AUDIT GATES USE pass_after_synthesis_audit OR ALLOWED not_applicable/not_required
        runtime_adapter_path_status == implemented
        layer3_method_config_consumption_status == pass_after_synthesis_audit

    GENERATE package_layout.yaml FROM THE INVOCATION SCOPE, REVIEWED DENOMINATOR, DRAFT COMPLETION MATRIX, AND STANDARD PACKAGE LOCATIONS

    RUN PUBLICATION INDEX SANITY CHECK ON THE DRAFT COMPLETION MATRIX

    IF PUBLICATION_INDEX_SANITY_STATUS == repair_required:
        RECORD PUBLICATION INDEX FINDING
        RETURN FIRST REPAIR TO THE AFFECTED METHOD SUBAGENT OR FINAL COLLATION STEP
        RERUN THE AFFECTED METHOD, SURFACE, EVIDENCE CLASS, OR COLLATION CHECK
        RESTART FROM AFFECTED METHOD, SURFACE, OR EVIDENCE CLASS

    ASSIGN FINAL downstream_selectable=true ONLY FOR ROWS WITH proposed_downstream_selectable=true AND PUBLICATION_INDEX_SANITY_STATUS == pass

    IF PUBLICATION_STATUS != PUBLISHABLE:
        RECORD PUBLICATION COLLATION FINDING
        RETURN FIRST REPAIR TO THE AFFECTED METHOD SUBAGENT OR FINAL COLLATION STEP
        RERUN THE AFFECTED METHOD, SURFACE, EVIDENCE CLASS, OR COLLATION CHECK
        RESTART FROM AFFECTED METHOD, SURFACE, OR EVIDENCE CLASS

    RUN GLOBAL COMPLETION VERIFIER ON THE DRAFT PUBLICATION PACKAGE

    IF GLOBAL_VERIFIER_RESULT == FAIL_WITH_REPAIRS:
        RECORD VERIFIER REPAIR PACKET AS TRANSIENT BUILDER EVIDENCE
        RETURN FIRST REPAIR TO THE AFFECTED METHOD SUBAGENT OR FINAL COLLATION STEP
        APPLY OR ASSIGN THE REPAIR IN THE METHOD-OWNED IMPLEMENTATION PATH OR FINAL COLLATION STEP
        RERUN THE AFFECTED METHOD, SURFACE, EVIDENCE CLASS, PUBLICATION RECORD, AND GLOBAL VERIFIER
        RESTART FROM AFFECTED METHOD, SURFACE, EVIDENCE CLASS, OR PUBLICATION RECORD

    CONFIRM package_layout.yaml STILL MATCHES THE CURRENT IN-SCOPE METHODS, REVIEWED DENOMINATOR SURFACES, FINAL COMPLETION MATRIX, AND STANDARD PACKAGE LOCATIONS
    DO NOT CHANGE METHOD, SURFACE, OR ROW-RECORD POINTERS AFTER GLOBAL VERIFIER PASS UNLESS THE PACKAGE IS RECOLLATED AND GLOBAL VERIFIER IS RERUN

    PUBLISH FINAL REGISTRATION, COMPLETION MATRIX, PACKAGE LAYOUT, COMPLETION REPORT, AND PER-ROW RECORDS
    PACKAGE_CLOSURE_STATUS = PASS
```

## Builder Internal Closure Inspection

Builder-side closure inspection uses only workflow-local statuses: `STOP_BEFORE_IMPLEMENTATION`, `REPAIR_REQUIRED`, `PASS`, and `PUBLISHABLE`.

```text
INSPECT ROW ACTION-PATH CLOSURE:
    TRACE LAYER3 CALLABLE TO LAYER4 IMPLEMENTATION
    FOR EACH ACTION BINDING ITEM:
        CONFIRM IMPLEMENTATION FILE AND SYMBOL ARE ON TRACE
        CONFIRM TRACE EXECUTES REVIEWED NATIVE/REWRITE SOURCE
        CONFIRM PRODUCED STATE/OUTPUT/ARTIFACT IS RECORDED
        CONFIRM PRODUCED STATE/OUTPUT/ARTIFACT IS USED FOR CURRENT ROW STRICT OUTPUT
        CONFIRM ACTION EVIDENCE COMES FROM EXECUTED LAYER4 BINDING, NOT FROM SUPPORTING EVIDENCE ALONE
        CONFIRM REWRITE OR COMPATIBILITY GLUE HAS PRIOR REVIEW BASIS OR LIGHTWEIGHT PRESERVATION/EQUIVALENCE EVIDENCE
        CONFIRM PRODUCTION PATH DOES NOT USE MOCK, FAKE, PLACEHOLDER, DUMMY, RANDOM, OR CONTRACT-ONLY SURROGATE STATE/OUTPUT
        CONFIRM BACKEND-UNAVAILABLE OR NOT-STARTED PATHS FAIL CLOSED INSTEAD OF PRODUCING SUCCESS STRICT OUTPUT
        CONFIRM STARTED LONG-RUNNING PATHS RECORD RUNTIME OBSERVATION EVIDENCE RATHER THAN FAILING SOLELY FOR ELAPSED TIME
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT ST IMAGE ALIGNMENT CONTRACT:
    FOR EACH BUILD-REQUIRED ROW WHOSE REVIEWED ROUTE USES H&E OR MORPHOLOGY IMAGE PAYLOAD FOR SCIENTIFIC-OUTPUT-DETERMINING BEHAVIOR:
        CONFIRM PLATFORM FAMILY IS RECORDED
        CONFIRM SPATIAL COORDINATE SEMANTICS ARE RECORDED SEPARATELY FROM IMAGE PIXEL FRAME
        CONFIRM IMAGE SOURCE, IMAGE KEY OR RESOLUTION, IMAGE SHAPE, AND TRANSFORM EVIDENCE ARE RECORDED
        FOR VISIUM IMAGE-AWARE ROUTES:
            CONFIRM HIRES OR LOWRES IMAGE PATCHING USES THE MATCHING SCALEFACTOR WHEN COORDINATES ARE FULLRES PIXEL COORDINATES
            CONFIRM ARRAY ROW/COL COORDINATES ARE NOT USED AS IMAGE PIXEL CROP COORDINATES WITHOUT REVIEWED MAPPING EVIDENCE
        FOR XENIUM IMAGE-AWARE ROUTES:
            CONFIRM VISIUM SCALEFACTOR LOGIC IS NOT ASSUMED
            CONFIRM MORPHOLOGY IMAGE COORDINATE OR PHYSICAL-TO-PIXEL TRANSFORM EVIDENCE IS RECORDED
        CONFIRM SELECTED BRIDGE SMOKE CHECK OR BOUNDED ALIGNMENT CHECK EXERCISES A NONTRIVIAL TRANSFORM WHEN THE REVIEWED ROUTE REQUIRES ONE
        IF REQUIRED ALIGNMENT EVIDENCE IS MISSING OR THE IMPLEMENTATION DIRECTLY CROPS THE SELECTED IMAGE WITH UNMAPPED SPATIAL COORDINATES, RECORD repair_required
        IF THE ROW IS NOT IMAGE-AWARE, RECORD not_applicable
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT SELECTED BRIDGE SMOKE CHECK:
    FOR EACH SURFACE WITH LANGUAGE BRIDGE, OBJECT CONVERSION, BACKEND INITIALIZATION WRAPPER, PACKAGE HELPER API, OR RUNTIME-ONLY COMPATIBILITY GLUE:
        CONFIRM THE CHECK USES THE COMPLETE REVIEWED INVOCATION
        CONFIRM THE CHECK ENTERS THE METHOD-OWNED LAYER4 BRIDGE PATH RATHER THAN ONLY IMPORTING A PACKAGE
        CONFIRM BACKEND INITIALIZATION SUCCEEDS OR FAILS CLOSED WITH REPAIR EVIDENCE
        CONFIRM THE FIRST SELECTED NATIVE/GLUE ACTION BOUNDARY IS REACHED WITH MINIMAL BOUNDED INPUT WHEN FEASIBLE
        CONFIRM FAILURES ARE CLASSIFIED WITH THE FIRST FAILED BRIDGE BOUNDARY
        CONFIRM THE CHECK DOES NOT CLAIM STRICT-OUTPUT PRODUCTION OR METHOD VALIDATION SUCCESS
    AGGREGATE REQUIRED BUILD-ROW STATUS:
        IF NO TRIGGERING BRIDGE BOUNDARY EXISTS FOR THE BUILD-REQUIRED ROW, RECORD not_required
        IF EVERY REQUIRED CHECK PASSES, RECORD pass
        IF ANY REQUIRED CHECK IS MISSING, FAILS, BYPASSES THE METHOD-OWNED LAYER4 PATH, OR LACKS REPAIR EVIDENCE, RECORD repair_required
        IF THE ROW IS REVIEWED HELD OR NON-BUILD-REQUIRED, RECORD held_with_reason AND downstream_selectable=false
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT DOWNSTREAM-RUNTIME-PATH READINESS:
    FOR EACH ROW WITH build_required=true AND PROPOSED downstream_selectable=true:
        CONFIRM THE REGISTERED LAYER3 CALLABLE HAS A NORMAL RUNTIME ADAPTER PATH INTO METHOD-OWNED LAYER4 CODE
        CONFIRM THE NORMAL PATH IS NOT SMOKE-CHECK-ONLY, probe_backend-ONLY, UNCONDITIONAL DEFERRED-RUNTIME FAILURE, OR NotImplementedError
        CONFIRM SELECTED BRIDGE SMOKE-CHECK EVIDENCE IS SEPARATE FROM RUNTIME ADAPTER IMPLEMENTATION EVIDENCE
        CONFIRM THE PATH IDENTIFIES REQUIRED CANONICAL INPUT OR PRIOR METHOD STATE
        CONFIRM THE PATH IDENTIFIES THE REVIEWED STRICT OUTPUT, METHOD STATE, OR ARTIFACT IT PRODUCES OR ADVANCES
        CONFIRM BUILD CALLABLE-PATH OR BOUNDED-ADAPTER CHECK STATUS IS NOT USED AS A SUBSTITUTE FOR IMPLEMENTATION EVIDENCE
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT SURFACE-BINDING SEMANTIC CORRESPONDENCE:
    FOR EACH build_required=true ROW PROPOSED downstream_selectable=true:
        EXTRACT reviewed_surface_intent, reviewed_strict_output_or_state, AND reviewed_native_or_rewrite_actions FROM REVIEWED INPUTS
        TRACE THE REGISTERED LAYER3 CALLABLE NORMAL PATH TO METHOD-OWNED LAYER4 BINDING
        CLASSIFY implemented_binding.actual_calls AS executed_call, symbol_lookup, import_only, dll_routine_presence, metadata_only, prior_state_consume, OR reviewed_equivalent
        CONFIRM THE ACTUAL BINDING CALLS BELONG TO THE CURRENT REVIEWED SURFACE OR HAVE REVIEWED OWNERSHIP CHANGE
        CONFIRM THE BINDING TARGET MATCHES THE REVIEWED STRICT OUTPUT OR STATE INTENT
        CONFIRM SYMBOL LOOKUP, IMPORT, DLL ROUTINE PRESENCE, METADATA, SMOKE-ONLY, OR PROBE-ONLY PATHS ARE NOT ACCEPTED AS CORRESPONDENCE PASS WITHOUT REVIEWED EQUIVALENCE OR OWNERSHIP CHANGE
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT REVIEWED ACTION EFFECT RECONCILIATION:
    FOR EACH build_required=true ROW PROPOSED downstream_selectable=true:
        EXTRACT REVIEWED ACTION INVENTORY FROM GATE2 BRIDGE PLANNING AND METHOD PROMPT native_or_rewrite_actions
        FOR EACH REVIEWED ACTION:
            RECORD expected_effect AND effect_basis
            CLASSIFY THE IMPLEMENTED BINDING CALL AS executed_call, symbol_lookup, import_only, dll_routine_presence, metadata_only, prior_state_consume, OR reviewed_equivalent
            CONFIRM THE ACTION HAS EFFECT-BEARING EVIDENCE FROM EXECUTED CALL, PRODUCED STATE/OUTPUT, CONSUMED PRIOR STATE, REVIEWED EQUIVALENT, OR REVIEWED REWRITE
            CONFIRM SYMBOL LOOKUP, IMPORT, DLL ROUTINE PRESENCE, METADATA, STATE-STRING-ONLY, LIFECYCLE PROSE, OR BRIDGE-SMOKE BOUNDARY-ONLY EVIDENCE IS NOT USED AS ACTION-EFFECT PASS
            CONFIRM PRODUCED STATE OR OUTPUT IS CONSUMED BY THE CURRENT SURFACE WHEN THAT EFFECT IS REQUIRED FOR THE REVIEWED STRICT OUTPUT
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT METHOD-CHAIN LIFECYCLE:
    CONFIRM REVIEWED SURFACE ORDER IS RECORDED
    CONFIRM CONSUMED PRIVATE STATE HAS EARLIER PRODUCER
    CONFIRM STATE SHAPE MATCHES CONSUMER PATTERN
    CONFIRM ACTION OWNERSHIP IS RECORDED FOR OUTPUT-DETERMINING ACTIONS
    CONFIRM NO DUPLICATE OUTPUT-DETERMINING ACTION IS EXECUTED ACROSS SEQUENTIAL SURFACES WITHOUT REVIEWED NON-OUTPUT-DETERMINING/IDEMPOTENT RATIONALE
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT PUBLICATION INDEX SANITY:
    CONFIRM COMPLETION MATRIX HAS REQUIRED COLUMNS FROM THE CURRENT BUILD OUTPUT TEMPLATE
    FOR EACH ROW WITH build_required=true AND (proposed_downstream_selectable=true OR downstream_selectable=true):
        CONFIRM KEY STATUS FIELDS ARE PRESENT AND USE ALLOWED PASS VALUES
        CONFIRM runtime_adapter_path_status IS PRESENT AND COMPATIBLE WITH proposed_downstream_selectable OR downstream_selectable
        CONFIRM surface_binding_correspondence_status IS pass_after_synthesis_audit AND surface_binding_correspondence_evidence IS PRESENT, EXISTS, AND IS READABLE
        CONFIRM reviewed_action_effect_status IS pass_after_synthesis_audit AND reviewed_action_effect_reconciliation_evidence IS PRESENT, EXISTS, AND IS READABLE
        CONFIRM INDEPENDENT AUDIT VERDICTS ARE PRESENT AND USE pass_after_synthesis_audit WHERE REQUIRED BY THE COMPLETION MATRIX
        CONFIRM CORE POINTER FIELDS ARE PRESENT
        CONFIRM CORE FILE POINTERS EXIST AND ARE READABLE
        CONFIRM build_output_result AND build_audit REFER TO THE SAME METHOD AND EXECUTION SURFACE AS THE MATRIX ROW
        CONFIRM PER-ROW downstream_selectable DOES NOT CONTRADICT THE MATRIX ROW
        DO NOT REPLACE INDEPENDENT SEMANTIC AUDITS WITH PUBLICATION INDEX SANITY
    RETURN PASS OR REPAIR_REQUIRED
```

```text
INSPECT LAYER3-M CONFIG CALLABLE CONSUMPTION:
    CONFIRM METHOD CONFIG EXISTS
    CONFIRM CURRENT EXECUTION SURFACE SECTION EXISTS
    CONFIRM REGISTERED LAYER3 CALLABLE ACCEPTS OR LOADS CONFIG
    CONFIRM CURRENT EXECUTION SURFACE HAS A callable_config_projection
    CONFIRM THE PROJECTION PRODUCES THE KEY/VALUE SHAPE PASSED AS Layer4 CALLABLE config
    CONFIRM PROJECTED CONFIG KEYS MATCH THE Layer4 CALLABLE CONFIG PARSER OR CONSUMER ACCEPTED KEYS
    CONFIRM CONFIG VALUES PASS INTO METHOD-OWNED LAYER4 BINDING THROUGH THAT PROJECTION
    RETURN PASS OR REPAIR_REQUIRED
```

## Import Check Boundary

Import checks are allowed only under the reviewed environment binding record (`harness_environment.yaml`) or reviewed environment build output path.

Callable import checks and route-level backend-load checks use the complete reviewed invocation selected from environment build evidence, including command-level environment variables when those variables were required for backend-load `PASS`.

Allowed import checks may import the BioHarness implementation module, callable registration path, adapter or wrapper registration path, or selected backend through the reviewed adapter/wrapper/rewrite boundary.

Import checks establish importability and backend loadability. They do not satisfy reviewed action binding unless the corresponding Layer4 code path is also verifier-confirmed.

Selected bridge smoke checks are separate from import checks and route-level backend-load checks. A package-level import, module import, or `library(...)` success is not sufficient when the implemented Layer4 path performs additional bridge initialization, conversion activation, helper API calls, or object conversion before reaching the selected native action.
