# Contributing to Cosmic-IB Dashboard

Thank you for considering a contribution! This document outlines the process for
reporting bugs, suggesting enhancements, and submitting pull requests.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Commit Message Convention](#commit-message-convention)

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/)
Code of Conduct. By participating you agree to abide by its terms.

---

## Reporting Bugs

1. Search [existing issues](../../issues) first to avoid duplicates.
2. Open a new issue using the **Bug Report** template and include:
   - A clear, concise title (e.g. `"Ricci map section crashes when ricci_map_nside16.fits is missing"`)
   - Steps to reproduce the bug
   - Expected vs. actual behaviour
   - Python / OS / Streamlit version (`pip show streamlit`)
   - Relevant error traceback (paste in a code block)

---

## Suggesting Enhancements

1. Open an issue with the **Feature Request** template.
2. Describe the use-case and the value it would add.
3. Indicate whether you are willing to implement it yourself.

Good enhancement ideas include:
- New HEALPix resolutions or datasets
- Additional MI estimators (e.g. MINE, EDGE)
- Export of interactive Plotly figures to HTML
- Unit tests for data-loading functions

---

## Development Setup

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/cosmic-ib-dashboard.git
cd cosmic-ib-dashboard

# 2. Create a feature branch
git checkout -b feature/my-awesome-feature

# 3. Set up the virtual environment
python -m venv .venv
source .venv/bin/activate

# 4. Install dependencies + dev extras
pip install -r requirements.txt
pip install ruff black pytest

# 5. Extract the data archive (requires files.7z in repo root)
bash scripts/extract_data.sh

# 6. Run the app locally to verify everything works
streamlit run app.py
```

---

## Code Style

This project uses:

| Tool | Purpose | Config |
|------|---------|--------|
| [`black`](https://black.readthedocs.io) | Auto-formatting | default (line length 100) |
| [`ruff`](https://docs.astral.sh/ruff/) | Linting | default ruleset |

Before committing, run:

```bash
black app.py
ruff check app.py --fix
```

Additional style rules:
- **Docstrings:** Every function should have a one-line docstring.
- **Type hints:** Use Python type annotations where practical.
- **Constants:** Place module-level constants in `UPPER_SNAKE_CASE` near the top of the file.
- **Comments:** Prefer self-documenting code; comments should explain *why*, not *what*.
- **Imports:** Group as stdlib → third-party → local, separated by blank lines.

---

## Pull Request Process

1. Ensure your branch is up-to-date with `main`:
   ```bash
   git fetch origin
   git rebase origin/main
   ```
2. Make sure the app runs without errors:
   ```bash
   streamlit run app.py
   ```
3. If you added new Python code, add or update docstrings.
4. Open a PR against `main` with:
   - A descriptive title using the [Conventional Commits](#commit-message-convention) style.
   - A summary of what changed and why.
   - Screenshots / GIFs if the change is visual.
5. At least one maintainer review is required before merging.
6. Squash commits if the PR history is noisy.

---

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

| Type | When to use |
|------|------------|
| `feat` | New feature or visualisation |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `chore` | Build process, dependency updates |

**Examples:**

```
feat(scale): add nside=4 resolution support
fix(healpix): handle missing ricci_map gracefully
docs(readme): add Docker deployment section
```
