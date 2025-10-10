---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [system]
description: Message queue design and optimization with queue theory
---

# Queue Command

Message queue design and optimization with queue theory

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: system

## Examples

```bash
/queue "Design job processing system" rabbitmq
/queue "Optimize queue throughput" sqs
```

Invoke the queue-theorist agent with: $ARGUMENTS
