# 🤖 Agentic Framework

**Universal Multi-Agent Orchestration System for Enterprise Software Development**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Tools](https://img.shields.io/badge/AI%20Tools-Tabnine%20%7C%20Copilot%20%7C%20Cursor-blue)](https://github.com/LinoGoncalves/agentic-framework)
[![Agents](https://img.shields.io/badge/Agents-22%2B-green)](https://github.com/LinoGoncalves/agentic-framework)

## 🎯 Overview

This directory contains a **reusable, tool-agnostic agentic AI framework** designed for human-AI collaboration across the full software development lifecycle (SDLC). The framework is completely independent of any specific project domain and can be extracted for use in ANY software project.

## 🚀 Key Features

- **Universal AI Tool Compatibility**: Works seamlessly with Tabnine, GitHub Copilot, Cursor, Codeium, JetBrains AI, and other AI coding assistants
- **Master Agent Orchestration**: Central coordinator that delegates to 22+ specialized agents
- **Rich Metadata Schema**: YAML frontmatter in all agent files for enhanced AI context awareness
- **Comprehensive Standards**: 20+ universal development standards covering API design, security, testing, documentation, and more
- **Human-in-the-Loop (HITL)**: Dynamic oversight modes (stepwise, autonomous, hybrid, standard)
- **Cognitive Enhancement**: Built-in meta-cognitive triggers for complex problem-solving

## 📁 Framework Structure

```text
agentic-framework/
├── master-agent.md              # 🎯 Master orchestrator (START HERE)
│
├── sub-agents/                  # 22+ specialized agent personas
│   ├── business-analyst-agent.md
│   ├── solutions-architect-agent.md
│   ├── software-developer-agent.md
│   ├── security-expert-agent.md
│   ├── ML-engineer-agent.md
│   ├── data-scientist-agent.md
│   ├── QA-engineer-agent.md
│   ├── devops-engineer-agent.md
│   └── ... (and 14 more)
│
├── standards/                   # Universal development standards
│   ├── api_design_patterns.md
│   ├── architectural-principles.md
│   ├── coding_styleguide.md
│   ├── testing_strategy.md
│   ├── secure_coding_checklist.md
│   ├── security_policies.md
│   ├── database_schema_standards.md
│   ├── iac_standards.md
│   ├── sre_handbook.md
│   └── ... (and 11 more)
│
├── scripts/                     # Framework CLI tools
│   └── cli.py                  # Command-line interface
│
├── templates/                   # Project scaffolding templates
│   ├── framework-management-guide.md
│   ├── project-brief-template.md
│   ├── quality-gates.md
│   └── workflow-state-management.md
│
└── agent-roster.json           # Agent registry and metadata
```

## 🤖 Agent Specializations

The framework includes specialized agents across all SDLC disciplines:

### **Business & Requirements**
- Product Owner Agent
- Business Analyst Agent
- UX Research Agent

### **Architecture & Design**
- Solutions Architect Agent
- Principal Engineer Agent
- UI Designer Agent

### **Development**
- Software Developer Agent
- ML Engineer Agent
- Data Engineer Agent
- Database Engineer Agent

### **Quality Assurance**
- QA Engineer Agent
- Test Manager Agent
- Test Automation Expert Agent

### **Security & Compliance**
- Security Expert Agent
- Network Engineer Agent

### **Operations & Infrastructure**
- DevOps Engineer Agent
- Site Reliability Engineer (SRE) Agent
- Cloud Engineer Agent

### **Process & Governance**
- Project Manager Agent
- Scrum Master Agent
- Technical Writer Agent

### **Advanced Capabilities**
- Critical Analyst Agent (assumption validation, evidence-based decision making)
- Blueprint Executor Agent (systematic implementation, debugging)

## 🚀 Quick Start

### For AI Tools (Tabnine, Copilot, Cursor, etc.)

```bash
# In your AI tool's chat interface
@workspace Load master-agent.md to orchestrate specialized agents
```

### For Human Developers

1. **Start with the Master Agent**: Read `master-agent.md` to understand the orchestration patterns
2. **Explore Specialized Agents**: Browse `sub-agents/` for domain-specific expertise
3. **Review Standards**: Reference `standards/` for best practices
4. **Use Templates**: Apply `templates/` for consistent project structure

### For CLI Workflow

```bash
# Start agentic workflow
python scripts/cli.py start
```

## 📚 Universal Development Standards

The framework includes comprehensive, tool-agnostic standards:

- **API Design**: RESTful patterns, GraphQL, gRPC, versioning
- **Architecture**: Microservices, event-driven, CQRS, clean architecture
- **Coding Style**: Language-agnostic best practices, formatting, naming
- **Testing**: Unit, integration, E2E, TDD, BDD strategies
- **Security**: OWASP Top 10, zero trust, encryption, access control
- **Database**: Schema design, migrations, indexing, normalization
- **Infrastructure as Code**: Terraform, CloudFormation, Bicep patterns
- **SRE**: Observability, incident response, SLOs, capacity planning
- **Documentation**: API docs, architecture diagrams, user guides
- **Agile Ceremonies**: Sprints, retrospectives, planning, standups

## 🔧 How to Use This Framework

### Option 1: Clone and Reference

Clone the framework into your project:

```bash
# Clone into your project
cd your-project/
git clone https://github.com/LinoGoncalves/agentic-framework.git

# Your project structure
your-project/
├── agentic-framework/      # This framework
├── your-domain/            # Your domain-specific content
├── src/                    # Your application code
└── ...
```

### Option 2: Git Submodule

Add as a git submodule for version tracking:

```bash
git submodule add https://github.com/LinoGoncalves/agentic-framework.git
git submodule update --init --recursive
```

### Option 3: Copy and Customize

Copy the entire framework directory to customize:

```bash
# Copy to new project
cp -r agentic-framework/ ../new-project/agentic-framework/

# Update references in new project
# Use master-agent.md as the orchestration entry point
```

## 🎯 Human Oversight Modes

The framework supports dynamic control over AI autonomy:

- **STEPWISE**: AI proposes each step, human reviews/approves
- **AUTONOMOUS**: AI executes full workflow, pauses at milestones
- **HYBRID**: AI asks for review at key decision points
- **STANDARD**: Default HITL workflow (AI drafts, human approves)

Change modes anytime with: `MODE: [STEPWISE | AUTONOMOUS | HYBRID | STANDARD]`

## 🧠 Cognitive Enhancement

Built-in meta-cognitive triggers automatically engage advanced reasoning:

- **Beast Mode**: For deadline-critical tasks and production issues
- **Quantum Thinking**: For strategic decisions and multi-stakeholder scenarios
- **Critical Analysis**: For assumption validation and risk assessment

## 🔗 Integration with Your Project

### 1. Load the Master Agent

Point your AI tool to `master-agent.md` as the orchestration entry point.

### 2. Define Your Domain Context

Create a separate directory (e.g., `your-domain/`) with:
- Project brief and requirements
- Domain-specific standards
- Business rules and logic
- Project context files

### 3. Build Your Application

Keep application code in `src/`, tests in `tests/`, etc.

### 4. Leverage Framework Standards

Reference `standards/` for universal best practices.

## 📖 Documentation

- **`master-agent.md`**: Complete orchestration guide and workflow patterns
- **`sub-agents/*.md`**: Individual agent capabilities and prompts
- **`standards/*.md`**: Detailed development standards and guidelines
- **`templates/*.md`**: Reusable project templates

## 🤝 Contributing

To add new agents or standards to the framework:

1. Follow the YAML metadata schema in existing agent files
2. Ensure tool-agnostic approach (works with all AI coding assistants)
3. Document cognitive triggers and interaction patterns
4. Add to `agent-roster.json` registry
5. Submit a pull request with clear documentation

## 📜 License

[MIT License](LICENSE) - Free to use, modify, and distribute.

## 🌟 Example Projects

This framework is successfully used in:
- **Telco Call Centre Agent**: AI-powered ticket classification with Google Gemini LLM
- More examples coming soon!

## 📞 Support & Community

- **Issues**: [GitHub Issues](https://github.com/LinoGoncalves/agentic-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/LinoGoncalves/agentic-framework/discussions)
- **Contributions**: Pull requests welcome!

## 🎉 Framework Philosophy

**"AI Drafts, Human Approves"**

The core principle is collaboration, not replacement. Every specialized agent produces a first draft that humans review, refine, and approve. The framework enhances human capabilities without removing human judgment from the critical path.

---

**Ready to orchestrate?** Start with `master-agent.md` 🚀

## 📊 Stats

- **22+ Specialized Agents** across all SDLC disciplines
- **20+ Universal Standards** for enterprise development
- **Tool-Agnostic Design** works with any AI coding assistant
- **YAML-Enhanced Metadata** for improved AI context awareness
- **Human-in-the-Loop** modes for flexible autonomy control
