'''
Print out IMDB Top 250 movies
'''
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.imdb.com/chart/top")
r_html = r.text
soup = BeautifulSoup(r_html)
for titleColumn in soup.find_all("td", class_ ="titleColumn"):
    #if titleColumn.a:
    #open_file = open('IMDB250.txt', 'w')
    #open_file.write(titleColumn.a.text)
    #open_file.close()
    #with open('IMDB250.txt', 'w') as open_file:
        #open_file.write(titleColumn.a.text)
    print(titleColumn.a.text)
    #else:
    #print(titleColumn.contents[0].strip())
