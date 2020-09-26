from flask import Blueprint, Flask, render_template, request, redirect
from models.game import Game
import repositories.game_repo as game_repo

from models.team import Team
import repositories.team_repo as team_repo

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repo.select_all()
    return render_template("games/index.html", games=games)

# @games_blueprint.route("/games/<id>")
# def show_game(id):
#     team_1 = team_repo.select(id)
#     team_2 = team_repo.select(id)
#     return render_template("games/show.html", games=games)