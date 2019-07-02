import requests
from bs4 import BeautifulSoup
import sys


url = "http://www.imdb.com/chart/top?ref_=nv_ch_250_4"
headers = {"Accept-Language":"en-US,en;q=0.5"}
source = requests.get(url, headers=headers).text

soup = BeautifulSoup(source, "lxml")
sys.stdout = open("imdb.txt", "wt")

for titleColumn in soup.find_all('td',class_='titleColumn'):

    title = titleColumn.text.strip()
    print("Rank: ",title[0:].split('.')[0])

    name = titleColumn.a.text
    print("Title: ", name)

    an = titleColumn.span.text[1:-1]
    print("Year:", an)

    print()

sys.stdout.close()





