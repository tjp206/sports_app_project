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

def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    game = Game(result["name"], result["id"])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET name = %s WHERE id = %s"
    values = [game.name, game.id]
    run_sql(sql, values)