# Skill: Analyze Trends

**Purpose:** Analyze trends for a given platform and return a contract-shaped response (request_id, trends array, pagination, metrics, analysis). No logic is implemented; this README and the tests define the contract.

---

## Role in the Architecture

This skill is used by the **Trend Fetcher** and **Content Generator** sub-agents (see **`research/architecture_strategy.md`** §2.2). It feeds trend data (topics, metrics, virality, content gaps, recommendations) into content planning and validation. The Worker invokes it as part of the skill layer (§6).

---

## Skill Information

| Field | Value |
|-------|--------|
| **Name** | skill_analyze_trends |
| **Version** | 1.0.0 |
| **Type** | Runtime Skill |
| **Category** | Content Acquisition / Research |

---

## Input Contract

- **Required:** `platform` (string, enum: `youtube` | `tiktok` | `twitter`).
- **Optional:** `options` with e.g. `limit`, `min_confidence`, `time_range_hours`.
- See **`schema.json`** in this directory for the full JSON Schema.

---

## Output Contract (To Be Implemented)

The implementation **must** return a single object with:

| Field | Type | Description |
|-------|------|-------------|
| **request_id** | string (UUID) | Unique id for the request. |
| **trends** | array | List of trend objects (see below). |
| **pagination** | object | At least `page`, `limit`, `total`, `has_more`. |
| **analysis** | object or null | When success: `confidence`, `content_gaps`, `recommendations`. When error: null. |
| **error** | object or null | When failure: `{ "code": "...", "message": "..." }`. When success: null. |

Each **trend** object must include:

- `trend_id`, `topic`, `platform`, `confidence_score`, `source`, `created_at`
- **metrics:** `views`, `likes`, `shares`, `velocity`
- **virality_score** (number)

Error responses must still include `request_id`, `trends` (empty array), `pagination`, and `error` with `code` (e.g. `INVALID_PLATFORM`) and `message`.

---

## Implementation Status

- **Current:** Stub only. `analyze_trends(platform, options)` raises `NotImplementedError`.
- **Tests:** `tests/test_trend_fetcher.py` and `tests/test_skills_interface.py` assert the full contract; they **fail** until this skill is implemented to satisfy the above and the test expectations.

---

## References

- `research/architecture_strategy.md` – §2.2, §6.
- `specs/functional.md` – FR-2.2 (detect trends, generate trend alerts).
- `tests/test_trend_fetcher.py` – Exact assertions for request_id, trends[], pagination, metrics, virality_score, analysis, error handling.
