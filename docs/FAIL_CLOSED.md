# Fail Closed

## Purpose

The Agent must not automatically allow an action when the action is unknown or cannot be safely classified.

The security rule is:

UNKNOWN → DENY

## Why Fail Closed?

A security system should not assume that an unknown action is safe.

If the system does not understand an action, automatically allowing it could allow an unintended operation to continue.

Fail closed means that when the system cannot make a safe decision, it keeps the action blocked.

## Behavior

Known action:

Action
→ ActionType
→ PermissionManager
→ Rule Permission

Unknown action:

Action
→ UNKNOWN
→ PermissionManager
→ DENY

## Security Rule

An UNKNOWN action must never become ALLOW through a normal permission rule.

For example, even if a rule contains:

Action: UNKNOWN
Permission: ALLOW

PermissionManager returns:

DENY

This provides a security boundary between unknown actions and execution.

## Relationship With ActionClassifier

The ActionClassifier identifies the action type.

It does not decide whether the action is allowed.

If it cannot recognize an action, it returns:

ActionType.UNKNOWN

The PermissionManager then applies the fail-closed rule.

## Testing

Day 22 tests verify that:

- known actions still use their configured permission
- UNKNOWN actions are denied
- UNKNOWN cannot be allowed simply because a rule contains ALLOW

Current test suite result:

18 tests passed.