# Action Classifier

## Purpose

The ActionClassifier identifies what type of action the Agent is trying to perform before the action reaches the permission and security system.

It converts a human-readable action into a controlled ActionType.

Example:

"Delete this file"
→ FILE_DELETE

## Responsibility

The ActionClassifier is responsible only for classification.

It does not:

- decide whether an action is allowed
- execute the action
- request permission
- bypass security
- change permission rules

Those responsibilities belong to other parts of the security architecture.

## Supported Action Types

The current classifier supports:

- FILE_READ
- FILE_WRITE
- FILE_DELETE
- WEB_READ
- WEB_SEARCH

## Security Principle

Unknown actions must not be silently accepted.

If the classifier cannot recognize an action, it raises a ValueError.

This prevents the system from making an unsafe assumption about an unknown action.

## Architecture

The current security flow is:

User Action
→ ActionClassifier
→ ActionType
→ Permission System
→ PermissionManager
→ Action Guard
→ Tool

The ActionClassifier identifies the action, while the permission system decides what should happen with that action.

## Current Limitation

The current classifier is rule-based.

It uses simple text matching and is intended as a foundation for the security architecture.

It is not the final natural-language understanding system.

A more advanced classifier can be added later without changing the basic security principle that actions must be classified before authorization and execution.

## Testing

The ActionClassifier is tested for:

- file read
- file write
- file delete
- web read
- web search
- unknown actions

Current project test result:

17 tests passed.