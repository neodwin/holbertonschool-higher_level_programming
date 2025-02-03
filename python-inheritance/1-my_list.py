#!/usr/bin/python3
"""
Class MyList that inherits fro list
"""


class MyList(list):
    """
    That prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        """
        Prints the elements of the list sorted.
        """
        print(sorted(self))
