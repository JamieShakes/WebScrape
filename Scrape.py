import re
from urllib.request import urlopen

url = "https://news.ycombinator.com"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "a href=.*?titlelink.*?</a>"
match_titles = re.findall(pattern, html, re.IGNORECASE)
print(match_titles)
