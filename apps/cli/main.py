import datetime as dt
import typer
from packages.core.streaks import compute_today_progress
from packages.storage.repo import HabitRepo

app = typer.Typer()
repo = HabitRepo.default()

@app.command()
def add(name: str, cadence: str = "daily", target_per_week: int = 7):
    hid = repo.create_habit(name, cadence, target_per_week)
    typer.echo(f"Created habit {name} ({hid})")

@app.command()
def done(name: str, note: str = "", source: str = "cli"):
    habit = repo.get_by_name(name)
    repo.add_completion(habit.id, dt.date.today(), source, note)
    typer.echo(f"Logged completion for {name} today.")

@app.command()
def list(active: bool = True):
    for h in repo.list_habits(active=active):
        typer.echo(f"- {h.name} (cadence={h.cadence})")

@app.command()
def progress(week: bool = True):
    out = compute_today_progress(repo, week=week)
    typer.echo(out.as_text())

if __name__ == "__main__":
    app()