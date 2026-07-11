# ==========================================================
# FIFA World Cup 2026 Analytics Dashboard
# Exploratory Data Analysis (EDA)
# Author: Sarthak Mandal
# ==========================================================

# ----------------------------------------------------------
# Import Libraries
# ----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("FIFA WORLD CUP 2026 - EXPLORATORY DATA ANALYSIS")
print("=" * 70)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

matches = pd.read_excel("../data/cleaned/matches_featured.xlsx")

print("\nDataset Loaded Successfully!")

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

matches.info()

# ----------------------------------------------------------
# Dataset Shape
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print("Rows :", matches.shape[0])
print("Columns :", matches.shape[1])

# ----------------------------------------------------------
# First Five Rows
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("FIRST FIVE ROWS")
print("=" * 70)

print(matches.head())

# ----------------------------------------------------------
# Statistical Summary
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("STATISTICAL SUMMARY")
print("=" * 70)

print(matches.describe())

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(matches.isnull().sum())

# ----------------------------------------------------------
# Duplicate Records
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

print(matches.duplicated().sum())

# ----------------------------------------------------------
# Tournament KPIs
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("TOURNAMENT KPIs")
print("=" * 70)

matches_played = matches[matches["match_result"] != "Not Played"]

total_matches = len(matches)

matches_completed = len(matches_played)

total_goals = matches_played["total_goals"].sum()

average_goals = matches_played["total_goals"].mean()

highest_scoring_match = matches_played["total_goals"].max()

largest_winning_margin = matches_played["goal_difference"].max()

print(f"Total Matches            : {total_matches}")
print(f"Matches Completed        : {matches_completed}")
print(f"Matches Remaining        : {total_matches - matches_completed}")
print(f"Total Goals              : {total_goals}")
print(f"Average Goals Per Match  : {average_goals:.2f}")
print(f"Highest Scoring Match    : {highest_scoring_match}")
print(f"Largest Winning Margin   : {largest_winning_margin}")

# ----------------------------------------------------------
# Match Result Distribution
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("MATCH RESULT DISTRIBUTION")
print("=" * 70)

print(matches["match_result"].value_counts())

# ----------------------------------------------------------
# Stage-wise Matches
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("MATCHES BY STAGE")
print("=" * 70)

print(matches["stage"].value_counts())

# ----------------------------------------------------------
# Highest Scoring Matches
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 HIGHEST SCORING MATCHES")
print("=" * 70)

top_matches = matches_played.sort_values(
    by="total_goals",
    ascending=False
)

print(
    top_matches[
        [
            "home_team",
            "away_team",
            "home_goals",
            "away_goals",
            "total_goals"
        ]
    ].head(10)
)

# ----------------------------------------------------------
# Top 10 Biggest Victories
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 BIGGEST VICTORIES")
print("=" * 70)

largest_wins = matches_played.sort_values(
    by="goal_difference",
    ascending=False
)

print(
    largest_wins[
        [
            "home_team",
            "away_team",
            "goal_difference"
        ]
    ].head(10)
)

# ----------------------------------------------------------
# Average Goals by Stage
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("AVERAGE GOALS BY STAGE")
print("=" * 70)

print(
    matches_played.groupby("stage")["total_goals"]
    .mean()
    .sort_values(ascending=False)
)

# ----------------------------------------------------------
# Average Shots by Stage
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("AVERAGE SHOTS BY STAGE")
print("=" * 70)

print(
    matches_played.groupby("stage")["total_shots"]
    .mean()
    .sort_values(ascending=False)
)

# ----------------------------------------------------------
# Correlation Matrix
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

correlation = matches[
    [
        "total_goals",
        "goal_difference",
        "total_shots",
        "total_shots_on_target",
        "total_fouls",
        "total_corners",
        "average_possession",
        "goal_efficiency"
    ]
].corr()

print(correlation)

# ----------------------------------------------------------
# Top 10 Stadiums by Attendance
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("TOP STADIUMS BY ATTENDANCE")
print("=" * 70)

attendance = (
    matches_played
    .groupby("stadium")["attendance"]
    .sum()
    .sort_values(ascending=False)
)

print(attendance.head(10))

# ----------------------------------------------------------
# Final Summary
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)

print("""
Insights Generated Successfully:

✓ Tournament KPIs
✓ Dataset Statistics
✓ Missing Value Summary
✓ Duplicate Check
✓ Match Result Distribution
✓ Stage Analysis
✓ Highest Scoring Matches
✓ Biggest Victories
✓ Average Goals by Stage
✓ Average Shots by Stage
✓ Stadium Attendance
✓ Correlation Matrix

Dataset is now ready for SQL Analysis.
""")