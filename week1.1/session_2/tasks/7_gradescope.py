# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!

def get_number(): 
    num = input("Enter a number: ")

    try:
        num = int(num)
    except:
        exit("That is not a number")

    return num

num1 = get_number()
num2 = get_number()
result = num1 * num2

print(f"The multiple of {num1} and {num2} is {result}")