#!/usr/bin/python3
"""Module of class Rectangle."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Derived class from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize new Rectangle."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
