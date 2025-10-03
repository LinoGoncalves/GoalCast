## 📝 Description

<!-- Provide a clear and concise description of what this PR does -->

## 🔗 Related Issues

<!-- Link to GitHub issues this PR addresses -->
Closes #

## 🔄 Type of Change

- [ ] 🎉 New feature (non-breaking change which adds functionality)
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🔨 Refactoring (no functional changes)
- [ ] ⚙️ Configuration/tooling change

## 🧪 Testing

- [ ] All existing tests pass (`uv run pytest`)
- [ ] New tests added for new functionality
- [ ] Coverage maintained/improved: **___%**
- [ ] Manual testing completed (if applicable)

### Test Evidence

<!--
Paste test output or describe manual testing steps:
```
uv run pytest -v
```
-->

## ✅ Quality Checks

- [ ] Ruff linting passes (`uv run ruff check .`)
- [ ] Ruff formatting passes (`uv run ruff format --check .`)
- [ ] MyPy type checking passes (`uv run mypy src/goalcast`)
- [ ] No security issues (`uv run bandit -c pyproject.toml -r src/goalcast`)
- [ ] Pre-commit hooks pass (`uv run pre-commit run --all-files`)

## 📋 Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (docstrings, README, etc.)
- [ ] No breaking changes (or clearly documented if unavoidable)
- [ ] Semantic commit messages used
- [ ] Branch is up to date with `main`

## 🖼️ Screenshots (if applicable)

<!-- Add screenshots for UI changes -->

## 📌 Additional Notes

<!-- Any additional context, design decisions, or trade-offs made -->

---

**Review Instructions for AI/Human:**

- [ ] Code is correct and follows functional programming principles
- [ ] Type hints are comprehensive and accurate
- [ ] Error handling is robust
- [ ] No code duplication (DRY principle)
- [ ] Functions are small and single-purpose
- [ ] Tests cover edge cases and error paths
