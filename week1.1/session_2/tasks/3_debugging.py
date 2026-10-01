# there are several errors in this code
# run the code, read the error messages or look at the output, and fix the problems

# Find and fix the errors

name = input("Enter your name: ") # imput instead of input
age = int(input("Enter your age: ")) # int wrapper needs to go on input not variable
city = input("Enter your city: ") # leading whitespace at the start of the line

print("Hello {name}, you are {age} years old and live in {city}.") # missing an f before "" to allow for inline variables in a print statement