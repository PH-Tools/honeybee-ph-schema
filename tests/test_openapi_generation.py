from pathlib import Path

from honeybee_ph_schema.build_schemas import build_all


def test_openapi_generation_writes_expected_files() -> None:
    build_all()
    root = Path(__file__).resolve().parents[1]
    expected = [
        "schemas/ph-model.json",
        "schemas/ph-model.yaml",
        "schemas/ph-hvac.json",
        "schemas/ph-hvac.yaml",
        "schemas/ph-energy.json",
        "schemas/ph-energy.yaml",
        "schemas/model_json_schema.json",
        "schemas/compatibility-matrix.json",
    ]
    for rel in expected:
        assert (root / rel).exists(), f"Missing generated artifact: {rel}"
