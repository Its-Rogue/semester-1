# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def distance_to(self, point_2):
        x_displacement = point_2.x - self.x
        y_displacement = point_2.y - self.y
        return math.sqrt((x_displacement * x_displacement) + (y_displacement * y_displacement))

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return round((math.pi * self.radius * self.radius), 2)

    def perimeter(self):
        return round((math.pi * 2 * self.radius), 2)