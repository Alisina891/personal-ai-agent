# Local AI Provider

## Purpose

The Local AI Provider connects the Personal AI Agent to a locally running AI model through Ollama.

It allows the agent to use AI without sending prompts to a cloud AI service.

Current provider:

- Ollama
- Model: qwen3:4b
- Default address: http://127.0.0.1:11434

---

## Architecture

```text
Agent Core
    ↓
AIProvider
    ↓
LocalAIProvider
    ↓
Ollama
    ↓
Local AI Model