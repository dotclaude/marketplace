---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <question-topic> [--level=staff|principal] [--category=leadership|influence|conflict|ambiguity|failure|vision]
description: Prepare for behavioral and competency interview questions using STAR method
---

# Behavioral Interview Coach

Master the behavioral/competency interview with STAR method stories calibrated for Staff+ engineers. Focus on demonstrating technical judgment, leadership, and impact.

## Interview Structure (30-45 minutes)

### Opening (1 minute)
- Warm greeting
- "Tell me about yourself" (30-sec version, then pivot to questions)

### Behavioral Questions (25-30 minutes)
- Ask 3-5 targeted questions
- Listen for specificity and agency
- Follow up to understand your thinking

### Your Questions (5 minutes)
- Show genuine interest
- Ask about growth, culture, technical challenges

### Closing
- Thank you and next steps

## STAR Method Framework

**Situation** (15-20 seconds)
- Context: Where were you working?
- Challenge: What was the situation?
- Constraints: What made it hard?

**Task** (10 seconds)
- What needed to happen?
- What was your responsibility?

**Action** (60-90 seconds)
- What specifically did YOU do?
- Focus on your decisions and reasoning
- Include 2-3 specific steps or decisions

**Result** (20-30 seconds)
- What was the outcome?
- Use metrics/numbers when possible
- What did you learn?

**Total per story**: 2-3 minutes

## Staff vs Principal Calibration

### Staff Engineer Stories
**Show**:
- Technical depth in your domain
- Mentoring and multiplying through others
- Taking on bigger scope than expected
- Making architectural decisions
- Influencing people with expertise, not authority

**Narrative Focus**:
- "I became the expert in [domain]"
- "I helped the team level up by..."
- "I recognized [pattern], which became how we..."
- "I took on [stretch project] and learned..."

### Principal Engineer Stories
**Show**:
- Organizational impact and vision
- Shifting how the company thinks about problems
- Building capability that multiplies across the org
- Influence at executive levels
- Creating lasting change, not just fixing things

**Narrative Focus**:
- "I identified [organizational gap] and built [solution]"
- "I shifted how we think about [problem]"
- "I created [framework/pattern] that the org now uses"
- "This impacted [multiple teams/business metrics]"

## Question Categories & Preparation

### Leadership & Influence (Most Important for Staff+)

**"Tell me about a time you influenced a technical decision without direct authority"**

Staff approach:
```
Situation: Team was about to choose database that I thought would scale poorly
Task: Convince them to reconsider without having authority over decision
Action:
- Analyzed growth projections vs database scaling curves
- Created comparison showing where each option breaks
- Proposed low-risk: try with our data patterns first
- Presented as "here's the cost-benefit" not "you're wrong"
Result: Team switched. Prevented major rewrite later. Became go-to for architecture questions.
```

Principal approach:
```
Situation: Org was doing microservices without platform support; chaos ensuing
Task: Shift organization's thinking from "do it now" to "build foundations first"
Action:
- Didn't argue; modeled the operational cost
- Showed 3-year roadmap: capabilities → services
- Proposed partnership: I'd build platform, they'd phase services
- Made it their success, not my pushback
Result: Org adopted phased approach. Better outcome. I led platform team.
```

### Handling Ambiguity & Complexity

**"Tell me about a time you had incomplete information and had to decide"**

Challenge: Show you gather data before deciding, or decide quickly when you must
Include: How you frame the decision, how you commit despite uncertainty

### Mentorship & Growth

**"Tell me about someone you mentored and helped grow"**

For Staff: Show concrete growth (junior → mid) or helped someone transition areas
For Principal: Show broad impact (multiple people, org capability building)

### Conflict & Disagreement

**"Tell me about a conflict you resolved"**

Key insight: The best answer shows how you converted conflict into collaboration
Include: Listening to understand, finding shared goals, proposing together

### Failure & Learning

**"Tell me about something you'd do differently"**

Don't say: "I didn't really fail"
Do say: "I made assumption X that turned out wrong. Here's what I learned."

### Technical Vision

**"Describe your biggest technical contribution"**

For Staff: Deep expertise that became team/org standard
For Principal: Platform/capability that others build on

## Interview Red Flags

❌ **Vague answers**: "We did X" instead of "I did X"
❌ **No specific details**: "Everything went well" vs "This metric improved 40%"
❌ **Rambling stories**: "Let me back up... actually, before that..."
❌ **Defensive tone**: "I wasn't wrong, the other person was"
❌ **No learning**: "It worked great" with no reflection
❌ **Unrelated stories**: Story doesn't address the question

✓ **Specific examples**: "In Q3 2022, I..."
✓ **Your agency**: "I recognized... so I..."
✓ **Concrete outcomes**: "Reduced latency by 60%, improved reliability to 99.99%"
✓ **Clear learning**: "This taught me that..."
✓ **Focused narrative**: Answer in 2-3 minutes

## Building Your Story Bank

Create stories covering:
- [ ] Technical depth / expertise
- [ ] Influence without authority
- [ ] Mentoring / growth
- [ ] Conflict / disagreement
- [ ] Failure / learning
- [ ] Ambiguity / decision-making
- [ ] Innovation / new idea
- [ ] Scale / big project

Have 1-2 stories per category, flexible enough to adapt to questions.

## Adapting Stories to Questions

Same story, different angle:

**Your story**: "I designed a caching layer that improved latency 60%"

**If asked about technical depth**:
Focus: "The hard part was cache coherency patterns. We chose [approach] because..."

**If asked about influence**:
Focus: "The team was skeptical about complexity. Here's how I convinced them..."

**If asked about learning**:
Focus: "We made assumption X that failed at scale. So I redesigned around..."

## Interviewer's Perspective

**They're evaluating**:
1. Can you think clearly under pressure?
2. Do you have good judgment?
3. Are you easy to work with?
4. Do you take responsibility?
5. Are you growing?
6. Will you make our org better?

Your stories should show all of these.

## Talking Points for Interviews

When you're stuck:
- "Let me think for a moment..."
- "That's a great question—it reminds me of..."
- "I want to give you an honest answer rather than rush one"

When explaining your reasoning:
- "I recognized that [insight]"
- "So I proposed [approach]"
- "The result was [outcome], and the learning was [insight]"

When asked follow-up questions:
- "That's a great point. Actually, it's why I..."
- "I hadn't thought about it that way. It changed my perspective on..."
- "Yes, and what I learned from that was..."

## Execution Day Tips

**Before interview**:
- Review your story bank (don't memorize, internalize)
- Get good sleep
- Arrive 5 min early

**During interview**:
- Listen fully to question before answering
- Take 2 seconds to collect thoughts
- Tell story conversationally (not rehearsed sounding)
- Check for understanding: "Does that make sense?"
- Be specific: names, dates, metrics

**If you get stuck**:
- "Let me think about the best example..."
- "Want me to tell you about another time...?"
- Ask: "What part would you like to know more about?"

## After Interview

**How you did well**:
- They asked follow-up questions (means they were engaged)
- They smiled/nodded (means they believed you)
- They spent time on your story (means it resonated)
- They asked your questions back (means they're interested)

**Signs to improve**:
- They seemed disengaged
- They interrupted to move to next question
- You rambled (they redirected)
- You couldn't answer follow-ups

## The Ultimate Goal

Interviews aren't about being perfect. They're about showing:
- You think clearly
- You can communicate
- You take responsibility
- You're growing
- You'll make their team better

Your stories are the proof.
