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

@games_blueprint.route("/games/new")
def new_game():
    return render_template("/games/new.html")

@games_blueprint.route("/games", methods=["POST"])
def create_game():
    name = request.form["name"]
    new_game = Game(name)
    game_repo.save(new_game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    game = game_repo.select(id)
    return render_template('/games/edit.html', game=game)

@games_blueprint.route("/games/<id>", methods=["POST"])
def update_game(id):
    name = request.form["name"]
    game = Game(name, id)
    game_repo.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repo.delete(id)
    return redirect("/games")

# @games_blueprint.route("/games/<id>/book")
# def book_tickets(id):
#     game = game_repo.select(id)
#     return render_template("/games/book.html", game=game)