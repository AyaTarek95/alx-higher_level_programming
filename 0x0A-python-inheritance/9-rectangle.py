#!/usr/bin/python3
"""Module of class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Derived from BaseGeometry class."""
    def __init__(self, width, height):
        """Initialize new Rectangle."""
        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)

    def area(self):
        """Calculates area."""
        return self.__width * self.__height

    def __str__(self):
        """str representation method."""
        return "[Rectangle]" + str(self.__width) + "/" + str(self.__height)
