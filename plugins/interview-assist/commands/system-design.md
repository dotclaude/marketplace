---
model: claude-opus-4-1
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <system-name> [--depth=standard|deep] [--focus=architecture|scalability|trade-offs] [--generate-diagram=true|false]
description: Design complete systems with WHY, WHAT, HOW, CONSIDERATIONS, and DEEP-DIVE framework
---

# System Design Interview Coach

Complete framework for designing systems from problem to implementation. Includes WHY/WHAT/HOW structure, trade-off analysis, mermaid diagrams, and deep-dive optimizations.

## Interview Flow (60 minutes)

### Phase 1: Requirements & Context (5 minutes)
**Your goal**: Understand the problem deeply before designing

Ask clarifying questions:
- Scale: users, requests per second, data volume?
- Availability: SLA requirements (99.9%, 99.99%)?
- Latency: response time targets?
- Consistency: strong or eventual?
- Features: read-heavy, write-heavy, or balanced?
- Growth: expected growth rate?

**Interviewer's watching**:
- Do you ask the right questions?
- Do you understand the constraints?
- Can you estimate numbers?

### Phase 2: High-Level Architecture (10 minutes)
**Your goal**: Outline the system at 30,000 feet

Cover:
- Major components (load balancer, services, databases, caches)
- Communication patterns (sync/async, protocols)
- Data flow from user request to response
- Rough scalability approach

Draw simple diagram showing component interactions.

**Interviewer's watching**:
- Do you think in systems?
- Can you structure complexity?
- Do you know when to keep it simple?

### Phase 3: Detailed Component Design (20 minutes)
**Your goal**: Explain key components with confidence

Pick 2-3 components to discuss:
- How does this component work?
- Why this technology choice?
- What are the constraints it handles?
- How does it scale?

**Interviewer's watching**:
- Do you have technical depth?
- Can you justify decisions?
- Do you know trade-offs?

### Phase 4: Scalability & Trade-Offs (15 minutes)
**Your goal**: Show senior-level thinking

Discuss:
- Bottlenecks: What breaks first at 10x growth?
- Consistency: Strong vs eventual? Why?
- Reliability: Failure modes and recovery?
- Cost: What drives operational expense?
- Complexity: Is this operationally feasible?

**Interviewer's watching**:
- Do you think like a Staff engineer?
- Can you make principled trade-offs?
- Do you understand operational reality?

### Phase 5: Extensions & Deep-Dives (8 minutes)
**Your goal**: Demonstrate mastery

Address follow-up questions:
- "How would you handle [new requirement]?"
- "What's the hardest part of operating this?"
- "What would you optimize for [metric]?"
- "How would you debug this in production?"

**Interviewer's watching**:
- Are you thinking ahead?
- Can you handle surprises?
- Do you know what you don't know?

## System Design Framework

### WHY: Problem & Context
**What to cover**:
- Problem statement (1-2 sentences)
- Primary use cases (top 3-5)
- User base and growth expectations
- Non-functional requirements (scale, latency, availability)
- Business context (why does this matter?)

**For interviewer's benefit**:
- Shows you understand the problem before solving it
- Demonstrates customer empathy
- Proves you can estimate and scope

### WHAT: Components & Data Model
**What to cover**:
- Core entities (Users, Posts, Comments, etc.)
- Entity relationships
- Storage requirements (how much data?)
- Major services (Authentication, Feed, Search, etc.)
- API contracts (what endpoints do we need?)

**For interviewer's benefit**:
- Shows you think about data structure
- Demonstrates you can decompose systems
- Proves you understand component boundaries

### HOW: Architecture & Patterns
**What to cover**:
- Request flow (from user → response)
- Service architecture (monolith vs microservices decision)
- Communication patterns (synchronous, asynchronous, pub-sub)
- Storage topology (where does data live?)
- Caching strategy (where, what, how long?)
- Replication and failover

**For interviewer's benefit**:
- Shows you know architectural patterns
- Demonstrates systems thinking
- Proves you can make principled decisions

### CONSIDERATIONS: Trade-Offs & Reality
**What to analyze**:

**Consistency**
- Strong: Always get latest data (high latency, low availability)
- Eventual: Might get stale data (low latency, high availability)
- Your choice: "For [reason], we accept [consistency model]"

**Scalability**
- Vertical: Big machines (simpler, limited)
- Horizontal: More machines (complex, unlimited)
- Your choice: "We scale [direction] because [reason]"

**Reliability**
- Single point of failure? (bad)
- Replication strategy? (multiple copies)
- Disaster recovery? (backup and restore procedure)
- Your choice: "We replicate [this way] to handle [failure]"

**Cost**
- Storage: What's the cost per GB?
- Compute: What's the cost of this many servers?
- Bandwidth: What's the egress cost?
- Your choice: "This costs [X] but solves [Y]"

