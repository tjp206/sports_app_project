from flask import Blueprint, Flask, render_template, redirect, request
from models.result import Result
import repositories.result_repo as result_repo

results_blueprint = Blueprint("results", __name__)

@results_blueprint.route("/results")
def results():
    print('results')
    return render_template("results/index.html", results=results)