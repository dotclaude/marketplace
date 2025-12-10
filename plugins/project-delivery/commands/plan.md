---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <goal> [timeframe]
description: Sprint planning, estimation, and agile ceremony facilitation
---

# Plan Command

Sprint planning, estimation, and agile ceremony facilitation

## Arguments

**$1 (Required)**: goal

**$2 (Optional)**: timeframe

## Examples

```bash
/plan "Next sprint planning" 2-weeks
/plan "Estimate feature development" story-points
```

Invoke the agile-coach agent with: $ARGUMENTS
