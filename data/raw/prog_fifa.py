import requests
import pandas as pd

url = "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/scoreboard"
resp = requests.get(url, params={"dates": "20260611-20260719", "limit": 200})
data = resp.json()

rows = []
for event in data["events"]:
    comp = event["competitions"][0]
    home, away = comp["competitors"][0], comp["competitors"][1]
    if home["homeAway"] != "home":
        home, away = away, home

    def stat(team, name):
        for s in team["statistics"]:
            if s["name"] == name:
                return s["displayValue"]
        return None

    rows.append({
        "match_id": event["id"],
        "date": event["date"][:10],
        "home_team": home["team"]["displayName"],
        "away_team": away["team"]["displayName"],
        "home_score": home.get("score"),
        "away_score": away.get("score"),
        "attendance": comp.get("attendance"),
        "venue": comp["venue"]["fullName"],
        "home_possession": stat(home, "possessionPct"),
        "away_possession": stat(away, "possessionPct"),
        "home_shots": stat(home, "totalShots"),
        "away_shots": stat(away, "totalShots"),
        "home_shots_on_target": stat(home, "shotsOnTarget"),
        "away_shots_on_target": stat(away, "shotsOnTarget"),
        "home_fouls": stat(home, "foulsCommitted"),
        "away_fouls": stat(away, "foulsCommitted"),
        "home_corners": stat(home, "wonCorners"),
        "away_corners": stat(away, "wonCorners"),
        "home_assists": stat(home, "goalAssists"),
        "away_assists": stat(away, "goalAssists"),
    })

df = pd.DataFrame(rows)
df.to_csv("wc2026_espn_match_stats.csv", index=False)
print(df.shape)