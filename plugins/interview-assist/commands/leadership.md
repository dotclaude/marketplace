---
model: claude-opus-4-1
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <scenario-type> [--level=staff|principal] [--context=situation|analysis|response]
description: Master Staff+ and Principal leadership scenarios for senior interviews
---

# Leadership Scenarios Coach

Master the unique interview challenges at Staff+ and Principal levels. These aren't IC technical contributions—they're about strategic influence, organizational thinking, and transformational impact.

## Scenario Types

### Type 1: Influence Without Direct Authority

**The Situation**: You see something critical that needs to happen, but you have no authority to mandate it.

**Staff+ Example**:
```
Scenario: Team is about to choose a database that won't scale to anticipated size
Challenge: You don't manage them; they trust different people
Approach:
  1. Get the data (growth forecasts, scaling curves)
  2. Make it clear, not preachy ("Here's what happens at 10x")
  3. Propose low-risk path ("Let's test on our data patterns first")
  4. Make them the decision-maker (not you imposing)
Response: "I'd present the analysis, propose a test, and let them decide"
Impact: Decision changes before hitting the scaling wall
```

**Principal Example**:
```
Scenario: Org pursuing microservices without ops/platform readiness
Challenge: Leadership committed to this direction
Approach:
  1. Understand their motivations (why do they want this?)
  2. Acknowledge the benefits (don't dismiss)
  3. Show the operational cost (with numbers)
  4. Propose staged approach (first: build platforms that enable services)
  5. Offer to lead platform development
Response: "Rather than say no, I'd say here's when we're ready, and here's what we need first"
Impact: Organization de-risks while moving forward; I lead platform capability
```

### Type 2: Difficult People / Conflict Resolution

**The Situation**: You disagree with a peer on something important, and they have political influence.

**Staff+ Approach**:
```
Situation: Backend engineer wants tech choice that frontend can't support
Challenge: Both have valid reasons; political factors at play
Approach:
  1. Separate person from problem ("We both want shipping to work")
  2. Understand their actual concern (not dismiss their reasoning)
  3. Find what each is optimizing for
  4. Reframe to shared problem ("How do we get both benefits?")
  5. Propose solution that respects both concerns
Result: Path forward feels like collaboration, not compromise
```

**Principal Approach**:
```
Situation: Two teams in conflict over architectural boundaries
Challenge: Both partly right; conflict is costing organization coherence
Approach:
  1. Get curious, not defensive ("Why do you feel strongly about this?")
  2. Identify the real issue (usually different goals, not stupidity)
  3. Reframe at organizational level (not team level)
  4. Propose structural solution (clear ownership, decision rights)
  5. Make resolution about org clarity, not person vindication
Result: Problem solved at system level; both teams better off
```

### Type 3: Scaling Yourself / Multiplication

**The Situation**: Too much work for one person; need to multiply impact through others.

**Staff+ Example**:
```
Situation: You're the only one who understands critical systems
Challenge: You're bottleneck; that's not sustainable
Approach:
  1. Extract the knowledge (what's your mental model?)
  2. Document patterns (frameworks others can follow)
  3. Mentor someone specific (not just documentation)
  4. Step back and let them lead
  5. Move to next leverage point
Impact: Expertise became team capability; you're available for new work
```

**Principal Example**:
```
Situation: Org wide capability gap (e.g., performance, security, reliability)
Challenge: This isn't one team's problem; it's org architectural
Approach:
  1. Identify the gap at org level
  2. Build the platform/capability that enables others
  3. Teach how to use it (change how decisions are made)
  4. Create governance that propagates the pattern
  5. Measure org-level improvement
Impact: Organization's capability increased; you changed how they think
```

### Type 4: Navigating Broken Processes

**The Situation**: You see a process that's creating problems; fixing it requires changing how people work.

**Staff+ Example**:
```
Situation: Deployment process is slow, people are frustrated
Challenge: Process is organizational, not just technical
Approach:
  1. Document the cost (time, frustration, broken deployments)
  2. Propose a better process (easy to try, easy to revert)
  3. Make it better for participants ("Your job becomes easier")
  4. Help others adopt it
  5. Celebrate early wins
Impact: Process improved, team happier, velocity increased
```

