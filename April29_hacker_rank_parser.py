from bs4 import BeautifulSoup as bs
import requests

def get_ranks(soup):
    ranks = soup.find_all("span", {"class":"rank"})

    rank_list = []
    for rank in ranks:
        num = rank.text.replace(".","")
        rank_list.append(num)
    return rank_list

def get_articles(soup, rank_list, main_link):
    all_links = soup.find_all("a", {"class":"storylink"})
    counter = 0
    final_list = []
    for article in all_links:
        article_dict = {}
        article_dict["text"] = article.text
        article_link = article.get("href")
        
        rank = rank_list[counter]
        article_dict["rank"] = rank
        if "http://" in article_link or "https://" in article_link:
            article_dict["link"] = article.get("href")
        else:
            abs_url = main_link + article_link
            article_dict["link"] = abs_url
        final_list.append(article_dict)
        
        counter += 1
    return final_list

def main(link):
    response = requests.get(link)
    html_data = response.content
    soup = bs(html_data)

    ranks = get_ranks(soup)
    articles = get_articles(soup, ranks, link)
    return articles

if __name__ == "__main__":
    link = "https://news.ycombinator.com/"
    result = main(link)
print(result)