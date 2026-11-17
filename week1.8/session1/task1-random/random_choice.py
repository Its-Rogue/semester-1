import random
from pathlib import Path

names_file = Path(__file__).with_name("names.txt")
with names_file.open() as infile:
    names = [line.strip() for line in infile if line.strip()]

count = int(input("How many names do you want to pick? "))
if count < 0:
    raise ValueError("number of names must not be negative")
if count > len(names):
    raise ValueError("not enough names in the file")

chosen = random.sample(names, count)
for name in chosen:
    print(name)
