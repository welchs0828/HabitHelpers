from fastapi import FastAPI
from pydantic import BaseModel
from packages.storage.repo import HabitRepo
from packages.core.gamify import award_xp

app = FastAPI()
repo = HabitRepo.default()

class HabitIn(BaseModel):
    name: str
    cadence: str = "daily"
    target_per_week: int = 7

@app.post("/habits")
def create_habit(h: HabitIn):
    hid = repo.create_habit(h.name, h.cadence, h.target_per_week)
    return {"id": hid}

class CompletionIn(BaseModel):
    habit_id: str
    note: str = ""
    source: str = "web"

@app.post("/completions")
def complete(c: CompletionIn):
    rec = repo.add_completion(c.habit_id, None, c.source, c.note)
    award_xp(repo, c.habit_id, rec.date)
    return {"ok": True}