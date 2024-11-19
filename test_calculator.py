import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_negative_number(self):
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(7, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()