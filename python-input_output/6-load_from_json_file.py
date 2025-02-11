#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Returns an object created from a JSON file.
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
