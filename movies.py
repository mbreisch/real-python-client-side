import json
import requests
import sqlite3

TOKEN = "129d3d14-aa10-4202-adfe-40b703481517"
url = requests.get("http://api.myapifilms.com/imdb/inTheaters?token={}&format=json&language=en-us".format(TOKEN))

binary = url.content
output = json.loads(binary)

movies = output['data']['inTheaters']

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            if (meta['title']):
                c.execute("INSERT INTO new_movies VALUES (?,?,?,?,?,?)", (
                meta['title'], meta['year'], meta['votes'], meta['releaseDate'], meta['metascore'], meta['rating']))
    c.execute("SELECT * FROM new_movies ORDER BY title ASC ")

    rows=c.fetchall()

    for r in rows:
        print r[0],r[1],r[2],r[3],r[4],r[5]
