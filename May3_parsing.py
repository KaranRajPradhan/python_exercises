import requests
from bs4 import BeautifulSoup as bs

link = "https://news.ycombinator.com"

html_data = requests.get(link).content
html_soup = bs(html_data)

stories = html_soup.find_all("a", {"class":"storylink"})

print(stories[0].get("href"))
print(stories[0].text)