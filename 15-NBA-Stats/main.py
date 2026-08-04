from nba_api import get_games

print("=" * 45)
print("        🏀 HOOPHUB")
print("=" * 45)

games = get_games()

if not games:
    print("\nNo NBA games scheduled today.")

else:

    for game in games:

        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]

        home_score = game["homeTeam"]["score"]
        away_score = game["awayTeam"]["score"]

        status = game["gameStatusText"]

        print(f"\n{away} vs {home}")
        print(f"Status : {status}")
        print(f"Score  : {away_score} - {home_score}")