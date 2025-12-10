---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [method]
description: Authentication and authorization system design and implementation
---

# Auth Command

Authentication and authorization system design and implementation

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: method

## Examples

```bash
/auth "Implement OAuth2 flow" oauth2
/auth "Design JWT refresh strategy" jwt
```

Invoke the auth-specialist agent with: $ARGUMENTS
