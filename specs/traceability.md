# Traceability
Purpose: Map specs to tests and validation checks.

## Mapping

| Requirement | Evidence (tests, policies, docs) |
| --- | --- |
| FR-1.0 | `agents/personas/SOUL.md` |
| FR-1.1 | `memory/README.md` |
| FR-1.2 | `memory/README.md` |
| FR-2.0 | `research/architecture_strategy.md` |
| FR-2.1 | `research/architecture_strategy.md` |
| FR-2.2 | `tests/test_trend_fetcher.py` |
| FR-3.0 | `skills/README.md`, `skills/skill_download_youtube/schema.json`, `skills/skill_transcribe_audio/schema.json`, `skills/skill_post_social/schema.json` |
| FR-3.1 | `specs/technical.md` |
| FR-3.2 | `specs/technical.md` |
| FR-4.0 | `agents/AGENTS.md`, `skills/skill_post_social/README.md`, `skills/skill_post_social/schema.json` |
| FR-4.1 | `research/architecture_strategy.md` |
| FR-5.0 | `commerce/README.md` |
| FR-5.1 | `commerce/README.md` |
| FR-5.2 | `agents/roles.md` |
| FR-6.0 | `services/planner/README.md`, `services/worker/README.md`, `services/judge/README.md`, `specs/technical.md` |
| FR-6.1 | `architecture/adr/0001-initial-architecture.md`, `specs/technical.md` |
| NFR-1.0 | `agents/protocols.md` |
| NFR-1.1 | `hitl/README.md`, `specs/technical.md` |
| NFR-1.2 | `policies/sensitive-topics.md` |
| NFR-2.0 | `policies/disclosure.md` |
| NFR-2.1 | `agents/AGENTS.md` |
| NFR-3.0 | `specs/technical.md` |
| NFR-3.1 | `specs/technical.md` |

## Rules
- Every functional requirement must map to a test or policy check.
- Every test must reference a requirement ID.
