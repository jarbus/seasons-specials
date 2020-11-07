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

cities = []
with open("cities.txt") as file:
    for line in file:
        cities.append(line.strip())

for city in cities[:1]:
    print(f"downloading {city}")
    state = city[-2:]
    with open(f"data/{state}/{city[:-2]}") as file:
        wiki = f"https://www.localharvest.org/{city}"
        page = requests.get(wiki)
        soup = BeautifulSoup(page.text, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href[:len(city)] == city and href[len(city):] not in blacklist:
                file.write(href[len(city):])
