# Layer3/4 v0.7.1 Acceptance Checklist

## Static template acceptance

- [ ] Required files exist.
- [ ] Layer3 YAML is valid.
- [ ] Layer4 YAML is valid.
- [ ] Layer3 contains no raw backend function names.
- [ ] Layer4 contains required sections.
- [ ] Every Layer3 functional surface has a Layer4 binding status.
- [ ] Evidence authority exists.
- [ ] Evidence resolution levels are recorded.
- [ ] Environment hold is not final without probe evidence.
- [ ] Coordinate contract is semantic at Layer3 and backend-specific at Layer4.
- [ ] Multi-sample policy is explicit.
- [ ] Target domain count policy is explicit.
- [ ] Validation distinguishes smoke, contract, visual sanity, fidelity, and runtime.
- [ ] Risk register exists.
- [ ] Decision log exists.
- [ ] No production support is claimed.

## Implementation readiness

- [ ] Critical backend symbols are resolved to symbol-level or line-level evidence.
- [ ] Environment import probe has run.
- [ ] Minimal smoke fixture has run.
- [ ] Output schema has been observed.
- [ ] Runtime and memory have been measured.
- [ ] Provenance has been emitted.
- [ ] Optional runtime paths are verified or disabled.
- [ ] License/package distribution review is complete.

## Production readiness

- [ ] Adapter implementation exists.
- [ ] Tests pass.
- [ ] Reproducible environment is available.
- [ ] RunRecord and ValidationReport are emitted.
- [ ] Cross-machine replay has been tested.
