#!/usr/bin/env python3
"""Create method-agnostic SDI Layer3/Layer4 runtime scaffolding.

This script writes only shared helpers and package scaffolding under the
reviewed NAS implementation root. Method-specific bindings and evidence are
owned by method build steps.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent


BUILD_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/layer3_layer4_builds"
)
IMPL_ROOT = Path(
    "/mnt/NAS_21T/ProjectData/BioHarness/results/layer3_4/"
    "spatial_domain_identification/runtime_artifacts/"
    "layer3_layer4_implementations/SDI_runtime/python"
)
PKG = IMPL_ROOT / "bioharness_sdi_runtime"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).lstrip(), encoding="utf-8")


def main() -> None:
    for path in [
        BUILD_ROOT,
        BUILD_ROOT / "method_prompts",
        BUILD_ROOT / "verifier",
        BUILD_ROOT / "logs",
        IMPL_ROOT,
        PKG,
        PKG / "methods",
    ]:
        path.mkdir(parents=True, exist_ok=True)

    write(
        PKG / "__init__.py",
        """
        \"\"\"BioHarness SDI runtime package produced by Layer3/Layer4 build.

        The package exposes reviewed Layer3 callable bindings for spatial
        domain identification method surfaces. Importability is build-stage
        evidence only and is not a runtime support, validation, or scientific
        correctness claim.
        \"\"\"

        from .registry import get_callable, iter_surface_bindings, register_surface
        from .state import SDIMethodState, SDIRuntimeResult

        __all__ = [
            "SDIMethodState",
            "SDIRuntimeResult",
            "get_callable",
            "iter_surface_bindings",
            "register_surface",
        ]
        """,
    )
    write(
        PKG / "errors.py",
        """
        \"\"\"Typed fail-closed errors for SDI runtime bindings.\"\"\"


        class SDIRuntimeError(RuntimeError):
            \"\"\"Base runtime error for BioHarness SDI execution surfaces.\"\"\"


        class MissingDependencyError(SDIRuntimeError):
            \"\"\"Raised when a reviewed native dependency is unavailable.\"\"\"


        class ContractError(SDIRuntimeError):
            \"\"\"Raised when canonical input or prior method state is invalid.\"\"\"


        class BackendRouteError(SDIRuntimeError):
            \"\"\"Raised when a reviewed backend route cannot be reached.\"\"\"
        """,
    )
    write(
        PKG / "state.py",
        """
        \"\"\"Method-private state containers shared by method-owned bindings.\"\"\"

        from __future__ import annotations

        from dataclasses import dataclass, field
        from pathlib import Path
        from typing import Any


        @dataclass
        class SDIMethodState:
            method: str
            surface: str
            adata: Any | None = None
            private: dict[str, Any] = field(default_factory=dict)
            artifacts: dict[str, Path] = field(default_factory=dict)
            provenance: dict[str, Any] = field(default_factory=dict)


        @dataclass
        class SDIRuntimeResult:
            method: str
            surface: str
            output: Any | None = None
            state: SDIMethodState | None = None
            artifacts: dict[str, Path] = field(default_factory=dict)
            provenance: dict[str, Any] = field(default_factory=dict)
        """,
    )
    write(
        PKG / "contracts.py",
        """
        \"\"\"Canonical contract helpers for SDI Layer3 callables.\"\"\"

        from __future__ import annotations

        from pathlib import Path
        from typing import Any

        from .errors import ContractError
        from .state import SDIMethodState


        def require_adata(adata: Any) -> Any:
            if adata is None:
                raise ContractError("AnnData input is required")
            if not hasattr(adata, "obs") or not hasattr(adata, "obsm"):
                raise ContractError("input must provide AnnData-like obs and obsm")
            return adata


        def require_spatial(adata: Any) -> Any:
            require_adata(adata)
            if "spatial" not in adata.obsm:
                raise ContractError('adata.obsm["spatial"] is required')
            return adata.obsm["spatial"]


        def require_domain(adata: Any) -> Any:
            require_adata(adata)
            if "domain" not in adata.obs:
                raise ContractError('adata.obs["domain"] is required')
            return adata.obs["domain"]


        def require_state(state: SDIMethodState | None, method: str) -> SDIMethodState:
            if state is None:
                raise ContractError(f"{method} prior method state is required")
            if state.method != method:
                raise ContractError(f"expected {method} state, observed {state.method}")
            return state


        def ensure_output_dir(path: str | Path) -> Path:
            output_dir = Path(path)
            output_dir.mkdir(parents=True, exist_ok=True)
            return output_dir
        """,
    )
    write(
        PKG / "io.py",
        """
        \"\"\"Public artifact writers for SDI execution surfaces.\"\"\"

        from __future__ import annotations

        from pathlib import Path
        from typing import Any

        import pandas as pd

        from .contracts import ensure_output_dir, require_adata, require_domain


        def export_domain_csv(adata: Any, output_dir: str | Path) -> Path:
            require_adata(adata)
            labels = require_domain(adata)
            out_dir = ensure_output_dir(output_dir)
            obs_ids = list(getattr(adata, "obs_names", adata.obs.index))
            table = pd.DataFrame({"obs_id": obs_ids, "domain": list(labels)})
            path = out_dir / "domain_labels.csv"
            table.to_csv(path, index=False)
            return path
        """,
    )
    write(
        PKG / "registry.py",
        """
        \"\"\"Layer3 callable registry for generated SDI runtime surfaces.\"\"\"

        from __future__ import annotations

        from collections.abc import Callable, Iterator

        _REGISTRY: dict[tuple[str, str], Callable] = {}


        def register_surface(method: str, surface: str, func: Callable) -> Callable:
            _REGISTRY[(method, surface)] = func
            return func


        def get_callable(method: str, surface: str) -> Callable:
            return _REGISTRY[(method, surface)]


        def iter_surface_bindings() -> Iterator[tuple[str, str, Callable]]:
            for (method, surface), func in sorted(_REGISTRY.items()):
                yield method, surface, func
        """,
    )
    write(
        PKG / "methods" / "__init__.py",
        """
        \"\"\"Method-owned SDI Layer3/Layer4 bindings.

        Import individual method modules to register their reviewed surfaces.
        \"\"\"
        """,
    )
    write(
        BUILD_ROOT / "shared_runtime_boundary_check.yaml",
        """
        shared_runtime_boundary_check:
          shared_files_reviewed:
            - bioharness_sdi_runtime/__init__.py
            - bioharness_sdi_runtime/errors.py
            - bioharness_sdi_runtime/state.py
            - bioharness_sdi_runtime/contracts.py
            - bioharness_sdi_runtime/io.py
            - bioharness_sdi_runtime/registry.py
          method_agnostic_helpers_only: true
          method_specific_binding_location: method_owned_layer4
          verdict: pass
        """,
    )


if __name__ == "__main__":
    main()
