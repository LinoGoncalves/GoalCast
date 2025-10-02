# Autonomous Cognitive Trigger Configuration

## Overview

This document defines the automatic trigger conditions that enable the Master Agent to autonomously engage advanced meta-cognitive reasoning modes without explicit human prompting. These triggers ensure that appropriate cognitive enhancement is applied based on task characteristics, risk factors, and quality requirements.

## Trigger Classification System

### Tier 1: Complexity-Based Auto-Escalation

**Activation Conditions:**
```yaml
complexity_triggers:
  - task_complexity: HIGH
  - multiple_dependencies: >= 5
  - cross_functional_teams: >= 3
  - technical_debt_risk: HIGH
  - integration_complexity: MEDIUM+
```

**Auto-Engaged Agents:**
- `quantum-thinking-framework-agent`: Multi-dimensional analysis
- `research-specialist-agent`: Knowledge discovery (if new_domain == TRUE)

**Reasoning Enhancement:**
- Surface/hidden/meta layer analysis
- Dependency mapping and risk assessment
- Multi-perspective validation

### Tier 2: Risk-Based Auto-Escalation

**Activation Conditions:**
```yaml
risk_triggers:
  - security_implications: TRUE
  - data_privacy_risk: TRUE
  - compliance_required: TRUE
  - financial_impact: >= MEDIUM
  - reputation_risk: >= MEDIUM
  - regulatory_oversight: TRUE
```

**Auto-Engaged Agents:**
- `critical-analyst-agent`: Assumption validation and risk analysis
- `quantum-thinking-framework-agent`: Multi-dimensional risk assessment
- `security-expert-agent`: Security domain expertise (if security_implications == TRUE)

**Reasoning Enhancement:**
- Adversarial validation of assumptions
- Constitutional framework application
- Risk mitigation strategy development

### Tier 3: Quality-Based Auto-Escalation

**Activation Conditions:**
```yaml
quality_triggers:
  - production_deployment: TRUE
  - customer_facing: TRUE
  - mission_critical: TRUE
  - performance_requirements: HIGH
  - reliability_requirements: >= 99.9%
  - zero_downtime_required: TRUE
```

**Auto-Engaged Agents:**
- `beast-mode-executor-agent`: Autonomous excellence execution
- `critical-analyst-agent`: Quality validation and testing rigor
- `principal-engineer-agent`: Technical excellence oversight

**Reasoning Enhancement:**
- Exhaustive validation until perfect outcomes
- Iterative refinement and optimization
- Comprehensive quality gate enforcement

### Tier 4: Innovation-Based Auto-Escalation

**Activation Conditions:**
```yaml
innovation_triggers:
  - new_technology: TRUE
  - architectural_change: TRUE
  - research_required: TRUE
  - prototype_development: TRUE
  - proof_of_concept: TRUE
  - experimental_approach: TRUE
```

**Auto-Engaged Agents:**
- `quantum-thinking-framework-agent`: Multi-dimensional exploration
- `research-specialist-agent`: Knowledge synthesis and validation
- `principal-engineer-agent`: Technical innovation leadership
- `critical-analyst-agent`: Innovation risk assessment

**Reasoning Enhancement:**
- Systematic research and discovery protocols
- Multi-perspective innovation analysis
- Evidence-based decision making for new approaches

## Context-Aware Auto-Enhancement

### Project Context Multipliers

**High Stakes Project:**
```yaml
high_stakes_multipliers:
  - auto_escalate_all_tasks: tier_2_minimum
  - mandatory_agents: ["critical-analyst-agent", "principal-engineer-agent"]
  - validation_requirements: EXHAUSTIVE
  - approval_gates: MULTIPLE_HUMAN_REVIEWERS
```

**Learning/Research Project:**
```yaml
learning_multipliers:
  - default_agents: ["research-specialist-agent", "quantum-thinking-framework-agent"]
  - knowledge_building: PRIORITIZED
  - experimentation_encouraged: TRUE
  - documentation_requirements: COMPREHENSIVE
```

**Compliance/Regulated Project:**
```yaml
compliance_multipliers:
  - mandatory_critical_analysis: ALL_DECISIONS
  - audit_trail_required: TRUE
  - regulatory_validation: CONTINUOUS
  - risk_assessment: MANDATORY
```

**Innovation Project:**
```yaml
innovation_multipliers:
  - default_quantum_thinking: TRUE
  - research_specialist_engagement: CONTINUOUS
  - experimental_validation: REQUIRED
  - iterative_refinement: ENCOURAGED
```

### Domain-Specific Auto-Routing

**Cloud/Infrastructure Tasks:**
```yaml
cloud_auto_routing:
  - primary_specialist: "azure-principal-architect-agent"
  - quality_assurance: "beast-mode-executor-agent" 
  - if: production_deployment == TRUE
  - security_review: "security-expert-agent"
  - if: external_facing == TRUE
```

**Frontend Development:**
```yaml
frontend_auto_routing:
  - primary_specialist: "expert-react-frontend-engineer-agent"
  - user_experience_validation: "critical-analyst-agent"
  - accessibility_review: "critical-analyst-agent"
  - if: customer_facing == TRUE
```

