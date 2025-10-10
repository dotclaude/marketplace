---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <service> [type]
description: SLO/SLI definition and reliability tracking
---

# Slo Command

SLO/SLI definition and reliability tracking

## Arguments

**$1 (Required)**: service

**$2 (Optional)**: type

## Examples

```bash
/slo "payment-api" availability
/slo "search-service" latency
```

Invoke the sre-engineer agent with: $ARGUMENTS
