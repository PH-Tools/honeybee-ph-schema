"""PH-Energy extension schema models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PhEnergyProperties(BaseModel):
    """Placeholder envelope for PH-Energy schema contract."""

    model_config = ConfigDict(extra="allow")

    type: str = Field(default="PhEnergyProperties")
