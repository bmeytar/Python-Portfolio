from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")

article_texts = []
article_links = []
article_scores = [int(score.getText().split()[0]) for score in scores]

for tag in articles:
    text = tag.find(name="a").getText()
    article_texts.append(text)
    link = tag.find(name="a").get("href")
    article_links.append(link)


index = article_scores.index(max(article_scores))
print(article_texts[index])
print(article_links[index])
