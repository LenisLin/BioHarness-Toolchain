# Layer3 Method Config Template

## Purpose

This template defines the method-level Layer3-M config produced during `layer3_layer4_build`.

`layer3_method_config.yaml` records the controllable variable surface for one method, grouped by execution surface, plus concise binding targets and callable config projections needed for the build-produced Layer3 callable and method-owned Layer4 binding to consume the config.

## Status

This is a template artifact. It is not an independent workflow, prompt, verifier, method audit report, or Layer4 implementation record.

Layer3-M is build-side config output. It does not replace Layer3 callable contracts, Layer4 implementation closure, lifecycle trace evidence, action binding evidence, or later validation evidence.

## Required Shape

```yaml
method:

execution_surfaces:
  <execution_surface_name>:
    input_type:
    output_type:
    binding_targets:
      - name:
        kind: function | class | script | object_field | output_artifact | workflow_anchor
        role:
    variables:
      <variable_name>:
        variable_kind:
        function:
        value_type:
        allowed_values_or_range:
        notes:
    callable_config_projection:
      rule_or_path:
      projected_config_keys:
        - <layer4_config_key>
      layer4_accepted_config_keys_or_parser:
      projection_notes:
```

`variables` does not contain default values.

Layer4 resolves default behavior and native or rewrite binding details. Layer3-M defines the method-local controllable variable surface exposed to the registered Layer3 callable and records how that surface projects into the `config` key/value shape consumed by method-owned Layer4 code.

Every downstream-selectable execution surface must include `callable_config_projection`. A descriptive variable schema without a projection to Layer4 accepted `config` keys is insufficient for build publication.

## Boundary

Layer3-M may name concise native function, class, script, object-field, output-artifact, or workflow anchors when they clarify where controllable variables bind.

Layer3-M must not include:

- full native call sequence;
- source walkthrough;
- parser internals;
- workdir internals;
- environment invocation internals;
- object conversion internals;
- Layer4 implementation code.

Those details remain in reviewed bridge planning, method-chain lifecycle trace, action binding evidence, build audit, and Layer4 implementation files.

## Config Consumption Evidence

Build output and verification records should use this minimum evidence shape when referring to Layer3-M consumption:

```yaml
config_consumption:
  layer3_callable_accepts_or_loads_config: true
  config_values_passed_to_layer4: true
  callable_config_projection_path_or_rule:
  projected_config_keys:
    - <layer4_config_key>
  layer4_accepted_config_keys_or_parser:
  method_evidence_path_or_symbol:
```

`config_consumption` proves the parse/pass channel from the registered Layer3 callable into the method-owned Layer4 binding, including the projection from Layer3-M variables into the Layer4 callable `config` shape. It does not prove native final parameter values, runtime support, functional correctness, algorithmic equivalence, or biological correctness.

Post-synthesis config projection audit status is assigned only in the completion matrix by the main implementation window or verifier. This template records method evidence, not final matrix `layer3_method_config_consumption_status=pass_after_synthesis_audit`.

Config consumption evidence must not be used as action-path evidence. Passing config values to Layer4 proves only the parse/pass channel; it does not prove that the reviewed native action, accepted glue, bounded equivalent implementation, or reviewed rewrite executed or was reached.
