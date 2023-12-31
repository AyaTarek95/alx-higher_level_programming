#!/usr/bin/python3
"""Define Class Student."""


class Studen:
    """Represenr a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of student."""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
