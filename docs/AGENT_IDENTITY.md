# Agent Identity

## Purpose

Agent Identity defines the technical identity and current authorization-related state of the Personal AI Agent.

The purpose is to give the system a clear answer to:

* Which agent is this?
* What is the agent's current status?
* Which tools are allowed for this agent?
* Which tools are explicitly denied?

Agent Identity is part of the security foundation of the Personal AI Agent.

---

## Identity Structure

The current identity contains four main parts:

```text
AgentIdentity
│
├── assistant_id
├── status
├── allowed_tools
└── denied_tools
```

### 1. Assistant ID

`assistant_id` uniquely identifies the agent.

Example:

```text
personal-agent-001
```

The ID can later be used by:

* audit logs
* security events
* device management
* multi-device systems
* debugging
* future multi-agent support

The Assistant ID identifies the agent. It does not represent the agent's personality or intelligence.

---

## 2. Agent Status

Agent status describes whether the agent is currently active or restricted.

Current statuses:

```text
ACTIVE
DISABLED
LOCKED
```

### ACTIVE

The agent is operational and can continue through the normal security process.

### DISABLED

The agent has been disabled and should not perform actions.

### LOCKED

The agent is in a restricted security state and should not perform actions until the lock condition is resolved.

Agent status is separate from action permission.

For example:

```text
Agent Status = ACTIVE
```

does not automatically mean:

```text
Action = ALLOWED
```

The action must still pass the security system.

---

## 3. Allowed Tools

`allowed_tools` contains tools that the agent is permitted to use.

Example:

```text
file_read
web_search
```

Having a tool in the allowed list does not automatically authorize every action performed through that tool.

For example:

```text
file_write ∈ allowed_tools
```

does not mean the agent can automatically write to every file.

The action must still pass the appropriate permission and security checks.

This separation is important:

```text
Tool exists
    ≠
Tool is allowed
    ≠
Every action through the tool is allowed
```

---

## 4. Denied Tools

`denied_tools` contains tools that are explicitly prohibited for the agent.

Example:

```text
system_command
change_permission
disable_security
```

Explicit denial provides a clear security boundary for dangerous capabilities.

The agent should never assume that a tool is safe simply because it exists in the software.

---

## Authorization Ambiguity

A tool must not exist in both `allowed_tools` and `denied_tools`.

For example:

```text
Allowed:
    file_read

Denied:
    file_read
```

This creates an ambiguous authorization state.

The current implementation rejects this configuration.

Conceptually:

```text
allowed_tools ∩ denied_tools
            ↓
        must be empty
```

If an overlap exists, the identity configuration raises an error instead of choosing an arbitrary result.

This follows the project's security principle:

> Ambiguous security configuration should fail closed.

---

## Separation of Responsibilities

Agent Identity describes the agent.

It does not execute tools.

It does not decide whether a specific action is safe.

It does not replace the Permission Manager.

It does not replace the Action Guard.

The intended architecture is:

```text
Agent Identity
      ↓
Permission System
      ↓
Action Classification
      ↓
Risk Evaluation
      ↓
Confirmation / Verification
      ↓
Action Guard
      ↓
Tool
```

Each component has a separate responsibility.

This reduces the chance that one component becomes responsible for the entire security system.

---

## Relationship With Security

Agent Identity provides information that future security components can use.

For example:

```text
Agent Identity
      │
      ├── Is the agent active?
      │
      ├── Is this tool allowed?
      │
      └── Is this tool explicitly denied?
      │
      ↓
Security checks
```

However, Agent Identity does not bypass the existing security architecture.

Even an allowed tool must still pass the relevant permission, risk, confirmation, verification, and action-guard checks.

---

## Current Scope

Day 31 intentionally implements only the identity foundation.

The current implementation does not yet provide:

* persistent identity storage
* cryptographic identity
* device authentication
* multi-device identity synchronization
* automatic identity recovery
* complete integration with ActionGuard
* complete integration with PermissionManager

These can be added later when the roadmap requires them.

The goal of Day 31 is to establish a clean and understandable identity foundation without unnecessarily expanding the system.

---

## Security Principles

The Agent Identity design follows these principles:

### 1. Identity does not equal authority

Knowing which agent is acting does not automatically give that agent permission to perform an action.

### 2. Tool availability does not equal authorization

A tool can exist in the software without being available to the agent.

### 3. Explicit denial matters

Dangerous capabilities can be explicitly denied rather than relying only on the absence of an allow rule.

### 4. Ambiguity fails closed

A tool cannot simultaneously be allowed and denied.

### 5. Security responsibilities remain separated

Agent Identity, Permission Management, Action Classification, Confirmation, Security Boundary, and Action Guard remain separate components.

---

## Tests

Day 31 adds tests for:

* default agent identity
* custom allowed and denied tools
* invalid overlapping tool permissions
* agent status values

The complete project test suite passes after implementing Agent Identity.

Current test result:

```text
48 passed
```

This confirms that the new identity foundation works without breaking the existing project functionality.

---

## Future Direction

As the Personal AI Agent becomes more capable, Agent Identity may become connected with:

```text
Agent Identity
      ↓
Device Identity
      ↓
User Identity / Ownership
      ↓
Permission System
      ↓
Security Policy
      ↓
Tool Authorization
      ↓
Audit Log
```

These integrations should be added carefully.

The core principle remains:

> Intelligence may grow. Authority does not grow automatically.
