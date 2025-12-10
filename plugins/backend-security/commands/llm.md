---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [pattern]
description: LLM integration patterns, RAG systems, and prompt engineering
---

# Llm Command

LLM integration patterns, RAG systems, and prompt engineering

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: pattern

## Examples

```bash
/llm "Build RAG system for docs" rag
/llm "Implement chat interface" streaming
```

Invoke the llm-integrator agent with: $ARGUMENTS
