from flask import Blueprint, Flask, render_template, redirect, request
from models.team import Team
import repositories.team_repo as team_repo

teams_blueprint = Blueprint("teams", __name__)