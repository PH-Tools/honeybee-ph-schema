"""PH-HVAC extension schema models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PhHvacProperties(BaseModel):
    """Placeholder envelope for PH-HVAC schema contract."""

    model_config = ConfigDict(extra="allow")

    type: str = Field(default="PhHvacProperties")
