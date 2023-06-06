import pdb
from db.run_sql import run_sql
from models.artist import Artist
import repositories.album_repository as album_repository

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
