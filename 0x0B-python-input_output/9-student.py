#!/usr/bin/python3
"""Define class Student."""


class Student:
    """Represent Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of student."""
        return self.__dict__
