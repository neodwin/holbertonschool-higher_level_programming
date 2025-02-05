#!/usr/bin/env python3
"""
Defines a class VerboseList.
"""


class VerboseList(list):
    """
    Class VerboseList.
    """

    def append(self, item):
        """
        Append method: After adding the item to the list, print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend method: After extending the list, print a message.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove method: Before removing the item from the list, print a message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop method: Before popping the item from the list, print a message.
        """
        item = self[index] if self else 'None (list is empty)'
        result = super().pop(index) if self else None
        print(f"Popped [{item}] from the list.")
        return result
