---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <target> [framework]
description: Audit logging and compliance tracking for enterprise requirements
---

# Audit Command

Audit logging and compliance tracking for enterprise requirements

## Arguments

**$1 (Required)**: target

**$2 (Optional)**: framework

## Examples

```bash
/audit "User access logs" soc2
/audit "Data retention policies" gdpr
```

Invoke the compliance-auditor agent with: $ARGUMENTS
