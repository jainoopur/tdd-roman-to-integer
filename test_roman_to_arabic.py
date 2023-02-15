import unittest

from roman_to_arabic import roman_to_arabic


# 1, 2, 5, 6, 4, 10, 9
class TestRomanToArabic(unittest.TestCase):
    def test_I(self):
        self.assertEqual(1, roman_to_arabic("I"))

    def test_II(self):
        self.assertEqual(2, roman_to_arabic("II"))

    # Do we need this? It is not a failing test...
    def test_III(self):
        self.assertEqual(3, roman_to_arabic("III"))

    def test_V(self):
        self.assertEqual(5, roman_to_arabic("V"))

    def test_VI(self):
        self.assertEqual(6, roman_to_arabic("VI"))

    def test_IV(self):
        self.assertEqual(4, roman_to_arabic("IV"))

    def test_X(self):
        self.assertEqual(10, roman_to_arabic("X"))

    def test_IX(self):
        self.assertEqual(9, roman_to_arabic("IX"))

    def test_XIV(self):
        self.assertEqual(14, roman_to_arabic("14"))
