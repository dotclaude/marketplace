---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [pattern]
description: ETL/ELT pipeline design and implementation
---

# Etl Command

ETL/ELT pipeline design and implementation

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: pattern

## Examples

```bash
/etl "Design data ingestion pipeline" batch
/etl "Build real-time processing" streaming
```

Invoke the streaming-architect agent with: $ARGUMENTS
