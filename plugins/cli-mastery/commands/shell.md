---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <script-purpose> [robustness]
description: Shell script creation with error handling and best practices
---

# Shell Command

Shell script creation with error handling and best practices

## Arguments

**$1 (Required)**: script-purpose

**$2 (Optional)**: robustness

## Examples

```bash
/shell "Backup database with rotation" production
/shell "Deploy application with health checks"
```

Invoke the shell-scripter agent with: $ARGUMENTS
