# Contributing to Agentic Framework

Thank you for your interest in contributing to the Agentic Framework! This document provides guidelines for contributing to this project.

## 🤝 How to Contribute

### Reporting Issues

1. Check if the issue already exists in [GitHub Issues](https://github.com/LinoGoncalves/agentic-framework/issues)
2. Use the issue templates provided
3. Include clear descriptions and examples

### Suggesting Enhancements

1. Open a discussion in [GitHub Discussions](https://github.com/LinoGoncalves/agentic-framework/discussions)
2. Describe the enhancement and its benefits
3. Explain how it maintains tool-agnostic compatibility

### Adding New Agents

When creating a new specialized agent:

1. **Follow the YAML Metadata Schema**:
   ```yaml
   ---
   agent_type: "specialized"
   specialization: "Your Specialization"
   tools_compatible: ["tabnine", "github_copilot", "cursor", "codeium", "jetbrains_ai"]
   context_scope: "local"  # or "global"
   interaction_patterns: ["step_by_step", "approval_checkpoints"]
   model_suggestions:
     optimal: ["o1-mini", "claude-3.5-sonnet"]
     acceptable: ["gpt-4", "gemini-pro"]
   oversight_mode: "HITL"
   ---
   ```

2. **Structure Your Agent File**:
   - Clear role definition
   - Cognitive triggers (when to engage this agent)
   - Key responsibilities
   - Source of truth references (to standards/)
   - Deliverable format specifications
   - Quality criteria

3. **Maintain Tool Agnosticism**:
   - Avoid tool-specific syntax
   - Focus on universal AI interaction patterns
   - Test with multiple AI coding assistants

4. **Update Registry**:
   - Add your agent to `agent-roster.json`
   - Include all required metadata fields

### Adding New Standards

When contributing new development standards:

1. **Ensure Universal Applicability**:
   - Not tied to specific technologies
   - Applicable across domains
   - Industry best practices

2. **Clear Documentation**:
   - Purpose and scope
   - When to apply
   - Examples and anti-patterns
   - Related standards

3. **Consistency**:
   - Follow existing standard formats
   - Use clear section headings
   - Include practical examples

### Pull Request Process

1. **Fork the Repository**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**:
   - Follow existing code/documentation style
   - Update relevant documentation
   - Add/update tests if applicable

4. **Test Your Changes**:
   - Verify with multiple AI tools if possible
   - Ensure no broken references
   - Check markdown rendering

5. **Commit with Clear Messages**:
   ```bash
   git commit -m "feat: add [feature name]

   - Detailed description of changes
   - Why this change is needed
   - Any breaking changes"
   ```

6. **Push and Create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```
   - Fill out the PR template completely
   - Link related issues
   - Describe testing performed

7. **Code Review**:
   - Respond to feedback promptly
   - Make requested changes
   - Maintain discussion focus

## 📝 Style Guidelines

### Markdown Files
- Use clear headings (H1 for title, H2 for sections)
- Include code examples where relevant
- Use bullet points for lists
- Keep line length reasonable (~80-120 chars)

### YAML Frontmatter
- Always include all required fields
- Use consistent formatting
- Add comments for complex configurations

### Documentation
- Write for clarity
- Include examples
- Explain "why" not just "what"
- Keep it tool-agnostic

## 🔍 Testing

Before submitting:
- [ ] Test with at least 2 different AI coding assistants
- [ ] Verify all links and references work
- [ ] Check markdown formatting
- [ ] Ensure YAML is valid
- [ ] Update agent-roster.json if needed

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🎯 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn
- Assume good intentions

## 💡 Questions?

- Open a [Discussion](https://github.com/LinoGoncalves/agentic-framework/discussions)
- Tag maintainers for guidance
- Check existing issues and PRs

Thank you for contributing to making AI-human collaboration better! 🚀
