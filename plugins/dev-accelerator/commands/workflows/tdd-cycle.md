---
model: claude-opus-4-1
allowed-tools: Task, Read, Write, Bash(*), Grep, Glob
argument-hint: <feature-requirement> [--complexity=<level>] [--learning-mode=<approach>] [--dissent-level=<intensity>]
description: Test-Driven Development with multi-expert orchestration and adaptive learning integration
---

# Advanced TDD Orchestration Engine

Execute comprehensive Test-Driven Development through multi-expert collaboration with structured dissent, adaptive learning, and cognitive harmonics optimization. Transform traditional TDD into an intelligent, self-improving development process that builds both code quality and team understanding.

[Extended thinking: This enhanced workflow integrates Split Team Framework for multi-perspective analysis, Teacher Framework for adaptive learning, and structured dissent protocols for robust test design. Each phase includes constructive challenge mechanisms and meta-cognitive reflection for continuous improvement.]

## Configuration

### Multi-Expert Team Configuration
**Core TDD Specialists:**
- **Test Strategist**: Overall test approach and architecture design
- **Quality Guardian**: Test completeness and edge case coverage advocate
- **Implementation Guide**: Code structure and maintainability focus
- **Performance Analyst**: Testing efficiency and execution speed optimization
- **Usability Advocate**: Developer experience and test readability champion

**Challenge Perspectives:**
- **Constructive Critic**: Questions test assumptions and approaches
- **Pragmatic Realist**: Balances ideal practices with practical constraints
- **Future-Proofing Visionary**: Considers long-term maintainability and evolution

### Adaptive Learning Parameters
- **Novice Mode**: Heavy scaffolding, detailed explanations, step-by-step guidance
- **Intermediate Mode**: Moderate guidance with pattern recognition development
- **Advanced Mode**: Minimal scaffolding, collaborative peer-level interaction
- **Expert Mode**: Innovation-focused with paradigm challenging

### Quality Thresholds
- **Coverage Standards**: Line coverage 80%, Branch coverage 75%, Critical path 100%
- **Complexity Limits**: Cyclomatic complexity ≤ 10, Method length ≤ 20 lines
- **Architecture Standards**: Class length ≤ 200 lines, Duplicate blocks ≤ 3 lines
- **Test Quality**: Fast (<100ms), Isolated, Repeatable, Self-validating

## Phase 1: Multi-Expert Requirements Analysis and Test Strategy

### 1. Collaborative Requirements Analysis
[Extended thinking: Leverage multi-perspective analysis to ensure comprehensive understanding of requirements from different stakeholder viewpoints, reducing blind spots and improving test coverage.]

**Primary Analysis:**
- Use `/multi_perspective` command with `"$ARGUMENTS requirements analysis" technical --perspectives=5 --integration=comprehensive`
- **Test Strategist**: Overall testing approach and comprehensive coverage strategy
- **Quality Guardian**: Edge cases, error conditions, and boundary value identification
- **Implementation Guide**: Code structure implications and testability requirements
- **Performance Analyst**: Performance testing needs and execution constraints
- **Usability Advocate**: Developer experience and test maintainability considerations

**Constructive Challenge:**
- Use `/constructive_dissent` command with `"Proposed test strategy for $ARGUMENTS" --dissent-intensity=systematic --alternatives=2`
- Challenge assumptions about what needs testing and how
- Generate alternative testing approaches for comparison
- Question whether requirements are testable as specified

**Adaptive Learning Integration:**
- Use `/teach_concept` command with `"test strategy for $ARGUMENTS" intermediate --approach=socratic` for learning-oriented sessions
- Build understanding of testing principles through guided discovery
- Develop pattern recognition for similar future testing challenges

### 2. Enhanced Test Architecture Design
[Extended thinking: Create robust test architecture through collaborative design with structured disagreement to identify potential weaknesses and improvements.]

**Collaborative Design:**
- Use `/orchestrate` command with `"design test architecture for $ARGUMENTS" moderate test-automator,performance-engineer,architect-review --mode=dialectical`
- Generate test architecture through structured collaboration
- Include fixture design, mock strategy, and test data management
- Ensure architecture supports TDD principles: fast, isolated, repeatable, self-validating

**Architecture Validation:**
- Use `/assumption_audit` command with `"Test architecture assumptions for $ARGUMENTS" --audit-depth=structural --challenge-method=alternative-generation`
- Challenge fundamental assumptions about test organization and structure
- Generate alternative architectural approaches for comparison
- Validate architecture against long-term maintainability and scalability needs

## Phase 2: RED - Write Failing Tests

### 3. Write Unit Tests (Failing)
- Use Task tool with subagent_type="test-automator"
- Prompt: "Write FAILING unit tests for: $ARGUMENTS. Tests must fail initially. Include edge cases, error scenarios, and happy paths. DO NOT implement production code."
- Output: Failing unit tests, test documentation
- **CRITICAL**: Verify all tests fail with expected error messages

### 4. Verify Test Failure
- Use Task tool with subagent_type="code-reviewer"
- Prompt: "Verify that all tests for: $ARGUMENTS are failing correctly. Ensure failures are for the right reasons (missing implementation, not test errors). Confirm no false positives."
- Output: Test failure verification report
- **GATE**: Do not proceed until all tests fail appropriately

