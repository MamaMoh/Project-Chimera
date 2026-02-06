# Conflict Resolution

**Purpose:** When agents or rules disagree (e.g. campaign goal vs. safety, or two different policy clauses), this document defines the precedence order and the workflow to resolve disputes. The goal is to avoid arbitrary or inconsistent behaviour and to escalate to humans when the system cannot decide safely.

**Context:** In a multi-agent system, the Planner, Worker, and Judge may each apply different constraints (specs, policies, acceptance criteria). Conflicts can also arise between `AGENTS.md` and campaign-specific instructions. Precedence and tie-break rules ensure a single, predictable outcome.

---

## Precedence Order

When two or more rules or outputs conflict, apply them in this order (higher number wins; 1 is highest authority):

| Order | Source | Explanation |
|-------|--------|-------------|
| 1 | **AGENTS.md policies** | Central governance: MCP-only, disclosure, HITL thresholds, data handling. No agent may override these. |
| 2 | **Legal and platform constraints** | Laws, ToS, and platform rules (e.g. no hate speech, no unauthorised financial advice). |
| 3 | **SRS and spec requirements** | `specs/functional.md`, `specs/technical.md`, and other formal specs (FR/NFR). |
| 4 | **Planner acceptance criteria** | Criteria attached to the current Task. They must not contradict 1–3. |
| 5 | **Worker execution preferences** | Implementation choices (e.g. format, retry strategy) that do not affect policy or spec. |

Example: If a campaign goal says “post every hour” but the platform rate limit (2) or AGENTS.md (1) restricts frequency, the restriction wins and the Planner or Orchestrator should adapt the plan (e.g. reduce cadence or escalate).

---

## Tie-Break Rules

When precedence does not clearly separate two options, use these principles:

- **Safety wins over performance.** Prefer the option that avoids harm, policy violation, or reputational risk even if it is slower or less optimal.
- **Compliance wins over growth.** Prefer the option that satisfies legal and platform constraints over the one that maximises engagement or reach.
- **Human reviewer wins over Judge on edge cases.** When the Judge has escalated to HITL, the human’s approve/reject decision is final for that item. The Judge does not override the human.

---

## Dispute Workflow

When a conflict is detected (e.g. Judge sees that acceptance criteria and policy disagree, or Planner cannot satisfy both campaign and safety):

1. **Identify** the conflicting rule or output. State which two (or more) sources disagree and how (e.g. “Campaign asks for medical tip; AGENTS.md forbids medical advice”).
2. **Compare against precedence order.** Apply the table above. If one source is higher, follow it and log the resolution (e.g. in traces or audit).
3. **If unresolved,** do not guess. Escalate to HITL with a short summary: what was requested, what constraint blocked it, and which sources conflicted. A human can then decide or update policy/spec.

Agents must not invent a compromise that is not explicitly allowed by 1–3 (e.g. “partial medical advice”). When in doubt, escalate.

---

## References

- `agents/AGENTS.md` – Top of precedence; escalation and policy conflict.
- `specs/functional.md` – Spec requirements (order 3).
- `research/architecture_strategy.md` – §3 (HITL flow for escalation).
- `hitl/README.md` – Approval queue and human review.
