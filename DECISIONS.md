# Architecture and Technical Decisions

This document records important technical and architectural decisions made during development.

The purpose is to preserve the reasoning behind decisions so that the project can evolve without losing its original design principles.

---

## Decision 001 — Local-First Architecture

**Status:** Accepted

### Decision

The Personal AI Agent will follow a local-first architecture.

The Agent should primarily operate on the user's computer, with optional cloud services when useful and authorized.

### Reason

A personal Agent may work with private files, memories, projects, and other sensitive information.

Keeping important data and capabilities local by default improves privacy and user control.

### Consequence

The architecture must clearly distinguish between:

* local processing
* cloud processing
* optional external services

Cloud access should not become the default for every operation.

---

## Decision 002 — User Is the Highest Authority

**Status:** Accepted

### Decision

The user remains the highest authority over the Agent.

The Agent may suggest, plan, and request actions, but it must not independently grant itself additional authority.

### Reason

The purpose of a personal Agent is to help the user, not replace the user's control over the computer or personal information.

### Consequence

Permission and security systems must exist independently from the AI reasoning system.

---

## Decision 003 — AI Does Not Have Direct System Access

**Status:** Accepted

### Decision

The AI must not directly control protected system resources.

Actions should follow a controlled flow:

```text
AI
 ↓
REQUEST
 ↓
SECURITY POLICY
 ↓
PERMISSION GUARD
 ↓
ACTION GUARD
 ↓
TOOL
 ↓
VERIFICATION
```

### Reason

Giving an AI unrestricted access to the operating system would create unnecessary security and privacy risks.

### Consequence

System capabilities must be exposed through controlled tools.

---

## Decision 004 — Capability and Authority Are Separate

**Status:** Accepted

### Decision

Having a capability does not automatically mean the Agent has permission to use it.

```text
Capability ≠ Authority
```

### Reason

The Agent may become more capable over time, but increased capability should not automatically increase its authority.

### Consequence

Permission checks must occur before protected actions.

---

## Decision 005 — SQLite as the Planned Primary Database

**Status:** Accepted

### Decision

SQLite is planned as the primary local structured database.

### Reason

The Agent is local-first, and SQLite provides a simple, reliable local database without requiring a separate database server.

### Consequence

The main application data layer should be designed around a local database.

Cloud storage should not automatically replace the local primary database.

---

## Decision 006 — Google Drive for Optional Sync and Backup

**Status:** Accepted

### Decision

Google Drive may be used for synchronization or backup when explicitly authorized.

### Reason

The Agent may eventually need to work across multiple devices and protect against local data loss.

### Consequence

Google Drive should remain an optional external service rather than becoming the only storage location.

---

## Decision 007 — Replaceable AI Providers

**Status:** Accepted

### Decision

The Agent should not be tightly coupled to one AI provider.

### Reason

AI providers can change in:

* capability
* price
* availability
* privacy characteristics
* API design

The project should remain flexible.

### Consequence

The AI layer should eventually use an abstraction that allows different providers to be connected without redesigning the entire Agent.

---

## Decision 008 — Centralized Configuration

**Status:** Accepted

### Decision

Application configuration should be centralized through:

```text
.env
 ↓
config/settings.py
 ↓
application components
```

### Reason

If every component reads configuration independently, configuration logic becomes duplicated and difficult to maintain.

Centralizing configuration gives the application one clear configuration interface.

### Consequence

Application components should use the settings system rather than independently parsing `.env`.

---

## Decision 009 — `.env` Is Not Committed

**Status:** Accepted

### Decision

The local `.env` file must not be committed to Git.

### Reason

The file may eventually contain private configuration or secrets.

### Consequence

`.env` is ignored by Git, while `.env.example` provides a safe template.

---

## Decision 010 — Avoid Unnecessary Dependencies

**Status:** Accepted

### Decision

Libraries should only be added when they solve a real project need.

### Reason

Every dependency adds maintenance, security, and compatibility considerations.

The Python standard library should be preferred when it provides a practical solution.

### Consequence

New dependencies should have a clear purpose.

For example, `python-dotenv` was added because the project uses `.env` configuration and Python does not automatically load `.env` files.

---

## Decision 011 — Documentation Is Part of Development

**Status:** Accepted

### Decision

Important architectural, security, and technical decisions should be documented.

### Reason

The project is intended to grow over a long period.

Without documentation, important reasoning can be forgotten and future changes may conflict with the original architecture.

### Consequence

Important decisions should be recorded in this file and related documentation should be updated when necessary.

---

## Future Decisions

New important decisions should be added using a similar structure:

```text
Decision XXX — Title

Status:
Accepted / Proposed / Rejected / Superseded

Decision:

Reason:

Consequence:
```

Decisions should explain not only **what** was chosen, but also **why** it was chosen.
