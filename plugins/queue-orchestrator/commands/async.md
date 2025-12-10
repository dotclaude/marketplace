---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <task> [pattern]
description: Asynchronous processing patterns and worker orchestration
---

# Async Command

Asynchronous processing patterns and worker orchestration

## Arguments

**$1 (Required)**: task

**$2 (Optional)**: pattern

## Examples

```bash
/async "Implement background jobs" workers
/async "Design retry strategy" exponential-backoff
```

Invoke the async-specialist agent with: $ARGUMENTS
