import requests
from bs4 import BeautifulSoup

URL = 'https://pitchfork.com/features/lists-and-guides/the-200-best-albums-of-the-2010s/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

mydivs = soup.find_all("div", {"class": "grid--item body body__container article__body"})
file = open("Music.txt", "a")

for i in soup.find_all(["h2"]):
    file.write(i.text + '\n')
file.close()
