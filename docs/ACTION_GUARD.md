# Action Guard

## Purpose

The ActionGuard is the security gate immediately before an action can continue toward execution.

The AI must not directly execute tools.

The AI can request an action, but the ActionGuard checks whether that action is allowed to continue.

## Responsibility

The ActionGuard currently checks the PermissionState.

- ALLOW → action can continue
- ASK → action cannot continue yet
- DENY → action is blocked

## Security Flow

AI
→ Action
→ PermissionManager
→ PermissionState
→ ActionGuard
→ Tool

Only an ALLOW result can pass the current ActionGuard.

## Important Security Principle

The AI does not have direct authority to execute an action.

The ActionGuard provides a security boundary between the Agent's decision-making system and the tools that can perform real actions.

## Current Behavior

```text
ALLOW → True
ASK   → False
DENY  → False