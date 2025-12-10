---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [solution]
description: State management patterns and implementation
---

# State Command

State management patterns and implementation

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: solution

## Examples

```bash
/state "Manage shopping cart state" zustand
/state "Implement form validation" react-hook-form
```

Invoke the state-manager agent with: $ARGUMENTS
