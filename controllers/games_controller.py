from flask import Blueprint, Flask, render_template, request, redirect
from models.game import Game
import repositories.game_repo as game_repo

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repo.select_all()
    return render_template("games/index.html", games=games)