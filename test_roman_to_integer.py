import unittest

from roman_to_integer import roman_to_integer


class TestRomanToInteger(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, roman_to_integer('I'))

    def test_2(self):
        self.assertEqual(2, roman_to_integer('II'))

    def test_5(self):
        self.assertEqual(5, roman_to_integer('V'))

    def test_6(self):
        self.assertEqual(6, roman_to_integer('VI'))

    def test_10(self):
        self.assertEqual(10, roman_to_integer('X'))

    def test_4(self):
        self.assertEqual(4, roman_to_integer('IV'))

    def test_9(self):
        self.assertEqual(9, roman_to_integer('IX'))

    def test_50(self):
        self.assertEqual(50, roman_to_integer('L'))

    def test_40(self):
        self.assertEqual(40, roman_to_integer('XL'))
