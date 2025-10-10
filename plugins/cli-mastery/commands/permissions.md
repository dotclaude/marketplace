---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <security-requirement>
description: Unix permissions and security configuration guidance
---

# Permissions Command

Unix permissions and security configuration guidance

## Arguments

**$1 (Required)**: security-requirement

**$2 (Optional)**: Additional options

## Examples

```bash
/permissions "Secure API keys in filesystem"
/permissions "Setup shared project directory"
```

Invoke the permissions-guardian agent with: $ARGUMENTS
