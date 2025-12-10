---
model: claude-sonnet-4-0
allowed-tools: Task
argument-hint: <proposition-or-claim> [intensity-level]
description: Structured debate with opposing personas examining a proposition from multiple angles through productive disagreement
---

# Multi-Persona Debate Command

Orchestrate structured debate around a proposition or claim, featuring opposing perspectives that challenge assumptions and explore alternatives through productive disagreement.

## How It Works

This command creates a debate-focused analysis where:
1. Multiple personas examine the proposition critically
2. Constructive critics challenge the mainstream view
3. Alternative approaches are systematically generated
4. Assumptions are tested through first-principles thinking
5. Synthesis reveals robust insights from creative tension

## Arguments

**$1 (Required)**: Proposition, claim, or approach to debate

**$2 (Optional)**: Level of challenging scrutiny
- `balanced`: Respectful challenge with alternatives (default)
- `rigorous`: Systematic assumption testing
- `maximum`: Aggressive first-principles questioning

## Examples

### Balanced Debate
```bash
/debate "We should adopt microservices architecture"
```
Personas explore benefits, challenges, alternatives, and contexts where the proposition holds or fails.

### Rigorous Scrutiny
```bash
/debate "TypeScript provides better developer experience than JavaScript" rigorous
```
Deep assumption testing, edge case exploration, systematic challenge of premises.

### Maximum Challenge
```bash
/debate "Code review improves code quality" maximum
```
First-principles questioning, counterintuitive alternatives, paradigm-level examination.

## Use Cases

**Technology Decisions**
- Debate framework choices
- Challenge architectural assumptions
- Evaluate tool adoption proposals

**Best Practices**
- Question conventional wisdom
- Test methodology assumptions
- Explore alternative approaches

**Strategic Direction**
- Challenge product roadmap decisions
- Debate market positioning
- Question resource allocation

**Process & Culture**
- Evaluate team practices
- Challenge organizational assumptions
- Explore alternative workflows

## Debate Structure

### Phase 1: Proposition Framing
- Establish the claim or approach being examined
- Clarify context and underlying assumptions

### Phase 2: Supportive Analysis
- Personas (Systems Architect, Analytical Thinker) examine merits
- Identify contexts where proposition holds
- Document supporting evidence and reasoning

### Phase 3: Critical Challenge
- Constructive Critic and Risk Analyst systematically challenge
- Test assumptions through first-principles thinking
- Generate alternative approaches

### Phase 4: Alternative Exploration
- Creative Innovator proposes unconventional alternatives
- Pragmatic Realist assesses practical viability
- Explore edge cases and boundary conditions

### Phase 5: Synthesis
- Coordinator integrates insights from debate
- Clarify contexts where proposition works vs. fails
- Provide nuanced recommendations

## What You Get

1. **Assumption Audit**: Systematic identification of hidden premises
2. **Alternative Approaches**: Multiple options beyond the original proposition
3. **Context Clarity**: Understanding when the proposition holds or fails
4. **Robust Insights**: Solutions strengthened through critical examination
5. **Nuanced Recommendations**: Avoiding false dichotomies and oversimplification

## Split-Team Principles in Debate

**Productive Disagreement**: Constructive challenge strengthens understanding

**First-Principles Thinking**: Break assumptions down to fundamental truths

**Alternative Generation**: Explore options beyond binary choices

**Evidence-Based Challenge**: Ground disagreement in logic and data

## Tips for Effective Debates

1. **Frame Clearly**: State the proposition precisely
2. **Provide Context**: Include relevant constraints and goals
3. **Embrace Challenge**: Dissent reveals blind spots
4. **Seek Nuance**: Avoid forcing binary yes/no conclusions
5. **Value Alternatives**: Often the best solution emerges from synthesis

## Example Session

```bash
/debate "We should prioritize velocity over code quality to meet market deadlines" rigorous
```

**Result**: Personas systematically challenge this false dichotomy, explore hidden assumptions (quality vs. velocity trade-off, technical debt impact), generate alternatives (quality-enabling speed, incremental quality), and synthesize nuanced guidance about when to optimize for speed vs. when quality accelerates delivery.

## Debate Output Format

```markdown
## Debate: [Proposition]

### Proposition Framing
[Clear statement and context]

### Supporting Analysis
- [Supportive persona perspectives]
- [Contexts where proposition holds]

### Critical Challenge
- [Systematic assumption testing]
- [First-principles questioning]
- [Alternative approaches]

### Creative Alternatives
- [Unconventional options]
- [Edge case exploration]

### Synthesis & Recommendations
[Nuanced guidance integrating debate insights]
[Context-dependent recommendations]
[Acknowledged trade-offs]
```

Invoke the persona-coordinator agent with debate mode: $ARGUMENTS
