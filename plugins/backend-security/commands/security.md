---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <concern> [focus]
description: Application security with OWASP best practices and threat modeling
---

# Security Command

Application security with OWASP best practices and threat modeling

## Arguments

**$1 (Required)**: concern

**$2 (Optional)**: focus

## Examples

```bash
/security "Review authentication flow" owasp
/security "Audit input validation" injection
```

Invoke the security-guardian agent with: $ARGUMENTS
