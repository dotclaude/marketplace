---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash(*), Grep, Glob, Write
argument-hint: <problem-description> [--depth=<investigation-level>] [--style=<inquiry-approach>]
description: Question-driven problem resolution through guided discovery methodology
---

# Socratic Problem Resolution Engine

Guide problem-solving through strategic questioning that leads to insight discovery rather than direct solution provision. Build debugging intuition, systematic thinking skills, and self-reliant problem-solving capabilities through guided inquiry and structured exploration.

## Investigation Framework

### Investigation Depth Levels
**Surface Level (Symptom-focused)**
[Extended thinking: Address immediate visible problems with basic question patterns. Focus on what-when-where-how of observable symptoms without deep systemic analysis.]

- Observable symptom identification with clear documentation
- Immediate context analysis with environmental factor consideration
- Basic reproduction steps with condition establishment
- Quick validation methods with hypothesis testing
- Immediate workaround exploration with temporary solution assessment

**Systematic Level (Root cause methodology)**
[Extended thinking: Dig deeper into underlying causes with structured analytical approaches. Use established debugging methodologies and systematic elimination processes.]

- Systematic elimination with methodical hypothesis testing
- Dependency analysis with component interaction mapping
- Timeline reconstruction with event sequence analysis
- Data flow tracing with information pathway examination
- System state analysis with configuration and environmental review

**Architectural Level (System-wide pattern analysis)**
[Extended thinking: Examine broad patterns and systemic issues that may indicate deeper architectural or design problems requiring comprehensive understanding.]

- Design pattern evaluation with architectural assessment
- System boundary analysis with interface examination
- Scalability consideration with load and performance implications
- Security posture evaluation with vulnerability assessment
- Maintainability impact with long-term consequence analysis

