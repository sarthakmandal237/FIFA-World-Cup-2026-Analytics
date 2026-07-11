import pandas as pd

# Load match dataset
matches = pd.read_excel("../data/cleaned/matches_featured.xlsx")

# -----------------------------
# HOME TEAM STATS
# -----------------------------
home = matches[[
    "home_team",
    "home_goals",
    "home_shots",
    "home_shots_on_target",
    "home_corners",
    "home_fouls",
    "home_possession"
]].copy()

home.columns = [
    "team",
    "goals",
    "shots",
    "shots_on_target",
    "corners",
    "fouls",
    "possession"
]

home["wins"] = (matches["winner"] == matches["home_team"]).astype(int)

# -----------------------------
# AWAY TEAM STATS
# -----------------------------
away = matches[[
    "away_team",
    "away_goals",
    "away_shots",
    "away_shots_on_target",
    "away_corners",
    "away_fouls",
    "away_possession"
]].copy()

away.columns = [
    "team",
    "goals",
    "shots",
    "shots_on_target",
    "corners",
    "fouls",
    "possession"
]

away["wins"] = (matches["winner"] == matches["away_team"]).astype(int)

# -----------------------------
# Combine Home + Away
# -----------------------------
team_stats = pd.concat([home, away])

# Remove rows for future matches
team_stats = team_stats.dropna(subset=["team"])

# -----------------------------
# Aggregate
# -----------------------------
team_stats = team_stats.groupby("team").agg({
    "goals":"sum",
    "wins":"sum",
    "shots":"sum",
    "shots_on_target":"sum",
    "corners":"sum",
    "fouls":"sum",
    "possession":"mean"
}).reset_index()

team_stats["possession"] = team_stats["possession"].round(2)

# -----------------------------
# Save
# -----------------------------
team_stats.to_excel(
    "../data/cleaned/team_stats.xlsx",
    index=False
)

print(team_stats.head())
print("\nteam_stats.xlsx created successfully!")