# Ambiguity Detection

## Purpose

Day 44 adds **Ambiguity Detection** to the Understanding Layer.

The purpose is to detect situations where the agent has received information, but that information is **not specific enough to safely determine what the user means**.

Example:

> “Review that PDF.”

The agent can understand that the user is referring to a PDF, but it does not know which PDF.

Therefore:

```text
Entity Type = FILE
Entity Value = "that PDF"

Ambiguity = AMBIGUOUS
```

Compare this with:

> “Review report.pdf.”

Here the file is explicitly identified:

```text
Entity Type = FILE
Entity Value = "report.pdf"

Ambiguity = CLEAR
```

---

# Why Ambiguity Detection Is Needed

Understanding a request is not always enough to execute it.

A request can have:

* a valid intent
* a valid entity
* but still be ambiguous

For example:

```text
"Delete that file."
```

The agent may understand:

```text
Intent = ACTION
Entity Type = FILE
```

But the phrase:

```text
"that file"
```

does not identify a specific file.

Executing an action at this point could cause the agent to operate on the wrong resource.

Therefore the system must detect ambiguity **before execution**.

---

# Ambiguity vs Uncertainty

The project already has an **Uncertainty Detection** component from Day 40.

These concepts are related but different.

### Uncertainty

Uncertainty asks:

> “Do I understand the request sufficiently?”

Example:

```text
"Something with the project."
```

The system may not have enough information to determine the user's intent and entity.

### Ambiguity

Ambiguity asks:

> “Is the reference specific enough to know exactly what the user means?”

Example:

```text
"Open that PDF."
```

The system understands:

```text
Intent = FILE
Entity = PDF
```

but the specific PDF is unknown.

The relationship can be represented as:

```text
User Request
     ↓
Understanding
     ↓
Uncertainty Detection
     ↓
Intent + Entity
     ↓
Ambiguity Detection
     ↓
CLEAR / AMBIGUOUS
```

Both mechanisms help prevent the agent from making assumptions.

---

# Ambiguity Model

Day 44 introduces:

```text
AmbiguityLevel
```

with two states:

```text
CLEAR
AMBIGUOUS
```

## CLEAR

The system has enough specificity to continue to the next stage.

Example:

```text
report.pdf
```

Result:

```text
CLEAR
```

## AMBIGUOUS

The request contains an unclear or insufficiently specific reference.

Examples:

```text
that PDF
the PDF
that file
the file
this PDF
this file
```

Result:

```text
AMBIGUOUS
```

---

# Ambiguity Detector

The `AmbiguityDetector` is responsible for determining whether an entity is sufficiently specific.

Its input is an `Entity`:

```text
Entity
├── type
└── value
```

Its output is:

```text
AmbiguityLevel
```

Conceptually:

```text
Entity
   ↓
AmbiguityDetector
   ↓
CLEAR / AMBIGUOUS
```

The detector currently uses deterministic rules.

For example:

```text
Entity(FILE, "report.pdf")
        ↓
CLEAR
```

while:

```text
Entity(FILE, "that PDF")
        ↓
AMBIGUOUS
```

---

# Handling Missing Entities

If the detector receives:

```text
None
```

it currently returns:

```text
AMBIGUOUS
```

This is intentionally conservative.

The agent should not assume that a missing entity is safe to act upon.

This follows the project's broader security philosophy:

> When important information is missing, do not silently guess.

---

# Why Deterministic Rules Are Used

Day 44 intentionally does not use an AI model for ambiguity detection.

The initial rules provide:

* predictable behavior
* easy testing
* offline operation
* easy debugging
* clear failure conditions
* low complexity

This is important for a security-sensitive personal agent.

A future implementation can become more advanced.

For example:

```text
"Open the report."
        ↓
Filesystem search
        ↓
3 matching reports
        ↓
AMBIGUOUS
```

Or:

```text
"Open the report."
        ↓
Filesystem search
        ↓
1 matching report
        ↓
CLEAR
```

Context and memory could also eventually help resolve references.

However, those capabilities belong to later stages of the architecture.

---

# Security Relationship

Ambiguity detection is part of understanding.

It is **not a permission system**.

For example:

```text
"Delete that PDF."
```

could produce:

```text
Intent = ACTION
Entity = FILE: that PDF
Ambiguity = AMBIGUOUS
```

This does not mean the action is allowed.

The security architecture remains:

```text
Understanding
      ↓
Intent + Entity
      ↓
Ambiguity / Uncertainty
      ↓
Planning
      ↓
Permission System
      ↓
Confirmation
      ↓
ActionGuard
      ↓
Execution
```

The important principle is:

> **Understanding determines what the user appears to mean. Security determines whether the agent is allowed to act.**

Ambiguity detection therefore strengthens safety without becoming a security authority itself.

---

# Testing

Day 44 added tests covering:

1. Ambiguous PDF reference
2. Clear file reference
3. Missing entity

Examples:

```text
"that PDF"
    → AMBIGUOUS
```

```text
"report.pdf"
    → CLEAR
```

```text
None
    → AMBIGUOUS
```

The complete non-integration test suite was executed:

```text
95 passed, 1 deselected in 0.98s
```

The integration test remains deselected because it requires the external local AI service.

---

# Current Limitations

The Day 44 implementation is intentionally limited.

It does not yet:

* search the filesystem
* check how many files match
* use conversation context
* use memory to resolve references
* detect all ambiguous phrases
* understand complex natural-language ambiguity
* ask the user a clarification question

For example:

```text
"Open the report."
```

may still be considered clear by the current simple detector even if there are ten reports.

Resolving that type of ambiguity requires access to actual context or resources.

That is intentionally left for future development.

---

# Connection to Day 45

Day 44 answers:

> **“Is the request ambiguous?”**

Day 45 will answer:

> **“What should the agent do when it is ambiguous?”**

The next flow will become:

```text
User Request
     ↓
Understanding
     ↓
Intent + Entity
     ↓
Ambiguity Detection
     ↓
AMBIGUOUS
     ↓
Clarification Engine
     ↓
Question to User
```

For example:

```text
User:
"Review that PDF."

Agent:
"Which PDF do you mean?"
```

The agent should not guess.

---

# Day 44 Result

Completed:

* [x] Ambiguity model
* [x] `CLEAR` state
* [x] `AMBIGUOUS` state
* [x] Ambiguity detector
* [x] Ambiguous file reference detection
* [x] Missing entity handling
* [x] Unit tests
* [x] Full non-integration test validation

Final result:

```text
95 passed, 1 deselected
```

## Day 44 Status

**COMPLETE**

The Understanding Layer can now distinguish between information that is sufficiently specific and information that requires clarification.

This creates the foundation for **Day 45 — Clarification Engine**, where ambiguity will be converted into a clear question for the user.
