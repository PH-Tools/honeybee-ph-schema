"""PH core extension schema models."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class PhCertification(BaseModel):
    """Certification shape used by PHI/Phius payloads."""

    model_config = ConfigDict(extra="allow")

    standard: Literal["PHI", "PHIUS", "ENERPHIT", "NONE"] | None = None
    program_name: str | None = None


class PhSpace(BaseModel):
    """Minimal PH space payload envelope for contract-first evolution."""

    model_config = ConfigDict(extra="allow")

    id: str | None = None
    tfa: float | None = None
    icfa: float | None = None
    volume: float | None = None


class PhRoomProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str = Field(default="PhRoomProperties")
    spaces: list[PhSpace] = Field(default_factory=list)
    certification: PhCertification | None = None


class PhFaceProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str = Field(default="PhFaceProperties")
    assembly_id: str | None = None


class PhApertureProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str = Field(default="PhApertureProperties")
    window_type_id: str | None = None