**Backend Development:**
```yaml
backend_auto_routing:
  - primary_specialist: "expert-dotnet-software-engineer-agent"
  - architecture_review: "quantum-thinking-framework-agent"
  - if: architectural_impact == TRUE
  - performance_validation: "beast-mode-executor-agent"
  - if: performance_critical == TRUE
```

**Data Science/ML:**
```yaml
datascience_auto_routing:
  - research_specialist: "research-specialist-agent"
  - comprehensive_analysis: "quantum-thinking-framework-agent"
  - validation_rigor: "critical-analyst-agent"
  - ml_expertise: "ML-engineer-agent"
```

## Autonomous Activation Protocols

### Beast Mode Auto-Activation

**Trigger Conditions:**
1. **Deadline Critical**: `timeline <= 48_hours AND scope >= MEDIUM`
2. **Production Issues**: `severity >= HIGH AND customer_impact == TRUE`
3. **Complex Problem**: `solution_attempts >= 2 AND progress < 50%`
4. **Quality Gates**: `deployment_readiness_check == TRUE`

**Activation Protocol:**
```yaml
beast_mode_protocol:
  behavior: "Continue autonomous iteration until task completion"
  validation: "All acceptance criteria + quality standards met"
  research: "Comprehensive until perfect understanding"
  refinement: "Iterative until optimal solution achieved"
  exit_condition: "Human validation of complete solution"
```

### Quantum Thinking Auto-Activation

**Trigger Conditions:**
1. **Strategic Decisions**: `system_architecture OR business_strategy affected`
2. **Multi-Stakeholder**: `stakeholder_count >= 4 AND conflicting_requirements == TRUE`
3. **Risk Assessment**: `potential_impact >= HIGH`
4. **Innovation**: `new_feature_development OR technology_evaluation`

**Activation Protocol:**
```yaml
quantum_thinking_protocol:
  analysis_layers: ["surface", "hidden", "meta", "systemic", "temporal"]
  adversarial_validation: "Challenge all assumptions"
  constitutional_framework: "Apply core principles to decisions"
  multi_perspective: "Technical, business, user, operational, strategic"
  synthesis: "Integrate insights into coherent recommendation"
```

## Human Override & Transparency

### Autonomous Enhancement Disclosure

Every auto-enhanced interaction includes:
```yaml
meta_cognitive_disclosure:
  enhancement_status: "ACTIVE"
  reasoning_mode: "[Beast Mode | Quantum Thinking | Critical Analysis]"
  trigger_source: "[Complexity | Risk | Quality | Innovation]"
  engaged_agents: ["agent1", "agent2", "agent3"]
  human_override: "Type 'STANDARD' to disable enhancement"
  reasoning_trail: "Available for human review"
```

### Human Authority Preservation

**Override Commands:**
- `STANDARD`: Disable all auto-enhancement for current session
- `MANUAL_COGNITIVE`: Human will explicitly choose reasoning modes
- `AUDIT_MODE`: Show all trigger evaluations but don't auto-activate
- `ENHANCED_ONLY`: Force maximum cognitive enhancement for all tasks

**HITL Compliance:**
- All autonomous decisions tagged with full reasoning trail
- Human approval required for final deliverable sign-off
- Transparent disclosure of cognitive enhancement status
- Immediate human override capability maintained

## Implementation Guidelines

### Integration with Master Agent

1. **Trigger Evaluation**: Master agent evaluates triggers on every incoming request
2. **Agent Pre-loading**: Automatically loads appropriate meta-cognitive agents
3. **Enhanced Workflow**: Executes standard workflow with cognitive enhancement
4. **Human Handoff**: Maintains HITL principles with enhanced deliverables
5. **Transparency**: Clear disclosure of autonomous reasoning enhancement

### Quality Assurance

- **Trigger Accuracy**: Regular validation that triggers activate appropriately
- **Enhancement Value**: Measurement of cognitive enhancement impact on outcomes
- **Human Satisfaction**: Monitoring of human acceptance of autonomous enhancements
- **Performance Impact**: Ensuring cognitive enhancement doesn't degrade efficiency

### Continuous Improvement

- **Trigger Refinement**: Iterative improvement of trigger conditions based on outcomes
- **New Pattern Integration**: Adding new cognitive patterns as they prove valuable
- **Domain Expansion**: Extending auto-routing to additional technical domains
- **Feedback Integration**: Human feedback loop for cognitive enhancement effectiveness

---

## Configuration Management

**File Location**: `telco-call-centre/development-standards/autonomous-cognitive-triggers.md`

**Version Control**: All trigger modifications require:
- Documentation of change rationale
- Impact assessment on existing workflows
- Human review and approval of trigger modifications
- Rollback capability for trigger configuration changes

**Tool Compatibility**: Universal configuration works across:
- Tabnine: Context-aware trigger evaluation
- GitHub Copilot: Chat-based cognitive enhancement
- Cursor: Composer-integrated reasoning modes
- Codeium: Universal meta-cognitive activation
- JetBrains AI: IDE-integrated autonomous enhancement