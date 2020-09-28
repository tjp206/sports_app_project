from db.run_sql import run_sql
from models.player import Player
from models.team import Team
import repositories.team_repo as team_repo

def save(player):
    sql = "INSERT INTO players (name, position, rating, team_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [player.name, player.position, player.rating, player.team.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)
    # print(results)
    for row in results:
        team = team_repo.select(row["team_id"])
        print(team)
        player = Player(row['name'], row['position'], row['rating'], team, row['id'])
        players.append(player)
        # print(players)
    return players

def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    team = team_repo.select(result["team_id"])
    player = Player(result["name"], result["position"], result["rating"], team, result["id"])
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET (name, position, rating, team_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.position, player.rating, player.id, player.team.id]
    run_sql(sql, values)