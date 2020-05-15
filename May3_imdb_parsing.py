import requests
from bs4 import BeautifulSoup as bs

link = "https://www.imdb.com/name/nm0000123/"

html_data = requests.get(link).content
html_soup = bs(html_data)

# stories = html_soup.find_all("span", {"class":"year_column"})

stories = html_soup.find_all("div", {"class":"filmo-row"})
# stories = html_soup.find_all("a")

# print(stories[1].a.text)
# print(stories[1].span.text)

for story in stories:
    print(story.a.text)
    print(story.span.text)
    
#     check = story.get("id")
#     if "actor" in check:
#         print(check)

# print(stories[0].get("href"))
# for story in stories:
#     print(story.text)