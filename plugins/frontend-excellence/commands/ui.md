---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <component-need> [approach]
description: Component design, styling, and design system implementation
---

# Ui Command

Component design, styling, and design system implementation

## Arguments

**$1 (Required)**: component-need

**$2 (Optional)**: approach

## Examples

```bash
/ui "Design button component variants" design-system
/ui "Create responsive navigation" mobile-first
```

Invoke the component-architect agent with: $ARGUMENTS
