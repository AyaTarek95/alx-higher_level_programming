#!/usr/bin/python3
""" Define obj attribute lookup function."""


def lookup(obj):
    """Return list of attributes and methods of object"""
    return (dir(obj))
