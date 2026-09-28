# Tool Authorization

## Purpose

Tool Authorization determines whether a specific tool is authorized for the Personal AI Agent.

The purpose is to create a clear separation between:

* the identity of the agent
* which tools the agent may use
* whether a specific action is permitted
* whether an action may actually execute

Tool Authorization is one layer of the security architecture.

---

## Basic Flow

The current architecture is:

```text
Agent Identity
      ↓
Tool Authorization
      ↓
Permission System
      ↓
Action Guard
      ↓
Tool Execution
```

Each layer has a different responsibility.

---

## What Tool Authorization Checks

Tool Authorization answers one specific question:

> Is this tool authorized for this agent?

For example:

```text
Allowed Tools:

file_read
web_search
```

A request to use:

```text
file_read
```

returns:

```text
ALLOW
```

A request to use:

```text
system_command
```

returns:

```text
DENY
```

An unknown tool also returns:

```text
DENY
```

---

## Authorization Decision

The current decision process is:

```text
Tool requested
      ↓
Is the tool explicitly denied?
      │
   YES → DENY
      │
     NO
      ↓
Is the tool explicitly allowed?
      │
   YES → ALLOW
      │
     NO
      ↓
    DENY
```

Explicit denial is checked first.

The identity model also prevents a tool from being placed in both the allowed and denied collections.

---

## Fail-Closed Behavior

Unknown tools are denied by default.

For example, if the agent has:

```text
allowed_tools = {
    "file_read"
}
```

and requests:

```text
"camera"
```

the result is:

```text
DENY
```

The system does not assume that a new or unknown tool is safe.

This follows the project's security principle:

> Unknown capabilities should not automatically receive authority.

This is especially important as the project grows.

If a new tool is added later, the tool should require explicit authorization before the agent can use it.

---

## Separation From Action Permission

Tool Authorization does not replace the existing Permission System.

These are different questions.

### Tool Authorization

```text
Can the agent use this tool?
```

### Permission System

```text
Is this particular action permitted?
```

### Action Guard

```text
Can this action actually execute?
```

For example:

```text
Agent
  ↓
Is file_write authorized?
  ↓
YES
  ↓
Is writing this particular file permitted?
  ↓
Security checks
  ↓
Confirmation if required
  ↓
ActionGuard
  ↓
Execution
```

Therefore:

> Being authorized to use a tool does not mean every action performed through that tool is automatically allowed.

---

## Responsibility of `ToolAuthorization`

The `ToolAuthorization` component is intentionally small.

Its responsibility is only to check tool authorization.

It does not:

* execute tools
* classify actions
* determine risk
* request confirmation
* verify results
* change permissions
* bypass the Action Guard
* access protected files

Keeping this responsibility small makes the security architecture easier to understand and maintain.

---

## Relationship With Agent Identity

Tool Authorization receives an `AgentIdentity`.

The identity contains:

```text
AgentIdentity
│
├── assistant_id
├── status
├── allowed_tools
└── denied_tools
```

Tool Authorization uses the tool lists to make its decision.

Conceptually:

```text
AgentIdentity
      │
      ├── allowed_tools
      │
      └── denied_tools
             │
             ↓
      ToolAuthorization
             │
             ↓
       ALLOW / DENY
```

---

## Security Principle

The system follows:

```text
Tool exists
    ≠
Tool is authorized
```

and:

```text
Tool is authorized
    ≠
Every action through that tool is allowed
```

This separation prevents the agent's authority from automatically expanding just because new capabilities are added to the software.

---

## Tests

Day 32 adds tests for:

1. An explicitly allowed tool is authorized.
2. An explicitly denied tool is not authorized.
3. An unknown tool is not authorized.

The existing unauthorized-tool security test also remains in the project.

The complete test suite passes after implementing Tool Authorization.

Current result:

```text
51 passed
```

---

## Future Integration

Tool Authorization will later be connected with the broader security architecture.

A future flow may look like:

```text
User Request
      ↓
Agent Identity
      ↓
Tool Authorization
      ↓
Action Classification
      ↓
Data Classification
      ↓
Risk Evaluation
      ↓
Permission Manager
      ↓
Confirmation Manager
      ↓
Security Boundary
      ↓
Action Guard
      ↓
Tool
      ↓
Verification
      ↓
Audit Log
```

The exact integration should be introduced only when the roadmap reaches those components.

---

## Design Principle

Tool Authorization follows the project's central security principle:

> Intelligence may grow. Authority does not grow automatically.

Adding a new capability to the agent should not automatically give the agent permission to use it.
