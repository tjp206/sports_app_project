from flask import Blueprint, Flask, render_template, redirect, request
from models.team import Team
import repositories.team_repo as team_repo

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    print('teams')
    return render_template("teams/index.html", teams=teams)