**Operational Complexity**
- How many different technologies?
- How hard is debugging?
- What's the on-call pain?
- Your choice: "We keep it simple: [reason]"

### DEEP-DIVE: Component Optimization
**For each major component**, be prepared to discuss:

1. **Bottleneck Analysis**
   - What's the scaling limit?
   - Where would we hit the wall first?
   - How do we know?

2. **Optimization Opportunities**
   - What could we do to handle more load?
   - What are the trade-offs?
   - When is this optimization worth doing?

3. **Failure Modes**
   - What if [component] fails?
   - How do we detect it?
   - How do we recover?

4. **Operational Concerns**
   - How do we monitor this?
   - What metrics matter?
   - How do we debug issues?

5. **Alternative Approaches**
   - What's another way to design this?
   - When would you choose it?
   - What problems does it have?

## Mermaid Diagram Strategy

Create diagrams that show:
1. **Architecture Diagram**: Components and communication
2. **Data Flow**: Request path through the system
3. **Database Schema**: Key entities and relationships

**Tips**:
- Keep diagrams simple initially
- Add detail when asked
- Label important decisions
- Annotate bottlenecks

## Example: Design Facebook Feed

### WHY
- **Problem**: Show users their friends' posts in a personalized, real-time feed
- **Use Cases**:
  1. User opens app → see recent posts from friends
  2. Friend posts → appears in followers' feeds quickly
  3. Massive scale: billions of posts, minutes of latency acceptable
- **Requirements**:
  - Read-heavy (100:1 read to write ratio)
  - Latency: Feed load < 200ms
  - Availability: 99.99%
  - Consistency: Eventual OK (a few minutes lag acceptable)

### WHAT
- **Entities**: User, Post, Friendship, Like, Comment
- **Relationships**: User → Post (1:many), User → Friend (many:many)
- **Storage**: Posts: 100s of billions, User data: billions
- **Services**: Auth, Post Creation, Feed Service, Search
- **APIs**:
  - POST /posts (create)
  - GET /feed (get user's feed)
  - POST /posts/{id}/like (like post)

### HOW
- Load balancers distribute requests
- Stateless web servers handle auth and routing
- Post service writes posts to database
- Feed service reads from cache first, database second
- Cache layer (Redis) stores hot posts
- Fanout on write: When user posts, push to all followers' feeds
- Asynchronous: Queue for fanout, workers process

### CONSIDERATIONS
- **Consistency**: Eventual consistency (a few second lag OK)
- **Scalability**: Horizontal—more servers as needed
- **Reliability**: Multi-region replication for availability
- **Cost**: Balance storage vs computation
- **Complexity**: Fanout-on-write is complex but enables fast reads

### DEEP-DIVE
1. **Fanout Bottleneck**: Celebrity posts with 100M followers?
   - Solution: Hybrid fanout—fanout for normal users, cache for celebrities
2. **Feed Personalization**: How do we rank posts?
   - Solution: ML model, but start with recency + engagement
3. **Real-time Updates**: How do we push new posts?
   - Solution: Long-polling, WebSockets, or event stream

## Talking Points During Interview

**When introducing your design**:
- "Let me outline the system at a high level..."
- "The key insight here is [insight]"
- "This design makes [requirement] easy"

**When defending a choice**:
- "We chose [option] because [constraint] → [option] is better"
- "The trade-off is [cost] for [benefit]"
- "This would change if [different constraint]"

**When asked about scaling**:
- "Currently [component] is the bottleneck"
- "We'd scale [direction] because [reason]"
- "This approach works until [limit], then we'd [next evolution]"

**When asked about failure**:
- "If [component] fails, [other component] takes over"
- "We'd detect it via [monitoring], then [recovery action]"
- "This is why we replicate [data/component]"

## Red Flags to Avoid

❌ Diving into implementation details too early
❌ Not asking clarifying questions
❌ Designing for scale you don't need
❌ Making technology choices without justification
❌ Ignoring operational reality
❌ Treating consistency/availability as separate concerns
❌ Not discussing trade-offs

✓ Start broad, add detail on request
✓ Ask clarifying questions upfront
✓ Design for the specified scale
✓ Justify technology choices
✓ Consider how humans operate it
✓ Explicitly discuss trade-offs
✓ Show you understand what you don't know

## Success Criteria

You're ready when you can:
- ✓ Clarify ambiguous requirements with good questions
- ✓ Outline architecture clearly on a whiteboard
- ✓ Explain each component's role
- ✓ Justify your technology choices
- ✓ Discuss trade-offs explicitly
- ✓ Handle "what if" questions with confidence
- ✓ Show understanding of operational reality
- ✓ Demonstrate Staff+ systems thinking
