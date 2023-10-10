#!/usr/bin/python3
"""Define function save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a file using json representaion."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
