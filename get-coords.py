import os
import re
import json
import requests
from time import sleep

i = 0
for state in ["ny", "ak"]:
    for csa in os.listdir(f"{state}"):
        if i < 127:
            i+= 1
            continue
        with open(f"{state}/{csa}/address") as address_file:
            addr = address_file.read()
        if addr == "None":
            continue

        town = int(re.search(r"\d\d\d\d\d",addr).group(0))
        req = requests.get(f"http://geocode.xyz/{town}?geoit=json")
        obj = json.loads(req.text)
        print(i, town, obj["latt"], obj["longt"])
        print(obj)

        with open(f"{state}/{csa}/coords","w") as coord_file:
            coord_file.write(f"{obj['latt']} {obj['longt']}\n")
        sleep(1.2)
        i += 1
