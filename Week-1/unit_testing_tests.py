import unittest
from unit_testing_function import add_numbers

class TestFunction (unittest.TestCase):
# Test case for addition function

    def test_addition(self):
        # Test addition of two positive numbers
        result = add_numbers(3,5)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        # Test addition involving negative numbers
        result = add_numbers(-2,7)
        self.assertEqual(result, 5)

    def test_addition_float_numbers(self):
        # Test addition of floating point numbers
        result  = add_numbers(1.5, 2.5)
        self.assertAlmostEqual(result, 4.0, places = 2)

if __name__ == '__main__':
    unittest.main()