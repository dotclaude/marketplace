---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <question> [approach]
description: Data analytics, visualization, and insights extraction
---

# Analytics Command

Data analytics, visualization, and insights extraction

## Arguments

**$1 (Required)**: question

**$2 (Optional)**: approach

## Examples

```bash
/analytics "Analyze user behavior patterns" sql
/analytics "Create performance dashboard" visualization
```

Invoke the analytics-expert agent with: $ARGUMENTS
