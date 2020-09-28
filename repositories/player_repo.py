from db.run_sql import run_sql
from models.player import Player

def save(player):
    sql = "INSERT INTO players (name, position, rating) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.position, player.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['name'], row['position'], row['rating'], row['id'])
        players.append(player)
        print(players)
    return players

def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    game = Player(result["name"], result["id"])
    return Player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET name = %s WHERE id = %s"
    values = [player.name, player.id]
    run_sql(sql, values)