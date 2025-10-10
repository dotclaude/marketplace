---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [focus]
description: Distributed systems design and consensus patterns
---

# Distributed Command

Distributed systems design and consensus patterns

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: focus

## Examples

```bash
/distributed "Design distributed cache" consistency
/distributed "Implement leader election" consensus
```

Invoke the distributed-systems-expert agent with: $ARGUMENTS
