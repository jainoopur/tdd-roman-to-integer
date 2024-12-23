import unittest

'''
1 -> 1
2 -> 2
3 -> 'Fizz'
4 -> 4
5 -> 'Buzz'
6 -> 'Fizz'
...
15 -> 'FizzBuzz'

more here - https://kata-log.rocks/fizz-buzz-kata
'''
class TestFizzBuzz(unittest.TestCase):
    ## Failing test make it pass
    def test_1(self):
        self.assertEqual(1, fizz_buzz(1))