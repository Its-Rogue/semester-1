import random
from pathlib import Path

count = int(input("How many random numbers do you want? "))
numbers = [random.randint(1, 100) for _ in range(count)]
output = Path(__file__).with_name("random.txt")

with output.open("w") as outfile:
    for number in numbers:
        outfile.write(f"{number}\n")

print(f"Wrote {count} random numbers to {output.name}")
