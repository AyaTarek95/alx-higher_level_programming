#!/usr/bin/python3
"""Module of class Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A derived class of Rectangle."""
    def __init__(self, size):
        """Initialize new Square."""
        self.__size = size
        self.integer_validator = ("size", size)
        super().__init__(size, size)

    def area(self):
        """Area of square method."""
        return self.__size ** 2

    def __str__(self):
        """Method represent of square as a string."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
