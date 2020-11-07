import os

with open("states.txt") as file:
    for state in file:
        os.system(f"mkdir data/{state}")
