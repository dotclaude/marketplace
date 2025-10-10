---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <environment> [strategy]
description: Orchestrate deployments with rollback strategies and health checks
---

# Infrastructure Deployment Command

Orchestrate sophisticated infrastructure deployments with CI/CD best practices, automated rollback strategies, and comprehensive health checks. Manage blue-green, canary, rolling, and recreate deployment patterns across environments.

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