---
model: claude-sonnet-4-0
allowed-tools: Task
argument-hint: <solution-or-proposal> [focus-areas]
description: Multi-persona evaluation of solutions or proposals through diverse expert lenses with comprehensive assessment
---

# Multi-Persona Evaluation Command

Evaluate solutions, proposals, or designs through multiple expert perspectives, providing comprehensive assessment of strengths, weaknesses, risks, and opportunities.

## How It Works

This command creates evaluation-focused analysis where:
1. Multiple personas assess the solution from their expertise
2. Each perspective applies distinct evaluation criteria
3. Strengths and weaknesses are systematically identified
4. Risks and opportunities are comprehensively assessed
5. Synthesis provides balanced evaluation with improvement recommendations

## Arguments

**$1 (Required)**: Solution, proposal, or design to evaluate

**$2 (Optional)**: Focus areas for evaluation (comma-separated)
- Examples: `security,performance`, `usability,scalability`, `cost,maintainability`
- If not specified, uses comprehensive multi-dimensional assessment

## Examples

### General Evaluation
```bash
/evaluate "We'll use Redis for caching, PostgreSQL for data, and Next.js on the frontend"
```
Comprehensive assessment from all relevant perspectives.

### Focused Evaluation
```bash
/evaluate "Authentication via JWT tokens stored in localStorage" security,usability
```
Security and user experience focused assessment.

### Architecture Evaluation
```bash
/evaluate "Microservices with event-driven communication via Kafka" scalability,complexity,reliability
```
Focused on scale, complexity, and reliability dimensions.

## Use Cases

**Architecture Review**
- Evaluate system designs
- Assess technology choices
- Review integration patterns

**Feature Assessment**
- Evaluate product proposals
- Assess user experience designs
- Review feature implementation approaches

**Security Review**
- Evaluate authentication mechanisms
- Assess security architectures
- Review access control designs

**Performance Evaluation**
- Assess optimization approaches
- Evaluate scaling strategies
- Review caching designs

## Evaluation Dimensions

### Technical Assessment
- **Systems Architect**: Structural soundness, scalability, integration
- **Analytical Thinker**: Performance metrics, efficiency, measurability

### Risk & Feasibility
- **Risk Analyst**: Failure modes, vulnerabilities, contingencies
- **Pragmatic Realist**: Implementation feasibility, resource requirements

### Innovation & Alternatives
- **Creative Innovator**: Opportunities for improvement, alternative approaches
- **Constructive Critic**: Assumption testing, overlooked considerations

### User & Experience
- **User Advocate**: User experience, accessibility, human impact

## Evaluation Framework

### Phase 1: Solution Understanding
- Coordinator establishes what's being evaluated
- Clarifies context, goals, and constraints

### Phase 2: Multi-Dimensional Assessment
Each persona evaluates through their lens:
- **Strengths**: What works well from this perspective
- **Weaknesses**: Gaps, limitations, concerns
- **Risks**: What could go wrong
- **Opportunities**: How to improve or enhance

### Phase 3: Comprehensive Synthesis
- Integrate assessments across dimensions
- Identify critical issues requiring attention
- Highlight notable strengths
- Recommend improvements
- Provide overall assessment

## What You Get

1. **Comprehensive Coverage**: Assessment from technical, user, risk, and innovation perspectives
2. **Balanced View**: Both strengths and weaknesses identified
3. **Risk Identification**: Potential problems surfaced early
4. **Improvement Opportunities**: Actionable suggestions for enhancement
5. **Overall Assessment**: Clear recommendation on viability

## Output Format

```markdown
## Multi-Persona Evaluation: [Solution]

### Solution Overview
[What's being evaluated and context]

### Dimensional Assessments

#### Systems Architect Evaluation
**Strengths**: [Positive aspects]
**Concerns**: [Architectural issues]
**Recommendations**: [Improvements]

#### Risk Analyst Assessment
**Strengths**: [Risk-mitigation strengths]
**Vulnerabilities**: [Risk factors]
**Recommendations**: [Risk mitigation strategies]

[Continue for each persona]

### Synthesis & Overall Assessment

**Critical Strengths**: [Top 3 positive aspects]

**Key Concerns**: [Top 3 issues requiring attention]

**Risk Summary**: [High/Medium/Low with key factors]

**Improvement Recommendations**:
1. [Priority improvement 1]
2. [Priority improvement 2]
3. [Priority improvement 3]

**Overall Assessment**: [Clear evaluation with context]
```

## Tips for Best Evaluations

1. **Provide Context**: Include goals, constraints, alternatives considered
2. **Be Specific**: Detailed proposals get detailed assessments
3. **State Priorities**: Mention what's most important (speed vs. quality, etc.)
4. **Include Criteria**: Use second argument for focused evaluation
5. **Expect Balanced**: Good solutions have trade-offs; perfect solutions don't exist

## Example Session

```bash
/evaluate "We'll implement real-time features using WebSockets with Redis pub/sub for scaling across servers. Fallback to long-polling for older browsers." scalability,reliability,complexity
```

**Result**: Systems Architect assesses scalability approach, Risk Analyst evaluates reliability and failure modes, Pragmatic Realist considers implementation complexity, Constructive Critic challenges assumptions about scaling needs. Synthesis provides balanced assessment with improvement suggestions like connection management, monitoring strategies, and fallback testing.

Invoke the persona-coordinator agent with evaluation mode: $ARGUMENTS
