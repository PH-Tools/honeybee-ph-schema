"""Compatibility matrix helpers for runtime/schema version tracking."""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class CompatibilityRecord:
    runtime_version: str
    schema_version: str
    status: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
