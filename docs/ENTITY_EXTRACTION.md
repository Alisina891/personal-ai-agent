# Entity Extraction

## Purpose

Day 43 adds the **Entity Extraction** foundation to the Understanding Layer.

The goal is to identify important objects or references inside a user's request.

Examples:

* file
* date
* person
* project
* location

Instead of keeping entity information as an unstructured string, the system now represents an entity with:

1. **Type** — what kind of entity it is.
2. **Value** — the actual value found in the request.

Example:

```text
User request:
Read README.md

Extracted entity:
Type: FILE
Value: README.md
```

---

## Why Entity Extraction Is Needed

Understanding a user's request requires more than knowing the user's intent.

For example:

```text
Open README.md
```

The system needs to understand:

```text
Intent = FILE
Entity = README.md
Entity Type = FILE
```

Another future request could be:

```text
Find the project called Personal AI Agent
```

The system may eventually understand:

```text
Intent = SEARCH
Entity Type = PROJECT
Entity Value = Personal AI Agent
```

Entity extraction therefore gives the agent more structured information about **what the request refers to**.

---

## Architecture

The current Understanding Layer is becoming:

```text
User Request
     ↓
Understanding
     ↓
Intent Detection
     ↓
Entity Extraction
     ↓
Structured Request
```

The resulting structure can contain:

```text
StructuredRequest
├── intent
└── entity
    ├── type
    └── value
```

This creates a clean boundary between the user's raw language and the rest of the agent.

---

# Entity Types

The system defines the following entity types:

```text
FILE
DATE
PERSON
PROJECT
LOCATION
```

They are represented by the `EntityType` enum.

## FILE

Represents a file referenced by the user.

Examples:

```text
README.md
main.py
config.json
data.csv
report.pdf
```

## DATE

Represents a date or time reference.

Examples:

```text
tomorrow
September 30
next Monday
```

Date extraction is defined as part of the architecture but is not yet implemented by the current extractor.

## PERSON

Represents a person mentioned in a request.

Example:

```text
Ali
John
Sarah
```

Person extraction is defined but not yet implemented.

## PROJECT

Represents a project referenced by the user.

Example:

```text
Personal AI Agent
Auto Grader
```

Project extraction is defined but not yet implemented.

## LOCATION

Represents a physical or geographic location.

Examples:

```text
Kabul
Afghanistan
New York
```

Location extraction is defined but not yet implemented.

---

# Entity Model

The `Entity` model stores the extracted entity.

Conceptually:

```text
Entity
├── type
└── value
```

Example:

```python
Entity(
    type=EntityType.FILE,
    value="README.md",
)
```

This is better than passing around a plain string because other components can now know **what the value represents**.

For example:

```text
"README.md"
```

does not explain itself.

But:

```text
FILE → README.md
```

is structured information.

---

# Entity Extractor

The `EntityExtractor` is responsible for finding entities in text.

The first implementation uses deterministic rules.

Currently it recognizes common file extensions:

```text
.txt
.md
.py
.json
.csv
.pdf
```

Example:

```text
Open main.py
```

produces:

```text
Type:
FILE

Value:
main.py
```

If no supported entity is found:

```text
Hello there
```

the extractor returns:

```text
None
```

---

# Why We Started With Rules

The project will eventually become much more intelligent, but the first implementation intentionally uses simple deterministic rules.

This gives us several benefits:

* predictable behavior
* easy testing
* easy debugging
* no dependency on an AI model
* works offline
* clear failure behavior
* establishes the interface before adding complexity

Later, the implementation can become more advanced without changing the rest of the architecture.

For example:

```text
Current:

EntityExtractor
      ↓
Simple Rules


Future:

EntityExtractor
      ↓
Advanced NLP / Local AI
      ↓
Structured Entities
```

The interface can remain stable.

---

# Structured Request

The `StructuredRequest` model now contains:

```text
intent
entity
```

The entity is represented using the `Entity` model rather than a plain string.

Example:

```text
User:
Read README.md

Structured Request:

intent:
FILE

entity:
    type = FILE
    value = README.md
```

This gives later components structured information instead of requiring them to interpret raw text again.

---

# Testing

Day 43 added tests for:

* Markdown file extraction
* Python file extraction
* unknown entities
* empty input

The full project test suite was executed:

```text
93 passed in 164.30s
```

Therefore:

```text
Day 43 Tests
     ↓
93 passed
     ↓
No test failures
```

The existing Understanding Layer tests also continue to pass after introducing the new `Entity` model.

---

# Important Design Principle

Entity extraction identifies **what the user is referring to**.

It does **not** give the agent permission to perform an action.

For example:

```text
Delete secret.pdf
```

might produce:

```text
Intent = ACTION
Entity Type = FILE
Entity Value = secret.pdf
```

But this does **not** mean:

```text
Permission = ALLOW
```

The security system must still decide whether the action is permitted.

The architecture remains:

```text
Understanding
      ↓
Intent + Entity
      ↓
Planning
      ↓
Security / Permission
      ↓
Confirmation
      ↓
ActionGuard
      ↓
Execution
```

**Understanding describes the request.
Security decides whether the request may be executed.**

---

# Current Limitations

The current implementation is intentionally small.

It does not yet reliably handle:

* dates
* people
* projects
* locations
* multiple entities
* complex file paths
* natural-language variations
* entities with punctuation
* ambiguous entity references

These are future improvements.

We should not add unnecessary complexity before the basic architecture is validated.

---

# Future Evolution

The entity system can later evolve from:

```text
One Entity
```

to:

```text
Multiple Entities
```

For example:

```text
Send the report.pdf to Ali tomorrow.
```

could eventually produce:

```text
FILE
    report.pdf

PERSON
    Ali

DATE
    tomorrow
```

This is one reason the entity model is separated from the raw request.

The architecture can grow without forcing the entire system to understand raw natural language everywhere.

---

# Day 43 Result

Day 43 established the foundation for entity-aware understanding.

Completed:

* [x] EntityType model
* [x] FILE entity
* [x] DATE entity definition
* [x] PERSON entity definition
* [x] PROJECT entity definition
* [x] LOCATION entity definition
* [x] Entity value model
* [x] EntityExtractor
* [x] StructuredRequest integration
* [x] Entity extraction tests
* [x] Full test suite validation

Final test result:

```text
93 passed
```

## Day 43 Status

**COMPLETE**

The Understanding Layer can now represent both:

```text
Intent
```

and:

```text
Entity
```

in a structured form.

This prepares the agent for more advanced understanding, planning, and eventually AI-assisted language interpretation while keeping the security boundary separate from intelligence.