**Principal Example**:
```
Situation: Entire org's decision-making process creates bottlenecks
Challenge: This is cultural; affects strategy
Approach:
  1. Make the cost visible (opportunity cost, culture impact)
  2. Design new process (with stakeholders, not imposed)
  3. Make the case (how does this enable our goals?)
  4. Lead the transition carefully
  5. Measure business impact
Impact: Org moves faster; decision quality actually improves
```

### Type 5: Technical Vision & Strategy

**The Situation**: You see 3-5 years forward; current path is suboptimal.

**Staff+ Example**:
```
Situation: Tech debt accumulating, will become problem in 2 years
Challenge: Business wants features, not refactoring
Approach:
  1. Align with business goals ("Tech debt blocks the features you want")
  2. Propose incremental path (can do both)
  3. Build credibility through delivering
  4. Gradually shift thinking
Result: Team now thinks about debt as business problem
```

**Principal Example**:
```
Situation: Org architecture will limit growth in 2-3 years
Challenge: Business doing fine now; no urgency
Approach:
  1. Create leading indicators (what would suggest this matters?)
  2. Build the team to start architectural work
  3. Show early wins (component that's more efficient)
  4. Position architecture as competitive advantage
Result: Org starts architectural transition early; executes better
```

## Interview Framework

### What They're Evaluating

**Staff+**:
- Do you see problems others miss?
- Can you move things without authority?
- Can you multiply your impact?
- Will you make the organization better?

**Principal**:
- Do you think strategically (3-5 year horizon)?
- Can you shift organizational thinking?
- Do you create lasting change vs short-term fixes?
- Are you comfortable with ambiguity and complexity?

### Answer Structure

1. **Problem Recognition** (15 sec)
   - What did you notice?
   - Why did others miss it?

2. **Approach** (60-90 sec)
   - How did you think about it?
   - Specific steps you took
   - How you involved others

3. **Results & Impact** (30 sec)
   - What changed?
   - How do you measure it?

4. **Reflection** (20 sec)
   - What did you learn?
   - How does this apply to this role?

### Key Phrases

**When explaining your approach**:
- "Rather than [surface approach], I thought [deeper approach]"
- "I recognized [pattern/gap] that others hadn't seen yet"
- "I made it safe for people to [desired behavior]"
- "This shifted from [old way] to [new way]"

**When discussing impact**:
- "The organization went from [state] to [state]"
- "It changed how [team/org] thinks about [topic]"
- "Created lasting [capability/pattern] that still applies"
- "Multiple teams now use [framework/approach]"

**When asked difficult follow-up**:
- "That's a great point. Here's why I made that trade-off..."
- "I think about it differently now because of [learning]"
- "If I did it again, I would [improvement]"

## Red Flags (What NOT to do)

❌ "I just told them to..."  → Shows authority thinking
✓ "I helped them see..."     → Shows influence thinking

❌ "The team wasn't smart enough to..."  → Blames others
✓ "The team wasn't equipped to see..."   → Shows empathy

❌ "I fixed it myself"      → Not multiplying
✓ "I built capability"      → Multiplying impact

❌ "Nobody listened"        → Victim narrative
✓ "I changed my approach"   → Leadership narrative

❌ "This was obvious"       → Dismissive
✓ "This became obvious once we..."  → Collaborative

## Preparing Your Scenarios

Build 4-5 stories covering:
- [ ] Influencing without authority
- [ ] Handling conflict/disagreement
- [ ] Multiplying through others
- [ ] Navigating broken org dynamics
- [ ] Strategic/visionary thinking

Practice telling them in 2-3 minutes with focus on your thinking.

## The Core Question Behind All These

Interviewer is really asking:

**"Will you make this organization better at the leadership level?"**

Not: Are you smart enough? (Assumed)
Not: Can you code? (Assumed)
But: Can you see what needs to happen and make it happen?

Your stories should prove you can.

## Success Indicators

You did well if:
- ✓ They asked follow-up questions (means they're engaged)
- ✓ They challenged your thinking (means you passed baseline)
- ✓ They leaned forward (means they're interested)
- ✓ They took notes (means it stood out)
- ✓ They discussed their org challenges (means they're thinking about your fit)

These are leadership interviews. Show you think and act like a leader.
