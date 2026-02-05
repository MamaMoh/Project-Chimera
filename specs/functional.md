# Functional Specs
Purpose: Define user-facing behavior and acceptance criteria.

## Scope
This file captures functional requirements for Project Chimera features.

## Requirements
- FR-1.0: The system SHALL support persona instantiation via `SOUL.md` with backstory, voice/tones, values, and directives.
- FR-1.1: The system SHALL implement hierarchical memory retrieval (short-term + long-term) before reasoning steps.
- FR-1.2: The system SHALL support dynamic persona evolution by summarizing successful interactions into long-term memory.
- FR-2.0: The system SHALL poll configured MCP Resources for updates.
- FR-2.1: The system SHALL semantically filter ingested content and only trigger tasks above a relevance threshold.
- FR-2.2: The system SHALL detect trends via a background worker and generate trend alerts.
- FR-3.0: The system SHALL generate multimodal content via MCP tools for text, image, and video.
- FR-3.1: The system SHALL enforce character consistency via reference IDs or LoRA in image generation.
- FR-3.2: The system SHALL implement tiered video generation based on priority and budget.
- FR-4.0: The system SHALL execute all social actions via MCP tools only.
- FR-4.1: The system SHALL support a bi-directional interaction loop (ingest → plan → generate → act → verify).
- FR-5.0: Each agent SHALL be assigned a unique non-custodial wallet via AgentKit.
- FR-5.1: The system SHALL support on-chain actions (transfer, deploy token, balance) via AgentKit.
- FR-5.2: A CFO Judge SHALL enforce budget limits and flag anomalies.
- FR-6.0: The system SHALL implement Planner, Worker, and Judge as decoupled services with queues.
- FR-6.1: The Judge SHALL implement optimistic concurrency control before committing state.

## Non-Functional Requirements
- NFR-1.0: Each action SHALL include a confidence_score.
- NFR-1.1: The system SHALL route tasks by confidence thresholds (auto-approve, async approval, reject/retry).
- NFR-1.2: Sensitive topic filters SHALL trigger mandatory HITL review.
- NFR-2.0: The system SHALL use platform-native AI labeling features when available.
- NFR-2.1: The system SHALL disclose AI identity when asked directly.
- NFR-3.0: The system SHALL support at least 1,000 concurrent agents.
- NFR-3.1: High-priority interactions SHALL complete within 10 seconds (excluding HITL).

## Acceptance Criteria
- Persona config is loaded from `agents/personas/SOUL.md`.
- Resource polling triggers tasks only above relevance threshold.
- All external actions are routed through MCP tools.
- HITL receives low-confidence or sensitive outputs.
- Planner-Worker-Judge loop executes end-to-end with state checks.

## Out of Scope
- UI implementation details beyond required capabilities.
