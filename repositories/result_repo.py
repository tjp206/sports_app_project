from db.run_sql import run_sql
from models.result import Result

def save(result):
    sql = "INSERT INTO results (scores, team_id, game_id) VALUES (%s, %s, %s) RETURNING id"
    values = [result.scores, result.team.id, result.game.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    result.id = id
