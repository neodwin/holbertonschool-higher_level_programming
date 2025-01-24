#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_one(self):
        self.assertEqual(max_integer([2]), 2)

    def test_one_neg(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_upper(self):
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)


if __name__ == '__main__':
    unittest.main()
