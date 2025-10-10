---
model: claude-opus-4-1
allowed-tools: Task, Read, Write, Bash(*), Glob, Grep
argument-hint: <system-or-application> [--threat-model=<category>] [--compliance=<framework>] [--learning=<security-education>]
description: Multi-expert security hardening with threat modeling and adaptive security education
---

# Advanced Security Hardening Engine

Implement comprehensive security measures through multi-expert collaboration with threat modeling, structured dissent, and adaptive security learning. Transform security implementation into a sophisticated, educational process that builds both robust protection and security expertise.

[Extended thinking: Enhanced workflow integrates multi-perspective threat analysis, constructive challenge of security assumptions, adaptive learning for security skill development, and structured dissent to identify security blind spots and strengthen defenses.]

## Phase 1: Multi-Expert Threat Analysis and Security Assessment

### 1. Comprehensive Security Multi-Perspective Analysis
[Extended thinking: Leverage multiple expert perspectives to ensure comprehensive threat identification and risk assessment from different attack vectors and defense viewpoints.]

**Multi-Expert Threat Assessment:**
- Use `/multi_perspective` command with `"$ARGUMENTS security analysis" security --perspectives=6 --integration=comprehensive --depth=systematic`
- **Security Architect**: Overall security design and defense-in-depth strategy
- **Penetration Tester**: Offensive perspective identifying attack vectors and vulnerabilities
- **Compliance Specialist**: Regulatory requirements and audit preparation
- **Infrastructure Security**: Network, server, and deployment security concerns
- **Application Security**: Code-level vulnerabilities and secure development practices
- **Incident Responder**: Monitoring, detection, and response capability assessment

**Threat Model Challenge:**
- Use `/constructive_dissent` command with `"Primary security threats for $ARGUMENTS" --dissent-intensity=rigorous --alternatives=3 --focus=threat-assumptions`
- Challenge assumptions about primary threats and attack vectors
- Generate alternative threat scenarios and attack pathways
- Question whether security focus areas are appropriately prioritized

**Security Learning Integration:**
- Use `/teach_concept` command with `"threat modeling for $ARGUMENTS" intermediate --approach=experiential --pathway=analytical`
- Build understanding of security principles through hands-on threat analysis
- Develop security intuition and pattern recognition skills
- Create transferable security knowledge for future projects

### 2. Enhanced Architecture Security Design
[Extended thinking: Create robust security architecture through collaborative design with red-team thinking and structured challenge of security assumptions.]

**Collaborative Security Architecture:**
- Use `/orchestrate` command with `"design secure architecture for $ARGUMENTS" complex security-auditor,backend-architect,network-engineer,devops-troubleshooter --mode=dialectical`
- Generate secure architecture through multi-expert collaboration
- Include threat modeling, defense layers, and security boundaries
- Ensure architecture supports zero-trust principles and defense-in-depth

**Red Team Architecture Challenge:**
- Use `/guest_expert` command with `"cybersecurity" "How would you attack this $ARGUMENTS architecture?" --expertise-depth=authority --perspective-count=3 --style=adversarial`
- Assume attacker perspective to identify architecture weaknesses
- Generate attack scenarios and exploitation pathways
- Validate architecture against sophisticated threat actors

**Security Assumption Audit:**
- Use `/assumption_audit` command with `"Security architecture assumptions for $ARGUMENTS" --audit-depth=paradigmatic --challenge-method=red-team-analysis`
- Challenge fundamental assumptions about security boundaries and trust models
- Examine assumptions about user behavior, system reliability, and threat environment
- Generate alternative security paradigms and approaches

## Phase 2: Security Implementation

### 3. Backend Security Hardening
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Implement backend security measures for: $ARGUMENTS. Include authentication, authorization, input validation, and secure data handling based on security audit findings."
- Output: Secure API implementations, auth middleware, validation layers

### 4. Infrastructure Security
- Use Task tool with subagent_type="devops-troubleshooter"
- Prompt: "Implement infrastructure security for: $ARGUMENTS. Configure firewalls, secure secrets management, implement least privilege access, and set up security monitoring."
- Output: Infrastructure security configs, secrets management, monitoring setup

### 5. Frontend Security
- Use Task tool with subagent_type="frontend-developer"
- Prompt: "Implement frontend security measures for: $ARGUMENTS. Include CSP headers, XSS prevention, secure authentication flows, and sensitive data handling."
- Output: Secure frontend code, CSP policies, auth integration

## Phase 3: Compliance and Testing

### 6. Compliance Verification
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Verify compliance with security standards for: $ARGUMENTS. Check OWASP Top 10, GDPR, SOC2, or other relevant standards. Validate all security implementations."
- Output: Compliance report, remediation requirements

### 7. Security Testing
- Use Task tool with subagent_type="test-automator"
- Prompt: "Create security test suites for: $ARGUMENTS. Include penetration tests, security regression tests, and automated vulnerability scanning."
- Output: Security test suite, penetration test results, CI/CD integration

## Phase 4: Deployment and Monitoring

### 8. Secure Deployment
- Use Task tool with subagent_type="deployment-engineer"
- Prompt: "Implement secure deployment pipeline for: $ARGUMENTS. Include security gates, vulnerability scanning in CI/CD, and secure configuration management."
- Output: Secure CI/CD pipeline, deployment security checks, rollback procedures

### 9. Security Monitoring Setup
- Use Task tool with subagent_type="devops-troubleshooter"
- Prompt: "Set up security monitoring and incident response for: $ARGUMENTS. Include intrusion detection, log analysis, and automated alerting."
- Output: Security monitoring dashboards, alert rules, incident response procedures

## Coordination Notes
- Security findings from each phase inform subsequent implementations
- All agents must prioritize security in their recommendations
- Regular security reviews between phases ensure nothing is missed
- Document all security decisions and trade-offs

Security hardening target: $ARGUMENTS