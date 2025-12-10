---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [api-type]
description: REST and GraphQL API design, implementation, and best practices
---

# Api Command

REST and GraphQL API design, implementation, and best practices

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: api-type

## Examples

```bash
/api "Design user management endpoints" rest
/api "Create product catalog API" graphql
```

Invoke the api-architect agent with: $ARGUMENTS
