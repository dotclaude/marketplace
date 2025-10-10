---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <processing-task>
description: Text processing with sed, awk, grep, and regex mastery
---

# Text Command

Text processing with sed, awk, grep, and regex mastery

## Arguments

**$1 (Required)**: processing-task

**$2 (Optional)**: Additional options

## Examples

```bash
/text "Extract email addresses from log"
/text "Transform CSV to JSON format"
```

Invoke the text-surgeon agent with: $ARGUMENTS
