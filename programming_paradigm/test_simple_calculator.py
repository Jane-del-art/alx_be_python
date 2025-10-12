import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------------- Addition Tests ----------------
    def test_addition_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_sign_numbers(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(5, -3), 2)

    def test_addition_with_zero(self):
        """Test addition where one operand is zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # ---------------- Subtraction Tests ----------------
    def test_subtraction_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_sign_numbers(self):
        """Test subtraction of positive and negative numbers."""
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_with_zero(self):
        """Test subtraction where one operand is zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # ---------------- Multiplication Tests ----------------
    def test_multiplication_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_sign_numbers(self):
        """Test multiplication of positive and negative numbers."""
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_with_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # ---------------- Division Tests ----------------
    def test_division_positive_numbers(self):
        """Test division of two positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        """Test division of two negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_sign_numbers(self):
        """Test division of positive and negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_division_result_is_float(self):
        """Ensure division returns a float result."""
        self.assertIsInstance(self.calc.divide(3, 2), float)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_zero_numerator(self):
        """Test dividing zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0)

# Run all tests when this file is executed directly
if __name__ == '__main__':
    unittest.main()
