from flask import Blueprint, Flask, render_template, redirect, request
from models import Team
import repositories.games_repo as games_repo
import repositories.results_repo as results_repo
import repositories.teams_repo as teams_repo

teams_blueprint = Blueprint("teams", __name__)