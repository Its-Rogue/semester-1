# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

from geometry import Point
from geometry import Circle

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

p1 = Point(1.0, 2.0)
c1 = Circle(p1, 5)

print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")

