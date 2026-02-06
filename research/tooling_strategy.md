# Tooling Strategy – Developer MCP

## Purpose
This document defines the Model Context Protocol (MCP) servers used to
support developer productivity during the build phase of Project Chimera.
These tools assist humans and AI copilots during design, coding, and review.

---

## Selected MCP Servers

### 1. filesystem-mcp
**Purpose:** Enable structured access to project files.

**Capabilities:**
- Read/write markdown specs
- Update configuration files
- Create and modify agent rules

**Usage Context:**
- Editing `/specs`, `/research`, and `.cursor/rules`
- Maintaining versioned documentation

**Risk & Controls:**
- Restricted to project root
- No destructive operations without confirmation

---

### 2. git-mcp
**Purpose:** Provide version control awareness and automation.

**Capabilities:**
- Read git status and diffs
- Create commits with structured messages
- Assist in PR preparation

**Usage Context:**
- Spec-driven development
- Traceability between specs and code

---

### 3. shell-mcp
**Purpose:** Execute local commands in a controlled manner.

**Capabilities:**
- Run tests
- Execute linters or validators
- Verify repository health

**Usage Context:**
- Pre-commit checks
- Validation of generated artifacts

---

## Out of Scope
- No production credentials
- No direct access to client systems
- No runtime data manipulation
