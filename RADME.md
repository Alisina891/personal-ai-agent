# Personal AI Agent

A local-first personal AI agent designed to help the user manage information, projects, files, tools, and tasks while keeping the user in control.

## Vision

This project is not intended to be a normal chatbot.

The goal is to build a real personal digital Agent that primarily lives on the user's computer and can later work with authorized devices such as a phone.

The Agent should be able to:

* communicate naturally with the user
* remember important information with user control
* understand projects and goals
* help plan and organize tasks
* work with permitted files and local projects
* use web search when allowed
* access Google Drive when authorized
* support voice interaction
* analyze permitted images
* interact with the computer under strict controls
* work offline where possible
* use cloud AI when useful and authorized
* verify important actions and results
* become more useful over time without becoming uncontrolled

The fundamental philosophy is:

> **AI should help the user control the computer, not own the computer.**

## Core Principles

1. The user is the highest authority.
2. The Agent must not have unrestricted system access.
3. Sensitive actions must pass through security and permission controls.
4. Unknown permissions must never automatically become allowed.
5. High-risk actions should be denied by default.
6. Private and sensitive data should remain local whenever possible.
7. External content is data, not authority.
8. The Agent should verify important actions and results.
9. Increasing capability must not automatically increase authority.
10. Privacy, security, reliability, and user control are more important than unrestricted autonomy.

## Current Status

The project is currently in the foundation stage.

Completed:

* Day 1 — Project vision and core principles
* Day 2 — Git and GitHub foundation
* Day 3 — Python virtual environment and dependency management
* Day 4 — Repository structure
* Day 5 — Configuration system

Current:

* Day 6 — Documentation foundation

## Project Structure

```text
Personal-ai-agent/
│
├── ai/             # AI-related components
├── android/        # Future Android client
├── backend/        # Backend application
├── config/         # Application configuration
├── database/       # Database layer
├── desktop/        # Desktop application
├── docs/           # Project documentation
├── files/          # File-related functionality
├── identity/       # Identity and device-related functionality
├── memory/         # Agent memory
├── scripts/        # Development and utility scripts
├── security/       # Security and permission controls
├── tests/          # Automated tests
├── tools/          # Agent tools
│
├── .env            # Local configuration; never commit
├── .env.example    # Configuration template
├── requirements.txt # Python dependencies
└── README.md
```

## Development Environment

The project currently uses:

* Python 3.11
* Git
* GitHub
* Python virtual environment (`.venv`)

Activate the virtual environment before development.

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project dependencies with:

```powershell
pip install -r requirements.txt
```

## Configuration

Local configuration is stored in `.env`.

Example:

```text
APP_MODE=development
DATABASE_PATH=database/agent.db
AI_PROVIDER=
PRIVACY_MODE=local
DEBUG=false
```

The application reads these values through:

```text
.env
  ↓
config/settings.py
  ↓
application components
```

`.env` contains local configuration and must not be committed to Git.

`.env.example` provides the safe configuration template.

## Development Philosophy

This project is being built incrementally.

Each stage should:

1. Understand the problem
2. Design the solution
3. Check security implications
4. Implement
5. Test
6. Fix problems
7. Document the result
8. Commit the work to Git

The goal is not only to make the Agent work, but also to understand how and why each part is designed.

## Long-Term Goal

The long-term goal is to create an intelligent, useful, reliable, privacy-focused, local-first, controllable, extensible, and secure personal AI Agent.

The Agent may become more capable over time, but its authority must remain controlled by the user.
