---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [focus]
description: Product strategy, roadmap planning, and prioritization
---

# Product Command

Product strategy, roadmap planning, and prioritization

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: focus

## Examples

```bash
/product "Plan Q2 roadmap" prioritization
/product "Define feature strategy" vision
```

Invoke the product-strategist agent with: $ARGUMENTS
