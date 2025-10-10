---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <incident> [phase]
description: Incident response orchestration and SRE best practices
---

# Incident Command

Incident response orchestration and SRE best practices

## Arguments

**$1 (Required)**: incident

**$2 (Optional)**: phase

## Examples

```bash
/incident "Database connection pool exhausted" triage
/incident "Yesterday's outage analysis" postmortem
```

Invoke the sre-engineer agent with: $ARGUMENTS
