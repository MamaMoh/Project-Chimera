# Skills Layer

**Purpose:** Define invokable agent abilities (skills) and their **input/output contracts**. No runtime logic is implemented for most skills; behaviour is specified in each skill’s README and `schema.json`, and tests define the expected contracts and fail until implementation.

---

## Role in the Architecture

Skills are the building blocks used by the **Worker** (see **`research/architecture_strategy.md`** §2.2 and §6). The Content Generator and Engagement Manager sub-agents use skills to download video, transcribe audio, analyze trends, and post to social platforms. The diagram in §6 shows:

- Worker → `skill_download_video`, `skill_download_youtube`, `skill_transcribe_audio`, `skill_post_social` (and `skill_analyze_trends`) → Task Result.

All external actions (e.g. posting to Twitter, calling trend APIs) must go through **MCP tools only** (FR-4.0). Skills are the abstraction that the Worker calls; the actual I/O is done via MCP.

---

## Contract Rules

1. **Inputs and outputs** – Each skill has a `schema.json` (input contract) and, where applicable, an output contract described in the skill’s README. Tests in `tests/test_skills_interface.py` require that skill schemas define required inputs and, when the test is enabled, an **output_schema** or **output** for the response shape.
2. **MCP-only** – Skills do not call external APIs directly; they call MCP tools. See `agents/AGENTS.md` and `specs/functional.md` FR-4.0.
3. **Resources** – Each skill README describes required resources (e.g. API keys via env, MCP server config) and constraints (e.g. max duration, rate limits).

---

## Skills Registry

| Skill | Purpose | Input (required) | Status |
|-------|---------|------------------|--------|
| **skill_download_video** | Download video from YouTube, TikTok, Twitter | `url`, `platform` | Spec + schema only |
| **skill_download_youtube** | Download YouTube video (duration cap) | `url`, `max_duration_seconds` | Spec + schema only |
| **skill_transcribe_audio** | Transcribe audio to text segments | `audio_path`, `language` | Spec + schema only |
| **skill_post_social** | Publish content to Twitter, Instagram, Threads | `platform`, `text_content` | Spec + schema only |
| **skill_analyze_trends** | Analyze trends for a platform; return request_id, trends[], pagination, metrics, analysis | `platform` | Stub raises; tests fail until implemented |

Each skill directory contains:

- **README.md** – Full specification (overview, input/output contract, error codes, dependencies, integration points, performance, security). Aligned with the style used in the research and spec documents.
- **schema.json** – JSON Schema for the **input** contract. Output contract is described in the README and, when added, in schema or a separate output_schema.

---

## Implementation Status

- **Current:** No logic is implemented except stubs (e.g. `skill_analyze_trends` raises `NotImplementedError`). Tests in `tests/test_trend_fetcher.py` and `tests/test_skills_interface.py` define the expected response shape and **fail by design** until implementations satisfy the contracts in the READMEs and research docs.

---

## References

- `research/architecture_strategy.md` – §2.2 (Conceptual Agent Structure), §6 (Skill Layer Interaction), §7 (Directory structure).
- `specs/functional.md` – FR-2.2 (trends), FR-3.0/FR-4.0 (content, MCP-only).
- Each skill’s **README.md** – Authoritative contract and behaviour for that skill.
