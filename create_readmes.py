#!/usr/bin/env python3
"""
Generate README.md and .gitignore files for all 9 new plugins.
"""

from pathlib import Path

BASE_DIR = Path("/home/projectspace/projects/dotclaude-plugins/marketplace/plugins")

GITIGNORE_CONTENT = """# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Temp
*.tmp
.cache/
"""

PLUGINS = {
    "infra-pipeline": {
        "display_name": "Infrastructure & Deployment Pipeline",
        "tagline": "Complete infrastructure lifecycle from IaC to deployment",
        "description": "Master AWS, Terraform, CI/CD pipelines, GitOps workflows, and deployment automation for both home projects and enterprise systems.",
        "commands": ["deploy", "infra", "pipeline", "automate"],
        "use_cases": [
            "**AWS Infrastructure Design** - Terraform, CDK, CloudFormation for cloud infrastructure",
            "**CI/CD Pipeline Optimization** - GitHub Actions, GitLab CI, Jenkins automation",
            "**Deployment Strategies** - Blue-green, canary, rolling deployments with rollback",
            "**DevOps Automation** - Workflow scripting, infrastructure automation, GitOps"
        ]
    },
    "observability-ops": {
        "display_name": "Observability & Operations Excellence",
        "tagline": "Production reliability and comprehensive observability",
        "description": "Master Datadog, CloudWatch, monitoring, incident response, SRE practices, and audit logging for enterprise compliance.",
        "commands": ["monitor", "trace", "incident", "slo", "audit"],
        "use_cases": [
            "**Monitoring Setup** - Datadog dashboards, CloudWatch alarms, Prometheus queries",
            "**Performance Analysis** - Distributed tracing, APM, bottleneck identification",
            "**Incident Response** - SRE practices, runbooks, blameless postmortems",
            "**Compliance Auditing** - SOC2, HIPAA, GDPR audit logging and evidence collection"
        ]
    },
    "frontend-excellence": {
        "display_name": "Frontend Excellence & React Mastery",
        "tagline": "Modern React and UI development expertise",
        "description": "Master React 19, Next.js 15, component architecture, state management, performance optimization, and design systems.",
        "commands": ["react", "ui", "frontend", "state"],
        "use_cases": [
            "**React Development** - React 19 hooks, server components, concurrent rendering",
            "**Component Architecture** - Design systems, component libraries, reusable patterns",
            "**Performance Optimization** - Core Web Vitals, bundle optimization, lazy loading",
            "**State Management** - Redux, Zustand, Context, modern state patterns"
        ]
    },
    "backend-security": {
        "display_name": "Backend & Security Excellence",
        "tagline": "Backend development with security-first approach",
        "description": "Master REST/GraphQL APIs, OWASP security, LLM integration, authentication systems, and secure coding practices.",
        "commands": ["api", "security", "llm", "auth"],
        "use_cases": [
            "**API Design** - REST and GraphQL architecture, versioning, documentation",
            "**Security Hardening** - OWASP Top 10, threat modeling, penetration testing",
            "**LLM Integration** - RAG systems, embeddings, prompt engineering, production patterns",
            "**Authentication Systems** - OAuth2, OIDC, JWT, session management"
        ]
    },
    "data-intelligence": {
        "display_name": "Data Intelligence & Analytics",
        "tagline": "Data engineering and time series analysis mastery",
        "description": "Expert in jq, SQL, pandas, time series forecasting, ETL pipelines, streaming, and analytics visualization.",
        "commands": ["data", "timeseries", "analytics", "etl"],
        "use_cases": [
            "**Data Processing** - jq transformations, pandas operations, SQL analytics",
            "**Time Series Analysis** - Forecasting, anomaly detection, trend analysis",
            "**Analytics & Visualization** - Business intelligence, dashboards, insights",
            "**ETL Pipelines** - Batch and streaming data processing, Kafka, data quality"
        ]
    },
    "queue-orchestrator": {
        "display_name": "Queue Theory & Async Systems",
        "tagline": "Message queues and distributed systems expertise",
        "description": "Master queue theory, RabbitMQ, SQS, Kafka, async processing, backpressure, and distributed system patterns.",
        "commands": ["queue", "async", "backpressure", "distributed"],
        "use_cases": [
            "**Queue Design** - RabbitMQ, SQS, Kafka, message routing and reliability",
            "**Async Processing** - Worker pools, job scheduling, retry strategies",
            "**Backpressure Management** - Rate limiting, circuit breakers, flow control",
            "**Distributed Systems** - CAP theorem, consensus, eventual consistency"
        ]
    },
    "ux-product": {
        "display_name": "UX & Product Strategy",
        "tagline": "User-centered design and product excellence",
        "description": "Master user research, UX design, accessibility, product strategy, user journey mapping, and inclusive design practices.",
        "commands": ["ux", "product", "user-research", "journey"],
        "use_cases": [
            "**UX Design** - User research, wireframes, prototypes, usability testing",
            "**Product Strategy** - Roadmap planning, prioritization, OKRs, market fit",
            "**Accessibility** - WCAG compliance, screen reader support, inclusive design",
            "**User Journey Mapping** - Flow optimization, friction analysis, touchpoints"
        ]
    },
    "project-delivery": {
        "display_name": "Agile Project Delivery",
        "tagline": "Project orchestration from planning to delivery",
        "description": "Master Scrum, Kanban, sprint planning, roadmaps, retrospectives, team metrics, and stakeholder management.",
        "commands": ["plan", "roadmap", "retro", "metrics", "stakeholder"],
        "use_cases": [
            "**Sprint Planning** - Story estimation, velocity tracking, capacity planning",
            "**Roadmap Management** - Milestone planning, dependency tracking, timeline optimization",
            "**Team Optimization** - Retrospectives, metrics analysis, process improvement",
            "**Stakeholder Management** - Communication planning, expectation alignment, status updates"
        ]
    },
    "cli-mastery": {
        "display_name": "CLI Excellence & Unix Wizardry",
        "tagline": "Command-line excellence from a 10+ year terminal native",
        "description": "Expert in shell scripting, Unix pipelines, text processing (sed/awk/grep), permissions, and CLI tool composition.",
        "commands": ["cli", "pipe", "shell", "permissions", "text"],
        "use_cases": [
            "**CLI Tool Selection** - Unix philosophy, tool composition, minimal dependencies",
            "**Pipeline Design** - Data flow optimization, stream processing, filter-map-reduce",
            "**Shell Scripting** - Robust automation, error handling, POSIX compliance",
            "**Text Processing** - sed, awk, grep mastery for complex transformations"
        ]
    }
}

