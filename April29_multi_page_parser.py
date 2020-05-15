import April29_hacker_rank_parser
from pprint import pprint

page_number = 1
link = f"https://news.ycombinator.com/news?p={page_number}"

result = hacker_rank_parser.main(link)
pprint(result)