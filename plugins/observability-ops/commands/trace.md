---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <service> [focus]
description: Distributed tracing and performance bottleneck analysis
---

# Trace Command

Distributed tracing and performance bottleneck analysis

## Arguments

**$1 (Required)**: service

**$2 (Optional)**: focus

## Examples

```bash
/trace "checkout-service" latency
/trace "payment-api" bottlenecks
```

Invoke the performance-analyst agent with: $ARGUMENTS
