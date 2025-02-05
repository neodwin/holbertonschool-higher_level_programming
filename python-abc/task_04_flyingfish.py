#!/usr/bin/env python3
"""
Defines classes Fish, Bird, FlyingFish.
"""


class Fish:
    """
    Class fish.
    """
    def swim(self):
        """
        Method to print "The flying fish is swimming!".
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method to print "The fish lives in water".
        """
        print("The fish lives in water")


class Bird:
    """
    Class bird.
    """
    def fly(self):
        """
        Method to print "The bird is flying".
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method to print "The bird lives in the sky".
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class FlyingFish.
    """
    def swim(self):
        """
        Method to print "The flying fish is swimming!".
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Method to print "The flying fish is soaring!".
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Method to print "The flying fish lives both in water and the sky!".
        """
        print("The flying fish lives both in water and the sky!")
