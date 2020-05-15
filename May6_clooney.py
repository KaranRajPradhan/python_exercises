import requests
from bs4 import BeautifulSoup as bs

link = "https://www.imdb.com/name/nm0000123/"

html_data = requests.get(link).content
html_soup = bs(html_data)

# stories = html_soup.find_all("span", {"class":"year_column"})

stories = html_soup.find_all("div", {"class":"filmo-category-section"})

# print(stories[0].get("href"))
# for story in stories:
print(stories[0])