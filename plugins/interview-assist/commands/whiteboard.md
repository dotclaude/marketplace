---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <concept-or-problem> [--format=system-design|algorithm|architecture] [--scenario=explain|walkthrough|deep-dive]
description: Master whiteboarding and technical communication for interviews
---

# Technical Communication & Whiteboarding Coach

Learn to think out loud, explain complex concepts clearly, and communicate your technical thinking in real time during interviews.

## Core Communication Principle

Your thinking is more important than your solution. Interviewers want to see:
- How you approach unfamiliar problems
- How you incorporate feedback
- How you explain your reasoning
- How you handle uncertainty

## Interview Whiteboarding Flow

### Setup (First 1 minute)
**What to do**:
1. Take a breath (shows confidence)
2. Repeat the problem back (shows understanding)
3. Ask clarifying questions (shows thoughtfulness)
4. Outline your approach (shows structure)

**Example**:
```
"So you want me to design [system] with [constraints].

Let me make sure I understand:
- [Constraint 1]?
- [Constraint 2]?
- Success metrics are [metric 1] and [metric 2]?

Here's how I'll approach this:
1. Outline components
2. Walk through user flow
3. Discuss trade-offs
4. Explore deep-dive questions

Does that work for you?"
```

This buys you time while staying engaged.

### Thinking Out Loud (The Critical Skill)

**What NOT to do**:
```
[Sit silently for 5 minutes]
[Write code/diagram in silence]
[Explain everything at the end]
```

**What TO do**:
```
"Let me think about this structure...

The challenge is [problem].

One approach would be [option A], but that would [drawback].
Another approach would be [option B], which [benefit] but [cost].

Given [constraint], I think [option A] is better because [reasoning].

Does that make sense, or would you want me to explore [option B]?"
```

**Why this works**:
- Shows your thinking process
- Gives interviewer chance to guide you
- Prevents you from going down wrong path alone
- Demonstrates communication skill

### Whiteboard Technique: System Design

**Layout**:
```
┌─────────────────────────────────────────┐
│      [Title: System Name]               │
└─────────────────────────────────────────┘

[Client Layer]          [API Gateway]
        ↓                     ↓
[Load Balancer] ─────→ [Service 1]
                       [Service 2]
                            ↓
                    ┌──────────────┐
                    │[Database]    │
                    │[Cache]       │
                    │[Queue]       │
                    └──────────────┘

[Key Decisions/Annotations on the side]
```

**Tips**:
- Use boxes for components (services, databases)
- Use arrows for communication with labels (HTTP, gRPC, async)
- Use cylinders for databases
- Label everything (what, why)
- Leave space to add detail
- Draw rough; clarity matters more than art

### Whiteboard Technique: Algorithm

**Layout**:
```
Problem: [Statement]

Approach: [High-level strategy]

Example:
  Input: [example]
  Process:
    Step 1: [what, why]
    Step 2: [what, why]
  Output: [result]

Complexity: Time O(?) Space O(?)
```

**Tips**:
- Write problem clearly at top
- Work through example step-by-step
- Show your thinking
- Label complexity clearly
- Mark improvements with arrows

### Narrating Your Thinking

**Pattern to use**:
```
"I'm thinking about [aspect].

The key insight is [insight].
So my approach is [approach].

Let me walk through this on the example:
  [Step 1]: [explain]
  [Step 2]: [explain]
  [Step 3]: [explain]

Does this make sense? Any questions before I code this?"
```

**For System Design**:
```
"One challenge is [bottleneck].
To handle this, I'd use [technology] because [side effect].
That dissolves [problem] and enables [benefit].

Here's what it looks like:
[Draw component]
[Explain interaction]
"
```

## Handling Questions During Whiteboarding

### When asked "What about X?"

**Don't**: Dismiss it or add it to your diagram
**Do**: "That's a great point. Currently I have [approach]. For X, we could [option]. Which would you rather see me explore?"

### When you don't know something

**Don't**: Pretend to know or go silent
**Do**: "I'm not sure off the top of my head. Let me think... I'd probably [approach] and then validate with [method]"

### When they push back on your design

**Don't**: Get defensive
**Do**: "I see your concern. That's why we [mitigation]. The trade-off is [what we gain] vs [what we lose]."

### When they ask you to go deeper

**Do prepare** by understanding which components need depth:
- They ask you to explain → you explain in detail
- They ask "how would you..." → you think through the new constraint
- They ask "what if..." → you adjust your design live

