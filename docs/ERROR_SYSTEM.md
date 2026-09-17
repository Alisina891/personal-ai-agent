# Error Foundation

## Purpose

The Error Foundation provides a common error structure for the Personal AI Agent.

Different parts of the application can raise specific error types instead of using generic exceptions for every failure.

## Error Hierarchy

All application-specific errors inherit from `AgentError`.

The current hierarchy is:

AgentError
- ValidationError
- SecurityError
- ToolError
- DatabaseError
- AIError
- NetworkError

## Error Types

### ValidationError

Used when input or data does not meet the required rules.

### SecurityError

Used when a security rule blocks or rejects an operation.

### ToolError

Used when a tool cannot complete its requested operation.

### DatabaseError

Used when a database operation fails.

### AIError

Used when an AI provider or AI operation fails.

### NetworkError

Used when a network operation fails.

## Why Use Specific Errors?

Specific errors allow the application to handle different failures differently.

For example:

- Validation errors may require corrected input.
- Security errors should not be automatically bypassed.
- Network errors may be retryable.
- Database errors may require database recovery.
- AI errors may require provider failure handling.

These recovery behaviors will be implemented in later roadmap stages.

## Design Principle

The Error Foundation defines error categories only.

Individual systems are responsible for using the appropriate error type when their implementation is developed.

The system should never hide a real failure by reporting false success.