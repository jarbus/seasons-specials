import os
import re
import json
from time import sleep

for state in ["ny", "ak"]:
    for csa in os.listdir(f"{state}"):
        with open(f"{state}/{csa}/address") as address_file:
            addr = address_file.read()
        if addr == "None":
            continue

        abbreviation = re.search(r", [A-Z]{2}",addr).group(0)[2:]
        print(abbreviation)

        with open(f"{state}/{csa}/state","w") as state_file:
            state_file.write(f"{abbreviation}")
