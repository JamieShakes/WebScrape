import re
from urllib.request import urlopen

url = "https://news.ycombinator.com"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "a href=.*?titlelink.*?</a>"
match_titles = re.findall(pattern, html, re.IGNORECASE)
for i in match_titles:
    i = re.search("\".*?\"", i, re.IGNORECASE)
    print(i.group().strip('"'))
