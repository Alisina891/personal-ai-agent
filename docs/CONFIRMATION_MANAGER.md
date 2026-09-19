# Confirmation Manager

## Purpose

The ConfirmationManager handles the user's confirmation before an action that requires confirmation is executed.

Its purpose is to make sure an action does not continue when the user has not confirmed it.

## Responsibility

The ConfirmationManager receives the user's confirmation decision.

- True → confirmation received
- False → confirmation not received

It does not execute the action.

## Security Flow

Action
→ PermissionManager
→ ASK
→ ConfirmationManager
→ User confirmation
→ Execute

If the user does not confirm:

Action
→ PermissionManager
→ ASK
→ ConfirmationManager
→ Stop

## Important Security Principle

Confirmation is separate from execution.

The ConfirmationManager only determines whether confirmation was received.

It must not execute tools or perform actions itself.

## Relationship With PermissionManager

PermissionManager decides whether an action can be:

- ALLOW
- ASK
- DENY

When the result is ASK, the system needs confirmation from the user.

ConfirmationManager handles that confirmation decision.

## Testing

Day 23 tests verify:

- a confirmed action returns True
- an unconfirmed action returns False

The current implementation is intentionally simple.

Later, the ConfirmationManager can be connected to the Agent's user interface and Action Guard.