# pylint: disable-all

import unittest
from ex2 import today_weather

class TestTodayWeather(unittest.TestCase):
    def test_new_york(self):
        self.assertEqual(today_weather('new york'), 2459115)

    def test_london(self):
        self.assertEqual(today_weather('london'), 44418)

    def test_non_city(self):
        self.assertEqual(today_weather(''), 'City not found')


