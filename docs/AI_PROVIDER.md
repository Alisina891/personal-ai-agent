# AI Provider Interface

## Purpose

The AI Provider Interface creates a stable contract between the Agent core and AI providers.

The Agent should not depend directly on a specific AI company, API, or model.

Instead, the Agent depends on the `AIProvider` interface.

## Interface

`ai/provider.py`

The interface defines:

- `provider_name` — identifies the provider.
- `generate(prompt)` — generates an AI response.

## Architecture

```text
Agent Core
     |
     v
 AIProvider
     |
     +------------------+
     |                  |
     v                  v
OpenAIProvider     LocalProvider
     |
     +------------------+
     |
     v
   Other Providers