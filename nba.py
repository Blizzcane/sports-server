from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
from nba_api.live.nba.endpoints import scoreboard, boxscore

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_games():
    board = scoreboard.ScoreBoard()
    return scoreboard.ScoreBoard().get_json()

@app.route("/games")
def get_games_again():
    board = scoreboard.ScoreBoard()
    return scoreboard.ScoreBoard().get_json()
 
@app.route('/boxscore')
def get_boxscore():
    gameId = request.args.get('gameId')
    box = boxscore.BoxScore(gameId)
    return box.get_json()

if __name__ == "__main__": 
    serve(app, host='0.0.0.0', port=5000)