def create_readme(plugin_name, plugin_data):
    """Create README.md for a plugin."""
    commands_list = "\n".join([f'- **`/{cmd}`**' for cmd in plugin_data['commands']])
    use_cases_list = "\n".join([f"- {uc}" for uc in plugin_data['use_cases']])

    examples = "\n".join([f'/{cmd} "example usage"' for cmd in plugin_data['commands'][:2]])

    content = f"""# {plugin_data['display_name']}

**{plugin_data['tagline']}**

{plugin_data['description']}

## 🎯 Commands

{commands_list}

## 📦 Installation

```bash
# Add the dotclaude marketplace
/plugin marketplace add dotclaude/marketplace

# All plugins install automatically with the marketplace
```

## 🚀 Quick Start

```bash
{examples}
```

## 💡 Use Cases

{use_cases_list}

## 📄 License

MIT License - see LICENSE file for details

## 🌟 Part of the DotClaude Ecosystem

Complete development pipeline with 14 specialized plugins:
- **Cognitive Orchestration** - Multi-expert decision making
- **Adaptive Learning** - Skill building and teaching
- **Dev Accelerator** - TDD and development workflows
- **Insight Engine** - Meta-cognitive analysis
- **Personalities** - Multi-persona problem solving
- **{plugin_data['display_name']}** - This plugin
- [8 more plugins](https://github.com/dotclaude/marketplace)

---

**Ready to get started?** Install the marketplace and access all DotClaude plugins.
"""

    file_path = BASE_DIR / plugin_name / "README.md"
    file_path.write_text(content)
    print(f"Created: {file_path}")

def create_gitignore(plugin_name):
    """Create .gitignore for a plugin."""
    file_path = BASE_DIR / plugin_name / ".gitignore"
    file_path.write_text(GITIGNORE_CONTENT)
    print(f"Created: {file_path}")

def main():
    """Generate all README and .gitignore files."""
    print("=" * 80)
    print("Creating README.md and .gitignore files...")
    print("=" * 80)

    for plugin_name, plugin_data in PLUGINS.items():
        print(f"\n### Processing {plugin_name}")
        create_readme(plugin_name, plugin_data)
        create_gitignore(plugin_name)

    print("\n" + "=" * 80)
    print("All documentation complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
