import os, subprocess, datetime as dt, pathlib, json

REPO_DIR = pathlib.Path("/tmp/habitcraft-completions")
REMOTE = "git@github.com:YOURUSER/habitcraft-completions.git"

def ensure_repo():
    if not REPO_DIR.exists():
        subprocess.run(["git","clone",REMOTE,str(REPO_DIR)], check=True)

def log_completion(habit_name: str, note: str = ""):
    ensure_repo()
    day = dt.date.today().isoformat()
    data_file = REPO_DIR / f"logs/{day}.jsonl"
    data_file.parent.mkdir(parents=True, exist_ok=True)
    with open(data_file, "a") as f:
        f.write(json.dumps({"habit": habit_name, "note": note}) + "\n")
    subprocess.run(["git","-C",str(REPO_DIR),"add","-A"], check=True)
    subprocess.run(["git","-C",str(REPO_DIR),"commit","-m",f"habit: {habit_name} on {day}"], check=True)
    subprocess.run(["git","-C",str(REPO_DIR),"push"], check=True)