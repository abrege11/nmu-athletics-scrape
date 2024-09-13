from bs4 import BeautifulSoup
import urllib.request
import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

def custom_selector(tag):
	# Return "span" tags with a class name of "target_span"
	return tag.name == "span" and tag.has_attr("class") and "flex-item-1" in tag.get("class")

# def getYears(name):
#     years=[] 
#     return years

sports = ["wBasketball", "wCrossCountry", "wGolf", "wLacrosse", "wNordicSkiing", "wSoccer", "wSwimmingDiving", "wTrackField", "wVolleyBall", "wWrestling", "mBasketball", "mFootball", "mGolf", "mHockey", "mNordicSkiing", "mSoccer", "mSwimmingDiving"]
sportsUrls = ["womens-basketball", "womens-cross-country", "womens-golf", "womens-lacrosse", "womens-kiing", "womens-soccer", "womens-swimming-and-diving", "womens--track-and-field", "womens-volleyBall", "womens-wrestling", "mens-basketball", "mens-football", "mens-golf", "mens-hockey", "mens-skiing", "mens-soccer", "mens-swimming-and-diving"]
footballYears = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
football={}

for year in footballYears:
    temp=[]
    # print("this is for year " + str(year))
    html = urllib.request.urlopen("https://nmuwildcats.com/sports/football/schedule/" + str(year))
    soup = BeautifulSoup(html, features="lxml")
    spans = soup.find_all(custom_selector)
    for span in spans:
        temp.append(span.text)
    football[year] = temp
for i in range(len(footballYears)):
    football[footballYears[i]].append(footballYears[i])
    football[footballYears[i]].append(12)
    db.execute('INSERT INTO sportsInfo (ovrName, ovrValue, ovrPCTName, ovrPCTValue, confName, confValue, confPCTName, confPCTValue, streakName, streakValue, homeName, homeValue, awayName, awayValue, neutralName, neutralValue, year, sportsId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', football[footballYears[i]])

connection.commit()
connection.close()