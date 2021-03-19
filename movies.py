import requests
from bs4 import BeautifulSoup

URL = 'https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='page-content')
job_elems = results.find_all(class_='list-item__title')

file = open("Movies.txt", "a")

for i in job_elems:
    file.write(i.text + '\n')
file.close()
