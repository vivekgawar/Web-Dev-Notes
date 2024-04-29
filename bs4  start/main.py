from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
print(article_upvotes[max_upvotes_index])
























# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
# # all_anchor_tags = soup.find_all(name="a")
#
# for tags in all_anchor_tags:
#    print(tags.getText())
#    print(tags.get("href"))
#
# print(soup.find(name="h1", id="name"))
