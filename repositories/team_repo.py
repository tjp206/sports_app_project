from db.run_sql import run_sql
from models.team import Team
from models.game import Game

def save(team):
    sql = "INSERT INTO teams (name, coach, wins, losses) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.name, team.coach, team.wins, team.losses]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id


def outcome(team):
    games = []

    sql = "SELECT games.* FROM games INNER JOIN results ON results.game_id = games.id WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        game = Game(row['name'], row['id'])
        games.append(game)
    return games
