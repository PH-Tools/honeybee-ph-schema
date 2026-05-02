#!/usr/bin/env python3
"""Generate OpenAPI and JSON Schema artifacts."""

from honeybee_ph_schema.build_schemas import build_all


if __name__ == "__main__":
    build_all()
