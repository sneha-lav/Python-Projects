from nba_api.live.nba.endpoints import scoreboard


def get_games():

    games = scoreboard.ScoreBoard()

    return games.games.get_dict()