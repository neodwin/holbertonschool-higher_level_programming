#!/usr/bin/python3
"""
Defines a class CountedIterator.
"""


class CountedIterator:
    """
    Class CountedIterator.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Returns a counter to track the number of items iterated.
        """
        return self

    def __next__(self):
        """
        Increment the counter each time.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Retrieve and print the number of items that have been fetched.
        """
        return self.count
