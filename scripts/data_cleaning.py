# ==========================================================
# FIFA World Cup 2026 Analytics Dashboard
# Data Cleaning Script
# Author: Sarthak Mandal
# ==========================================================

# ------------------------
# Import Libraries
# ------------------------

import pandas as pd
import numpy as np

print("=" * 60)
print("FIFA WORLD CUP 2026 DATA CLEANING")
print("=" * 60)

# ------------------------
# Load Datasets
# ------------------------

matches = pd.read_excel("../data/raw/matchess.xlsx")
teams = pd.read_csv("../data/raw/teams.csv")
match_stats = pd.read_csv("../data/raw/match_stats.csv")

print("\nDatasets Loaded Successfully!")

# ==========================================================
# DATA INSPECTION
# ==========================================================

print("\n" + "=" * 60)
print("MATCHES DATA")
print("=" * 60)
print(matches.head())

print("\n" + "=" * 60)
print("TEAMS DATA")
print("=" * 60)
print(teams.head())

print("\n" + "=" * 60)
print("MATCH STATS DATA")
print("=" * 60)
print(match_stats.head())

# ------------------------
# Dataset Information
# ------------------------

print("\n" + "=" * 60)
print("MATCHES INFO")
print("=" * 60)
matches.info()

print("\n" + "=" * 60)
print("TEAMS INFO")
print("=" * 60)
teams.info()

print("\n" + "=" * 60)
print("MATCH STATS INFO")
print("=" * 60)
match_stats.info()

# ------------------------
# Missing Values
# ------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print("\nMatches")
print(matches.isnull().sum())

print("\nTeams")
print(teams.isnull().sum())

print("\nMatch Stats")
print(match_stats.isnull().sum())

# ------------------------
# Duplicate Records
# ------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print("Matches :", matches.duplicated().sum())
print("Teams :", teams.duplicated().sum())
print("Match Stats :", match_stats.duplicated().sum())

# ==========================================================
# DATA CLEANING
# ==========================================================

print("\n" + "=" * 60)
print("STANDARDIZING COLUMN NAMES")
print("=" * 60)

matches.columns = (
    matches.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

teams.columns = (
    teams.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

match_stats.columns = (
    match_stats.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("Column names standardized successfully.")

# ==========================================================
# REMOVE EXTRA SPACES
# ==========================================================

print("\nRemoving extra spaces...")

# Matches
matches["home_team"] = matches["home_team"].str.strip()
matches["away_team"] = matches["away_team"].str.strip()
matches["stage"] = matches["stage"].str.strip()
matches["stadium"] = matches["stadium"].str.strip()

# Teams
teams["team"] = teams["team"].str.strip()
teams["group"] = teams["group"].str.strip()
teams["confederation"] = teams["confederation"].str.strip()

print("Extra spaces removed.")

# ==========================================================
# STANDARDIZE TEXT
# ==========================================================

print("\nStandardizing text format...")

matches["home_team"] = matches["home_team"].str.title()
matches["away_team"] = matches["away_team"].str.title()

teams["team"] = teams["team"].str.title()
teams["group"] = teams["group"].str.upper()
teams["confederation"] = teams["confederation"].str.upper()

print("Text standardized successfully.")

# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

print("\nRemoving duplicate rows...")

matches.drop_duplicates(inplace=True)
teams.drop_duplicates(inplace=True)
match_stats.drop_duplicates(inplace=True)

print("Duplicate removal completed.")

# ==========================================================
# DATA TYPES
# ==========================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print("\nMatches")
print(matches.dtypes)

print("\nTeams")
print(teams.dtypes)

print("\nMatch Stats")
print(match_stats.dtypes)

# ==========================================================
# SAVE CLEANED DATA
# ==========================================================

matches.to_excel("../data/cleaned/matches_cleaned.xlsx", index=False)

teams.to_csv("../data/cleaned/teams_cleaned.csv", index=False)

match_stats.to_csv("../data/cleaned/match_stats_cleaned.csv", index=False)

print("\n" + "=" * 60)
print("CLEANED DATASETS SAVED SUCCESSFULLY")
print("=" * 60)

print("\nSaved Files:")
print("✔ matches_cleaned.xlsx")
print("✔ teams_cleaned.csv")
print("✔ match_stats_cleaned.csv")

print("\nLocation:")
print("../data/cleaned/")

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)