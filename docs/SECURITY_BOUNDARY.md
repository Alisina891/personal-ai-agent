# Security Boundary

## Purpose

The Security Boundary defines capabilities that the AI must not access or execute directly.

The AI can request an action, but sensitive capabilities must pass through the security system before execution.

## Core Principle

AI intelligence does not automatically give the AI authority.

The user remains the final authority.

## Directly Forbidden Capabilities

The current security boundary forbids direct AI access to:

- file deletion
- file writing
- system commands
- changing permissions
- disabling security
- unrestricted access to sensitive data

## Security Flow

AI
→ Request
→ Security Boundary
→ Permission / Confirmation
→ ActionGuard
→ Tool
→ Execute

The AI must not bypass this flow.

## Important Distinction

If an action is not listed as forbidden by the Security Boundary, that does not automatically mean it is allowed.

Other security components still apply.

For example:

```text
normal_read
→ not forbidden by SecurityBoundary
→ other permission checks still apply