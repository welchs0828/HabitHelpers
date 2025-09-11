import datetime as dt
from collections import defaultdict
from uuid import uuid4

class Habit:
    def __init__(self, name, cadence="daily", target_per_week=7):
        self.id = str(uuid4())
        self.name = name
        self.cadence = cadence
        self.target_per_week = target_per_week

class HabitRepo:
    def __init__(self):
        self.habits = {}
        self.completions = defaultdict(list)

    @classmethod
    def default(cls):
        return cls()

    def create_habit(self, name, cadence, target_per_week):
        h = Habit(name, cadence, target_per_week)
        self.habits[h.id] = h
        return h.id

    def get_by_name(self, name):
        return next((h for h in self.habits.values() if h.name == name), None)

    def add_completion(self, habit_id, date=None, source="cli", note=""):
        date = date or dt.date.today()
        self.completions[habit_id].append(date)
        return {"habit_id": habit_id, "date": date, "source": source, "note": note}

    def get_completion_dates(self, habit_id, start, end):
        return [d for d in self.completions[habit_id] if start <= d <= end]

    def list_habits(self, active=True):
        return list(self.habits.values())