## Active Listening Signals

Show you're listening:
- ✓ Pause before responding (shows you heard them)
- ✓ Reference their point: "When you mentioned X, that suggests..."
- ✓ Adjust based on feedback: "So you're saying reliability matters more, which means..."
- ✓ Look at them when they're talking (yes, even at whiteboard)
- ✓ Nod or indicate understanding

This matters as much as your technical answer.

## Pacing Your Explanation

### The 2-Minute Rule
- **For any concept**: Explain in 2 minutes at high level
- **If they want detail**: They'll ask, then go 5 minutes deep
- **If running out of time**: "In the interest of time, let me jump to [important part]"

### Time Management Template

**60-minute system design**:
- 0-5 min: Clarify requirements
- 5-15 min: High-level design
- 15-40 min: Component detail
- 40-55 min: Trade-offs and deep-dive
- 55-60 min: Your questions

**45-minute coding**:
- 0-2 min: Clarify problem
- 2-5 min: Approach outline
- 5-25 min: Code + explanation
- 25-40 min: Complexity + optimization
- 40-45 min: Edge cases + questions

## Specific Scenarios

### Explaining Cache Invalidation

Straightforward approach:
```
"We use a cache layer for frequently accessed data.

The challenge is: how do we handle stale data?

I'd approach it with TTLs (time-to-live):
- Data cached for [duration]
- After TTL expires, cache invalidates
- Next request fetches fresh data

Trade-off: We accept some staleness (max [duration]) to gain speed
"
```

### Explaining Consistency Models

```
"We have two options:

Strong Consistency:
- Always latest data
- But slower (coordinates across systems)
- Use when correctness is critical (payments, orders)

Eventual Consistency:
- Might be slightly stale (by [duration])
- But fast (no coordination)
- Use when freshness tolerance is high (feeds, recommendations)

Given [constraint], I'd choose [model]"
```

### Explaining Failure Handling

```
"If [component] fails, here's what happens:

Detection: [monitoring mechanism]
Failover: [backup takes over]
Recovery: [how we restore]

This ensures [SLA]"
```

## Anti-Patterns to Avoid

❌ **Silent coding**: Code while thinking
→ ✓ Narrate while you code: "I'm adding this check because..."

❌ **Waiting for perfection**: Perfect diagram before explaining
→ ✓ Rough diagram + narration: explain as you draw

❌ **Technical jargon without explanation**: "We'll use eventual consistency"
→ ✓ Explain for humans: "We accept [small lag] to gain [speed]"

❌ **Dismissing interruptions**: "Let me finish my explanation"
→ ✓ Embrace interruptions: "Good point, that means we need [adjustment]"

❌ **Long monologues**: Talk for 10 minutes straight
→ ✓ Conversation: "Does this make sense? Any questions?"

❌ **Vague descriptions**: "It's like AWS S3"
→ ✓ Concrete description: "A distributed file system where [how it works]"

## Confidence Techniques

### Show Confidence Without Arrogance
- Speak clearly (not fast)
- Use decisive language: "I'd choose X" not "maybe we could possibly try"
- Explain your reasoning (not just the answer)
- Invite questions: shows you're secure in your thinking

### When Uncertain
- "Let me think through that..." (shows you're careful)
- "That's a good question—I hadn't considered..." (shows openness)
- "I'd want to validate that with [method]..." (shows rigor)

### Physical Presence
- Stand tall (not defensive slouch)
- Use the whiteboard space (don't cower in corner)
- Make eye contact (show you're engaged)
- Gesture naturally (show you're comfortable)

## Practice Techniques

### Solo Practice
1. **Record yourself**: Watch how you explain without audience
2. **Whiteboard solo**: Explain to empty room
3. **Narrate videos**: Watch architecture videos, pause and explain aloud

### With Partner
1. **Think-aloud protocol**: Explain while they listen
2. **Interruption practice**: Have them interrupt with questions
3. **Feedback focus**: "Could you follow my thinking?"

### In-person Mock
1. Find someone to play interviewer
2. Use actual whiteboard
3. Time yourself
4. Get specific feedback

## The Goal

Whiteboarding well means:
- ✓ Clear thinking that's easy to follow
- ✓ Inviting collaboration, not defending a solution
- ✓ Showing your reasoning, not just your answer
- ✓ Comfortable thinking out loud under pressure
- ✓ Responsive to feedback

You're not trying to be perfect. You're trying to think well with an audience.
