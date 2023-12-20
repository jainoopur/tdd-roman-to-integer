import unittest

from roman_to_integer import roman_to_integer


class TestRomanToInteger(unittest.TestCase):
    def test_I(self):
        self.assertEqual(1, roman_to_integer('I'))

    def test_II(self):
        self.assertEqual(2, roman_to_integer('II'))

    def test_III(self):
        self.assertEqual(3, roman_to_integer('III'))

    def test_V(self):
        self.assertEqual(5, roman_to_integer('V'))

    def test_VI(self):
        self.assertEqual(6, roman_to_integer('VI'))

    def test_VII(self):
        self.assertEqual(6, roman_to_integer('VI'))

    def test_IV(self):
        self.assertEqual(4, roman_to_integer('IV'))

    def test_VIII(self):
        self.assertEqual(8, roman_to_integer('VIII'))

    def test_IX(self):
        self.assertEqual(9, roman_to_integer('IX'))

    def test_X(self):
        self.assertEqual(10, roman_to_integer('X'))

    def test_XIV(self):
        self.assertEqual(14, roman_to_integer('XIV'))

    def test_XX(self):
        self.assertEqual(20, roman_to_integer('XX'))

    def test_39(self):
        self.assertEqual(39, roman_to_integer('XXXIX'))

    def test_18(self):
        self.assertEqual(18, roman_to_integer('XVIII'))





if __name__ == '__main__':
    unittest.main()
