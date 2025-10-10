---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <environment> [strategy]
description: Orchestrate deployments with rollback strategies and health checks
---

# Infrastructure Deployment Command

Orchestrate sophisticated infrastructure deployments with CI/CD best practices, automated rollback strategies, and comprehensive health checks. Manage blue-green, canary, rolling, and recreate deployment patterns across environments.

## SECURITY WARNING

**CRITICAL: Deployment operations have high-privilege access and can modify production systems.**

Deployment scripts will:
- Execute commands on production infrastructure
- Modify load balancer configurations
- Update database schemas or trigger migrations
- Handle sensitive environment variables and secrets
- Potentially cause service disruptions if misconfigured

### Pre-Deployment Security Checklist

BEFORE executing any deployment, verify:

- [ ] **Credentials Management**: No secrets in code, use vaults or secret managers
- [ ] **Access Control**: Deployment executed by authorized personnel only
- [ ] **Change Approval**: Required approvals obtained for production deployments
- [ ] **Rollback Plan**: Tested rollback procedure available
- [ ] **Secrets Rotation**: No hardcoded credentials, proper secret injection
- [ ] **Audit Logging**: All deployment actions logged with who/what/when
- [ ] **Validation Gates**: Pre-deployment health checks passed
- [ ] **Backup Verification**: Recent backup available before destructive operations
- [ ] **Blast Radius**: Impact scope understood and limited
- [ ] **Communication**: Relevant teams notified of deployment window

### Deployment Security Best Practices

1. **Secret Management**
   - Use AWS Secrets Manager, HashiCorp Vault, or similar
   - Rotate secrets regularly, especially after deployments
   - Never log or echo secrets in deployment scripts
   - Use scoped, short-lived credentials when possible

2. **Least Privilege Deployment**
   - Use service accounts with minimum required permissions
   - Avoid deploying as root or with admin privileges
   - Scope IAM roles to specific resources and actions
   - Review and audit deployment permissions quarterly

3. **Secure Communication**
   - All deployment traffic over TLS/HTTPS
   - Verify TLS certificates, don't disable validation
   - Use VPN or bastion hosts for production access
   - Implement network segmentation and firewalls

4. **Validation & Safety**
   - Dry-run mode to preview changes before execution
   - Health checks at every stage of deployment
   - Automated rollback triggers on error thresholds
   - Database migrations in transactions when possible
   - Blue-green keeps previous version running until validated

### Red Flags to Never Ignore

**STOP IMMEDIATELY if you see:**
- Secrets hardcoded in deployment scripts
- Deployment scripts with 777 permissions
- Root credentials used for deployment
- Deployment bypassing change approval process
- No rollback strategy for production changes
- Untested deployment to production
- Missing health checks or monitoring

## How It Works

This command invokes the deployment-coordinator agent to:
1. Validate deployment readiness and environment configuration
2. Execute pre-deployment checks and dependency verification
3. Orchestrate the selected deployment strategy
4. Monitor health checks and performance metrics
5. Manage automated rollback if issues are detected
6. Generate deployment reports and audit trails

## Arguments

**$1 (Required)**: Deployment target or environment
- `staging`: Staging environment deployment
- `production`: Production environment deployment
- `dev`: Development environment deployment
- Custom environment names as configured

**$2 (Optional)**: Deployment strategy
- `blue-green`: Zero-downtime deployment with instant rollback capability (default for production)
- `canary`: Progressive rollout with traffic shifting
- `rolling`: Gradual instance replacement with configurable batch size
- `recreate`: Simple stop-start deployment (default for staging/dev)

## Examples

### Blue-Green Production Deployment
```bash
/deploy production blue-green
```
Orchestrates zero-downtime deployment with automated traffic switching and instant rollback capability

### Canary Staging Deployment
```bash
/deploy staging canary
```
Progressive deployment with 10% -> 50% -> 100% traffic shifting and automated rollback on error thresholds

### Rolling Update
```bash
/deploy production rolling
```
Gradual instance replacement with health checks between batches and automatic pause on failures

### Simple Staging Deployment
```bash
/deploy staging
```
Uses recreate strategy for straightforward staging deployment with basic health validation

## Use Cases

**Production Deployments**
- Zero-downtime releases
- Traffic management
- Automated rollback
- Performance validation

**Staging Validation**
- Pre-production testing
- Integration validation
- Performance benchmarking
- Security scanning

**Emergency Rollbacks**
- Instant blue-green switch
- Canary traffic reversal
- Rolling update pause/rollback
- State preservation

**Multi-Region Deployments**
- Region-by-region rollout
- Cross-region validation
- Failover management
- Global load balancing

## What You Get

1. **Deployment Orchestration**: Automated execution of complex deployment patterns
2. **Health Monitoring**: Continuous validation with configurable thresholds and metrics
3. **Rollback Automation**: Instant rollback triggers based on health, performance, or error rates
4. **Audit Trail**: Complete deployment history with decision points and metrics
5. **Integration Points**: CI/CD pipeline integration with GitHub Actions, GitLab CI, Jenkins

## Deployment Strategy Details

**Blue-Green**:
- Maintains two identical production environments
- Instant traffic switching via load balancer
- Zero downtime with immediate rollback
- Best for critical production systems

**Canary**:
- Progressive traffic shifting (10% -> 50% -> 100%)
- Automated metrics comparison between versions
- Gradual rollback with minimal user impact
- Ideal for validating new features

**Rolling**:
- Configurable batch size and wait times
- Health checks between batches
- Automatic pause on threshold breaches
- Good for large-scale deployments

**Recreate**:
- Simple stop-start deployment
- Brief downtime acceptable
- Minimal complexity
- Suitable for dev/staging environments

## Tips for Best Results

1. **Test in Staging**: Always validate deployment strategies in staging first
2. **Define Health Checks**: Configure comprehensive health endpoints and thresholds
3. **Set Rollback Criteria**: Define clear metrics for automated rollback triggers
4. **Monitor Actively**: Use observability tools during deployment windows
5. **Document Changes**: Include deployment notes and change logs

## Example Session

```bash
/deploy production blue-green
```

**Result**: Deployment coordinator validates infrastructure, runs pre-flight checks, provisions blue environment, validates health, switches traffic at load balancer, monitors for 5 minutes, and either commits or rolls back based on metrics. Full audit trail and performance report generated.

Invoke the deployment-coordinator agent with: $ARGUMENTS