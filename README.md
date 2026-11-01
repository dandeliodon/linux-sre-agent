# Linux SRE Agent

[![CI](https://github.com/dandeliodon/linux-sre-agent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dandeliodon/linux-sre-agent/actions/workflows/ci.yml)

An agent that watches a Linux server: it detects incidents, diagnoses them with evidence from
logs, proposes a fix, and applies it **only after human approval**. Then it verifies recovery
and writes an incident report.

> **Status:** early development. The project scaffolding and CI are in place; the agent itself
> is not built yet.

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.

```bash
uv sync               # create .venv and install dependencies from uv.lock
uv run ruff check     # lint
uv run ruff format    # format
uv run mypy           # type check (strict)
uv run pytest         # tests
```

## Design decisions

Architecture decision records are in [`docs/adr/`](docs/adr/).
