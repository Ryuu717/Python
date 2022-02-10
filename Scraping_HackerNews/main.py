from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# print(response.text)
web_text = response.text
soup = BeautifulSoup(web_text, "html.parser")
# print(soup)

articles = soup.find_all(name="a", class_="titlelink")
# print(articles)

article_texts = []
article_urls = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    url = article.get("href")
    article_urls.append(url)
# print(article_texts)
# print(article_urls)

#Find High Score Articles
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_score = max(scores)
max_score_index = scores.index(max_score)+1

print(article_texts[max_score_index])
print(article_urls[max_score_index])









