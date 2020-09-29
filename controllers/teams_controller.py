from flask import Blueprint, Flask, render_template, redirect, request
from models.team import Team
import repositories.team_repo as team_repo

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repo.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("/teams/new.html")

@teams_blueprint.route("/teams/<id>/edit")
def edit_teams(id):
    team = team_repo.select(id)
    return render_template("/teams/edit.html", team=team)

@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["name"]
    coach = request.form["coach"]
    wins = request.form["wins"]
    losses = request.form["losses"]
    new_team = Team(name, coach, wins, losses)
    team_repo.save(new_team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["name"]
    coach = request.form["coach"]
    wins = request.form["wins"]
    losses = request.form["losses"]
    team = Team(name, coach, wins, losses, id)
    team_repo.update(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repo.delete(id)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repo.select(id)
    return render_template("teams/show.html", team=team)



