#!/usr/bin/env python3
"""
Functionality to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    A Python Dictionary with data. If the output file
    already exists it should be replaced.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    This function returns a Python Dictionary with
    the deserialized JSON data from the file.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
