
## Features

- **CLI Tracker** — Add, complete, and view habits directly from the terminal with streak counters.
- **GitHub Bridge** — Log completions to your contribution graph via commits or daily issues.
- **Gamified Web App** — FastAPI + React/Tailwind dashboard with XP, streaks, and RushCoins rewards.
- **Mood Analytics** — Correlate mood with habit data, generate insights, and visualize progress.
- **Discord/Slack Bots** — Daily reminders, `/habit done` commands, and accountability partners.
- **Advanced ML Coach** *(planned)* — Personalized nudges and habit recommendations based on your data.

##  Tech Stack

- **Backend** — Python 3.12, FastAPI, SQLAlchemy, Alembic, Pydantic  
- **Frontend** — React, Vite, Tailwind CSS  
- **CLI** — Typer (Click-based), SQLite storage  
- **Bots** — Discord.py or Slack Bolt  
- **Testing & Security** — pytest, ruff, mypy, bandit, pip-audit, Trivy, Syft (SBOM)  

---

## Quickstart

```bash
# Clone & install
git clone https://github.com/ginesthoii/HabitHelpers.git
cd HabitHelpers
uv venv && uv pip install -e .

# Set secrets
cp .env.example .env   # add GH_TOKEN, DISCORD_TOKEN if using integrations

# Run database migrations
alembic upgrade head

# Try the CLI
python apps/cli/main.py add "Read 10 pages"
python apps/cli/main.py done "Read 10 pages"
python apps/cli/main.py progress --week

# Start the web API
uvicorn apps.web.api:app --reload