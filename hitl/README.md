# Human-in-the-Loop (HITL)

**Purpose:** Define how human review is integrated into the Chimera flow before content is published or sensitive actions are committed. This directory holds the specification and future implementation of the approval queue and review criteria; no runtime logic is implemented here yet.

---

## Role in the Architecture

HITL is the **safety layer** described in **`research/architecture_strategy.md`** §3:

- The **Judge** produces a Decision (approve / escalate / reject).
- Content or actions that are **escalated** (or that meet certain risk levels) are sent to an **Approval Queue**.
- A **Human Operator** is notified (e.g. email/Slack), reviews the item, and either approves or rejects with feedback.
- On approval, the system can publish to social APIs; on rejection, feedback is returned for revision.
- Timeouts (e.g. 24 hours) can auto-expire pending items.

The sequence diagram in §3 of the architecture strategy illustrates Agent → Queue → Human → Social flow.

---

## Approval Gates (from Architecture Strategy §3)

| Stage | Trigger | Human action | Timeout |
|-------|---------|--------------|---------|
| Content generation | New content created | Review & approve | 24 hours |
| Publishing | Content ready to post | Final sign-off | 4 hours |
| Engagement reply | Automated response triggered | Pre-approve templates | N/A (template-based) |
| Agent update | Configuration change | Admin approval | 72 hours |

---

## Risk Levels and Responses

| Risk level | Example | Response |
|------------|---------|----------|
| CRITICAL | Potential policy violation | Block immediately; flag for human |
| HIGH | Controversial topic | Require human approval |
| MEDIUM | New engagement pattern | Template-based; log for review |
| LOW | Routine content | Auto-approve with monitoring |

---

## Implementation Status

- **Current:** Specification only. No queue or notification logic is implemented in this directory.
- **References:** `agents/AGENTS.md` (HITL thresholds), `research/architecture_strategy.md` §3, `specs/functional.md` (acceptance criteria for HITL).
