"""
Vec2: 2 dimensional vector class

This is the class for handling 2 dimensional vectors
"""

import math
from .constants import *


class Vec2(object):
    """Class representing a 2D-Vector. Values are always stored as float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        """Convert vector to string
        """
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"

    def copy(self):
        """
        :return: copy of current vector
        """
        return Vec2(self.x, self.y)