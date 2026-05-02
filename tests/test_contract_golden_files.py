import json
from pathlib import Path

from honeybee_ph_schema.build_schemas import build_all


def test_generated_openapi_has_components() -> None:
    build_all()
    root = Path(__file__).resolve().parents[1]
    model_path = root / "schemas/ph-model.json"
    data = json.loads(model_path.read_text(encoding="utf-8"))
    assert data["openapi"] == "3.1.0"
    assert "components" in data
    assert "schemas" in data["components"]
