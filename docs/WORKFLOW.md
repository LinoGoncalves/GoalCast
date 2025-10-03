# Development Workflow Guide

## 🎯 Overview

This document describes the recommended development workflow for GoalCast, optimized for solo development with AI assistance.

## 📋 Quick Reference

```bash
# 1. Install pre-commit hooks (one-time setup)
uv run pre-commit install

# 2. Create feature branch
git checkout -b feature/epic-1-data-ingestion

# 3. Make changes, commit with semantic messages
git add .
git commit -m "feat(data): implement fixtures ingestion"

# 4. Pre-commit hooks run automatically
# ✅ Ruff linting
# ✅ Ruff formatting
# ✅ MyPy type checking
# ✅ Bandit security scan
# ✅ File quality checks

# 5. Push to GitHub
git push origin feature/epic-1-data-ingestion

# 6. Create Pull Request
gh pr create --title "feat(data): Fixtures ingestion pipeline" \
             --body "Implements #8 for EPIC #1"

# 7. GitHub Actions CI runs automatically
# 8. Review PR → Merge to main
```

---

## 🌳 Branching Strategy

### Branch Types

| Branch Type | Pattern | Purpose | Example |
|------------|---------|---------|---------|
| **Main** | `main` | Production-ready code | `main` |
| **Feature** | `feature/<epic>-<description>` | New features/epics | `feature/epic-1-data-ingestion` |
| **Bugfix** | `bugfix/<issue>-<description>` | Bug fixes | `bugfix/123-xg-validation` |
| **Enhancement** | `enhancement/<description>` | Improvements | `enhancement/add-correlation-analysis` |
| **Refactor** | `refactor/<description>` | Code cleanup | `refactor/extract-data-validators` |
| **Docs** | `docs/<description>` | Documentation only | `docs/api-endpoints` |

### Creating a Feature Branch

```bash
# Always start from latest main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/epic-2-poisson-model

# Verify you're on the right branch
git branch --show-current
```

---

## 💬 Commit Message Convention

We use **Conventional Commits** for clear, searchable history.

### Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **refactor**: Code refactoring (no behavior change)
- **test**: Adding/updating tests
- **chore**: Tooling, dependencies, config
- **perf**: Performance improvement
- **style**: Code style/formatting (not CSS)
- **ci**: CI/CD configuration

### Scopes

- `data` - Data ingestion module
- `models` - Statistical models
- `simulation` - Monte Carlo engine
- `llm` - LLM interpretation
- `api` - FastAPI services
- `ui` - Streamlit dashboard
- `utils` - Utilities
- `tests` - Test files
- `ci` - CI/CD configuration
- `deps` - Dependencies

### Examples

```bash
# Feature
git commit -m "feat(models): implement Poisson baseline model"

# Bug fix
git commit -m "fix(data): handle missing xG values in validation schema"

# With body
git commit -m "feat(simulation): add Monte Carlo rival analysis

- Simulate 10,000 seasons
- Track rival performances
- Calculate probability distributions
- Add visualization helpers

Closes #15"

# Multiple changes
git commit -m "test(models): add Dixon-Coles edge case tests"
git commit -m "docs(api): document FastAPI prediction endpoints"
git commit -m "chore(deps): upgrade pandas to 2.3.4"
```

### Breaking Changes

```bash
git commit -m "feat(api)!: change prediction endpoint response schema

BREAKING CHANGE: prediction endpoint now returns Pydantic model
instead of dict. Update API clients accordingly."
```

---

## 🔒 Pre-commit Hooks

### Initial Setup

```bash
# Install pre-commit hooks (one-time)
uv run pre-commit install

# Verify installation
uv run pre-commit --version
```

### What Runs on Every Commit?

1. **Ruff Linting** - Code quality checks
2. **Ruff Formatting** - Auto-format code
3. **MyPy** - Type checking
4. **Bandit** - Security vulnerability scan
5. **File Quality** - Trailing whitespace, line endings, YAML/JSON syntax

### Manual Execution

```bash
# Run on all files (useful after updating config)
uv run pre-commit run --all-files

# Run specific hook
uv run pre-commit run ruff --all-files
uv run pre-commit run mypy --all-files

# Update hook versions
uv run pre-commit autoupdate
```

### Bypassing Hooks (Emergency Only)

```bash
# Skip pre-commit hooks (NOT recommended)
git commit -m "fix: emergency hotfix" --no-verify

# Only use in emergencies:
# - Production is down
# - Critical security patch
# - Fixing a broken deployment
```

---

## 🔄 Pull Request Workflow

### 1. Push Feature Branch

```bash
# Ensure all commits are clean
git status

# Push to GitHub
git push origin feature/epic-1-data-ingestion
```

### 2. Create Pull Request

**Option A: GitHub CLI (Recommended)**