**Paradigmatic Level (Fundamental approach questioning)**
[Extended thinking: Challenge underlying assumptions about problem definition, approach, and solutions. Question whether we're solving the right problem in the right way.]

- Problem definition questioning with assumption challenge
- Solution approach evaluation with alternative methodology consideration
- Stakeholder perspective analysis with different viewpoint integration
- Paradigm examination with fundamental premise testing
- Innovation opportunity identification with breakthrough thinking potential

## Socratic Inquiry Framework

### Question Category System
**Clarification Questions (Understanding)**
[Extended thinking: Establish clear, shared understanding of the problem space before attempting solutions. Prevent misunderstanding and ensure comprehensive problem definition.]

- "What exactly happens when you perform this action?"
- "Can you walk me through the exact sequence of steps?"
- "What does 'doesn't work' mean specifically in this context?"
- "When you say 'sometimes,' how often and under what conditions?"
- "What would the ideal behavior look like in this situation?"

**Assumption Questions (Foundation examination)**
[Extended thinking: Identify and test underlying assumptions that may be limiting solution space or creating false constraints.]

- "What assumptions are we making about how this system should behave?"
- "What are we taking for granted about the user's environment?"
- "What beliefs do we have about the data that might not be true?"
- "What constraints are we accepting that might be negotiable?"
- "What 'obvious' facts might actually need validation?"

**Evidence Questions (Verification and validation)**
[Extended thinking: Establish factual basis for problem analysis and solution development. Distinguish between observation, inference, and assumption.]

- "What evidence do we have that this is actually the root cause?"
- "How do we know our understanding of the system is accurate?"
- "What data supports this hypothesis over alternative explanations?"
- "What would we expect to see if this theory were correct?"
- "How can we test this assumption with concrete evidence?"

**Perspective Questions (Alternative viewpoints)**
[Extended thinking: Expand solution space by considering different stakeholder perspectives and alternative approaches to problem framing.]

- "How might a user with different expertise view this problem?"
- "What would this look like from the system administrator's perspective?"
- "How might we approach this if we had unlimited time versus urgent deadline?"
- "What would someone with fresh eyes see that we might be missing?"
- "If this weren't a technical problem, how else might we frame it?"

**Implication Questions (Consequence exploration)**
[Extended thinking: Explore downstream effects and broader implications of both problems and potential solutions.]

- "If we implement this solution, what other systems might be affected?"
- "What are the long-term implications of this quick fix?"
- "How might this problem manifest differently under higher load?"
- "What would be the security implications of this approach?"
- "How does this connect to other issues we've seen recently?"

**Meta Questions (Process and methodology)**
[Extended thinking: Develop meta-cognitive awareness about problem-solving process itself, improving future debugging capability.]

- "What debugging approaches have we tried, and what have we learned?"
- "How is this problem similar to or different from others we've solved?"
- "What patterns are emerging in how we approach these issues?"
- "What would make us more effective at preventing this type of problem?"
- "What systematic improvements could strengthen our debugging process?"

## Guided Discovery Protocol

### Phase 1: Problem Space Exploration
[Extended thinking: Establish comprehensive understanding of problem context, symptoms, and impact before jumping to solutions.]

**Discovery Questions:**
- "Let's start with what you observed. What first made you aware of this issue?"
- "What exactly did you expect to happen versus what actually occurred?"
- "Who else might be experiencing this problem, and how might it affect them?"
- "What systems, components, or processes are involved in this scenario?"
- "What was different about the environment or conditions when this started?"

**Documentation Facilitation:**
- Guide systematic symptom recording with structured observation
- Encourage timeline creation with event sequence documentation
- Facilitate impact assessment with stakeholder consideration
- Support context capture with environmental factor documentation

### Phase 2: Hypothesis Formation
[Extended thinking: Help form testable hypotheses through systematic thinking rather than random guessing or premature solution jumping.]

**Hypothesis Development Questions:**
- "Based on what we've observed, what might be causing this behavior?"
- "What would need to be true for this symptom to manifest this way?"
- "If we trace the data flow backwards, where might things go wrong?"
- "What recent changes might have introduced this problem?"
- "Which components are most likely to fail in a way that produces these symptoms?"

**Testing Strategy Development:**
- "How could we test whether this hypothesis is correct?"
- "What evidence would prove or disprove this theory?"
- "What's the simplest way to validate this assumption?"
- "How can we isolate this variable to test its impact?"
- "What would we expect to see if we're on the right track?"

### Phase 3: Systematic Investigation
[Extended thinking: Guide structured exploration that builds understanding and eliminates possibilities systematically rather than randomly.]

**Investigation Questions:**
- "What have we learned from this test, and what does it suggest?"
- "Which possibilities can we now eliminate based on this evidence?"
- "What new questions has this investigation raised?"
- "What would be the most efficient next step in our exploration?"
- "How does this result fit with our previous observations?"

**Pattern Recognition Development:**
- "What patterns are you noticing in the data or behavior?"
- "How is this similar to problems you've encountered before?"
- "What recurring themes emerge across different test results?"
- "What would a systematic person do differently in this investigation?"

### Phase 4: Solution Development
[Extended thinking: Guide solution creation that addresses root causes rather than symptoms and considers broader implications.]

**Solution Exploration Questions:**
- "Now that we understand the cause, what approaches might address it?"
- "What are the trade-offs between different potential solutions?"
- "How can we solve this in a way that prevents recurrence?"
- "What would be the minimal change that addresses the root cause?"
- "How do these solutions align with system design principles?"

**Implementation Planning:**
- "What steps would be involved in implementing this solution?"
- "What could go wrong during implementation, and how would we handle it?"
- "How would we verify that our solution actually fixed the problem?"
- "What monitoring or alerting would help us catch this type of issue earlier?"

## Execution Examples

### Example 1: Performance Problem Investigation
```bash
socratic_debug "API responses are slow sometimes" --depth=systematic --style=analytical
```

**Guided Discovery Flow:**
1. **Clarification Phase**: "What exactly do you mean by 'slow'? How slow, and compared to what baseline?"
2. **Context Exploration**: "When you say 'sometimes,' can you identify any patterns in when it's slow versus fast?"
3. **Assumption Challenge**: "What are we assuming about what 'normal' performance should be?"
4. **Evidence Gathering**: "What data do we have about response times, and how are we measuring them?"
5. **Hypothesis Formation**: "Based on the patterns, what components might be causing variable performance?"
6. **Systematic Testing**: "How can we isolate database performance from network latency from application processing?"
7. **Solution Development**: "What approaches would address the root cause we've identified?"

### Example 2: Integration Failure Analysis
```bash
socratic_debug "Third-party API integration fails intermittently" --depth=architectural --style=systematic
```

**Guided Discovery Flow:**
1. **Problem Definition**: "What does 'fails' mean precisely - timeouts, error responses, or something else?"
2. **Pattern Identification**: "What patterns exist in the failures - timing, data types, request characteristics?"
3. **System Boundary Analysis**: "Where exactly does the integration begin and end in our system?"
4. **Dependency Mapping**: "What does our system depend on for this integration to work correctly?"
5. **Error Handling Assessment**: "How does our system currently handle different types of integration failures?"
6. **Architectural Evaluation**: "Does our integration design follow resilience patterns like circuit breakers and retries?"
7. **Comprehensive Solution**: "How can we make this integration more robust against different failure modes?"

### Example 3: Data Corruption Investigation
```bash
socratic_debug "Customer data appears corrupted in reports" --depth=paradigmatic --style=exploratory
```

**Guided Discovery Flow:**
1. **Problem Framing**: "What do you mean by 'corrupted' and how did you first notice this?"
2. **Scope Assessment**: "How widespread is this corruption - all customers, specific types, certain time periods?"
3. **Data Journey Tracing**: "Can you walk through the complete path this data takes from creation to report?"
4. **Assumption Audit**: "What assumptions do we make about data integrity at each step?"
5. **Paradigm Questioning**: "Are we defining 'corruption' correctly, or might this be expected transformation?"
6. **System Design Evaluation**: "Does our data architecture properly separate concerns and maintain integrity?"
7. **Fundamental Solution**: "How might we redesign our data flow to prevent this class of problems?"

## Advanced Inquiry Techniques

### Debugging Intuition Development
[Extended thinking: Build pattern recognition and systematic thinking skills that improve future debugging capability.]

**Pattern Recognition Training:**
- "What patterns do you notice across different debugging sessions?"
- "How do successful debugging approaches differ from unsuccessful ones?"
- "What early warning signs might help identify problems before they manifest?"
- "Which types of problems tend to have similar root causes?"

**Systematic Thinking Development:**
- "What systematic approach would you use if facing this problem again?"
- "How can we structure our investigation to be more methodical?"
- "What would a debugging checklist look like for this type of issue?"
- "How might we build better mental models of system behavior?"

### Meta-Cognitive Enhancement
[Extended thinking: Develop awareness of thinking processes and problem-solving strategies for continuous improvement.]

**Process Awareness:**
- "What debugging strategies are you using, and how effective are they?"
- "When do you tend to jump to conclusions versus taking time to investigate?"
- "What triggers your intuition, and how reliable has it been?"
- "How do you balance systematic investigation with time constraints?"

**Learning Optimization:**
- "What insights from this debugging session will help with future problems?"
- "How has your debugging approach evolved through this investigation?"
- "What would you do differently if you encountered this problem again?"
- "What tools or knowledge gaps became apparent during this process?"

## Success Indicators

### Problem Resolution Quality
- **Root Cause Identification**: Addressing underlying causes rather than symptoms
- **Solution Robustness**: Fixes that prevent recurrence and handle edge cases
- **Understanding Depth**: Comprehensive grasp of problem context and implications
- **Learning Transfer**: Insights applicable to future similar problems

### Inquiry Effectiveness
- **Question Quality**: Strategic questions that reveal key insights
- **Discovery Facilitation**: Guiding learner to their own insights rather than providing answers
- **Systematic Progress**: Structured advancement through investigation phases
- **Meta-Cognitive Development**: Building debugging skills and intuition

### Educational Impact
- **Self-Reliance Building**: Increased independence in future problem-solving
- **Critical Thinking Enhancement**: Improved analytical and questioning skills
- **Confidence Development**: Growing comfort with systematic investigation approaches
- **Knowledge Transfer**: Application of learned approaches to new problem domains

The socratic_debug command transforms problem-solving from reactive troubleshooting into proactive skill development, building systematic thinking capabilities that enhance long-term debugging effectiveness and system understanding.