#!/usr/bin/python3
"""
Function that reads a text file (UTF-8) and prints it
to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
