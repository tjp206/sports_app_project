from flask import Blueprint, Flask, render_template, redirect, request
from models import Game
import repositories.games_repo as games_repo
import repositories.results_repo as results_repo
import repositories.teams_repo as teams_repo

games_blueprint = Blueprint("games", __name__)

