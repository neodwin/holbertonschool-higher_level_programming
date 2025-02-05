#!/usr/bin/python3
"""
Module defines an abstract class.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Sound method in each subclass.
        """
        pass


class Dog(Animal):
    """
    Class Dog.
    """

    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Class Cat.
    """

    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow"
