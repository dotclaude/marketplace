---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <flow> [focus]
description: User journey mapping and flow optimization
---

# Journey Command

User journey mapping and flow optimization

## Arguments

**$1 (Required)**: flow

**$2 (Optional)**: focus

## Examples

```bash
/journey "Map onboarding experience" touchpoints
/journey "Optimize purchase flow" friction-points
```

Invoke the interaction-designer agent with: $ARGUMENTS
