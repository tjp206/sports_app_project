from db.run_sql import run_sql
from models.game import Game
from models.team import Team
import repositories.team_repo as team_repo

def save(game):
    sql = "INSERT INTO games (name, home_team_id, away_team_id) VALUES (%s, %s, %s) RETURNING id"
    values = [game.name, game.home_team.id, game.away_team.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        home_team = team_repo.select(row['home_team_id'])
        away_team = team_repo.select(row['away_team_id'])
        game = Game(row['name'], home_team, away_team, row['id'])
        games.append(game)
    return games

def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    home_team = team_repo.select(result['home_team_id'])
    away_team = team_repo.select(result['away_team_id'])
    game = Game(result["name"], home_team, away_team, result["id"])
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
    values = [game.name, game.home_team.id, game.away_team.id, game.id]
    run_sql(sql, values)