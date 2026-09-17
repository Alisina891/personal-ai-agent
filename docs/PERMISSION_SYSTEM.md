# Permission States

The Personal AI Agent uses permission states to control whether an action is allowed.

## ALLOW

The agent is allowed to perform the action without asking the user again.

Example:

A user allows the agent to read a public project file.

## ASK

The agent must ask the user before performing the action.

Example:

The agent wants to use a private document for an external AI request.

The user must decide whether to allow the action.

## DENY

The agent is not allowed to perform the action.

Example:

The agent tries to send LOCAL_ONLY data outside the device when the security policy does not permit it.

## Important Rule

Permission states do not classify data.

Data classification answers:

"What kind of data is this?"

Permission state answers:

"Can the agent perform this action?"

The future security policy system will connect these concepts.

## Security Flow

Data
    ↓
Data Classification
    ↓
Security Policy
    ↓
Permission State
    ↓
AI Action