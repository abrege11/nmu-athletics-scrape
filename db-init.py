import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()
sports = ["wBasketball", "wCrossCountry", "wGolf", "wLacrosse", "wNordicSkiing", "wSoccer", "wSwimmingDiving", "wTrackField", "wVolleyBall", "wWrestling", "mBasketball", "mFootball", "mGolf", "mHockey", "mNordicSkiing", "mSoccer", "mSwimmingDiving"]

db.execute('''
    DROP TABLE IF EXISTS sports
''')

db.execute('''
    DROP TABLE IF EXISTS sportsInfo
''')

db.execute('''
    CREATE TABLE sports (
        sportsId INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
);
''')

db.execute('''
CREATE TABLE sportsInfo (
    sportsInfoId INTEGER PRIMARY KEY AUTOINCREMENT,
    sportsId,
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
    neutralValue TEXT,
    FOREIGN KEY (sportsId) REFERENCES sports(sportsId)
);
''')

for sport in sports:
    db.execute("INSERT INTO sports (name) VALUES (?)", (sport,))

connection.commit()
connection.close()


