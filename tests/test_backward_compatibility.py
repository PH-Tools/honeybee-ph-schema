import json
from pathlib import Path

from honeybee_ph_schema.build_schemas import build_all


def test_compatibility_matrix_exists_and_has_record() -> None:
    build_all()
    root = Path(__file__).resolve().parents[1]
    matrix_path = root / "schemas/compatibility-matrix.json"
    data = json.loads(matrix_path.read_text(encoding="utf-8"))
    assert "records" in data
    assert len(data["records"]) >= 1
