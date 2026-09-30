# AI Output Validation

## Purpose

AI Output Validation ensures that a successful request to an AI provider does not automatically mean that the AI returned a valid result.

The Personal AI Agent must validate AI output before passing it to other parts of the system.

---

## Why This Exists

An AI provider can successfully respond at the HTTP level but still return invalid data.

Examples:

* Missing `response` field
* Empty response
* Whitespace-only response
* Non-string response
* Malformed JSON

Without validation, invalid AI output could continue through the system and cause unexpected behavior.

The rule is:

> A successful provider request is not automatically a successful AI result.

---

## Current Validation Rules

`LocalAIProvider` validates the following:

### 1. Response field exists

The provider response must contain:

```text
response
```

If it is missing, an `AIError` is raised.

### 2. Response must be a string

For example:

```text
"Hello"
```

is valid.

But:

```text
123
```

is invalid.

### 3. Response cannot be empty

This is invalid:

```text
""
```

### 4. Response cannot contain only whitespace

This is invalid:

```text
"   "
```

A normal response such as:

```text
"  Hello  "
```

is accepted.

---

## Error Handling

Invalid provider output raises:

```text
AIError
```

This prevents invalid AI data from silently entering the rest of the agent.

The provider therefore follows this basic flow:

```text
AI Provider
     ↓
HTTP Request
     ↓
HTTP Error Check
     ↓
JSON Parsing
     ↓
Response Field Validation
     ↓
Type Validation
     ↓
Empty Output Validation
     ↓
Valid AI Output
```

---

## Security Principle

AI output is still **data**, not authority.

Even when output validation succeeds, the AI response must not automatically gain permission to:

* execute commands
* access files
* send messages
* modify data
* use protected tools
* change permissions

Security controls such as the Action Guard and permission system remain responsible for authorization.

This follows the project principle:

> Intelligence may grow. Authority does not grow automatically.

---

## Testing

Day 39 added tests for:

* Empty response
* Whitespace-only response
* Non-string response
* Valid response
* Missing response
* Connection failure
* Timeout
* HTTP failure

The fast test suite currently passes:

```text
68 passed, 1 deselected
```

The real Ollama integration test also passes:

```text
1 passed, 68 deselected
```

The integration test confirms that the real `qwen3:4b` model can produce an output that passes the validation layer.

---

## Architecture

Current AI flow:

```text
                    ┌─────────────────┐
                    │     Ollama      │
                    │    qwen3:4b     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ LocalAIProvider │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Output          │
                    │ Validation      │
                    └────────┬────────┘
                             │
                       Valid output
                             │
                             ▼
                    ┌─────────────────┐
                    │     Agent       │
                    └─────────────────┘
```

---

## Important Limitation

This validation checks the **structure and basic validity** of AI output.

It does not determine whether the AI's answer is:

* factually correct
* logically correct
* safe in every context
* aligned with the user's intention
* authorized to perform an action

Those responsibilities belong to later parts of the architecture.

Day 39 establishes the basic rule:

> Invalid AI output must not silently continue through the system.
