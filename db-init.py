import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

db.execute('''
    DROP TABLE IF EXISTS sports
''')

db.execute('''
CREATE TABLE sports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INT,
    name TEXT,
    ovrName TEXT,
    ovrValue TEXT,
    ovrPCTName TEXT,
    ovrPCTValue TEXT,
    confName TEXT,
    confValue TEXT,
    confPCTName TEXT,
    confPCTValue TEXT,
    streakName TEXT,
    streakValue TEXT,
    homeName TEXT,
    homeValue TEXT,
    awayName TEXT,
    awayValue TEXT,
    neutralName TEXT,
    neutralValue TEXT
);
''')



connection.commit()
connection.close()


