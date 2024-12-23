import unittest

from roman_to_integer import roman_to_integer


class TestRomanToInteger(unittest.TestCase):
    def test_I(self):
        self.assertEqual(1, roman_to_integer('I'))

    def test_II(self):
        self.assertEqual(2, roman_to_integer('II'))

    def test_III(self):
        self.assertEqual(3, roman_to_integer('III'))

    def test_IV(self):
        self.assertEqual(4, roman_to_integer('IV'))

    def test_V(self):
        self.assertEqual(5, roman_to_integer('V'))

    def test_VI(self):
        self.assertEqual(6, roman_to_integer('VI'))

    def test_VII(self):
        self.assertEqual(7, roman_to_integer('VII'))

    def test_IX(self):
        self.assertEqual(9, roman_to_integer('IX'))

    def test_invalid(self):
        self.assertRaises(ValueError, roman_to_integer, 'invalid')

    def test_XIV(self):
        self.assertEqual(14, roman_to_integer('XIV'))

    def test_XVII(self):
        self.assertEqual(17, roman_to_integer('XVII'))

    def test_XIX(self):
        self.assertEqual(19, roman_to_integer('XIX'))

    def test_XL(self):
        self.assertEqual(40, roman_to_integer('XL'))

    def test_LXXXXVIII(self):
        self.assertEqual(88, roman_to_integer('LXXXVIII'))

    ## Failing test make it pass
    def test_Invalid_VIIII(self):
        self.assertRaises(ValueError, roman_to_integer, 'VIIII')