import requests
import pandas as pd
from datetime import date, timedelta

# Calculate Game Score Function
def calc_gamescore(df):
    def innings_to_outs(inn):
        if pd.isna(inn):
            return 0
        # innings is given as string "6.2" sometimes → float
        inn = float(inn)
        whole_innings = int(inn)
        decimal = round((inn - whole_innings) * 10)
        return whole_innings * 3 + decimal

    outs = df["Innings"].apply(innings_to_outs)
    inning_bonus = (outs // 3 - 4).clip(lower=0) * 2

    df["GameScore"] = (
        50
        + outs
        + inning_bonus
        + df["SO"]
        - 2 * df["H"]
        - 4 * df["ER"]
        - 2 * df["UER"]
        - df["BB"]
    )
    return df

# --- Pull daily pitcher statlines ---
def get_daily_pitcher_stats(game_date=None):
    if game_date is None:
        game_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    # Espn API from yesterday's games
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={game_date}"
    schedule = requests.get(url).json()

    all_pitchers = []

    # API gives gamePk data - Use to access boxscore's for each game from yesterday
    for date_block in schedule.get("dates", []):
        for game in date_block.get("games", []):
            game_pk = game["gamePk"]
            box_url = f"https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore"
            box = requests.get(box_url).json()

            # Access all pitcher's boxscores, return relevant info. Adjust if desire different pulled data
            for side in ["home", "away"]:
                players = box["teams"][side]["players"]
                for _, pdata in players.items():
                    if "pitching" in pdata["stats"]:
                        s = pdata["stats"]["pitching"]
                        all_pitchers.append({
                            "Pitcher": pdata["person"]["fullName"],
                            "Team": box["teams"][side]["team"]["name"],
                            "Innings": s.get("inningsPitched", "0.0"),
                            "SO": s.get("strikeOuts", 0),
                            "H": s.get("hits", 0),
                            "ER": s.get("earnedRuns", 0),
                            "UER": s.get("unearnedRuns", 0),
                            "BB": s.get("baseOnBalls", 0),
                            "GamePk": game_pk,
                            "Date": game_date
                        })

    df = pd.DataFrame(all_pitchers)
    return df

# --- Main pipeline ---
def daily_gamescore_rankings():
    pitchers = get_daily_pitcher_stats()
    pitchers = calc_gamescore(pitchers)
    pitchers = pitchers.sort_values("GameScore", ascending=False).reset_index(drop=True)
    return pitchers

# Gather Yesterday's Top 3 Pitchers
if __name__ == "__main__":
    df = daily_gamescore_rankings()
    print(df[["Pitcher", "Team", "Innings", "SO", "H", "ER", "UER", "BB", "GameScore"]].head(3))