## Phase 3: GREEN - Make Tests Pass

### 5. Minimal Implementation
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Implement MINIMAL code to make tests pass for: $ARGUMENTS. Focus only on making tests green. Do not add extra features or optimizations. Keep it simple."
- Output: Minimal working implementation
- Constraint: No code beyond what's needed to pass tests

### 6. Verify Test Success
- Use Task tool with subagent_type="test-automator"
- Prompt: "Run all tests for: $ARGUMENTS and verify they pass. Check test coverage metrics. Ensure no tests were accidentally broken."
- Output: Test execution report, coverage metrics
- **GATE**: All tests must pass before proceeding

## Phase 4: REFACTOR - Improve Code Quality

### 7. Code Refactoring
- Use Task tool with subagent_type="code-reviewer"
- Prompt: "Refactor implementation for: $ARGUMENTS while keeping tests green. Apply SOLID principles, remove duplication, improve naming, and optimize performance. Run tests after each refactoring."
- Output: Refactored code, refactoring report
- Constraint: Tests must remain green throughout

### 8. Test Refactoring
- Use Task tool with subagent_type="test-automator"
- Prompt: "Refactor tests for: $ARGUMENTS. Remove test duplication, improve test names, extract common fixtures, and enhance test readability. Ensure tests still provide same coverage."
- Output: Refactored tests, improved test structure
- Validation: Coverage metrics unchanged or improved

## Phase 5: Integration and System Tests

### 9. Write Integration Tests (Failing First)
- Use Task tool with subagent_type="test-automator"
- Prompt: "Write FAILING integration tests for: $ARGUMENTS. Test component interactions, API contracts, and data flow. Tests must fail initially."
- Output: Failing integration tests
- Validation: Tests fail due to missing integration logic

### 10. Implement Integration
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Implement integration code for: $ARGUMENTS to make integration tests pass. Focus on component interaction and data flow."
- Output: Integration implementation
- Validation: All integration tests pass

## Phase 6: Continuous Improvement Cycle

### 11. Performance and Edge Case Tests
- Use Task tool with subagent_type="test-automator"
- Prompt: "Add performance tests and additional edge case tests for: $ARGUMENTS. Include stress tests, boundary tests, and error recovery tests."
- Output: Extended test suite
- Metric: Increased test coverage and scenario coverage

### 12. Final Code Review
- Use Task tool with subagent_type="architect-review"
- Prompt: "Perform comprehensive review of: $ARGUMENTS. Verify TDD process was followed, check code quality, test quality, and coverage. Suggest improvements."
- Output: Review report, improvement suggestions
- Action: Implement critical suggestions while maintaining green tests

## Incremental Development Mode

For test-by-test development:
1. Write ONE failing test
2. Make ONLY that test pass
3. Refactor if needed
4. Repeat for next test

Use this approach by adding `--incremental` flag to focus on one test at a time.

## Test Suite Mode

For comprehensive test suite development:
1. Write ALL tests for a feature/module (failing)
2. Implement code to pass ALL tests
3. Refactor entire module
4. Add integration tests

Use this approach by adding `--suite` flag for batch test development.

## Validation Checkpoints

### RED Phase Validation
- [ ] All tests written before implementation
- [ ] All tests fail with meaningful error messages
- [ ] Test failures are due to missing implementation
- [ ] No test passes accidentally

### GREEN Phase Validation
- [ ] All tests pass
- [ ] No extra code beyond test requirements
- [ ] Coverage meets minimum thresholds
- [ ] No test was modified to make it pass

### REFACTOR Phase Validation
- [ ] All tests still pass after refactoring
- [ ] Code complexity reduced
- [ ] Duplication eliminated
- [ ] Performance improved or maintained
- [ ] Test readability improved

## Coverage Reports

Generate coverage reports after each phase:
- Line coverage
- Branch coverage
- Function coverage
- Statement coverage

## Failure Recovery

If TDD discipline is broken:
1. **STOP** immediately
2. Identify which phase was violated
3. Rollback to last valid state
4. Resume from correct phase
5. Document lesson learned

## TDD Metrics Tracking

Track and report:
- Time in each phase (Red/Green/Refactor)
- Number of test-implementation cycles
- Coverage progression
- Refactoring frequency
- Defect escape rate

## Anti-Patterns to Avoid

- Writing implementation before tests
- Writing tests that already pass
- Skipping the refactor phase
- Writing multiple features without tests
- Modifying tests to make them pass
- Ignoring failing tests
- Writing tests after implementation

## Success Criteria

- 100% of code written test-first
- All tests pass continuously
- Coverage exceeds thresholds
- Code complexity within limits
- Zero defects in covered code
- Clear test documentation
- Fast test execution (< 5 seconds for unit tests)

## Notes

- Enforce strict RED-GREEN-REFACTOR discipline
- Each phase must be completed before moving to next
- Tests are the specification
- If a test is hard to write, the design needs improvement
- Refactoring is NOT optional
- Keep test execution fast
- Tests should be independent and isolated

TDD implementation for: $ARGUMENTS