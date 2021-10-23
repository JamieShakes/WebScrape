import re
from urllib.request import urlopen

class FoundThing:
    def __init__(self, link):
        self.link = link
        self.title = ""
    def set_title(self, title):
        self.title = title

url = "https://news.ycombinator.com"
page = urlopen(url)
html = page.read().decode("utf-8")

foundThings = []

patternlinks = "a href=.*?titlelink.*?</a>"
match_links = re.findall(patternlinks, html, re.IGNORECASE)
for i in match_links:
    i = re.search("\".*?\"", i, re.IGNORECASE)
    theLink = i.group().strip('"')
    thing = FoundThing(theLink)
    foundThings.append(thing)

patterntitles = "titlelink\"\>.*?\<"
match_titles = re.findall(patterntitles, html, re.IGNORECASE)
f = 0
for j in match_titles:
    j = re.search(">.*?<", j, re.IGNORECASE)
    theTitle = j.group().strip('<').strip('>')
    foundThings[f].set_title(theTitle)
    f+= 1
    
for thing in foundThings:
    print(thing.title + ": " + thing.link)
    
