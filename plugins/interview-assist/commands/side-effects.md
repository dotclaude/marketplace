---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <problem-or-system> [--depth=basic|detailed|deep] [--focus=coding|system-design|both]
description: Master side-effect decomposition for interview problem-solving
---

# Side-Effects Engineering Interview Coach

Learn to dissolve problems by recognizing primitive side effects and composing them for emergent properties. Based on the philosophy: instead of solving problems, design substrates where problems can't exist.

## Core Framework

### The Dissolution Approach vs Traditional Solving

**Traditional**: Problem → Design Solution → Implement → New Problems → Patch → Accumulate Complexity

**Side-Effects**: Problem → Identify Emergent Properties → Catalog Side Effects → Compose Primitives → Problem Dissolves

## Methodology

### Step 1: Reframe the Problem

Instead of: "How do I solve X?"
Ask: "What substrate makes X impossible to express?"

**Examples**:
- **Two Sum**: "What if finding complements were instant?" → Hash table
- **URL Shortener**: "What if collisions were impossible (not handled)?" → Monotonic counter per shard
- **Event Ordering**: "What if message ordering was guaranteed by design?" → Partitioned queue
- **Cache Invalidation**: "What if staleness wasn't a problem?" → TTL + eventual consistency

### Step 2: Identify Side Effects

Every primitive has consequences that make operations trivial:

**Hash Table**:
- Side effect: O(1) lookup
- Side effect: Duplicate detection automatic
- Side effect: Historical tracking free
- Dissolves: Search problems, frequency counting

**Sorted Array + Two Pointers**:
- Side effect: Monotonicity
- Side effect: Bi-directional logic
- Dissolves: Palindrome, container, range problems

**Heap**:
- Side effect: Instant min/max
- Side effect: Lazy evaluation
- Dissolves: Top-K, k-way merge, priority-based operations

**Queue with Partitioning**:
- Side effect: FIFO guarantee per partition
- Side effect: Ordering by key
- Dissolves: Ordering problems, distributed ordering

### Step 3: Compose for Emergence

Select primitives whose side effects combine to produce the property you want.

**Example: URL Shortener**

**Property 1: Collisions impossible**
- Primitive: Counter per shard
- Side effect: Monotonic IDs = inherently unique
- Result: Collision question is meaningless

**Property 2: Scaling without coordination**
- Primitive: Consistent hashing
- Side effect: Automatic shard routing
- Result: Horizontal scaling is free

**Property 3: Analytics automatic**
- Primitive: Write-Ahead Log
- Side effect: Creates event stream
- Result: Analytics consume stream (not added separately)

### Step 4: Verify Dissolution

The problem can't exist in the new substrate.

