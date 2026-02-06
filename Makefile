SHELL := /bin/sh

.PHONY: setup test spec-check test-docker

setup:
	@if command -v uv >/dev/null 2>&1; then uv sync; \
	else python -m pip install -U pip && python -m pip install pytest python-dotenv requests; fi

test:
	python -m pytest

test-docker:
	docker build -t project-chimera-test .
	docker run --rm project-chimera-test

spec-check:
	@python - <<'PY'
from pathlib import Path
required = [
    "specs/_meta.md",
    "specs/functional.md",
    "specs/technical.md",
    "specs/openclaw_integration.md",
    "specs/traceability.md",
]
missing = [p for p in required if not Path(p).exists()]
if missing:
    raise SystemExit(f"Missing required spec files: {missing}")
print("Spec check passed.")
PY