```bash
gh pr create --title "feat(data): Fixtures data ingestion pipeline" \
             --body "Implements user story #8 for EPIC #1

## Changes
- Add PremierLeague.com scraper
- Implement Pydantic validation schemas
- Add unit tests with 95% coverage

## Testing
All tests passing, coverage increased to 78%

Closes #8" \
             --assignee @me
```

**Option B: GitHub Web UI**

1. Go to `https://github.com/LinoGoncalves/GoalCast/pulls`
2. Click "New Pull Request"
3. Select `feature/epic-1-data-ingestion` → `main`
4. Fill out PR template
5. Assign to yourself
6. Link to issue (#8)

### 3. Automated CI Checks

GitHub Actions will run:

- ✅ Ruff linting
- ✅ Ruff formatting check
- ✅ MyPy type checking
- ✅ Bandit security scan
- ✅ Pytest (all tests)
- ✅ Coverage report
- ✅ Build check

**View CI results:**
```bash
gh pr checks
```

### 4. Code Review

**AI-generated code → Human reviews:**
- Review code quality and correctness
- Check test coverage
- Verify edge cases handled
- Ensure documentation is clear
- Approve or request changes

**Human-generated code → AI/Bot reviews:**
- GitHub Actions CI provides automated feedback
- Optional: Enable GitHub Copilot PR reviews
- Optional: Enable Codecov bot for coverage comments

### 5. Merge to Main

```bash
# Option A: Merge via GitHub CLI
gh pr merge --squash --delete-branch

# Option B: Merge via GitHub Web UI
# Click "Squash and merge" button
# Delete branch after merge
```

### Merge Strategies

**Recommended: Squash and Merge**
- Keeps main history clean
- One commit per PR
- Easy to revert if needed

**Alternatives:**
- **Merge Commit**: Preserves full history (can get messy)
- **Rebase**: Linear history but rewrites commits (avoid for solo dev)

---

## 🚀 GitHub Actions CI/CD

### Workflow Overview

**Trigger:** Push to `main` or PR to `main`

**Jobs:**

1. **Quality Checks** (15 min timeout)
   - Ruff linting
   - Ruff formatting
   - MyPy type checking
   - Bandit security scan
   - Pytest with coverage
   - Codecov upload

2. **Build Check** (5 min timeout)
   - Package build
   - Distribution check

3. **Semgrep Security** (PRs only)
   - Advanced security scanning

### Viewing CI Results

```bash
# View PR checks
gh pr checks

# View workflow runs
gh run list

# View specific run
gh run view <run-id>

# Watch live run
gh run watch
```

### Debugging Failed CI

```bash
# Download CI logs
gh run view <run-id> --log

# Re-run failed jobs
gh run rerun <run-id> --failed
```

---

## 🛠️ Development Workflow Examples

### Example 1: AI Implements Feature (EPIC #1)

```bash
# 1. Human: Create user story issue
gh issue create --title "Ingest fixtures data from PremierLeague.com" \
                --body "As a data scientist, I need..." \
                --label "user-story" \
                --project "GoalCast"

# 2. AI: Create feature branch
git checkout -b feature/epic-1-fixtures-ingestion

# 3. AI: Implement code
# (creates src/goalcast/data/ingest.py, tests, etc.)

# 4. AI: Commit changes
git add src/goalcast/data/ingest.py tests/test_data_ingest.py
git commit -m "feat(data): implement PremierLeague.com fixtures scraper

- Add BeautifulSoup scraper for fixtures
- Implement Pydantic FixtureSchema validation
- Add unit tests with 95% coverage
- Handle missing data gracefully

Closes #8"

# 5. Pre-commit hooks run automatically ✅

# 6. AI: Push and create PR
git push origin feature/epic-1-fixtures-ingestion
gh pr create --title "feat(data): Fixtures ingestion pipeline" \
             --body "Implements #8"

# 7. GitHub Actions CI runs ✅

# 8. Human: Review PR in GitHub UI
#    - Check code quality
#    - Verify tests
#    - Approve PR

# 9. Human: Merge PR
gh pr merge --squash --delete-branch

# 10. Local cleanup
git checkout main
git pull origin main
git branch -d feature/epic-1-fixtures-ingestion
```

### Example 2: Human Implements Feature

```bash
# 1. Create feature branch
git checkout -b enhancement/add-expected-assists

# 2. Write code
# (edit src/goalcast/data/schemas.py)

# 3. Commit
git add src/goalcast/data/schemas.py
git commit -m "feat(data): add expected assists (xA) to player schema"

# 4. Pre-commit runs ✅ (if any issues, fix and commit again)

# 5. Push
git push origin enhancement/add-expected-assists

# 6. Create PR
gh pr create --title "feat(data): Add xA to player schema"

# 7. GitHub Actions CI runs ✅

# 8. Review (GitHub Copilot or self-review)

# 9. Merge
gh pr merge --squash --delete-branch
```

### Example 3: Hotfix

```bash
# 1. Critical bug found in production
git checkout main
git pull origin main

# 2. Create bugfix branch
git checkout -b bugfix/999-xg-division-by-zero

# 3. Fix bug
# (edit src/goalcast/models/xg.py)

# 4. Commit
git commit -m "fix(models): handle zero shots in xG calculation

Fixes #999"

# 5. Push
git push origin bugfix/999-xg-division-by-zero

# 6. Create PR (expedited review)
gh pr create --title "fix(models): Handle zero shots in xG" \
             --label "priority:high"

# 7. Fast review and merge
gh pr merge --squash --delete-branch
```

---

## 📊 Code Quality Standards

### Required Before Merge

- ✅ Ruff linting: 0 errors
- ✅ Ruff formatting: passes
- ✅ MyPy: 0 type errors
- ✅ Bandit: 0 high/critical security issues
- ✅ Pytest: All tests passing
- ✅ Coverage: ≥80% (target)
- ✅ PR approved by reviewer

### Local Quality Checks

```bash
# Full quality check suite (run before pushing)
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
uv run mypy src/goalcast
uv run bandit -c pyproject.toml -r src/goalcast
uv run pytest --cov=goalcast --cov-report=term-missing

# Auto-fix formatting
uv run ruff format src/ tests/

# Auto-fix linting (safe fixes only)
uv run ruff check --fix src/ tests/
```

---

## 🎯 Best Practices

### Do's ✅

- ✅ Create feature branch for every change
- ✅ Use semantic commit messages
- ✅ Write tests for new features
- ✅ Keep PRs small and focused
- ✅ Link PRs to issues
- ✅ Review your own code before requesting review
- ✅ Run pre-commit hooks before pushing
- ✅ Update documentation when needed
- ✅ Delete merged branches

### Don'ts ❌

- ❌ Commit directly to `main` (except docs/typos)
- ❌ Push without running tests
- ❌ Skip pre-commit hooks (except emergencies)
- ❌ Create giant PRs (>500 lines)
- ❌ Merge PRs with failing CI
- ❌ Leave stale branches
- ❌ Use non-descriptive commit messages ("fix stuff")
- ❌ Commit sensitive data (API keys, passwords)

---

## 🆘 Troubleshooting

### Pre-commit Hook Failures

**Problem:** Ruff formatting fails

```bash
# Solution: Auto-format
uv run ruff format src/ tests/
git add .
git commit -m "..."
```

**Problem:** MyPy type errors

```bash
# Solution: Fix type hints
# Add missing type annotations or use # type: ignore as last resort
```

**Problem:** Bandit security warnings

```bash
# Solution: Review and fix security issues
# Or add # nosec comment with justification
```

### CI Failures

**Problem:** Tests fail on GitHub but pass locally

```bash
# Solution: Check Python version mismatch
python --version  # Should be 3.13.x

# Or check missing dependencies
uv sync --all-extras --dev
```

**Problem:** Coverage drops below threshold

```bash
# Solution: Add more tests
uv run pytest --cov=goalcast --cov-report=term-missing
# Identify uncovered lines and add tests
```

### Git Issues

**Problem:** Merge conflict

```bash
# Solution: Rebase on main
git checkout feature/epic-1-...
git fetch origin
git rebase origin/main

# Resolve conflicts in editor
git add .
git rebase --continue
git push --force-with-lease
```

**Problem:** Pushed sensitive data

```bash
# Solution: Remove from history (DANGEROUS)
# Contact GitHub support or use git-filter-repo
# NEVER commit API keys/passwords
```

---

## 📚 Additional Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub CLI Documentation](https://cli.github.com/)
- [Semantic Versioning](https://semver.org/)

---

## 🎓 Summary

**Solo Development with AI Workflow:**

1. **Feature Branch** per Epic/User Story
2. **Pre-commit Hooks** enforce quality locally
3. **Pull Requests** for all code changes to `main`
4. **GitHub Actions CI** enforces quality remotely
5. **Human Reviews AI** (or vice versa) before merge
6. **Squash and Merge** keeps history clean
7. **Delete Branches** after merge

**Key Commands:**

```bash
uv run pre-commit install              # One-time setup
git checkout -b feature/epic-N-...     # Start work
git commit -m "feat(scope): ..."       # Commit
git push origin feature/epic-N-...     # Push
gh pr create                           # Create PR
gh pr merge --squash --delete-branch   # Merge
```

**Automation:**
- Pre-commit hooks → Local quality gate
- GitHub Actions CI → Remote quality gate
- Codecov → Coverage tracking
- Semantic commits → Clear history
