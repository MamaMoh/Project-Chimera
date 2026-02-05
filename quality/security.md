# Security Policy
Purpose: Define secrets handling, dependency scanning, and threat model notes.

## Requirements
- Secrets must never be committed to the repository.
- All credentials are injected via environment variables.
- Dependency scanning must run in CI.

## Scope
- Python dependencies and Docker images.
