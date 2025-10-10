---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <script-purpose> [robustness]
description: Shell script creation with error handling and best practices
---

# Shell Command

Shell script creation with error handling and best practices

## SECURITY WARNING

**CRITICAL: This command creates shell scripts with Bash execution capabilities.**

Scripts you create will have the power to:
- Execute system commands
- Modify/delete files
- Access network resources
- Change permissions and ownership
- Potentially escalate privileges

**BEFORE requesting a script, consider:**
- What's the blast radius if this script is exploited?
- Does this script handle any untrusted input?
- Will this script access sensitive data or credentials?
- What's the minimum privilege level needed?

### Security Requirements Checklist

EVERY shell script must include:

- [ ] **Strict error handling**: `set -euo pipefail`
- [ ] **Input validation**: Validate ALL external inputs with regex
- [ ] **Quoted variables**: ALWAYS quote variables to prevent injection
- [ ] **No hardcoded secrets**: Use env vars or secret management
- [ ] **Secure temp files**: Use `mktemp`, never predictable names
- [ ] **Least privilege**: Run with minimum necessary permissions
- [ ] **Cleanup handlers**: Use `trap` to clean up on exit/error
- [ ] **Safe file permissions**: chmod 700 for scripts, 600 for configs
- [ ] **Command validation**: Validate commands before execution
- [ ] **Audit logging**: Log security-relevant operations

### Dangerous Operations to Avoid

**STOP and think before using:**
- `rm -rf` with variables
- `chmod 777` or similar overly permissive modes
- `sudo` without specific command limits
- `eval` with external input
- Unquoted variables in commands
- Shell injection via unsanitized input

## Arguments

**$1 (Required)**: script-purpose

**$2 (Optional)**: robustness (production requires strict security)

## Examples

```bash
/shell "Backup database with rotation" production
/shell "Deploy application with health checks"
```

Invoke the shell-scripter agent with: $ARGUMENTS
