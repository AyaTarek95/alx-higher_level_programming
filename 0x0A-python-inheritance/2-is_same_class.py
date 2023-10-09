#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """Return True if object is exactly instance of the specified class."""
    return type(obj) == a_class
