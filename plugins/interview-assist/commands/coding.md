---
model: claude-sonnet-4-0
allowed-tools: Task, Read, Bash, Grep, Glob, Write
argument-hint: <problem-name> [--level=staff|principal] [--pattern=hash-map|sliding-window|etc] [--difficulty=easy|medium|hard]
description: Practice coding problems with brute-force to optimized solution evolution
---

# Coding Interview Coach

Guide through a coding problem with evolution from brute-force to optimized solution. Includes talking points, complexity analysis, and pattern recognition for Staff+ interviews.

## Problem Categories

### Classic Patterns
- **Hash Map**: Two Sum, Three Sum, Anagrams, Frequencies
- **Sliding Window**: Substrings, Subarrays with constraints, Max window
- **Two Pointers**: Palindromes, Containers, Merge operations
- **Heap/Priority Queue**: Top-K, K-way merge, Running median
- **Graph**: Connectivity, Paths, Cycles, Components
- **DP/Recursion**: Overlapping subproblems, Optimal substructure
- **Prefix/Suffix**: Range queries, Pre-computed information
- **Binary Search**: Sorted array operations, Search space reduction

### Difficulty Levels
- **Easy**: Straightforward application of one pattern
- **Medium**: Pattern recognition required, some optimization
- **Hard**: Multiple patterns, system-level thinking, novel combination

## Execution Framework

### Phase 1: Problem Clarification (2-3 minutes)
Ask clarifying questions:
- What are the constraints? (Array size, value ranges)
- Can there be duplicates?
- What's the return format?
- Are there special cases?
- Time/space requirements?

### Phase 2: Brute-Force Solution (5-10 minutes)
Start simple:
1. Outline the straightforward approach
2. Walk through on a concrete example
3. Write clean, understandable code
4. Analyze time/space complexity honestly
5. Verify it works on edge cases

**Critical Talking Points**:
- "This approach tries every possibility"
- "It's O(?) because [explanation]"
- "Why I'm starting here: it's correct, which matters most"

### Phase 3: Analysis & Insight (2-3 minutes)
Identify where brute-force struggles:
- What operation is repeated?
- What would speed up [operation]?
- What data structure has a useful side effect?

Example: "The brute-force searches for complements repeatedly. If we could look them up in O(1), the problem dissolves."

### Phase 4: Optimized Solution (5-10 minutes)
Introduce the optimization:
1. State the primitive and its side effect
2. Explain how we compose it with our approach
3. Code the optimization
4. Walk through on example
5. Analyze new complexity

**Critical Talking Points**:
- "This primitive has [side effect] that dissolves the problem"
- "Instead of [old operation], we now [new operation]"
- "Complexity improves to O(?) because [reasoning]"

### Phase 5: Trade-Off Discussion (2-3 minutes)
Articulate the trade-off:
- What space do we use?
- When is this trade-off worth it?
- Alternative approaches for different constraints?
- How would this scale to [larger problem]?

### Phase 6: Pattern Recognition (1-2 minutes)
Connect to broader pattern family:
- "This pattern solves problems like: [family]"
- "The key insight applies to: [variations]"
- "You'd use this when: [scenario]"

## Interview-Ready Presentation

When presenting a solution, follow this structure:

```
1. Problem Restatement (30 sec)
   "So we're finding X in Y with constraint Z"

2. Brute-Force Overview (1 min)
   "My first approach: [simple strategy]"
   "Time/Space: O(?)/O(?)"
   "Why start here: it's correct"

3. The Optimization (2 min)
   "[Problem observation]"
   "[Primitive solution]"
   "[Why this works]"
   "New complexity: O(?)/O(?)"

4. Code Walk-Through (2-3 min)
   "Looking at the code..."
   "[Explain key parts]"

5. Verification (1 min)
   "On this example: [walk through]"
   "Edge cases: [how it handles]"

6. Talking Points (1 min)
   "The key insight is..."
   "This applies to..."
```

Total: 8-12 minutes for medium problem = Interview realistic

## Complexity Cheat Sheet

### Time Complexity (Common)
- O(1): Hash lookup, Array access
- O(log n): Binary search, Tree height
- O(n): Single pass through array
- O(n log n): Sorting, Search + sort
- O(n²): Nested loops
- O(2ⁿ): Brute-force with choices
- O(n!): Permutations

### Space Complexity (Common)
- O(1): Constant extra space
- O(log n): Recursion depth
- O(n): Hash map, extra array
- O(n²): Nested data structures

## When Stuck

**If unclear on problem**: Ask 3 clarifying questions
**If unsure on approach**: Walk through brute-force first (always valid)
**If code not working**: Trace through your example step-by-step
**If code correct but slow**: Look for the repeated operation
**If time running out**: Explain what you'd do next

## Example: Two Sum

```
Problem: Find two indices where array[i] + array[j] == target

Brute-Force:
- Try every pair with nested loop
- O(n²) time, O(1) space
- Talks point: "We check every combination"

Insight:
- For each number, we need to find its complement
- Hash map gives us O(1) lookup

Optimized:
- Single pass: check if complement exists, then add number
- O(n) time, O(n) space
- Talking point: "Hash lookup dissolves the 'find complement' problem"

Trade-off:
- Space: using O(n) extra space
- Worth it: O(n²) → O(n) is massive improvement
- When to choose differently: if space is extremely constrained
```

## Success Criteria

You're interview-ready when you can:
- ✓ Explain your thinking out loud clearly
- ✓ Identify the brute-force without optimization obsession
- ✓ Spot the optimization opportunity
- ✓ Articulate why the optimization works
- ✓ Code it cleanly
- ✓ Discuss trade-offs intelligently
- ✓ Apply patterns to novel problems

This command helps you practice the entire flow until it becomes natural.
