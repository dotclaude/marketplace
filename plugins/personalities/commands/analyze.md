---
model: claude-sonnet-4-0
allowed-tools: Task
argument-hint: <problem-or-question> [complexity-level] [perspective-count]
description: Multi-persona analysis using split-team framework with cognitive harmonics and productive disagreement
---

# Multi-Persona Analysis Command

Orchestrate sophisticated multi-perspective analysis of problems using the split-team framework. Assemble optimal persona teams, facilitate cognitive harmonics, and synthesize insights through productive disagreement.

## How It Works

This command invokes the persona-coordinator agent to:
1. Analyze your problem and determine required perspectives
2. Assemble an optimal team of 3-7 persona agents
3. Orchestrate divergent analysis from each perspective
4. Facilitate productive disagreement and assumption challenging
5. Synthesize insights into coherent, actionable recommendations

## Arguments

**$1 (Required)**: Problem statement or question to analyze

**$2 (Optional)**: Complexity level
- `simple`: 3-4 personas, straightforward analysis
- `moderate`: 5-6 personas, balanced trade-offs (default)
- `complex`: 7+ personas, multifaceted challenges

**$3 (Optional)**: Number of personas (3-10)
- Overrides complexity-based team size
- Must be between 3 and 10

## Examples

### Simple Analysis
```bash
/analyze "Should we use REST or GraphQL for our API?" simple
```
Assembles: Analytical Thinker + Pragmatic Realist + Systems Architect

### Moderate Analysis (Default)
```bash
/analyze "Design an authentication system for our platform"
```
Assembles: Systems Architect + Risk Analyst + User Advocate + Pragmatic Realist + Constructive Critic

### Complex Analysis
```bash
/analyze "Should we migrate from monolith to microservices?" complex
```
Assembles: Systems Architect + Risk Analyst + Pragmatic Realist + Creative Innovator + Constructive Critic + User Advocate + Analytical Thinker

### Custom Team Size
```bash
/analyze "Evaluate our tech stack choices" moderate 6
```
Assembles: 6 most relevant personas for the problem

## Use Cases

**Architecture Decisions**
- Technology selection
- System design choices
- Migration strategies
- Scaling approaches

**Product Strategy**
- Feature prioritization
- User experience design
- Market positioning
- Competitive analysis

**Technical Challenges**
- Performance optimization
- Security hardening
- Debugging complex issues
- Code architecture review

**Strategic Planning**
- Long-term technology roadmap
- Resource allocation
- Risk assessment
- Innovation opportunities

## What You Get

1. **Diverse Perspectives**: Each persona contributes unique insights through their specialized lens
2. **Productive Disagreement**: Constructive challenge of assumptions and alternatives
3. **Cognitive Harmonics**: Emergent insights from persona interactions
4. **Synthesis**: Coherent integration of perspectives with clear recommendations
5. **Trade-off Clarity**: Explicit acknowledgment of competing concerns and balanced choices

## Split-Team Framework Principles

**Voice Differentiation**: Each persona maintains unique vocabulary, questions, and analytical approach

**Cognitive Harmonics**: Multiple perspectives create constructive interference for emergent insights

**Productive Disagreement**: Systematic challenge strengthens solutions and prevents groupthink

**Integration Synthesis**: Coordinator weaves perspectives into coherent, actionable guidance

## Tips for Best Results

1. **Be Specific**: Provide context and constraints in your problem statement
2. **State Goals**: Mention success criteria or what you're optimizing for
3. **Match Complexity**: Use simple for straightforward questions, complex for critical decisions
4. **Trust the Process**: Persona disagreement is valuable, not problematic
5. **Implementation Focus**: Include practical constraints for realistic recommendations

## Example Session

```bash
/analyze "We need to choose between PostgreSQL and MongoDB for user data storage. We have 10M users, need strong consistency, but want flexibility for future features." moderate
```

**Result**: Assembles 5 personas who examine through data/performance (Analytical Thinker), implementation reality (Pragmatic Realist), system architecture (Systems Architect), risk factors (Risk Analyst), and challenges assumptions (Constructive Critic). Synthesis provides clear recommendation with rationale and acknowledged trade-offs.

Invoke the persona-coordinator agent with: $ARGUMENTS
