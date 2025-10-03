# GitHub Branch Protection Recommendations

## Branch Protection Settings for `main`

### **Recommended GitHub Settings**

Navigate to: `https://github.com/LinoGoncalves/GoalCast/settings/branches`

**Configure the following for `main` branch:**

### ✅ **Require Pull Request Reviews**
- ✅ Require pull request before merging
- ✅ Require approvals: **1** (you review AI-generated PRs, or GitHub bot reviews yours)
- ❌ Dismiss stale pull request approvals (not needed for solo dev)
- ❌ Require review from code owners (not needed yet)

### ✅ **Require Status Checks to Pass**
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- **Required checks** (after CI/CD setup):
  - `ruff-lint` (code quality)
  - `ruff-format-check` (formatting)
  - `mypy` (type checking)
  - `pytest` (all tests passing)
  - `coverage` (minimum 80%)

### ✅ **Additional Restrictions**
- ✅ Require conversation resolution before merging
- ✅ Require linear history (optional, keeps clean history)
- ❌ Include administrators (allow yourself to bypass in emergencies)
- ❌ Restrict who can push (not needed for solo dev)

---

## Workflow in Practice

### **AI Generates Code → You Review via PR**

```bash
# 1. AI creates feature branch
git checkout -b feature/epic-1-fixtures-ingestion

# 2. AI commits code
git add src/goalcast/data/ingest.py tests/test_data_ingest.py
git commit -m "feat(data): implement fixtures data ingestion

- Add PremierLeague.com scraper
- Implement Pydantic validation schemas
- Add unit tests with 95% coverage
- Closes #8"

# 3. Push to GitHub
git push origin feature/epic-1-fixtures-ingestion

# 4. Create PR via GitHub UI or CLI
gh pr create --title "feat(data): Fixtures data ingestion pipeline" \
  --body "Implements user story #8 for EPIC #1" \
  --assignee @me

# 5. GitHub Actions run automated checks (CI/CD)
# 6. You review code in PR interface
# 7. Merge to main after approval
```

### **You Generate Code → AI/GitHub Bot Reviews**

Same process, but you can:
- Use **GitHub Copilot Pull Request Reviews** (if available)
- Set up **Codecov bot** for coverage comments
- Use **pre-commit hooks** for instant local feedback

---

## Why Pull Requests for Solo Development?

### **Benefits:**

1. **HITL Checkpoint**: Forces you to review AI-generated code before it hits `main`
2. **Change Context**: PR description captures *why* the change was made
3. **GitHub Integration**: Links to Issues (#1, #2), closes them automatically
4. **Audit Trail**: Complete history of all changes with rationale
5. **CI/CD Gate**: Automated quality checks run before merge
6. **Rollback Safety**: Easy to revert a merged PR if needed
7. **Future Collaboration**: Already set up if you add team members

### **When to Skip PRs:**

- ❌ Typos in documentation (direct commit to `main` is fine)
- ❌ README updates (low risk)
- ⚠️ **Everything else should go through PR** (especially AI-generated code)

---

## Semantic Commit Messages

Use **Conventional Commits** for clear history:

```bash
feat(scope): add new feature
fix(scope): bug fix
docs(scope): documentation only
refactor(scope): code refactoring
test(scope): adding tests
chore(scope): tooling, dependencies

# Examples:
git commit -m "feat(models): implement Poisson baseline model"
git commit -m "fix(data): handle missing xG values in validation"
git commit -m "test(simulation): add Monte Carlo edge case tests"
git commit -m "docs(api): add FastAPI endpoint documentation"
git commit -m "chore(deps): upgrade pandas to 2.3.4"
```

**Scope options:**
- `data` - Data ingestion module
- `models` - Statistical models
- `simulation` - Monte Carlo engine
- `llm` - LLM interpretation
- `api` - FastAPI services
- `ui` - Streamlit dashboard
- `utils` - Utilities
- `tests` - Test files
- `ci` - CI/CD configuration

---

## PR Template

`.github/pull_request_template.md` (to be created):

```markdown
## Description
<!-- Brief description of what this PR does -->

## Related Issues
<!-- Link to GitHub issues -->
Closes #

## Type of Change
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Coverage: ___%

## Quality Checks
- [ ] Ruff linting passes
- [ ] Ruff formatting passes
- [ ] Mypy type checking passes
- [ ] No security issues (bandit/semgrep)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (if needed)
- [ ] No breaking changes (or documented if unavoidable)
```

---

## Recommended Approach

**For Solo Development with AI Assistance:**

1. ✅ Use feature branches per Epic/User Story
2. ✅ Require PRs for all code changes to `main`
3. ✅ Set up pre-commit hooks (local quality gate)
4. ✅ Set up GitHub Actions CI/CD (remote quality gate)
5. ✅ Use semantic commit messages
6. ✅ Self-review PRs before merging
7. ✅ Link PRs to GitHub Issues
8. ⚠️ Allow direct commits to `main` for docs/typos (optional)
