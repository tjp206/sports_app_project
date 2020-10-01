from flask import Blueprint, Flask, render_template, request, redirect
from models.game import Game
import repositories.game_repo as game_repo
from models.team import Team
import repositories.team_repo as team_repo

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repo.select_all()
    print(games)
    return render_template("games/index.html", games=games)

@games_blueprint.route("/games/new")
def new_game():
    teams = team_repo.select_all()
    return render_template("/games/new.html", teams=teams)

@games_blueprint.route("/games", methods=["POST"])
def create_game():
    name = request.form["name"]
    home_team = team_repo.select(request.form["home_team_id"])
    away_team = team_repo.select(request.form["away_team_id"])
    new_game = Game(name, home_team, away_team)
    game_repo.save(new_game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    teams = team_repo.select_all()
    game = game_repo.select(id)
    return render_template('/games/edit.html', game=game, teams=teams)

@games_blueprint.route("/games/<id>", methods=["POST"])
def update_game(id):
    name = request.form["name"]
    home_team = team_repo.select(request.form["home_team_id"])
    away_team = team_repo.select(request.form["away_team_id"])
    game = Game(name, home_team, away_team, id)
    print("This is where I'm printing", game)
    game_repo.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repo.delete(id)
    return redirect("/games")

@games_blueprint.route("/games/<id>")
def show(id):
    game = game_repo.select(id)
    return render_template("/games/show.html", game=game)

@games_blueprint.route("/games/<id>/simulate")
def get_winner(id):
    game = game_repo.select(id)
    winner = game.winner(game.home_team, game.away_team)
    return render_template("/games/simulate.html", game=game, winner=winner)

# @games_blueprint.route("/games/<id>/book")
# def book_tickets(id):
#     game = game_repo.select(id)
#     return render_template("/games/book.html", game=game)