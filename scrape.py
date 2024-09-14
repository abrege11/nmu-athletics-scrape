from bs4 import BeautifulSoup
import urllib.request
import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

def info_selector(tag):
	# Return "span" tags with a class name of "target_span"
	return tag.name == "span" and tag.has_attr("class") and "flex-item-1" in tag.get("class")

def year_selector(tag):
	return tag.name == "option" and tag.has_attr("value") and "schedule" in tag["value"]

# "womens-cross-country", "womens-golf", "womens-skiing", "womens-swimming-and-diving", "womens--track-and-field", "mens-golf", "mens-swimming-and-diving"
# "wCrossCountry", "wGolf", "wNordicSkiing", "wSwimmingDiving", "wTrackField", "mGolf", "mNordicSkiing", "mSwimmingDiving"
sports = ["wBasketball", "wLacrosse", "wSoccer", "wVolleyBall", "wWrestling", "mBasketball", "mFootball", "mHockey", "mSoccer"]
sportsUrls = ["womens-basketball", "womens-lacrosse", "womens-soccer", "womens-volleyball", "womens-wrestling", "mens-basketball", "football", "mens-ice-hockey", "mens-soccer"]
football={}
print("Parsing data...")
def getYears(sport):
    print("Getting years...")
    temp=[]
    html = urllib.request.urlopen(f"https://nmuwildcats.com/sports/{sport}/schedule/")
    soup = BeautifulSoup(html, features="lxml")
    years = soup.find_all(year_selector)
    for year in years: 
        temp.append(year.text.strip())
    return temp
print("Beginning sports loop...")
for sport in sportsUrls:
    years = getYears(sport)
    for year in years:
        temp=[]
        # print("this is for year " + str(year))
        html = urllib.request.urlopen(f"https://nmuwildcats.com/sports/{sport}/schedule/{year}")
        soup = BeautifulSoup(html, features="lxml")
        spans = soup.find_all(info_selector)
        id = sportsUrls.index(sport) + 1
        for span in spans:
            temp.append(span.text)
        temp.append(year)
        temp.append(id)
        football[year] = temp

    for year in years:
        db.execute('INSERT INTO sportsInfo (ovrName, ovrValue, ovrPCTName, ovrPCTValue, confName, confValue, confPCTName, confPCTValue, streakName, streakValue, homeName, homeValue, awayName, awayValue, neutralName, neutralValue, year, sportsId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', football[year])
print("✔ data parsed, exiting.")
connection.commit()
connection.close()