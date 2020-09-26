from db.run_sql import run_sql
from models.result import Result

def save(result):
    sql = "INSERT INTO results (result) VALUES (%s) RETURNING id"
    values = [result.result]
    results = run_sql(sql, values)
    id = results[0]['id']
    result.id = id