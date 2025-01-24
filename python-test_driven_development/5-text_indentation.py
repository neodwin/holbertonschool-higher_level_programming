#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Text must be a string
    Raise a TypeError
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print("\n".join([line.strip() for line in text.split("\n")]), end="")
