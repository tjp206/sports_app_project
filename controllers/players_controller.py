from flask import Flask, Blueprint, render_template, redirect, request
from models.player import Player
import repositories.player_repo as player_repo
from models.team import Team
import repositories.team_repo as team_repo

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repo.select_all()
    return render_template("/players/index.html", players=players)

@players_blueprint.route("/players/new")
def new_player():
    teams = team_repo.select_all()
    return render_template("/players/new.html", teams=teams)

@players_blueprint.route("/players", methods=["POST"])
def create_player():
    name = request.form["name"]
    position = request.form["position"]
    rating = request.form["rating"]
    team_id = request.form["team_id"]
    team = team_repo.select(team_id)
    new_player = Player(name, position, rating, team)
    player_repo.save(new_player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repo.select(id)
    return render_template('/players/edit.html', player=player)

@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    name = request.form["name"]
    position = request.form["position"]
    rating = request.form["rating"]
    team_id = request.form["team_id"]
    team = team_repo.select(team_id)
    player = Player(name, position, rating, team, id)
    player_repo.update(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repo.delete(id)
    return redirect("/players")

@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repo.select(id)
    return render_template("/players/show.html", player=player)