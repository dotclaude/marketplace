---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <task> [tool]
description: Data processing and transformation with jq, pandas, SQL
---

# Data Command

Data processing and transformation with jq, pandas, SQL

## Arguments

**$1 (Required)**: task

**$2 (Optional)**: tool

## Examples

```bash
/data "Transform JSON logs to CSV" jq
/data "Clean and normalize dataset" pandas
```

Invoke the data-engineer agent with: $ARGUMENTS
