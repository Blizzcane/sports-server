from flask import Flask, jsonify
from flask_cors import CORS

from nba_api.live.nba.endpoints import scoreboard, boxscore

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_games():
    board = scoreboard.ScoreBoard()
    return scoreboard.ScoreBoard().get_json()

    # games = board.games.get_dict()
    # games_list = []
    # for game in games:
    #     box = boxscore.BoxScore(game['gameId'])   
    #     current_score = "{homeScore} - {awayScore}".format(
    #         homeScore=box.get_dict()['game']['homeTeam']['score'],
    #         awayScore=box.get_dict()['game']['awayTeam']['score'])
    #     game_dict = {
    #         'gameId': game['gameId'],
    #         'awayTeam': game['awayTeam']['teamName'],
    #         'homeTeam': game['homeTeam']['teamName'],
    #         'currentScore': current_score,
    #         'gameStatusText': game['gameStatusText']
    #     }
    #     games_list.append(game_dict)
    # return jsonify(games_list)
@app.route("/games")
def get_games_again():
    board = scoreboard.ScoreBoard()
    return scoreboard.ScoreBoard().get_json()
 


if __name__ == "__main__": 
    app.run()
