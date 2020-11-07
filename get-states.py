import requests
from bs4 import BeautifulSoup

blacklist = {
"farms",
"csa",
"farmers-markets",
"restaurants",
"food-coops",
"u-pick",
"farm-stands",
"others",
"list"}

city = '/locations/'
wiki = f"https://www.localharvest.org/{city}"
page = requests.get(wiki)
soup = BeautifulSoup(page.text, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href[:len(city)] == city and href[len(city):] not in blacklist:
        print(href[len(city):])
