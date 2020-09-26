from db.run_sql import run_sql
from models.team import Team

def save(team):
    sql = "INSERT INTO teams (name, coach, wins, losses) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.name, team.coach, team.wins, team.losses]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id