---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <task> [preference]
description: CLI tool selection and usage patterns from terminal-native expert
---

# Cli Command

CLI tool selection and usage patterns from terminal-native expert

## Arguments

**$1 (Required)**: task

**$2 (Optional)**: preference

## Examples

```bash
/cli "Find large files efficiently" modern
/cli "Monitor system resources" standard
```

Invoke the cli-wizard agent with: $ARGUMENTS
