---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <question> [method]
description: User research, testing, and insight gathering
---

# User Research Command

User research, testing, and insight gathering

## Arguments

**$1 (Required)**: question

**$2 (Optional)**: method

## Examples

```bash
/user-research "Why do users abandon checkout?" interviews
/user-research "Test new feature prototype" usability-testing
```

Invoke the user-researcher agent with: $ARGUMENTS
