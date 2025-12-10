---
model: claude-opus-4-1
allowed-tools: Task, Read, Write, Bash(*), Glob, Grep
argument-hint: <feature-description> [--complexity=<level>] [--learning-focus=<aspect>] [--collaboration=<mode>]
description: Intelligent feature development with multi-expert orchestration and adaptive learning
---

# Intelligent Feature Development Engine

Implement complete features through multi-expert collaboration with adaptive learning, structured dissent, and cognitive harmonics optimization. Transform feature development into a comprehensive learning and building experience that delivers both functionality and team capability growth.

[Extended thinking: Enhanced workflow integrates Split Team Framework for comprehensive feature analysis, Teacher Framework for skill development during implementation, and structured dissent for robust architectural decisions. Each phase includes meta-cognitive reflection and knowledge transfer opportunities.]

## Intelligent Development Framework

### Multi-Expert Team Assembly
**Core Development Specialists:**
- **Feature Architect**: Overall design strategy and system integration
- **Frontend Specialist**: User interface and experience implementation
- **Backend Engineer**: Service logic and data management
- **Quality Assurance**: Testing strategy and validation
- **Performance Optimizer**: Efficiency and scalability considerations
- **Security Analyst**: Protection and compliance requirements

**Learning and Growth Roles:**
- **Adaptive Mentor**: Skill development and knowledge transfer
- **Pattern Recognition**: Best practice identification and application
- **Knowledge Bridge**: Cross-domain learning and connection building

**Challenge and Innovation:**
- **Constructive Critic**: Design assumption challenging and alternative generation
- **Future-Proofing Visionary**: Long-term evolution and maintainability advocacy

### Development Approach Selection

#### Option A: Collaborative Multi-Expert Development
- Use `/orchestrate` command for comprehensive team coordination
- Integrate multiple perspectives for robust feature design
- Include structured dissent for design validation
- Emphasis on learning and capability building

#### Option B: Enhanced TDD-Driven Development
- Use `/tdd-cycle` workflow with multi-expert enhancement
- Integrate constructive challenge in test design
- Include adaptive learning for TDD skill development
- Meta-cognitive reflection on testing effectiveness

#### Option C: Learning-Focused Development
- Use `/teach_concept` for skill building during implementation
- Use `/adaptive_mentor` for personalized development guidance
- Include `/pattern_discovery` for reusable pattern identification
- Emphasis on transferable knowledge and capability growth

### Adaptive Complexity Management
- **Simple Features**: Direct implementation with basic orchestration
- **Moderate Features**: Multi-expert collaboration with structured phases
- **Complex Features**: Comprehensive orchestration with structured dissent
- **Learning Features**: High educational focus with mentoring integration

## Traditional Development Steps

1. **Backend Architecture Design**
   - Use Task tool with subagent_type="backend-architect" 
   - Prompt: "Design RESTful API and data model for: $ARGUMENTS. Include endpoint definitions, database schema, and service boundaries."
   - Save the API design and schema for next agents

2. **Frontend Implementation**
   - Use Task tool with subagent_type="frontend-developer"
   - Prompt: "Create UI components for: $ARGUMENTS. Use the API design from backend-architect: [include API endpoints and data models from step 1]"
   - Ensure UI matches the backend API contract

3. **Test Coverage**
   - Use Task tool with subagent_type="test-automator"
   - Prompt: "Write comprehensive tests for: $ARGUMENTS. Cover both backend API endpoints: [from step 1] and frontend components: [from step 2]"
   - Include unit, integration, and e2e tests

4. **Production Deployment**
   - Use Task tool with subagent_type="deployment-engineer"
   - Prompt: "Prepare production deployment for: $ARGUMENTS. Include CI/CD pipeline, containerization, and monitoring for the implemented feature."
   - Ensure all components from previous steps are deployment-ready

## TDD Development Steps

When using TDD mode, the sequence changes to:

1. **Test-First Backend Design**
   - Use Task tool with subagent_type="tdd-orchestrator"
   - Prompt: "Design and write failing tests for backend API: $ARGUMENTS. Define test cases before implementation."
   - Create comprehensive test suite for API endpoints

2. **Test-First Frontend Design**
   - Use Task tool with subagent_type="tdd-orchestrator"
   - Prompt: "Write failing tests for frontend components: $ARGUMENTS. Include unit and integration tests."
   - Define expected UI behavior through tests

3. **Incremental Implementation**
   - Use Task tool with subagent_type="tdd-orchestrator"
   - Prompt: "Implement features to pass tests for: $ARGUMENTS. Follow strict red-green-refactor cycles."
   - Build features incrementally, guided by tests

4. **Refactoring & Optimization**
   - Use Task tool with subagent_type="tdd-orchestrator"
   - Prompt: "Refactor implementation while maintaining green tests: $ARGUMENTS. Optimize for maintainability."
   - Improve code quality with test safety net

5. **Production Deployment**
   - Use Task tool with subagent_type="deployment-engineer"
   - Prompt: "Deploy TDD-developed feature: $ARGUMENTS. Verify all tests pass in CI/CD pipeline."
   - Ensure test suite runs in deployment pipeline

## Execution Parameters

- **--tdd**: Enable TDD mode (uses tdd-orchestrator agent)
- **--strict-tdd**: Enforce strict red-green-refactor cycles
- **--test-coverage-min**: Set minimum test coverage threshold (default: 80%)
- **--tdd-cycle**: Use dedicated tdd-cycle workflow for granular control

Aggregate results from all agents and present a unified implementation plan.

Feature description: $ARGUMENTS
