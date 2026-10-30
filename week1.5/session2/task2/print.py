# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object

from geometry import Point
from geometry import Circle

point = Point(0,5)
circle = Circle(5, point)

print(point.__str__())
print(circle.__str__())