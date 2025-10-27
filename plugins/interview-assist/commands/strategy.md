---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <company-name-or-type> <role-title> [--research-depth=surface|comprehensive] [--focus=company|role|alignment|preparation-plan]
description: Develop interview strategy for specific companies and roles
---

# Interview Strategy & Preparation Coach

Develop a tailored strategy for your specific company and role. Understand what they're looking for, predict likely questions, and create a preparation plan.

## Company Type Analysis

### FAANG Scale (Google, Meta, Amazon, Apple, Netflix)

**Interview Characteristics**:
- **Coding**: Hard algorithmic problems (LeetCode hard)
- **System Design**: Scale of millions/billions of users
- **Bar**: Very high; they're selective
- **Process**: Multiple rounds (4-6 hours total)

**Preparation Focus**:
- Master algorithms (this is their baseline)
- Practice hard problems daily
- Design for massive scale (1B+ users)
- Have stories about scale challenges

**Typical Questions**:
- "Design a feed system like Facebook"
- "Design a rate limiter"
- "Design a distributed cache"
- "Design a URL shortener at global scale"

**Company-Specific Notes**:
- Google: Loves system design depth + algorithms
- Meta: Cares about scale and rapid iteration
- Amazon: Values customer obsession + operational excellence
- Apple: Quality and user experience matter
- Netflix: Cares about resilience and performance

### High-Growth Startup (Series C/D/E)

**Interview Characteristics**:
- **Coding**: Practical problems (can you ship?)
- **System Design**: Scaling from thousands to millions
- **Bar**: Moderate-high, but more practical
- **Process**: 2-3 rounds (2-3 hours)

**Preparation Focus**:
- Show you can ship quickly
- Demonstrate adaptability
- Have stories about scaling under pressure
- Understand their specific problems

**Typical Questions**:
- "We're at 100K users, getting slow. Fix it."
- "Design a system for our specific use case"
- "How would you approach our biggest technical problem?"
- "Tell me about scaling something rapidly"

**Pre-Interview Research**:
- Use their product
- Read their engineering blog
- Understand their tech stack
- Know their current challenges (from news/Crunchbase)

### Well-Established Tech Company (Microsoft, Adobe, IBM, Oracle)

**Interview Characteristics**:
- **Coding**: Practical over theoretical
- **System Design**: Real-world with constraints
- **Bar**: Solid, but less extreme than FAANG
- **Process**: 2-3 rounds (2-3 hours)

**Preparation Focus**:
- Show you understand enterprise constraints
- Have stories about complex org navigation
- Know their products
- Understand their competitive position

**Typical Questions**:
- "Design a system for our customers"
- "How would you approach this legacy codebase?"
- "Tell me about working in large organizations"
- "How do you balance innovation and stability?"

### Early-Stage Startup (Seed/Series A/B)

**Interview Characteristics**:
- **Coding**: May be optional or lighter
- **System Design**: Medium scale, specific to their needs
- **Bar**: Moderate, emphasis on fit
- **Process**: Casual (1-2 rounds, 1-2 hours)

**Preparation Focus**:
- Show genuine interest (not career move)
- Have opinions on their technical direction
- Demonstrate adaptability and learning
- Understand their vision

**Typical Questions**:
- "Tell me about yourself"
- "What would you work on first?"
- "How do you think about our technical challenges?"
- "Why do you want to join us?"

## Role-Specific Strategy

### IC Track (Individual Contributor)

**What They Want**:
- Technical contribution
- Mentorship/multiplying impact
- Technical leadership (without management)

**Preparation**:
- Coding: Solid (probably LeetCode medium+)
- System Design: Yes (you design systems)
- Behavioral: Focus on technical impact + mentorship

**Sample Questions**:
- "Design a system for this use case"
- "Tell me about your technical expertise"
- "How do you mentor others?"
- "Describe a system you scaled"

### Tech Lead Track

**What They Want**:
- Technical excellence + people skills
- Can make architecture decisions
- Can help engineers succeed

**Preparation**:
- Coding: Strong (you need to code still)
- System Design: Yes (you decide architecture)
- Behavioral: Focus on both technical + people stories

**Sample Questions**:
- "Tell me about a team you've led"
- "How do you develop people?"
- "Design this system"
- "How do you handle technical disagreement?"

### Manager Track

**What They Want**:
- Can grow people
- Can navigate org
- Can deliver results through others

