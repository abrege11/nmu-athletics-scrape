import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

data = db.execute("SELECT ovrValue, sportsId, year FROM sportsInfo").fetchall()
sportsNames = db.execute("SELECT * FROM sports").fetchall()

for row in data:
    print(row)
for name in sportsNames:
    print(name)


connection.commit()
connection.close()