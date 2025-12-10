---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [platform]
description: CI/CD pipeline design and optimization for modern platforms
---

# Pipeline Command

CI/CD pipeline design and optimization for modern platforms

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: platform

## Examples

```bash
/pipeline "Add automated testing and deployment" github-actions
/pipeline "Optimize build speed" gitlab-ci
```

Invoke the cicd-engineer agent with: $ARGUMENTS
