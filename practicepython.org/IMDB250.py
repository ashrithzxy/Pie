'''
Print out IMDB Top 250 movies
'''
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.imdb.com/chart/top")
r_html = r.text
soup = BeautifulSoup(r_html)
for titleColumn in soup.find_all("td", class_ ="titleColumn"):
    print(titleColumn.a.text)
