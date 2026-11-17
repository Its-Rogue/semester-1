# See README.md for instructions on what to do this program

import random

# Seeding makes the pseudo-random sequence repeatable. Without a seed,
# Python uses system entropy and generally produces different results.
random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)
