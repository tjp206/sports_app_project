from flask import Flask, Blueprint, render_template, redirect, request
from models.player import Player
import repositories.player_repo as player_repo

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repo.select_all()
    return render_template("/players/index.html", players=players)

@players_blueprint.route("/players/new")
def new_player():
    return render_template("/players/new.html")

@players_blueprint.route("/players", methods=["POST"])
def create_player():
    name = request.form["name"]
    position = request.form["position"]
    rating = request.form["rating"]
    new_player = Player(name, position, rating)
    player_repo.save(new_player)
    return redirect("/players")
