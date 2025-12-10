---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [focus]
description: Frontend architecture and performance optimization
---

# Frontend Command

Frontend architecture and performance optimization

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: focus

## Examples

```bash
/frontend "Optimize bundle size" performance
/frontend "Implement code splitting" architecture
```

Invoke the frontend-optimizer agent with: $ARGUMENTS
