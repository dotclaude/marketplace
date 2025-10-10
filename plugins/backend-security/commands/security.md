---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <concern> [focus]
description: Application security with OWASP best practices and threat modeling
---

# Security Command

Application security with OWASP best practices and threat modeling

## Purpose

Comprehensive security review and hardening for applications, APIs, infrastructure, and automation scripts. Identifies vulnerabilities, recommends mitigations, and ensures security best practices are followed.

## SECURITY FOCUS AREAS

This command helps you identify and fix security issues across:

### Input Validation & Injection Prevention
- SQL injection vulnerabilities
- Command injection risks
- LDAP/XPath/XML injection
- Path traversal attacks
- Input sanitization gaps

### Authentication & Authorization
- Broken authentication flows
- Session management issues
- Weak credential storage
- Authorization bypass vulnerabilities
- JWT/token handling problems

### Secrets Management
- Hardcoded credentials detection
- API keys in code or configs
- Unencrypted sensitive data
- Secrets in logs or error messages
- Insecure secret transmission

### OWASP Top 10 Coverage
1. Broken Access Control
2. Cryptographic Failures
3. Injection Flaws
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Software/Data Integrity Failures
9. Security Logging Failures
10. Server-Side Request Forgery

### Bash Script Security
- Command injection vulnerabilities
- Unquoted variable usage
- Hardcoded secrets detection
- Insufficient input validation
- Dangerous command patterns
- Permission misconfigurations

## Arguments

**$1 (Required)**: Security concern or component to review
- Authentication flow, API endpoint, shell script, configuration, etc.

**$2 (Optional)**: Specific focus area
- `owasp`: OWASP Top 10 systematic review
- `injection`: Injection vulnerability focus
- `auth`: Authentication/authorization review
- `secrets`: Secrets management audit
- `bash`: Shell script security review
- `api`: API security assessment

## Examples

### OWASP Security Review
```bash
/security "Review authentication flow" owasp
```
Systematic OWASP Top 10 review of authentication implementation

### Injection Vulnerability Audit
```bash
/security "Audit input validation" injection
```
Deep dive on SQL, command, and other injection vulnerabilities

### Bash Script Security Review
```bash
/security "Review deployment script" bash
```
Comprehensive shell script security analysis including command injection, secret detection, and permission review

### API Security Assessment
```bash
/security "Analyze REST API endpoints" api
```
API-specific security review covering authentication, rate limiting, input validation, and OWASP API Security Top 10

### Secrets Management Audit
```bash
/security "Audit application for secrets" secrets
```
Scan for hardcoded credentials, API keys, tokens, and recommend secure secret management

## Security Review Protocol

The security-guardian agent will:

1. **Threat Model**: Identify attack vectors and security boundaries
2. **Code Review**: Analyze for common vulnerability patterns
3. **Configuration Review**: Check security settings and misconfigurations
4. **Secrets Scan**: Detect hardcoded credentials and insecure storage
5. **Permission Analysis**: Verify least privilege and access control
6. **Recommendations**: Provide specific, actionable remediation steps
7. **Priority Assessment**: Categorize findings by severity (Critical/High/Medium/Low)

## What You Get

- **Vulnerability Report**: Detailed findings with severity levels
- **Exploit Scenarios**: How vulnerabilities could be exploited
- **Remediation Steps**: Specific code fixes and configuration changes
- **Security Patterns**: Recommended secure alternatives
- **Testing Guidance**: How to validate fixes
- **Compliance Mapping**: OWASP, CWE, and compliance framework mapping

Invoke the security-guardian agent with: $ARGUMENTS
