from bs4 import BeautifulSoup
import urllib.request

def custom_selector(tag):
	# Return "span" tags with a class name of "target_span"
	return tag.name == "span" and tag.has_attr("class") and "flex-item-1" in tag.get("class")

football = {}

footballYears = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
for year in footballYears:
    print("this is for year " + str(year))
    html = urllib.request.urlopen("https://nmuwildcats.com/sports/football/schedule/" + str(year))
    soup = BeautifulSoup(html, features="html.parser")
    # spans = soup.find('div', role='complementary').li.text
    spans = soup.find_all(custom_selector)
    for span in spans:
        print(span.text)




