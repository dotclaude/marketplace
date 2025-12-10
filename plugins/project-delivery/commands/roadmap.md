---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <scope> [horizon]
description: Product roadmap and milestone planning
---

# Roadmap Command

Product roadmap and milestone planning

## Arguments

**$1 (Required)**: scope

**$2 (Optional)**: horizon

## Examples

```bash
/roadmap "Q2 feature roadmap" quarterly
/roadmap "Infrastructure migration plan" 6-months
```

Invoke the project-manager agent with: $ARGUMENTS
