-- habit
id TEXT PRIMARY KEY
name TEXT NOT NULL
created_at DATETIME NOT NULL
cadence TEXT NOT NULL           -- 'daily','weekly','n-of-m'
target_per_week INTEGER DEFAULT 7
is_active BOOLEAN DEFAULT 1

-- completion
id TEXT PRIMARY KEY
habit_id TEXT NOT NULL REFERENCES habit(id)
date DATE NOT NULL
source TEXT NOT NULL            -- 'cli','web','discord','github'
note TEXT

-- mood
id TEXT PRIMARY KEY
date DATE NOT NULL
rating INTEGER NOT NULL         -- 1..5
tags TEXT                       -- csv: 'anxious,focused'
journal TEXT

-- user_profile
id TEXT PRIMARY KEY
timezone TEXT DEFAULT 'America/Chicago'
personality_json TEXT           -- store Big5/MBTI/Enneagram SURVEY SCORES, not labels only
nudges_enabled BOOLEAN DEFAULT 1
