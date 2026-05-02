"""Top-level schema documents for OpenAPI emission."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from honeybee_ph_schema.ph import PhApertureProperties, PhFaceProperties, PhRoomProperties
from honeybee_ph_schema.ph_energy import PhEnergyProperties
from honeybee_ph_schema.ph_hvac import PhHvacProperties


class PhModelEnvelope(BaseModel):
    """Top-level extension payload mapping used in HBJSON properties."""

    model_config = ConfigDict(extra="allow")

    room: PhRoomProperties | None = None
    face: PhFaceProperties | None = None
    aperture: PhApertureProperties | None = None
    hvac: PhHvacProperties | None = None
    energy: PhEnergyProperties | None = None


class OpenApiInfo(BaseModel):
    title: str
    version: str


class OpenApiDocument(BaseModel):
    openapi: str = Field(default="3.1.0")
    info: OpenApiInfo
    paths: dict[str, dict] = Field(default_factory=dict)
    components: dict[str, dict]
