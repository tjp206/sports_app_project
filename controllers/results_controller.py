from flask import Blueprint, Flask, render_template, redirect, request
from models.result import Result
import repositories.result_repo as result_repo

results_blueprint = Blueprint("results", __name__)