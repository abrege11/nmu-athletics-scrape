import sqlite3
from collections import defaultdict

connection = sqlite3.connect('sports.db')
db = connection.cursor()
length = len(["wBasketball", "wLacrosse", "wSoccer", "wVolleyBall", "wWrestling", "mBasketball", "mFootball", "mHockey", "mSoccer"])
namingDictionary = {
    1: "Womens Basketball",
    2: "Womens Lacrosse",
    3: "Womens Soccer",
    4: "Womens Volleyball",
    5: "Womens Wrestling",
    6: "Mens Basketball",
    7: "Mens Football",
    8: "Mens Hockey",
    9: "Mens Soccer"
}
data = db.execute("SELECT ovrValue, sportsId, year FROM sportsInfo").fetchall()
sportsNames = db.execute("SELECT * FROM sports").fetchall()

winningStatsList = {}

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

def listToDict(values):
    res = defaultdict(list)
    for value in values:
        res[value[3]].append(value)
    return res

# get a list of lists of all values 
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

# get total win loss tie for each team, along with years recorded in a list
# output: dictionary of lists
def getTotals():
    values = getAllValues()
    temp = []
    res = listToDict(values)
    for key, val in res.items():
        temp = [0, 0, 0, 0, []]
        for i in range(len(val)-1):
            temp[0] += int(val[i][0])
            temp[1] += int(val[i][1])
            temp[2] += int(val[i][2])
            temp[3] = key
            temp[4].append(val[i][4])
        
        res[key] = temp[:]
        temp.clear()
    return res

# get each teams years showing if they had a winning or losing season
def getWinningYears():
    values = getAllValues()
    res = listToDict(values)
    for key, val in res.items():
        for i in range(len(val)-1):
            print(val[i])
    return res

# -- getAllValues call
# values = getAllValues()
# print(values)

# -- getTotals call
vals = getTotals()
for val in vals.values():
    print(f"{namingDictionary[val[3]]}: {val}\n")

# getWinningYears()


connection.commit()
connection.close()