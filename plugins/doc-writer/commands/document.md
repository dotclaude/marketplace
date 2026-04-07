---
model: sonnet
allowed-tools: Task, Read, Write, Bash(*), Glob, Grep
argument-hint: <topic> [doc-type] [audience]
description: Multi-persona documentation authoring using split-team framework with research, drafting, review, and refinement phases coordinated by specialized documentation personas
---

# Multi-Persona Document Authoring Command

Orchestrate high-quality technical documentation through a team of specialized documentation personas. The team researches, drafts, reviews, and refines documents through structured before/during/after workflow phases.

## How It Works

This command invokes the doc-coordinator agent to:
1. Analyze your topic and determine the best document type
2. Assemble an optimal team of 4-8 documentation-specialized personas
3. Research available source material (code, specs, existing docs)
4. Present a Document Plan for your approval
5. Draft the document following the approved structure
6. Review for accuracy, clarity, and audience-appropriateness
7. Iterate based on your feedback until the document meets quality bar

## Arguments

**$1 (Required)**: Topic, system, or subject to document

**$2 (Optional)**: Document type
- `api`: API Reference Guide — endpoints, schemas, auth, errors
- `wiki`: Wiki Page — internal knowledge base article, runbook, decision record
- `overview`: System Overview — high-level architecture, data flows, "how it works"
- `trace`: Trace Document — end-to-end request flow through the system
- `onboarding`: Onboarding Guide — getting started for new team members or consumers
- `adr`: Architecture Decision Record — structured decision documentation
- `consumer-guide`: Consumer Team Guide — integration docs for downstream teams
- If not specified, the coordinator analyzes the topic and determines the best type

**$3 (Optional)**: Target audience
- `developer`: Software engineers integrating or maintaining the system
- `team-lead`: Technical leads needing architectural understanding
- `new-hire`: New team members getting up to speed
- `external-consumer`: External teams or third-party developers
- If not specified, the coordinator infers the audience from context

## Examples

### Auto-Detected Document Type
```bash
/document "Payment Processing Service"
```
Coordinator analyzes the topic, determines the best document type (likely System Overview or API Reference), assembles the optimal team, and presents a Document Plan before proceeding.

### API Reference Guide
```bash
/document "User Authentication API" api developer
```
Assembles: API Specialist (lead) + Domain Researcher + Accuracy Reviewer + Technical Writer + Audience Advocate
Produces: Complete endpoint documentation with auth flows, request/response schemas, error codes, and code examples.

### System Overview
```bash
/document "How our event-driven order pipeline works" overview team-lead
```
Assembles: Information Architect (lead) + Domain Researcher + Technical Writer + Clarity Editor + Audience Advocate
Produces: High-level architecture doc with component interactions, data flows, and design rationale.

### Trace Document
```bash
/document "How a payment flows from checkout to settlement" trace developer
```
Assembles: Domain Researcher (lead) + Technical Writer + Accuracy Reviewer + Information Architect
Produces: End-to-end request flow showing how data moves through each system component.

### Onboarding Guide
```bash
/document "Getting started with the Data Platform" onboarding new-hire
```
Assembles: Audience Advocate (lead) + Technical Writer + Domain Researcher + Information Architect + Clarity Editor
Produces: Step-by-step getting started guide with prerequisites, setup instructions, and first-task walkthroughs.

### Consumer Team Guide
```bash
/document "Integrating with the Notification Service" consumer-guide external-consumer
```
Assembles: Technical Writer (lead) + API Specialist + Audience Advocate + Domain Researcher + Clarity Editor
Produces: Integration guide with SDK setup, authentication, common patterns, and troubleshooting.

### Architecture Decision Record
```bash
/document "Why we chose PostgreSQL over DynamoDB for user data" adr developer
```
Assembles: Domain Researcher + Technical Writer + Accuracy Reviewer + Audience Advocate
Produces: Structured ADR with context, decision, alternatives considered, consequences, and status.

### Wiki Page
```bash
/document "Incident Response Runbook for Database Failover" wiki
```
Assembles: Technical Writer (lead) + Domain Researcher + Accuracy Reviewer + Clarity Editor
Produces: Internal wiki article with step-by-step procedures, escalation paths, and recovery verification.

## Workflow Phases

### BEFORE — Research & Planning
1. Doc Coordinator analyzes the request and determines document type
2. Domain Researcher gathers raw context (reads code, traces flows, extracts concepts)
3. Information Architect proposes document structure and outline
4. Audience Advocate defines the target reader profile and their needs
5. Team presents a **Document Plan** to you for approval

### DURING — Drafting & Assembly
1. Lead writer (Technical Writer or API Specialist) produces the first draft
2. API Specialist handles API-specific sections (endpoints, schemas, examples)
3. Domain Researcher fills in technical details and edge cases
4. Doc Coordinator manages section integration and consistency

### AFTER — Review & Refinement
1. Accuracy Reviewer validates all technical claims against source material
2. Clarity Editor reviews for readability, tone, and audience-appropriateness
3. Audience Advocate confirms the document serves its intended readers
4. Doc Coordinator synthesizes review feedback and coordinates revisions
5. Team iterates based on your feedback until the document meets quality bar

## Document Types at a Glance

| Type | Best For | Typical Team Size |
|------|----------|-------------------|
| API Reference | Endpoint documentation, schemas, auth | 4-6 personas |
| Consumer Guide | Integration docs for downstream teams | 5-6 personas |
| System Overview | "How it works" architecture docs | 4-5 personas |
| Wiki Page | Internal knowledge base, runbooks | 3-5 personas |
| Trace Document | End-to-end request flow documentation | 4-5 personas |
| Onboarding Guide | Getting started for new users/members | 5-6 personas |
| ADR | Structured decision records | 3-4 personas |

## What You Get

1. **Document Plan**: Proposed structure, audience profile, and team composition — presented for your approval before any drafting begins
2. **Research Foundation**: Source material gathered and organized by Domain Researcher with traceability
3. **Structured Draft**: Well-organized document following progressive disclosure (overview → details → reference)
4. **Multi-Perspective Review**: Accuracy, clarity, and audience-fit validated by specialized reviewers
5. **Iterative Refinement**: Multiple revision cycles incorporating your feedback
6. **Production-Ready Output**: Polished Markdown document with consistent formatting, cross-references, and metadata

## Quality Principles

**Progressive Disclosure**: Documents layer complexity from overview to details to reference material

**Example-First**: Concrete examples precede abstract explanations

**Audience-Appropriate**: Language and depth match the target reader's skill level

**Traceable**: Technical claims link back to source code, specs, or authoritative references

**Cross-Referenced**: Related concepts, APIs, and documents are linked where appropriate

## Tips for Best Results

1. **Provide Context**: Share relevant code paths, specs, or existing docs the team can reference
2. **Specify Audience**: The more clearly you define who will read this, the better the result
3. **Trust the Plan**: Review and approve the Document Plan — it shapes the entire output
4. **Give Feedback**: The after-phase review cycle is designed for your input — use it
5. **Iterate**: Complex documents benefit from multiple refinement passes

Invoke the doc-coordinator agent with: $ARGUMENTS
