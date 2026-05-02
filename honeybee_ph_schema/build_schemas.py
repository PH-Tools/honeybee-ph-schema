"""Generate OpenAPI and JSON Schema artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from honeybee_ph_schema.compatibility import CompatibilityRecord
from honeybee_ph_schema.model import OpenApiDocument, OpenApiInfo, PhModelEnvelope
from honeybee_ph_schema.ph_energy import PhEnergyProperties
from honeybee_ph_schema.ph_hvac import PhHvacProperties

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _build_openapi(schema_name: str, schema_dict: dict, version: str) -> dict:
    doc = OpenApiDocument(
        info=OpenApiInfo(title=schema_name, version=version),
        components={"schemas": {schema_name: schema_dict}},
    )
    return doc.model_dump(exclude_none=True)


def build_all(version: str = "0.1.0") -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)

    model_schema = PhModelEnvelope.model_json_schema()
    hvac_schema = PhHvacProperties.model_json_schema()
    energy_schema = PhEnergyProperties.model_json_schema()

    model_openapi = _build_openapi("PhModelEnvelope", model_schema, version)
    hvac_openapi = _build_openapi("PhHvacProperties", hvac_schema, version)
    energy_openapi = _build_openapi("PhEnergyProperties", energy_schema, version)

    _write_json(SCHEMAS / "model_json_schema.json", model_schema)
    _write_json(SCHEMAS / "ph-model.json", model_openapi)
    _write_yaml(SCHEMAS / "ph-model.yaml", model_openapi)
    _write_json(SCHEMAS / "ph-hvac.json", hvac_openapi)
    _write_yaml(SCHEMAS / "ph-hvac.yaml", hvac_openapi)
    _write_json(SCHEMAS / "ph-energy.json", energy_openapi)
    _write_yaml(SCHEMAS / "ph-energy.yaml", energy_openapi)

    compatibility = {
        "records": [
            CompatibilityRecord(
                runtime_version="unbound",
                schema_version=version,
                status="exact-match",
            ).to_dict()
        ]
    }
    _write_json(SCHEMAS / "compatibility-matrix.json", compatibility)
