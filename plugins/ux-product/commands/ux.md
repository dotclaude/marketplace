---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [approach]
description: User experience research, design, and usability optimization
---

# Ux Command

User experience research, design, and usability optimization

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: approach

## Examples

```bash
/ux "Improve checkout flow" user-research
/ux "Design mobile navigation" interaction-design
```

Invoke the ux-designer agent with: $ARGUMENTS
