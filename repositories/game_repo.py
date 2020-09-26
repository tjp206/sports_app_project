from db.run_sql import run_sql
from models.game import Game

def save(game):
    sql = "INSERT INTO games (name) VALUES (%s) RETURNING id"
    values = [game.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
