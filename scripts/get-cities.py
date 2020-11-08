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

initials = []
with open("states.txt") as file:
    for line in file:
        initials.append(line.strip())

head = "https://www.localharvest.org"
for location in initials:
    tail = f"/locations/{location}"

    page = requests.get(head+tail)
    soup = BeautifulSoup(page.text, "html.parser")
    for link in soup.find_all('a'):
        href = link.get('href')
        if href[-3:] == f"-{location}":
            print(href[1:])

#city = '/locations/'
#wiki = f"https://www.localharvest.org/{city}"
#page = requests.get(wiki)
#soup = BeautifulSoup(page.text, "html.parser")
#for link in soup.find_all('a'):
#    href = link.get('href')
#    if href[:len(city)] == city and href[len(city):] not in blacklist:
#        print(href[len(city):])
