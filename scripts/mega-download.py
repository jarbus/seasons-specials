import requests
import string
import os
import re
from time import sleep
from bs4 import BeautifulSoup


def get_food_from_csa_url(page):
    soup = BeautifulSoup(page.text, "html.parser")
    season_to_foods = dict()
    for s in soup.find_all(class_="tab-panel"):
        season = s.find_all("h5")
        if not season:
            continue
        season = str(season[0].contents[0])
        foods = [str(link.get("href")[1:-4])  for link in s.find_all("a")]
        season_to_foods[season] = foods
    return season_to_foods

#print(get_food_from_csa_url("https://www.localharvest.org/back-home-farm-M45242"))

def get_csa_urls():
    # For troy new york csas
    #urls = []
    #for i in range(1,4):
    #    page = requests.get(f"https://www.localharvest.org/search.jsp?m&lat=42.744&lon=-73.60512&scale=8&ty=0&p={i}")
    #    soup = BeautifulSoup(page.text, "html.parser")
    #    for farm in soup.find_all(class_="membercell"):
    #        urls.append(farm.a.get("href")[1:])

    # For anchorage alaska csas
    urls = []
    page = requests.get(f"https://www.localharvest.org/search.jsp?jmp&scale=7&lat=61.218666&lon=-149.8671")
    soup = BeautifulSoup(page.text, "html.parser")
    for farm in soup.find_all(class_="membercell"):
        urls.append(farm.a.get("href")[1:])


    # For all CSAs
    # farms = "https://www.localharvest.org/organic-farms/list"
    # for char in string.ascii_uppercase:
    #    page = requests.get(f"https://www.localharvest.org/organic-farms/list?l={char}")
    #    soup = BeautifulSoup(page.text, "html.parser")
    #    for link in soup.find("blockquote").find_all("a"):
    #        urls.append(link.get("href")[1:])
    return urls

#print(get_csa_urls())



def get_csa_location(page):

    page = page.text.replace("\n","")
    locblock = re.search(r"<h5>Location</h5>(.*?)</div>",page)
    if not locblock:
        return "None"
    address = re.sub(r'<.*?>','',locblock.group(1))
    address = re.sub(r'\s\s+',' ',address).strip()
    return address

# Download all farm urls
#with open("csas-ak","w") as file:
#    for url in get_csa_urls():
#        file.write(url+"\n")

with open("csas-ak.txt","r") as file:
    for line in file:
        line = line.strip()
        print(f"Downloading {line}...")

        #os.system(f"mkdir {line}")
        page = requests.get(f"https://www.localharvest.org/{line}")
        with open(f"{line}/address","w") as farm:
            farm.write(get_csa_location(page))
        food = get_food_from_csa_url(page)
        with open(f"{line}/spring","w") as spring:
            if "Spring" in food:
                for item in food["Spring"]:
                    spring.write(f"{item}\n")
        with open(f"{line}/summer","w") as summer:
            if "Summer" in food:
                for item in food["Summer"]:
                    summer.write(f"{item}\n")
        with open(f"{line}/winter","w") as winter:
            if "Winter" in food:
                for item in food["Winter"]:
                    winter.write(f"{item}\n")
        with open(f"{line}/fall","w") as fall:
            if "Fall" in food:
                for item in food["Fall"]:
                    fall.write(f"{item}\n")
