# honeybee-ph-schema

Schema contracts for Honeybee-PH HBJSON extensions.

This repository is intentionally separate from `honeybee_ph` runtime code. It publishes machine-readable schema artifacts (OpenAPI and JSON Schema) that downstream consumers can use for code generation and contract testing.

## Goals

- Mirror runtime serialization behavior from `honeybee_ph` without changing runtime APIs.
- Publish versioned schema artifacts for PH core, PH-HVAC, and PH-Energy extension payloads.
- Detect schema drift in CI and classify compatibility impact.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
python scripts/build_schemas.py
pytest
```

## Artifacts

Generated files are committed under `schemas/`:

- `schemas/ph-model.json`
- `schemas/ph-model.yaml`
- `schemas/ph-hvac.json`
- `schemas/ph-hvac.yaml`
- `schemas/ph-energy.json`
- `schemas/ph-energy.yaml`
- `schemas/model_json_schema.json`
- `schemas/compatibility-matrix.json`

## CI and Release

- `ci.yml` validates tests and fails if generated artifacts are stale.
- `release.yml` builds artifacts on tags and attaches schema files to GitHub Releases.
- `sync-from-runtime.yml` listens for `repository_dispatch` events from `honeybee_ph` releases and opens update PRs.
