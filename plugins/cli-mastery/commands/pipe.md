---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <data-task>
description: Unix pipeline design for elegant data flow and processing
---

# Pipe Command

Unix pipeline design for elegant data flow and processing

## Arguments

**$1 (Required)**: data-task

**$2 (Optional)**: Additional options

## Examples

```bash
/pipe "Extract errors from logs and count by type"
/pipe "Find duplicate files by content hash"
```

Invoke the pipe-architect agent with: $ARGUMENTS
