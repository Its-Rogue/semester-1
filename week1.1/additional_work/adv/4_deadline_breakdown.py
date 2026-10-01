"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = input("Minutes remaining until the deadline: ")

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead

try:
    minutes_remaining_input = int(minutes_remaining_input)
except:
    print("Invalid input")
    exit()

if (minutes_remaining_input < 0):
    print("The deadline has already passed")
    exit()    

days = minutes_remaining_input // 1440
minutes_remaining_input = minutes_remaining_input % 1440
hours = minutes_remaining_input // 60
minutes = minutes_remaining_input % 60

print(f"There are {days} days, {hours} hours and {minutes} minutes until the deadline.")