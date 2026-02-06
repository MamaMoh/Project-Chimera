# Feature Specification: Core Swarm Orchestration

**Feature Branch**: `001-main`  
**Created**: 2026-02-04  
**Status**: Draft  
**Input**: User description: "main"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - End-to-End Task Orchestration (Priority: P1)

As a network operator, I need the system to take a goal and produce a validated decision through the Planner, Worker, and Judge flow so that campaigns can run safely.

**Why this priority**: This is the minimal viable orchestration loop that enables all autonomous work.

**Independent Test**: Can be fully tested by submitting a single goal and observing a decision output without external integrations.

**Acceptance Scenarios**:

1. **Given** a valid goal, **When** the orchestration loop runs, **Then** a decision is produced with an approval state.
2. **Given** a valid goal, **When** the orchestration loop runs, **Then** the decision includes a rationale and timestamp.

---

### User Story 2 - Human Review Escalation (Priority: P2)

As a human reviewer, I need escalated outputs routed for review so that low-confidence or sensitive actions are not published automatically.

**Why this priority**: Human oversight is required to satisfy safety and governance rules.

**Independent Test**: Can be tested by forcing a low-confidence result and verifying escalation behavior.

**Acceptance Scenarios**:

1. **Given** a low-confidence result, **When** the Judge evaluates it, **Then** the decision is escalation for review.

---

### User Story 3 - Policy-Aligned Execution (Priority: P3)

As a governance operator, I need agent actions to respect MCP-only execution and policy constraints so that external actions remain auditable.

**Why this priority**: Prevents unsafe direct API usage and enforces traceability.

**Independent Test**: Can be tested by validating that action pathways reference MCP tools only.

**Acceptance Scenarios**:

1. **Given** an action request, **When** it is executed, **Then** the pathway references MCP tools rather than direct external APIs.

---

### Edge Cases

- What happens when a required resource is missing from the task context?
- How does the system handle a task that repeatedly fails validation?
- What happens when the global state changes between execution and review?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST generate a task from a goal with acceptance criteria.
- **FR-002**: System MUST execute a task and return a structured result.
- **FR-003**: System MUST evaluate results and output an approve, reject, or escalate decision.
- **FR-004**: System MUST include confidence scoring in each result.
- **FR-005**: System MUST enforce MCP-only external actions for all agent outputs.

### Key Entities *(include if feature involves data)*

- **Task**: A unit of work with type, priority, context, and acceptance criteria.
- **Result**: The output of task execution with confidence and artifacts.
- **Decision**: The Judge outcome with rationale and state version.
- **Policy**: Governance constraints applied during review.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of tasks produce a decision with rationale and timestamp.
- **SC-002**: 100% of results include a confidence score between 0.0 and 1.0.
- **SC-003**: Escalation occurs for all outputs below the defined confidence threshold.
- **SC-004**: No external actions are executed outside MCP tool pathways.
