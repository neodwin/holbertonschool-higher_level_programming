#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""

import sys
from os.path import exists

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_items_to_list_and_save():
    """
    Adds all arguments to a Python list, and then save them to a file.
    """

    if exists("add_item.json"):
        items = load_from_json_file("add_item.json")
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    add_items_to_list_and_save()
