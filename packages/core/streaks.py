import datetime as dt
from dataclasses import dataclass

@dataclass
class Progress:
    lines: list[str]
    def as_text(self) -> str: return "\n".join(self.lines)

def compute_streak(dates: set[dt.date], today: dt.date) -> int:
    s, cur = 0, today
    while cur in dates:
        s += 1
        cur = cur - dt.timedelta(days=1)
    return s

def compute_today_progress(repo, week: bool = True) -> Progress:
    today = dt.date.today()
    start = today - dt.timedelta(days=6) if week else today
    lines = []
    for h in repo.list_habits():
        dates = set(repo.get_completion_dates(h.id, start, today))
        streak = compute_streak(dates, today)
        done_today = today in dates
        lines.append(f"{'(✓' if done_today else '▫️'} {h.name} — streak {streak}")
    return Progress(lines)