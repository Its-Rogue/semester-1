# Week 1.5, Session 2: Task 1

# Add type checking to the constructor of Point

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """

        if isinstance(x, int) or isinstance(x, float):
            self.x = x
        else:
            raise TypeError("X must be an int or a float")

        if isinstance(y, int) or isinstance(y, float):
            self.y = y
        else:
            raise TypeError("Y must be an int or a float")

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """

        if isinstance(self, Point):
            return math.hypot(self.x, self.y)
        else:
            raise TypeError("Input must be a Point object")

    def distance_to(self, p):
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

p = Point("two", "one")
print(p.distance())
