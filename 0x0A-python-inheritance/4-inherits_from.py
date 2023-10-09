#!/usr/bin/python3
"""Module for method inherits_from."""


def inherits_from(obj, a_class):
    """check wether object is derived from a_class."""
    return isinstance(obj, a_class) and type(obj) != a_class
