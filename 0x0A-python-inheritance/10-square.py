#!/usr/bin/python3
"""Module of class square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass to Rectangle class."""
   
   def __init__(self, size):
        """Initialize new square."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculate area method."""
        return self.__size **2
