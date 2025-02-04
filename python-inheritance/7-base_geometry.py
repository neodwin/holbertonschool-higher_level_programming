#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class with public instance methods.
    """

    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
