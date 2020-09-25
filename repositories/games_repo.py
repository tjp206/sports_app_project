from db.run_sql import run_sql
from models.game import Game
from models.result import Result
from models.team import Team
import repositories.results_repo as results_repo
import repositories.teams_repo as teams_repo

def save(game):
    sql = "INSERT INTO games (name) VALUES (%s) RETURNING id"
    values = [game.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id