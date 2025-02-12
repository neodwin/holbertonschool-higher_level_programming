#!/usr/bin/env python3
import csv
import json
"""
Function named convert_csv_to_json.
"""


def convert_csv_to_json(csv_filename):
    """
    Function named convert_csv_to_json that takes the CSV filename
    as its parameter and writes the JSON data to data.json.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w', newline='') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
