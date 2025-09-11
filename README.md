![WIP](https://img.shields.io/badge/status-Work_in_Progress-yellow?style=for-the-badge&logoColor=white)


<p align="center">
  <img src="https://github.com/user-attachments/assets/2ed42ec7-0800-46f6-8b62-c97d36a7c0ad" width="450" height="250" >
</p>


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

<p align="center">
  <img src="https://github.com/user-attachments/assets/58c935fa-6965-4cda-a685-bbbce96a43bb" width="500" height="250" >
</p>

---

## Quickstart

bash
### Clone & install
git clone https://github.com/ginesthoii/HabitHelpers.git <br>
cd HabitHelpers  <br>
uv venv && uv pip install -e .

### Set secrets
cp .env.example .env   # add GH_TOKEN, DISCORD_TOKEN if using integrations

### Run database migrations
alembic upgrade head

### Try the CLI
python apps/cli/main.py add "Read 10 pages" <br>
python apps/cli/main.py done "Read 10 pages" <br>
python apps/cli/main.py progress --week <br>

### Start the web API
uvicorn apps.web.api:app --reload



---




<p align="center">
  <img src="https://github.com/user-attachments/assets/1f526beb-f795-4aec-85f5-a9fa2ea8794d" width="400" height="250" >
</p>
