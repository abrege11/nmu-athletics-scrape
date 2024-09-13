import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

data = db.execute("SELECT ovrValue FROM sports")

for row in data:
    print(row[0])

connection.commit()
connection.close()