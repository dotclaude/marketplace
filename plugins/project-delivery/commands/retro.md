---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <sprint-or-period> [focus]
description: Retrospective facilitation and continuous improvement
---

# Retro Command

Retrospective facilitation and continuous improvement

## Arguments

**$1 (Required)**: sprint-or-period

**$2 (Optional)**: focus

## Examples

```bash
/retro "Sprint 24 retrospective" improvements
/retro "Q1 team retrospective" process
```

Invoke the agile-coach agent with: $ARGUMENTS
