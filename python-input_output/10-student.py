#!/usr/bin/python3
"""
Class Student that defines a student.
"""


class Student:
    """
    Student class with atributes first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes instance attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):

            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }

        return self.__dict__
