#!/usr/bin/python3
"""
Defines classes Mixins & Dragon.
"""


class SwimMixin:
    """
    Class Swimmixing.
    """
    def swim(self):
        """
        Method to print "The creature swims!".
        """
        print("The creature swims!")


class FlyMixin:
    """
    Class FlyMixin.
    """
    def fly(self):
        """
        Method to print "The creature flies!".
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class Dragon.
    """
    def roar(self):
        """
        Method to print "The dragon roars!".
        """
        print("The dragon roars!")
