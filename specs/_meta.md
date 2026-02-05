# Specs Meta
Purpose: Define how specs are written, reviewed, and enforced.

## Spec Types
- Functional: user-facing behavior and acceptance criteria
- Technical: architecture constraints, integrations, and NFRs
- Integration: third-party contracts and failure handling

## Required Sections (per spec)
- Title and scope
- Goals and non-goals
- Requirements (FR/NFR)
- Acceptance criteria
- Risks and mitigations
- Traceability references

## Ownership and Approval
- Owner: feature lead or system architect
- Reviewers: security, platform, and product
- Status: draft | reviewed | approved | superseded

## Versioning
- Changes are tracked in git and referenced in ADRs when architectural impact occurs.
- Superseded specs must link to their replacements.

## Validation
- Specs must pass `spec.schema.json` validation.
- CI blocks changes without an approved spec reference.
