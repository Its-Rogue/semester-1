# Week 1.5, Session 1: Task 3

import math

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



# Finally, add code here to demonstrate use of Point

p1 = Point(1.0,2.0)
p2 = Point(2.0,3.0)

print(p1.distance_to(p2))