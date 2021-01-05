# pylint: disable-all

import unittest
from ex1 import range_sum

class TestRangeSum(unittest.TestCase):
    def test_numbers_0_0(self):
        self.assertEqual(range_sum(5, 10), 45)

    def test_numbers_2_3(self):
        self.assertEqual(range_sum(2, 3), 5)

    def test_with_negative_numbers(self):
        self.assertEqual(range_sum(5, 1), 'incorrect range')
