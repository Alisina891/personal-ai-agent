# Architecture

This document describes the planned architecture of the Local-First Personal AI Agent.

The architecture is designed to keep the system modular, secure, privacy-focused, and controllable by the user.

## 1. High-Level Architecture

The Agent is organized into several major areas:

```text
                    USER
                      │
                      ▼
              ┌───────────────┐
              │ User Interface │
              │ Desktop/Phone │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Agent Core    │
              │ Understanding │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Context       │
              │ + Memory      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Planner       │
              └───────┬───────┘
                      │
                      ▼
              ┌─────────────────────┐
              │ Security /          │
              │ Permission System   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Action Guard        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Tools / Services    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Verification        │
              └──────────┬──────────┘
                         │
                         ▼
                       RESULT
```

This is a conceptual architecture. Individual components will be implemented gradually.

## 2. Main Components

### User Interface

The interface is how the user communicates with the Agent.

Planned interfaces include:

* Desktop
* Android/mobile
* Voice interaction

The interface should not directly bypass the security system.

### Agent Core

The Agent Core coordinates the main reasoning and interaction process.

Responsibilities may include:

* understanding user requests
* maintaining conversation context
* coordinating planning
* requesting tools
* presenting results

The Agent Core should not have unrestricted system access.

### Context Builder

The Context Builder prepares relevant information for the Agent.

Possible context sources include:

* current conversation
* selected memory
* project information
* user-approved files
* tool results
* configuration

Only appropriate data should be included according to privacy and permission rules.

### Memory

The Memory system stores information that the user has allowed the Agent to remember.

Memory should eventually support:

* user-controlled information
* project information
* preferences
* useful historical context
* deletion or modification by the user

The AI itself is not the database.

Memory should be stored in a dedicated data layer.

### Planner

The Planner converts complex requests into structured steps.

For example:

```text
User Request
     ↓
Understand
     ↓
Create Plan
     ↓
Check Permissions
     ↓
Execute Approved Actions
     ↓
Verify Results
```

Planning does not grant permission.

A plan must still pass through security controls.

## 3. Security Architecture

Security is a separate architectural layer rather than something implemented only inside the AI.

The intended flow is:

```text
AI
 ↓
REQUEST
 ↓
SECURITY POLICY
 ↓
PERMISSION GUARD
 ↓
ACTION GUARD
 ↓
TOOL
 ↓
VERIFICATION
```

This separation is important because the AI should not be able to decide its own authority.

## 4. Security Policy

The Security Policy determines the rules that apply to an action.

It considers factors such as:

* requested action
* data sensitivity
* risk level
* user permissions
* device identity
* current privacy mode

The Security Policy should produce a controlled decision rather than allowing arbitrary AI behavior.

## 5. Permission Guard

The Permission Guard determines whether an action is:

```text
ALLOW
ASK
DENY
```

Unknown or unclear permissions should never automatically become `ALLOW`.

The user remains the final authority for actions that require confirmation.

## 6. Action Guard

The Action Guard provides another protection layer before a tool is executed.

It should check that:

* the requested action matches the approved action
* required permissions are still valid
* the target is appropriate
* the action has not changed unexpectedly

This helps prevent a tool from performing something different from what was authorized.

## 7. Tools

Tools are controlled capabilities that allow the Agent to interact with external systems.

Potential tools include:

* file operations
* database operations
* web search
* Google Drive
* computer interaction
* communication services
* other authorized integrations

Tools should not automatically be trusted simply because the AI requested them.

Tool access must pass through the security architecture.

## 8. Verification

After an important tool action, the system should verify the result.

For example:

```text
REQUEST
   ↓
APPROVAL
   ↓
ACTION
   ↓
VERIFY
   ↓
RESULT
```

Verification helps prevent the Agent from assuming that an action succeeded when it actually failed or produced an unexpected result.

## 9. Data Layer

The project is intended to use a local database as its primary structured data store.

The planned approach is:

```text
Application
     ↓
Database Layer
     ↓
SQLite
```

Google Drive may later be used for synchronization or backup when authorized.

Google Drive should not automatically replace the local primary database.

## 10. File System

Files are treated separately from structured database information.

The Agent may eventually work with:

* documents
* images
* project files
* user-selected files

Private files should remain local by default.

Cloud access should require appropriate authorization.

## 11. AI Provider

The AI Provider layer should separate the Agent architecture from a specific AI service.

Conceptually:

```text
Agent
  ↓
AI Provider Interface
  ↓
Local AI / Cloud AI Provider
```

This allows the project to change AI providers without redesigning the entire Agent.

Cloud AI should be optional where practical.

## 12. Identity

The Identity system will eventually manage:

* user identity
* device identity
* authorized devices
* authentication
* trusted relationships between devices

This becomes important when the Agent expands from one computer to multiple authorized devices.

## 13. Configuration

Configuration is centralized:

```text
.env
  ↓
config/settings.py
  ↓
Application Components
```

Components should obtain configuration through the configuration system instead of independently reading `.env`.

## 14. Audit and Logging

Important actions should eventually produce an audit record.

The audit system can help answer:

* What action was requested?
* Who requested it?
* What permission was used?
* What tool was executed?
* What happened?
* Was the result verified?

Audit logging will be developed later as the system becomes capable of performing real actions.

## 15. Privacy Model

The project uses a local-first philosophy.

Data categories include:

```text
PUBLIC
PRIVATE
SENSITIVE
LOCAL_ONLY
```

Privacy requirements should influence:

* where data is stored
* which tools can access it
* whether cloud services can receive it
* whether user confirmation is required

## 16. Device Architecture

The long-term system may contain multiple clients:

```text
             ┌──────────────┐
             │   Desktop    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ Personal AI  │
             │    Core      │
             └──────┬───────┘
                    │
             ┌──────┴───────┐
             ▼              ▼
        ┌─────────┐    ┌──────────┐
        │ Android │    │  Other   │
        │ Device  │    │ Devices  │
        └─────────┘    └──────────┘
```

Additional devices must be explicitly authorized.

A new device should not automatically become trusted.

## 17. Architectural Principle

The most important architectural principle is:

> **Capability and authority are separate.**

The Agent may gain more capabilities over time.

However, gaining a capability must not automatically give the Agent permission to use it.

The system should always preserve:

```text
Capability ≠ Authority
```

The architecture must keep the user in control as the Agent becomes more capable.