**Preparation**:
- Coding: May be lighter (but not absent)
- System Design: Lighter (you don't design systems)
- Behavioral: Focus on people growth, retention, culture

**Sample Questions**:
- "Tell me about developing a person"
- "How do you handle underperforming engineer?"
- "Describe your team dynamics"
- "How do you balance business and team needs?"

## Pre-Interview Preparation Plan

### Week 1: Company Deep-Dive
- [ ] Use their product (spend 2+ hours)
- [ ] Read recent press (last 6 months)
- [ ] Study engineering blog (last 2 years)
- [ ] Check their job postings (understand hiring)
- [ ] Research leadership team
- [ ] Identify 5 technical challenges they likely face
- [ ] Understand their business model and competitors

**Deliverable**: One-page company summary with challenges you could solve

### Week 2: Role Alignment
- [ ] Study job description deeply
- [ ] List top 10 requirements
- [ ] Map your background to each
- [ ] Identify gaps (be prepared to address)
- [ ] Write "why I want this role" (1-2 minutes)
- [ ] Prepare 3-5 relevant stories
- [ ] Generate 5-7 thoughtful questions to ask

**Deliverable**: Interview talking points aligned to role

### Week 3: Interview Practice
- [ ] Practice coding (5-10 problems at their difficulty)
- [ ] Design 2-3 systems they likely build
- [ ] Mock interview (with friend)
- [ ] Get feedback on communication
- [ ] Time yourself (coding 30 min, system design 40 min)
- [ ] Practice behavioral stories (2-3 min each)
- [ ] Record yourself (watch for tics, clarity)

**Deliverable**: Confidence that you can execute under pressure

### Week 4: Mental Prep
- [ ] Review your story bank (don't memorize, internalize)
- [ ] Review company research (brief last look)
- [ ] Prepare your work setup (quiet place, good internet)
- [ ] Get good sleep night before
- [ ] Eat healthy
- [ ] Arrive early (5 min buffer for tech checks)

**Deliverable**: Calm, prepared mindset

## Question Prediction by Company Type

### FAANG Typical Questions
- "Design a feed system"
- "Design a cache"
- "Design a rate limiter"
- "Design a distributed storage system"
- "How would you monitor this?"
- "Tell me about your biggest technical contribution"
- "How do you handle disagreement?"

### Startup Typical Questions
- "Design an analytics system"
- "We're at X scale, it's slow. How do you solve it?"
- "Design a system for our specific need"
- "Tell me about rapid scaling"
- "How would you improve our tech?"
- "What would you work on first?"

### Enterprise Typical Questions
- "Design a system for our customers"
- "How would you approach this legacy system?"
- "Tell me about working in large orgs"
- "How do you balance innovation and stability?"
- "Describe a complex project"
- "How do you influence across teams?"

## Positioning Your Background

### The Alignment Formula

For each major requirement in the job:

**Step 1**: Identify the requirement
"They need someone who can [X]"

**Step 2**: Show you have it
"At [company], I [did similar work]"

**Step 3**: Make it specific
"Here's an example: [concrete project]"

**Step 4**: Quantify the impact
"The result was [metric/outcome]"

### Example Alignments

**Requirement**: "Experience scaling systems"
**Your background**: "I scaled our database from 100K to 10M QPS"
**In interview**: "That required [challenges], which is why I approach scaling by [methodology]"

**Requirement**: "Technical leadership"
**Your background**: "I led architecture decisions across 3 teams"
**In interview**: "I did this by [approach], which shows [capability]"

**Requirement**: "Infrastructure expertise"
**Your background**: "I designed our microservices infrastructure from scratch"
**In interview**: "The lessons I learned were [insights]"

## Your "Why" Story (2 minutes)

Prepare to answer: "Why are you interested in this role?"

**Structure**:
```
1. What excites you about what they're building
2. Specific technical problem you want to solve
3. How your background prepares you
4. What's next for you
```

**Example**:
```
"I'm interested because:

1. You're solving distributed systems at scale—that's exciting
2. Specifically, I want to dive deep into distributed consensus—I've done similar work
3. My background in systems design means I can contribute immediately
4. I'm looking to go deeper on distributed systems, which this role offers
"
```

## Red Flags & How to Address

### If you're worried...

**Concern**: "I don't have exact experience in [X]"
**Strategy**: "I have deep experience in [related skill], which transfers to [X]"

**Concern**: "I haven't worked at a company their size"
**Strategy**: "I've scaled [system/team] from [small] to [large], showing I can grow"

**Concern**: "I'm coming from a different tech stack"
**Strategy**: "I learn new tech quickly. Here's my approach to learning: [methodology]"

**Concern**: "I'm transitioning roles (IC→Lead, etc.)"
**Strategy**: "I've been preparing by [evidence], and I'm excited about [new domain]"

## Interview Day

### Night Before
- Get good sleep (matters more than extra studying)
- Light review of company facts
- Prepare your work space

### Morning Of
- Healthy breakfast
- Review your "why" story and key talking points
- Get to call 5 minutes early

### During
- Take your time (silence while thinking is OK)
- Ask clarifying questions
- Think out loud
- Show genuine curiosity
- Be yourself

### After
- Thank you email within 24 hours
- Reference something specific from conversation
- Reiterate genuine interest
- Keep it brief (don't oversell)

## Success Metrics

You're well-prepared when:
- ✓ Can discuss their company/problems intelligently
- ✓ Have relevant stories for their role requirements
- ✓ Can solve coding problems at their difficulty
- ✓ Can design systems for their scale
- ✓ Can articulate why this role matters to you
- ✓ Have thoughtful questions to ask them
- ✓ Feel confident about your background/experience

You nailed the strategy when they seem interested in YOU specifically, not just looking for "anyone who can code."
