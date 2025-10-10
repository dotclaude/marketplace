---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [tool]
description: Infrastructure as Code design with Terraform, CDK, and CloudFormation
---

# Infra Command

Infrastructure as Code design with Terraform, CDK, and CloudFormation

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: tool

## Examples

```bash
/infra "Setup EKS cluster" terraform
/infra "Configure S3 with CloudFront CDN" cdk
```

Invoke the infra-architect agent with: $ARGUMENTS
