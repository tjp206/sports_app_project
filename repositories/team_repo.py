from db.run_sql import run_sql
from models.team import Team
from models.player import Player
import repositories.player_repo as player_repo


def save(team):
    sql = "INSERT INTO teams (name, coach, wins, losses) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.name, team.coach, team.wins, team.losses]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        # player = player_repo.select(row["player_id"])
        # print(player)
        team = Team(row['name'], row['coach'],row['wins'], row['losses'], row['id'])
        teams.append(team)
        print(teams)
    return teams

def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    # player = player_repo.select(result["team_id"])
    team = Team(result["name"], result['coach'], result['wins'], result['losses'], result["id"])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, coach, wins, losses) = (%s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.coach, team.wins, team.losses]
    run_sql(sql, values)
