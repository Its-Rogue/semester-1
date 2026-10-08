# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Enter the integer grade: ")

try:
    grade = int(grade)
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade > 100 or grade < 0:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 40:
    print(f"{grade} is a Fail")
elif grade >= 40 and grade < 70:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")