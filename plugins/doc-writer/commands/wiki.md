---
model: sonnet
allowed-tools: Task, Read, Write, Bash(*), Glob, Grep
argument-hint: <topic> [depth]
description: Wiki page documentation shortcut — assembles a knowledge-base focused persona team to produce internal wiki articles, runbooks, decision records, and knowledge base entries
---

# Wiki Page Documentation Command

Shortcut for producing internal wiki pages and knowledge base articles. Pre-selects the Wiki document type and assembles a knowledge-base focused documentation team to produce well-structured internal articles, runbooks, how-to guides, and decision records.

## How It Works

This command invokes the doc-coordinator agent in Wiki mode to:
1. Assemble a wiki-focused team (Technical Writer lead + Domain Researcher + Accuracy Reviewer)
2. Research the topic from available source material
3. Present a Wiki Document Plan for your approval
4. Draft a well-structured knowledge base article
5. Review for accuracy and readability
6. Iterate based on your feedback

## Arguments

**$1 (Required)**: Topic or subject for the wiki article

**$2 (Optional)**: Depth of coverage
- `overview`: Quick reference, key points only (1-2 pages)
- `detailed`: Standard wiki article with full explanation (default, 3-5 pages)
- `comprehensive`: In-depth reference with examples, edge cases, and related topics (5+ pages)

## Examples

### Standard Wiki Article
```bash
/wiki "Database Connection Pooling Configuration"
```
Produces a standard-depth wiki article covering configuration options, best practices, and common issues.

### Quick Overview
```bash
/wiki "Feature Flag System" overview
```
Produces a concise overview covering what the system is, how to use it, and where to find more details.

### Comprehensive Reference
```bash
/wiki "Incident Response Procedures" comprehensive
```
Produces an in-depth runbook with step-by-step procedures, escalation paths, decision trees, recovery verification, and post-incident review templates.

### How-To Guide
```bash
/wiki "How to Set Up Local Development Environment"
```
Produces a step-by-step guide with prerequisites, installation steps, verification, and troubleshooting.

### Decision Record
```bash
/wiki "Why We Chose Kafka Over RabbitMQ for Event Streaming"
```
Produces a structured decision record with context, options evaluated, decision rationale, and consequences.

### Runbook
```bash
/wiki "Redis Cache Invalidation Runbook" comprehensive
```
Produces a detailed operational runbook with monitoring, diagnosis, remediation steps, and verification procedures.

## Wiki Article Types

The coordinator detects the article type from your topic:

| Signal | Article Type | Structure |
|--------|-------------|-----------|
| "How to...", setup, configure | **How-To Guide** | Prerequisites → Steps → Verification → Troubleshooting |
| Procedures, runbook, incident | **Runbook** | Overview → Monitoring → Diagnosis → Remediation → Verification |
| "Why we chose...", decision, trade-offs | **Decision Record** | Context → Options → Decision → Consequences |
| System, service, component | **Knowledge Article** | Overview → Architecture → Key Concepts → Configuration → FAQ |
| Process, workflow, lifecycle | **Process Guide** | Overview → Phases → Roles → Tools → Exceptions |

## Team Composition

| Persona | Role in Wiki Docs |
|---------|------------------|
| **Technical Writer** (Lead) | Structures and writes the article with clear, scannable prose |
| **Domain Researcher** | Gathers technical context, identifies key concepts and edge cases |
| **Accuracy Reviewer** | Validates all technical claims and procedures against source material |
| **Information Architect** | Added for comprehensive depth — structures navigation and cross-references |
| **Clarity Editor** | Added for broad-audience articles — reduces jargon and ensures accessibility |

## Depth Guidelines

### Overview Depth
- 1-2 pages
- Key concepts and quick reference
- "What is it?" and "How do I use it?" focus
- Links to detailed resources for further reading
- 3 personas: Technical Writer + Domain Researcher + Accuracy Reviewer

### Detailed Depth (Default)
- 3-5 pages
- Full explanation with examples
- Configuration options, best practices, and common pitfalls
- Cross-references to related topics
- 3-4 personas: Technical Writer + Domain Researcher + Accuracy Reviewer + Clarity Editor

### Comprehensive Depth
- 5+ pages
- In-depth reference with exhaustive coverage
- Edge cases, troubleshooting, and advanced configuration
- Decision rationale and historical context
- Visual aids (diagrams, flowcharts, tables)
- 5 personas: Technical Writer + Domain Researcher + Accuracy Reviewer + Information Architect + Clarity Editor

## Output Format

```markdown
## [Wiki Article Title]

### Metadata
- **Category**: [Knowledge Article | How-To Guide | Runbook | Decision Record | Process Guide]
- **Audience**: [Internal engineering team]
- **Last Updated**: [Date]
- **Owner**: [Team or individual]

---

### Overview
[Brief summary — what this article covers and why it matters]

### [Core Content Sections]
[Structured based on article type — see Wiki Article Types above]

### Related Topics
- [Link to related wiki article 1]
- [Link to related wiki article 2]
- [Link to related wiki article 3]

### FAQ
[Common questions and quick answers]

### Changelog
[History of significant updates to this article]
```

## Tips for Best Wiki Articles

1. **Be Specific**: Narrow topics produce better articles than broad ones
2. **Share Context**: Mention what team owns this, what systems are involved
3. **Specify Depth**: Use `overview` for quick references, `comprehensive` for runbooks
4. **Include Constraints**: Mention if the article needs to follow a specific wiki template
5. **Link Existing Docs**: Reference any existing documentation the team should be aware of

Invoke the doc-coordinator agent with Wiki mode: $ARGUMENTS
