# Flask Voting Application — Git Versioning Assignment

## Project Description

This project is a small voting application built with Python and Flask.
It lets users vote for candidates by visiting a URL and keeps vote counts in memory.
Users can view the current standings and clear all votes when required.
The project demonstrates feature-based Version 1 and Version 2 releases using a `dev` → `main` Git workflow.

## Prerequisites

- Python 3.x
- Git
- GitHub account
- Flask

## Installation and Setup

### 1. Clone the repository

Replace the URL with your GitHub repository URL:

```bash
git clone https://github.com/YOUR_USERNAME/flask-git-assignment.git
cd flask-git-assignment
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python3 app.py
```

The application runs at:

```text
http://127.0.0.1:5000
```

## API Endpoint Reference

| Endpoint | Method | What it does | Example response |
|---|---|---|---|
| `/` | GET | Displays the welcome message | `Welcome to the App` |
| `/health` | GET | Confirms that the app is running | `App is running` |
| `/vote/<name>` | GET | Records one vote for a candidate | `{"candidate":"Alice","message":"Vote recorded","votes":1}` |
| `/results` | GET | Returns all current vote counts as JSON | `{"Alice":2,"Bob":1}` |
| `/reset` | GET | Clears all stored vote counts | `{"message":"All vote counts have been reset"}` |

### Example voting flow

```text
GET /vote/Alice
GET /vote/Alice
GET /vote/Bob
GET /results
```

Expected `/results` response:

```json
{
  "Alice": 2,
  "Bob": 1
}
```

Reset the data:

```text
GET /reset
```

Then `/results` returns:

```json
{}
```

## Git Workflow

All new development is performed on the `dev` branch. The `main` branch contains stable, completed versions only.

```text
Version 1
dev
 │
 ├── Implement Flask voting endpoints
 │
 └── commit → push dev
        │
        ▼
      main
        │
        └── merge Version 1 → push main

Version 2
dev
 │
 ├── Add /reset
 │
 └── commit → push dev
        │
        ▼
      main
        │
        └── merge Version 2 → push main
```

The evaluator can therefore see that Version 2 was built on top of Version 1 rather than replacing the history.

Useful verification commands:

```bash
git branch -a
git status
git log --oneline --graph --decorate --all
```

## Version History

| Version | Contents |
|---|---|
| Version 1 | Flask app with `/`, `/health`, `/vote/<name>`, and `/results` |
| Version 2 | Added `/reset` to clear all stored vote counts |

## Mandatory Screenshots

The assignment requires these screenshots to be embedded directly inside this README:

1. **Application running in a browser** showing at least one working endpoint.
2. **GitHub repository page** showing both `dev` and `main` branches.
3. **Commit/merge history** showing the Version 1 and Version 2 releases.

Save the real screenshots as:

```text
docs/screenshots/app-running.png
docs/screenshots/github-branches.png
docs/screenshots/github-history.png
```

Then embed them directly in this README:

```markdown
![Application running](docs/screenshots/app-running.png)

![GitHub branches](docs/screenshots/github-branches.png)

![GitHub version history](docs/screenshots/github-history.png)
```

**Important:** These must be real screenshots from your browser and your GitHub repository. The project template cannot generate your personal GitHub screenshots.

## Testing Checklist

Before submission:

- [ ] `/` returns `Welcome to the App`
- [ ] `/health` returns `App is running`
- [ ] `/vote/Alice` records a vote
- [ ] Voting for Alice again increases her count
- [ ] A new candidate starts at 1
- [ ] `/results` returns JSON
- [ ] `/reset` clears all votes
- [ ] `/results` returns `{}` after reset
- [ ] Both `dev` and `main` exist on GitHub
- [ ] Version 1 is merged into `main`
- [ ] Version 2 is developed on `dev` and merged into `main`
- [ ] README contains all three mandatory screenshots

## Assignment Alignment

The implementation follows the assignment's required Flask endpoints, voting application option, `dev`/`main` branching workflow, Version 1 and Version 2 development, and README documentation. The assignment specifies `/` and `/health` on page 3, `/vote/<name>` and `/results` on pages 3–4, `/reset` and the second Git merge on page 5, and the README plus three embedded screenshots on pages 5–6.
