"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = int(input("How many miles will you travel? "))
time_hours_input = int(input("How many hours will the journey take? "))

# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values

if (distance_miles_input <= 0 | time_hours_input <= 0):
    print("Input cannot be less than or equal to 0")
    exit()

avg_speed = distance_miles_input / time_hours_input
print(f"Your average speed going to {destination} will be {avg_speed:.2f} mph.")
