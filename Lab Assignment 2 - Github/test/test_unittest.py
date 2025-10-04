import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import temp_converter


class TestTempConverter(unittest.TestCase):

    def test_to_celsius(self):
        self.assertAlmostEqual(temp_converter.to_celsius(32), 0)
        self.assertAlmostEqual(temp_converter.to_celsius(212), 100)
        self.assertAlmostEqual(temp_converter.to_celsius(98.6), 37.0, places=1)
        with self.assertRaises(ValueError):
            temp_converter.to_celsius("abc")

    def test_to_fahrenheit(self):
        self.assertAlmostEqual(temp_converter.to_fahrenheit(0), 32)
        self.assertAlmostEqual(temp_converter.to_fahrenheit(100), 212)
        self.assertAlmostEqual(temp_converter.to_fahrenheit(37), 98.6, places=1)
        with self.assertRaises(ValueError):
            temp_converter.to_fahrenheit(None)

    def test_avg_temperature(self):
        self.assertEqual(temp_converter.avg_temperature([0, 10, 20]), 10)
        self.assertAlmostEqual(temp_converter.avg_temperature([32, 212]), 122.0)
        with self.assertRaises(ValueError):
            temp_converter.avg_temperature([30, "hot", 50])


if __name__ == '__main__':
    unittest.main()
