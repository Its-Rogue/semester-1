# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # original string 
print(f"Modified String 1: {user_string.lower()}") # sets all characters to lower case
print(f"Modified String 2: {user_string.upper()}") # sets all characters to upper case
print(f"Modified String 3: {user_string.strip()}") # removes trailing and leading whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces all 'a' characters with '@'
print(f"Modified String 5: {user_string.capitalize()}") # capitalises alphabetic characters that trail a whitespace
print(f"Modified String 6: {user_string[::-1]}") # inverses the order of the string
print(f"Modified String 7: {user_string.title()}") # formats the string into a title (capital letters trailing spaces, unless the word is a preposition)
print(f"Modified String 8: {len(user_string)}") # returns the length of the string
print(f"Modified String 9: {user_string.find('a')}") # returns the position of the first a in the string, or -1 if the string does not contain one
print(f"Modified String 10: {user_string.count('a')}") # counts the number of 'a' characters in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks if the first 5 characters are "Hello"
print(f"Modified String 12: {user_string.endswith('!')}") # checks if the final character of the string is '!'
print(f"Modified String 13: {user_string.isalnum()}") # checks if the string only contains alphanumeric characters
print(f"Modified String 14: {user_string.isalpha()}") # checks if the string only contains alphabetic characters
print(f"Modified String 15: {user_string.isdigit()}") # checks if the string only contains numericac characters



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!