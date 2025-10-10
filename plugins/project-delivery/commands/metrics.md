---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <metric-type> [timeframe]
description: Team metrics, velocity tracking, and performance analysis
---

# Metrics Command

Team metrics, velocity tracking, and performance analysis

## Arguments

**$1 (Required)**: metric-type

**$2 (Optional)**: timeframe

## Examples

```bash
/metrics "Team velocity analysis" last-quarter
/metrics "Cycle time optimization" current-sprint
```

Invoke the team-optimizer agent with: $ARGUMENTS
