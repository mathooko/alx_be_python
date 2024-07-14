import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):

        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):

        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_division(self):
        
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(1, 1), 1)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.

# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b