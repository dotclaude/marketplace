---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <communication-need> [audience]
description: Stakeholder communication and expectation management
---

# Stakeholder Command

Stakeholder communication and expectation management

## Arguments

**$1 (Required)**: communication-need

**$2 (Optional)**: audience

## Examples

```bash
/stakeholder "Project status update" executives
/stakeholder "Feature demo preparation" customers
```

Invoke the stakeholder-liaison agent with: $ARGUMENTS
