import os

with open("csas-ak.txt") as file:
    for state in file:
        os.system(f"mkdir {state}")
