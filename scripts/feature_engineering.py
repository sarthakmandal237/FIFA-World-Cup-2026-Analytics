# ==========================================================
# FIFA World Cup 2026 Analytics Dashboard
# Feature Engineering Script
# Author: Sarthak Mandal
# ==========================================================

# ----------------------------------------------------------
# Import Libraries
# ----------------------------------------------------------

import pandas as pd
import numpy as np

print("=" * 60)
print("FIFA WORLD CUP 2026 FEATURE ENGINEERING")
print("=" * 60)

# ----------------------------------------------------------
# Load Cleaned Datasets
# ----------------------------------------------------------

matches = pd.read_excel("../data/cleaned/matches_cleaned.xlsx")
teams = pd.read_csv("../data/cleaned/teams_cleaned.csv")
match_stats = pd.read_csv("../data/cleaned/match_stats_cleaned.csv")

print("\nDatasets Loaded Successfully!")

# ----------------------------------------------------------
# Create Total Goals
# ----------------------------------------------------------

matches["total_goals"] = (
    matches["home_goals"].fillna(0)
    + matches["away_goals"].fillna(0)
)

# ----------------------------------------------------------
# Create Goal Difference
# ----------------------------------------------------------

matches["goal_difference"] = (
    matches["home_goals"].fillna(0)
    - matches["away_goals"].fillna(0)
).abs()

# ----------------------------------------------------------
# Create Match Result
# ----------------------------------------------------------

def match_result(row):

    if pd.isna(row["home_goals"]) or pd.isna(row["away_goals"]):
        return "Not Played"

    elif row["home_goals"] > row["away_goals"]:
        return "Home Win"

    elif row["away_goals"] > row["home_goals"]:
        return "Away Win"

    else:
        return "Draw"


matches["match_result"] = matches.apply(match_result, axis=1)

# ----------------------------------------------------------
# Create Winner Column
# ----------------------------------------------------------

def winner(row):

    if row["match_result"] == "Home Win":
        return row["home_team"]

    elif row["match_result"] == "Away Win":
        return row["away_team"]

    elif row["match_result"] == "Draw":
        return "Draw"

    else:
        return "Not Played"


matches["winner"] = matches.apply(winner, axis=1)

# ----------------------------------------------------------
# Merge Match Statistics
# ----------------------------------------------------------

matches = matches.merge(
    match_stats,
    on="match_id",
    how="left"
)

print("\nMatch statistics merged successfully!")

# ----------------------------------------------------------
# Total Shots
# ----------------------------------------------------------

matches["total_shots"] = (
    matches["home_shots"].fillna(0)
    + matches["away_shots"].fillna(0)
)

# ----------------------------------------------------------
# Total Shots On Target
# ----------------------------------------------------------

matches["total_shots_on_target"] = (
    matches["home_shots_on_target"].fillna(0)
    + matches["away_shots_on_target"].fillna(0)
)

# ----------------------------------------------------------
# Total Fouls
# ----------------------------------------------------------

matches["total_fouls"] = (
    matches["home_fouls"].fillna(0)
    + matches["away_fouls"].fillna(0)
)

# ----------------------------------------------------------
# Total Corners
# ----------------------------------------------------------

matches["total_corners"] = (
    matches["home_corners"].fillna(0)
    + matches["away_corners"].fillna(0)
)

# ----------------------------------------------------------
# Average Possession
# ----------------------------------------------------------

matches["average_possession"] = (
    matches["home_possession"].fillna(0)
    + matches["away_possession"].fillna(0)
) / 2

# ----------------------------------------------------------
# Goal Efficiency
# Goals per Shot
# ----------------------------------------------------------

matches["goal_efficiency"] = np.where(
    matches["total_shots"] > 0,
    matches["total_goals"] / matches["total_shots"],
    0
)

matches["date"] = pd.to_datetime(
    matches["date"],
    dayfirst=True
).dt.strftime("%Y-%m-%d")

# ----------------------------------------------------------
# Display New Dataset
# ----------------------------------------------------------

print("\n")
print("=" * 60)
print("FEATURED DATASET PREVIEW")
print("=" * 60)

print(matches.head())

print("\n")
print("=" * 60)
print("NEW FEATURES CREATED")
print("=" * 60)

print("""
✓ total_goals
✓ goal_difference
✓ match_result
✓ winner
✓ total_shots
✓ total_shots_on_target
✓ total_fouls
✓ total_corners
✓ average_possession
✓ goal_efficiency
""")

# ----------------------------------------------------------
# Save Featured Dataset
# ----------------------------------------------------------
matches.to_excel(
    "../data/cleaned/matches_featured.xlsx",
    index=False
)

matches.to_csv(
    "../data/cleaned/matches_featured.csv",
    index=False
)
# matches.to_excel(
#     "../data/cleaned/matches_featured.xlsx",
#     index=False
# )

print("=" * 60)
print("FEATURE ENGINEERING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFile Saved Successfully!")

print("\nLocation:")
print("../data/cleaned/matches_featured.xlsx")

print("\nTotal Records :", len(matches))
print("Total Columns :", len(matches.columns))

print("\nProject Ready for Exploratory Data Analysis (EDA)")