'''
Write IMDB Top 250 movies to a .txt file
'''
import requests
from bs4 import BeautifulSoup
url = "http://www.imdb.com/chart/top"
r = requests.get(url)
soup = BeautifulSoup(r.text)
with open('IMDB250.txt', 'w') as open_file:
    for titleColumn in soup.find_all("td", class_ ="titleColumn"):
        open_file.write(titleColumn.a.text + '\n')
