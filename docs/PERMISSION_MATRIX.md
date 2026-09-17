# Permission Matrix

The permission matrix describes how the Personal AI Agent should evaluate actions.

## Fields

### Action

The operation the agent wants to perform.

Examples:
- Read a file
- Write a file
- Delete a file
- Send data externally

### Permission

The resulting permission state:

- ALLOW
- ASK
- DENY

### Risk

The estimated risk of the action:

- LOW
- MEDIUM
- HIGH

### Confirmation

Defines whether the user must explicitly confirm the action.

### Verification

Defines whether the system must verify that the requested action or result actually occurred.

## Example

| Action | Permission | Risk | Confirmation | Verification |
|---|---|---|---|---|
| Read public file | ALLOW | LOW | No | Yes |
| Read private file | ASK | MEDIUM | Yes | Yes |
| Send sensitive data externally | DENY | HIGH | No | Yes |
| Delete important user data | ASK | HIGH | Yes | Yes |

These examples describe the concept only. The final rules will be implemented as the security policy develops.

## Architecture

The permission matrix connects:

Data Classification
    ↓
Action
    ↓
Risk Level
    ↓
Permission State
    ↓
Confirmation
    ↓
Verification

The matrix describes the rules. A future Permission Manager will evaluate and enforce them.