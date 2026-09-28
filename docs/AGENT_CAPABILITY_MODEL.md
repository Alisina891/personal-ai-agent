# Agent Capability Model

## Purpose

The Agent Capability Model defines what capabilities the Agent currently has and what capabilities are unavailable.

The model allows the Agent to answer:

- What can I do?
- What can I NOT do?

## Components

### AgentCapability

`identity/agent_capability.py`

Defines the known capabilities of the Agent.

Current capabilities:

- FILE_READ
- WEB_SEARCH
- VOICE_INPUT
- IMAGE_ANALYSIS
- SYSTEM_COMMAND
- EMAIL_SEND

### CapabilityModel

`identity/capability_model.py`

Stores the capabilities currently available to the Agent.

It provides:

- `can()` — checks whether a capability is available.
- `cannot()` — checks whether a capability is unavailable.

## Security Principle

Unknown or unavailable capabilities must not be treated as available.

The model follows a fail-closed approach:

```text
Unknown / unavailable
        ↓
Not available