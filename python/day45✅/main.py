from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
data = response.text
soup = BeautifulSoup(data , 'html.parser')
tags = soup.find(name='a' , class_='score')
print(soup)
texts = []
links = []
for tag in tags:
    texts.append(tag.getText())
    links.append(tag.get('herf'))


upvote = [score.getText() for score in soup.find_all(name='span' , class_='score').getText()]


print(texts , links , upvote)















# with open("website.html") as file:
#     data = file.read()
#     soup = BeautifulSoup(data , 'html.parser')
    