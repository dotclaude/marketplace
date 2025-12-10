---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <system> [strategy]
description: Backpressure and rate limiting strategies for system stability
---

# Backpressure Command

Backpressure and rate limiting strategies for system stability

## Arguments

**$1 (Required)**: system

**$2 (Optional)**: strategy

## Examples

```bash
/backpressure "Handle API rate limits" circuit-breaker
/backpressure "Implement flow control" token-bucket
```

Invoke the backpressure-expert agent with: $ARGUMENTS
