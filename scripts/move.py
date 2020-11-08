import os

with open("csas-ak.txt") as file:
    for line in file:
        print(line)
        os.system(f"mv {line.strip()} ak/")
