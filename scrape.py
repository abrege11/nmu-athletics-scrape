from bs4 import BeautifulSoup
import urllib.request
import lxml
import sqlite3

connection = sqlite3.connect('sports.db')
db = connection.cursor()

def custom_selector(tag):
	# Return "span" tags with a class name of "target_span"
	return tag.name == "span" and tag.has_attr("class") and "flex-item-1" in tag.get("class")

footballList = []
footballYears = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
football={}

def helper(spans):
    for span, index in zip(spans, indexes):
        temp[index] = span.text
    football[footballYears[i]] = temp

for i in range(len(footballYears)):
    # print("this is for year " + str(year))
    html = urllib.request.urlopen("https://nmuwildcats.com/sports/football/schedule/" + str(footballYears[i]))
    soup = BeautifulSoup(html, features="lxml")
    indexes = ["ovrName", "ovrValue", "ovrPCTName", "ovrPCTValue", "confName", "confValue", "confPCTName", "confPCTValue", "streakName", "streakValue", "homeName", "homeValue", "awayName", "awayValue", "neutralName", "neutralValue"]
    # spans = soup.find('div', role='complementary').li.text
    spans = soup.find_all(custom_selector)
    temp={}
    for span, index in zip(spans, indexes):
        temp[index] = span.text
    football[footballYears[i]] = temp
    footballList.append(football)
for item, year, index in zip(footballList, footballYears, indexes):
    print("This is year " + str(year))
    print(item[year])
    # db.execute(f"INSERT INTO sports VALUES ( {item[year]['ovrName']}, {item[year]['ovrValue']}, {item[year]['ovrPCTName']}, {item[year]['ovrPCTValue']}, {item[year]['confName']}, {item[year]['confValue']}, {item[year]['confPCTName']}, {item[year]['confPCTValue']}, {item[year]['streakName']}, {item[year]['streakValue']}, {item[year]['homeName']}, {item[year]['homeValue']}, {item[year]['awayName']}, {item[year]['awayValue']}, {item[year]['neutralName']}, {item[year]["neutralValue"]})")
    # print(db.execute("SELECT * FROM SPORTS"))
    print("\n")


