# Intent Detection

## Purpose

Intent Detection identifies the general purpose of a user's request.

The Understanding Layer receives natural language from the user and determines what type of request it appears to be.

Day 42 introduces six intent categories:

* `QUESTION`
* `TASK`
* `FILE`
* `MEMORY`
* `SEARCH`
* `ACTION`

---

## Architecture

```text
User Request
     ↓
Understanding
     ↓
Intent Detection
     ↓
Intent
     ↓
Structured Request
```

The intent is then available to other parts of the agent.

---

## Intent Categories

### QUESTION

The user is asking for information or an explanation.

Example:

```text
"What is Python?"
```

Result:

```text
Intent.QUESTION
```

---

### TASK

The user wants the agent to perform or prepare a task.

Example:

```text
"Create a new project"
```

Result:

```text
Intent.TASK
```

---

### FILE

The request concerns a file or filesystem operation.

Example:

```text
"Read README.md"
```

Result:

```text
Intent.FILE
```

---

### MEMORY

The user is asking about information stored from previous interactions.

Example:

```text
"What did we discuss about Day 30?"
```

Result:

```text
Intent.MEMORY
```

---

### SEARCH

The user wants information to be searched or looked up.

Example:

```text
"Search Python documentation"
```

Result:

```text
Intent.SEARCH
```

---

### ACTION

The user is requesting an action that may affect the system or an external resource.

Example:

```text
"Run the tests"
```

Result:

```text
Intent.ACTION
```

---

## Rule Priority

Some requests can match more than one category.

For example:

```text
"What did we discuss about Day 30?"
```

looks like a question because it starts with `What`, but its actual purpose is retrieving previous information.

Therefore it should be classified as:

```text
MEMORY
```

rather than:

```text
QUESTION
```

The detector evaluates more specific patterns before broader patterns.

This is an important design principle:

> Specific intent rules should take priority over broad rules when patterns overlap.

---

## Important Security Boundary

Intent detection does not provide authorization.

For example:

```text
Intent.ACTION
```

does not mean:

```text
Permission.ALLOW
```

Intent answers:

> "What does the user appear to want?"

The security system answers:

> "Is the agent allowed to do it?"

The architecture therefore remains:

```text
User Request
     ↓
Intent Detection
     ↓
Security / Permission
     ↓
Tool Authorization
     ↓
Execution
```

This preserves the project's core security principle:

> Intelligence may grow. Authority does not grow automatically.

---

## Current Implementation

Day 42 uses deterministic rules rather than an AI model.

This provides:

* predictable behavior
* fast execution
* easy testing
* no additional AI inference time
* easy debugging

The interface can later be improved without changing the rest of the system.

For example, a future implementation could use a local AI model for more complicated language while keeping the same conceptual interface:

```text
IntentDetector.detect(text)
```

---

## Current Limitation

The current detector is intentionally simple.

It relies primarily on known phrases and prefixes.

Therefore, natural language such as:

```text
"Could you take a look at my README?"
```

may not yet be classified correctly.

This is expected at this stage.

Future improvements can make intent detection more capable without changing the overall architecture.

---

## Testing

Day 42 tests cover:

* QUESTION detection
* TASK detection
* FILE detection
* MEMORY detection
* SEARCH detection
* ACTION detection
* Unknown request handling
* Overlapping intent behavior

The test suite verifies that the intent detector produces predictable results.

---

## Relationship With Understanding

Intent Detection is one component of the larger Understanding Layer.

The current direction is:

```text
User Request
     ↓
Understanding
     ├── Intent Detection
     ├── Entity Extraction
     └── Uncertainty Detection
              ↓
        Clarification
```

Day 42 establishes the intent portion of this architecture.
