from db.run_sql import run_sql
from models.game import Game

def save(game):
    sql = "INSERT INTO games (name) VALUES (%s) RETURNING id"
    values = [game.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        game = Game(row['name'], row['id'])
        games.append(game)
        print(games)
    return games