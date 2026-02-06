# Project Chimera

**Autonomous AI Influencer System** – researches trends, generates content, and engages audiences with minimal human oversight.

---

## Document Information

- **Version:** 1.0.0  
- **Status:** Spec-driven; runtime logic not implemented.
- **Authority:** All behaviour is defined in `research/` and `specs/`; code follows those documents.

---

## Overview

Project Chimera is an **architecture-first** system. Development follows:

1. **Spec-Driven Development (SDD)** – Features and contracts are defined in `specs/` and `research/` before any implementation.
2. **Agentic Orchestration** – A Chief Agent (Orchestrator) coordinates Planner, Worker, and Judge services; see `research/architecture_strategy.md`.
3. **Robust Infrastructure** – PostgreSQL, Redis, Elasticsearch, Docker, GitHub Actions, and MCP Sense for telemetry (see §7–8 of the architecture strategy).

**Current state:** No runtime logic is implemented. Entrypoint (`main.py`), Orchestrator, Planner, Worker, Judge, and skills are **stubs only**. Tests are written to define the expected contracts and **fail by design** until the behaviour described in the research and spec documents is implemented.

---

## Where Everything Is Defined

| Concern | Primary document(s) |
|--------|----------------------|
| **Architecture, agent pattern, flow** | `research/architecture_strategy.md` |
| **Tooling and MCP (developer)** | `research/tooling_strategy.md` |
| **Functional requirements** | `specs/functional.md` |
| **Technical contracts** | `specs/technical.md` |
| **Agent governance** | `agents/AGENTS.md`, `agents/personas/SOUL.md` |
| **Skill contracts** | `skills/<skill_name>/README.md` and `schema.json` |
| **Quality** | `quality/testing.md`, `quality/security.md`, `quality/linting.md` |

---

## Project Goals

1. **Spec fidelity** – Every feature is specified in `specs/` and/or `research/` before implementation.
2. **Agentic orchestration** – Planner → Worker → Judge cycle with clear roles (see architecture strategy §2.3).
3. **Safety and traceability** – Human-in-the-loop (HITL) before publishing; MCP-only for external actions; MCP Sense for logging.
4. **Extensibility** – New skills and MCP tools integrate via defined contracts.

---

## Directory Structure (Aligned with Architecture Strategy)

- **`main.py`** – Entrypoint (stub; raises until implemented).
- **`orchestrator/`** – Chief Agent coordination (stub). See `research/architecture_strategy.md` §2.3–2.4.
- **`services/`** – Planner, Worker, Judge (stubs). Same document §2.3.
- **`skills/`** – Invokable agent abilities; each skill has a README and `schema.json`. §6.
- **`specs/`** – Spec-driven documentation and contracts.
- **`research/`** – Architecture and tooling strategy (source of truth for design).
- **`agents/`** – Governance (`AGENTS.md`) and personas (`personas/SOUL.md`).
- **`schemas/`** – Shared JSON schemas (e.g. task, result).
- **`policies/`** – Disclosure and sensitive-topics policy.
- **`tests/`** – Contract and policy tests; written to **fail** until logic is implemented.
- **`hitl/`** – Human-in-the-loop review (see architecture §3).
- **`memory/`**, **`mcp_servers/`** – Memory and MCP server contracts (see tooling strategy).

---

## Testing Strategy

- Tests reference FR/NFR IDs and enforce **contracts** (inputs, outputs, errors).
- **No logic is implemented yet** – tests are intended to **fail** until you implement the behaviour described in the research and spec documents.
- Run: `make test` or `uv run pytest tests/ -v`.
- See `quality/testing.md` for policy.

---

## Tooling and MCP

Developer tooling and MCP usage are defined in **`research/tooling_strategy.md`** (e.g. filesystem, git, shell MCPs). Runtime MCP servers (social, memory, commerce) are described in `mcp_servers/README.md`. All external actions must go through **MCP tools only** (FR-4.0; see `agents/AGENTS.md` when updated).

---

## CI/CD and Governance

- **CI:** GitHub Actions run on push/PR (`make setup`, `make spec-check`, quality checks, `make test`). See architecture strategy §8.
- **Governance:** `agents/AGENTS.md`, `policies/`, and HITL flow in `research/architecture_strategy.md` §3.

---

## Next Steps (from Architecture Strategy §9)

1. Stakeholder approval of architecture.
2. Define detailed API contracts in `specs/technical.md`.
3. Implement Chief Agent (Orchestrator) and Planner/Worker/Judge to satisfy tests and specs.
4. Set up Docker and PostgreSQL dev environment.
5. Connect MCP Sense telemetry.

---

## References

- `research/architecture_strategy.md` – Full architecture, diagrams, and decisions.
- `research/tooling_strategy.md` – Developer MCP and tooling.
- `specs/functional.md` – Functional requirements.
- Project Chimera SRS (in `docs/`).
