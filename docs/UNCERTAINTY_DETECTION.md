# Uncertainty Detection

## Purpose

Uncertainty Detection allows the Personal AI Agent to represent how much information it currently has about a user request.

The system uses three levels:

* `CONFIDENT`
* `UNCERTAIN`
* `UNKNOWN`

The goal is to prevent the agent from guessing when important information is missing.

---

## Uncertainty Levels

### CONFIDENT

The required understanding information is available.

Example:

```text
Intent: FILE_READ
Entity: README.md

Result: CONFIDENT
```

The agent can continue to the next stage.

### UNCERTAIN

Some information is available, but something important is missing.

Example:

```text
Intent: FILE_READ
Entity: None

Result: UNCERTAIN
```

The agent should ask the user for clarification.

### UNKNOWN

The system does not have enough information to determine the request.

Example:

```text
Intent: None
Entity: None

Result: UNKNOWN
```

The agent should not guess. It should request clarification.

---

## Components

### `uncertainty.py`

Defines the `UncertaintyLevel` enum.

It provides one shared vocabulary for the rest of the agent.

### `uncertainty_detector.py`

Determines the current uncertainty level from the available intent and entity information.

Current Day 40 rules:

```text
Intent + Entity
    → CONFIDENT

Intent only
    → UNCERTAIN

Entity only
    → UNCERTAIN

Neither
    → UNKNOWN
```

This is intentionally a simple first implementation.

It represents structural completeness, not true semantic confidence.

### `clarification.py`

Determines whether the agent should ask the user for clarification.

```text
CONFIDENT
    → Continue

UNCERTAIN
    → Clarify

UNKNOWN
    → Clarify
```

---

## Architecture

```text
User Input
    ↓
Understanding
    ↓
Uncertainty Detection
    ↓
┌─────────────┬─────────────┬─────────────┐
│ CONFIDENT   │ UNCERTAIN   │ UNKNOWN     │
│     ↓       │      ↓      │      ↓       │
│ Continue    │ Clarify     │ Clarify     │
└─────────────┴─────────────┴─────────────┘
```

---

## Important Design Principle

The agent must not pretend to understand something that it does not understand.

When required information is missing:

```text
Do not guess.
Do not invent information.
Ask for clarification.
```

This supports the larger project principle:

> The agent helps the user while keeping the user in control.

---

## Current Limitation

The current Day 40 implementation does not calculate a numerical confidence score and does not perform deep semantic analysis.

`CONFIDENT` currently means that the expected intent and entity information are present.

Later understanding components can make this decision more sophisticated.

The architecture allows that improvement without changing the three-level uncertainty model.

---

## Testing

Day 40 includes tests for:

* All three uncertainty levels
* Confident detection
* Uncertain detection
* Unknown detection
* Clarification for uncertain input
* Clarification for unknown input
* No clarification for confident input

The tests ensure that uncertainty behavior remains deterministic and predictable.
