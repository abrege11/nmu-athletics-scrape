import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

data = db.execute("SELECT ovrValue, sportsId, year FROM sportsInfo").fetchall()
sportsNames = db.execute("SELECT * FROM sports").fetchall()

class Scorecard:
    def __init__(self, win, loss, tie, id, year):
        self.win = win
        self.loss = loss
        self.tie = tie
        self.id = id
        self.year = year

    def printValues(self):
        return [self.win, self.loss, self.tie, self.id, self.year]
    
scorecardList = []

def getAllValues():
    values = []
    for row in data:
        dataList = row[0].split('-')
        if(len(dataList) == 3):
            scorecardList.append(Scorecard(dataList[0], dataList[1], dataList[2], row[1], row[2]))
        else:
            scorecardList.append(Scorecard(dataList[0], dataList[1], 0, row[1], row[2]))

    for scorecard in scorecardList:
        values.append(scorecard.printValues())
    return values

values = getAllValues()
print(values)



connection.commit()
connection.close()