**Check**: Can you ask the old question?
- "How do we handle collisions?" → Meaningless (can't happen)
- "How do we scale?" → Already solved by design
- "How do we collect analytics?" → It emerges automatically

## Primitive Catalog

### Data Structure Primitives

**Hash Map/Dictionary**
- Side effects: O(1) lookup, duplicate detection, historical tracking
- Dissolves: Search families, frequency, grouping
- Interview: "Instant lookup makes the problem trivial"

**Sorted Array + Two Pointers**
- Side effects: Monotonicity, bi-directional logic
- Dissolves: Palindrome, container, range problems
- Interview: "Sorting exploits monotonicity; pointers eliminate search"

**Heap/Priority Queue**
- Side effects: Instant min/max, lazy evaluation
- Dissolves: Top-K, merge, scheduling
- Interview: "We always know what matters next"

**Prefix/Suffix Arrays**
- Side effects: Pre-computed info, O(1) queries
- Dissolves: Range queries
- Interview: "Pre-computation trades space for constant time"

### Algorithmic Primitives

**Divide and Conquer**
- Side effects: Problem decomposition, recursive structure
- Dissolves: Tree problems, merge problems
- Interview: "The problem is already decomposed"

**Binary Search**
- Side effects: Logarithmic search space reduction
- Dissolves: Search in sorted data
- Interview: "Monotonicity gives us O(log n) locations"

**Dynamic Programming**
- Side effects: Caching subproblems, optimal substructure
- Dissolves: Exponential → polynomial complexity
- Interview: "Memoization eliminates redundant computation"

### System Design Primitives

**Counter per Shard**
- Side effects: Monotonic uniqueness, no coordination
- Dissolves: Collision handling, distributed ID generation
- Interview: "Monotonic IDs are inherently unique"

**Consistent Hashing**
- Side effects: Automatic routing, minimal rebalancing
- Dissolves: Manual sharding logic
- Interview: "Hashing gives us automatic distribution"

**Partition by Key**
- Side effects: FIFO guarantee, ordering preservation
- Dissolves: Distributed ordering problems
- Interview: "Partitioning enforces ordering by design"

**Write-Ahead Log**
- Side effects: Creates event stream, enables replication
- Dissolves: Separate analytics pipeline
- Interview: "The log is the single source of truth"

**Caching Layer**
- Side effects: Instant access for cached data
- Dissolves: Database bottleneck for hot data
- Interview: "Cache misses become the only database queries"

## Interview Application

### For Coding Problems

**Flow**:
1. Identify the brute-force bottleneck
2. Ask: "What operation is repeated?"
3. Ask: "Which primitive's side effect makes this operation free?"
4. Compose and explain

**Example: Two Sum**
- Bottleneck: Finding each number's complement
- Side effect needed: O(1) lookup
- Primitive: Hash map
- Composition: Single pass, check then add
- Result: "Hash lookup dissolves the search problem"

### For System Design Problems

**Flow**:
1. Identify desired emergent properties
2. Ask: "What would make this requirement trivial?"
3. Catalog primitives with those side effects
4. Compose the architecture
5. Verify the problem dissolves

**Example: Design Notification System**
- Property 1: Scalable message ingestion
  - Primitive: Message queue (side effect: buffering + ordering)
- Property 2: Reliable delivery
  - Primitive: Persistent queue + acknowledgment (side effect: guaranteed delivery)
- Property 3: Low latency notifications
  - Primitive: Publish-subscribe (side effect: fan-out from one message)
- Result: Architecture emerges from side effect composition

## Talking Points for Interviews

### When explaining your approach:
- *"Rather than handle [problem], I'd design for [property] impossible to express it"*
- *"This primitive has a side effect: [consequence]. That dissolves the [problem]"*
- *"Composing [primitive A] with [primitive B] gives us [emergent property]"*
- *"The substrate makes this question meaningless"*

### When defending a decision:
- *"We don't need special logic for [case] because the design prevents it"*
- *"This scales because [side effect] makes [concern] automatic"*
- *"The property isn't added—it emerges from the composition"*

### When addressing trade-offs:
- *"We're using [space] to gain [side effect], which dissolves [problem]"*
- *"The trade-off is worth it because we convert exponential to linear"*
- *"Without this primitive, we'd need custom logic for [multiple cases]"*

## Practice Problems

### Beginner Level
1. **Two Sum**: What side effect dissolves the complement problem?
2. **Anagrams**: What side effect detects frequency matching?
3. **Palindrome**: What side effect exploits string structure?

### Intermediate Level
1. **LRU Cache**: What compositions give us LRU behavior for free?
2. **K-Way Merge**: What side effect gives instant next element?
3. **Sliding Window**: What side effect maintains window constraints?

### Advanced Level
1. **Design a URL Shortener**: What substrate prevents collisions?
2. **Design a Distributed Lock**: What primitives give us atomic operations?
3. **Design Event Sourcing**: What side effects does WAL enable?

## Key Distinction: Solve vs Dissolve

**Solving**:
- Problem: "How do we prevent X?"
- Solution: "Add logic to detect and handle X"
- Cost: Complexity accumulates with each edge case

**Dissolving**:
- Problem: "How do we make X impossible?"
- Solution: "Choose primitives where X can't exist"
- Benefit: Problem space shrinks; complexity decreases

**Interview Example**:

❌ **Solving Approach**:
"We prevent cache consistency problems by: invalidating on write, using TTLs, checking staleness..."

✓ **Dissolving Approach**:
"We don't prevent consistency problems—we choose eventual consistency. The substrate is: cache with TTL. Within the TTL, it's correct. After TTL, it refreshes. Consistency problems dissolve."

## Success Indicators

You understand side-effects engineering when you:
- ✓ See problems and ask "what substrate dissolves this?"
- ✓ Know primitives deeply (not just API, but side effects)
- ✓ Recognize composition opportunities
- ✓ Explain solutions via emergent properties
- ✓ Identify impossible-to-express problems in your substrate
- ✓ Can apply this thinking to novel problems

This approach separates engineers who memorize solutions from engineers who dissolve problem spaces.
